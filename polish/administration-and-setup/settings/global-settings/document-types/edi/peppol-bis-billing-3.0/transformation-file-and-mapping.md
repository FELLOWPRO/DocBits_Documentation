# Plik transformacji i mapowanie

## 1. **Cel**

Plik ten odpowiada za wyodrębnianie danych z pliku XML Peppol BIS Billing 3.0, ich przetwarzanie i zapisywanie odpowiednich informacji w określonym formacie. Został zaprojektowany tak, aby umożliwić wyodrębnianie kluczowych pól w celu ułatwienia dalszego przetwarzania lub integracji z DocBits.

## 2. **Przegląd**

* **Plik źródłowy**: Dane wejściowe to plik XML Peppol zgodny ze standardem Peppol BIS Billing 3.0.
* **Proces ekstrakcji**: Plik wykonuje szereg kroków w celu odczytania, przeanalizowania i wyodrębnienia kluczowych elementów, takich jak szczegóły faktury, informacje o dostawcy, kwoty i daty.
* **Dane wyjściowe**: Wyodrębnione dane są przechowywane w ustrukturyzowanym formacie, w innym pliku XML.

## _**3.**_**&#x20;Pobierz** **plik transformacji XML Peppol.**

* Przykład: _Plik ten zawiera logikę transformacji XML Peppol do wyodrębniania i zapisywania danych do innego pliku XML._
* Jeśli wystąpią problemy z bieżącym plikiem lub stanie się on bezużyteczny, pobierz tę wersję zapasową, aby przywrócić funkcjonalność transformacji.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Oto mapowanie:

<details>

<summary>Mapowanie informacji AccountingSupplierParty</summary>



* **Adres elektroniczny dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID schematu adresu elektronicznego dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Identyfikacja dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` w sekcji `Supplier` zostanie wyodrębniony.
* **ID schematu identyfikacji dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` będzie miał odpowiadający mu identyfikator schematu.
* **Nazwa dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu dostawcy 1**
  * **Źródło**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu dostawcy 2**
  * **Źródło**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu dostawcy 3**
  * **Źródło**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Zmapowane do**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Może wystąpić wielokrotnie**: Nie.
* **NIP dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Schemat podatkowy dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Nazwa prawna dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID prawny dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID schematu ID prawnego dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Forma prawna dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod pocztowy dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Miasto dostawcy**
  * **Źródło**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><CITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Podjednostka kraju dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod kraju dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Nazwisko osoby kontaktowej dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Telefon kontaktowy dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **E-mail kontaktowy dostawcy**
  * **Źródło**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Zmapowane do**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Może wystąpić wielokrotnie**: Nie.

</details>

<details>

<summary>Mapowanie informacji AccountingCustomerParty</summary>



* **Adres elektroniczny kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID schematu adresu elektronicznego kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Zmapowane do**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Identyfikacja kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` w sekcji `Buyer` zostanie wyodrębniony.
* **ID schematu identyfikacji kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Zmapowane do**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` będzie miał odpowiadający mu identyfikator schematu.
* **Nazwa kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu kupującego 1**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu kupującego 2**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu kupującego 3**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Może wystąpić wielokrotnie**: Nie.
* **NIP kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><VAT_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Schemat podatkowy kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Nazwa prawna kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID prawny kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID schematu ID prawnego kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Zmapowane do**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Forma prawna kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod pocztowy kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><POST_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Miasto kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><CITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Podjednostka kraju kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod kraju kupującego**
  * **Źródło**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Nazwisko osoby kontaktowej kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Telefon kontaktowy kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **E-mail kontaktowy kupującego**
  * **Źródło**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Zmapowane do**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Może wystąpić wielokrotnie**: Nie.

</details>

<details>

<summary>Mapowanie informacji PayeeParty</summary>



1. **Identyfikacja beneficjenta**
   * **Źródło**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Zmapowane do**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` w sekcji `PayeeParty` zostanie wyodrębniony.
2. **ID schematu identyfikacji beneficjenta**
   * **Źródło**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Zmapowane do**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Może wystąpić wielokrotnie**: Każdy element `<PartyIdentification>` będzie miał odpowiadający mu identyfikator schematu.
3. **Nazwa beneficjenta**
   * **Źródło**: `//PayeeParty/PartyName/Name/text()`
   * **Zmapowane do**: `<INVOICE><PAYEE><NAME>`
   * **Może wystąpić wielokrotnie**: Nie.
