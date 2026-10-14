# Peppol BIS Billing 3.0

### Überblick

Dieser Abschnitt beschreibt den Implementierungsplan für den Import und die Zuordnung von Daten aus XML-Dateien unter Verwendung des Peppol BIS Billing 3.0-Schemas. Peppol BIS Billing 3.0 wurde entwickelt, um elektronische Rechnungsstellungsprozesse zu standardisieren und die Einhaltung europäischer Standards sicherzustellen.

### Ziele

* Sicherstellung der vollständigen Konformität mit den Peppol BIS Billing 3.0-Spezifikationen.
* Nahtlose Integration von E-Rechnungsdaten in unser Kreditorenbuchhaltungssystem mit DocBits.
* Verbesserung der Datenqualität und der Verarbeitungseffizienz.

### Umfang

Der Umfang dieses Projekts besteht darin, Schlüsselelemente des Peppol BIS Billing 3.0-Schemas unseren internen Datenstrukturen zuzuordnen. Insbesondere wird die Zuordnung die folgenden Bereiche abdecken:

* Verkäufer- und Käuferdetails
* Rechnungsdetails
* Rechnungspositionen
* Zahlungsanweisungen
* Steuer- und rechtliche Informationen

### Schlüsselelemente und Zuordnung

**Verkäuferinformationen:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Elektronische Adresse des Verkäufers
  * cbc:Name: Handelsname des Verkäufers
  * cbc:CompanyID: Gesetzliche Registrierungsnummer des Verkäufers
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Adressdetails des Verkäufers

**Käuferinformationen:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Elektronische Adresse des Käufers
  * cbc:Name: Handelsname des Käufers
  * cbc:CompanyID: Gesetzliche Registrierungsnummer des Käufers
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Adressdetails des Käufers

**Rechnungsdetails:**

* cbc:ID: Rechnungsnummer
* cbc:IssueDate: Ausstellungsdatum der Rechnung
* cbc:DueDate: Fälligkeitsdatum der Rechnung
* cbc:InvoiceTypeCode: Rechnungstyp

**Rechnungspositionen:**

* cac:InvoiceLine
  * cbc:ID: Rechnungspositionsnummer
  * cbc:InvoicedQuantity: In Rechnung gestellte Menge
  * cbc:LineExtensionAmount: Zeilenerweiterungsbetrag
  * cbc:Description: Beschreibung der Abrechnungsposition
  * cac:Item
    * cbc:Name: Artikelname
    * cbc:SellerItemIdentification/cbc:ID: Artikelnummer des Verkäufers
  * cac:Price
    * cbc:PriceAmount: Preis pro Einheit
    * cbc:BaseQuantity: Basismenge für den Preis

**Zahlungsanweisungen:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Code zur Identifizierung der Zahlungsmethode
  * cbc:PaymentID: Zahlungskennung

**Steuerinformationen:**

* cac:TaxTotal
  * cbc:TaxAmount: Gesamtsteuerbetrag
  * cac:TaxSubtotal: Details für jeden Zwischensteuerbetrag

### PDF-Vorschau für E-Rechnung

Es wird ein PDF-Dokument gemäß einem Standardlayout mit den importierten Feldern generiert, um dem Benutzer eine Vorschau zu Referenzzwecken zur Verfügung zu stellen. Eine weitere Anpassung des PDF-Vorschaulayouts ist möglich, erfordert jedoch zusätzlichen Aufwand.
