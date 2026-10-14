# Transformationsdatei und Zuordnung

## 1. **Zweck**

Diese Datei ist dafür verantwortlich, Daten aus einer PEPPOL BIS Billing 3.0 XML-Datei zu extrahieren, zu verarbeiten und die relevanten Informationen in einem bestimmten Format zu speichern. Sie ist darauf ausgelegt, die Extraktion von Schlüsselfeldern zu ermöglichen, um die weitere Verarbeitung oder Integration in DocBits zu erleichtern.

## 2. **Überblick**

* **Quelldatei**: Die Eingabe ist eine PEPPOL-XML-Datei, die dem PEPPOL BIS Billing 3.0-Standard entspricht.
* **Extraktionsprozess**: Die Datei führt eine Reihe von Schritten aus, um Schlüsselelemente wie Rechnungsdetails, Lieferanteninformationen, Beträge und Daten zu lesen, zu analysieren und zu extrahieren.
* **Ausgabe**: Die extrahierten Daten werden in einem strukturierten Format in einer anderen XML-Datei gespeichert.

## _**3.**_**&#x20;Herunterladen** **der PEPPOL-XML-Transformationsdatei.**

* Beispiel: _Diese Datei enthält die PEPPOL-XML-Transformationslogik zum Extrahieren und Speichern von Daten in einer anderen XML-Datei._
* Wenn Sie Probleme mit Ihrer aktuellen Datei haben oder diese unbrauchbar wird, laden Sie diese Backup-Version herunter, um die Transformationsfunktionalität wiederherzustellen.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Hier ist die Zuordnung:

<details>

<summary>Zuordnung der AccountingSupplierParty-Informationen</summary>



* **Elektronische Adresse des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Kann mehrfach vorkommen**: Nein.
* **Schema-ID der elektronischen Adresse des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferantenidentifikation**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element unter `Supplier` wird extrahiert.
* **Schema-ID der Lieferantenidentifikation**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element hat seine entsprechende Schema-ID.
* **Name des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferantenadresse Zeile 1**
  * **Quelle**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferantenadresse Zeile 2**
  * **Quelle**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferantenadresse Zeile 3**
  * **Quelle**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Zugeordnet zu**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferanten-USt-ID**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Lieferanten-Steuerschema**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtlicher Name des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtliche ID des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Schema-ID der rechtlichen ID des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtsform des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Kann mehrfach vorkommen**: Nein.
* **Postleitzahl des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Stadt des Lieferanten**
  * **Quelle**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><CITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländersubentität des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländercode des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontaktname des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontakttelefon des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontakt-E-Mail des Lieferanten**
  * **Quelle**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Zugeordnet zu**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Kann mehrfach vorkommen**: Nein.

</details>

<details>

<summary>Zuordnung der AccountingCustomerParty-Informationen</summary>



* **Elektronische Adresse des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Kann mehrfach vorkommen**: Nein.
* **Schema-ID der elektronischen Adresse des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käuferidentifikation**
  * **Quelle**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element unter `Buyer` wird extrahiert.
* **Schema-ID der Käuferidentifikation**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element hat seine entsprechende Schema-ID.
* **Name des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käuferadresse Zeile 1**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käuferadresse Zeile 2**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käuferadresse Zeile 3**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käufer-USt-ID**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><VAT_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Käufer-Steuerschema**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtlicher Name des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtliche ID des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Schema-ID der rechtlichen ID des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Rechtsform des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Kann mehrfach vorkommen**: Nein.
* **Postleitzahl des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><POST_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Stadt des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><CITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländersubentität des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländercode des Käufers**
  * **Quelle**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontaktname des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontakttelefon des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Kontakt-E-Mail des Käufers**
  * **Quelle**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Zugeordnet zu**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Kann mehrfach vorkommen**: Nein.

</details>

<details>

<summary>Zuordnung der PayeeParty-Informationen</summary>



1. **Empfängeridentifikation**
   * **Quelle**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Zugeordnet zu**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element unter `PayeeParty` wird extrahiert.
2. **Schema-ID der Empfängeridentifikation**
   * **Quelle**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Zugeordnet zu**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Kann mehrfach vorkommen**: Jedes `<PartyIdentification>`-Element hat seine entsprechende Schema-ID.
3. **Name des Empfängers**
   * **Quelle**: `//PayeeParty/PartyName/Name/text()`
   * **Zugeordnet zu**: `<INVOICE><PAYEE><NAME>`
   * **Kann mehrfach vorkommen**: Nein.