4. **ID prawny beneficjenta**
   * **Źródło**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Zmapowane do**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Może wystąpić wielokrotnie**: Nie.
5. **ID schematu ID prawnego beneficjenta**
   * **Źródło**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Zmapowane do**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Może wystąpić wielokrotnie**: Nie.

</details>

<details>

<summary>Mapowanie informacji TaxRepresentativeParty</summary>



* **Nazwa przedstawiciela podatkowego**
  * **Źródło**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu przedstawiciela podatkowego 1**
  * **Źródło**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu przedstawiciela podatkowego 2**
  * **Źródło**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Linia adresu przedstawiciela podatkowego 3**
  * **Źródło**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Może wystąpić wielokrotnie**: Nie.
* **NIP przedstawiciela podatkowego**
  * **Źródło**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Schemat podatkowy przedstawiciela podatkowego**
  * **Źródło**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Miasto przedstawiciela podatkowego**
  * **Źródło**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod pocztowy przedstawiciela podatkowego**
  * **Źródło**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Podjednostka kraju przedstawiciela podatkowego**
  * **Źródło**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Może wystąpić wielokrotnie**: Nie.
* **Kod kraju przedstawiciela podatkowego**
  * **Źródło**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Zmapowane do**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.

</details>

<details>

<summary>Ogólne informacje o fakturze</summary>



1. **Typ faktury**
   * **Źródło**: `"Invoice"`
   * **Zmapowane do**: `<INVOICE><INVOICE_TYPE>`
   * **Może wystąpić wielokrotnie**: Nie.
2. **Podtyp faktury**
   * **Źródło**: `"Purchase Invoice"`
   * **Zmapowane do**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Może wystąpić wielokrotnie**: Nie.
3. **ID faktury**
   * **Źródło**: `//ID/text()`
   * **Zmapowane do**: `<INVOICE><INVOICE_ID>`
   * **Może wystąpić wielokrotnie**: Nie.
4. **Kod typu faktury**
   * **Źródło**: `//InvoiceTypeCode/text()`
   * **Zmapowane do**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Może wystąpić wielokrotnie**: Nie.
5. **Data faktury**
   * **Źródło**: `normalize-space(//IssueDate/text())`
   * **Zmapowane do**: `<INVOICE><INVOICE_DATE>`
   * **Może wystąpić wielokrotnie**: Nie.
   * **Przetwarzanie**: Używa szablonu `DateTimeString` do formatowania.
6. **Data płatności**
   * **Źródło**: `normalize-space(//DueDate/text())`
   * **Zmapowane do**: `<INVOICE><DUE_DATE>`
   * **Może wystąpić wielokrotnie**: Nie.
   * **Przetwarzanie**: Używa szablonu `DateTimeString` do formatowania.
7. **Data obowiązku podatkowego**
   * **Źródło**: `normalize-space(//TaxPointDate/text())`
   * **Zmapowane do**: `<INVOICE><TAX_POINT_DATE>`
   * **Może wystąpić wielokrotnie**: Nie.
   * **Przetwarzanie**: Używa szablonu `DateTimeString` do formatowania.
8. **Uwaga do faktury**
   * **Źródło**: `//Note/text()`
   * **Zmapowane do**: `<INVOICE><INVOICE_NOTE>`
   * **Może wystąpić wielokrotnie**: Nie.
9. **Kod waluty dokumentu**
   * **Źródło**: `//DocumentCurrencyCode/text()`
   * **Zmapowane do**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Może wystąpić wielokrotnie**: Nie.
10. **Kod waluty podatku**
    * **Źródło**: `//TaxCurrencyCode/text()`
    * **Zmapowane do**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Może wystąpić wielokrotnie**: Nie.
11. **Koszt księgowy**
    * **Źródło**: `//AccountingCost/text()`
    * **Zmapowane do**: `<INVOICE><ACCOUNTING_COST>`
    * **Może wystąpić wielokrotnie**: Nie.
12. **Data rozpoczęcia okresu objętego fakturą**
    * **Źródło**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Zmapowane do**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Może wystąpić wielokrotnie**: Nie.
    * **Przetwarzanie**: Używa szablonu `DateTimeString` do formatowania.
13. **Data zakończenia okresu objętego fakturą**
    * **Źródło**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Zmapowane do**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Może wystąpić wielokrotnie**: Nie.
    * **Przetwarzanie**: Używa szablonu `DateTimeString` do formatowania.
