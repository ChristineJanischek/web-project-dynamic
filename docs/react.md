# React Einstieg

React baut Oberflächen aus Komponenten.

Mini-Komponente:
```jsx
function Begruessung({ name }) {
  return <h2>Hallo {name}</h2>;
}
```
State mit Hook:
```jsx
import { useState } from "react";
function Counter(){
  const [c,setC] = useState(0);
  return <button onClick={()=>setC(c+1)}>Zähler: {c}</button>;
}
```
Weiter: `python.md`.
