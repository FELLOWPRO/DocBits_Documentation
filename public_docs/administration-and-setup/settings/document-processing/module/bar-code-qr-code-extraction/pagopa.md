# PagoPA

## Przegląd

**PagoPA** to standard płatniczego kodu QR włoskiej administracji publicznej. Każda faktura wystawiona przez organ PA we Włoszech (gminy, uniwersytety, ochrona zdrowia, organy podatkowe) zawiera kod QR PagoPA. DocBits dekoduje payload i zwraca cztery wymagane pola płatności w odpowiedzi API dokumentu.

### Przegląd funkcji

Payloady PagoPA są zwarte i ściśle strukturalne: dokładnie **pięć pól oddzielonych pionową kreską** w jednej linii. Kwoty są kodowane w **centach** (liczba całkowita) i automatycznie konwertowane przez ekstraktor na dziesiętne euro. Wiodące zera w `codice_avviso` (18-cyfrowe powiadomienie płatności) są zachowywane — nie wolno go nigdy interpretować jako liczby całkowitej, ponieważ jest to identyfikator o stałej szerokości.

#### Kluczowe korzyści

* **Obowiązkowe pokrycie** dla faktur PA we Włoszech: `codice_avviso` i kod fiskalny wierzyciela wyodrębniane do nazwanych pól.
* **Bezpieczna obsługa numeryczna**: 18-cyfrowy `codice_avviso` zachowuje wiodące zera; kwota w centach jest również udostępniana jako float euro.

***

### Wykrywanie

- Magiczny prefiks: `PAGOPA|002|`
- Dokładnie **5 pól oddzielonych pionową kreską** po prefiksie: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Tylko EUR** — żadna inna waluta nie jest zgodna ze specyfikacją

### Wyodrębnione pola

Wszystkie pola używają prefiksu `pagopa_`:

| Pole | Opis |
|------|------|
| `pagopa_codice_avviso` | 18-cyfrowe powiadomienie płatności — wiodące zera zachowane (string) |
| `pagopa_fiscal_code_creditor` | 11-cyfrowy kod fiskalny wierzyciela (string) |
| `pagopa_amount_cents` | Kwota w centach (liczba całkowita) |
| `pagopa_amount` | Kwota w euro (dziesiętna, pochodna od `pagopa_amount_cents`) |
| `pagopa_auth` | Opcjonalny wskaźnik auth/wersji z payloadu |

### Przykładowa odpowiedź API

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Jak włączyć funkcję

Parsowanie PagoPA jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
