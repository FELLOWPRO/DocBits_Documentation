# Stati di disabilitazione dell'OP

## **Panoramica**

L'impostazione **PO disable statuses** stabilisce quali stati delle righe di Purchase Order (PO) sono bloccati nella schermata di matching. Una riga con uno stato disabilitato configurato viene mostrata barrata e non può essere trascinata in un abbinamento. Usare l'impostazione per controllare l'idoneità al matching per il tipo di documento interessato.

## **Passaggi di attivazione**

1. Aprire **Settings → Document Types**.
2. Individuare il tipo di documento da configurare. L'esempio seguente usa **Invoice**. Aprire il relativo pulsante a ingranaggio (**More settings**).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-invoice-card-native-en-20261102.png" alt="Intestazione attuale, in inglese, della scheda del tipo di documento Invoice con i controlli Activate ed Extraction e l'ingranaggio More settings"><figcaption><p>La scheda Invoice esistente e il relativo ingranaggio More settings. I controlli Activate ed Extraction sono separati dalla selezione degli stati PO.</p></figcaption></figure>

3. Aprire la sezione **Purchase Order** e individuare **PO disable statuses**.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-field-native-en-20261102.png" alt="Campo PO disable statuses attuale in inglese, con la freccia a discesa e il pulsante Apply"><figcaption><p>Il campo PO disable statuses e il relativo pulsante Apply. La selezione vuota mostrata qui è un esempio della configurazione di test esistente.</p></figcaption></figure>

### **Come riconoscere un Purchase Order disabilitato**

Nella [Purchase Order Matching Screen](https://docs.docbits.com/end-user-and-partner-section/end-user-section/purchase-order-matching) una riga il cui stato è disabilitato è contrassegnata da una barratura e non può essere trascinata in un abbinamento. Quando si verifica perché la riga non è disponibile, controllare lo stato della riga e l'elenco degli stati disabilitati del tipo di documento.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disabled-row-historical-strike-strokes-masked-20261102.png" alt="Riga storica di un PO annullato con identificatori e valori numerici mascherati; le barrature originali restano visibili"><figcaption><p>Una riga storica conservata di un PO annullato. Blocchi grigi nascondono identificatori e valori numerici, compresa la quantità abbinata. I brevi tratti orizzontali mantengono la barratura originale.</p></figcaption></figure>

### **Come configurarla**

1. Fare clic sul campo **PO disable statuses** per aprire gli stati disponibili.
2. Selezionare le caselle di controllo degli stati che il processo esclude dal matching. Deselezionare una casella per rimuovere quello stato dalla selezione.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-options-native-en-20261102.png" alt="Menu a discesa PO disable statuses attuale in inglese con tutte le undici caselle di controllo degli stati e il pulsante Apply; il contenuto circostante della pagina è mascherato"><figcaption><p>Le opzioni di stato attuali con il loro stato non selezionato esistente. Il contenuto circostante della pagina è mascherato; il menu a discesa e il pulsante Apply sono invariati.</p></figcaption></figure>

3. Fare clic su **Apply** per salvare la selezione per questo tipo di documento. Aprire il menu a discesa da solo non salva alcuna modifica.

**Available Statuses**

* Canceled
* Deleted
* Invoiced
* Open
* Partially Invoiced
* Partially Received
* Received
* Rejected
* Unapproved
* Hold
* Closed
