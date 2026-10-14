# Mapowanie pól ZUGFeRD + Swiss QR Code

## Przegląd

Podczas przetwarzania faktur PDF zawierających zarówno dane ZUGFeRD XML, jak i Swiss QR Code, DocBits wyodrębnia dane z obu źródeł i inteligentnie je łączy.

## Jak to działa

1.  **Ekstrakcja ZUGFeRD XML** - DocBits najpierw wyodrębnia pola z osadzonego ZUGFeRD XML
2.  **Wykrywanie Swiss QR Code** - Usługa barcode wykrywa i parsuje kody Swiss QR
3.  **Inteligentne Scalanie (Smart Merge)** - Puste pola są wypełniane danymi ze Swiss QR (pola z wartościami są zachowywane)
4.  **Ścieżka audytu (Audit Trail)** - Pełne dane kodu QR są przechowywane w `qr_code_data` w celu weryfikacji

## Tabela Mapowania Pól

### Mapowanie Swiss QR Code → DocBits

| Pole Swiss QR | Pole DocBits | Opis |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN wierzyciela (np. CH9300762011...) |
| Amount | `total_amount` | Kwota płatności (np. 1234.56) |
| Currency | `currency` | Kod waluty (CHF lub EUR) |
| Reference | `payment_reference` / `esr_reference` | Referencja QR lub numer ESR |
| Creditor.Name | `supplier_name` | Nazwa firmy dostawcy |
| Creditor.AddressLine1 | `supplier_address` | Adres (ulica) |
| Creditor.PostalCode | `supplier_plz` | Kod pocztowy |
| Creditor.City | `supplier_city` | Miasto |
| Creditor.Country | `supplier_country` | Kod kraju (CH) |
| Debtor.Name | `company_name` | Nazwa firmy odbiorcy |
| Debtor.AddressLine1 | `company_street` | Adres odbiorcy |
| Debtor.PostalCode | `company_plz` | Kod pocztowy odbiorcy |
| Debtor.City | `company_city` | Miasto odbiorcy |

## Przykład: Przetwarzanie Przykładowej Faktury

### Dokument Wejściowy

*   **PDF**: Faktura z osadzonym ZUGFeRD 1.0 XML + kodem kreskowym Swiss QR Code

### Dane Wyodrębnione ze Swiss QR Code

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Wyniki Ekstrakcji Pól

| Pole | Wartość | Źródło | Metoda |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Metody Ekstrakcji

| Kod Metody | Opis |
| :--- | :--- |
| **ED** | Dokument Elektroniczny (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Ekstrakcja kodu kreskowego Swiss QR Code |
| **OCR** | Optyczne Rozpoznawanie Znaków |
| **ML** | Ekstrakcja Machine Learning |

## Priorytet Scalania (Merge)

1.  **ZUGFeRD XML** ma najwyższy priorytet (dane strukturalne, wiarygodne)
2.  **Swiss QR Code** wypełnia puste pola (gwarantowana dokładność danych płatniczych)
3.  **OCR/ML** używane dla pól niewystępujących w źródłach elektronicznych

## Obsługiwane Wersje Swiss QR Code

*   Format Swiss QR Bill (ISO 20022)
*   Format QR-IBAN (zaczyna się od 30, 31)
*   Standardowy format IBAN
*   Z/bez referencji strukturalnej (QRR, SCOR)

## Wymagania Wersji

Ta funkcja wymaga **api w wersji 10.95.6** oraz **barcode w wersji 1.0.5** lub nowszej.

### Wersje Składników (Środowisko Dev)

| Składnik | Wersja | Opis |
| :--- | :--- | :--- |
| `api` | 10.95.6 | Główne API z obsługą ekstrakcji ZUGFeRD 1.0 |
| `barcode` | 1.0.5 | Wykrywanie i parsowanie Swiss QR Code |
| `Auth` | 1.48.8 | Usługa uwierzytelniania |

