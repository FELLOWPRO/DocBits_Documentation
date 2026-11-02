# Mapowanie ZUGFeRD 2.3

## Przegląd

ZUGFeRD 2.3 to najnowsza główna wersja, uwzględniająca ulepszenia zapewniające lepszą interoperacyjność i zgodność z nowoczesnymi wymaganiami e-fakturowania.

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

### Informacje o płatności

| Ścieżka ZUGFeRD CII                                | Pole DocBits     | Pole Infor BOD | Typ    | Opis          |
| -------------------------------------------------- | ---------------- | -------------- | ------ | ------------- |
| `PayeePartyCreditorFinancialAccount/IBANID`        | `IBAN_EXTRACTED` | `PayeeIBAN`    | STRING | IBAN          |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC`            | `PayeeBIC`     | STRING | Kod BIC/SWIFT |

### Podział podatków (klasyfikowany według poziomów)

Bloki `ApplicableTradeTax` są rozdzielane na trzy poziomy oparte na stawce (nie według indeksów pozycyjnych): pola stawki standardowej (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) obejmują stawkę ≥ 19; pola stawki obniżonej (`*_2`) obejmują 0 < stawka < 19; pola stawki zerowej (`*_3`) obejmują stawkę = 0. Pełną listę pól znajdziesz w [Podział podatków ZUGFeRD](./#podzial-podatkow-klasyfikowany-wedlug-poziomow).

## Mapowanie pozycji

| Ścieżka ZUGFeRD CII                      | Pole DocBits   | Pole Infor BOD     | Typ    | Opis                   |
| ---------------------------------------- | -------------- | ------------------ | ------ | ---------------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | Numer pozycji          |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | Opis pozycji           |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | Ilość zafakturowana    |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | Cena jednostkowa netto |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | Wartość pozycji        |
