# Workflow Beispiel: Bedingter Exportauslöser



<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="Workflow Bestellung Export Genehmigung Übersicht"><figcaption></figcaption></figure>

Dieser Workflow umreißt die Bedingungen, unter denen ein Exportprozess gestartet werden soll. Er stellt sicher, dass nur Dokumente, die alle festgelegten Kriterien erfüllen, für den Export verarbeitet werden, um die Datenintegrität und die Einhaltung der Geschäftsregeln zu verbessern.

### Wann:

* Ein Dokument im System wird auf Exportberechtigung geprüft.

### Logik:

1. **Dokumententypenprüfung**
* Das Dokument muss einen bestimmten Typ haben (z. B. "Rechnung" oder "Beleg"). Geben Sie den Dokumententyp an, der für den Exportprozess qualifiziert ist.
2. **Statusüberprüfung**
* Der aktuelle Status des Dokuments muss vordefinierte Kriterien erfüllen (z. B. "Genehmigt" oder "Bereit für Export"), was darauf hinweist, dass es für weitere Verarbeitungsschritte bereit ist.
3. **Kontextbezogene Bedingungen**
* Es werden zusätzliche Überprüfungen durchgeführt, um sicherzustellen, dass die Details des Dokuments mit spezifischen Anforderungen übereinstimmen. Diese Überprüfungen können die Überprüfung von Informationen in Auftragsbestätigungen oder Bestellungen umfassen. Geben Sie die speziellen Bedingungen an, die erfüllt sein müssen. Zum Beispiel:
* Alle in der Auftragsbestätigung aufgeführten Artikel stimmen mit denen in der Bestellung überein.
* Der Gesamtbetrag in der Auftragsbestätigung stimmt mit dem Gesamtbetrag in der Bestellung überein.
* Die in der Auftragsbestätigung angegebenen Liefertermine stimmen mit denen in der Bestellung überein.

### Dann:

#### Aktion:

* **Export starten**
* Wenn alle oben genannten Bedingungen erfüllt sind, startet das System automatisch den Exportprozess für das Dokument.
* Dies kann die Generierung einer Exportdatei, das Senden von Daten an ein externes System oder das Auslösen eines Workflows in einer anderen Anwendung umfassen.

#### Implementierungsbeispiel:
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

