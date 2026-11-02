# Transformatiebestand en mapping

## 1. **Doel**

Dit bestand haalt gegevens uit een PEPPOL BIS Billing 3.0-XML-bestand, verwerkt ze en slaat relevante informatie in een opgegeven formaat op. Het extraheert belangrijke velden voor verdere verwerking of integratie in DocBits.

## 2. **Overzicht**

* **Bronbestand**: de invoer is een PEPPOL-XML-bestand volgens de norm PEPPOL BIS Billing 3.0.
* **Extractieproces**: het bestand leest en ontleedt de invoer en extraheert belangrijke elementen, zoals factuurgegevens, leveranciersinformatie, bedragen en datums.
* **Uitvoer**: de geëxtraheerde gegevens worden gestructureerd opgeslagen in een ander XML-bestand.

## **3. Het PEPPOL-XML-transformatiebestand downloaden**

* Voorbeeld: _dit bestand bevat de PEPPOL-XML-transformatielogica om gegevens te extraheren en in een ander XML-bestand op te slaan._
* Download deze reserveversie als uw huidige bestand problemen veroorzaakt of onbruikbaar is geworden, om de transformatiefunctie te herstellen.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### De mapping:

<details>

<summary>Gegevensmapping voor AccountingSupplierParty </summary>



* **Elektronisch adres van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Kan meermaals voorkomen**: nee.
* **Schema-ID van het elektronische leveranciersadres**
  * **Bron**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Leveranciersidentificatie**
  * **Bron**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element onder `Supplier` wordt geëxtraheerd.
* **Schema-ID van de leveranciersidentificatie**
  * **Bron**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element krijgt het bijbehorende schema-ID.
* **Leveranciersnaam**
  * **Bron**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 1 van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 2 van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 3 van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Gekoppeld aan**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Kan meermaals voorkomen**: nee.
* **Btw-nummer van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Belastingschema van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Kan meermaals voorkomen**: nee.
* **Statutaire naam van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Wettelijk identificatienummer van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Schema-ID van het wettelijke identificatienummer van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Rechtsvorm van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Kan meermaals voorkomen**: nee.
* **Postcode van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **Plaats van de leverancier**
  * **Bron**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><CITY>`
  * **Kan meermaals voorkomen**: nee.
* **Deelgebied van het land van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Kan meermaals voorkomen**: nee.
* **Landcode van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **Naam van de contactpersoon van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Telefoonnummer van de contactpersoon van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Kan meermaals voorkomen**: nee.
* **E-mailadres van de contactpersoon van de leverancier**
  * **Bron**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Gekoppeld aan**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Kan meermaals voorkomen**: nee.

</details>

<details>

<summary>Gegevensmapping voor AccountingCustomerParty</summary>



* **Elektronisch adres van de koper**
  * **Bron**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Kan meermaals voorkomen**: nee.
* **Schema-ID van het elektronische kopersadres**
  * **Bron**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Kopersidentificatie**
  * **Bron**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element onder `Buyer` wordt geëxtraheerd.
* **Schema-ID van de kopersidentificatie**
  * **Bron**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element krijgt het bijbehorende schema-ID.
* **Naam van de koper**
  * **Bron**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 1 van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 2 van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 3 van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Kan meermaals voorkomen**: nee.
* **Btw-nummer van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><VAT_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Belastingschema van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Kan meermaals voorkomen**: nee.
* **Statutaire naam van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Wettelijk identificatienummer van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Schema-ID van het wettelijke identificatienummer van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Rechtsvorm van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Kan meermaals voorkomen**: nee.
* **Postcode van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><POST_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **Plaats van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><CITY>`
  * **Kan meermaals voorkomen**: nee.
* **Deelgebied van het land van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Kan meermaals voorkomen**: nee.
* **Landcode van de koper**
  * **Bron**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **Naam van de contactpersoon van de koper**
  * **Bron**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Telefoonnummer van de contactpersoon van de koper**
  * **Bron**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Kan meermaals voorkomen**: nee.
* **E-mailadres van de contactpersoon van de koper**
  * **Bron**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Gekoppeld aan**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Kan meermaals voorkomen**: nee.

</details>

<details>

<summary>Gegevensmapping voor PayeeParty</summary>



1. **Identificatie van de begunstigde**
   * **Bron**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Gekoppeld aan**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element onder `PayeeParty` wordt geëxtraheerd.
2. **Schema-ID van de identificatie van de begunstigde**
   * **Bron**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Gekoppeld aan**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Kan meermaals voorkomen**: elk `<PartyIdentification>`-element krijgt het bijbehorende schema-ID.
