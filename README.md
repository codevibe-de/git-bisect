# Git Bisect – Übungsrepository

Dieses Repository dient als Spielwiese, um `git bisect` kennenzulernen und zu üben.

## Hintergrund

Das Repository enthält eine kleine Python-Anwendung (`stats.py`), die statistische Berechnungen durchführt – zum Beispiel Summe, Durchschnitt, Median und Standardabweichung.

Irgendwo in der Commit-Historie hat sich ein Bug eingeschlichen. Eine Funktion liefert seitdem falsche Ergebnisse, ohne dass dabei ein Fehler geworfen wird. Deine Aufgabe ist es, mit `git bisect` den genauen Commit zu finden, der den Fehler eingeführt hat.

## Voraussetzungen

- Python 3 installiert
- Git installiert

## Aufgabe

### 1. Reproduziere den Bug

Führe die Anwendung aus und schau dir die Ausgabe an:

```bash
python stats.py
```

Überlege, welcher der ausgegebenen Werte nicht stimmen könnte. Das Testskript hilft dir dabei, den Fehler eindeutig zu erkennen:

```bash
python test_average.py
```

### 2. Starte die Bisect-Suche

Markiere zunächst den aktuellen Stand als fehlerhaft und einen frühen Commit als funktionierend:

```bash
git bisect start
git bisect bad                  # aktueller Stand ist fehlerhaft
git bisect good <commit-hash>   # ein früher Commit, der noch korrekt war
```

Den Hash eines frühen Commits findest du mit:

```bash
git log --oneline
```

### 3. Teste jeden Zwischenstand

Git wechselt nun automatisch zwischen Commits. Nach jedem Wechsel testest du, ob der Bug vorhanden ist:

```bash
python test_average.py
```

Teile Git dann das Ergebnis mit:

```bash
git bisect good   # dieser Commit ist noch fehlerfrei
# oder
git bisect bad    # dieser Commit ist bereits fehlerhaft
```

### 4. Automatische Suche (optional)

Statt jeden Commit manuell zu testen, kann Git das Testskript auch selbst ausführen:

```bash
git bisect run python test_average.py
```

### 5. Auswertung

Sobald Git den problematischen Commit gefunden hat, schau dir die Änderung genau an:

```bash
git show <gefundener-commit-hash>
```

Kannst du den Fehler im Code erkennen?

### 6. Bisect beenden

Vergiss nicht, die Bisect-Sitzung abzuschließen, bevor du weitermachst:

```bash
git bisect reset
```

## Lernziele

Nach dieser Übung solltest du verstehen:

- wie `git bisect` eine binäre Suche über die Commit-Historie durchführt
- wie du mit `git bisect good` und `git bisect bad` Commits bewertest
- wie du mit `git bisect run` die Suche vollständig automatisierst
- warum ein automatisierbarer Test die Voraussetzung für eine effiziente Bisect-Suche ist
