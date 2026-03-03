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

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List


class ArchitectureChecker:
    def __init__(
        self,
        base_path: str = ".",
        check_paths: List[str] | None = None,
        output_dir: str = "reports",
    ):
        self.base_path = Path(base_path)
        self.output_dir = self.base_path / output_dir
        self.issues: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []
        self.good_practices: List[str] = []

        default_paths = [
            "version1",
            "version2",
            "version3",
            "version4",
            "version5",
            "templates",
            "shared-examples",
            "src",
        ]
        self.check_paths = check_paths if check_paths else default_paths

    def relative_path(self, file_path: Path) -> str:
        """Gibt einen lesbaren relativen Pfad zurück."""
        return str(file_path.relative_to(self.base_path))

    @staticmethod
    def deduplicate(items: List[str]) -> List[str]:
        """Entfernt Duplikate, behält Reihenfolge."""
        return list(dict.fromkeys(items))

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
            if not file_path.is_file():
                continue

            suffix = file_path.suffix.lower()
            if suffix == ".html":
                self.check_html_file(file_path)
            elif suffix == ".css":
                self.check_css_file(file_path)
            elif suffix == ".js":
                self.check_js_file(file_path)

    # ========== 1. ABSTRAKTION ==========

    def check_html_file(self, file_path: Path):
        """Prüft HTML auf Abstraktion und Struktur"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            semantic_tags = ["<header", "<nav", "<main", "<section", "<article", "<aside", "<footer"]
            has_semantic = any(tag in content for tag in semantic_tags)
            location = self.relative_path(file_path)

            if has_semantic:
                self.good_practices.append(
                    f"✅ {location}: Nutzt semantische HTML-Tags (Abstraktion)"
                )
            elif len(content) > 500:
                self.suggestions.append(
                    f"💡 {location}: Erwäge semantische Tags wie <header>, <main>, <footer> statt nur <div> (Prinzip: Abstraktion)"
                )

            inline_styles = re.findall(r'style="[^"]*"', content)
            if len(inline_styles) > 3:
                self.warnings.append(
                    f"⚠️ {location}: {len(inline_styles)} inline-Styles gefunden. Besser: CSS-Klassen verwenden (Prinzip: Abstraktion, Wiederverwendbarkeit)"
                )

            inline_js = re.findall(r'onclick="[^"]*"', content, re.IGNORECASE)
            if inline_js:
                self.suggestions.append(
                    f"💡 {location}: {len(inline_js)}x onclick im HTML. Besser: Event-Listener in separater JS-Datei (Prinzip: MVC, Wartbarkeit)"
                )

        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")

    # ========== 2. WIEDERVERWENDBARKEIT ==========

    def check_css_file(self, file_path: Path):
        """Prüft CSS auf Wiederverwendbarkeit"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            location = self.relative_path(file_path)
            has_variables = ":root" in content and "--" in content
            if has_variables:
                var_count = len(re.findall(r"--[\w-]+:", content))
                self.good_practices.append(
                    f"✅ {location}: Nutzt {var_count} CSS-Variablen (Wiederverwendbarkeit, Erweiterbarkeit)"
                )
            elif len(content) > 1000:
                self.suggestions.append(
                    f"💡 {location}: Erwäge CSS-Variablen für Farben/Abstände (Prinzip: Wiederverwendbarkeit, Erweiterbarkeit)"
                )

            color_definitions = re.findall(r"color:\s*#[0-9a-fA-F]{3,6}", content)
            if len(color_definitions) > len(set(color_definitions)) * 1.5:
                self.suggestions.append(
                    f"💡 {location}: Viele gleiche Farbwerte. Erwäge CSS-Variablen (Prinzip: Wiederverwendbarkeit)"
                )

            important_count = content.count("!important")
            if important_count > 2:
                self.warnings.append(
                    f"⚠️ {location}: {important_count}x !important gefunden. Deutet auf Spezifitäts-Probleme hin (Prinzip: Wartbarkeit)"
                )

        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")

    # ========== 3. ZERLEGUNG & 7. MVC ==========

    def check_js_file(self, file_path: Path):
        """Prüft JavaScript auf Zerlegung und Struktur"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            location = self.relative_path(file_path)
            function_declarations = len(re.findall(r"function\s+\w+\s*\(", content))
            arrow_functions = len(
                re.findall(r"(?:const|let|var)\s+\w+\s*=\s*\([^)]*\)\s*=>", content)
            )
            class_definitions = len(re.findall(r"class\s+\w+", content))

            total_functions = function_declarations + arrow_functions
            if total_functions > 3:
                self.good_practices.append(
                    f"✅ {location}: {total_functions} Funktionen gefunden - gute Zerlegung!"
                )

            if class_definitions > 0:
                self.good_practices.append(
                    f"✅ {location}: Nutzt {class_definitions} Klassen (Abstraktion, MVC)"
                )

            functions = re.split(r"\n(?=function\s|\w+\s*:\s*function)", content)
            for func in functions:
                lines = func.split("\n")
                if len(lines) > 50:
                    self.suggestions.append(
                        f"💡 {location}: Funktion mit {len(lines)} Zeilen gefunden. Erwäge Aufteilung (Prinzip: Zerlegung)"
                    )
                    break

            console_logs = len(re.findall(r"console\.log", content))
            if console_logs > 5:
                self.suggestions.append(
                    f"💡 {location}: {console_logs}x console.log gefunden. Vor Produktion entfernen oder Logger nutzen (Prinzip: Wartbarkeit)"
                )

            comments = len(re.findall(r"//.*|/\*[\s\S]*?\*/", content))
            if comments > 3:
                self.good_practices.append(
                    f"✅ {location}: {comments} Kommentare gefunden (Wartbarkeit)"
                )

        except Exception as e:
            print(f"⚠️ Fehler beim Lesen von {file_path}: {e}")

    # ========== 5. SICHERHEIT ==========

    def check_security(self):
        """Prüft auf Sicherheitsprobleme"""
        print("\n🔒 Prüfe Sicherheit...")

        sensitive_patterns = [
            (r"password\s*[=:]\s*[\"\'][^\"\']+[\"\']", "Passwort"),
            (r"api[_-]?key\s*[=:]\s*[\"\'][^\"\']+[\"\']", "API-Key"),
            (r"secret\s*[=:]\s*[\"\'][^\"\']+[\"\']", "Secret"),
        ]
        scan_suffixes = {".js", ".ts", ".php", ".py", ".env"}

        for path in self.check_paths:
            full_path = self.base_path / path
            if not full_path.exists():
                continue

            for file_path in full_path.rglob("*"):
                if not file_path.is_file() or file_path.suffix.lower() not in scan_suffixes:
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    location = self.relative_path(file_path)
                    for pattern, name in sensitive_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            self.issues.append(
                                f"❌ {location}: Mögliches {name} im Code gefunden! (Prinzip: Sicherheit)"
                            )

                    if file_path.suffix.lower() in {".js", ".ts"} and "innerHTML" in content:
                        self.warnings.append(
                            f"⚠️ {location}: innerHTML verwendet. Prüfe auf XSS-Risiken - nutze textContent für Benutzereingaben (Prinzip: Sicherheit)"
                        )
                except Exception:
                    continue

    # ========== 4. ERWEITERBARKEIT ==========

    def check_extensibility(self):
        """Prüft auf Erweiterbarkeit"""
        print("\n🚀 Prüfe Erweiterbarkeit...")

        config_files = [".editorconfig", ".prettierrc", ".eslintrc.json", "package.json"]
        for config in config_files:
            if (self.base_path / config).exists():
                self.good_practices.append(f"✅ {config} vorhanden (Erweiterbarkeit, Wartbarkeit)")

    # ========== 6. WARTBARKEIT ==========

    def check_maintainability(self):
        """Prüft auf Wartbarkeit"""
        print("\n🔧 Prüfe Wartbarkeit...")

        for path in self.check_paths:
            full_path = self.base_path / path
            if not full_path.exists():
                continue

            readme_files = list(full_path.rglob("README.md"))
            if readme_files:
                self.good_practices.append(
                    f"✅ {path}/: Hat {len(readme_files)} README.md Datei(en) (Wartbarkeit)"
                )

            has_css_folder = (full_path / "css").exists() or (full_path / "aufgabe" / "css").exists()
            has_js_folder = (full_path / "js").exists() or (full_path / "aufgabe" / "js").exists()
            if has_css_folder and has_js_folder:
                self.good_practices.append(
                    f"✅ {path}/: Saubere Ordnerstruktur (css/, js/) (Wartbarkeit, MVC)"
                )

    # ========== REPORT ==========

    def generate_report(self) -> Dict:
        """Generiert den Abschlussbericht"""

        self.check_security()
        self.check_extensibility()
        self.check_maintainability()

        self.issues = self.deduplicate(self.issues)
        self.warnings = self.deduplicate(self.warnings)
        self.suggestions = self.deduplicate(self.suggestions)
        self.good_practices = self.deduplicate(self.good_practices)

        total_checks = (
            len(self.issues)
            + len(self.warnings)
            + len(self.suggestions)
            + len(self.good_practices)
        )

        report = {
            "total_checks": total_checks,
            "issues": len(self.issues),
            "warnings": len(self.warnings),
            "suggestions": len(self.suggestions),
            "good_practices": len(self.good_practices),
            "details": {
                "issues": self.issues,
                "warnings": self.warnings,
                "suggestions": self.suggestions,
                "good_practices": self.good_practices,
            },
        }

        self.create_markdown_report(report)

        self.output_dir.mkdir(parents=True, exist_ok=True)
        details_path = self.output_dir / "architecture_details.json"
        with open(details_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        return report

    def create_markdown_report(self, report: Dict):
        """Erstellt einen Markdown-Bericht"""

        lines: List[str] = []
        lines.append("# 🏛️ Architektur-Prinzipien Prüfbericht\n")
        lines.append(f"**Datum:** {self.get_current_date()}\n")
        lines.append(f"**Geprüfte Pfade:** {', '.join(self.check_paths)}\n")
        lines.append("\n---\n")

        lines.append("## 📊 Zusammenfassung\n")
        lines.append(f"- ✅ **Gute Praktiken gefunden:** {report['good_practices']}")
        lines.append(f"- 💡 **Verbesserungsvorschläge:** {report['suggestions']}")
        lines.append(f"- ⚠️ **Warnungen:** {report['warnings']}")
        lines.append(f"- ❌ **Kritische Probleme:** {report['issues']}\n")

        if report["issues"] == 0:
            if report["warnings"] == 0:
                lines.append("### 🎉 Bewertung: **AUSGEZEICHNET**\n")
                lines.append("Alle Architektur-Prinzipien werden vorbildlich eingehalten!\n")
            else:
                lines.append("### ✅ Bewertung: **GUT**\n")
                lines.append("Solide Architektur mit einigen Verbesserungsmöglichkeiten.\n")
        else:
            lines.append("### ⚠️ Bewertung: **VERBESSERUNGSWÜRDIG**\n")
            lines.append("Einige wichtige Architektur-Prinzipien sollten beachtet werden.\n")

        lines.append("\n---\n")

        if self.good_practices:
            lines.append("## ✅ Gute Praktiken\n")
            for practice in self.good_practices[:10]:
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
        lines.append(
            "📖 **Mehr erfahren:** [Architektur-Prinzipien Dokumentation](docs/handbook/architektur-prinzipien.md)\n"
        )

        self.output_dir.mkdir(parents=True, exist_ok=True)
        report_path = self.output_dir / "architecture_report.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print("\n" + "=" * 60)
        print("\n".join(lines))
        print("=" * 60)

    @staticmethod
    def get_current_date():
        from datetime import datetime

        return datetime.now().strftime("%d.%m.%Y %H:%M")


def main():
    """Hauptfunktion"""
    parser = argparse.ArgumentParser(description="Architektur-Prinzipien Checker")
    parser.add_argument(
        "--paths",
        nargs="+",
        help="Optionale Liste von Pfaden, die geprüft werden sollen (relativ zum Repo-Root)",
    )
    parser.add_argument(
        "--output-dir",
        default="reports",
        help="Ausgabeverzeichnis für Bericht und JSON-Details (Standard: reports)",
    )
    args = parser.parse_args()

    checker = ArchitectureChecker(check_paths=args.paths, output_dir=args.output_dir)
    report = checker.check_all()

    if report["issues"] > 0:
        print("\n⚠️ Hinweis: Kritische Architektur-Probleme gefunden.")
        print("Dies blockiert nicht den Build, sollte aber behoben werden!")

    print("\n✅ Architektur-Prüfung abgeschlossen!")
    print(f"📄 Bericht: {checker.output_dir / 'architecture_report.md'}")

    return 0


if __name__ == "__main__":
    exit(main())
