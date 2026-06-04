# Calculate Columns with

<figure><img src="../../../../.gitbook/assets/image (294).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Calculate Columns in Table"** wird verwendet, um Berechnungen zwischen Spalten in einer ausgewählten Tabelle durchzuführen. Sie ermöglicht es Benutzern, Spalten auszuwählen, eine mathematische Operation anzuwenden und das Ergebnis in einer angegebenen Ergebnisspalte zu speichern.

## **Bestandteile der Karte:**

1. **Tabellenname**
   * **Beschreibung:** Gibt die **Tabelle** an, in der die Spalten berechnet werden.
   * **Detail:** Zur Auswahl wird eine Dropdown-Liste aller verfügbaren **Tabellen** bereitgestellt.
2. **Spaltenname (1. Spalte)**
   * **Beschreibung:** Gibt die **erste Spalte** an, die an der Berechnung beteiligt ist.
   * **Detail:** Zur Auswahl wird eine Liste aller verfügbaren **Spalten** bereitgestellt.
3. **Operation**
   * **Beschreibung:** Legt die mathematische Operation fest, die zwischen den ausgewählten Spalten angewendet wird.
   * **Optionen:**
     * **Addieren (+):** Addiert den Wert der zweiten Spalte zum Wert der ersten Spalte.
     * **Subtrahieren (-):** Subtrahiert den Wert der zweiten Spalte vom Wert der ersten Spalte.
     * **Multiplizieren (\*):** Multipliziert den Wert in der ersten Spalte mit dem Wert in der zweiten Spalte.
     * **Dividieren (/):** Dividiert den Wert in der ersten Spalte durch den Wert in der zweiten Spalte.
4. **Spaltenname (2. Spalte)**
   * **Beschreibung:** Gibt die **zweite Spalte** an, die an der Berechnung beteiligt ist.
   * **Detail:** Zur Auswahl wird eine Liste der verfügbaren **Spalten** bereitgestellt.
5. **Ergebnisspalte**
   * **Beschreibung:** Gibt die **Spalte** an, in der das Ergebnis der Berechnung gespeichert wird.
   * **Detail:** Es wird eine Liste der verfügbaren **Spalten** bereitgestellt, in der der berechnete Wert gespeichert wird.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Spaltenberechnung:**\
  Die Karte führt die ausgewählte mathematische Operation zwischen den beiden gewählten Spalten durch.
* **Ergebnisspeicherung:**\
  Das Ergebnis der Berechnung wird in der ausgewählten **Ergebnisspalte** gespeichert.

## **Einrichtung und Konfiguration:**

* **Tabelle auswählen:**\
  Wählen Sie die **Tabelle**, in der die Spalten berechnet werden.
* **Spalten wählen:**\
  Wählen Sie die **erste Spalte** und die **zweite Spalte**, die in der Berechnung verwendet werden.
* **Operation auswählen:**\
  Wählen Sie die mathematische Operation (**Addieren (+)**, **Subtrahieren (-)**, **Multiplizieren (\*)**, **Dividieren (/)**), die zwischen den Spalten angewendet wird.
* **Ergebnisspalte auswählen:**\
  Wählen Sie die **Ergebnisspalte**, in der die Berechnung gespeichert wird.

## **Fazit:**

Die Workflow-Karte **"Calculate Columns in Table"** ermöglicht es Benutzern, dynamische Berechnungen zwischen Spalten in einer Tabelle durchzuführen und die Ergebnisse in einer festgelegten Spalte zu speichern. Die Karte bietet Flexibilität, um verschiedene mathematische Operationen anzuwenden, und stellt sicher, dass das Ergebnis in der angegebenen Spalte gespeichert wird.
