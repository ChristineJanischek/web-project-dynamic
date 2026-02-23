# Testen

Tests prüfen ob Code wie erwartet funktioniert.

## Arten

Siehe auch: [JavaScript Grundlagen](js.md) für Testmethoden.

- Unit-Test: Einzelne Funktion.
- Integrationstest: Zusammenspiel mehrerer Teile.

## Beispiel (JavaScript Jest)

```js
test("add", () => {
  expect(1 + 2).toBe(3);
});
```

## Beispiel (Python Pytest)

```python
def test_add():
    assert 1+2 == 3
```

## Beispiel (PHP PHPUnit)

```php
public function testAdd(): void {
  $this->assertSame(3, 1+2);
}
```

Später folgen konkrete Setups in den jeweiligen Ordnern.
