# SPAYD / Short Payment Descriptor (Czeski)

## Przegląd

**SPAYD** (Short Payment Descriptor), znany również jako **SPD**, to standardowy kod QR płatności zdefiniowany przez Czeskie Stowarzyszenie Banków. Drukowany jest na praktycznie każdej czeskiej fakturze biznesowej i używany częściowo również na Słowacji. DocBits dekoduje payloady SPAYD i zwraca pełną instrukcję płatności — włączając czeskie specyficzne symbole (variable, specific, constant) — w odpowiedzi API dokumentu.

### Przegląd funkcji

Payload SPAYD to lista par klucz:wartość oddzielonych gwiazdkami. Wartości są kodowane procentowo, więc imiona odbiorców i wiadomości w UTF-8 są zachowywane. DocBits obsługuje popularny wariant `ACC` (IBAN plus opcjonalny BIC, oddzielone `+`), `ALT-ACC` (alternatywne IBAN-y oddzielone przecinkami) i zachowuje nieznane klucze specyficzne dla dostawcy w dedykowanym polu (`spayd_raw_pairs`), dzięki czemu konsumenci downstream nigdy nie tracą danych.

#### Kluczowe korzyści

* **Pełne pokrycie czeskich płatności**: IBAN/BIC oraz symbole VS/SS/KS są wyodrębniane do nazwanych pól.
* **Unicode-safe**: kodowane procentowo imiona odbiorców i wiadomości UTF-8 przechodzą bez szkody.
* **Forward-compatible**: nieznane klucze są zachowywane w `spayd_raw_pairs`.

***

### Wykrywanie

- Magiczny prefiks: `SPD*1.0*`
- Payload to lista par `KEY:value` oddzielonych `*`, np. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Wartości są **kodowane procentowo** (RFC 3986)
- `ACC` może zawierać `IBAN+BIC` (oddzielone `+`); `ALT-ACC` zawiera alternatywne IBAN-y oddzielone przecinkami

### Wyodrębnione pola

Wszystkie pola używają prefiksu `spayd_`:

| Pole | Opis |
|------|------|
| `spayd_iban` | Główny IBAN (z `ACC`) |
| `spayd_bic` | BIC (z `ACC`, jeśli obecny) |
| `spayd_alt_ibans` | Lista alternatywnych IBAN-ów (z `ALT-ACC`) |
| `spayd_amount` | Kwota (dziesiętna, z `AM`) |
| `spayd_currency` | Waluta (z `CC`, zazwyczaj `CZK`) |
| `spayd_variable_symbol` | Symbol zmienny (`VS`) — numer faktury/referencji |
| `spayd_specific_symbol` | Symbol specyficzny (`SS`) |
| `spayd_constant_symbol` | Symbol stały (`KS`) |
| `spayd_recipient_name` | Nazwa odbiorcy (z `RN`) |
| `spayd_due_date` | Termin płatności (z `DT`, `YYYYMMDD`) |
| `spayd_message` | Swobodna wiadomość (z `MSG`) |
| `spayd_raw_pairs` | Nieznane lub specyficzne dla dostawcy pary `KEY:value`, zachowane dosłownie |

### Przykładowa odpowiedź API

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### Jak włączyć funkcję

Parsowanie SPAYD jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
