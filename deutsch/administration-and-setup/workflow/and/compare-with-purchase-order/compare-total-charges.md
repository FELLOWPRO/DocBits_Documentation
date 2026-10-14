# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte vergleicht die Gesamtkosten in einem Dokumentfeld mit den entsprechenden Kosten in einer Bestellung. Die Karte hilft sicherzustellen, dass die Kosten im Dokument unter Berücksichtigung festgelegter Toleranzgrenzen mit denen in der Bestellung übereinstimmen. Der Vergleich kann Aktionen auslösen, wenn Abweichungen festgestellt werden, etwa das Markieren von Abweichungen zur Prüfung oder das entsprechende Anpassen der Kosten.

## **Bestandteile der Karte:**

1. **Feldname:**
   * **Beschreibung**: Gibt das Dokumentfeld an, das die Gesamtkostenwerte enthält, die mit den Kosten in der Bestellung verglichen werden.
   * **Detail**: Der Wert in diesem Feld stellt die im Dokument (z. B. Rechnung) angewendeten Gesamtkosten dar und wird mit den Kosten der Bestellung verglichen.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung fest, die auf den Vergleich zwischen den Gesamtkosten im Dokument und den Kosten in der Bestellung angewendet wird.
   * **Optionen**:
     * **Gleich (=)**: Überprüft, ob die Gesamtkosten im Dokument mit den Kosten in der Bestellung übereinstimmen.
     * **Ungleich (≠)**: Stellt sicher, dass sich die Gesamtkosten im Dokument von den Kosten in der Bestellung unterscheiden.
     * **Größer als (>)**: Überprüft, ob die Gesamtkosten im Dokument größer als die Kosten in der Bestellung sind.
     * **Größer oder gleich (≥)**: Überprüft, ob die Gesamtkosten im Dokument größer oder gleich den Kosten in der Bestellung sind.
     * **Kleiner als (<)**: Überprüft, ob die Gesamtkosten im Dokument kleiner als die Kosten in der Bestellung sind.
     * **Kleiner oder gleich (≤)**: Überprüft, ob die Gesamtkosten im Dokument kleiner oder gleich den Kosten in der Bestellung sind.
3. **Toleranzbetrag**
   * **Beschreibung**: Gibt den Toleranzschwellenwert für den Vergleich der Gesamtkosten an.
   * **Detail**: Dieser numerische Wert stellt die zulässige Abweichung der Kosten zwischen dem Dokument und der Bestellung dar.
4. **Toleranztyp:**
   * **Beschreibung**: Gibt die Art der angewendeten Toleranz an.
   * **Optionen**:
     * **Prozentsatz**: Die Toleranz wird als Prozentsatz der Bestellkosten angewendet.
     * **Wert**: Die Toleranz wird als fester numerischer Betrag angewendet.
5. **Trennzeichen:**
   * **Beschreibung**: Gibt das Trennzeichen an, das verwendet wird, um die Charge-ID am Ende des Feldnamens zu unterscheiden.
   * **Detail**: Das Trennzeichen trennt das Kostenfeld von der eindeutigen Charge-ID, die verwendet wird, um die Dokumentkosten mit den entsprechenden Kosten in der Bestellung zu verknüpfen.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System vergleicht die Gesamtkosten im Dokumentfeld mit den entsprechenden Kosten in der Bestellung auf Basis des Operators und der Toleranz. Die Toleranz wird angewendet, um zu bestimmen, ob die Differenz zwischen den beiden Kostenwerten innerhalb eines zulässigen Bereichs liegt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Stimmen die Kosten (unter Berücksichtigung der Toleranz) überein und ist die Bedingung erfüllt, wird der Workflow mit der definierten Aktion fortgesetzt, etwa der Dokumentfreigabe oder der weiteren Verarbeitung.
  * **Bedingung nicht erfüllt (False)**: Ist die Bedingung nicht erfüllt (d. h. die Kosten stimmen innerhalb der Toleranz nicht überein), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* Benutzer beginnen mit der Auswahl des Dokumentfelds, das den Gesamtkostenwert enthält. Anschließend wählen sie den Operator, um festzulegen, wie die Kosten mit den Bestellkosten verglichen werden. Danach legen die Benutzer den Toleranzbetrag und den Toleranztyp (Prozentsatz oder absolut) fest. Zuletzt geben sie das Trennzeichen und die Charge-ID an, die für den Vergleich verwendet werden.

## **Beispiel-Szenario:**

Eine Rechnung weist im Feld "Gesamtkosten" Kosten von 500 $ aus. Die entsprechenden Bestellkosten betragen 480 $, und die Toleranz ist auf 20 $ (absolute Toleranz) gesetzt. Die Karte vergleicht die Dokumentkosten mit den Bestellkosten:

* Die Gesamtkosten im Dokument liegen innerhalb der 20-$-Toleranz der Bestellung, und der Workflow wird ohne Probleme fortgesetzt.
* Überschreiten die Kosten die Toleranz, markiert der Workflow die Abweichung zur Prüfung.

## **Fazit:**

Die Workflow-Karte "Compare Total Charges" stellt sicher, dass die Kosten in Dokumenten unter Berücksichtigung festgelegter Toleranzgrenzen mit denen in Bestellungen übereinstimmen. Dies hilft Organisationen, den Prüfprozess zu automatisieren, Abweichungen frühzeitig zu erkennen und eine bessere Kontrolle über kostenbezogene Prozesse zu behalten.