14. **Kod opisu okresu objętego fakturą**
    * **Źródło**: `//InvoicePeriod/DescriptionCode/text()`
    * **Zmapowane do**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Może wystąpić wielokrotnie**: Nie.
15. **Referencja zamówienia zakupu**
    * **Źródło**: `//OrderReference/ID/text()`
    * **Zmapowane do**: `<INVOICE><PURCHASE_ORDER>`
    * **Może wystąpić wielokrotnie**: Nie.
16. **Referencja zamówienia sprzedaży**
    * **Źródło**: `//OrderReference/SalesOrderID/text()`
    * **Zmapowane do**: `<INVOICE><SALES_ORDER>`
    * **Może wystąpić wielokrotnie**: Nie.

</details>

<details>

<summary>Mapowanie referencji dokumentów i dodatkowych szczegółów dokumentu</summary>

1. **Referencja kupującego**
   * **Źródło**: `//BuyerReference/text()`
   * **Zmapowane do**: `<INVOICE><BUYER_REFERENCE>`
   * **Może wystąpić wielokrotnie**: Nie.

2)  **Referencja bilingowa**

    * **Źródło**: `//BillingReference`
    * **Zmapowane do**: `<INVOICE><BILLING_REFERENCE>`
    * **Może wystąpić wielokrotnie**: Tak. Każdy element `<BillingReference>` w danych źródłowych wygeneruje element `<BILLING_REFERENCE>`.

    **Dla każdej referencji bilingowej:**

    * **NUMER\_POPRZEDNIEJ\_FAKTURY**
      * **Źródło**: `InvoiceDocumentReference/ID/text()`
      * **Zmapowane do**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Może wystąpić wielokrotnie**: Nie.
    * **DATA\_WYSTAWIENIA\_POPRZEDNIEJ\_FAKTURY**
      * **Źródło**: `InvoiceDocumentReference/IssueDate/text()`
      * **Zmapowane do**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Może wystąpić wielokrotnie**: Nie.

3. **Referencja dokumentu wysyłkowego**
   * **Źródło**: `//DespatchDocumentReference/ID/text()`
   * **Zmapowane do**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Może wystąpić wielokrotnie**: Nie.

4) **Referencja dokumentu odbioru**
   * **Źródło**: `//ReceiptDocumentReference/ID/text()`
   * **Zmapowane do**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Może wystąpić wielokrotnie**: Nie.

5. **Referencja dokumentu wystawcy**
   1. **Źródło**: `//OriginatorDocumentReference/ID/text()`
   2. **Zmapowane do**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Może wystąpić wielokrotnie**: Nie.

#### Referencja dokumentu umowy

* **Źródło**: `//ContractDocumentReference/ID/text()`
* **Zmapowane do**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Może wystąpić wielokrotnie**: Nie.

#### Referencja projektu

* **Źródło**: `//ProjectReference/ID/text()`
* **Zmapowane do**: `<INVOICE><PROJECT_REFERENCE>`
* **Może wystąpić wielokrotnie**: Nie.

#### Dodatkowa referencja dokumentu

* **Źródło**: `//AdditionalDocumentReference`
* **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Może wystąpić wielokrotnie**: Tak. Każdy element `<AdditionalDocumentReference>` w danych źródłowych wygeneruje element `<ADDITIONAL_DOCUMENT_REFERENCE>`.

**Dla każdej dodatkowej referencji dokumentu:**

* **ID**
  * **Źródło**: `ID/text()`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **ID\_SCHEMATU**
  * **Źródło**: `ID/@schemeID`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Może wystąpić wielokrotnie**: Nie.
* **KOD\_TYPU\_DOKUMENTU**
  * **Źródło**: `DocumentTypeCode/text()`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **OPIS\_DOKUMENTU**
  * **Źródło**: `DocumentDescription/text()`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Może wystąpić wielokrotnie**: Nie.

**Informacje o załączniku (dla każdej dodatkowej referencji dokumentu):**

* **OBIEKT\_BINARNY\_DOKUMENTU\_OSADZONEGO**
  * **Źródło**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Może wystąpić wielokrotnie**: Nie.
* **KOD\_MIME**
  * **Źródło**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Może wystąpić wielokrotnie**: Nie.
* **NAZWA\_PLIKU**
  * **Źródło**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Może wystąpić wielokrotnie**: Nie.
* **URL\_REFERENCJI\_ZEWNĘTRZNEJ**
  * **Źródło**: `Attachment/ExternalReference/URI/text()`
  * **Zmapowane do**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Może wystąpić wielokrotnie**: Nie.

</details>
