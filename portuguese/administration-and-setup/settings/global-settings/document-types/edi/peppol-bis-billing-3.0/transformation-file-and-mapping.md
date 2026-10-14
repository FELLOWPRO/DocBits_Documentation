# Arquivo de transformação e Mapeamento

## 1. **Objetivo**

Este arquivo é responsável por extrair dados de um arquivo XML Peppol BIS Billing 3.0, processá-los e salvar as informações relevantes em um formato especificado. Ele foi projetado para permitir a extração de campos principais para facilitar o processamento posterior ou a integração no DocBits.

## 2. **Visão geral**

* **Arquivo de Origem**: A entrada é um arquivo XML Peppol que segue o padrão Peppol BIS Billing 3.0.
* **Processo de Extração**: O arquivo executa uma série de etapas para ler, analisar e extrair elementos-chave, como detalhes da fatura, informações do fornecedor, valores e datas.
* **Saída**: Os dados extraídos são armazenados em um formato estruturado, em outro arquivo XML.

## _**3.**_**&#x20;Download** **do Arquivo de Transformação XML Peppol.**

* Exemplo: _Este arquivo contém a lógica de transformação XML Peppol para extrair e salvar dados em outro arquivo XML._
* Se você encontrar problemas com seu arquivo atual ou se ele se tornar inutilizável, baixe esta versão de backup para restaurar a funcionalidade de transformação.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Aqui está o Mapeamento:

<details>

<summary>Mapeamento de Informações do AccountingSupplierParty</summary>



* **Endereço Eletrônico do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Pode aparecer várias vezes**: Não.
* **ID do Esquema do Endereço Eletrônico do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Mapeado para**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Identificação do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` sob `Supplier` será extraído.
* **ID do Esquema de Identificação do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapeado para**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` terá seu ID de esquema correspondente.
* **Nome do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><NAME>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Fornecedor Linha 1**
  * **Origem**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Fornecedor Linha 2**
  * **Origem**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Fornecedor Linha 3**
  * **Origem**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapeado para**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Pode aparecer várias vezes**: Não.
* **ID de IVA do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Esquema de Imposto do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Pode aparecer várias vezes**: Não.
* **Nome Legal do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Pode aparecer várias vezes**: Não.
* **ID Legal do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Pode aparecer várias vezes**: Não.
* **ID do Esquema do ID Legal do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapeado para**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Forma Legal do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Pode aparecer várias vezes**: Não.
* **Código Postal do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **Cidade do Fornecedor**
  * **Origem**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><CITY>`
  * **Pode aparecer várias vezes**: Não.
* **Subentidade do País do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Pode aparecer várias vezes**: Não.
* **Código do País do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **Nome de Contato do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Pode aparecer várias vezes**: Não.
* **Telefone de Contato do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Pode aparecer várias vezes**: Não.
* **E-mail de Contato do Fornecedor**
  * **Origem**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Mapeado para**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Pode aparecer várias vezes**: Não.

</details>

<details>

<summary>Mapeamento de Informações do AccountingCustomerParty</summary>



* **Endereço Eletrônico do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Mapeado para**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Pode aparecer várias vezes**: Não.
* **ID do Esquema do Endereço Eletrônico do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Mapeado para**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Identificação do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Mapeado para**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` sob `Buyer` será extraído.
* **ID do Esquema de Identificação do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapeado para**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` terá seu ID de esquema correspondente.
* **Nome do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Mapeado para**: `<INVOICE><BUYER><NAME>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Comprador Linha 1**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Mapeado para**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Comprador Linha 2**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado para**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Comprador Linha 3**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapeado para**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Pode aparecer várias vezes**: Não.
* **ID de IVA do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapeado para**: `<INVOICE><BUYER><VAT_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Esquema de Imposto do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado para**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Pode aparecer várias vezes**: Não.
* **Nome Legal do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapeado para**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Pode aparecer várias vezes**: No.
* **ID Legal do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapeado para**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Pode aparecer várias vezes**: Não.
* **ID do Esquema do ID Legal do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapeado para**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Forma Legal do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapeado para**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Pode aparecer várias vezes**: Não.
* **Código Postal do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Mapeado para**: `<INVOICE><BUYER><POST_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **Cidade do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Mapeado para**: `<INVOICE><BUYER><CITY>`
  * **Pode aparecer várias vezes**: Não.
* **Subentidade do País do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapeado para**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Pode aparecer várias vezes**: Não.
* **Código do País do Comprador**
  * **Origem**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado para**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **Nome de Contato do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Mapeado para**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Pode aparecer várias vezes**: Não.
* **Telefone de Contato do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Mapeado para**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Pode aparecer várias vezes**: Não.
* **E-mail de Contato do Comprador**
  * **Origem**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Mapeado para**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Pode aparecer várias vezes**: Não.

