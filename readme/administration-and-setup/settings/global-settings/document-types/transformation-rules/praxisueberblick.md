# Transformationsregeln: vollständiger Praxisüberblick

Stand der Prüfung: 28. Oktober 2026. Die Beispiele wurden mit synthetischen Schulungswerten auf Dev NOVA geprüft. Eine Vorschau ist kein Nachweis einer gespeicherten Dokumentänderung, eines Bestellabgleichs oder eines ERP-Exports.

## Vier Geltungsbereiche

| Bereich | Eingabe und Ziel | Typische Aufgabe |
| --- | --- | --- |
| Kopffeld | Ein Feld pro Dokument; Quelle kann ein anderes Kopffeld sein | Rechnungsnummer bereinigen, Bestellnummer übernehmen |
| Tabellenspalte | Die gewählte Spalte je Zeile der gewählten Tabelle | Artikelnummern oder Einheitencodes vereinheitlichen |
| Tabellenzeilen | Ganze Tabelle | Zeilen entfernen oder definierte Positionen hinzufügen |
| Routing | Dokumentattribut `sub_org_id` | Vorhandene Unterorganisation zuweisen |

Die Bereiche laufen **Kopffeld → Routing → Tabellenzeilen → Tabellenspalte**. Innerhalb eines Bereichs bestimmen Priorität und Regelschlüssel die Reihenfolge. Die Schritte einer Regel laufen von oben nach unten. Eine nachgelagerte Regel kann daher bereits geänderte Werte lesen. Die Reihenfolge der Bereiche wird nicht durch die Priorität einer einzelnen Regel umgekehrt.

## Alle Schritte des Editors

Der geprüfte Editor bietet 14 Wertschritte für Kopf/Spalte, zwei Schritte für ganze Tabellen und eine feste Zuweisung im Routing. `Festwert` und die feste Routingzuweisung verwenden serverseitig beide `set_value`. Zusätzlich kennt die Schnittstelle `default`; dieser Schritt wird im geprüften normalen Schrittmenü nicht angeboten.

