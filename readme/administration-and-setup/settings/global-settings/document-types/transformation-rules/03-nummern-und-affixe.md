# Nummern formen: Auffüllen, Kürzen, Präfix und Suffix

[Zurück zum vollständigen Praxisüberblick](praxisueberblick.md)

Kopffeld · pad: Länge 10, Zeichen 0, links; truncate: Länge 10; affix: exakte Präfix-/Suffixoperation.

## Vorgehen im Editor

1. Den vorgesehenen Dokumenttyp öffnen und den Geltungsbereich wählen.
2. Ziel und gegebenenfalls eine getrennte Quelle einstellen.
3. Die unten beschriebenen Schritte in der passenden Reihenfolge konfigurieren.
4. Eingabe und Gegenfall in der Vorschau prüfen und mit dem Servertest vergleichen.
5. Eine gespeicherte Regel erneut öffnen; die Dokumentwirkung mit einem isolierten Beleg prüfen.

<figure><img src="../../../../../.gitbook/assets/transformation-series-03-steps-de-20261028.png" alt="Konfiguration der Schritte – Nummern formen: Auffüllen, Kürzen, Präfix und Suffix"><figcaption><p>Konfiguration der Schritte. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente. Der Editor nennt Auffüllen derzeit „Unterlage“; gemeint ist die Ergänzung auf eine Mindestlänge.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/transformation-series-03-preview-de-20261028.png" alt="Live-Vorschau mit Schulungswert – Nummern formen: Auffüllen, Kürzen, Präfix und Suffix"><figcaption><p>Live-Vorschau mit Schulungswert. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

## 1. Länge

Auffüllen ergänzt links oder rechts ein einzelnes Füllzeichen bis zur Mindestlänge. Mit zehn Stellen und Null links wird aus einer vierstelligen Nummer eine zehnstellige Kennung. Eine bereits längere Nummer bleibt länger. Auffüllen ist also keine Längenprüfung. Kürzen behält dagegen nur die ersten Zeichen bis zur gewählten Höchstlänge. Diese Information geht verloren. Vor einem ERP-Einsatz prüfe ich, ob verschiedene Nummern nach dem Kürzen identisch werden könnten. Kurze Werte bleiben unverändert.

## 2. Präfix und Suffix

Affix bietet vier Varianten: Präfix hinzufügen, Suffix hinzufügen, Präfix entfernen und Suffix entfernen. Ein hinzugefügtes Präfix wird nicht noch einmal ergänzt, wenn der Wert bereits genau damit beginnt. Das gilt entsprechend für ein Suffix. Entfernen prüft dagegen genau den Anfang oder das Ende. Eine abweichende Großschreibung wird nicht automatisch gleichgesetzt. Steht der Text mitten im Wert, bleibt er erhalten. Für beliebige Fundstellen verwende ich Suchen und Ersetzen.

## 3. Erneute Anwendung

Auch eine einfache Pipeline braucht einen Wiederholungstest. Entferne ich ein Präfix von einem doppelt vorangestellten Präfix, bleibt nach dem ersten Durchlauf noch eines übrig. Beim nächsten Durchlauf würde auch dieses verschwinden. Deshalb prüfe ich die gesamte Regel und nicht nur jeden Schritt einzeln. Die typische Rechnungsnummernpipeline lautet: Trimmen, Großschreibung, Präfix ergänzen. Ich teste eine rohe Nummer, eine schon fertige Nummer und einen abweichenden Lieferanten. Die Bedingung sorgt dafür, dass nur der vereinbarte Fall geändert wird.

## Geprüfte Beispiele und Gegenfälle

Diese Werte wurden serverseitig als trockener Test geprüft. Ein solcher Test verändert keine gespeicherten Dokumente.

| Fall | Eingabe | Serverergebnis |
| --- | --- | --- |
| pad | `4711` | `0000004711` |
| pad | `12345678901` | `12345678901` |
| pad-right | `ABC` | `ABC___` |
| truncate | `ABCDEFGHIJKL` | `ABCDEFGHIJ` |
| truncate | `ABC` | `ABC` |
| prefix-add | `4711` | `INV-4711` |
| prefix-add | `INV-4711` | `INV-4711` |
| suffix-add | `4711` | `4711-DE` |
| suffix-add | `4711-DE` | `4711-DE` |
| prefix-strip | `Art.-Nr. 4711` | `4711` |
| prefix-strip | `ART.-NR. 4711` | `ART.-NR. 4711` |
| prefix-strip | `Art.-Nr. Art.-Nr. 4711` | `Art.-Nr. 4711` |
| suffix-strip | `123 EUR` | `123` |
| suffix-strip | `123 EUR netto` | `123 EUR netto` |

## Abnahme

Prüfen Sie einen passenden Fall, einen Gegenfall, einen leeren Wert und ein bereits verarbeitetes Ergebnis. Wiederholen Sie den Dokument-Speichervorgang. Prüfen Sie PO-Abgleich und ERP-Empfang zusätzlich, wenn sie zum fachlichen Ziel gehören.