</details>

<details>

<summary>Mapeamento de Informações do PayeeParty</summary>



1. **Identificação do Beneficiário**
   * **Origem**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Mapeado para**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` sob `PayeeParty` será extraído.
2. **ID do Esquema de Identificação do Beneficiário**
   * **Origem**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Mapeado para**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Pode aparecer várias vezes**: Cada elemento `<PartyIdentification>` terá seu ID de esquema correspondente.
3. **Nome do Beneficiário**
   * **Origem**: `//PayeeParty/PartyName/Name/text()`
   * **Mapeado para**: `<INVOICE><PAYEE><NAME>`
   * **Pode aparecer várias vezes**: Não.
4. **ID Legal do Beneficiário**
   * **Origem**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Mapeado para**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Pode aparecer várias vezes**: Não.
5. **ID do Esquema do ID Legal do Beneficiário**
   * **Origem**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Mapeado para**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Pode aparecer várias vezes**: Não.

</details>

<details>

<summary>Mapeamento de Informações do TaxRepresentativeParty</summary>



* **Nome do Representante Fiscal**
  * **Origem**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Representante Fiscal Linha 1**
  * **Origem**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Representante Fiscal Linha 2**
  * **Origem**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Pode aparecer várias vezes**: Não.
* **Endereço do Representante Fiscal Linha 3**
  * **Origem**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Pode aparecer várias vezes**: Não.
* **ID de IVA do Representante Fiscal**
  * **Origem**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Pode aparecer várias vezes**: Não.
* **Esquema de Imposto do Representante Fiscal**
  * **Origem**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Pode aparecer várias vezes**: Não.
* **Cidade do Representante Fiscal**
  * **Origem**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Pode aparecer várias vezes**: Não.
* **Código Postal do Representante Fiscal**
  * **Origem**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **Subentidade do País do Representante Fiscal**
  * **Origem**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Pode aparecer várias vezes**: Não.
* **Código do País do Representante Fiscal**
  * **Origem**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado para**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Pode aparecer várias vezes**: Não.

</details>

<details>

<summary>Informações Gerais da Fatura</summary>



1. **Tipo de Fatura**
   * **Origem**: `"Invoice"`
   * **Mapeado para**: `<INVOICE><INVOICE_TYPE>`
   * **Pode aparecer várias vezes**: Não.
2. **Subtipo de Fatura**
   * **Origem**: `"Purchase Invoice"`
   * **Mapeado para**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Pode aparecer várias vezes**: Não.
3. **ID da Fatura**
   * **Origem**: `//ID/text()`
   * **Mapeado para**: `<INVOICE><INVOICE_ID>`
   * **Pode aparecer várias vezes**: Não.
4. **Código do Tipo de Fatura**
   * **Origem**: `//InvoiceTypeCode/text()`
   * **Mapeado para**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Pode aparecer várias vezes**: Não.
5. **Data da Fatura**
   * **Origem**: `normalize-space(//IssueDate/text())`
   * **Mapeado para**: `<INVOICE><INVOICE_DATE>`
   * **Pode aparecer várias vezes**: Não.
   * **Processamento**: Usa o modelo `DateTimeString` para formatação.
6. **Data de Vencimento**
   * **Origem**: `normalize-space(//DueDate/text())`
   * **Mapeado para**: `<INVOICE><DUE_DATE>`
   * **Pode aparecer várias vezes**: Não.
   * **Processamento**: Usa o modelo `DateTimeString` para formatação.
7. **Data do Ponto de Imposto**
   * **Origem**: `normalize-space(//TaxPointDate/text())`
   * **Mapeado para**: `<INVOICE><TAX_POINT_DATE>`
   * **Pode aparecer várias vezes**: Não.
   * **Processamento**: Usa o modelo `DateTimeString` para formatação.
8. **Nota da Fatura**
   * **Origem**: `//Note/text()`
   * **Mapeado para**: `<INVOICE><INVOICE_NOTE>`
   * **Pode aparecer várias vezes**: Não.
9. **Código de Moeda do Documento**
   * **Origem**: `//DocumentCurrencyCode/text()`
   * **Mapeado para**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Pode aparecer várias vezes**: Não.
10. **Código de Moeda de Imposto**
    * **Origem**: `//TaxCurrencyCode/text()`
    * **Mapeado para**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Pode aparecer várias vezes**: Não.
11. **Custo Contábil**
    * **Origem**: `//AccountingCost/text()`
    * **Mapeado para**: `<INVOICE><ACCOUNTING_COST>`
    * **Pode aparecer várias vezes**: Não.
