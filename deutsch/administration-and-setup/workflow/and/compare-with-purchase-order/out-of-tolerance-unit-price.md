# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob der kombinierte Wert aus Stückpreisen und einem angegebenen Feld einen definierten Schwellenwert über- oder unterschreitet. Sie hilft, Abweichungen zu erkennen, bei denen die Stückpreise in Kombination mit anderen Feldern außerhalb der Toleranz liegen, stellt sicher, dass die Preisbedingungen den Erwartungen entsprechen, und markiert etwaige Probleme zur Prüfung oder weiteren Bearbeitung.

## **Bestandteile der Karte:**

1. **Feldname:**
   * **Beschreibung**: Gibt das Dokumentfeld an, das den mit dem Stückpreis zu kombinierenden Wert enthält.
   * **Detail**: Der Wert in diesem Feld wird mit dem Stückpreis kombiniert, um den kombinierten Gesamtwert für den Vergleich zu bilden.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung für den Vergleich des kombinierten Werts aus Stückpreis und Feldwert mit dem angegebenen Wert fest.
   * **Optionen**:
     * **Gleich (=)**: Überprüft, ob der kombinierte Wert aus Stückpreis und Feld mit dem angegebenen Wert übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich der kombinierte Wert aus Stückpreis und Feld vom angegebenen Wert unterscheidet.
     * **Größer als (>)**: Überprüft, ob der kombinierte Wert aus Stückpreis und Feld den angegebenen Wert übersteigt.
     * **Größer oder gleich (≥)**: Überprüft, ob der kombinierte Wert aus Stückpreis und Feld größer oder gleich dem angegebenen Wert ist.
     * **Kleiner als (<)**: Überprüft, ob der kombinierte Wert aus Stückpreis und Feld kleiner als der angegebene Wert ist.
     * **Kleiner oder gleich (≤)**: Überprüft, ob der kombinierte Wert aus Stückpreis und Feld kleiner oder gleich dem angegebenen Wert ist.
3. **Wert:**
   * **Beschreibung**: Gibt den Wert an, mit dem der kombinierte Wert aus Stückpreis und Feld verglichen wird.
   * **Detail**: Dieser numerische Wert stellt den Schwellenwert für den Vergleich dar. Über- oder unterschreitet der kombinierte Wert aus Stückpreis und Feld diesen Wert (je nach ausgewähltem Operator), löst die Bedingung die festgelegten Aktionen aus.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System berechnet den kombinierten Wert, indem es je nach Konfiguration den Stückpreis mit dem Feldwert multipliziert oder addiert. Das Ergebnis wird anschließend mithilfe des ausgewählten Operators mit dem angegebenen Wert verglichen. Ist die Bedingung erfüllt (d. h. der kombinierte Wert liegt außerhalb der Toleranz), fährt der Workflow mit dem nächsten Schritt fort, sei es Freigabe, Ablehnung oder weitere Prüfung.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt der Vergleich „wahr“ (d. h. der kombinierte Wert erfüllt die Bedingung), löst der Workflow die mit der True-Bedingung verknüpfte Aktion aus (z. B. Freigabe oder Benachrichtigung).
  * **Bedingung nicht erfüllt (False)**: Ergibt der Vergleich „falsch“ (d. h. der kombinierte Wert erfüllt die Bedingung nicht), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* Benutzer wählen das Feld aus, das den mit dem Stückpreis zu kombinierenden Wert enthält. Anschließend wählen sie den passenden Operator, um festzulegen, wie der kombinierte Wert mit dem angegebenen Wert verglichen wird. Zuletzt legt der Benutzer den Wert fest, mit dem der kombinierte Preis verglichen wird.

## **Beispiel-Szenario:**

* Eine Rechnung führt 50 Einheiten eines Produkts zu je 30 $ auf, insgesamt 1500 $. Das zugehörige Dokument hat ein Mengenfeld mit dem Wert 10. Der kombinierte Preis wird berechnet, indem der Stückpreis (30 $) mit der Menge (10) multipliziert wird, was 300 $ ergibt. Die Karte vergleicht diesen kombinierten Wert anschließend mit einem Schwellenwert von 250 $. Mit dem Operator "Größer als" stellt die Karte fest, dass 300 $ größer als 250 $ sind, und löst einen Freigabeprozess für das Dokument aus.

## **Fazit:**

Die Workflow-Karte "Out of Tolerance Unit Prices Combined with Fields" hilft sicherzustellen, dass Preis- und Feldwerte mit den Geschäftsregeln übereinstimmen. Durch die Automatisierung dieser Prüfung können Organisationen Abweichungen frühzeitig im Prozess erkennen und so sicherstellen, dass außerhalb der Toleranz liegende Stückpreise zur Prüfung oder zur erforderlichen Maßnahme markiert werden.
