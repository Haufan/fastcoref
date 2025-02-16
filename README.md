# Koreference-Auflösung mit Farb-Hervorhebung

Dieses Python-Programm liest eine Textdatei, löst Kofreferenzen mithilfe der `fastcoref`-Bibliothek auf und gibt den Text aus, wobei Kofreferenzen farblich hervorgehoben werden, um Cluster verwandter Wörter visuell zu kennzeichnen. Es verwendet `colorama` für die Unterstützung von Farben im Terminal, was es einfach macht, Kofreferenzen im Text zu identifizieren und zu analysieren.

> **Hinweis:** Das Modell funktioniert nur mit englischen Texten.

## Funktionen
- Löst Kofreferenzen in einem gegebenen englischen Text mit dem `fastcoref`-Modell auf.
- Färbt Kofreferenten im Text mit unterschiedlichen Farben.
- Gibt eine nummerierte Liste der Kofreferenz-Cluster aus.
- Ermöglicht die optionale Hervorhebung eines bestimmten Kofreferenz-Clusters mittels eines Kommandozeilen-Arguments.
- Unterstützt vollständig die Terminal-Ausgabe mit Farben (über `colorama`).

## Anforderungen

- Python 3.9
- `fastcoref`-Bibliothek
- `colorama`-Bibliothek

## Verwendung

### Ausführen des Programms

Um das Programm auszuführen, verwenden Sie den folgenden Befehl in Ihrem Terminal:

```bash
python coreference_print.py <file_path> [--cluster <cluster_number>]
```

### Parameter

- **`<file_path>`**: Der Pfad zur Textdatei, die den Text enthält, den Sie analysieren möchten.
- **`--cluster <cluster_number>`**: Ein optionales Argument, mit dem ein bestimmtes Kofreferenz-Cluster hervorgehoben werden kann. Wenn dieses Argument weggelassen wird, werden alle Kofreferenzen hervorgehoben.

### Beispiel-Verwendung

#### Alle Kofreferenz-Cluster hervorheben:

```bash
python coreference_print.py "C:/path/to/your/file.txt"
```

Dies wird die Kofreferenzen in der angegebenen Datei auflösen und die Ausgabe mit jedem Cluster in einer anderen Farbe anzeigen.

#### Ein bestimmtes Kofreferenz-Cluster hervorheben:

```bash
python coreference_print.py "C:/path/to/your/file.txt" --cluster 1
```

Dies wird nur die Wörter im Cluster 1 färben und die Farben für den Rest des Textes zurücksetzen.

### Ausgabeformat

Das Programm gibt die Kofreferenz-Cluster als nummerierte Liste aus, wobei die Wörter jedes Clusters im Originaltext daneben angezeigt werden. Danach wird der Text mit den farblich markierten Kofreferenz-Clustern ausgegeben. Die Ausgabe könnte folgendermaßen aussehen:

```bash
Coreference Clusters:

Cluster 1: ['John', 'his', 'him']\
Cluster 2: ['his friend, Sarah', 'She']


Text mit Koferrenzen in Farben:

John went to the park to meet hishis friend, Sarah.
She had been waiting for him near the fountain.
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.