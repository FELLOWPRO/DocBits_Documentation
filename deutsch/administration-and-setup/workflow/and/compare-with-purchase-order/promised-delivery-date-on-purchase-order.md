# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Diese DocBits-Karte ist darauf ausgelegt, den präzisen Vergleich der zugesagten Lieferdaten auf Bestellungen mit den für Positionen in einer Tabelle angegebenen Lieferdaten zu ermöglichen. Durch die Integration eines Toleranzwerts sorgt die Karte für Flexibilität bei der Überwachung von Lieferterminen und hilft so, die Genauigkeit der Bestandsplanung und die Kundenzufriedenheit zu erhalten.

## **Bestandteile der Karte**

1. **Operator**
   * **Beschreibung:** Legt die Bedingung fest, die zum Vergleich der Lieferdaten angewendet wird.
   * **Optionen:**
     * **Gleich (=):** Prüft, ob das zugesagte Lieferdatum der Position mit dem Lieferdatum der Bestellung übereinstimmt.
     * **Ungleich (≠):** Stellt sicher, dass das zugesagte Lieferdatum der Position nicht mit dem Datum auf der Bestellung übereinstimmt.
     * **Größer als (>):** Überprüft, ob das zugesagte Lieferdatum der Position später ist als das Lieferdatum der Bestellung.
     * **Größer oder gleich (≥):** Prüft, ob das zugesagte Lieferdatum der Position dem Lieferdatum der Bestellung entspricht oder später ist.
     * **Kleiner als (<):** Bestätigt, ob das zugesagte Lieferdatum der Position früher ist als das Lieferdatum der Bestellung.
     * **Kleiner oder gleich (≤):** Überprüft, ob das zugesagte Lieferdatum der Position dem Lieferdatum der Bestellung entspricht oder früher ist.
2. **Wert**
   * **Beschreibung:** Gibt eine zulässige Fehlertoleranz beim Vergleich der Lieferdaten an.
   * **Detail:** Benutzer legen die Anzahl der Tage fest, um die das Lieferdatum der Position vom zugesagten Lieferdatum abweichen darf.

## **Funktionalität**

* **Bedingungsauswertung:**\
  Die Karte berechnet die Differenz zwischen dem zugesagten Lieferdatum der Bestellung und den Lieferdaten der Positionen in der Tabelle. Anschließend wird der ausgewählte Operator angewendet, um zu bestimmen, ob die Bedingung erfüllt ist.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Liegt die Differenz des Lieferdatums innerhalb des Toleranzbereichs und entspricht der durch den Operator festgelegten Bedingung, wird der Workflow fortgesetzt.
  * **Bedingung nicht erfüllt (False):** Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration**

* Der Operator wird ausgewählt, um die gewünschte Vergleichsbedingung festzulegen, etwa gleich, größer als oder kleiner als. Zuletzt geben Benutzer einen Toleranzwert in Tagen an, der kleine Abweichungen beim Vergleich zulässt, ohne Warnungen auszulösen.

## **Beispiel-Szenario**

* Eine Bestellung gibt ein zugesagtes Lieferdatum vom 1. Dezember an. Eine Position in der Tabelle hat ein zugesagtes Lieferdatum vom 3. Dezember. Bei einem auf 2 Tage gesetzten Toleranzwert und dem ausgewählten Operator **Gleich (≥)** betrachtet die Karte das Lieferdatum als innerhalb des zulässigen Bereichs. Es wird keine Warnung ausgelöst, sodass geringfügige Abweichungen toleriert werden, ohne den Betrieb zu stören.

## **Fazit**

Die Karte "Promised Delivery Date Comparison" hilft, Lieferkettenprozesse zu optimieren, indem sie eine präzise Überwachung von Lieferterminen ermöglicht. Mit ihrer Fähigkeit, Toleranzen und flexible Vergleichsoperatoren einzubeziehen, stellt sie die Einhaltung von Liefererwartungen sicher und vermeidet gleichzeitig unnötige Warnungen bei geringfügigen Abweichungen. Dies verbessert das Lieferantenmanagement und die Workflow-Effizienz insgesamt.
