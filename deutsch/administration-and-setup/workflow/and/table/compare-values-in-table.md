# Compare values in table

<figure><img src="../../../../.gitbook/assets/image (48).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte führt auf Basis einer gewählten Bedingung einen Vergleich zwischen Werten in zwei angegebenen Spalten innerhalb einer Tabelle durch. Sie ist nützlich für Szenarien, die die Validierung von Beziehungen zwischen Datenpunkten erfordern, etwa Qualitätskontrolle, Datenkonsistenzprüfungen oder Compliance-Überprüfungen.

## **Funktionalität:**

* **Spaltenvergleich:** Diese Karte ermöglicht es Benutzern, Bedingungen festzulegen, um Werte zwischen zwei Spalten in derselben Tabelle zu vergleichen.
* **Operatoren:** Die folgenden Operatoren stehen zur Definition des Vergleichs zur Verfügung:
  * **Gleich (=):** Prüft, ob die Werte in den beiden Spalten exakt gleich sind.
  * **Ungleich (≠):** Stellt sicher, dass sich die Werte in den beiden Spalten unterscheiden.
  * **Größer als (>):** Bestätigt, dass die Werte in der ersten Spalte größer sind als die in der zweiten Spalte.
  * **Größer oder gleich (≥):** Stellt sicher, dass die Werte in der ersten Spalte größer oder gleich denen in der zweiten Spalte sind.
  * **Kleiner als (<):** Prüft, ob die Werte in der ersten Spalte kleiner sind als die in der zweiten Spalte.
  * **Kleiner oder gleich (≤):** Stellt sicher, dass die Werte in der ersten Spalte kleiner oder gleich denen in der zweiten Spalte sind.
* **Tabellen- und Spaltenauswahl:** Benutzer geben die Tabelle und die beiden Spalten an, die sie vergleichen möchten.

## **Verwendung:**

Diese Karte eignet sich ideal für Datenanalysten, Qualitätskontrollteams oder Compliance-Verantwortliche, die sicherstellen müssen, dass die Werte in einer Spalte gemäß bestimmten Regeln mit den Werten in einer anderen Spalte in Beziehung stehen, und ermöglicht so eine fortgeschrittene Datenvalidierung.

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie prüft, ob die Werte in der Spalte "Current Stock" **größer oder gleich (≥)** den Werten in der Spalte "Minimum Stock Level" in der Tabelle "Inventory" sind. Erfüllen alle Werte diese Bedingung, wird der Workflow fortgesetzt und bestätigt, dass die Lagerbestände ausreichend sind.

Durch die Verwendung der Karte "Column Value Comparison" können Organisationen Datenkonsistenz sicherstellen, Qualitätsstandards wahren und Datenbeziehungen innerhalb von Tabellen validieren.
