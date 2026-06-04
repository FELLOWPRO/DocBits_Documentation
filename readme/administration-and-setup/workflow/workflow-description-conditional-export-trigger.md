# Descrizione del Workflow: Trigger di Esportazione Condizionale



<figure><img src="../../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Impostazioni Flusso di lavoro"><figcaption></figcaption></figure>

Questo workflow descrive le condizioni in cui deve essere avviato un processo di esportazione. Garantisce che solo i documenti che soddisfano tutti i criteri specificati vengano elaborati per l'esportazione, migliorando l'integrità dei dati e l'allineamento con le regole aziendali.

### When:

* Un documento all'interno del sistema viene valutato per l'idoneità all'esportazione.

### Logica:

1. **Document Type Check**
   * Il documento deve essere di un determinato tipo (es. "Invoice" o "Receipt"). Specifica il tipo di documento che si qualifica per il processo di esportazione.
2. **Status Verification**
   * Lo stato corrente del documento deve soddisfare criteri predefiniti (es. "Approved" o "Ready for Export") che indicano che è pronto per l'ulteriore elaborazione.
3. **Contextual Conditions**
   * Vengono eseguiti controlli aggiuntivi per garantire che i dettagli del documento siano allineati a requisiti specifici. Questi controlli possono includere la verifica delle informazioni all'interno delle conferme d'ordine o degli ordini di acquisto. Specifica le condizioni particolari che devono essere soddisfatte. Ad esempio:
     * Tutti gli articoli elencati nella conferma d'ordine corrispondono a quelli nell'ordine di acquisto.
     * L'importo totale nella conferma d'ordine corrisponde all'importo totale nell'ordine di acquisto.
     * Le date di consegna specificate nella conferma d'ordine sono allineate a quelle nell'ordine di acquisto.

### Then:

#### Azione:

* **Initiate Export**
  * Se tutte le condizioni precedenti sono soddisfatte, il sistema avvia automaticamente il processo di esportazione per il documento.
  * Questo può comportare la generazione di un file di esportazione, l'invio di dati a un sistema esterno o l'attivazione di un workflow in un'altra applicazione.

#### Esempio di Implementazione:

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
