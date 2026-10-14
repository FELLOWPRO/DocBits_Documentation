# non trovato nel addebito diretto

## **Passo 1: Controlla la Configurazione LN**

1. Accedi a **LN CE**.
2. Vai al menu **Opzioni** e seleziona **Esegui Programma**.
3. Nel campo di input, digita **Parametri ACP** e premi Invio per aprire il programma.
4. Fai clic sulla freccia accanto al campo **Set Attuale** per espandere le impostazioni.
5. Vai alla sezione **Corrispondenza**.
   * **Controlla l'Impostazione di Corrispondenza Automatica:**
     * Se la **Corrispondenza Automatica** è impostata su **Corrispondi alla Ricevuta di Acquisto**, procedi al passaggio successivo.
     * Se non è impostata su **Corrispondi alla Ricevuta di Acquisto**, ma hai comunque ricevuto questo errore, ti preghiamo di contattarci.

## **Passo 2: Apri le Impostazioni di DocBits**

Se la **Corrispondenza Automatica** è impostata su **Corrispondi alla Ricevuta di Acquisto**, procedi con i seguenti passaggi in DocBits:

1. Apri **DocBits** e vai alla sezione **Impostazioni**.
2. Vai a **Elaborazione Documenti**.
3. Seleziona **Esporta**.
4. Nella sezione **Esporta**, fai clic sull'icona dei **tre punti** accanto all'esportazione che non funziona e seleziona **Modifica**.
5. Nel menu **Modifica Impostazioni di Esportazione**, fai clic su **Scarica il file di Mappatura LN**.

## **Passo 3: Modifica il File di Mappatura LN**

1. Apri il file di **Mappatura LN** scaricato.
2. Cerca il campo **IRF\_PackingSlip**.
   * Se il campo **IRF\_PackingSlip** è presente e impostato su **niente** (vuoto), aggiornalo a **TF\_packing\_slip**.
   * Se il campo **IRF\_PackingSlip** **non è presente**, aggiungilo al file e imposta il suo valore su **TF\_packing\_slip**.
3. Per il campo **Campi Ricevuta Fattura**, aggiungi **PackingSlip** ai valori.

Dovrebbe apparire come segue:

<figure><img src="../../../../.gitbook/assets/PackingSlip.png" alt=""><figcaption></figcaption></figure>

## **Passo 4: Aggiungi il File Aggiornato a DocBits**

1. Torna alla sezione **Esporta** in DocBits dove hai precedentemente scaricato il file di **Mappatura LN**.
2. Carica il file di **Mappatura LN** modificato con le nuove aggiunte.

## Se incontri ancora l'**Errore durante l'esportazione del documento su LN** con codice di stato **500**, ti preghiamo di contattarci
