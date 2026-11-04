# Peppol BIS Billing 3.0

### Overzicht

Deze sectie beschrijft het implementatieplan voor het importeren en koppelen van XML-gegevens volgens Peppol BIS Billing 3.0. Deze specificatie is ontwikkeld om elektronische facturatie te standaardiseren en aansluiting op Europese normen te ondersteunen.

### Doelstellingen&#x20;

* Volledig voldoen aan de specificaties van Peppol BIS Billing 3.0.
* Elektronische factuurgegevens met DocBits in de crediteurenadministratie integreren.
* De gegevenskwaliteit en verwerkingsefficiëntie verbeteren.

### Reikwijdte&#x20;

Dit project koppelt belangrijke elementen van Peppol BIS Billing 3.0 aan onze interne gegevensstructuren. De mapping omvat vooral de volgende gebieden:

* Gegevens van leverancier en koper
* Factuurgegevens&#x20;
* Factuurregels
* Betalingsinstructies
* Fiscale en juridische informatie

### Belangrijke elementen en mapping

**Leveranciersgegevens:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: elektronisch adres van de leverancier
  * cbc:Name: handelsnaam van de leverancier
  * cbc:CompanyID: wettelijk registratienummer van de leverancier
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: adresgegevens van de leverancier

**Kopersgegevens:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: elektronisch adres van de koper
  * cbc:Name: handelsnaam van de koper
  * cbc:CompanyID: wettelijk registratienummer van de koper
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: adresgegevens van de koper

**Factuurgegevens:**

* cbc:ID: factuurnummer
* cbc:IssueDate: uitgiftedatum van de factuur
* cbc:DueDate: vervaldatum van de factuur
* cbc:InvoiceTypeCode: factuurtype

**Factuurregels:**

* cac:InvoiceLine
  * cbc:ID: factuurregelnummer
  * cbc:InvoicedQuantity: gefactureerde hoeveelheid
  * cbc:LineExtensionAmount: regelbedrag
  * cbc:Description: omschrijving van de factuurregel
  * cac:Item
    * cbc:Name: artikelnaam
    * cbc:SellerItemIdentification/cbc:ID: artikelnummer van de leverancier
  * cac:Price
    * cbc:PriceAmount: prijs per eenheid
    * cbc:BaseQuantity: basishoeveelheid voor de prijs

**Betalingsinstructies:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: code van de betaalmethode
  * cbc:PaymentID: betalingsidentificatie

**Belastinggegevens:**

* cac:TaxTotal
  * cbc:TaxAmount: totaal belastingbedrag
  * cac:TaxSubtotal: uitsplitsing per belastingdeelbedrag

### PDF-voorbeeld van de elektronische factuur

Voor de gebruiker wordt ter referentie een PDF met een standaardlay-out en de geïmporteerde velden gegenereerd. Verdere aanpassing van deze PDF-lay-out is mogelijk, maar vereist extra werk.
