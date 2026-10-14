# Szwajcarski QR Bill

## Przegląd

**Szwajcarski QR Bill** to krajowy standard pokwitowań płatności, który od 30 czerwca 2020 zastąpił pomarańczowe i czerwone szwajcarskie druki wpłat. Każda krajowa szwajcarska faktura — od dostawców mediów, ubezpieczycieli po partnerów biznesowych — zawiera dziś kod Swiss QR Bill. DocBits dekoduje te kody automatycznie i udostępnia każde pole płatności w odpowiedzi API.

### Przegląd funkcji

Szwajcarskie QR Billy są zgodne ze standardem płatności **ISO 20022** i są wydawane w dwóch wersjach: **v1.0** (wczesne wdrożenie) i **v2.0** (aktualna). Ekstraktor DocBits obsługuje obie. Rozpoznane payloady są dekodowane do pełnego zestawu pól — wierzyciel, dłużnik, IBAN / QR-IBAN, kwota, waluta, typ referencji (QRR, SCOR lub NON), wiadomości strukturalne i swobodne oraz alternatywne schematy płatności.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Kluczowe korzyści

* **Zero ręcznego wprowadzania** dla szwajcarskich faktur: IBAN, kwota, referencja i wierzyciel trafiają bezpośrednio do dokumentu.
* **Obsługa obu wersji**: v1.0 i v2.0 są wykrywane automatycznie.
* **Zachowane typy referencji**: QRR, SCOR i NON pozostają dokładnie takie, jak wydrukowane, co utrzymuje poprawność uzgadniania downstream.

***

### Wykrywanie

- Magiczny prefiks: `SPC\n0100` (v1.0) lub `SPC\n0200` (v2.0)
- Zgodny z ISO 20022
- Parser udostępnia również `alt-schemes` (alternatywne procedury płatności), jeśli są obecne

### Wyodrębnione pola

Wszystkie pola używają prefiksu `swissqr_`:

| Pole | Opis |
|------|------|
| `swissqr_account` | IBAN lub QR-IBAN wierzyciela |
| `swissqr_creditor_name` | Nazwa wierzyciela |
| `swissqr_creditor_street` | Ulica / linia adresowa wierzyciela |
| `swissqr_creditor_city` | Miasto wierzyciela |
| `swissqr_creditor_postal_code` | Kod pocztowy wierzyciela |
| `swissqr_creditor_country` | Kraj wierzyciela (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Nazwa dłużnika (jeśli wydrukowana) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Adres dłużnika |
| `swissqr_amount` | Kwota (dziesiętna) |
| `swissqr_currency` | Waluta (ISO 4217) — zazwyczaj `CHF` lub `EUR` |
| `swissqr_reference` | Referencja strukturalna (QRR lub SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` lub `NON` |
| `swissqr_unstructured_message` | Swobodny tekst tytułu |
| `swissqr_bill_information` | Strukturalne informacje rozliczeniowe (S1 / Swico) |
| `swissqr_alt_schemes` | Alternatywne procedury (jeśli obecne) |

### Przykładowa odpowiedź API

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Jak włączyć funkcję

Parsowanie szwajcarskiego QR Bill jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
