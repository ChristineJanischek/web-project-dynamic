#!/usr/bin/env python3
"""
Architektur-Prinzipien Checker für Web-Projekte

Prüft auf:
1. Abstraktion - Funktionen/Klassen sind sinnvoll genutzt
2. Wiederverwendbarkeit - CSS-Klassen, JS-Funktionen
3. Zerlegung - Dateien sind modular strukturiert
4. Erweiterbarkeit - CSS-Variablen, konfigurierbare Parameter
5. Sicherheit - Keine Secrets, sichere Patterns
6. Wartbarkeit - Kommentare, konsistente Struktur
7. MVC - Trennung von HTML/CSS/JS
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class ArchitectureChecker:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.issues = []
        self.warnings = []
        self.suggestions = []
        self.good_practices = []
        
        # Pfade zum Prüfen
        self.check_paths = [
            "version1", "version2", "version3",
            "templates", "shared-examples"
        ]
    
    def check_all(self) -> Dict:
        """Führt alle Architektur-Checks durch"""
        print("🔍 Starte Architektur-Validierung...")
        
        for path in self.check_paths:
            full_path = self.base_path / path
            if full_path.exists():
                print(f"\n📁 Prüfe {path}...")
                self.check_directory(full_path)
        
        return self.generate_report()
    
    def check_directory(self, directory: Path):
        """Prüft ein Verzeichnis rekursiv"""
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                if file_path.suffix == ".html":
                    self.check_html_file(file_path)
                elif file_path.suffix == ".css":
                    self.check_css_file(file_path)
                elif file_path.suffix == ".js":
                    self.check_js_file(file_path)
    
    # ========== 1. ABSTRAKTION ==========
    
    def check_html_file(self, file_path: Path):
        """Prüft HTML auf Abstraktion und Struktur"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Semantische HTML-Tags (gute Abstraktion)
            semantic_tags = ['<header', '<nav', '<main', '<section', '<article', '<aside', '<footer']
            has_semantic = any(tag in content for tag in semantic_tags)
            
            if has_semantic:
                self.good_practices.append(
                    f"✅ {file_path.name}: Nutzt semantische HTML-Tags (Abstraktion)"
                )
            else:
                # Nur Warnung bei größeren Dateien
                if len(content) > 500:
                    self.suggestions.append(
                        f"💡 {file_path.name}: Erwäge semantische Tags wie <header>, <main>, <footer> statt nur <div> (Prinzip: Abstraktion)"
                    )
            
            # Inline-Styles (schlechte Abstraktion)
            inline_styles = re.findall(r'style="[^"]*"', content)
            if len(inline_styles) > 3:
                self.warnings.append(
                    f"⚠️ {file_path.name}: {len(inline_styles)} inline-Styles gefunden. Besser: CSS-Klassen verwenden (Prinzip: Abstraktion, Wiederverwendbarkeit)"
                )
            
            # MVC: Inline-JavaScript
            inline_js = re.findall(r'onclick="[^"]*"', content, re.IGNORECASE)
            if inline_js:
                self.suggestions.append(
                    f"💡 {file_path.name}: {len(inline_js)}x onclick im HTML. Besser: Event-Listener in separater JS-Datei (Prinzip: MVC, Wartbarkeit)"
                )
        
        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")
    
    # ========== 2. WIEDERVERWENDBARKEIT ==========
    
    def check_css_file(self, file_path: Path):
        """Prüft CSS auf Wiederverwendbarkeit"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # CSS-Variablen (gute Wiederverwendbarkeit & Erweiterbarkeit)
            has_variables = ':root' in content and '--' in content
            if has_variables:
                var_count = len(re.findall(r'--[\w-]+:', content))
                self.good_practices.append(
                    f"✅ {file_path.name}: Nutzt {var_count} CSS-Variablen (Wiederverwendbarkeit, Erweiterbarkeit)"
                )
            else:
                # Nur bei größeren CSS-Dateien vorschlagen
                if len(content) > 1000:
                    self.suggestions.append(
                        f"💡 {file_path.name}: Erwäge CSS-Variablen für Farben/Abstände (Prinzip: Wiederverwendbarkeit, Erweiterbarkeit)"
                    )
            
            # Duplizierte Styles erkennen
            color_definitions = re.findall(r'color:\s*#[0-9a-fA-F]{3,6}', content)
            if len(color_definitions) > len(set(color_definitions)) * 1.5:
                self.suggestions.append(
                    f"💡 {file_path.name}: Viele gleiche Farbwerte. Erwäge CSS-Variablen (Prinzip: Wiederverwendbarkeit)"
                )
            
            # !important (schlechte Wartbarkeit)
            important_count = content.count('!important')
            if important_count > 2:
                self.warnings.append(
                    f"⚠️ {file_path.name}: {important_count}x !important gefunden. Deutet auf Spezifitäts-Probleme hin (Prinzip: Wartbarkeit)"
                )
        
        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")
    
    # ========== 3. ZERLEGUNG & 7. MVC ==========
    
    def check_js_file(self, file_path: Path):
        """Prüft JavaScript auf Zerlegung und Struktur"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Funktionen zählen (Zerlegung)
            function_declarations = len(re.findall(r'function\s+\w+\s*\(', content))
            arrow_functions = len(re.findall(r'(?:const|let|var)\s+\w+\s*=\s*\([^)]*\)\s*=>', content))
            class_definitions = len(re.findall(r'class\s+\w+', content))
            
            total_functions = function_declarations + arrow_functions
            
            if total_functions > 3:
                self.good_practices.append(
                    f"✅ {file_path.name}: {total_functions} Funktionen gefunden - gute Zerlegung!"
                )
            
            if class_definitions > 0:
                self.good_practices.append(
                    f"✅ {file_path.name}: Nutzt {class_definitions} Klassen (Abstraktion, MVC)"
                )
            
            # Sehr lange Funktionen (schlechte Zerlegung)
            functions = re.split(r'\n(?=function\s|\w+\s*:\s*function)', content)
            for func in functions:
                lines = func.split('\n')
                if len(lines) > 50:
                    self.suggestions.append(
                        f"💡 {file_path.name}: Funktion mit {len(lines)} Zeilen gefunden. Erwäge Aufteilung (Prinzip: Zerlegung)"
                    )
                    break
            
            # Console.log in Produktion (Wartbarkeit)
            console_logs = len(re.findall(r'console\.log', content))
            if console_logs > 5:
                self.suggestions.append(
                    f"💡 {file_path.name}: {console_logs}x console.log gefunden. Vor Produktion entfernen oder Logger nutzen (Prinzip: Wartbarkeit)"
                )
            
            # Kommentare (Wartbarkeit)
            comments = len(re.findall(r'//.*|/\*[\s\S]*?\*/', content))
            if comments > 3:
                self.good_practices.append(
                    f"✅ {file_path.name}: {comments} Kommentare gefunden (Wartbarkeit)"
                )
        
        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")
    
    # ========== 5. SICHERHEIT ==========
    
    def check_security(self):
        """Prüft auf Sicherheitsprobleme"""
        print("\n🔒 Prüfe Sicherheit...")
        
        # Secrets in Dateien
        sensitive_patterns = [
            (r'password\s*[=:]\s*["\'][^"\']+["\']', 'Passwort'),
            (r'api[_-]?key\s*[=:]\s*["\'][^"\']+["\']', 'API-Key'),
            (r'secret\s*[=:]\s*["\'][^"\']+["\']', 'Secret'),
        ]
        
        for path in self.check_paths:
            full_path = self.base_path / path
            if not full_path.exists():
                continue
                
            for file_path in full_path.rglob("*.js"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    for pattern, name in sensitive_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            self.issues.append(
                                f"❌ {file_path.name}: Mögliches {name} im Code gefunden! (Prinzip: Sicherheit)"
                            )
                    
                    # innerHTML mit Benutzereingaben (XSS-Risiko)
                    if 'innerHTML' in content:
                        self.warnings.append(
                            f"⚠️ {file_path.name}: innerHTML verwendet. Prüfe auf XSS-Risiken - nutze textContent für Benutzereingaben (Prinzip: Sicherheit)"
                        )
                
                except Exception as e:
                    pass
    
    # ========== 4. ERWEITERBARKEIT ==========
    
    def check_extensibility(self):
        """Prüft auf Erweiterbarkeit"""
        print("\n🚀 Prüfe Erweiterbarkeit...")
        
        # Prüfe ob Konfigurationsdateien existieren
        config_files = [
            '.editorconfig',
            '.prettierrc',
            '.eslintrc.json',
            'package.json'
        ]
        
        for config in config_files:
            if (self.base_path / config).exists():
                self.good_practices.append(
                    f"✅ {config} vorhanden (Erweiterbarkeit, Wartbarkeit)"
                )
    
    # ========== 6. WARTBARKEIT ==========
    
    def check_maintainability(self):
        """Prüft auf Wartbarkeit"""
        print("\n🔧 Prüfe Wartbarkeit...")
        
        for path in self.check_paths:
            full_path = self.base_path / path
            if not full_path.exists():
                continue
            
            # Prüfe README-Existenz
            readme_files = list(full_path.rglob("README.md"))
            if readme_files:
                self.good_practices.append(
                    f"✅ {path}/: Hat {len(readme_files)} README.md Datei(en) (Wartbarkeit)"
                )
            
            # Prüfe Ordnerstruktur
            has_css_folder = (full_path / "css").exists() or (full_path / "aufgabe" / "css").exists()
            has_js_folder = (full_path / "js").exists() or (full_path / "aufgabe" / "js").exists()
            
            if has_css_folder and has_js_folder:
                self.good_practices.append(
                    f"✅ {path}/: Saubere Ordnerstruktur (css/, js/) (Wartbarkeit, MVC)"
                )
    
    # ========== REPORT ==========
    
    def generate_report(self) -> Dict:
        """Generiert den Abschlussbericht"""
        
        # Zusätzliche Checks
        self.check_security()
        self.check_extensibility()
        self.check_maintainability()
        
        # Statistiken
        total_checks = len(self.issues) + len(self.warnings) + len(self.suggestions) + len(self.good_practices)
        
        report = {
            'total_checks': total_checks,
            'issues': len(self.issues),
            'warnings': len(self.warnings),
            'suggestions': len(self.suggestions),
            'good_practices': len(self.good_practices),
            'details': {
                'issues': self.issues,
                'warnings': self.warnings,
                'suggestions': self.suggestions,
                'good_practices': self.good_practices
            }
        }
        
        # Markdown-Report erstellen
        self.create_markdown_report(report)
        
        # JSON für weitere Verarbeitung
        with open('architecture_details.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report
    
    def create_markdown_report(self, report: Dict):
        """Erstellt einen Markdown-Bericht"""
        
        lines = []
        lines.append("# 🏛️ Architektur-Prinzipien Prüfbericht\n")
        lines.append(f"**Datum:** {self.get_current_date()}\n")
        lines.append(f"**Geprüfte Pfade:** {', '.join(self.check_paths)}\n")
        lines.append("\n---\n")
        
        # Zusammenfassung
        lines.append("## 📊 Zusammenfassung\n")
        lines.append(f"- ✅ **Gute Praktiken gefunden:** {report['good_practices']}")
        lines.append(f"- 💡 **Verbesserungsvorschläge:** {report['suggestions']}")
        lines.append(f"- ⚠️ **Warnungen:** {report['warnings']}")
        lines.append(f"- ❌ **Kritische Probleme:** {report['issues']}\n")
        
        # Bewertung
        if report['issues'] == 0:
            if report['warnings'] == 0:
                lines.append("### 🎉 Bewertung: **AUSGEZEICHNET**\n")
                lines.append("Alle Architektur-Prinzipien werden vorbildlich eingehalten!\n")
            else:
                lines.append("### ✅ Bewertung: **GUT**\n")
                lines.append("Solide Architektur mit einigen Verbesserungsmöglichkeiten.\n")
        else:
            lines.append("### ⚠️ Bewertung: **VERBESSERUNGSWÜRDIG**\n")
            lines.append("Einige wichtige Architektur-Prinzipien sollten beachtet werden.\n")
        
        lines.append("\n---\n")
        
        # Details
        if self.good_practices:
            lines.append("## ✅ Gute Praktiken\n")
            for practice in self.good_practices[:10]:  # Top 10
                lines.append(f"{practice}\n")
            if len(self.good_practices) > 10:
                lines.append(f"\n*...und {len(self.good_practices) - 10} weitere gute Praktiken!*\n")
            lines.append("\n")
        
        if self.suggestions:
            lines.append("## 💡 Verbesserungsvorschläge\n")
            for suggestion in self.suggestions:
                lines.append(f"{suggestion}\n")
            lines.append("\n")
        
        if self.warnings:
            lines.append("## ⚠️ Warnungen\n")
            for warning in self.warnings:
                lines.append(f"{warning}\n")
            lines.append("\n")
        
        if self.issues:
            lines.append("## ❌ Kritische Probleme\n")
            for issue in self.issues:
                lines.append(f"{issue}\n")
            lines.append("\n")
        
        # Prinzipien-Mapping
        lines.append("\n---\n")
        lines.append("## 📚 Architektur-Prinzipien\n")
        lines.append("\n")
        lines.append("Die Prüfung basiert auf diesen Prinzipien:\n")
        lines.append("\n")
        lines.append("1. **🧩 Abstraktion** - Komplexität hinter einfachen Schnittstellen verstecken\n")
        lines.append("2. **♻️ Wiederverwendbarkeit** - Code einmal schreiben, mehrfach nutzen\n")
        lines.append("3. **🔨 Zerlegung** - Große Probleme in kleine Module aufteilen\n")
        lines.append("4. **🚀 Erweiterbarkeit** - Neue Features leicht hinzufügen können\n")
        lines.append("5. **🔒 Sicherheit** - Anwendung vor Angriffen schützen\n")
        lines.append("6. **🔧 Wartbarkeit** - Code auch nach Monaten verstehen können\n")
        lines.append("7. **🏛️ MVC** - Daten, Darstellung und Logik trennen\n")
        lines.append("\n")
        lines.append("📖 **Mehr erfahren:** [Architektur-Prinzipien Dokumentation](docs/architektur-prinzipien.md)\n")
        
        # Schreibe Report
        with open('architecture_report.md', 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print("\n" + "="*60)
        print('\n'.join(lines))
        print("="*60)
    
    @staticmethod
    def get_current_date():
        from datetime import datetime
        return datetime.now().strftime("%d.%m.%Y %H:%M")


def main():
    """Hauptfunktion"""
    checker = ArchitectureChecker()
    report = checker.check_all()
    
    # Exit-Code basierend auf kritischen Problemen
    # Wir geben KEINEN Fehler zurück, nur Hinweise!
    if report['issues'] > 0:
        print("\n⚠️ Hinweis: Kritische Architektur-Probleme gefunden.")
        print("Dies blockiert nicht den Build, sollte aber behoben werden!")
    
    print("\n✅ Architektur-Prüfung abgeschlossen!")
    print(f"📄 Bericht: architecture_report.md")
    
    # Immer Success, da dies ein pädagogisches Tool ist
    return 0


if __name__ == "__main__":
    exit(main())
