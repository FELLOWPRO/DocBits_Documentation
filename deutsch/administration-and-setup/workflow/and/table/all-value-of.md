# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte wird verwendet, um zu validieren, ob **alle Werte** in einer bestimmten Tabellenspalte mit einem angegebenen Regex-Muster übereinstimmen. Damit der Workflow fortgesetzt wird, muss jeder Eintrag in der Spalte die Bedingung erfüllen, wodurch sich diese Karte ideal eignet, um Konsistenz und Datenintegrität über alle Einträge hinweg sicherzustellen.

## **Funktionalität:**

* **Validierung mit Regex-Muster:** Diese Karte prüft, ob **alle Werte** in einer angegebenen Tabellenspalte mit dem angegebenen regulären Ausdruck übereinstimmen. Der Workflow wird nur fortgesetzt, wenn jeder Eintrag in der Spalte die Bedingung erfüllt.
* **Operator:** Benutzer definieren die Spalte und geben das Regex-Muster an. Die verfügbare Bedingung umfasst:
  * **Matches Regex Pattern:** Überprüft, ob jeder Wert in der angegebenen Spalte mit dem Regex-Muster übereinstimmt.
* **Tabellen- und Spaltenauswahl:** Benutzer geben die Tabelle und die Spalte an, die sie auf vollständige Regex-Muster-Übereinstimmungen prüfen möchten.

## **Verwendung:**

Diese Karte eignet sich ideal für Fälle, in denen Datenuniformität erforderlich ist, etwa um sicherzustellen, dass alle Telefonnummern, Produkt-IDs oder andere Feldeinträge einem bestimmten Format entsprechen. Sie stellt sicher, dass Workflows nur dann fortfahren, wenn jeder relevante Eintrag dem Muster entspricht.

## **Beispiel-Szenario:**

* Ein Benutzer stellt die Karte so ein, dass sie die Spalte "Phone Number" in der Tabelle "Contacts" prüft, und verwendet ein Regex-Muster zur Validierung von Telefonnummernformaten. Stimmt jeder Telefonnummerneintrag in der Spalte mit dem Muster überein, löst die Karte den nächsten Schritt im Workflow aus und bestätigt so eine einheitliche Datenformatierung.

Durch die Verwendung der Karte "All Values Regex Pattern Matching" können Organisationen strenge Datenstandards durchsetzen und die Workflow-Genauigkeit verbessern, indem sichergestellt wird, dass jeder Eintrag in einer angegebenen Spalte das erforderliche Format erfüllt, bevor fortgefahren wird.
