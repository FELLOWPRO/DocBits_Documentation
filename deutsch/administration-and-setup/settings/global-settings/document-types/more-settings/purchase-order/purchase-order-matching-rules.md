# Regeln für die Übereinstimmung von Bestellungen

## Einführung: Bestellungen und Verwaltung der PO-Regeln

Die Übereinstimmung von Bestellungen (Purchase Order, PO) ist ein kritischer Prozess, um die Konsistenz zwischen Bestellungen (POs) und den entsprechenden eingehenden Rechnungen oder Wareneingängen sicherzustellen. Ein robustes Regelwerk ist unerlässlich, um eine hohe Rate an automatischer Übereinstimmung zu erreichen, Betrug zu verhindern und korrekte Zahlungen zu gewährleisten.

Diese Konfigurationsseite dient dazu, die Regeln zu definieren und zu verwalten, die bestimmen, _wie_ PO-Positionen mit dem entsprechenden eingehenden Dokument (Rechnung, Auftragsbestätigung) abgeglichen werden.

{% hint style="info" %}
**Voraussetzung:** Die Matching-Regeln werden nur verwendet, wenn **PO match server side** für den Dokumenttyp aktiviert ist (Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellung). Ist der Schalter deaktiviert, führt DocBits den Abgleich mit seinem eingebauten Matcher durch (Menge, Stückpreis, Artikelnummer, Bestellnummer) und ignoriert das Regelwerk.
{% endhint %}

***

## Zugriff

1.  Navigieren Sie zu **Einstellungen --> Globale Einstellungen --> Dokumenttypen**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Wählen Sie den gewünschten Dokumenttyp aus und klicken Sie auf **Weitere Einstellungen**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Gehen Sie dann zum Abschnitt Bestellung und klicken Sie auf den Button (PO match server side), danach klicken Sie auf Konfigurieren der PO-Matching-Regeln

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Globale Einstellungen (Basisregeln)

Diese Einstellungen legen den Rahmen fest, der für alle Matching-Regeln gilt:

* **Einstellung:** Match Quantity On
  * **Zweck:** Definiert, welche Menge der Bestellposition mit der Dokumentposition verglichen wird — zum Beispiel die bestellte Menge oder die **offene Rechnungsmenge** (bestellt minus bereits berechnet), was die übliche Wahl für Rechnungen ist.
  * **Gültige Werte:** Menge oder andere verfügbare Mengenfelder im System, abhängig von der Datenstruktur (z. B. ein alternatives normalisiertes Mengenfeld).
  * **Abhängigkeit:** Bestimmt die Grundlage für alle Matching-Regeln, die Menge in ihren Vergleichskriterien einschließen.