| Schritt | Varianten und Parameter | Beispiel | Grenze und Gegenprobe |
| --- | --- | --- | --- |
| Groß-/Kleinschreibung ändern (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Eigennamen/Abkürzungen können sich fachlich unerwünscht ändern. |
| Trimmen (`trim`) | beide / links / rechts; Zeichen leer = Leerraum | `  4711  ` → `4711` | `47 11` bleibt erhalten. Links Zeichen `0`: `004711` → `4711`, aber `000` → leer. Zeichen sind eine Menge, kein vollständiger Präfixtext. |
| Auffüllen (`pad`) | Mindestlänge, ein Füllzeichen, links/rechts | Länge 10, links `0`: `4711` → `0000004711` | Bereits 11 Zeichen bleiben 11 Zeichen. Rechts `_`, Länge 6: `ABC` → `ABC___`. |
| Kürzen (`truncate`) | maximale Länge | Länge 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` bleibt `ABC`. Abschneiden verliert Informationen und kann Nummern zusammenfallen lassen. |
| Affix (`affix`) | Präfix/Suffix hinzufügen/entfernen | `INV-` + `4711` → `INV-4711` | Vorhandenes exaktes Affix wird nicht doppelt hinzugefügt. Entfernen wirkt nur am passenden Rand und beachtet Großschreibung. |
| Zeichen bereinigen (`sanitize`) | alphanumerisch / Buchstaben / Ziffern / alphanumerisch + Leerzeichen behalten; alternativ Zeichenklasse entfernen | `DE 123.456.789` → `DE123456789` | Kennzeichen können bedeutungstragend sein. Beim Entfernen ist die Eingabe eine Regex-Zeichenklasse; Bindestrich korrekt schützen, z. B. `.\-/`. |
| Teilstück (`substring`) | Start + Länge **oder** Start + Ende; negative Indizes möglich | Start 3, Ende 7: `DE-4711-X` → `4711` | Start zählt ab 0, Ende ist exklusiv. Start −4: letzte vier Zeichen. Getrennte Originalquelle erforderlich. |
| Extrahieren (`regex_extract`) | regulärer Ausdruck, Erfassungsgruppe | `PO[- ]?(\d+)`, Gruppe 1: `Order PO-45001234` → `45001234` | Erster Treffer; Gruppe 0 = vollständiger Treffer. Ohne Treffer: leer. Getrennte Quelle erforderlich. |
| Suchen und Ersetzen (`regex_replace`) | Muster, Ersatz, Anzahl | `\s+` → Leerzeichen: `ACME    GmbH` → `ACME GmbH` | Anzahl 0 = alle, 1 = erster Treffer. Getrennte Quelle erforderlich. Browser-/Server-Regex bei komplexen Mustern separat prüfen. |
| Werte zuordnen (`value_map`) | vollständige von→nach-Paare; Großschreibung ignorieren; Ersatz ohne Treffer | `stk` → `PCE` mit `STK→PCE` und ignorierter Großschreibung | Leerer Ersatz bedeutet **Eingabe behalten**. `BOX` bleibt `BOX`; ein fester Ersatz `C62` würde `BOX` überschreiben. Trimmen erfolgt nicht automatisch. |
| Datum formatieren (`date_format`) | Ausgabemuster, z. B. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` im Textziel | Bei DATE-Kopffeldern kann der gespeicherte Wert ISO bleiben und nur die Darstellung wechseln. Unlesbarer Text bleibt unverändert; der Servertest nennt den Grund. |
| Zahl formatieren (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./max. Nachkommastellen | `1234.5` → `1234,50` bzw. `1234.50` im geprüften Serverergebnis | Kein Tausendertrennzeichen im geprüften Serverergebnis. Keine Währungs- oder Mengenumrechnung. Rundung und Wiederverarbeitung separat prüfen. |
| Festwert (`fix_value` im Editor, `set_value` in der API) | ein fester Wert | `USD` → `EUR` | Überschreibt auch vorhandene Werte. Nicht mit einem Standardwert verwechseln. |
| Leeren (`clear`) | keine Parameter | `Altwert` → `""` | Leert den Wert; löscht weder Felddefinition noch Dokument. |
| Alle Zeilen löschen (`clear_rows`) | nur Tabellenzeilen | 2 Positionen → 0 | Kann Zeilenbezüge und vorhandenen PO-Abgleich ungültig machen. |
| Zeile hinzufügen (`add_row`) | Anfang/Ende; pro Spalte fester Wert oder Kopfquelle | Menge `1`, Nettobetrag aus `header.total_net_amount` | Ohne vorheriges Löschen nur mit geeigneter Einmalausführung. Keine automatische Aggregation bestehender Positionen. |
| Feste Unterorganisation (`set_value`, Routing) | vorhandenes Ziel aus der Unterorganisationsauswahl | Lieferant A → Unterorganisation Nord | Kein beliebiges Status-/Benutzer-/Berechtigungsattribut. Alternativ Zuordnung über `value_map` und Quelle. |

### Standardwert über die Schnittstelle

`default` ergänzt seinen Wert nur bei fehlender/leerer Eingabe. Mit Standard `1` ergeben `null` und `""` den Wert `1`; `0` bleibt `0`, `100` bleibt `100`. Das ist serverseitig geprüft. Der normale Editor hat dafür im geprüften Stand keinen eigenen Schritt. Der fachlich entsprechende einfache Fall lässt sich häufig mit **Ziel ist leer → Festwert** abbilden. Das ist eine Regelbedingung mit Zuweisung, kein versteckter Menüpunkt.

## Neun ausführliche Praxisfolgen

- [01 · Grundlagen, Geltungsbereiche und sichere Tests](01-grundlagen.md)
- [02 · Text bereinigen: Schreibweise, Trimmen und Zeichen](02-text-bereinigen.md)
- [03 · Nummern formen: Auffüllen, Kürzen, Präfix und Suffix](03-nummern-und-affixe.md)
- [04 · Teilstücke und Muster: Ausschneiden, Extrahieren, Ersetzen](04-teilstuecke-und-muster.md)
- [05 · Wertzuordnungen und Regeln pro Tabellenzeile](05-werte-zuordnen.md)
- [06 · Datum und Zahlen richtig formatieren](06-datum-und-zahlen.md)
- [07 · Felder übernehmen, Festwerte, Leeren und Standardwerte](07-felduebernahme-und-standardwerte.md)
- [08 · Tabellenzeilen neu aufbauen](08-tabellenzeilen.md)
- [09 · Routing, Reihenfolge, Stammdaten und Wiederholungen](09-routing-und-ausfuehrung.md)

| Folge | Inhalt | Konkreter Prüfpunkt |
| --- | --- | --- |
| 01 Grundlagen | Ziel, Quelle, vier Bereiche, Pipeline, Bedingungen, Vorschau, Speicherung | Passender Fall, Gegenfall, gespeicherte Regel erneut öffnen |
| 02 Textbereinigung | Alle vier Schreibweisen, Trimmen, alle Bereinigungsmodi | Interne Leerzeichen, reine Nullfolge, bedeutungstragende Zeichen |
| 03 Nummern | Auffüllen, Kürzen, alle vier Affix-Varianten | Zu lange Nummer, schon vorhandenes Präfix, doppelte Präfixe |
| 04 Muster | Teilstück, negative Indizes, Extraktion/Gruppen, Ersetzen/Anzahl | Separate Quelle, kein Treffer, mehrere Treffer |
| 05 Zuordnung | Paare, Großschreibung, Ersatz, Anwendung je Zeile | `STK→PCE`, unbekanntes `BOX`, erneute Anwendung auf `PCE` |
| 06 Formate | Datum, DATE vs. Text, unlesbares Datum, Zahlenformate | Tatsächlicher Serverwert statt angenommener Browserdarstellung |
| 07 Feldübernahme | Andere Quelle, leeres Ziel, Festwert, Leeren, API-Standardwert | Vorhandene korrekte Bestellnummer schützen; Null bleibt Null |
| 08 Tabellen | Löschen, Hinzufügen, statische und dynamische Spaltenwerte | Reihenfolge, Wiederholung, Zeilenzahl und PO-Bezüge |
| 09 Zusammenspiel | Routing, Phasen, Lookup, Einmalausführung, Protokolle | Bereinigte Kopfquelle, übersprungene Bedingung, zweites Speichern |

## Bedingungen und Quellen

Mit „Stets“ gilt die Regel ohne fachliche Einschränkung für den Dokumenttyp. „Nur wenn…“ begrenzt sie durch Bedingungen. Kopfwerte stehen im Kontext `header.*`, Dokumentmerkmale in `doc.*`; `row.*` steht nur im Zeilenkontext einer Spaltenregel zur Verfügung. Verschachtelte Und-/Oder-Gruppen erlauben kombinierte Kriterien. Für die einzelnen Operatoren gilt die separate Dokumentation der Regelbedingungen.

**Beispiel Feldübernahme:** Ziel `purchase_order`, Quelle `header.invoice_id`, Bedingung `header.purchase_order` ist leer, Schritte Trimmen → Großschreibung. `  po-4711  ` ergibt `PO-4711`. Eine bereits richtig gefüllte Bestellnummer soll unverändert bleiben. Nicht die falsche Quelle leeren: Kopieren mit Verarbeitung verschiebt die Quelle nicht.

**Beispiel Artikelnummer:** Tabelle `INVOICE_TABLE`, Spalte `ITEM_NUMBER`, Präfix `Art.-Nr. ` entfernen → alphanumerisch behalten → Großschreibung. `Art.-Nr. ab-12/3` ergibt `AB123`. Nur geeignet, wenn das Zielsystem genau diese Form erwartet.

**Beispiel Gesamtzeile:** Für einen klar eingegrenzten Lieferanten zuerst `clear_rows`, dann `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` aus dem Nettobetrag des Kopfes. Ob ein Bestellabgleich auf die Gesamtsumme fachlich korrekt ist, wird durch die zusätzliche PO-Konfiguration und einen gesonderten Abgleichstest entschieden.

## Wiederholung und Einmalausführung

Regeln können in mehreren Verarbeitungsdurchläufen und beim Speichern erneut laufen. Prüfen Sie immer **die ganze Pipeline**, nicht nur die Stabilität eines einzelnen Schritts.

* `substring`, `regex_extract` und `regex_replace` dürfen im geprüften Serververtrag nicht ihren eigenen Zielwert lesen. Eine getrennte Quelle ist erforderlich; `run_once` hebt diese Vorgabe nicht auf.
* Ergänzen eines bereits vorhandenen exakten Affixes ist stabil. Entfernen eines mehrfach vorhandenen Präfixes kann dagegen bei jedem Durchlauf weiter entfernen.
* `A→B` und `B→C` in derselben Wertzuordnung können bei zwei Durchläufen aus `A` schließlich `C` machen. Testen Sie Ausgaben erneut als Eingaben.
* `clear_rows → add_row` baut eine Tabelle begrenzt neu auf. `add_row` ohne vorheriges Löschen benötigt eine geeignete Einmalausführung, sonst wächst die Tabelle bei jedem Speichern.
* „Nur einmal pro Dokument“ markiert eine tatsächlich angewendete Regel. Nicht erfüllte Bedingungen verbrauchen die Anwendung nicht. Ohne verlässlich lesbaren Dokument-/Anwendungsnachweis wird eine Einmalregel zurückgestellt.

## Nach dem Lookup und vor dem Bestellabgleich

„Auch nach der Stammdatensuche ausführen“ ergänzt eine Phase nach der Lookup-Befüllung und vor dem PO-Abgleich. Nur entsprechend markierte Regeln laufen in dieser Zusatzphase. Die übrigen Durchläufe bleiben bestehen. Kombiniert mit Einmalausführung wartet die Regel beim ersten Extraktionsdurchlauf auf die spätere Phase; fällt die Lookup-Phase aus, kommt ein späterer regulärer Durchlauf infrage. Die Phasenanzeige des aktuellen Editors zeigt diese Unterschiede.

## Ein belastbarer Abnahmetest

1. Fachliches Ziel, Zielsystemformat und Geltungsbereich festlegen.
2. Einen passenden Rohwert, einen Gegenfall, einen leeren Wert und ein bereits verarbeitetes Ergebnis vorbereiten.
3. Bedingungen und sämtliche Zwischenwerte in der Vorschau prüfen.
4. Serverseitigen Test gegen dasselbe Beispiel ausführen; komplexe Muster und Zahlen-/Datumsformate besonders vergleichen.
5. Regel speichern und erneut öffnen. Eine aktive Regel nur im vorgesehenen Testumfang einsetzen.
6. Bei einem isolierten Dokument speichern, neu laden und Wert sowie Anzeige prüfen; bei Tabellen auch Zeilenzahl und Spaltenwerte.
7. Noch einmal speichern. Das Ergebnis darf nicht ungewollt weiter verändert oder vervielfacht werden.
8. Wenn fachlich erforderlich, PO-Abgleich und tatsächlichen Empfang im Zielsystem zusätzlich prüfen. Ein Transformationsprotokoll allein beweist diese Ergebnisse nicht.

## Was eine Transformation nicht automatisch erledigt

Keine neue OCR-Erkennung, keine mathematische Einheiten- oder Währungsumrechnung, keine beliebige Tabellenaggregation und keine vollständige ERP-Buchung. Routing ist auf das angebotene Dokumentattribut begrenzt. Verfügbarkeit und genaue Anzeige hängen von der eingesetzten Version, dem Dokumenttyp und der Organisationskonfiguration ab.

## Durchgängiger Übungsbeleg

[Schulungsrechnung herunterladen](../../../../../.gitbook/assets/transformation-schulungsrechnung-20261028.pdf). Der fiktive Beleg enthält zwei Positionen, unterschiedliche Schreibweisen der Einheit und eine Bestellreferenz im Freitext. Für reproduzierbare Regeltests werden die Ausgangswerte gezielt vorbereitet; dies ist kein Nachweis einer automatisch fehlerfreien OCR-Extraktion.