3. **Naam van de begunstigde**
   * **Bron**: `//PayeeParty/PartyName/Name/text()`
   * **Gekoppeld aan**: `<INVOICE><PAYEE><NAME>`
   * **Kan meermaals voorkomen**: nee.
4. **Wettelijk identificatienummer van de begunstigde**
   * **Bron**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Gekoppeld aan**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Kan meermaals voorkomen**: nee.
5. **Schema-ID van het wettelijke identificatienummer van de begunstigde**
   * **Bron**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Gekoppeld aan**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Kan meermaals voorkomen**: nee.

</details>

<details>

<summary>Gegevensmapping voor TaxRepresentativeParty</summary>



* **Naam van de fiscaal vertegenwoordiger**
  * **Bron**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 1 van de fiscaal vertegenwoordiger**
  * **Bron**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 2 van de fiscaal vertegenwoordiger**
  * **Bron**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Kan meermaals voorkomen**: nee.
* **Adresregel 3 van de fiscaal vertegenwoordiger**
  * **Bron**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Kan meermaals voorkomen**: nee.
* **Btw-nummer van de fiscaal vertegenwoordiger**
  * **Bron**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Kan meermaals voorkomen**: nee.
* **Belastingschema van de fiscaal vertegenwoordiger**
  * **Bron**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Kan meermaals voorkomen**: nee.
* **Plaats van de fiscaal vertegenwoordiger**
  * **Bron**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Kan meermaals voorkomen**: nee.
* **Postcode van de fiscaal vertegenwoordiger**
  * **Bron**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **Deelgebied van het land van de fiscaal vertegenwoordiger**
  * **Bron**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Kan meermaals voorkomen**: nee.
* **Landcode van de fiscaal vertegenwoordiger**
  * **Bron**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Gekoppeld aan**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Kan meermaals voorkomen**: nee.

</details>

<details>

<summary>Algemene factuurgegevens </summary>



1. **Factuurtype**
   * **Bron**: `"Invoice"`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_TYPE>`
   * **Kan meermaals voorkomen**: nee.
2. **Factuursubtype**
   * **Bron**: `"Purchase Invoice"`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Kan meermaals voorkomen**: nee.
3. **Factuur-ID**
   * **Bron**: `//ID/text()`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_ID>`
   * **Kan meermaals voorkomen**: nee.
4. **Factuurtypecode**
   * **Bron**: `//InvoiceTypeCode/text()`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Kan meermaals voorkomen**: nee.
