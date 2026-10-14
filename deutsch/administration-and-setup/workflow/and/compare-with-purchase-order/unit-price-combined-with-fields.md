# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob der Stückpreis in Kombination mit einem angegebenen Feldwert (etwa Menge, Rabatt oder Zusatzkosten) eine definierte Bedingung erfüllt. Die Karte vergleicht den Stückpreis und den Feldwert mit einem angegebenen Schwellenwert, um sicherzustellen, dass die Preisgestaltung den Erwartungen entspricht. Dieser Vergleich kann Aktionen auf Basis bestimmter Bedingungen auslösen, etwa das Markieren von Abweichungen oder die Automatisierung von Freigabeprozessen in Beschaffungs- oder Wareneingangs-Workflows.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt das Dokumentfeld an, das den mit dem Stückpreis zu kombinierenden Wert enthält.
   * **Detail:** Dieser muss exakt mit dem Bezeichner des ersten Feldes innerhalb des Dokuments übereinstimmen.
2. **Operator**
   * **Beschreibung:** Legt die Bedingung fest, die auf den Vergleich zwischen dem kombinierten Wert und dem angegebenen Wert angewendet wird.
   * **Optionen:**
     * **Gleich (=):** Prüft, ob der kombinierte Wert aus Stückpreis und Feld mit dem angegebenen Wert übereinstimmt.
     * **Ungleich (≠):** Stellt sicher, dass sich der kombinierte Wert aus Stückpreis und Feld vom angegebenen Wert unterscheidet.
     * **Größer als (>):** Überprüft, ob der kombinierte Wert größer als der angegebene Wert ist.
     * **Größer oder gleich (≥):** Prüft, ob der kombinierte Wert größer oder gleich dem angegebenen Wert ist.
     * **Kleiner als (<):** Überprüft, ob der kombinierte Wert kleiner als der angegebene Wert ist.
     * **Kleiner oder gleich (≤):** Prüft, ob der kombinierte Wert kleiner oder gleich dem angegebenen Wert ist.
3. **Wert**
   * **Beschreibung:** Gibt den Wert an, mit dem der kombinierte Wert aus Stückpreis und Feld verglichen wird.
   * **Detail:** Der Wert muss ein numerischer Wert sein.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System wertet den kombinierten Wert aus Stückpreis und Feld auf Basis des ausgewählten Operators aus und vergleicht ihn mit dem angegebenen Wert. Das Ergebnis dieser Auswertung bestimmt, ob die Bedingung erfüllt oder nicht erfüllt ist.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Ergibt der Vergleich „wahr“ (z. B. übersteigt der kombinierte Wert den angegebenen Wert), fährt der Workflow mit der True-Bedingung fort. Dies kann Aktionen wie Freigabe, Dokumentweiterleitung oder das Anwenden von Verarbeitungsregeln auslösen.
  * **Bedingung nicht erfüllt (False):** Ergibt der Vergleich „falsch“ (z. B. erfüllt der kombinierte Wert die Bedingung nicht), fährt der Workflow mit der False-Bedingung fort. Dies kann eine Benachrichtigung auslösen, das Dokument zur manuellen Prüfung senden oder den Workflow stoppen.

## **Einrichtung und Konfiguration:**

* Benutzer beginnen mit der Auswahl des oder der Dokumentfelder, die den oder die mit dem Stückpreis zu kombinierenden Werte enthalten. Nach der Auswahl des Feldes wählen sie den passenden Operator, um festzulegen, wie der kombinierte Wert mit dem angegebenen Wert verglichen wird. Anschließend können sie den Wert festlegen.

## **Beispiel-Szenario:**

* Eine Rechnung führt 50 Einheiten eines Produkts zu je 20 $ auf, insgesamt 1000 $. Das zugehörige Dokument hat ein Mengenfeld mit dem Wert 10. Mit dem Operator "Größer als" vergleicht die Karte den kombinierten Wert aus Stückpreis (20 $) und Menge (10), der 200 $ ergibt. Die Karte prüft, ob der kombinierte Wert größer als 150 $ (der angegebene Wert) ist. Da der kombinierte Wert von 200 $ größer ist als der Schwellenwert von 150 $, fährt der Workflow fort und löst eine Freigabe für das Dokument aus.

## **Fazit:**

Die Workflow-Karte "Unit Price Combined with Fields" stellt sicher, dass Preisbedingungen erfüllt werden, indem sie den kombinierten Wert aus Stückpreis und einem angegebenen Feld auswertet. Durch die Automatisierung dieses Vergleichs können Organisationen Konsistenz sicherstellen und Abweichungen bei Preisen oder Mengen markieren, bevor mit der Freigabe fortgefahren wird, und so Beschaffungs- und Finanzprozesse optimieren.
