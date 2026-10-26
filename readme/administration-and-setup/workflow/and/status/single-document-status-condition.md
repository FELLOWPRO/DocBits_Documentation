# Statusbedingung für ein einzelnes Dokument

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-c0315ad39a89-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

**Zweck**

Diese Workflow-Karte ist darauf zugeschnitten, Operationen an Dokumenten auf Basis eines einzelnen, angegebenen Dokumentstatus zu steuern. Indem die Bedingung auf einen Status vereinfacht wird, konzentriert sich die Karte auf sehr spezifische Workflow-Auslöser und eignet sich damit ideal für gezielte Dokumentverarbeitungsaktivitäten innerhalb eines ERP-Systems.

**Bestandteile der Karte**

1. **Operator**
   * **Beschreibung**: Gibt die Methode zur Auswertung des Dokumentstatus anhand der ausgewählten Bedingung an.
   * **Optionen**:
     * **is**: Löst die Operation aus, wenn der aktuelle Status des Dokuments mit dem ausgewählten Status übereinstimmt.
     * **ist nicht**: Löst die Operation aus, wenn der aktuelle Status des Dokuments nicht mit dem ausgewählten Status übereinstimmt.
2. **Status**
   * **Beschreibung**: Ermöglicht die Auswahl eines einzelnen Dokumentstatus zur Festlegung der Bedingung.
   * **Statusbeispiele**: „Fehler“, „Exportfehler“, „Bereit zur Validierung“, „Bereit zur Überprüfung“, „Genehmigung ausstehend“, „Zweite Genehmigung ausstehend“.
   * **Detailliert**: Benutzer wählen einen Status aus einem Dropdown oder einer Reihe von Optionsfeldern. Dieser Status dient dann als Kriterium für die Operation der Karte.

**Funktionalität**

* **Erkennung des Dokumentstatus**: Identifiziert den aktuellen Status eines Dokuments, während es durch das ERP-System verarbeitet wird.
* **Bedingungsauswertung**:
  * Basierend auf dem ausgewählten Operator (`is` oder `is not`) prüft die Karte, ob der aktuelle Status des Dokuments mit dem gewählten Statuskriterium übereinstimmt.
* **Ausführung der Aktion**:
  * **Bedingung erfüllt (True)**: Stimmt der Status überein (oder nicht überein, je nach Operator), wird die entsprechende Aktion eingeleitet. Dies kann das Weiterleiten zur weiteren Verarbeitung, das Erzeugen von Benachrichtigungen oder andere vordefinierte Workflows sein.
  * **Bedingung nicht erfüllt (False)**: Ist die Bedingung nicht erfüllt, wird keine Aktion ausgeführt oder ein alternativer Pfad ausgelöst.
* **Integration mit anderen Workflows**: Obwohl sie für die Auswertung eines einzelnen Status ausgelegt ist, kann diese Karte effektiv in umfassendere Workflow-Sequenzen integriert werden, um eine präzise Dokumentbearbeitung sicherzustellen.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer richten die Karte ein, indem sie einen Operator auswählen und dann einen Status aus den verfügbaren Optionen wählen. Dieser Auswahlprozess ist unkompliziert und so gestaltet, dass Verwirrung vermieden wird.
* **Überwachung und Berichterstattung**: Ermöglicht die Überwachung über systemgenerierte Berichte oder Dashboards, die die Verarbeitung von Dokumenten auf Basis ihres Status verfolgen, und hilft so, die Wirksamkeit der implementierten Workflows zu überwachen.
* **Fehlerbehandlung und Benachrichtigungen**: Konfigurierbar, um Benutzer auf Verarbeitungsanomalien hinzuweisen oder Dokumente zu markieren, die die festgelegten Bedingungen nicht erfüllen, und so eine zeitnahe Aufmerksamkeit und Lösung sicherzustellen.

#### Fazit

Die Workflow-Karte "Single Document Status Condition" vereinfacht das Dokumentenmanagement, indem sie sich auf einzelne Statusbedingungen konzentriert. Diese Spezifikation hilft in Fällen, in denen eine präzise Kontrolle über Dokumentflüsse erforderlich ist, insbesondere in Umgebungen mit strengen Verarbeitungskriterien. Eine klare Dokumentation dieser Version der Karte stellt sicher, dass Benutzer ihre Anwendung vollständig verstehen und sie effektiv in ihre täglichen Abläufe integrieren können, und steigert so sowohl die Compliance als auch die Effizienz bei der Dokumentverarbeitung.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Wann nutzen:** Eine Folgeregel auf Belege in der ersten Freigabestufe begrenzen.

**Wo:** Standard-Workflow-Designer → Und → Status.

**Konfiguration:** Wählen Sie in Version 2 den Operator „ist“ (`is`) und den vorhandenen Status Genehmigung ausstehend (`validated_pending_approval`).

**Erwartetes Ergebnis und Gegenbeispiel:** Ein Beleg mit genau diesem Status erfüllt die Bedingung. Ein bereits exportierter Beleg erfüllt sie nicht. Die Karte prüft den Status und ändert ihn nicht. Für mehrere zulässige Status verwenden Sie die gesonderte Statuslisten-Karte.

Die Beispiele beschreiben erwartete Ergebnisse. Verwenden Sie die in Ihrer Organisation tatsächlich konfigurierten Felder und angebotenen Werte.

## Admin-Beispielvideo

Wann ich eine Bedingung auf einen bestimmten Belegstatus beschränke und wie ich den vorhandenen Status auswähle. Die Beispiele zeigen erwartete Ergebnisse.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-single-document-status-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-single-document-status-admin/v1/de-theme-v4.html)

[Transkript lesen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-single-document-status-admin/v1/de.txt)
