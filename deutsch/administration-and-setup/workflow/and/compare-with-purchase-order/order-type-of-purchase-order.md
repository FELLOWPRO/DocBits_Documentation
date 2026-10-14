# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, den Auftragstyp einer Bestellung mit einem angegebenen Wert zu vergleichen. Die Karte prüft, ob der Auftragstyp der Bestellung die angegebene Bedingung erfüllt (z. B. ob er gleich, ungleich, größer als ist oder eine andere Bedingung erfüllt), um sicherzustellen, dass die Bestellung korrekt klassifiziert ist. Dieser Vergleich kann Aktionen auf Basis bestimmter Bedingungen auslösen, etwa das Weiterleiten der Bestellung zur weiteren Prüfung oder Freigabe, wenn Abweichungen festgestellt werden.

## **Bestandteile der Karte:**

1. **Any/All:**
   * **Beschreibung**: Legt fest, ob die Bedingung für irgendeine oder alle im Workflow ausgewerteten Bestellungen gilt.
   * **Optionen**:
     * **Any**: Die Bedingung ist erfüllt, wenn irgendeine der Bestellungen die angegebene Bedingung erfüllt.
     * **All**: Die Bedingung ist nur erfüllt, wenn alle Bestellungen die angegebene Bedingung erfüllen.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung fest, die angewendet wird, um den Auftragstyp mit einem angegebenen Wert zu vergleichen.
   * **Optionen**:
     * **Gleich (=)**: Prüft, ob der Auftragstyp mit dem angegebenen Wert übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich der Auftragstyp vom angegebenen Wert unterscheidet.
3. **Auftragstyp:**
   * **Beschreibung**: Gibt den Wert an, mit dem der Auftragstyp der Bestellung verglichen wird.
   * **Detail**: Der Wert muss mit dem Auftragstyp oder der Klassifizierung im System übereinstimmen.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System wertet den Auftragstyp der Bestellung anhand der angegebenen Bedingung mithilfe des ausgewählten Operators aus. Stimmt der Auftragstyp mit dem angegebenen Wert überein (oder nicht überein), wird der Workflow entsprechend fortgesetzt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt die Bedingung „wahr“ (z. B. stimmt der Auftragstyp mit dem angegebenen Wert überein), wird der Workflow fortgesetzt und löst möglicherweise zusätzliche Aktionen oder Verarbeitungsschritte aus.
  * **Bedingung nicht erfüllt (False)**: Ergibt die Bedingung „falsch“ (z. B. stimmt der Auftragstyp nicht mit dem angegebenen Wert überein), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* Benutzer konfigurieren die Karte, indem sie das Auftragstyp-Feld der Bestellung auswählen und den Operator wählen, der festlegt, wie der Auftragstyp verglichen wird. Anschließend legen sie den angegebenen Wert fest und entscheiden, ob die Bedingung für irgendeine oder alle Bestellzeilen gilt.

## **Beispiel-Szenario:**

* Eine Bestellung hat den Auftragstyp "Standard". Der Workflow ist so konfiguriert, dass er prüft, ob der Auftragstyp "Urgent" ist. Mit dem Operator "Gleich" vergleicht die Karte den Auftragstyp und stellt fest, dass er nicht mit dem angegebenen Wert übereinstimmt, woraufhin der Workflow die Bestellung aufgrund der Abweichung zur Prüfung sendet.

## **Fazit:**

Die Workflow-Karte "Order Type of Purchase Order" stellt sicher, dass Bestellungen entsprechend ihrem angegebenen Auftragstyp korrekt klassifiziert werden. Durch die Automatisierung des Vergleichs von Auftragstypen können Organisationen sicherstellen, dass Bestellungen gemäß ihren erwarteten Klassifizierungen verarbeitet werden, was die Einhaltung von Vorgaben unterstützt und Beschaffungs-Workflows optimiert.
