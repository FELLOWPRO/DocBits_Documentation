# EDI Data Transformation Process

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/EDI (1).png" alt=""><figcaption></figcaption></figure>

#### Schritt 1: Strukturbeschreibung (Structure Descriptor)

* **Format**: JSON
* **Zweck**: In diesem Schritt wird die Struktur der EDI-Daten definiert. Dazu gehört die Angabe von Segmenten wie `SAC`, `N1` und `PO1` sowie die Beschreibung der in den einzelnen Segmenten enthaltenen Felder. Für Segmente, die verschachtelte Strukturen enthalten, werden Schleifen (Loops) definiert, um die Datenhierarchie korrekt zu organisieren. ...
