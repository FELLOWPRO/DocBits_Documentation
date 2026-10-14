# Items Have Shelf Life

<figure><img src="../../../../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte überprüft, ob Artikel in einem Datensatz angegebene Bedingungen auf Basis ihrer Haltbarkeit erfüllen. Die Karte ermöglicht es Benutzern, zwischen "any" oder "all" Artikeln für die Validierung zu wählen, und unterstützt verschiedene Vergleichsoperatoren. Dies eignet sich ideal für Szenarien, in denen Workflow-Entscheidungen von der Haltbarkeit der Artikel abhängen, etwa Qualitätskontrolle, Bestandsmanagement oder Compliance-Prüfungen.

## **Funktionalität:**

* **Haltbarkeitsvalidierung:** Diese Karte prüft die Haltbarkeit von Artikeln anhand einer angegebenen Bedingung. Benutzer können wählen, ob sie **irgendeinen** Artikel oder **alle** Artikel im Datensatz validieren, und verschiedene Vergleichsoperatoren anwenden, um die Bedingung zu definieren.
* **Artikelauswahl:** Benutzer können wählen zwischen:
  * **Any Item:** Die Karte wird ausgelöst, wenn mindestens ein Artikel die angegebene Haltbarkeitsbedingung erfüllt.
  * **All Items:** Die Karte wird nur ausgelöst, wenn alle Artikel die angegebene Haltbarkeitsbedingung erfüllen.
* **Operatoren:** Die folgenden Operatoren stehen zur Festlegung der Haltbarkeitsbedingung zur Verfügung:
  * **Gleich (=):** Prüft, ob die Haltbarkeit exakt dem angegebenen Wert entspricht.
  * **Ungleich (≠):** Stellt sicher, dass die Haltbarkeit nicht dem angegebenen Wert entspricht.
  * **Größer als (>):** Bestätigt, dass die Haltbarkeit größer als der angegebene Wert ist.
  * **Größer oder gleich (≥):** Stellt sicher, dass die Haltbarkeit größer oder gleich dem angegebenen Wert ist.
  * **Kleiner als (<):** Prüft, ob die Haltbarkeit kleiner als der angegebene Wert ist.
  * **Kleiner oder gleich (≤):** Stellt sicher, dass die Haltbarkeit kleiner oder gleich dem angegebenen Wert ist.



## **Verwendung:**

Diese Karte eignet sich für Qualitätskontrollteams, Bestandsverantwortliche oder Compliance-Verantwortliche, die sicherstellen müssen, dass Artikel bestimmte Haltbarkeitsanforderungen erfüllen, bevor sie mit weiteren Aktionen oder Workflows fortfahren.

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie prüft, ob **alle Artikel** eine Haltbarkeit von **größer oder gleich 30 Tagen** haben. Erfüllt jeder Artikel diese Bedingung, wird der Workflow fortgesetzt und bestätigt, dass alle Artikel eine ausreichende Haltbarkeit für den Verkauf oder die Verteilung haben.

Durch die Verwendung der Karte "Shelf Life Validation" können Organisationen Haltbarkeitsstandards durchsetzen, die Produktqualität wahren und die Workflow-Genauigkeit auf Basis der Haltbarkeitsbedingungen von Artikeln sicherstellen.
