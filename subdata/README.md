# Testdatensätze

Dieses Repository enthält CSV-Testdateien für das Statistik-Tool aus dem `git-bisect`-Projekt.

## Dateiformat

Jede CSV-Datei enthält eine einzige Spalte mit dem Header `value`. Jede Zeile darunter repräsentiert einen numerischen Wert, der als Eingabe für die Statistikfunktionen verwendet wird.

```
value
1.1
2.2
3.3
```

## Dateien

| Datei | Inhalt | Testschwerpunkt |
|---|---|---|
| `float_values.csv` | Fließkommazahlen (1,1 bis 9,9) | Genauigkeit bei Durchschnitt, Varianz und Standardabweichung |
| `empty.csv` | Keine Datenzeilen | Verhalten bei leeren Eingaben (`is_empty`, Absturzsicherheit) |
| `negative_values.csv` | Negative und positive Ganzzahlen inkl. Null | Bereich, Median über den Nullpunkt, Vorzeichen-Arithmetik |
