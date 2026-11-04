# Flusso di Lavoro Standard

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Flusso di lavoro Acquisto Ordine 4"><figcaption></figcaption></figure>

#### Panoramica dei Componenti del Flusso di Lavoro:

* **Email della Fattura AP**: Il processo inizia probabilmente con una fattura ricevuta via email.
* **DocBits**: Questo strumento potrebbe essere utilizzato per compiti iniziali di gestione dei documenti come acquisizione e digitalizzazione delle fatture.
* **Revisione Finanziaria**: Le fatture vengono sottoposte a una revisione finanziaria in cui vengono prese decisioni sulla loro validità e accuratezza.

#### Passaggi nel Flusso di Lavoro:

1. **Revisione Iniziale**:
* Le fatture vengono ricevute e elaborate inizialmente utilizzando DocBits.
* Vengono quindi esaminate dal team finanziario per garantire che vengano rimosse dal flusso di lavoro se sono complete, o spinte avanti per ulteriore elaborazione.
2. **Fatture con PO vs Senza PO**:
* Il flusso di lavoro distingue tra fatture correlate a ordini d'acquisto e fatture non correlate a ordini d'acquisto.
* Le fatture non correlate a ordini d'acquisto vengono instradate per ulteriore approvazione o rifiuto in base a criteri predefiniti come l'ID del fornitore, la quantità, il prezzo unitario e il numero dell'articolo.
3. **Confronto e Non Conformità**:
* Le fatture vengono controllate rispetto ai documenti di ricezione delle merci per garantire che i dettagli corrispondano (come l'ID del fornitore e la quantità).
* In caso di non conformità, la fattura è soggetta a ulteriore revisione e possibilmente a rifiuto.
4. **Revisione Finanziaria e dell'Acquirente**:
* Per le fatture correlate agli ordini d'acquisto, viene condotto un processo dettagliato di confronto che coinvolge una revisione dell'acquirente.
* Potrebbero essere necessari aggiustamenti agli ordini d'acquisto o ai documenti di ricezione delle merci.
5. **Decisioni Finali**:
* Le fatture che superano tutti i controlli vengono approvate e integrate nei sistemi finanziari per la tenuta dei registri.
* Le fatture respinte attivano notifiche, e potrebbe essere richiesta una nuova fattura dall'acquirente.
6. **Integrazione con Infor IDM & LN+M3**:
* Le fatture approvate vengono probabilmente inviate a Infor's IDM per la gestione dei documenti e a LN per la registrazione contabile.
* Questa integrazione garantisce che tutti i record finanziari siano aggiornati e che il flusso di lavoro si integri senza problemi nel sistema ERP più ampio.

#### Punti Decisionali:

* Durante il flusso di lavoro, ci sono vari punti decisionali in cui una fattura potrebbe essere approvata, respinta o rimandata per ulteriori informazioni. Vengono inviate notifiche dopo ritardi, garantendo un'elaborazione tempestiva.

Questi Flussi di Lavoro saranno inclusi nel Flusso di Lavoro Standard.
