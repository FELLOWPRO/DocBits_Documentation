# Compare In

<figure><img src="../../../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte führt einen Vergleich zwischen zwei Spalten in einer angegebenen Tabelle durch und ermöglicht es Benutzern, Bedingungen auf Basis der Werte in jeder Spalte festzulegen. Zusätzlich enthält diese Karte eine Abhängigkeitsfunktion, bei der der Vergleich nur stattfindet, wenn der Wert in einer dritten Spalte mit einem angegebenen Python-Regex-Muster übereinstimmt. Diese Einrichtung ist nützlich für bedingte Prüfungen, die von mehreren Datenpunkten innerhalb eines Datensatzes abhängen.

## **Funktionalität:**

* **Spaltenvergleich mit Abhängigkeit:** Diese Karte vergleicht Werte in zwei angegebenen Spalten auf Basis einer festgelegten Bedingung, die nur angewendet wird, wenn der Wert in einer dritten "Abhängigkeitsspalte" mit einem definierten Python-Regex-Muster übereinstimmt.
* **Operatoren:** Benutzer können die folgenden Operatoren für den Spaltenvergleich auswählen:
  * **Gleich (=):** Prüft, ob die Werte in den beiden Spalten exakt gleich sind.
  * **Ungleich (≠):** Stellt sicher, dass sich die Werte in den beiden Spalten unterscheiden.
  * **Größer als (>):** Bestätigt, dass die Werte in der ersten Spalte größer sind als die in der zweiten Spalte.
  * **Größer oder gleich (≥):** Stellt sicher, dass die Werte in der ersten Spalte größer oder gleich denen in der zweiten Spalte sind.
  * **Kleiner als (<):** Prüft, ob die Werte in der ersten Spalte kleiner sind als die in der zweiten Spalte.
  * **Kleiner oder gleich (≤):** Stellt sicher, dass die Werte in der ersten Spalte kleiner oder gleich denen in der zweiten Spalte sind.
* **Regex-Abhängigkeit:** Diese Karte enthält eine Abhängigkeitsfunktion, mit der Benutzer ein Regex-Muster für eine dritte Spalte definieren können. Die Vergleichsbedingung wird nur angewendet, wenn mindestens ein Wert in der Abhängigkeitsspalte mit dem Regex-Muster übereinstimmt.

## **Verwendung:**

Diese Karte ist besonders nützlich in Szenarien, in denen eine komplexe bedingte Logik erforderlich ist, etwa Qualitätsprüfungen, die von Beziehungen zwischen Datenpunkten abhängen, mit zusätzlichen Bedingungen auf Basis der Datenformatierung oder bestimmter Muster.

***

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie die Spalten "Quantity" und "Threshold" in einer Tabelle "Stock" mit der Bedingung **Quantity ≥ Threshold** vergleicht. Dieser Vergleich findet nur statt, wenn die Spalte "Item Code" mit dem Regex-Muster für bestimmte Codeformate übereinstimmt, etwa **^A\d{3}$** (was einen Artikelcode angibt, der mit "A" beginnt und von drei Ziffern gefolgt wird).

Durch die Verwendung der Karte "Conditional Column Comparison" können Organisationen fortgeschrittene, musterabhängige Vergleiche innerhalb von Datensätzen erstellen und so eine feinabgestimmte Datenverarbeitung und höhere Genauigkeit in bedingten Workflows ermöglichen.
