# Berechnen Sie Spalten mit

<figure><img src="../../../../.gitbook/assets/workflow_card_calc_columns_v1-de-de.png" alt="Berechnen Sie Spalten mit, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_calc_columns_v2-de-de.png" alt="Berechnen Sie Spalten mit, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Zweck:

Diese Workflow-Karte berechnet Zeile für Zeile einen Wert aus zwei Spalten einer Tabelle auf dem Dokument und speichert das Ergebnis in einer Ergebnisspalte. Sie kann zum Beispiel verwendet werden, um Zeilensummen aus Menge und Stückpreis zu berechnen.

## Admin-Video:

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v2/de.mp4" %}

[Video mit deutschen Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v2/de.html) · [Transkript lesen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v2/de.txt)

## Bestandteile der Karte:

1. **Tabelle**
   * **Beschreibung:** Die Tabelle auf dem Dokument, in der die Berechnung ausgeführt wird.
2. **Erste Spalte**
   * **Beschreibung:** Die Spalte mit dem ersten Wert jeder Zeile.
3. **Operation**
   * **Optionen:**
     * **+** addiert den zweiten Wert zum ersten.
     * **-** subtrahiert den zweiten Wert vom ersten.
     * **\*** multipliziert die beiden Werte.
     * **/** dividiert den ersten Wert durch den zweiten.
4. **Zweite Spalte**
   * **Beschreibung:** Die Spalte mit dem zweiten Wert jeder Zeile.
5. **Ergebnisspalte**
   * **Beschreibung:** Die Spalte, in der das Ergebnis jeder Zeile gespeichert wird.
   * **Detail:** Der Name wird in Großbuchstaben gespeichert, Leerzeichen werden durch Unterstriche ersetzt (`total amount` wird zu `TOTAL_AMOUNT`). Existiert die Spalte noch nicht, fügt die Karte sie hinzu; existiert sie, werden ihre Werte ersetzt.

Die Versionen 1 und 2 der Karte haben dieselben Einstellungen und arbeiten gleich.

## Funktionalität:

* **Berechnung:** Für jede Zeile der Tabelle liest die Karte die beiden Spalten (Groß- und Kleinschreibung der Spaltennamen spielt keine Rolle), wendet die Operation an und schreibt das Ergebnis in die Ergebnisspalte. Ergebnisse werden auf vier Nachkommastellen gerundet. Anschließend wird das Dokument mit den neuen Werten gespeichert.
  * Ein leerer oder fehlender Wert gilt als `0`. Sind beide Werte einer Zeile leer, bleibt das Ergebnis dieser Zeile leer.
  * Eine Division durch null lässt das Ergebnis dieser Zeile leer.
  * Mit **+** werden zwei Werte, die keine Zahlen sind, mit einem Leerzeichen verbunden statt addiert. Bei den anderen Operationen verursacht ein Wert, der keine Zahl ist, einen Fehler, und es werden keine Ergebnisse gespeichert.
* **Ausführung der Aktion:** Sind Berechnung und Speichern erfolgreich, wird der Workflow mit den nächsten Karten fortgesetzt. Existiert die Tabelle auf dem Dokument nicht, kann ein Wert nicht berechnet oder das Dokument nicht gespeichert werden, meldet die Karte einen Fehler im Workflow-Protokoll.
* **Testkarte:** Wird die Karte mit **Testkarte** ausgeführt, wird die Berechnung nur simuliert und das Dokument nicht geändert.

## Einrichtung und Konfiguration:

* Die Karte kann als Then-Aktion aus der Kategorie **Tabelle** hinzugefügt werden. Danach werden die Tabelle, die beiden Spalten, die Operation und die Ergebnisspalte ausgewählt.
* **Beispiel:** Tabelle `INVOICE_TABLE`, `QUANTITY` **\*** `UNIT_PRICE`, Ergebnisspalte `TOTAL_AMOUNT`. Eine Zeile mit Menge 2 und Stückpreis 10 erhält 20, eine Zeile mit 3 und 4 erhält 12.
* Da ein leerer Wert als `0` gilt, ergibt ein fehlender Preis das Ergebnis `0`. Eine Prüfung, ob die Eingabespalten gefüllt sind, zum Beispiel mit einer Bedingung vor dieser Karte, kann helfen, falsche Summen zu vermeiden.
* Bei Subtraktion und Division ist die Reihenfolge der beiden Spalten wichtig.

## Fazit:

Die Workflow-Karte „Calculate Columns with“ ergänzt Tabellenzeilen automatisch um berechnete Werte. Zeilensummen und ähnliche Werte stehen den folgenden Karten und dem Export ohne manuelle Berechnung zur Verfügung.
