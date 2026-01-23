# Algorithmen & Datenstrukturen

## Datenstrukturen
- Array / Liste: Folge von Elementen.
- Map / Objekt: Schlüssel-Werte.
- Stack: LIFO (zuletzt rein – zuerst raus).
- Queue: FIFO (zuerst rein – zuerst raus).

## Beispiel Sortieren (Bubble Sort JS)
```js
function bubbleSort(arr){
  for(let i=0;i<arr.length;i++){
    for(let j=0;j<arr.length-1;j++){
      if(arr[j] > arr[j+1]){
        [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
      }
    }
  }
  return arr;
}
```
## Suchen (Lineare Suche Python)
```python
def linear_search(items, target):
    for i, val in enumerate(items):
        if val == target:
            return i
    return -1
```
Weiter: `testen.md`.
