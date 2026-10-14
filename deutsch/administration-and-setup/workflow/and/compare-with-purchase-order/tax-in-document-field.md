# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob der Steuerwert in einem Dokumentfeld mit dem Steuerwert in einer Bestellung übereinstimmt, wobei Toleranzen auf Basis der Charge-ID berücksichtigt werden. Die Karte vergleicht diese beiden Steuerwerte (einen aus dem Dokumentfeld und einen aus der Bestellung) und prüft, ob sie eine angegebene Bedingung erfüllen (z. B. gleich, größer als, kleiner als usw.). Dies hilft sicherzustellen, dass Steuerwerte konsistent sind, und markiert Abweichungen zur weiteren Prüfung oder Freigabe in Beschaffungs-Workflows.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung**: Gibt das Dokumentfeld an, das den mit dem Steuerwert in der Bestellung zu vergleichenden Steuerwert enthält.
   * **Detail**: Dieses Feld muss exakt mit dem Bezeichner für den Steuerwert im Dokument übereinstimmen.
2. **Operator**
   * **Beschreibung**: Legt die Bedingung fest, die auf den Vergleich zwischen dem Steuerwert des Dokuments und dem Steuerwert der Bestellung angewendet wird.
   * **Optionen**:
     * **Gleich (=)**: Prüft, ob die Steuer im Dokumentfeld mit der Steuer in der Bestellung übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich die Steuer im Dokumentfeld von der Steuer in der Bestellung unterscheidet.
     * **Größer als (>)**: Überprüft, ob die Steuer im Dokumentfeld größer als die Steuer in der Bestellung ist.
     * **Größer oder gleich (≥)**: Prüft, ob die Steuer im Dokumentfeld größer oder gleich der Steuer in der Bestellung ist.
     * **Kleiner als (<)**: Überprüft, ob die Steuer im Dokumentfeld kleiner als die Steuer in der Bestellung ist.
     * **Kleiner oder gleich (≤)**: Prüft, ob die Steuer im Dokumentfeld kleiner oder gleich der Steuer in der Bestellung ist.
3. **Stammdatentabelle**
   * **Beschreibung**: Die Tabelle, die die Bestelldetails einschließlich der Charge-ID und der Steuerwerte enthält.
   * **Detail**: Diese Tabelle muss einen Verweis auf die Charge-ID enthalten, die mit dem Steuerwert der Bestellung verknüpft ist.
4. **Toleranzbetrag**
   * **Beschreibung**: Der Schwellenbetrag, innerhalb dessen die Steuerwerte variieren dürfen. Er wird verwendet, um geringfügige Abweichungen bei Steuerberechnungen zu berücksichtigen.
   * **Detail**: Der Toleranzbetrag sollte ein numerischer Wert sein, der die maximal zulässige Differenz zwischen den Steuerwerten definiert.
5. **Toleranztyp**
   * **Beschreibung**: Gibt die Art der angewendeten Toleranz an, entweder absolut oder prozentual.
   * **Optionen**:
     * **Wert**: Die Toleranz ist ein fester numerischer Wert.
     * **Prozentsatz**: Die Toleranz wird als Prozentsatz des Steuerwerts berechnet.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System wertet aus, ob der Steuerwert im Dokumentfeld die angegebene Bedingung erfüllt, wenn er mit dem Steuerwert in der Bestellung verglichen wird (mit dem Charge-ID-Verweis aus der Stammdatentabelle). Der Toleranzbetrag und -typ werden bei dieser Auswertung berücksichtigt, um geringfügige Unterschiede bei Steuerberechnungen zuzulassen.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Erfüllt die Steuer im Dokumentfeld die Bedingung im Vergleich zur Steuer der Bestellung (innerhalb von Toleranzbetrag und -typ), wird der Workflow fortgesetzt.
  * **Bedingung nicht erfüllt (False)**: Erfüllt die Steuer im Dokumentfeld die Bedingung nicht (entweder nicht innerhalb des Toleranzbereichs oder der Vergleich schlägt fehl), wird der Workflow gestoppt.

## **Einrichtung und Konfiguration:**

* Benutzer müssen das Dokumentfeld auswählen, das den zu vergleichenden Steuerwert enthält. Anschließend wählen sie den Operator für die Art des Vergleichs (z. B. gleich, größer als). Danach müssen Benutzer den Verweis auf die Stammdatentabelle angeben und den Toleranzbetrag und -typ festlegen, um geringfügige Steuerabweichungen zu berücksichtigen.

## **Beispiel-Szenario:**

* Eine Rechnung weist einen Steuerbetrag von 100 $ aus. Die entsprechende Bestellung, die in der Stammdatentabelle gefunden wird, gibt einen Steuerwert von 95 $ an. Mit dem Operator "Größer als" vergleicht das System den Steuerwert des Dokuments (100 $) mit dem Steuerwert der Bestellung (95 $) bei einer Toleranz von 10 $ (absoluter Toleranztyp). Da die Differenz von 5 $ innerhalb des Toleranzbereichs liegt, wird der Workflow fortgesetzt, ohne Warnungen auszulösen.

## **Fazit:**

Die Workflow-Karte "Tax in Document Field Comparison" stellt sicher, dass die Steuerwerte in Dokumenten mit den Bestelldetails übereinstimmen, und lässt dabei geringfügige Abweichungen auf Basis festgelegter Toleranzen zu. Durch die Automatisierung dieser Prüfung können Organisationen Fehler bei Steuerberechnungen minimieren und Beschaffungsprozesse optimieren, wodurch der Bedarf an manuellen Eingriffen oder Freigaben reduziert wird.
