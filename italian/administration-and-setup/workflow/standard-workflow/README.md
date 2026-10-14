# Workflow Standard

<figure><img src="../../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Flusso di lavoro Acquisto Ordine 4"><figcaption></figcaption></figure>

#### Panoramica dei Componenti del Workflow:

* **AP Invoice Email**: il processo probabilmente inizia con una fattura ricevuta via email.
* **DocBits**: questo strumento può essere utilizzato per le attività iniziali di gestione documentale, come l'acquisizione e la digitalizzazione delle fatture.
* **Finance Review**: le fatture sono sottoposte a una revisione finanziaria in cui vengono prese decisioni sulla loro validità e accuratezza.

#### Passaggi del Workflow:

1. **Initial Review**:
   * Le fatture vengono ricevute ed elaborate inizialmente con DocBits.
   * Vengono quindi esaminate dal team finanziario per assicurarsi che siano rimosse dal workflow se complete, oppure inoltrate per ulteriore elaborazione.
2. **PO vs Non-PO Invoices**:
   * Il workflow distingue tra fatture correlate a PO e fatture non correlate a PO.
   * Le fatture non correlate a PO vengono instradate per ulteriore approvazione o rifiuto in base a criteri predefiniti come ID fornitore, quantità, prezzo unitario e numero di articolo.
3. **Matching and Mismatching**:
   * Le fatture vengono confrontate con i ricevimenti merci per garantire che i dettagli corrispondano (come ID fornitore e quantità).
   * In caso di discrepanze, la fattura è soggetta a ulteriore revisione e possibilmente al rifiuto.
4. **Finance and Buyer Review**:
   * Per le fatture correlate a PO, viene condotto un dettagliato processo di abbinamento che coinvolge una revisione da parte dell'acquirente.
   * Potrebbero essere necessarie modifiche agli ordini di acquisto o ai ricevimenti merci.
5. **Final Decisions**:
   * Le fatture che superano tutti i controlli vengono approvate e integrate nei sistemi finanziari per la conservazione dei registri.
   * Le fatture rifiutate attivano notifiche e l'acquirente può richiedere una nuova fattura.
6. **Integration with Infor IDM & LN+M3**:
   * Le fatture approvate vengono probabilmente inviate all'IDM di Infor per la gestione documentale e a LN per la registrazione contabile.
   * Questa integrazione garantisce che tutti i registri finanziari siano aggiornati e che il workflow si integri senza soluzione di continuità nel più ampio sistema ERP.

#### Punti Decisionali:

* In tutto il workflow sono presenti vari punti decisionali in cui una fattura può essere approvata, rifiutata o rinviata per ulteriori informazioni. Le notifiche vengono inviate dopo eventuali ritardi, garantendo un'elaborazione tempestiva.

Questi Workflow saranno inclusi nel Workflow Standard