5. **Factuurdatum**
   * **Bron**: `normalize-space(//IssueDate/text())`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_DATE>`
   * **Kan meermaals voorkomen**: nee.
   * **Verwerking**: gebruikt het sjabloon `DateTimeString` voor de opmaak.
6. **Vervaldatum**
   * **Bron**: `normalize-space(//DueDate/text())`
   * **Gekoppeld aan**: `<INVOICE><DUE_DATE>`
   * **Kan meermaals voorkomen**: nee.
   * **Verwerking**: gebruikt het sjabloon `DateTimeString` voor de opmaak.
7. **Datum van het belastbare feit**
   * **Bron**: `normalize-space(//TaxPointDate/text())`
   * **Gekoppeld aan**: `<INVOICE><TAX_POINT_DATE>`
   * **Kan meermaals voorkomen**: nee.
   * **Verwerking**: gebruikt het sjabloon `DateTimeString` voor de opmaak.
8. **Factuuropmerking**
   * **Bron**: `//Note/text()`
   * **Gekoppeld aan**: `<INVOICE><INVOICE_NOTE>`
   * **Kan meermaals voorkomen**: nee.
9. **Valutacode van het document**
   * **Bron**: `//DocumentCurrencyCode/text()`
   * **Gekoppeld aan**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Kan meermaals voorkomen**: nee.
10. **Valutacode voor belasting**
    * **Bron**: `//TaxCurrencyCode/text()`
    * **Gekoppeld aan**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Kan meermaals voorkomen**: nee.
11. **Boekhoudkundige kosten**
    * **Bron**: `//AccountingCost/text()`
    * **Gekoppeld aan**: `<INVOICE><ACCOUNTING_COST>`
    * **Kan meermaals voorkomen**: nee.
12. **Begindatum van de factuurperiode**
    * **Bron**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Gekoppeld aan**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Kan meermaals voorkomen**: nee.
    * **Verwerking**: gebruikt het sjabloon `DateTimeString` voor de opmaak.
13. **Einddatum van de factuurperiode**
    * **Bron**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Gekoppeld aan**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Kan meermaals voorkomen**: nee.
    * **Verwerking**: gebruikt het sjabloon `DateTimeString` voor de opmaak.
14. **Beschrijvingscode van de factuurperiode**
    * **Bron**: `//InvoicePeriod/DescriptionCode/text()`
    * **Gekoppeld aan**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Kan meermaals voorkomen**: nee.
15. **Inkooporderreferentie**
    * **Bron**: `//OrderReference/ID/text()`
    * **Gekoppeld aan**: `<INVOICE><PURCHASE_ORDER>`
    * **Kan meermaals voorkomen**: nee.
16. **Verkooporderreferentie**
    * **Bron**: `//OrderReference/SalesOrderID/text()`
    * **Gekoppeld aan**: `<INVOICE><SALES_ORDER>`
    * **Kan meermaals voorkomen**: nee.

</details>

<details>

<summary>Mapping van documentreferenties en aanvullende documentgegevens</summary>

1. **Kopersreferentie**
   * **Bron**: `//BuyerReference/text()`
   * **Gekoppeld aan**: `<INVOICE><BUYER_REFERENCE>`
   * **Kan meermaals voorkomen**: nee.

2)  **Factuurreferentie**

    * **Bron**: `//BillingReference`
    * **Gekoppeld aan**: `<INVOICE><BILLING_REFERENCE>`
    * **Kan meermaals voorkomen**: ja. Elk `<BillingReference>`-element in de brongegevens levert een `<BILLING_REFERENCE>`-element op.

    **Voor elke factuurreferentie:**

    * **PRECEDING\_INVOICE\_NUMBER**
      * **Bron**: `InvoiceDocumentReference/ID/text()`
      * **Gekoppeld aan**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Kan meermaals voorkomen**: nee.
    * **PRECEDING\_INVOICE\_ISSUE\_DATE**
      * **Bron**: `InvoiceDocumentReference/IssueDate/text()`
      * **Gekoppeld aan**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Kan meermaals voorkomen**: nee.

3. **Referentie naar het verzenddocument**
   * **Bron**: `//DespatchDocumentReference/ID/text()`
   * **Gekoppeld aan**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Kan meermaals voorkomen**: nee.

4) **Referentie naar het ontvangstdocument**
   * **Bron**: `//ReceiptDocumentReference/ID/text()`
   * **Gekoppeld aan**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Kan meermaals voorkomen**: nee.

5. **Referentie naar het brondocument**
   1. **Bron**: `//OriginatorDocumentReference/ID/text()`
   2. **Gekoppeld aan**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Kan meermaals voorkomen**: nee.

#### Referentie naar het contractdocument

* **Bron**: `//ContractDocumentReference/ID/text()`
* **Gekoppeld aan**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Kan meermaals voorkomen**: nee.

#### Projectreferentie

* **Bron**: `//ProjectReference/ID/text()`
* **Gekoppeld aan**: `<INVOICE><PROJECT_REFERENCE>`
* **Kan meermaals voorkomen**: nee.

#### Aanvullende documentreferentie

* **Bron**: `//AdditionalDocumentReference`
* **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Kan meermaals voorkomen**: ja. Elk `<AdditionalDocumentReference>`-element in de brongegevens levert een `<ADDITIONAL_DOCUMENT_REFERENCE>`-element op.

**Voor elke aanvullende documentreferentie:**

* **ID**
  * **Bron**: `ID/text()`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Kan meermaals voorkomen**: nee.
* **SCHEME\_ID**
  * **Bron**: `ID/@schemeID`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Kan meermaals voorkomen**: nee.
* **DOCUMENT\_TYPE\_CODE**
  * **Bron**: `DocumentTypeCode/text()`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **DOCUMENT\_DESCRIPTION**
  * **Bron**: `DocumentDescription/text()`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Kan meermaals voorkomen**: nee.

**Bijlagegegevens voor elke aanvullende documentreferentie:**

* **EMBEDDED\_DOCUMENT\_BINARY\_OBJECT**
  * **Bron**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Kan meermaals voorkomen**: nee.
* **MIME\_CODE**
  * **Bron**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Kan meermaals voorkomen**: nee.
* **FILENAME**
  * **Bron**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Kan meermaals voorkomen**: nee.
* **EXTERNAL\_REFERENCE\_URL**
  * **Bron**: `Attachment/ExternalReference/URI/text()`
  * **Gekoppeld aan**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Kan meermaals voorkomen**: nee.

</details>

