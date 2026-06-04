# Item Receiving Method

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte prüft, ob Artikel in einem Datensatz eine angegebene Wareneingangsmethode haben. Benutzer können wählen, ob sie **irgendeinen** Artikel oder **alle** Artikel im Datensatz auf Basis einer ausgewählten Bedingung validieren, wodurch sie sich für Szenarien eignet, in denen Workflows von den Wareneingangsmethoden der Artikel abhängen, etwa im Lieferkettenmanagement oder bei der Bestandsverfolgung.

## **Funktionalität:**

* **Validierung der Wareneingangsmethode:** Diese Karte überprüft die Wareneingangsmethode von Artikeln anhand einer angegebenen Bedingung. Benutzer können zwischen **irgendeinem** Artikel oder **allen** Artikeln im Datensatz wählen und die Bedingung als **gleich** oder **ungleich** festlegen.
* **Artikelauswahl:** Benutzer können angeben:
  * **Any Item:** Die Karte wird ausgelöst, wenn mindestens ein Artikel die angegebene Bedingung für die Wareneingangsmethode erfüllt.
  * **All Items:** Die Karte wird nur ausgelöst, wenn alle Artikel die angegebene Bedingung für die Wareneingangsmethode erfüllen.
* **Operatoren:** Die folgenden Operatoren stehen zur Definition der Bedingung zur Verfügung:
  * **Gleich (=):** Prüft, ob die Wareneingangsmethode mit dem angegebenen Wert übereinstimmt.
  * **Ungleich (≠):** Stellt sicher, dass die Wareneingangsmethode nicht mit dem angegebenen Wert übereinstimmt.

## **Verwendung:**

Diese Karte eignet sich ideal für Lagerleiter, Bestandskoordinatoren oder Logistikpersonal, die die Wareneingangsmethoden von Artikeln validieren müssen, bevor weitere Aktionen wie Verarbeitung, Lagerung oder Versand zugelassen werden.

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie prüft, ob **alle Artikel** die Wareneingangsmethode **gleich "Direct Delivery"** haben. Erfüllt jeder Artikel diese Bedingung, wird der Workflow fortgesetzt und bestätigt, dass alle Artikel für die Direktlieferung vorgesehen sind.

Durch die Verwendung der Karte "Receiving Method Validation" können Organisationen die Einhaltung von Wareneingangsprotokollen sicherstellen, Logistik-Workflows verbessern und die Genauigkeit bei der Artikelbehandlung auf Basis bestimmter Wareneingangsmethoden wahren.
