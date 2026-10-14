# Peppol BIS Billing 3.0

### Przegląd

Ta sekcja opisuje plan wdrożenia importowania i mapowania danych z plików XML przy użyciu schematu Peppol BIS Billing 3.0. Peppol BIS Billing 3.0 został opracowany w celu standaryzacji procesów e-fakturowania i zapewnienia zgodności ze standardami europejskimi.

### Cele

* Zapewnienie pełnej zgodności ze specyfikacjami Peppol BIS Billing 3.0.
* Bezproblemowa integracja danych e-faktur z naszym systemem zobowiązań przy użyciu DocBits.
* Poprawa jakości danych i wydajności przetwarzania.

### Zakres

Zakresem tego projektu jest zmapowanie kluczowych elementów schematu Peppol BIS Billing 3.0 na nasze wewnętrzne struktury danych. W szczególności mapowanie obejmie następujące obszary:

* Dane Sprzedawcy i Kupującego
* Dane faktury
* Linie faktury
* Instrukcje płatności
* Informacje podatkowe i prawne

### Kluczowe elementy i mapowanie

**Informacje o dostawcy:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Adres elektroniczny dostawcy
  * cbc:Name: Nazwa handlowa dostawcy
  * cbc:CompanyID: Numer rejestracji prawnej dostawcy
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Dane adresowe dostawcy

**Informacje o kupującym:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Adres elektroniczny kupującego
  * cbc:Name: Nazwa handlowa kupującego
  * cbc:CompanyID: Numer rejestracji prawnej kupującego
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Dane adresowe kupującego

**Dane faktury:**

* cbc:ID: Numer faktury
* cbc:IssueDate: Data wystawienia faktury
* cbc:DueDate: Data wymagalności faktury
* cbc:InvoiceTypeCode: Typ faktury

**Linie faktury:**

* cac:InvoiceLine
  * cbc:ID: Numer linii faktury
  * cbc:InvoicedQuantity: Ilość zafakturowana
  * cbc:LineExtensionAmount: Kwota rozszerzenia linii
  * cbc:Description: Opis pozycji rozliczeniowej
  * cac:Item
    * cbc:Name: Nazwa przedmiotu
    * cbc:SellerItemIdentification/cbc:ID: Numer przedmiotu dostawcy
  * cac:Price
    * cbc:PriceAmount: Cena za jednostkę
    * cbc:BaseQuantity: Ilość bazowa dla ceny

**Instrukcje płatności:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Kod identyfikujący metodę płatności
  * cbc:PaymentID: Identyfikator płatności

**Informacje podatkowe:**

* cac:TaxTotal
  * cbc:TaxAmount: Całkowita kwota podatku
  * cac:TaxSubtotal: Szczegóły dla każdej tymczasowej kwoty podatku

### Podgląd PDF dla e-faktury

Dokument PDF jest generowany zgodnie ze standardowym układem z zaimportowanymi polami, aby zapewnić użytkownikowi podgląd do celów referencyjnych. Dalsze dostosowywanie układu podglądu PDF jest możliwe, ale wymaga dodatkowego wysiłku.
