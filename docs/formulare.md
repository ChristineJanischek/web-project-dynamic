# Formulare erstellen & validieren

Formulare sind die Hauptmethode, um Daten von Nutzern zu sammeln - sei es ein Kontaktformular, Login, Umfrage oder Bestellung.

## Grundstruktur eines Formulars

```html
<form action="/submit" method="POST">
  <!-- Formularfelder hier -->
  <button type="submit">Absenden</button>
</form>
```

**Wichtige Attribute:**
- `action` = Wohin werden die Daten gesendet? (URL oder Skript)
- `method` = Wie werden sie gesendet?
  - `GET` = Daten in URL sichtbar (z.B. Suche)
  - `POST` = Daten versteckt (z.B. Login, Registrierung)

---

## Formularfelder

### Textfelder

```html
<!-- Einzeiliger Text -->
<label for="name">Name:</label>
<input type="text" id="name" name="name" required>

<!-- Mehrzeiliger Text -->
<label for="message">Nachricht:</label>
<textarea id="message" name="message" rows="5"></textarea>
```

### Email, Telefon, URL

```html
<label for="email">E-Mail:</label>
<input type="email" id="email" name="email" required>

<label for="phone">Telefon:</label>
<input type="tel" id="phone" name="phone">

<label for="website">Webseite:</label>
<input type="url" id="website" name="website">
```

**Browser validiert automatisch** das Format!

### Passwort

```html
<label for="password">Passwort:</label>
<input type="password" id="password" name="password" required minlength="8">
```

### Zahlen & Datum

```html
<!-- Zahl -->
<label for="age">Alter:</label>
<input type="number" id="age" name="age" min="18" max="100">

<!-- Datum -->
<label for="date">Datum:</label>
<input type="date" id="date" name="date">

<!-- Uhrzeit -->
<label for="time">Uhrzeit:</label>
<input type="time" id="time" name="time">
```

### Checkboxen

```html
<label>
  <input type="checkbox" name="newsletter" value="yes">
  Ich möchte den Newsletter erhalten
</label>

<!-- Mehrere Optionen -->
<fieldset>
  <legend>Interessen:</legend>
  <label><input type="checkbox" name="interest" value="sport"> Sport</label>
  <label><input type="checkbox" name="interest" value="musik"> Musik</label>
  <label><input type="checkbox" name="interest" value="reisen"> Reisen</label>
</fieldset>
```

### Radio Buttons

Nur **eine** Auswahl möglich (gleiches `name` Attribut):

```html
<fieldset>
  <legend>Geschlecht:</legend>
  <label><input type="radio" name="gender" value="m" required> Männlich</label>
  <label><input type="radio" name="gender" value="w"> Weiblich</label>
  <label><input type="radio" name="gender" value="d"> Divers</label>
</fieldset>
```

### Dropdown (Select)

```html
<label for="country">Land:</label>
<select id="country" name="country">
  <option value="">Bitte wählen...</option>
  <option value="de">Deutschland</option>
  <option value="at">Österreich</option>
  <option value="ch">Schweiz</option>
</select>

<!-- Mehrfachauswahl -->
<select name="hobbies" multiple size="4">
  <option value="sport">Sport</option>
  <option value="lesen">Lesen</option>
  <option value="kochen">Kochen</option>
  <option value="reisen">Reisen</option>
</select>
```

### Datei-Upload

```html
<form enctype="multipart/form-data">
  <label for="file">Datei hochladen:</label>
  <input type="file" id="file" name="file" accept="image/*">
</form>
```

**Wichtig:** `enctype="multipart/form-data"` für File-Uploads!

---

## HTML5 Validierung

### Required (Pflichtfeld)

```html
<input type="text" name="name" required>
```

### Pattern (Regex)

```html
<!-- Nur Buchstaben -->
<input type="text" pattern="[A-Za-z]+" title="Nur Buchstaben erlaubt">

<!-- Deutsche Postleitzahl -->
<input type="text" pattern="[0-9]{5}" title="5 Ziffern">

<!-- Telefon -->
<input type="tel" pattern="[0-9\-\+\s]+" title="Nur Zahlen, +, - und Leerzeichen">
```

### Min, Max, Minlength, Maxlength

```html
<input type="number" min="1" max="100">
<input type="text" minlength="3" maxlength="50">
<textarea maxlength="500"></textarea>
```

### Placeholder

```html
<input type="text" placeholder="Max Mustermann">
<input type="email" placeholder="max@example.com">
```

---

## Vollständiges Kontaktformular

### HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kontaktformular</title>
  <link rel="stylesheet" href="form.css">
