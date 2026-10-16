# Mapowanie ZUGFeRD 2.3.2

## Przegląd

ZUGFeRD 2.3.2 to wydanie konserwacyjne standardu 2.3, zapewniające zgodność z najnowszymi aktualizacjami CII.

## Mapowanie pól nagłówka

### Identyfikacja faktury

| Ścieżka ZUGFeRD CII               | Pole DocBits     | Pole Infor BOD     | Typ    | Opis                     |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Numer faktury            |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Data wystawienia faktury |

### Typ i podtyp dokumentu (sterowane przez TRA)

Domyślny TRANSFORMATION XSLT emituje dwa pola pochodne:

| Pole DocBits       | Źródło                                                                                                     | Logika                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` lub `261` → **Credit Note**; dowolny inny kod → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niepuste → **Purchase Invoice**; puste/brakujące → **Cost Invoice**         |

### Podział podatków (klasyfikowany według poziomów)

Bloki `ApplicableTradeTax` są rozdzielane na trzy poziomy oparte na stawce (nie pozycyjnie `[1]`/`[2]`/`[3]`): pola stawki standardowej (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) obejmują stawkę ≥ 19; pola stawki obniżonej (`*_2`) obejmują 0 < stawka < 19; pola stawki zerowej (`*_3`) obejmują stawkę = 0. Pełną listę pól znajdziesz w [Podział podatków ZUGFeRD](./#podzial-podatkow-klasyfikowany-wedlug-poziomow).

| Ścieżka ZUGFeRD CII                                   | Pole DocBits | Pole Infor BOD  | Typ    | Opis                              |
| ----------------------------------------------------- | ------------ | --------------- | ------ | --------------------------------- |
| `ApplicableTradeTax/RateApplicablePercent` (poziom 1) | `TAX_RATE`   | `TaxPercent`    | NUMBER | Standardowa stawka VAT (≥ 19)     |
| `ApplicableTradeTax/BasisAmount` (poziom 1)           | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Kwota netto stawki standardowej   |
| `ApplicableTradeTax/CalculatedAmount` (poziom 1)      | `TAX_AMOUNT` | `TaxAmount`     | AMOUNT | Kwota podatku stawki standardowej |

## Mapowanie pozycji

| Ścieżka ZUGFeRD CII                      | Pole DocBits   | Pole Infor BOD     | Typ    | Opis                   |
| ---------------------------------------- | -------------- | ------------------ | ------ | ---------------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | Numer pozycji          |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | Opis pozycji           |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | Ilość zafakturowana    |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | Cena jednostkowa netto |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | Wartość pozycji        |
