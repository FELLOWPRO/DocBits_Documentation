# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Change Status"** wird verwendet, um den Status eines Dokuments in einen der vordefinierten Zustände zu ändern – **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** – und optional auf Basis der Statusänderung zugehörige Workflows auszulösen. Diese Karte automatisiert den Prozess von Statusaktualisierungen und Workflow-Auslösern und gewährleistet so ein effizientes Dokumentenmanagement und eine effiziente Fehlerbehandlung.

## **Bestandteile der Karte:**

1. **Status**
   * **Beschreibung**: Gibt den neuen Status an, der auf das Dokument angewendet wird.
   * **Optionen**:
     * **Error**: Markiert das Dokument als fehlerbehaftet.
     * **Rejected**: Gibt an, dass das Dokument abgelehnt wurde und nicht weiter fortfährt.
     * **Ready for Validation**: Setzt das Dokument so, dass es vom nächsten Benutzer oder Systemprozess geprüft und validiert wird.
     * **Pending Approval**: Versetzt das Dokument in einen Wartezustand zur Freigabe.
     * **Pending Second Approval**: Stellt das Dokument für eine zweite Freigabestufe zurück, sofern zutreffend.
2. **Workflows auslösen**
   * **Beschreibung**: Legt fest, ob nach der Statusänderung nachfolgende Workflows ausgelöst werden sollen.
   * **Optionen**:
     * **True**: Startet alle relevanten Workflows auf Basis der Statusänderung.
     * **False**: Verhindert die Ausführung von Workflows nach der Statusänderung.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** festgelegten Bedingungen aus. Sind diese Bedingungen erfüllt, fährt die Karte fort und ändert den Status des Dokuments in den ausgewählten Wert.
* **Statusaktualisierung**: Sind die Bedingungen erfüllt, wird der Status des Dokuments je nach Auswahl des Benutzers auf eine der vordefinierten Optionen aktualisiert (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval).
* **Workflow-Auslöseaktion**: Ist **Workflows auslösen** auf **True** gesetzt, startet das System nach der Statusaktualisierung automatisch alle zugehörigen Workflows. Ist die Einstellung auf **False** gesetzt, werden keine zusätzlichen Workflows ausgelöst, und der Prozess endet mit der Statusänderung.

## **Einrichtung und Konfiguration:**

Um diese Karte zu konfigurieren, müssen Benutzer:

1. Den gewünschten **Status** angeben, auf den das Dokument bei der Bedingungsauswertung gesetzt wird (Error, Rejected, Ready for Validation, Pending Approval oder Pending Second Approval).
2. Wählen, ob nach der Statusänderung **Workflows ausgelöst** werden sollen, indem **True** oder **False** ausgewählt wird.
3. Die Karte führt ihre Aktion nur aus, wenn beide Bedingungen in den Abschnitten **"Where"** und **"And"** als erfüllt ausgewertet werden.

## **Fazit:**

Die Workflow-Karte **"Change Status"** bietet einen optimierten Ansatz zur Verwaltung von Dokumentstatus und zum Auslösen zugehöriger Workflows. Sie stellt sicher, dass Dokumente automatisch in den korrekten Status überführt und die erforderlichen Aktionen je nach Statusänderung ausgeführt werden. Durch das Festlegen klarer Bedingungen für die Ausführung reduziert sie den manuellen Aufwand und steigert die Workflow-Effizienz.
