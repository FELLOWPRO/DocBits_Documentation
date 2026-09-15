---
description: Stammdaten manuell über die API an DocBits senden
---

# Import über die API

Stammdaten erreichen DocBits normalerweise automatisch über Ihren ION-Datenfluss. Die Seiten in diesem Abschnitt beschreiben, wie Sie dieselben Daten manuell über die API-Testoberfläche senden — nützlich, wenn Sie einen Datensatz erneut importieren, etwas nachladen möchten, das nie angekommen ist, oder eine neue Feldzuordnung ausprobieren wollen, bevor Sie den automatischen Datenfluss einschalten.

Jede Seite folgt denselben fünf Schritten: den API-Link für Ihre Umgebung öffnen, mit Ihrer Org ID und Ihrem API Key autorisieren, das Formular ausfüllen, ausführen und prüfen, ob die Daten angekommen sind.

* [Lieferanten importieren (Supplier BOD)](supplier-bod.md)
* [Bestellungen importieren (Purchase Order BOD)](purchase-order-bod.md)
* [Wareneingänge importieren (Receive Delivery BOD)](receive-delivery-bod.md)
* [Stammdaten aus XML importieren](master-data-xml.md)

## Was Sie benötigen

* **Einen API Key** — siehe [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Ihre Org ID** — unter **Settings → Integration & SSO** im Abschnitt **ID**.
* **Die Daten selbst**, als XML-Datei oder als XML-Inhalt, den Sie einfügen können.

{% hint style="warning" %}
Ein Import schreibt direkt in die Stammdaten Ihrer Organisation. Prüfen Sie vor dem Ausführen, auf welche Umgebung, welche Region und welche Organisation Sie zeigen.
{% endhint %}
