# File di trasformazione e Mappatura

## 1. **Scopo**

Questo file è responsabile dell'estrazione dei dati da un file XML Peppol BIS Billing 3.0, della loro elaborazione e del salvataggio delle informazioni rilevanti in un formato specificato. È progettato per consentire l'estrazione di campi chiave per facilitare l'ulteriore elaborazione o l'integrazione in DocBits.

## 2. **Panoramica**

* **File sorgente**: L'input è un file XML Peppol che segue lo standard Peppol BIS Billing 3.0.
* **Processo di estrazione**: Il file esegue una serie di passaggi per leggere, analizzare ed estrarre elementi chiave come dettagli della fattura, informazioni sul fornitore, importi e date.
* **Output**: I dati estratti vengono memorizzati in un formato strutturato, in un altro file XML.

## _**3.**_**&#x20;Scarica** **il file di trasformazione XML Peppol.**

* Esempio: _Questo file contiene la logica di trasformazione XML Peppol per estrarre e salvare i dati in un altro file XML._
* Se riscontri problemi con il tuo file attuale o se diventa inutilizzabile, scarica questa versione di backup per ripristinare la funzionalità di trasformazione.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Ecco la mappatura:

<details>

<summary>Mappatura delle informazioni dell'AccountingSupplierParty</summary>



* **Indirizzo elettronico del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Può apparire più volte**: No.
* **ID dello schema dell'indirizzo elettronico del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Mappato su**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Può apparire più volte**: No.
* **Identificazione del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Può apparire più volte**: Verrà estratto ogni elemento `<PartyIdentification>` sotto `Supplier`.
* **ID dello schema di identificazione del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Mappato su**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Può apparire più volte**: Ogni elemento `<PartyIdentification>` avrà il suo ID di schema corrispondente.
* **Nome del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><NAME>`
  * **Può apparire più volte**: No.
* **Indirizzo del fornitore riga 1**
  * **Sorgente**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Può apparire più volte**: No.
* **Indirizzo del fornitore riga 2**
  * **Sorgente**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Può apparire più volte**: No.
* **Indirizzo del fornitore riga 3**
  * **Sorgente**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mappato su**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Può apparire più volte**: No.
* **Partita IVA del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Può apparire più volte**: No.
* **Schema fiscale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Può apparire più volte**: No.
* **Ragione sociale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Può apparire più volte**: No.
* **ID legale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Può apparire più volte**: No.
* **ID dello schema dell'ID legale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mappato su**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Può apparire più volte**: No.
* **Forma legale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Può apparire più volte**: No.
* **Codice postale del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Può apparire più volte**: No.
* **Città del fornitore**
  * **Sorgente**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><CITY>`
  * **Può apparire più volte**: No.
* **Sottoentità nazionale del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Può apparire più volte**: No.
* **Codice paese del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Può apparire più volte**: No.
* **Nome del referente del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Può apparire più volte**: No.
* **Telefono del referente del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Può apparire più volte**: No.
* **Email del referente del fornitore**
  * **Sorgente**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Mappato su**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Può apparire più volte**: No.

</details>

<details>

<summary>Mappatura delle informazioni dell'AccountingCustomerParty</summary>



* **Indirizzo elettronico dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Mappato su**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Può apparire più volte**: No.
* **ID dello schema dell'indirizzo elettronico dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Mappato su**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Può apparire più volte**: No.
* **Identificazione dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Mappato su**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Può apparire più volte**: Verrà estratto ogni elemento `<PartyIdentification>` sotto `Buyer`.
* **ID dello schema di identificazione dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Mappato su**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Può apparire più volte**: Ogni elemento `<PartyIdentification>` avrà il suo ID di schema corrispondente.
* **Nome dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Mappato su**: `<INVOICE><BUYER><NAME>`
  * **Può apparire più volte**: No.
* **Indirizzo dell'acquirente riga 1**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Mappato su**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Può apparire più volte**: No.
* **Indirizzo dell'acquirente riga 2**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mappato su**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Può apparire più volte**: No.
* **Indirizzo dell'acquirente riga 3**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mappato su**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Può apparire più volte**: No.
* **ID fiscale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mappato su**: `<INVOICE><BUYER><VAT_ID>`
  * **Può apparire più volte**: No.
* **Schema fiscale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappato su**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Può apparire più volte**: No.
* **Ragione sociale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mappato su**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Può apparire più volte**: No.
* **ID legale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mappato su**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Può apparire più volte**: No.
* **ID dello schema dell'ID legale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mappato su**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Può apparire più volte**: No.
* **Forma legale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mappato su**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Può apparire più volte**: No.
* **Codice postale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Mappato su**: `<INVOICE><BUYER><POST_CODE>`
  * **Può apparire più volte**: No.
* **Città dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Mappato su**: `<INVOICE><BUYER><CITY>`
  * **Può apparire più volte**: No.