</head>
<body>
  <div class="container">
    <h1>Kontaktieren Sie uns</h1>
    
    <form id="contactForm" action="/submit" method="POST">
      <!-- Name -->
      <div class="form-group">
        <label for="name">Name *</label>
        <input 
          type="text" 
          id="name" 
          name="name" 
          required 
          minlength="2"
          placeholder="Ihr vollständiger Name">
      </div>
      
      <!-- Email -->
      <div class="form-group">
        <label for="email">E-Mail *</label>
        <input 
          type="email" 
          id="email" 
          name="email" 
          required
          placeholder="ihre@email.de">
      </div>
      
      <!-- Telefon -->
      <div class="form-group">
        <label for="phone">Telefon</label>
        <input 
          type="tel" 
          id="phone" 
          name="phone"
          placeholder="+49 123 456789">
      </div>
      
      <!-- Betreff -->
      <div class="form-group">
        <label for="subject">Betreff *</label>
        <select id="subject" name="subject" required>
          <option value="">Bitte wählen...</option>
          <option value="anfrage">Allgemeine Anfrage</option>
          <option value="support">Support</option>
          <option value="feedback">Feedback</option>
          <option value="sonstiges">Sonstiges</option>
        </select>
      </div>
      
      <!-- Nachricht -->
      <div class="form-group">
        <label for="message">Nachricht *</label>
        <textarea 
          id="message" 
          name="message" 
          rows="6" 
          required
          minlength="10"
          placeholder="Ihre Nachricht an uns..."></textarea>
      </div>
      
      <!-- Newsletter -->
      <div class="form-group checkbox">
        <label>
          <input type="checkbox" name="newsletter" value="yes">
          Ich möchte den Newsletter erhalten
        </label>
      </div>
      
      <!-- Datenschutz -->
      <div class="form-group checkbox">
        <label>
          <input type="checkbox" name="privacy" required>
          Ich habe die <a href="/datenschutz">Datenschutzerklärung</a> gelesen *
        </label>
      </div>
      
      <!-- Buttons -->
      <div class="form-actions">
        <button type="reset" class="btn-secondary">Zurücksetzen</button>
        <button type="submit" class="btn-primary">Absenden</button>
      </div>
    </form>
  </div>
  
  <script src="form.js"></script>
</body>
</html>
```

### CSS (`form.css`)

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
  padding: 40px;
  max-width: 600px;
  width: 100%;
}

h1 {
  margin-bottom: 30px;
  color: #333;
  text-align: center;
}

/* Form Groups */
.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}

/* Input Felder */
input[type="text"],
input[type="email"],
input[type="tel"],
input[type="url"],
input[type="number"],
input[type="date"],
input[type="time"],
select,
textarea {
  width: 100%;
  padding: 12px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  font-family: inherit;
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* Placeholder */
::placeholder {
  color: #aaa;
}

/* Textarea */
textarea {
  resize: vertical;
  min-height: 100px;
}

/* Checkboxen */
.checkbox label {
  display: flex;
  align-items: center;
  font-weight: normal;
}

.checkbox input[type="checkbox"] {
  width: auto;
  margin-right: 10px;
}

/* Buttons */
.form-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

button {
  flex: 1;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: #e0e0e0;
  color: #555;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

/* Validierung */
input:invalid,
select:invalid,
textarea:invalid {
  border-color: #e74c3c;
}

input:valid,
select:valid,
textarea:valid {
  border-color: #2ecc71;
}

/* Fehlermeldungen */
.error {
  color: #e74c3c;
  font-size: 14px;
  margin-top: 5px;
}

/* Erfolgsmeldung */
.success {
  background: #d4edda;
  border: 1px solid #c3e6cb;
  color: #155724;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
  text-align: center;
}

/* Responsive */
@media (max-width: 600px) {
  .container {
    padding: 20px;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  button {
    width: 100%;
  }
}
```

### JavaScript Validierung (`form.js`)