4. **Rechtliche ID des Empfängers**
   * **Quelle**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Zugeordnet zu**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Kann mehrfach vorkommen**: Nein.
5. **Schema-ID der rechtlichen ID des Empfängers**
   * **Quelle**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Zugeordnet zu**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Kann mehrfach vorkommen**: Nein.

</details>

<details>

<summary>Zuordnung der TaxRepresentativeParty-Informationen</summary>



* **Name des Steuervertreters**
  * **Quelle**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Steuervertreter Adresse Zeile 1**
  * **Quelle**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Kann mehrfach vorkommen**: Nein.
* **Steuervertreter Adresse Zeile 2**
  * **Quelle**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Kann mehrfach vorkommen**: Nein.
* **Steuervertreter Adresse Zeile 3**
  * **Quelle**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Kann mehrfach vorkommen**: Nein.
* **Steuervertreter-USt-ID**
  * **Quelle**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **Steuervertreter-Steuerschema**
  * **Quelle**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Kann mehrfach vorkommen**: Nein.
* **Stadt des Steuervertreters**
  * **Quelle**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Postleitzahl des Steuervertreters**
  * **Quelle**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländersubentität des Steuervertreters**
  * **Quelle**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Kann mehrfach vorkommen**: Nein.
* **Ländercode des Steuervertreters**
  * **Quelle**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Zugeordnet zu**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Kann mehrfach vorkommen**: Nein.

</details>

<details>

<summary>Allgemeine Rechnungsinformationen</summary>



1. **Rechnungstyp**
   * **Quelle**: `"Invoice"`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_TYPE>`
   * **Kann mehrfach vorkommen**: Nein.
2. **Rechnungsuntertyp**
   * **Quelle**: `"Purchase Invoice"`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Kann mehrfach vorkommen**: Nein.
3. **Rechnungs-ID**
   * **Quelle**: `//ID/text()`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_ID>`
   * **Kann mehrfach vorkommen**: Nein.
4. **Rechnungstypcode**
   * **Quelle**: `//InvoiceTypeCode/text()`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Kann mehrfach vorkommen**: Nein.
5. **Rechnungsdatum**
   * **Quelle**: `normalize-space(//IssueDate/text())`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_DATE>`
   * **Kann mehrfach vorkommen**: Nein.
   * **Verarbeitung**: Verwendet die `DateTimeString`-Vorlage zur Formatierung.
6. **Fälligkeitsdatum**
   * **Quelle**: `normalize-space(//DueDate/text())`
   * **Zugeordnet zu**: `<INVOICE><DUE_DATE>`
   * **Kann mehrfach vorkommen**: Nein.
   * **Verarbeitung**: Verwendet die `DateTimeString`-Vorlage zur Formatierung.
7. **Steuerpunktdatum**
   * **Quelle**: `normalize-space(//TaxPointDate/text())`
   * **Zugeordnet zu**: `<INVOICE><TAX_POINT_DATE>`
   * **Kann mehrfach vorkommen**: Nein.
   * **Verarbeitung**: Verwendet die `DateTimeString`-Vorlage zur Formatierung.
8. **Rechnungshinweis**
   * **Quelle**: `//Note/text()`
   * **Zugeordnet zu**: `<INVOICE><INVOICE_NOTE>`
   * **Kann mehrfach vorkommen**: Nein.
9. **Währungscode des Dokuments**
   * **Quelle**: `//DocumentCurrencyCode/text()`
   * **Zugeordnet zu**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Kann mehrfach vorkommen**: Nein.
10. **Steuerwährungscode**
    * **Quelle**: `//TaxCurrencyCode/text()`
    * **Zugeordnet zu**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Kann mehrfach vorkommen**: Nein.
11. **Buchhaltungskosten**
    * **Quelle**: `//AccountingCost/text()`
    * **Zugeordnet zu**: `<INVOICE><ACCOUNTING_COST>`
    * **Kann mehrfach vorkommen**: Nein.
12. **Startdatum des Rechnungszeitraums**
    * **Quelle**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Zugeordnet zu**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Kann mehrfach vorkommen**: Nein.
    * **Verarbeitung**: Verwendet die `DateTimeString`-Vorlage zur Formatierung.
13. **Enddatum des Rechnungszeitraums**
    * **Quelle**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Zugeordnet zu**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Kann mehrfach vorkommen**: Nein.
    * **Verarbeitung**: Verwendet die `DateTimeString`-Vorlage zur Formatierung.
14. **Beschreibungscode des Rechnungszeitraums**
    * **Quelle**: `//InvoicePeriod/DescriptionCode/text()`
    * **Zugeordnet zu**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Kann mehrfach vorkommen**: Nein.
15. **Bestellreferenz**
    * **Quelle**: `//OrderReference/ID/text()`
    * **Zugeordnet zu**: `<INVOICE><PURCHASE_ORDER>`
    * **Kann mehrfach vorkommen**: Nein.
16. **Verkaufsauftragsreferenz**
    * **Quelle**: `//OrderReference/SalesOrderID/text()`
    * **Zugeordnet zu**: `<INVOICE><SALES_ORDER>`
    * **Kann mehrfach vorkommen**: Nein.

</details>

<details>

<summary>Zuordnung von Dokumentenreferenzen und zusätzlichen Dokumentendetails</summary>

1. **Käuferreferenz**
   * **Quelle**: `//BuyerReference/text()`
   * **Zugeordnet zu**: `<INVOICE><BUYER_REFERENCE>`
   * **Kann mehrfach vorkommen**: Nein.

2)  **Abrechnungsreferenz**

    * **Quelle**: `//BillingReference`
    * **Zugeordnet zu**: `<INVOICE><BILLING_REFERENCE>`
    * **Kann mehrfach vorkommen**: Ja. Jedes `<BillingReference>`-Element in den Quelldaten generiert ein `<BILLING_REFERENCE>`-Element.

    **Für jede Abrechnungsreferenz:**

    * **PRECEDING\_INVOICE\_NUMBER**
      * **Quelle**: `InvoiceDocumentReference/ID/text()`
      * **Zugeordnet zu**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Kann mehrfach vorkommen**: Nein.
    * **PRECEDING\_INVOICE\_ISSUE\_DATE**
      * **Quelle**: `InvoiceDocumentReference/IssueDate/text()`
      * **Zugeordnet zu**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Kann mehrfach vorkommen**: Nein.

