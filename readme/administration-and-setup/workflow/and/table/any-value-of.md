# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte wird verwendet, um zu validieren, ob irgendein Wert in einer bestimmten Tabellenspalte mit einem angegebenen Regex-Muster übereinstimmt. Stimmt ein einzelner Eintrag in der Spalte mit dem Muster überein, wird der Workflow fortgesetzt, wodurch sie sich ideal für Anwendungsfälle eignet, in denen bereits eine einzige Übereinstimmung die nächsten Schritte im Prozess auslöst.

## **Funktionalität:**

* **Validierung mit Regex-Muster:** Diese Karte prüft, ob irgendein Wert in einer bestimmten Tabellenspalte mit dem angegebenen regulären Ausdruck übereinstimmt. Die Karte wird ausgelöst und lässt den Workflow fortfahren, wenn mindestens ein Eintrag in der Spalte die Bedingung erfüllt.
* **Operator:** Benutzer definieren die Spalte und geben das Regex-Muster an. Die verfügbare Bedingung umfasst:
  * **Matches Regex Pattern:** Überprüft, ob mindestens ein Wert in der angegebenen Spalte mit dem Regex-Muster übereinstimmt.
* **Tabellen- und Spaltenauswahl:** Benutzer geben die Tabelle und die Spalte an, die sie auf Regex-Muster-Übereinstimmungen prüfen möchten.

## **Verwendung:**

Diese Karte ist besonders nützlich für Szenarien, in denen eine Tabelle Daten enthält, die bestimmte Übereinstimmungen erfordern könnten, etwa die Validierung von E-Mail-Adressen, Rechnungsnummern oder Produkt-IDs. Sie stellt sicher, dass Workflows fortfahren, wenn irgendein relevanter Eintrag dem definierten Muster entspricht, ohne dass jeder Eintrag geprüft werden muss.

## **Beispiel-Szenario:**

* Ein Benutzer stellt die Karte so ein, dass sie Einträge in der Spalte "Email Address" der Tabelle "Customers" prüft, und verwendet ein Regex-Muster für gültige E-Mail-Formate. Stimmt mindestens eine E-Mail-Adresse in der Spalte mit dem Muster überein, löst die Karte den nächsten Workflow-Schritt aus und stellt so sicher, dass das System den gültigen Eintrag verarbeitet.

Durch die Verwendung der Karte "Regex Pattern Matching" können Organisationen Workflows auf Basis dynamischer, musterbasierter Validierungen automatisieren, Prozesse optimieren und sicherstellen, dass nur relevante Einträge weitere Aktionen auslösen.