* **Einstellung:** Standardtoleranz (Standardabweichung)
  * **Zweck:** Definiert, wie stark ein numerischer Wert im Dokument vom Bestellwert abweichen darf und trotzdem als Übereinstimmung gilt. Dies kompensiert Rundungsdifferenzen. Es gilt für **jede numerische Spalte**, bei der "Toleranz erlauben" aktiviert ist — sowohl Menge als auch Stückpreis.
  * **Gültiger Wert:** Eine Dezimalzahl. Ob diese als **absoluter Wert** (0,005 = eine Abweichung von bis zu 0,005 in der verglichenen Menge oder dem Preis) oder als **Prozentsatz** (0,5 = 0,5 % des verglichenen Werts) interpretiert wird, wird durch den **Toleranztyp** des Regelwerks festgelegt (`value` oder `percent`; neue Regelwerke verwenden `value`). Artikelspezifische Toleranzen (siehe [Toleranzeinstellungen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) überschreiben die Standardtoleranz für diesen Artikel.
  * **Abhängigkeit:** Gilt für Regeln, die numerische Felder zum Abgleich verwenden und bei denen die Option "Toleranz erlauben" aktiviert ist.

***

## Regelübersicht

Die Regelübersicht zeigt alle verfügbaren Matching-Regeln an und verwaltet deren Ausführungsreihenfolge.

#### Aufbau und Ausführung

* **Priorität:** Dieses numerische Feld (z. B. 1, 2, 3) bestimmt die Reihenfolge der Ausführung der Regeln. Regeln mit einer niedrigeren Prioritätsnummer werden zuerst versucht. Dies ermöglicht Administratoren, eine Hierarchie zu strukturieren, typischerweise beginnend mit den spezifischsten und strengsten Regeln (z. B. Abgleich nach Zeilennummer und Artikelnummer) und als Rückfall auf breitere oder weniger restriktive Regeln.
* **Name & Beschreibung:** Bietet eine klare Identifikation und Kontext für die Regel, erklärt die primären Kriterien (z. B. „Standardregel Nr. 1: Abgleich basierend auf Zeilennummer, Artikel-ID und Menge“).
* **Aktiv:** Ein einfacher Umschalter, der eine sofortige Aktivierung oder Deaktivierung der Regel ermöglicht, ohne die Konfiguration löschen zu müssen.

**Ausführungsablauf:** Das System führt den Abgleich in einer kaskadierenden Reihenfolge durch. Wenn eine Regel (z. B. Priorität 1) eine Position erfolgreich abgleicht, wird der Prozess für diese Position beendet. Wird keine Übereinstimmung gefunden, fährt das System mit der nächsten Regel in der Prioritätsreihenfolge fort (z. B. Priorität 2). Jeder Lauf wird im Dokument protokolliert; die **Matching-Historie** im Bildschirm zur Bestellabstimmung zeigt, welche Regel versucht wurde, welche übereinstimmte und welche übersprungen wurden und warum.

***

## Regelkonfiguration (Detail-Einstellungen)

Dieser detaillierte Konfigurationsbereich definiert die spezifische Logik und Kriterien für eine einzelne Regel.

#### Basisparameter

* **Regeltyp:** Gibt die Matching-Kardinalität an.

| Regeltyp           | Was sie bewirkt                                                                                                                                                                                          | Typische Verwendung                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Single match**   | Eine Bestellposition zu einer Dokumentposition. Jede konfigurierte Spalte muss übereinstimmen (innerhalb der erlaubten Toleranz).                                                                        | Der Standardfall.                                                              |
| **Multi match**    | Mehrere Bestellpositionen zu einer Dokumentposition oder mehrere Dokumentpositionen zu einer Bestellposition. Mengen werden **summiert**, der Stückpreis als **Durchschnitt** verglichen, die anderen Spalten müssen übereinstimmen. | Teillieferungen, eine Rechnungsposition, die mehrere Bestellpositionen abdeckt. |
| **Match on total** | Vergleicht einen **Betrag** — üblicherweise den Nettobetrag der Dokumentposition gegen die Bestellsumme — und gleicht die gesamte Bestellung auf einmal ab.                                              | Lieferanten, die pauschal abrechnen, Dienstleistungsrechnungen, Einzeilige Rechnungen. |

* **Automatischer Abgleich:** Wenn aktiviert, versucht das System, diese Regel vollständig automatisch anzuwenden. Für die automatische Verarbeitung ist ein hohes Vertrauen in die Kriterien erforderlich.
* **Manueller Abgleich:** Wenn aktiviert, kann diese Regel einem Benutzer während des manuellen Abgleichs präsentiert oder angewendet werden und bietet ihm einen vordefinierten Satz von Vergleichskriterien zur Lösung von Ausnahmen.
* **Fallback:** Eine als Fallback markierte Regel läuft in einer späteren Phase nur für die Positionspaare, die nach allen regulären Regeln noch nicht abgeglichen wurden. Verwenden Sie sie für die „lockerere“ Regel, die das auffangen soll, was die strengen Regeln verpasst haben.

#### Aktivierungsbedingungen

Eine Regel kann **Aktivierungsbedingungen** enthalten — Ausdrücke, die wahr sein müssen, bevor die Regel überhaupt ausgeführt wird. Ist eine Bedingung falsch, wird die Regel **für dieses Dokument übersprungen** (die Matching-Historie zeigt sie als „nicht ausgeführt“ mit dem Grund). Die Ausdrücke verwenden die Anzahl der Positionen, die abgeglichen werden:

| Ausdruck                | Bedeutung                                                             |
| ----------------------- | ------------------------------------------------------------------- |
| `[[count(po_lines)]]`    | Anzahl der für den Abgleich verfügbaren Bestellpositionen           |
| `[[count(table_lines)]]` | Anzahl der Positionen im Dokument, die für den Abgleich zugeordnet sind |

Vergleichen Sie sie mit `==`, `!=`, `>`, `>=`, `<`, `<=` und kombinieren Sie mehrere Bedingungen mit `&` (und). Beispiele:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — nur für Dokumente mit mehreren Positionen auf beiden Seiten (typisch für eine Multi-Match-Regel).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — nur für einzeilige Dokumente gegen eine einzeilige Bestellung.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — wann immer etwas abgeglichen werden soll.

{% hint style="warning" %}
Aktivierungsbedingungen sind der häufigste Grund, warum eine Regel „nichts tut“. Eine Match-on-Total-Regel mit der Bedingung `[[count(table_lines)]] > 1` läuft nie für eine einzeilige Rechnung — und eine [Transformationsregel](../../transformation-rules.md), die die Rechnung in eine Gesamtposition zusammenfasst, erzeugt genau ein solches Dokument. Prüfen Sie die Zählwerte in der Matching-Historie, bevor Sie die Regel selbst ändern.
{% endhint %}

#### Spaltenvergleich (Matching-Kriterien)

Dies ist die Kern-Definition der Logik der Regel, die angibt, welche Felder zwischen den Dokumenten übereinstimmen müssen.

1. Definition der zu vergleichenden Spalten:
   * **PO-Spalten:** Das Feld, das aus den Bestelldaten entnommen wird (z. B. Zeilennummer).
   * **Extrahierte Tabellenspalten:** Das entsprechende Feld, das aus dem eingehenden Dokument (Rechnung/Auftragsbestätigung) extrahiert oder geparst wurde (z. B. `POSITION`).
2. **Vergleichstyp:** Definiert die Art der erforderlichen Übereinstimmung (z. B. Tt für Text-/Stringvergleich, der eine genaue Zeichen-für-Zeichen-Übereinstimmung erfordert; # für numerischen Vergleich).
3. **Toleranz erlauben:** Für numerische Felder (Menge, Preis) weist diese Option das System an, die zuvor definierte globale Standardtoleranz anzuwenden. Ist diese Option _nicht_ aktiviert, müssen die Werte exakt übereinstimmen.
4. **Im manuellen Abgleich ignorieren:** Wenn aktiviert, wird dieses Kriterium bei manueller Intervention gelockert. Dies ist nützlich für Felder wie Beschreibungen oder interne Referenzen, die leicht variieren können, sodass der Benutzer kleinere, nicht kritische Abweichungen übergehen kann.

**Welche Spalten können verglichen werden**

| Spalte                          | Dokumentenseite                          | Bestellseite                            | Hinweis                                                                                                                                                                                                                         |
| ------------------------------- | --------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zeilennummer                   | `POSITION`                             | `line_number`                          | Text, exakt. Nur sinnvoll, wenn der Lieferant die Bestellpositionsnummern auf dem Dokument aufdruckt.                                                                                                                            |
| Artikelkennzeichen             | `ITEM_IDENTIFIER`                      | `item_identifier`                      | Text, exakt. Artikelnummer oder Lieferantenartikelnummer, auch über die [Lieferantenartikelnummernzuordnung](supplier-item-number-map-admin-documentation.md).                                                                   |
| Effektive normalisierte Menge | `QUANTITY_EFFECTIVE_NORMALIZED`        | `quantity_effective_normalized`        | Numerisch. Die Menge, die durch **Match Quantity On** ausgewählt wurde, umgerechnet in dieselbe Einheit auf beiden Seiten (Einheitenumrechnung, „pro“-Mengen).                                                                    |
| Effektiver normalisierter Stückpreis | `UNIT_PRICE_EFFECTIVE_NORMALIZED`      | `unit_price_effective_normalized`      | Numerisch. Der Stückpreis pro Einheit nach Rabatten und nach **Unit Price Per** — und, falls [Berechnung des PO-Stückpreises](calculate-po-unit-price.md) aktiviert ist, der aus dem Bestellpositionsbetrag und der Menge berechnete Preis. |
| Nettobetrag                   | `NET_AMOUNT`                           | `total_amount`                         | Numerisch. Wird von Match-on-Total-Regeln verwendet.                                                                                                                                                                            |

**Beispiel: Strenge PO-Matching-Regel (`DefaultRule#1`)**

Eine typische strenge Regel kombiniert obligatorische Identitätsprüfungen mit Wertprüfungen:

* **Obligatorische Identität:** Zeilennummer und Artikelkennzeichen müssen exakt übereinstimmen (Textvergleich, keine Toleranz).
* **Wertprüfungen:** Effektive normalisierte Menge und effektiver normalisierter Stückpreis müssen übereinstimmen (numerischer Vergleich, Toleranz erlaubt). Nur wenn alle vier Kriterien erfüllt sind (mit Toleranz für Werte), wird ein automatischer Abgleich durchgeführt.

***

## Das Standardregelwerk

Jede Organisation startet mit demselben Standardregelwerk. Es ist eine gute Referenz, wenn Sie eigene Regeln erstellen:

| Regel                      | Typ / Priorität               | Verglichene Spalten                                                      | Aktivierungsbedingung                                  |
| -------------------------- | ---------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------- |
| `DefaultRule#1`            | Single Match, Priorität 1    | Zeilennummer, Artikelkennzeichen, Menge (Toleranz), Stückpreis (Toleranz) | immer                                                 |
| `DefaultMultiMatchRules#1` | Multi Match, Priorität 1, Fallback | Artikelkennzeichen, Menge (Toleranz), Stückpreis (Toleranz)          | `count(po_lines) > 1` und `count(table_lines) > 1`    |
| `DefaultTotalMatchRules#1` | Match on Total, Priorität 1  | Nettobetrag ↔ Bestellsumme (keine Toleranz)                            | `count(po_lines) >= 1` und `count(table_lines) > 1`   |
| `DefaultRule#2`            | Single Match, Priorität 2, Fallback | Artikelkennzeichen, Menge (Toleranz), Stückpreis (Toleranz)          | immer                                                 |
| `DefaultRule#3`            | Single Match, Priorität 2, Fallback | Menge (Toleranz), Stückpreis (Toleranz)                              | `count(po_lines) == 1` und `count(table_lines) == 1`  |

Von oben nach unten gelesen: zuerst die strenge Regel (Zeilennummer und Artikel müssen auf dem Dokument aufgedruckt sein), dann die Fallbacks ohne Zeilennummer, dann eine letzte Möglichkeit für einzeilige Dokumente, die nur Menge und Preis vergleicht.

***

## Auswirkungen auf den PO-Matching-Prozess

Das definierte Regelwerk steuert direkt die Effizienz und Integrität des PO-Matching-Workflows:

* **Priorisierung und Fallbacks:** Die definierte Priorität stellt sicher, dass das System zuerst die zuverlässigsten Matching-Methoden versucht. Wenn die strengen, hochprioritären Regeln fehlschlagen, greift das System auf breitere Regeln zurück, um die Anzahl der Ausnahmen, die an Benutzer weitergeleitet werden, zu minimieren.
* **Steuerung der Match-Qualität:** Strengere Regeln (die genauere Übereinstimmungen und weniger Toleranz erfordern) führen zu weniger, aber sehr zuverlässigen automatischen Übereinstimmungen. Lockerere Regeln erhöhen die Rate der automatischen Übereinstimmungen, erhöhen jedoch das Risiko von Fehlalarmen.
* **Ausnahmebehandlung (Manueller Abgleich):** Durch die Aktivierung von Regeln für den manuellen Abgleich bietet das System strukturierte Optionen für Benutzer. Wenn eine Transaktion die Kriterien für den automatischen Abgleich nicht erfüllt, wird sie zur Ausnahme. Der Benutzer kann dann versuchen, die Ausnahme durch Anwendung einer vordefinierten manuellen Regel zu lösen, die gelockerte Kriterien haben kann (z. B. Ignorieren einer kleinen Textabweichung gemäß der Einstellung „Im manuellen Abgleich ignorieren“).

## Weitere Einflussfaktoren auf das Ergebnis

* **Wann der Abgleich läuft:** Während der Dokumentenverarbeitung, wenn ein Benutzer auf **Auto PO Match** klickt, und **bei jedem Speichern**, bei dem sich die Bestellnummer geändert hat oder zuvor nie abgefragt wurde (zum Beispiel wenn Stammdaten sie nachträglich gefüllt haben). Ein Speichern überschreibt niemals einen bereits bestehenden Abgleich.
* **[Transformationsregeln](../../transformation-rules.md)** laufen vor dem Abgleich und können die Positionen verändern — und damit die Zeilenzahlen, auf die sich die Aktivierungsbedingungen beziehen. Eine Tabellenregel, die die Positionen neu aufbaut, behält einen bestehenden Abgleich bei, solange die Positionen gleich bleiben; ersetzt sie abgeglichene Positionen, wird der Abgleich gelöscht und der Name der Regel als Grund angezeigt.
* **[Berechnung des PO-Stückpreises](calculate-po-unit-price.md)** ändert, welchen Stückpreis die Regeln auf der Bestellseite vergleichen.
* **[Toleranzeinstellungen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** und **[deaktivierte Status](purchase-order-disable-statuses.md)** bestimmen, wie streng der Vergleich ist und welche Bestellpositionen überhaupt angeboten werden.

## Fehlerbehebung

| Symptom                                                        | Was zu prüfen ist                                                                                                                                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| „Keine Übereinstimmung“, obwohl alle Werte übereinstimmen      | Öffnen Sie die Matching-Historie: Welche Regel lief, bei welcher Spalte schlug sie fehl (die Abweichung wird pro Spalte angezeigt), wurde die Regel durch eine Aktivierungsbedingung übersprungen? |
| Stückpreis stimmt genau um den Steuersatz nicht überein       | Die Bestellsumme enthält Steuer; aktivieren Sie [Berechnung des PO-Stückpreises](calculate-po-unit-price.md) (erst Nettobetrag) oder vergleichen Sie den Zeilennettobetrag.                          |
| Eine Match-on-Total-Regel läuft nie                            | Ihre Aktivierungsbedingung erfordert mehr als eine Dokumentposition. Setzen Sie `[[count(table_lines)]] >= 1` oder falten Sie die Positionen nicht mit einer Transformationsregel zusammen.         |
| Das Regelwerk hat überhaupt keine Wirkung                      | **PO match server side** ist für den Dokumenttyp deaktiviert oder das geänderte Regelwerk ist noch ein Entwurf — aktivieren Sie die Version.                                                      |

***

## PO-Matching-Regeln anpassen

Um die PO-Matching-Regeln zu bearbeiten, kann die Standardversion durch Klicken auf **„Versionierung konfigurieren“** geklont werden, indem die Option **„Als Entwurf klonen“** aus den verfügbaren Kartenoptionen verwendet wird.

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>