# Datum und Zahlen richtig formatieren

[Zurück zum vollständigen Praxisüberblick](praxisueberblick.md)

Textziel · date_format: %d.%m.%Y; number_format: de_DE, min. 2, max. 2 Nachkommastellen.

## Vorgehen im Editor

1. Den vorgesehenen Dokumenttyp öffnen und den Geltungsbereich wählen.
2. Ziel und gegebenenfalls eine getrennte Quelle einstellen.
3. Die unten beschriebenen Schritte in der passenden Reihenfolge konfigurieren.
4. Eingabe und Gegenfall in der Vorschau prüfen und mit dem Servertest vergleichen.
5. Eine gespeicherte Regel erneut öffnen; die Dokumentwirkung mit einem isolierten Beleg prüfen.

<figure><img src="../../../../../.gitbook/assets/transformation-series-06-steps-de-20261028.png" alt="Konfiguration der Schritte – Datum und Zahlen richtig formatieren"><figcaption><p>Konfiguration der Schritte. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/transformation-series-06-preview-de-20261028.png" alt="Live-Vorschau mit Schulungswert – Datum und Zahlen richtig formatieren"><figcaption><p>Live-Vorschau mit Schulungswert. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente. Das sichtbare Tausendertrennzeichen gehört zur Browservorschau; der geprüfte Serverwert lautet 1234,50.</p></figcaption></figure>

## 1. Datum und Datentyp

Datum neu formatieren schreibt ein Datum nach dem gewählten Muster. Ein eindeutiges ISO-Datum ist eine gute Testeingabe. Tag, Monat und Jahr lassen sich beispielsweise mit Punkten ausgeben. Bei einem echten Datumskopffeld kann der interne Wert im ISO-Format bleiben, während sich die Anzeige ändert. Ein Textfeld oder eine Tabellenzelle kann dagegen den formatierten Text enthalten. Deshalb vergleiche ich nicht nur das sichtbare Feld, sondern auch den gespeicherten Wert und die spätere Verwendung.

## 2. Unlesbare und mehrdeutige Daten

Ein unlesbares Datum wird nicht einfach erfunden. In meinem Servertest bleibt der Text unverändert, und das Ergebnis nennt den Grund. Mehrdeutige Angaben wie Tag und Monat mit kleinen Zahlen brauchen einen eindeutig vereinbarten Kontext. Ein formatiertes Datum darf beim nächsten Speichern nicht als ein anderer Tag gelesen werden. Ich prüfe deshalb einen zweiten Durchlauf. Aus einem beliebigen Text ohne gültiges Datum kann diese Transformation kein verlässliches Datum machen.

## 3. Zahlenformat

Zahlen formatieren verwendet ein Gebietsschema und eine minimale sowie maximale Zahl von Nachkommastellen. Das ändert Darstellung und gegebenenfalls Rundung, aber keinen Wechselkurs und keine Mengeneinheit. Für meine Eingabe tausendzweihundertvierunddreißig Komma fünf liefert der aktuelle Server mit zwei Nachkommastellen eine deutsche Kommaschreibweise oder eine englische Punktschreibweise. Ein Tausendertrennzeichen ist im geprüften Serverergebnis nicht enthalten. Ich übernehme deshalb keine schönere Browserdarstellung als Beweis für den Export. Null, negative Beträge, zusätzliche Nachkommastellen und der gespeicherte Ergebniswert brauchen eigene Tests.

## Geprüfte Beispiele und Gegenfälle

Diese Werte wurden serverseitig als trockener Test geprüft. Ein solcher Test verändert keine gespeicherten Dokumente.

| Fall | Eingabe | Serverergebnis |
| --- | --- | --- |
| date | `2026-10-28` | `28.10.2026` |
| date | `kein Datum` | `kein Datum` |
| number-de | `1234.5` | `1234,50` |
| number-us | `1234.5` | `1234.50` |

## Abnahme

Prüfen Sie einen passenden Fall, einen Gegenfall, einen leeren Wert und ein bereits verarbeitetes Ergebnis. Wiederholen Sie den Dokument-Speichervorgang. Prüfen Sie PO-Abgleich und ERP-Empfang zusätzlich, wenn sie zum fachlichen Ziel gehören.

Im geprüften Stand unterscheiden sich Zahlenvorschau und Server bei Tausendertrennzeichen. Die Tabelle nennt den tatsächlichen Serverwert.
