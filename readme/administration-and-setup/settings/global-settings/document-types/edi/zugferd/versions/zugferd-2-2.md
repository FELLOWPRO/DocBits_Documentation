# Mapowanie pól ZUGFeRD 2.2

## Przegląd

ZUGFeRD 2.2 był początkową wersją standardu. Choć jest to wersja starsza, wiele dokumentów nadal korzysta z tego formatu. DocBits zapewnia pełną obsługę wyodrębniania danych z plików XML ZUGFeRD 2.2.

## Mapowanie pól nagłówka

### Identyfikacja faktury

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Numer faktury |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Kod typu faktury |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data wystawienia faktury |

### Typ i podtyp dokumentu (sterowane przez TRA)

Domyślny TRANSFORMATION XSLT emituje dwa pola pochodne:

| Pole DocBits | Źródło | Logika |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` lub `261` → **Credit Note**; dowolny inny kod → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niepuste → **Purchase Invoice**; puste/brakujące → **Cost Invoice** |

### Podział podatków (klasyfikowany według poziomów)

Bloki `ApplicableTradeTax` są rozdzielane na trzy poziomy oparte na stawce (nie pozycyjnie): pola stawki standardowej (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) obejmują stawkę ≥ 19; pola stawki obniżonej (`*_2`) obejmują 0 < stawka < 19; pola stawki zerowej (`*_3`) obejmują stawkę = 0. Pełną listę pól znajdziesz w [Podział podatków ZUGFeRD](../README.md#tax-breakdown-tier-classified).

### Odniesienia do dokumentów

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numer zamówienia zakupu |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Odniesienie do umowy |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Odniesienie do dowodu dostawy |

### Informacje o dostawcy (sprzedawcy)

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID dostawcy |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nazwa dostawcy |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Linia adresu 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Kod pocztowy |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Miasto |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Kod kraju |

## Mapowanie pozycji liniowych

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Numer pozycji |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numer pozycji kupującego |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Opis pozycji |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Ilość zafakturowana |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Cena jednostkowa netto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Suma pozycji |
