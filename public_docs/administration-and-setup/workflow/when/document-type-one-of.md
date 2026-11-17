# Dokumenttyp aus einer Liste

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_list_v2-de-de.png" alt="Dokumenttyp aus einer Liste, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type-list/v1/de.mp4" %}

**Video:** Karte: Dokumenttyp: einer aus einer Liste · 0:31 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type-list/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Dokumenttyp: einer aus einer Liste** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type-list/v1/de.mp4#t=0.25)

Die Karte Dokumenttyp einer der folgenden prüft den Typ eines Dokuments gegen eine Liste. Wählen Sie Ist oder Ist nicht und dann einen oder mehrere Dokumenttypen. Ist trifft zu, wenn der Typ in der Liste steht, Ist nicht, wenn er nicht darin steht.

**Beispiel: Rechnungen und Gutschriften** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type-list/v1/de.mp4#t=18.25)

Zum Beispiel ein Workflow für Rechnungen und Gutschriften: Dokumenttyp ist einer von Rechnung und Gutschrift als Wenn-Karte, dann die Zuweisungskarte. Andere Dokumente starten diesen Workflow nicht.

</details>

## **Zweck:**

Diese DocBits-Karte gewährleistet die korrekte Klassifizierung eines Dokuments, indem überprüft wird, ob es einem der angegebenen Dokumententypen entspricht. Dies ist nützlich in Situationen, in denen ein Dokument mehreren Kategorien zugeordnet werden könnte, um eine umfassendere Validierung und automatisierte Verarbeitung zu ermöglichen.

## **Funktionalität:**

* **Validierung mehrerer Dokumententypen:** Diese Karte ermöglicht es Benutzern zu überprüfen, ob ein Dokument einem Satz von angegebenen Dokumententypen entspricht, um eine flexible Kategorisierung für komplexere Dokumenten-Workflows sicherzustellen.
* **Operator:** Benutzer können Bedingungen definieren, um das Dokument gegen mehrere Typen zu validieren. Verfügbare Operatoren sind:
  * **Ist:** Bestätigt, dass das Dokument einem der angegebenen Dokumententypen entspricht.
  * **Ist nicht:** Stellt sicher, dass das Dokument keinem der ausgewählten Dokumententypen entspricht.
* **Dokumententypen:** Benutzer können aus mehreren unterstützten Dokumententypen auswählen, darunter:
  * **Rechnung:** Finanzunterlagen, die zur Zahlung eingereicht werden.
  * **Gutschrift:** Dokumente, die eine Reduzierung des geschuldeten Betrags anzeigen.
  * **Bestellung:** Dokumente, die die Bestellung eines Käufers detaillieren.
  * **Auftragsbestätigung:** Dokumente, die bestätigen, dass eine Bestellung akzeptiert wurde.
  * **Versandanzeige:** Dokumente, die über eine bevorstehende Lieferung informieren.

## **Verwendung:**

Diese Karte eignet sich für Dokumentenmanager und Administratoren, die sicherstellen müssen, dass Dokumente in eine der verschiedenen Kategorien eingeordnet werden. Sie ist besonders nützlich für Dokumenten-Workflows, in denen ein Dokument unter mehreren Kategorien klassifiziert werden kann, um Automatisierung und Klassifizierungsgenauigkeit zu verbessern.

## **Beispiel Szenario:**

* Ein Benutzer lädt ein Dokument hoch, das entweder eine "Rechnung" oder eine "Gutschrift" sein könnte. Mit dem "Ist"-Operator bestätigt die Karte, dass das Dokument einem der ausgewählten Typen entspricht, sodass das System die entsprechenden Regeln und Kategorisierung anwenden kann.

Durch die Verwendung der Karte "Validierung mehrerer Dokumententypen" können Organisationen die Flexibilität des Workflows verbessern, die Kategorisierung automatisieren und sicherstellen, dass Dokumente ordnungsgemäß behandelt werden, auch wenn mehrere Typen zutreffen.
