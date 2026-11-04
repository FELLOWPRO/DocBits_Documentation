# ZATCA Fatoora (Arabia Saudyjska)

## Przegląd

**ZATCA Fatoora** to kod QR e-fakturowania wymagany przez Urząd Zakatu, Podatków i Ceł Arabii Saudyjskiej. Od **grudnia 2021 (Faza 1)** każda faktura B2C wystawiana w Królestwie musi zawierać QR Fatoora z pięcioma podstawowymi polami faktury, a od **stycznia 2023 (Faza 2)** QR zawiera dodatkowo kopertę podpisu kryptograficznego. DocBits dekoduje obie fazy i zwraca każde pole płatności z Fazy 1 jako nazwaną właściwość w odpowiedzi API dokumentu.

### Przegląd funkcji

ZATCA Fatoora używa formatu **binarnego TLV** (1 bajt ID tagu, 1 bajt długości, wartość) opakowanego w **Base64**. Cały tekst jest w UTF-8, więc arabskie nazwy sprzedawców dekodują się poprawnie. Ekstraktor udostępnia tagi 1–5 z Fazy 1 jako pola strukturalne, a — gdy są obecne — tagi 6–9 z Fazy 2 jako ciągi Base64 dla narzędzi compliance downstream. **Weryfikacja podpisu/skrótu jest celowo poza zakresem**; należy do dedykowanych stosów compliance e-fakturowania.

#### Kluczowe korzyści

* **Obowiązkowe pokrycie compliance**: każda saudyjska faktura B2C jest parsowana.
* **Wsparcie arabskiego**: nazwy sprzedawców UTF-8 przechodzą bez re-kodowania.
* **Faza 1 i Faza 2**: obie fazy wykrywane; faza udostępniana w wyjściu.
* **Koperta Fazy 2 zachowana**: hash, podpis, klucz publiczny i podpis certyfikatu zachowane jako ciągi Base64 dla narzędzi compliance.

***

### Wykrywanie

- Binarny TLV opakowany w Base64 (tagi 1–9, 1 bajt ID tagu + 1 bajt długości + wartość)
- Wykrywanie fazy: `zatca_phase = 1`, gdy obecne są tylko tagi 1–5; `zatca_phase = 2`, gdy obecne są również tagi 6–9

### Układ tagów TLV

| Tag | Faza | Zawartość |
|-----|------|-----------|
| 1 | 1 | Nazwa sprzedawcy (UTF-8, obsługuje arabski) |
| 2 | 1 | Numer rejestracji VAT |
| 3 | 1 | Znacznik czasu faktury (ISO 8601) |
| 4 | 1 | Suma faktury |
| 5 | 1 | Suma VAT |
| 6 | 2 | Hash faktury XML (Base64) |
| 7 | 2 | Podpis cyfrowy (Base64) |
| 8 | 2 | Klucz publiczny (Base64) |
| 9 | 2 | Podpis certyfikatu (Base64) |

### Wyodrębnione pola

Wszystkie pola używają prefiksu `zatca_`:

| Pole | Opis |
|------|------|
| `zatca_seller_name` | Nazwa sprzedawcy (UTF-8) |
| `zatca_vat_number` | Numer rejestracji VAT |
| `zatca_invoice_timestamp` | Data/czas faktury |
| `zatca_invoice_total` | Suma faktury (dziesiętna) |
| `zatca_vat_total` | Suma VAT (dziesiętna) |
| `zatca_phase` | `1` (Faza 1) lub `2` (Faza 2) |
| `zatca_invoice_hash` | Hash faktury XML — tylko Faza 2, Base64 |
| `zatca_signature` | Podpis cyfrowy — tylko Faza 2, Base64 |
| `zatca_public_key` | Klucz publiczny — tylko Faza 2, Base64 |
| `zatca_certificate_signature` | Podpis certyfikatu — tylko Faza 2, Base64 |

{% hint style="info" %}
**Poza zakresem**: DocBits nie weryfikuje podpisu kryptograficznego, hasha ani łańcucha certyfikatów. Ta weryfikacja to osobna kwestia compliance i powinna być obsługiwana przez certyfikowany przez ZATCA stos e-fakturowania.
{% endhint %}

### Przykładowa odpowiedź API (Faza 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Jak włączyć funkcję

Parsowanie ZATCA Fatoora jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