3. **Versanddokumentenreferenz**
   * **Quelle**: `//DespatchDocumentReference/ID/text()`
   * **Zugeordnet zu**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Kann mehrfach vorkommen**: Nein.

4) **Empfangsdokumentenreferenz**
   * **Quelle**: `//ReceiptDocumentReference/ID/text()`
   * **Zugeordnet zu**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Kann mehrfach vorkommen**: Nein.

5. **Urheberdokumentenreferenz**
   1. **Quelle**: `//OriginatorDocumentReference/ID/text()`
   2. **Zugeordnet zu**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Kann mehrfach vorkommen**: Nein.

#### Vertragsdokumentenreferenz

* **Quelle**: `//ContractDocumentReference/ID/text()`
* **Zugeordnet zu**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Kann mehrfach vorkommen**: Nein.

#### Projektreferenz

* **Quelle**: `//ProjectReference/ID/text()`
* **Zugeordnet zu**: `<INVOICE><PROJECT_REFERENCE>`
* **Kann mehrfach vorkommen**: Nein.

#### Zusätzliche Dokumentenreferenz

* **Quelle**: `//AdditionalDocumentReference`
* **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Kann mehrfach vorkommen**: Ja. Jedes `<AdditionalDocumentReference>`-Element in den Quelldaten generiert ein `<ADDITIONAL_DOCUMENT_REFERENCE>`-Element.

**Für jede zusätzliche Dokumentenreferenz:**

* **ID**
  * **Quelle**: `ID/text()`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **SCHEME\_ID**
  * **Quelle**: `ID/@schemeID`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Kann mehrfach vorkommen**: Nein.
* **DOCUMENT\_TYPE\_CODE**
  * **Quelle**: `DocumentTypeCode/text()`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **DOCUMENT\_DESCRIPTION**
  * **Quelle**: `DocumentDescription/text()`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Kann mehrfach vorkommen**: Nein.

**Anhangsinformationen (für jede zusätzliche Dokumentenreferenz):**

* **EMBEDDED\_DOCUMENT\_BINARY\_OBJECT**
  * **Quelle**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Kann mehrfach vorkommen**: Nein.
* **MIME\_CODE**
  * **Quelle**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Kann mehrfach vorkommen**: Nein.
* **FILENAME**
  * **Quelle**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Kann mehrfach vorkommen**: Nein.
* **EXTERNAL\_REFERENCE\_URL**
  * **Quelle**: `Attachment/ExternalReference/URI/text()`
  * **Zugeordnet zu**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Kann mehrfach vorkommen**: Nein.

</details>