* **Sottoentità nazionale dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mappato su**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Può apparire più volte**: No.
* **Codice paese dell'acquirente**
  * **Sorgente**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mappato su**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Può apparire più volte**: No.
* **Nome del referente dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Mappato su**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Può apparire più volte**: No.
* **Telefono del referente dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Mappato su**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Può apparire più volte**: No.
* **Email del referente dell'acquirente**
  * **Sorgente**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Mappato su**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Può apparire più volte**: No.

</details>

<details>

<summary>Mappatura delle informazioni della PayeeParty</summary>



1. **Identificazione del beneficiario**
   * **Sorgente**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Mappato su**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Può apparire più volte**: Verrà estratto ogni elemento `<PartyIdentification>` sotto `PayeeParty`.
2. **ID dello schema di identificazione del beneficiario**
   * **Sorgente**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Mappato su**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Può apparire più volte**: Ogni elemento `<PartyIdentification>` avrà il suo ID di schema corrispondente.
3. **Nome del beneficiario**
   * **Sorgente**: `//PayeeParty/PartyName/Name/text()`
   * **Mappato su**: `<INVOICE><PAYEE><NAME>`
   * **Può apparire più volte**: No.
4. **ID legale del beneficiario**
   * **Sorgente**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Mappato su**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Può apparire più volte**: No.
5. **ID dello schema dell'ID legale del beneficiario**
   * **Sorgente**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Mappato su**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Può apparire più volte**: No.

</details>

<details>

<summary>Mappatura delle informazioni della TaxRepresentativeParty</summary>



* **Nome del rappresentante fiscale**
  * **Sorgente**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Può apparire più volte**: No.
* **Indirizzo del rappresentante fiscale riga 1**
  * **Sorgente**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Può apparire più volte**: No.
* **Indirizzo del rappresentante fiscale riga 2**
  * **Sorgente**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Può apparire più volte**: No.
* **Indirizzo del rappresentante fiscale riga 3**
  * **Sorgente**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Può apparire più volte**: No.
* **Partita IVA del rappresentante fiscale**
  * **Sorgente**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Può apparire più volte**: No.
* **Schema fiscale del rappresentante fiscale**
  * **Sorgente**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Può apparire più volte**: No.
* **Città del rappresentante fiscale**
  * **Sorgente**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Può apparire più volte**: No.
* **Codice postale del rappresentante fiscale**
  * **Sorgente**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Può apparire più volte**: No.
* **Sottoentità nazionale del rappresentante fiscale**
  * **Sorgente**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Può apparire più volte**: No.
* **Codice paese del rappresentante fiscale**
  * **Sorgente**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Mappato su**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Può apparire più volte**: No.

</details>

<details>

<summary>Informazioni generali sulla fattura</summary>



1. **Tipo di fattura**
   * **Sorgente**: `"Invoice"`
   * **Mappato su**: `<INVOICE><INVOICE_TYPE>`
   * **Può apparire più volte**: No.
2. **Sottotipo di fattura**
   * **Sorgente**: `"Purchase Invoice"`
   * **Mappato su**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Può apparire più volte**: No.
3. **ID della fattura**
   * **Sorgente**: `//ID/text()`
   * **Mappato su**: `<INVOICE><INVOICE_ID>`
   * **Può apparire più volte**: No.
4. **Codice del tipo di fattura**
   * **Sorgente**: `//InvoiceTypeCode/text()`
   * **Mappato su**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Può apparire più volte**: No.
5. **Data della fattura**
   * **Sorgente**: `normalize-space(//IssueDate/text())`
   * **Mappato su**: `<INVOICE><INVOICE_DATE>`
   * **Può apparire più volte**: No.
   * **Elaborazione**: Utilizza il modello `DateTimeString` per la formattazione.
6. **Data di scadenza**
   * **Sorgente**: `normalize-space(//DueDate/text())`
   * **Mappato su**: `<INVOICE><DUE_DATE>`
   * **Può apparire più volte**: No.
   * **Elaborazione**: Utilizza il modello `DateTimeString` per la formattazione.
7. **Data del punto fiscale**
   * **Sorgente**: `normalize-space(//TaxPointDate/text())`
   * **Mappato su**: `<INVOICE><TAX_POINT_DATE>`
   * **Può apparire più volte**: No.
   * **Elaborazione**: Utilizza il modello `DateTimeString` per la formattazione.
8. **Nota della fattura**
   * **Sorgente**: `//Note/text()`
   * **Mappato su**: `<INVOICE><INVOICE_NOTE>`
   * **Può apparire più volte**: No.
9. **Codice valuta del documento**
   * **Sorgente**: `//DocumentCurrencyCode/text()`
   * **Mappato su**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Può apparire più volte**: No.
10. **Codice valuta fiscale**
    * **Sorgente**: `//TaxCurrencyCode/text()`
    * **Mappato su**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Può apparire più volte**: No.
