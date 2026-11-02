# Workflowvoorbeeld: voorwaardelijke exporttrigger



Deze workflow bepaalt onder welke voorwaarden een export wordt gestart. Alleen documenten die aan alle criteria voldoen, worden geëxporteerd. Dit ondersteunt de gegevensintegriteit en naleving van bedrijfsregels.

### Wanneer:

* Een document in het systeem wordt beoordeeld op geschiktheid voor export.

### Logica:

1. **Documenttype controleren**
   * Het document moet een bepaald type hebben, zoals "Invoice" of "Receipt". Geef aan welk documenttype voor export in aanmerking komt.
2. **Status controleren**
   * De huidige documentstatus moet aan vooraf bepaalde criteria voldoen, bijvoorbeeld "Approved" of "Ready for Export", om aan te geven dat het document klaar is voor verdere verwerking.
3. **Aanvullende voorwaarden**
   * Extra controles bepalen of de documentgegevens aan specifieke eisen voldoen, bijvoorbeeld door orderbevestigingen en inkooporders te vergelijken. Geef aan welke voorwaarden gelden, zoals:
     * Alle artikelen in de orderbevestiging komen overeen met die in de inkooporder.
     * Het totaalbedrag van de orderbevestiging komt overeen met dat van de inkooporder.
     * De leverdatums in de orderbevestiging sluiten aan op die in de inkooporder.

### Dan:

#### Actie:

* **Export starten**
  * Als aan alle bovenstaande voorwaarden is voldaan, start het systeem automatisch de export van het document.
  * Dit kan een exportbestand genereren, gegevens naar een extern systeem sturen of een workflow in een andere toepassing activeren.

#### Implementatievoorbeeld:

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
