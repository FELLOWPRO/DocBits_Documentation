# Peppol BIS Billing 3.0

### Panoramica

Questa sezione descrive il piano di implementazione per l'importazione e la mappatura dei dati da file XML utilizzando lo schema Peppol BIS Billing 3.0. Peppol BIS Billing 3.0 è stato sviluppato per standardizzare i processi di fatturazione elettronica e garantire la conformità agli standard europei.

### Obiettivi

* Garantire la piena conformità alle specifiche Peppol BIS Billing 3.0.
* Integrazione perfetta dei dati delle fatture elettroniche nel nostro sistema di contabilità fornitori utilizzando DocBits.
* Migliorare la qualità dei dati e l'efficienza dell'elaborazione.

### Ambito

L'ambito di questo progetto è mappare gli elementi chiave dello schema Peppol BIS Billing 3.0 alle nostre strutture dati interne. In particolare, la mappatura coprirà le seguenti aree:

* Dettagli del Venditore e dell'Acquirente
* Dettagli della fattura
* Righe della fattura
* Istruzioni di pagamento
* Informazioni fiscali e legali

### Elementi chiave e mappatura

**Informazioni sul fornitore:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Indirizzo elettronico del fornitore
  * cbc:Name: Nome commerciale del fornitore
  * cbc:CompanyID: Numero di registrazione legale del fornitore
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Dettagli dell'indirizzo del fornitore

**Informazioni sull'acquirente:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Indirizzo elettronico dell'acquirente
  * cbc:Name: Nome commerciale dell'acquirente
  * cbc:CompanyID: Numero di registrazione legale dell'acquirente
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Dettagli dell'indirizzo dell'acquirente

**Dettagli della fattura:**

* cbc:ID: Numero fattura
* cbc:IssueDate: Data di emissione della fattura
* cbc:DueDate: Data di scadenza della fattura
* cbc:InvoiceTypeCode: Tipo di fattura

**Righe della fattura:**

* cac:InvoiceLine
  * cbc:ID: Numero riga fattura
  * cbc:InvoicedQuantity: Quantità fatturata
  * cbc:LineExtensionAmount: Importo estensione riga
  * cbc:Description: Descrizione della posizione di fatturazione
  * cac:Item
    * cbc:Name: Nome dell'articolo
    * cbc:SellerItemIdentification/cbc:ID: Numero articolo del fornitore
  * cac:Price
    * cbc:PriceAmount: Prezzo per unità
    * cbc:BaseQuantity: Quantità di base per il prezzo

**Istruzioni di pagamento:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Codice per identificare il metodo di pagamento
  * cbc:PaymentID: Identificatore di pagamento

**Informazioni fiscali:**

* cac:TaxTotal
  * cbc:TaxAmount: Importo totale dell'imposta
  * cac:TaxSubtotal: Dettagli per ogni importo d'imposta intermedio

### Anteprima PDF per fattura elettronica

Viene generato un documento PDF secondo un layout standard con i campi importati per fornire all'utente un'anteprima a scopo di riferimento. È possibile un'ulteriore personalizzazione del layout dell'anteprima PDF, ma richiede uno sforzo aggiuntivo.
