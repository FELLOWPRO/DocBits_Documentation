# Stati di disabilitazione dell'OP

## **Panoramica**

L'impostazione **Stati di disabilitazione dell'OP** consente agli utenti di specificare gli stati degli ordini di acquisto (OP) che impediscono l'abbinamento delle fatture a quegli OP. Se un ordine di acquisto ha uno stato elencato in questa impostazione, **non può** essere utilizzato per l'abbinamento delle fatture nella schermata di abbinamento OP, bloccando ulteriori elaborazioni delle fatture correlate fino a quando lo stato dell'OP non cambia in uno stato che non è disabilitato.\
\
Utilizzando questa impostazione, gli utenti possono garantire che gli ordini di acquisto con stati specifici non subiscano ulteriori elaborazioni delle fatture, riducendo gli errori e prevenendo pagamenti non necessari.

## **Passi di attivazione**

1.  Vai a **Impostazioni → Impostazioni globali → Tipi di documenti**

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1_it.png" alt="Navigazione delle impostazioni di DocBits in spagnolo con i gruppi Global Settings e Document Processing e le voci di informazioni azienda e permessi utente"><figcaption></figcaption></figure>
2.  Seleziona il tipo di documento desiderato e fai clic su **Altre impostazioni**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2_it.png" alt="Pagina Document Types con l'elenco di Invoice, Credit Note, Delivery Note, Order Confirmation e Contract e le schede Edit layout, Document Sub Types, Table columns e Fields"><figcaption></figcaption></figure>
3.  Nella sezione **Ordine di acquisto**, vai all'opzione **Stati di disabilitazione dell'OP**.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_3_it.png" alt="Pagina More Settings per i tipi di documento con la sezione Purchase Order e l'opzione PO disable statuses evidenziata"><figcaption></figcaption></figure>

### **Come identificare un ordine di acquisto disabilitato**

Nella schermata **Abbinamento OP**, un ordine di acquisto disabilitato appare **sbarrato**. Questo indica visivamente che l'OP è attualmente limitato nell'essere abbinato a causa del suo stato.

<figure><img src="../../../../../../.gitbook/assets/disable_po_status_6.png" alt="Tabella della schermata di PO Matching con le colonne LINE NUMBER, ITEM ID, STATUS, QUANTITY, UNIT PRICE e MATCHED QUANTITY"><figcaption></figcaption></figure>

### **Come configurarlo**

1. Nella impostazione **Stati di disabilitazione dell'OP**, vedrai un campo di selezione sul lato sinistro.
2.  Facendo clic su questo campo si apre un elenco a discesa degli stati OP disponibili.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_4_it.png" alt="Pannello delle impostazioni dello stato PO con interruttore dello stato Purchase Order disattivato e finestra di conferma nell'interfaccia in spagnolo" width="261"><figcaption></figcaption></figure>
3. Seleziona uno o più stati facendo clic su di essi. Fai clic di nuovo per deselezionare.
4.  Fai clic sul pulsante **Applicare** per salvare le tue modifiche.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_5_it.png" alt="Impostazione degli stati disabilitati del PO con i valori selezionati Canceled, Deleted e Invoiced e il pulsante Apply"><figcaption></figcaption></figure>

**Stati disponibili**

* Annullato
* Soppresso
* Fatturato
* Open
* Parzialmente fatturati
* Parzialmente ricevuto
* Ricevuto
* Rifiutato
* Non approvato
* Tenere
* Chiuso
