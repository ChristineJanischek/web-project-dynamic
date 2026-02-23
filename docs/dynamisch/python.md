# Python (Flask Backend)

Siehe auch: [PHP Grundlagen](php.md) für weitere Informationen.

Für den vollständigen Grundlagen-Lernpfad (Ausgaben, Variablen, Rechenoperationen, Funktionen/Methoden, Kontrollstrukturen, Datenstrukturen, Algorithmen, Dateien) siehe:

- [Programmier-Grundlagen Übersicht](../programmierung/grundlagen/README.md)
- [Python Fundamentals (modular)](../programmierung/grundlagen/python/README.md)

Flask ist ein leichtes Web-Framework.

Minimal:

```python
from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hallo von Flask"
```

Start später: `flask run` (Konfiguration folgt).
Weiter: `php.md`.
