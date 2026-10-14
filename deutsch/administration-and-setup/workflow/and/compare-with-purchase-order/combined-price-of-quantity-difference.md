# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**:

Diese Workflow-Karte wertet den kombinierten Preis einer Mengendifferenz aus und vergleicht ihn mit einem angegebenen Wert. Sie hilft, Aktionen auf Basis von Preis- und Mengenabweichungen über zusammengehörige Dokumente hinweg zu automatisieren und verbessert so Beschaffungs- und Wareneingangs-Workflows. **Version 4** erweitert diese Funktionalität, indem sie Vergleiche zwischen verschiedenen Entitäten wie der Bestellung, den erhaltenen Mengen und dem Dokument selbst ermöglicht und so mehr Flexibilität und Kontrolle in den Workflow bringt.

## **Bestandteile der Karte**:

1. **Operator**:&#x20;
   * **Beschreibung:** Die Bedingung für den Vergleich des kombinierten Preises mit einem angegebenen Wert.
   * **Optionen:**
     * **Gleich (=)**: Prüft, ob der kombinierte Preis mit dem angegebenen Wert übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich der kombinierte Preis vom angegebenen Wert unterscheidet.
     * **Größer als (>)**: Überprüft, ob der kombinierte Preis größer als der angegebene Wert ist.
     * **Größer oder gleich (≥)**: Prüft, ob der kombinierte Preis größer oder gleich dem angegebenen Wert ist.
     * **Kleiner als (<)**: Überprüft, ob der kombinierte Preis kleiner als der angegebene Wert ist.
     * **Kleiner oder gleich (≤)**: Prüft, ob der kombinierte Preis kleiner oder gleich dem angegebenen Wert ist.
2. **Wert**:&#x20;
   * **Beschreibung:** Gibt den Wert an, mit dem der kombinierte Preis der Mengendifferenz verglichen wird.
   * **Detail:** Der Wert muss ein numerischer Wert sein.

## **Zusätzliche Komponenten in Version 4**:

* **Vergleichstyp**: Wählt die zu vergleichenden Entitäten aus. Die Optionen umfassen:
  * **Purchase Order to Document**: Vergleicht die Mengen und Preise zwischen der Bestellung und dem zugehörigen Dokument.
  * **Received to Document**: Vergleicht die erhaltenen Mengen mit den Mengen im Dokument.
  * **Purchase Order to Received**: Vergleicht die Bestellmengen mit den erhaltenen Mengen.

## **Funktionalität**:

* **Bedingungsauswertung**: Berechnet den kombinierten Preis, indem die Mengendifferenz mit dem Preis pro Einheit multipliziert wird, und vergleicht ihn mithilfe des ausgewählten Operators mit dem angegebenen Wert.\
  **Version 4** fügt die Option hinzu, je nach Benutzerkonfiguration zusätzliche Entitäten zu vergleichen, etwa Bestellung zu Erhalten oder Bestellung zu Dokument.
* **Ausführung der Aktion**: Abhängig davon, ob der kombinierte Preis die angegebene Bedingung erfüllt, wird der Workflow mit True- oder False-Bedingungen fortgesetzt, um Aktionen auszulösen oder den Workflow anzuhalten. **Version 4** ermöglicht außerdem eine dynamischere Aktionsausführung, bei der der Bedingungstyp (z. B. Bestellung zu Erhalten) den nächsten Schritt beeinflusst.

## **Einrichtung und Konfiguration**:

* **Version 3**: Benutzer konfigurieren die Karte, indem sie die Dokumentfelder für die Mengendifferenz und den Preis pro Einheit auswählen. Anschließend wird der Operator gewählt, um festzulegen, wie der kombinierte Preis mit dem angegebenen Wert verglichen wird. Schließlich legen die Benutzer die Fortsetzungsbedingung (True oder False) fest, die den nächsten Schritt im Workflow bestimmt.
* **Version 4**: Zusätzlich zur Konfiguration aus **Version 3** haben Benutzer die Option, den **Vergleichstyp** zu konfigurieren. Dieser legt fest, welche Entitäten verglichen werden, etwa **Purchase Order to Document**, **Received to Document** oder **Purchase Order to Received**.

## **Beispiel-Szenario**:

* Eine Rechnung weist 50 Einheiten eines Produkts zu je 100 $ aus, insgesamt 5000 $. Die zugehörige Bestellung autorisierte einen Einkauf von 4500 $ für 45 Einheiten. Die Mengendifferenz beträgt 5 Einheiten, und der kombinierte Preis der Differenz beträgt 500 $. Die Karte vergleicht die Bestellmenge (45 Einheiten) mit der erhaltenen Menge (50 Einheiten) und prüft, ob der kombinierte Preis größer als 400 $ (der angegebene Wert) ist. Mit dem Operator **Größer als (>)** erkennt die Karte die Abweichung und markiert sie zur Prüfung durch das Finanzteam.

## **Fazit**:

**Version 3** der Workflow-Karte "Combined Price of Quantity Difference" bietet einen unkomplizierten Ansatz, um Mengenabweichungen zu vergleichen und Aktionen auf Basis von Preisschwellen auszulösen.\
**Version 4** erweitert diese Funktionalität, indem sie Vergleiche zwischen verschiedenen Entitäten (Bestellung, Erhalten, Dokument) ermöglicht und so mehr Flexibilität und Kontrolle über den Workflow bietet. Organisationen können nun komplexere Szenarien automatisieren und eine engere Kontrolle über ihre Beschaffungs- und Wareneingangsprozesse durchsetzen.