12. **Data de Início do Período da Fatura**
    * **Origem**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Mapeado para**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Pode aparecer várias vezes**: Não.
    * **Processamento**: Usa o modelo `DateTimeString` para formatação.
13. **Data de Término do Período da Fatura**
    * **Origem**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Mapeado para**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Pode aparecer várias vezes**: Não.
    * **Processamento**: Usa o modelo `DateTimeString` para formatação.
14. **Código de Descrição do Período da Fatura**
    * **Origem**: `//InvoicePeriod/DescriptionCode/text()`
    * **Mapeado para**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Pode aparecer várias vezes**: Não.
15. **Referência do Pedido de Compra**
    * **Origem**: `//OrderReference/ID/text()`
    * **Mapeado para**: `<INVOICE><PURCHASE_ORDER>`
    * **Pode aparecer várias vezes**: Não.
16. **Referência do Pedido de Venda**
    * **Origem**: `//OrderReference/SalesOrderID/text()`
    * **Mapeado para**: `<INVOICE><SALES_ORDER>`
    * **Pode aparecer várias vezes**: Não.

</details>

<details>

<summary>Mapeamento de Referências de Documentos e Detalhes Adicionais de Documentos</summary>

1. **Referência do Comprador**
   * **Origem**: `//BuyerReference/text()`
   * **Mapeado para**: `<INVOICE><BUYER_REFERENCE>`
   * **Pode aparecer várias vezes**: Não.

2)  **Referência de Faturamento**

    * **Origem**: `//BillingReference`
    * **Mapeado para**: `<INVOICE><BILLING_REFERENCE>`
    * **Pode aparecer várias vezes**: Sim. Cada elemento `<BillingReference>` nos dados de origem gerará um elemento `<BILLING_REFERENCE>`.

    **Para cada Referência de Faturamento:**

    * **NÚMERO\_DA\_FATURA\_ANTERIOR**
      * **Origem**: `InvoiceDocumentReference/ID/text()`
      * **Mapeado para**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Pode aparecer várias vezes**: Não.
    * **DATA\_DE\_EMISSÃO\_DA\_FATURA\_ANTERIOR**
      * **Origem**: `InvoiceDocumentReference/IssueDate/text()`
      * **Mapeado para**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Pode aparecer várias vezes**: Não.

3. **Referência do Documento de Despacho**
   * **Origem**: `//DespatchDocumentReference/ID/text()`
   * **Mapeado para**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Pode aparecer várias vezes**: Não.

4) **Referência do Documento de Recebimento**
   * **Origem**: `//ReceiptDocumentReference/ID/text()`
   * **Mapeado para**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Pode aparecer várias vezes**: Não.

5. **Referência do Documento Originador**
   1. **Origem**: `//OriginatorDocumentReference/ID/text()`
   2. **Mapeado para**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Pode aparecer várias vezes**: Não.

#### Referência do Documento de Contrato

* **Origem**: `//ContractDocumentReference/ID/text()`
* **Mapeado para**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Pode aparecer várias vezes**: Não.

#### Referência do Projeto

* **Origem**: `//ProjectReference/ID/text()`
* **Mapeado para**: `<INVOICE><PROJECT_REFERENCE>`
* **Pode aparecer várias vezes**: Não.

#### Referência de Documento Adicional

* **Origem**: `//AdditionalDocumentReference`
* **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Pode aparecer várias vezes**: Sim. Cada elemento `<AdditionalDocumentReference>` nos dados de origem gerará um elemento `<ADDITIONAL_DOCUMENT_REFERENCE>`.

**Para cada Referência de Documento Adicional:**

* **ID**
  * **Origem**: `ID/text()`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Pode aparecer várias vezes**: Não.
* **ID\_DO\_ESQUEMA**
  * **Origem**: `ID/@schemeID`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Pode aparecer várias vezes**: Não.
* **CÓDIGO\_DO\_TIPO\_DE\_DOCUMENTO**
  * **Origem**: `DocumentTypeCode/text()`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **DESCRIÇÃO\_DO\_DOCUMENTO**
  * **Origem**: `DocumentDescription/text()`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Pode aparecer várias vezes**: Não.

**Informações de Anexo (para cada Referência de Documento Adicional):**

* **OBJETO\_BINÁRIO\_DO\_DOCUMENTO\_EMBUTIDO**
  * **Origem**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Pode aparecer várias vezes**: Não.
* **CÓDIGO\_MIME**
  * **Origem**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Pode aparecer várias vezes**: Não.
* **NOME\_DO\_ARQUIVO**
  * **Origem**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Pode aparecer várias vezes**: Não.
* **URL\_DE\_REFERÊNCIA\_EXTERNA**
  * **Origem**: `Attachment/ExternalReference/URI/text()`
  * **Mapeado para**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Pode aparecer várias vezes**: Não.

</details>
