# Text bereinigen: Schreibweise, Trimmen und Zeichen

[Zurück zum vollständigen Praxisüberblick](praxisueberblick.md)

Kopffeld · Ziel Ergebnis · Schritte einzeln testen: case, trim, sanitize.

## Vorgehen im Editor

1. Für das Schulungs-Kopffeld einen einzelnen Schritt **Groß-/Kleinschreibung ändern** anlegen. Die Modi upper, lower, title und capitalize nacheinander mit den Beispielen der Tabelle prüfen.
2. Für die Rechnungsnummer eine neue Pipeline mit **Trimmen** beginnen. Seite beide und ein leeres Zeichenfeld entfernen äußeren Leerraum; `47 11` muss seine innere Lücke behalten.
3. Als getrennte Gegenprobe beim Trimmen Seite links und Zeichen `0` einstellen: `004711` wird `4711`, `000` wird leer. Diesen Schritt nicht ungeprüft für echte Kennungen übernehmen.
4. Bei einer Steuerkennung **Zeichen bereinigen** mit alphanumerisch behalten verwenden. `DE 123.456.789` muss `DE123456789` ergeben. Die weiteren Behaltemodi mit `DE-123` bzw. `ACME GmbH!` prüfen.
5. Für capitalize ausdrücklich Vorschau und Server vergleichen: Beim geprüften `aCME GMBH` sind diese Ergebnisse unterschiedlich. Das Serverergebnis ist `Acme gmbh`; eine passende Browserdarstellung allein genügt nicht.

<figure><img src="../../../../../.gitbook/assets/transformation-series-02-steps-de-20261028.png" alt="Konfiguration der Schritte – Text bereinigen: Schreibweise, Trimmen und Zeichen"><figcaption><p>Konfiguration der Schritte. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/transformation-series-02-preview-de-20261028.png" alt="Live-Vorschau mit Schulungswert – Text bereinigen: Schreibweise, Trimmen und Zeichen"><figcaption><p>Live-Vorschau mit Schulungswert. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

## 1. Schreibweise

Großschreibung vereinheitlicht beispielsweise eine Rechnungsnummer. Kleinschreibung kann einen technischen Vergleichsschlüssel vereinheitlichen. Title Case und die Großschreibung des ersten Zeichens können auch den Rest des Wortes verändern. Aus einer Firmenabkürzung kann deshalb eine andere Schreibweise werden. Für Eigennamen verwende ich diese Varianten nur mit einer klaren fachlichen Vorgabe. Beim Modus Capitalise first gibt es im geprüften Stand eine Abweichung: Die Browservorschau lässt die übrige Schreibweise stehen, während der Server den Rest kleinschreibt. Ich verlasse mich hier deshalb nicht allein auf die Vorschau, sondern vergleiche ausdrücklich den Serverwert.

## 2. Trimmen

Trimmen entfernt Zeichen am Rand. Beide Seiten entfernt äußere Leerzeichen, aber kein Leerzeichen mitten in einer Nummer. Links mit dem Zeichen Null entfernt alle führenden Nullen. Ein Wert, der nur aus Nullen besteht, wird dadurch leer. Rechts arbeitet entsprechend am Ende. Das Feld Zeichen ist eine Menge einzelner Zeichen und kein vollständiges Präfix. Ein festes Artikelpräfix entferne ich deshalb mit Affix. Auffüllen und Abschneiden behandeln wir in der nächsten Folge.

## 3. Zeichen bereinigen

Beim Bereinigen kann ich nur Buchstaben und Ziffern, nur Buchstaben, nur Ziffern oder zusätzlich Leerzeichen behalten. Eine deutsche Steuerkennung mit Leerzeichen und Punkten wird so zu einem zusammenhängenden Schlüssel. Bei einer Artikelnummer können Bindestriche allerdings fachlich wichtig sein. Das Entfernen solcher Zeichen muss zur Schreibweise im Zielsystem passen. Die alternative Zeichenentfernung arbeitet mit einer regulären Zeichenklasse. Ein Bindestrich benötigt darin besondere Aufmerksamkeit. Für mein Beispiel prüfe ich deshalb den tatsächlichen Serverwert zusätzlich zur Vorschau. Bereits bereinigte Werte und leere Eingaben gehören in jeden Test.

## Geprüfte Beispiele und Gegenfälle

Diese Werte wurden serverseitig als trockener Test geprüft. Ein solcher Test verändert keine gespeicherten Dokumente.

| Fall | Eingabe | Serverergebnis |
| --- | --- | --- |
| case-upper | `inv-4711` | `INV-4711` |
| case-upper | `INV-4711` | `INV-4711` |
| case-lower | `INFO@BEISPIEL.DE` | `info@beispiel.de` |
| case-title | `acme gmbh` | `Acme Gmbh` |
| case-capitalize | `aCME GMBH` | `Acme gmbh` |
| trim | `  4711  ` | `4711` |
| trim | `47 11` | `47 11` |
| trim-zero | `004711` | `4711` |
| trim-zero | `000` | `` |
| sanitize | `DE 123.456.789` | `DE123456789` |
| sanitize-alpha | `DE-123` | `DE` |
| sanitize-numeric | `DE-123` | `123` |
| sanitize-space | `ACME GmbH!` | `ACME GmbH` |
| sanitize-strip | `ab-12/3.` | `ab123` |

## Abnahme

Prüfen Sie einen passenden Fall, einen Gegenfall, einen leeren Wert und ein bereits verarbeitetes Ergebnis. Wiederholen Sie den Dokument-Speichervorgang. Prüfen Sie PO-Abgleich und ERP-Empfang zusätzlich, wenn sie zum fachlichen Ziel gehören.

## Videoanleitung

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules-02-text-cleaning-preview-admin/v1/de.mp4" %}
Text bereinigen: Schreibweise, Trimmen und Zeichen – Konfiguration, Beispiele und Gegenfälle.
{% endembed %}

[Video mit deutschen Untertiteln und Kapiteln öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules-02-text-cleaning-preview-admin/v1/de.html). Die fachliche und vollständige Hörprüfung dieser Reviewfassung steht noch aus.
