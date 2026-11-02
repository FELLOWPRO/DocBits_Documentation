# Flusso di Esecuzione On-Premise

Per i clienti che eseguono l'operatore DocBits in locale, la seguente sequenza descrive come un documento elaborato attiva ed esegue un prompt dell'operatore tramite l'Agente DocBits locale.

1. **Caricamento e Elaborazione del Documento** Un documento viene caricato in DocBits e passa attraverso l'elaborazione standard (Estrazione, convalida, ecc.).
2. **Attivazione del Flusso di Lavoro** Una volta completata l'elaborazione, un Flusso di Lavoro configurato in DocBits valuta le sue condizioni di attivazione. Quando tali condizioni sono soddisfatte, il Flusso di Lavoro crea un nuovo **Task dell'Operatore**.
3. **Creazione e Invio del Task**
   * Il flusso di lavoro invia il testo dello script, le variabili, il numero massimo di passaggi, il numero massimo di tentativi come payload del task al Work Pool condiviso.
4. **Ciclo di Polling dell'Agente**
   * Un Agente DocBits on-prem (installato nell'ambiente del cliente) controlla il Work Pool ogni 5 minuti. Se non vengono trovati task, l'agente rimane inattivo e riprova dopo l'intervallo.
5. **Esecuzione del Task**
   * Quando compare un task nel Work Pool, l'Agente lo recupera e inizia l'esecuzione.
6. **Generazione dei Log**
   * Per ogni passaggio - successo o fallimento - l'agente registra log dettagliati (azioni, stati, timestamp). Al termine, compila il log completo e lo stato finale.
7. **Ritorno e Visualizzazione dei Risultati**
   * L'agente invia i log e lo stato a DocBits. La cronologia di esecuzione del flusso di lavoro di origine viene aggiornata e gli utenti possono esaminare i dettagli nella scheda **Log del Flusso di Lavoro**.