11. **Costo contabile**
    * **Sorgente**: `//AccountingCost/text()`
    * **Mappato su**: `<INVOICE><ACCOUNTING_COST>`
    * **Può apparire più volte**: No.
12. **Data inizio periodo fattura**
    * **Sorgente**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Mappato su**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Può apparire più volte**: No.
    * **Elaborazione**: Utilizza il modello `DateTimeString` per la formattazione.
13. **Data fine periodo fattura**
    * **Sorgente**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Mappato su**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Può apparire più volte**: No.
    * **Elaborazione**: Utilizza il modello `DateTimeString` per la formattazione.
14. **Codice descrizione periodo fattura**
    * **Sorgente**: `//InvoicePeriod/DescriptionCode/text()`
    * **Mappato su**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Può apparire più volte**: No.
15. **Riferimento ordine di acquisto**
    * **Sorgente**: `//OrderReference/ID/text()`
    * **Mappato su**: `<INVOICE><PURCHASE_ORDER>`
    * **Può apparire più volte**: No.
16. **Riferimento ordine di vendita**
    * **Sorgente**: `//OrderReference/SalesOrderID/text()`
    * **Mappato su**: `<INVOICE><SALES_ORDER>`
    * **Può apparire più volte**: No.

</details>

<details>

<summary>Mappatura dei riferimenti ai documenti e dettagli aggiuntivi del documento</summary>

1. **Riferimento dell'acquirente**
   * **Sorgente**: `//BuyerReference/text()`
   * **Mappato su**: `<INVOICE><BUYER_REFERENCE>`
   * **Può apparire più volte**: No.

2)  **Riferimento di fatturazione**

    * **Sorgente**: `//BillingReference`
    * **Mappato su**: `<INVOICE><BILLING_REFERENCE>`
    * **Può apparire più volte**: Sì. Ogni elemento `<BillingReference>` nei dati sorgente genererà un elemento `<BILLING_REFERENCE>`.

    **Per ogni riferimento di fatturazione:**

    * **NUMERO\_FATTURA\_PRECEDENTE**
      * **Sorgente**: `InvoiceDocumentReference/ID/text()`
      * **Mappato su**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Può apparire più volte**: No.
    * **DATA\_EMISSIONE\_FATTURA\_PRECEDENTE**
      * **Sorgente**: `InvoiceDocumentReference/IssueDate/text()`
      * **Mappato su**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Può apparire più volte**: No.

3. **Riferimento del documento di spedizione**
   * **Sorgente**: `//DespatchDocumentReference/ID/text()`
   * **Mappato su**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Può apparire più volte**: No.

4) **Riferimento del documento di ricezione**
   * **Sorgente**: `//ReceiptDocumentReference/ID/text()`
   * **Mappato su**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Può apparire più volte**: No.

5. **Riferimento del documento del creatore**
   1. **Sorgente**: `//OriginatorDocumentReference/ID/text()`
   2. **Mappato su**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Può apparire più volte**: No.

#### Riferimento del documento di contratto

* **Sorgente**: `//ContractDocumentReference/ID/text()`
* **Mappato su**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Può apparire più volte**: No.

#### Riferimento del progetto

* **Sorgente**: `//ProjectReference/ID/text()`
* **Mappato su**: `<INVOICE><PROJECT_REFERENCE>`
* **Può apparire più volte**: No.

#### Riferimento al documento aggiuntivo

* **Sorgente**: `//AdditionalDocumentReference`
* **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Può apparire più volte**: Sì. Ogni elemento `<AdditionalDocumentReference>` nei dati sorgente genererà un elemento `<ADDITIONAL_DOCUMENT_REFERENCE>`.

**Per ogni riferimento al documento aggiuntivo:**

* **ID**
  * **Sorgente**: `ID/text()`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Può apparire più volte**: No.
* **ID\_SCHEMA**
  * **Sorgente**: `ID/@schemeID`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Può apparire più volte**: No.
* **CODICE\_TIPO\_DOCUMENTO**
  * **Sorgente**: `DocumentTypeCode/text()`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Può apparire più volte**: No.
* **DESCRIZIONE\_DOCUMENTO**
  * **Sorgente**: `DocumentDescription/text()`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Può apparire più volte**: No.

**Informazioni sugli allegati (per ogni riferimento al documento aggiuntivo):**

* **OGGETTO\_BINARIO\_DOCUMENTO\_INCORPORATO**
  * **Sorgente**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Può apparire più volte**: No.
* **CODICE\_MIME**
  * **Sorgente**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Può apparire più volte**: No.
* **NOME\_FILE**
  * **Sorgente**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Può apparire più volte**: No.
* **URL\_RIFERIMENTO\_ESTERNO**
  * **Sorgente**: `Attachment/ExternalReference/URI/text()`
  * **Mappato su**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Può apparire più volte**: No.

</details>
