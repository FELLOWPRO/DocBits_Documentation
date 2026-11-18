# Dokumenttyp als Auslöser prüfen

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-de-de.png" alt="Dokumenttyp als Auslöser prüfen, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-de-de.png" alt="Dokumenttyp als Auslöser prüfen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/de.mp4" %}

**Video:** Karte: Dokumenttyp ist / ist nicht · 0:30 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Dokumenttyp ist / ist nicht** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/de.mp4#t=0.25)

Die Karte Dokumenttyp prüft den Typ eines Dokuments. Wählen Sie Ist oder Ist nicht und dann den Typ, zum Beispiel Rechnung. Ist nicht trifft auf jeden Typ außer dem gewählten zu.

**Beispiel: nur Rechnungen** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/de.mp4#t=17.183)

Zum Beispiel ein Workflow nur für Rechnungen: Dokumenttyp ist Rechnung als Wenn-Karte, dann eine Zuweisungskarte. Für Gutschriften, Angebote oder Bestellungen startet dieser Workflow nicht.

</details>

## **Zweck:**

Diese Workflow-Karte ist speziell darauf ausgelegt, vordefinierte Operationen an nach Typ kategorisierten Dokumenten durchzuführen. Sie optimiert die Bearbeitung verschiedener Dokumentenformen innerhalb eines ERP-Systems und stellt sicher, dass jeder Typ gemäß seinen einzigartigen Anforderungen und organisatorischen Richtlinien verarbeitet wird.

## **Funktionalität:**

* **Dokumenttyp-Validierung**: Diese Karte überprüft, ob ein Dokument einem bestimmten Typ entspricht, sodass Benutzer dessen Kategorisierung bestätigen können.
* **Operator**: Benutzer können Bedingungen festlegen, um den Dokumenttyp zu bestimmen. Verfügbare Operatoren sind:
  * **Ist**: Bestätigt, dass das Dokument dem angegebenen Dokumenttyp entspricht.
  * **Ist nicht**: Stellt sicher, dass das Dokument nicht dem angegebenen Dokumenttyp entspricht.
* **Dokumenttypen**: Unterstützte Dokumenttypen sind:
  * **Rechnung**
  * **Gutschrift**
  * **Lastschrift**
  * **Bestellung**
  * **Auftragsbestätigung**
  * **Lieferschein**

## **Verwendung**:

Diese Karte ist nützlich für Dokumentenmanager und Administratoren, die sicherstellen müssen, dass Dokumente korrekt klassifiziert werden, um die Bearbeitung zu optimieren. Die Validierung von Dokumenttypen verbessert die Workflow-Automatisierung, ermöglicht dokumentenspezifische Aktionen und hält Aufzeichnungen organisiert.

## **Beispiel-Szenario**:

* Ein Benutzer lädt ein Dokument mit der Bezeichnung "Lastschrift" hoch. Mit dem Operator "Ist" bestätigt die Karte, dass der Dokumenttyp tatsächlich "Lastschrift" ist, sodass das System relevante Verarbeitungsregeln anwenden und es entsprechend kategorisieren kann.

Durch den Einsatz der Karte "Dokumenttyp" können Organisationen die Dokumentenklassifizierung automatisieren, die Konsistenz in der Dokumentenbearbeitung sicherstellen und die Effizienz von Dokumentenmanagement-Workflows verbessern.
