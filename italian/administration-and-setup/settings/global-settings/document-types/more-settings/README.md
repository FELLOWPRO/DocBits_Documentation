# Altre impostazioni

## Panoramica

Nella sezione "Altre impostazioni", puoi trovare varie opzioni relative ai singoli tipi di documenti. Una volta attivata un'impostazione, si applicherà solo a quel tipo di documento specifico. Questa pagina fornisce una breve panoramica di cosa fa ciascuna impostazione.

## Come accedere

1.  Naviga su **Impostazioni** → **Impostazioni globali** → **Tipi di documenti**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1_it.png" alt=""><figcaption></figcaption></figure>
2.  Seleziona il tipo di documento desiderato e fai clic su **Altre impostazioni**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2_it.png" alt=""><figcaption></figcaption></figure>

## Estrazione della tabella

* **Saltare la convalida della tabella**: Abilita il bypass del processo di convalida standard per i dati della tabella. Questa opzione è utile in scenari in cui è richiesta una gestione dei dati flessibile o quando alcuni passaggi di convalida possono essere saltati per migliorare le prestazioni durante l'elaborazione dei dati.

## Rilevamento dei duplicati

* [**Rilevamento di documenti doppi**](duplicate-document-handling.md): Questo ti consente di rilevare e gestire documenti duplicati.

## In revisione

* **Modulo di revisione del progetto**: Configura il layout dei moduli di revisione utilizzando il **Costruttore di layout**. Questo layout determina come viene presentato il contenuto durante il processo di revisione del documento. Per istruzioni dettagliate su come utilizzare il **Costruttore di layout**, fai clic [qui](../../../../setup/document-types/layout-builder.md).

## Rifiuto

* **Modulo di rifiuto del design**: Configura il layout utilizzando il **Costruttore di layout** per il modulo di rifiuto visualizzato durante il processo di revisione del documento. Per istruzioni dettagliate su come utilizzare il **Costruttore di layout**, fai clic [qui](../../../../setup/document-types/layout-builder.md).

## Esportazione in formato PDF

* **Formato del file di esportazione**: Ti consente di specificare il formato PDF da utilizzare quando si esportano documenti.

## Approvazione

* **Approvare prima dell'esportazione**: Garantisce che i documenti debbano essere approvati prima di poter essere esportati dal sistema. Puoi anche configurare il layout della schermata di approvazione utilizzando il **Costruttore di layout**. Per istruzioni dettagliate su come utilizzare il **Costruttore di layout**, fai clic [qui](../../../../setup/document-types/layout-builder.md).
* **Approvare prima dell'esportazione V2**: Attiva l'Approvazione V2, che supporta l'uso di campi dinamici al posto di quelli statici. Puoi anche personalizzare il layout della schermata di approvazione utilizzando il **Costruttore di layout**. Per istruzioni dettagliate su come utilizzare il **Costruttore di layout**, fai clic [qui](../../../../setup/document-types/layout-builder.md).
* **Seconda approvazione**: Aggiunge un ulteriore livello di approvazione per una convalida migliorata e un maggiore controllo sull'elaborazione dei documenti. Puoi anche personalizzare il layout della schermata di approvazione utilizzando il **Costruttore di layout**. Per istruzioni dettagliate su come utilizzare il **Costruttore di layout**, fai clic [qui](../../../../setup/document-types/layout-builder.md).
* [**Timbro di approvazione**](approval/approval-stamp.md): Aggiunge un timbro al documento quando viene approvato.
* [**Storia dell'approvazione**](approval/approval-history.md): Abilita la visualizzazione della storia dell'approvazione sia nello schermo di approvazione che nella convalida dei campi.

## Ordine di acquisto

* [**Tabella PO nel generatore di layout**](purchase-order/po-table-in-layout-builder.md): Abilita l'inclusione di tabelle degli ordini di acquisto nel generatore di layout per layout di documenti personalizzati.
* [**Controllo automatico degli aggiornamenti dell'OP**](purchase-order/auto-check-for-po-updates.md): Quando abilitato, il sistema visualizza un indicatore visivo nello schermo di corrispondenza degli ordini di acquisto per mostrare quando un ordine di acquisto è stato aggiornato, invitando gli utenti a ricaricare per le ultime informazioni.
* **Aggiornamento automatico dei dati PO**: Attivando questo, i dati PO verranno aggiornati automaticamente quando sono disponibili nuovi dati.
* [**Stato della linea PO consumata**](purchase-order/consumed-po-line-status.md): Questa impostazione migliora lo schermo di corrispondenza degli Ordini di acquisto applicando un codice colore alle righe degli ordini di acquisto.
* [**Calcolo del prezzo unitario dell'OP**](purchase-order/calculate-po-unit-price.md): Questo ti consente di calcolare il prezzo unitario dell'OP utilizzando l'importo netto e la quantità, invece di estrarlo.
* [**Ordine di acquisto**](purchase-order/purchase-order.md): Attiva o disattiva se il documento deve essere elaborato nello schermo di corrispondenza degli ordini di acquisto. Puoi anche specificare su quale termine di quantità deve basarsi il processo di corrispondenza.
* [**Esportazione di righe PO non corrispondenti**](purchase-order/export-not-matched-po-lines.md): Questa funzionalità controlla l'esportazione delle righe degli ordini di acquisto. Quando disabilitata, vengono esportate solo le righe abbinate. Quando abilitata, tutte le righe degli ordini di acquisto vengono esportate, anche se non sono abbinate a una riga di conferma d'ordine.
* [**Impostazione della tolleranza PO**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): Questa funzionalità ti consente di impostare livelli di tolleranza per quantità e prezzo unitario, accogliendo piccole discrepanze senza segnalarle come non corrispondenti.
* [**Impostazione della tolleranza PO aggiuntiva**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#impostazione-per-configurare-le-ulteriori-impostazioni-di-tolleranza-per-gli-ordini-di-acquisto): Questa funzionalità ti consente di impostare livelli di tolleranza aggiuntivi per spedizione, spese e tasse, accogliendo piccole discrepanze senza segnalarle come non corrispondenti.
* [**Esportazione alternativa**](purchase-order/alternate-export.md): Questo ti consente di impostare un'esportazione alternativa per stati specifici.
* [**Stati di disabilitazione dell'OP**](purchase-order/purchase-order-disable-statuses.md): Ti consente di disabilitare stati specifici affinché non vengano considerati nel processo di corrispondenza.
* **Ignorare le linee già abbinate**: Attivando questo verranno saltate le righe che sono già state abbinate durante un nuovo processo di corrispondenza.
* [**Aggiorna lo stato dell'ordine di acquisto del documento**](purchase-order/update-document-purchase-order-status.md): Quando abilitato, la colonna Stato PO sulla dashboard viene aggiornata automaticamente ogni volta che lo stato dell'ordine di acquisto cambia.
* [**Numero di articolo del fornitore Mappa**](purchase-order/supplier-item-number-map-admin-documentation.md): Un'impostazione di utilità che mappa i numeri di articolo del fornitore ai numeri di articolo interni, garantendo precisione nella gestione dell'inventario e degli ordini di acquisto.