```javascript
const form = document.getElementById('contactForm');

form.addEventListener('submit', function(e) {
  e.preventDefault();  // Verhindert normales Absenden
  
  // Formulardaten sammeln
  const formData = new FormData(form);
  const data = Object.fromEntries(formData);
  
  console.log('Formulardaten:', data);
  
  // Validierung
  if (validateForm(data)) {
    // Daten senden (hier simuliert)
    submitForm(data);
  }
});

function validateForm(data) {
  let isValid = true;
  
  // Name prüfen
  if (data.name.trim().length < 2) {
    showError('name', 'Name muss mindestens 2 Zeichen haben');
    isValid = false;
  } else {
    clearError('name');
  }
  
  // Email prüfen
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(data.email)) {
    showError('email', 'Bitte gültige E-Mail eingeben');
    isValid = false;
  } else {
    clearError('email');
  }
  
  // Nachricht prüfen
  if (data.message.trim().length < 10) {
    showError('message', 'Nachricht muss mindestens 10 Zeichen haben');
    isValid = false;
  } else {
    clearError('message');
  }
  
  // Datenschutz prüfen
  if (!data.privacy) {
    alert('Bitte akzeptieren Sie die Datenschutzerklärung');
    isValid = false;
  }
  
  return isValid;
}

function showError(fieldId, message) {
  const field = document.getElementById(fieldId);
  const formGroup = field.closest('.form-group');
  
  // Entferne alte Fehlermeldung
  clearError(fieldId);
  
  // Neue Fehlermeldung erstellen
  const errorDiv = document.createElement('div');
  errorDiv.className = 'error';
  errorDiv.textContent = message;
  formGroup.appendChild(errorDiv);
  
  field.style.borderColor = '#e74c3c';
}

function clearError(fieldId) {
  const field = document.getElementById(fieldId);
  const formGroup = field.closest('.form-group');
  const existingError = formGroup.querySelector('.error');
  
  if (existingError) {
    existingError.remove();
  }
  
  field.style.borderColor = '#e0e0e0';
}

function submitForm(data) {
  // Hier würdest du normalerweise AJAX/Fetch verwenden
  // um Daten an Server zu senden
  
  // Simulation: Erfolgsmeldung anzeigen
  const container = document.querySelector('.container');
  
  const successMsg = document.createElement('div');
  successMsg.className = 'success';
  successMsg.textContent = 'Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet.';
  
  container.insertBefore(successMsg, form);
  
  // Formular zurücksetzen
  form.reset();
  
  // Nach 5 Sekunden Erfolgsmeldung entfernen
  setTimeout(() => {
    successMsg.remove();
  }, 5000);
}
```

---

## AJAX Formular-Übermittlung

Moderne Methode ohne Seitenneuladung:

```javascript
form.addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const formData = new FormData(form);
  
  try {
    const response = await fetch('/submit', {
      method: 'POST',
      body: formData
    });
    
    if (response.ok) {
      const result = await response.json();
      alert('Erfolgreich gesendet!');
      form.reset();
    } else {
      alert('Fehler beim Senden!');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Netzwerkfehler!');
  }
});
```

---

## Best Practices

✅ **Labels für alle Felder** - Barrierefreiheit!  
✅ **Required für Pflichtfelder** - HTML5 Validierung  
✅ **Placeholder als Hilfestellung** - Nicht als Ersatz für Label!  
✅ **Klare Fehlermeldungen** - Was ist falsch?  
✅ **Erfolgsmeldung zeigen** - Feedback geben  
✅ **Responsive Design** - Mobile-freundlich  
✅ **Datenschutz-Checkbox** - DSGVO-konform  
✅ **Submit-Button deaktivieren** während Senden  

---

## Häufige Fehler

❌ **Fehlende Labels**
```html
<input type="text" name="name">  <!-- Schlecht! -->
```

✅ **Richtig:**
```html
<label for="name">Name:</label>
<input type="text" id="name" name="name">
```

❌ **Placeholder statt Label**
```html
<input type="text" placeholder="Name">  <!-- Schlecht! -->
```

✅ **Beides nutzen:**
```html
<label for="name">Name:</label>
<input type="text" id="name" placeholder="Max Mustermann">
```

❌ **Keine Validierung**
```html
<input type="text" name="email">  <!-- Jede Eingabe erlaubt! -->
```

✅ **Richtiger Typ:**
```html
<input type="email" name="email" required>
```

---

## Server-seitige Verarbeitung

### PHP Beispiel

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars($_POST['message']);
    
    if ($name && $email && $message) {
        // Email senden oder in Datenbank speichern
        mail('kontakt@example.com', 'Kontaktformular', $message);
        echo 'Erfolgreich gesendet!';
    } else {
        echo 'Ungültige Daten!';
    }
}
?>
```

Mehr dazu in `php.md`!

### Python (Flask) Beispiel

```python
from flask import Flask, request, jsonify

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if name and email and message:
        # Daten speichern oder Email senden
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 400
```

Mehr dazu in `python.md`!

---

## Barrierefreiheit (A11y)

```html
<!-- ARIA Labels -->
<label for="name" id="name-label">Name *</label>
<input 
  type="text" 
  id="name" 
  name="name" 
  required 
  aria-labelledby="name-label"
  aria-required="true"
  aria-invalid="false">

<!-- Fehlermeldungen -->
<div id="name-error" role="alert" class="error">
  Bitte Namen eingeben
</div>
```

---

## Nächste Schritte

- **JavaScript** → `js.md` - Erweiterte Formular-Interaktionen
- **PHP** → `php.md` - Server-seitige Verarbeitung
- **Python** → `python.md` - Backend mit Flask
- **Datenbank** → `datenbank.md` - Daten speichern

---

## Ressourcen

- [MDN: Web Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms)
- [HTML5 Input Types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
- [Form Validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Barrierefreiheit
