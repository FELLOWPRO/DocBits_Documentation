# Esempio di Workflow: Attivatore di Esportazione Condizionale



<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits Flusso di lavoro Acquisto Ordine 7"><figcaption></figcaption></figure>

Questo workflow illustra le condizioni in base alle quali dovrebbe essere avviato un processo di esportazione. Garantisce che solo i documenti che soddisfano tutti i criteri specificati vengano elaborati per l'esportazione, migliorando l'integrità dei dati e l'allineamento alle regole aziendali.

### Quando:

* Un documento all'interno del sistema viene valutato per l'idoneità all'esportazione.

### Logica:

1. **Controllo del Tipo di Documento**
* Il documento deve essere di un certo tipo (ad esempio, "Fattura" o "Ricevuta"). Specificare il tipo di documento che si qualifica per il processo di esportazione.
2. **Verifica dello Stato**
* Lo stato attuale del documento deve soddisfare criteri predefiniti (ad esempio, "Approvato" o "Pronto per l'Esportazione") che indicano che è pronto per ulteriori elaborazioni.
3. **Condizioni Contestuali**
* Vengono eseguiti controlli aggiuntivi per garantire che i dettagli del documento siano conformi a requisiti specifici. Questi controlli potrebbero coinvolgere la verifica delle informazioni all'interno delle conferme d'ordine o degli ordini d'acquisto. Specificare le condizioni particolari che devono essere soddisfatte. Per esempio:
* Tutti gli articoli elencati nella conferma d'ordine corrispondono a quelli nell'ordine d'acquisto.
* L'importo totale nella conferma d'ordine corrisponde all'importo totale nell'ordine d'acquisto.
* Le date di consegna specificate nella conferma d'ordine sono allineate con quelle nell'ordine d'acquisto.

### Quindi:

#### Azione:

* **Avviare l'Esportazione**
* Se tutte le condizioni sopra indicate sono soddisfatte, il sistema avvia automaticamente il processo di esportazione per il documento.
* Questo potrebbe comportare la generazione di un file di esportazione, l'invio dei dati a un sistema esterno o l'attivazione di un workflow in un'altra applicazione.

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

