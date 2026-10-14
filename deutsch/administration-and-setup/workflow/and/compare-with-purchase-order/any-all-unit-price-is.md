# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte wird verwendet, um den Stückpreis in einem Dokument mit dem Stückpreis in einer Bestellung zu vergleichen und so sicherzustellen, dass die Preise innerhalb definierter Toleranzgrenzen übereinstimmen. Der Vergleich kann Aktionen auslösen, wenn der Stückpreis nicht den Erwartungen entspricht. **Version 4** bietet mehr Flexibilität, indem sie es Benutzern ermöglicht, verschiedene Entitäten für den Vergleich auszuwählen, und so eine tiefere Kontrolle über Preis- und Beschaffungsprozesse gibt.

## **Bestandteile der Karte:**

1. **Any / All:**
   * **Beschreibung**: Legt fest, ob die Bedingung für irgendeinen oder alle Fälle gilt, in denen der Stückpreis verglichen wird.
   * **Optionen**:
     * **Any**: Die Bedingung ist erfüllt, wenn irgendein Stückpreis die angegebene Vergleichsbedingung erfüllt.
     * **All**: Die Bedingung ist nur erfüllt, wenn alle Stückpreise die angegebene Vergleichsbedingung erfüllen.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung für den Vergleich des Stückpreises mit dem angegebenen Wert fest.
   * **Optionen**:
     * **Gleich (=)**: Überprüft, ob der Stückpreis mit dem angegebenen Wert übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich der Stückpreis vom angegebenen Wert unterscheidet.
     * **Größer als (>)**: Überprüft, ob der Stückpreis größer als der angegebene Wert ist.
     * **Größer oder gleich (≥)**: Überprüft, ob der Stückpreis größer oder gleich dem angegebenen Wert ist.
     * **Kleiner als (<)**: Überprüft, ob der Stückpreis kleiner als der angegebene Wert ist.
     * **Kleiner oder gleich (≤)**: Überprüft, ob der Stückpreis kleiner oder gleich dem angegebenen Wert ist.

## **Zusätzliche Komponenten in Version 4:**

**Vergleichstyp:**

* **Beschreibung**: Ermöglicht es Benutzern auszuwählen, welche Entitäten zusätzlich zum Stückpreis verglichen werden.
* **Optionen**:
  * **Purchase Order to Document**: Vergleicht den Stückpreis in der Bestellung mit dem Stückpreis im Dokument.
  * **Received to Document**: Vergleicht die erhaltene Menge mit dem Stückpreis im Dokument.
  * **Purchase Order to Received**: Vergleicht den Stückpreis in der Bestellung mit der erhaltenen Menge.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System vergleicht den Stückpreis im Dokument mit dem Stückpreis in der Bestellung (oder einer anderen ausgewählten Entität in Version 4) auf Basis des ausgewählten Operators. Ist der Vergleich erfüllt, wird der Workflow gemäß den nächsten Schritten fortgesetzt und löst entweder eine Freigabe aus oder stoppt den Prozess.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt die Bedingung „wahr“ (z. B. ist der Stückpreis im Dokument größer als der angegebene Wert), wird der Workflow mit der True-Aktion fortgesetzt (z. B. Freigabe, Dokumentverarbeitung).
  * **Bedingung nicht erfüllt (False)**: Ergibt die Bedingung „falsch“ (z. B. erfüllt der Stückpreis im Dokument den Vergleich nicht), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* **Einrichtung in Version 3:** Benutzer konfigurieren die Karte, indem sie den Stückpreis im Dokument auswählen, den passenden Operator wählen, um festzulegen, wie der Stückpreis mit dem angegebenen Wert verglichen wird, und den Vergleichswert festlegen. Zusätzlich wählen Benutzer aus, ob die Bedingung für irgendeinen oder alle Fälle des Stückpreisvergleichs gilt.
* **Einrichtung in Version 4:** In Version 4 haben Benutzer die zusätzliche Option, den Vergleichstyp auszuwählen. Dadurch können sie die zu vergleichenden Entitäten festlegen, etwa Purchase Order to Document, Received to Document oder Purchase Order to Received. Dies erhöht die Flexibilität der Karte, um Stückpreise in komplexeren Szenarien zu vergleichen.

## **Beispiel-Szenario:**

*   **Beispiel Version 3:**&#x20;

    Eine Rechnung weist einen Stückpreis von 50 $ aus. Die zugehörige Bestellung hat einen Stückpreis von 45 $. Die Karte vergleicht die beiden Stückpreise mit dem Operator "Größer als". Da der Stückpreis im Dokument (50 $) größer ist als der Stückpreis in der Bestellung (45 $), löst der Workflow die True-Bedingung aus (z. B. das Dokument zur Prüfung senden).
* **Beispiel Version 4:**\
  Eine Rechnung weist einen Stückpreis von 50 $ aus, und die zugehörige Bestellung autorisierte einen Stückpreis von 45 $. Zusätzlich beträgt die erhaltene Menge 60 Einheiten. Die Karte vergleicht die erhaltene Menge mit dem Stückpreis des Dokuments unter Verwendung des Operators "Größer als". Da die erhaltene Menge (60) größer ist als der Stückpreis (50 $), löst der Workflow die True-Bedingung aus, und das Dokument wird zur weiteren Prüfung markiert.

## **Fazit:**

Version 3 der Workflow-Karte "Unit Price Comparison" ist darauf ausgelegt, sicherzustellen, dass die Stückpreise in Dokumenten mit denen in Bestellungen übereinstimmen, und löst Aktionen auf Basis definierter Bedingungen aus. Version 4 erweitert diese Funktionalität durch die Einführung komplexerer Vergleichsoptionen, etwa den Vergleich von Bestellungen mit Dokumenten, erhaltenen Mengen mit Dokumenten und Bestellungen mit erhaltenen Mengen. Diese zusätzliche Flexibilität ermöglicht es Organisationen, anspruchsvollere Preis- und Beschaffungsszenarien zu handhaben und so die Kontrolle und Genauigkeit in ihren Workflows zu verbessern.
