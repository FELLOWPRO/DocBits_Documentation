# Mapowanie pól ZUGFeRD 2.2

## Przegląd

ZUGFeRD 2.2 kontynuuje dostosowanie do EN 16931 i uwzględnia dalsze aktualizacje standardu CII.

## Mapowanie pól nagłówka

### Identyfikacja faktury

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Numer faktury |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data wystawienia faktury |

### Typ i podtyp dokumentu (sterowane przez TRA)

Domyślny TRANSFORMATION XSLT emituje dwa pola pochodne:

| Pole DocBits | Źródło | Logika |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` lub `261` → **Credit Note**; dowolny inny kod → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niepuste → **Purchase Invoice**; puste/brakujące → **Cost Invoice** |

### Podział podatków (klasyfikowany według poziomów)

Bloki `ApplicableTradeTax` są rozdzielane na trzy poziomy oparte na stawce (nie według indeksów pozycyjnych): pola stawki standardowej (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) obejmują stawkę ≥ 19; pola stawki obniżonej (`*_2`) obejmują 0 < stawka < 19; pola stawki zerowej (`*_3`) obejmują stawkę = 0. Pełną listę pól znajdziesz w [Podział podatków ZUGFeRD](../README.md#podzial-podatkow-klasyfikowany-wedlug-poziomow).

### Waluta i kwoty

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Waluta faktury |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Łączna kwota netto |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Łączna kwota podatku |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Suma końcowa |

## Mapowanie pozycji

| Ścieżka ZUGFeRD CII | Pole DocBits | Pole Infor BOD | Typ | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Numer pozycji |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Opis pozycji |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Ilość zafakturowana |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Cena jednostkowa netto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Wartość pozycji |
