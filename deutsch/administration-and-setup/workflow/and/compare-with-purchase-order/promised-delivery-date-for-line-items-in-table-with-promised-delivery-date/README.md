# Zugesagtes Lieferdatum für Positionen in Tabelle mit zugesagtem Lieferdatum

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Zweck:

Diese Workflow-Karte ist darauf ausgelegt, das **zugesagte Lieferdatum von Positionen** mit dem **zugesagten Lieferdatum auf der Bestellung** zu vergleichen, wobei Vergleichsoperatoren und konfigurierbare Toleranzregeln verwendet werden. Sie ermöglicht es Workflows, termingerechte, frühe oder verspätete Lieferdaten automatisch zu erkennen und entsprechend zu reagieren.

## Bestandteile der Karte:

1. **Operator**
   * **Beschreibung:**\
     Legt fest, wie das zugesagte Lieferdatum der Position mit dem zugesagten Lieferdatum der Bestellung verglichen wird.
   * **Optionen:**
     * **Gleich (=):** Das Positionsdatum muss innerhalb des Toleranzfensters liegen.
     * **Ungleich (≠):** Das Positionsdatum muss außerhalb des Toleranzfensters liegen.
     * **Größer als (>):** Das Positionsdatum muss nach dem Toleranzfenster liegen.
     * **Größer oder gleich (≥):** Das Positionsdatum muss am oder nach dem Beginn des Toleranzfensters liegen.
     * **Kleiner als (<):** Das Positionsdatum muss vor dem Toleranzfenster liegen.
     * **Kleiner oder gleich (≤):** Das Positionsdatum muss am oder vor dem Ende des Toleranzfensters liegen.<br>
2. **Toleranztage**
   * **Beschreibung:**\
     Gibt die Anzahl der Tage an, die zur Berechnung des zulässigen Toleranzfensters um das zugesagte Lieferdatum der Bestellung verwendet werden.
   * **Detail:**\
     Dieser Wert ist eine Ganzzahl und legt fest, wie viele Tage vor und nach dem Bestelldatum bei der Validierung berücksichtigt werden.<br>
3. **Zulässige Toleranztage**
   * **Beschreibung:**\
     Legt fest, welche Wochentage bei der Berechnung der Toleranztage gezählt werden.
   * **Detail:**\
     Benutzer können bestimmte Wochentage auswählen (zum Beispiel Montag bis Freitag). Nur die ausgewählten Tage werden bei der Berechnung des Toleranzfensters einbezogen.

### Funktionalität:

* **Bedingungsauswertung:** Das System berechnet auf Basis der konfigurierten **Toleranztage** und **Zulässigen Toleranztage** ein Toleranzfenster um das zugesagte Lieferdatum der Bestellung.\
  Anschließend wird das zugesagte Lieferdatum jeder Position mithilfe des ausgewählten Operators mit diesem Fenster verglichen.
* Ausführung der Aktion:
  * **Bedingung erfüllt (True):** Liegt die Differenz des Lieferdatums innerhalb des Toleranzbereichs und entspricht der durch den Operator festgelegten Bedingung, wird der Workflow fortgesetzt.
  * **Bedingung nicht erfüllt (False):** Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

### Einrichtung und Konfiguration:

* Wählen Sie den passenden Vergleichsoperator aus.
* Geben Sie die Anzahl der Toleranztage ein.
* Wählen Sie aus, welche Wochentage als Toleranztage gezählt werden sollen.

### Fazit:

Die Workflow-Karte **Compare with Purchase Order – Promised Delivery Date for Line Items** bietet eine flexible Möglichkeit, Regeln für Lieferdaten durchzusetzen. Durch die Kombination von Operatoren mit einer wochentagsbewussten Toleranzbehandlung ermöglicht sie eine präzise Validierung von Lieferzusagen und reduziert gleichzeitig manuelle Prüfungen und Ausnahmen.
