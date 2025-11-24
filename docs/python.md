# Python (Flask Backend)

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
