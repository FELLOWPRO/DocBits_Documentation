# il valore deve essere numerico.

## **Passo 1: Indaga sull'Ordine di Acquisto**

**1. Controlla l'Ordine di Acquisto dal Pannello di Controllo**

* Se lo stato del documento è **Errore di Esportazione**:
  1. Trova il documento nel pannello di controllo.
  2. Clicca su di esso e poi seleziona il pulsante **Convalida Campi** per tornare alla schermata di convalida dei campi.
* Se lo stato del documento è **Pronto per la Convalida**:
  1. Clicca sul documento per procedere direttamente alla schermata di **Convalida Campi**.
* Se il documento è in stato di **Approvazione in Sospeso**:
  1. Vai alla **Schermata di Approvazione**.
  2. Accanto agli **Elementi dell'Ordine di Fatturazione**, trova la **Tabella dell'Ordine di Acquisto**.
  3. Vai al passaggio 3. Controlla il Numero di Consegna.

**2. Verifica l'Ordine di Acquisto**

1. Sulla schermata di **Convalida Campi**, assicurati che l'Ordine di Acquisto corretto sia selezionato.
2. Una volta confermato l'Ordine di Acquisto corretto, clicca sull'Ordine di Acquisto accanto alla tabella estratta, per aprire la vista della **Tabella dell'Ordine di Acquisto**.

**3. Controlla il Numero di Consegna**

* Nella Tabella dell'Ordine di Acquisto, cerca la colonna **Numero di Consegna**:
  * **Se è presente un Numero di Consegna**, procedi alla **Schermata di Approvazione** e controlla di nuovo se è presente, quando presente vai al **Passo 3**.
  * **Se non è presente alcun Numero di Consegna**, segui il **Passo 2** per risolvere questo problema.

## Passo 2: Verifica l'Ordine di Acquisto in LN

Prima di inviare l'Ordine di Acquisto a DocBits, verifica che il **Numero di Consegna** sia correttamente assegnato in **LN**. Controlla i dettagli dell'**Ordine di Acquisto** in **LN** per assicurarti che sia completo e preciso. Se il **Numero di Consegna** manca o è errato, potrebbe essere la causa dell'errore di esportazione.

Se l'**Ordine di Acquisto** sembra corretto e contiene i dettagli necessari, puoi procedere al passaggio successivo.

## **Passo 3: Apri le Impostazioni di DocBits**

1. Apri **DocBits** e vai alla sezione **Impostazioni**.
2. Naviga verso **Elaborazione Documenti**.
3. Seleziona **Esporta**.
4. Nella sezione **Esporta**, clicca sull'icona dei **tre punti** accanto all'esportazione che non funziona e seleziona **Modifica**.
5. Nel menu **Modifica Impostazioni di Esportazione**, clicca su **Scarica il file di Mappatura LN**.

## **Passo 3: Modifica il File di Mappatura LN**

1. Apri il file di **Mappatura LN** scaricato.
2. Cerca il campo **IRF\_ReceiptLine**.
   * Se il campo **IRF\_ReceiptLine** è presente e impostato su **niente** (vuoto), aggiornalo a **TF\_delivery\_line**.
   * Se il campo **IRF\_ReceiptLine** **non è presente**, aggiungilo al file e imposta il suo valore su **TF\_delivery\_line**.
3. Per il campo **Campi FatturaRicevuta**, aggiungi **ReceiptLine** ai valori.

Dovrebbe apparire come segue:

<figure><img src="../../../../.gitbook/assets/ReceiptLine.png" alt="" width="563"><figcaption></figcaption></figure>

## **Passo 4: Aggiungi il File Aggiornato a DocBits**

1. Torna alla sezione **Esporta** in DocBits dove hai precedentemente scaricato il file di **Mappatura LN**.
2. Carica il file di **Mappatura LN** modificato con le nuove aggiunte.

## Passo 5: Riprova l'Esportazione

Dopo aver confermato che l'**Ordine di Acquisto** ha un **Numero di Consegna** e aver verificato che il **file di esportazione è corretto**, segui questi passaggi per riprovare l'esportazione:

1. **Torna al Pannello di Controllo:**
   * Torna al pannello di controllo e trova il documento con l'errore di esportazione.
2. **Riprova il Processo di Esportazione:**
   * Clicca sul documento con l'errore di esportazione.
   * Se l'**Ordine di Acquisto** ha un **Numero di Consegna** valido e il **file di esportazione** è corretto, procedi a riprovare l'esportazione.
3. **Controlla il Risultato dell'Esportazione:**
   * Dopo aver riprovato, controlla nuovamente il processo di esportazione per vedere se il problema è stato risolto e il documento non viene più visualizzato come errore di esportazione.
   * Se l'esportazione ha successo, il problema dovrebbe essere risolto.
4. **Ulteriore Indagine (se il problema persiste):**
   * Se il problema persiste dopo aver riprovato l'esportazione, contatta il supporto per ulteriori indagini su possibili problemi di configurazione o di sistema.
