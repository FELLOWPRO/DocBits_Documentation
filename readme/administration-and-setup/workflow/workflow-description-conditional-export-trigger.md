# Workflow-Beispiel: Bedingter Export-Trigger

<figure><img src="../../.gitbook/assets/image (3) (2) (2).png" alt=""><figcaption></figcaption></figure>

Dieser Workflow beschreibt die Bedingungen, unter denen ein Export-Prozess gestartet werden soll. Er stellt sicher, dass nur Dokumente, die alle festgelegten Kriterien erfüllen, für den Export verarbeitet werden, wodurch die Datenintegrität und die Übereinstimmung mit Geschäftsregeln verbessert werden.

### When:

* Ein Dokument im System wird auf seine Export-Eignung geprüft.

### Logik:

1. **Prüfung des Dokumenttyps**
   * Das Dokument muss von einem bestimmten Typ sein (z. B. „Rechnung" oder „Beleg"). Geben Sie den Dokumenttyp an, der für den Export-Prozess infrage kommt.
2. **Statusprüfung**
   * Der aktuelle Status des Dokuments muss vordefinierte Kriterien erfüllen (z. B. „Genehmigt" oder „Bereit für Export"), die anzeigen, dass es für die weitere Verarbeitung bereit ist.
3. **Kontextbezogene Bedingungen**
   * Es werden zusätzliche Prüfungen durchgeführt, um sicherzustellen, dass die Details des Dokuments mit bestimmten Anforderungen übereinstimmen. Diese Prüfungen können die Überprüfung von Informationen in Auftragsbestätigungen oder Bestellungen umfassen. Geben Sie die konkreten Bedingungen an, die erfüllt sein müssen. Zum Beispiel:
     * Alle in der Auftragsbestätigung aufgeführten Positionen stimmen mit denen in der Bestellung überein.
     * Der Gesamtbetrag in der Auftragsbestätigung stimmt mit dem Gesamtbetrag in der Bestellung überein.
     * Die in der Auftragsbestätigung angegebenen Lieferdaten stimmen mit denen in der Bestellung überein.

### Then:

#### Aktion:

* **Export auslösen**
  * Wenn alle oben genannten Bedingungen erfüllt sind, startet das System automatisch den Export-Prozess für das Dokument.
  * Dies kann das Erzeugen einer Exportdatei, das Senden von Daten an ein externes System oder das Auslösen eines Workflows in einer anderen Anwendung umfassen.

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
