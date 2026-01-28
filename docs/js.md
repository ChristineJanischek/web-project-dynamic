# JavaScript Grundlagen

JavaScript läuft im Browser und macht Seiten dynamisch.

## Variablen

Siehe auch: [JavaScript Grundlagen](../js.md) für weitere Informationen.

```js
let zahl = 5;
const name = "Lisa";
```

## Funktionen

```js
function add(a, b) {
  return a + b;
}
```

## DOM Zugriff

```js
const titel = document.querySelector("h1");
titel.textContent = "Neuer Titel";
```

## Event

```js
document.querySelector("button").addEventListener("click", () => {
  alert("Geklickt!");
});
```

Weiter: `react.md`.
