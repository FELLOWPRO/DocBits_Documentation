# GiroCode (EPC069-12)

## Przegląd

**GiroCode** to kod QR płatności SEPA zdefiniowany przez European Payments Council w specyfikacji **EPC069-12**. Jest de facto standardem na fakturach niemieckich i austriackich banków (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria), a także wydawany w Holandii, Belgii i Finlandii. DocBits dekoduje obie rewizje (**v001** i **v002**) i zwraca pełny payload płatności SEPA w odpowiedzi API dokumentu.

### Przegląd funkcji

GiroCode zawiera wszystko, co potrzebne do zainicjowania przelewu SEPA: BIC i IBAN beneficjenta, nazwa beneficjenta, kwota, cel oraz albo strukturalna referencja wierzyciela, albo swobodny tytuł przelewu. DocBits normalizuje payload tak, aby **kwoty z `.` lub `,` jako separatorem dziesiętnym** — częste odstępstwo niemieckich generatorów od specyfikacji — były akceptowane bez błędu.

#### Kluczowe korzyści

* **Szerokie pokrycie DE / AT**: wszystkie duże banki detaliczne drukują GiroCode na fakturach dla klientów.
* **Obie rewizje obsługiwane**: v001 (BIC obowiązkowy) i v002 (BIC opcjonalny w EOG).
* **Tolerancja separatora dziesiętnego**: `227.01` i `227,01` akceptowane wymiennie.

***

### Wykrywanie

- Magiczny prefiks: `BCD\n001` (v001) lub `BCD\n002` (v002)
- Payload strukturalny liniowo zgodnie ze specyfikacją EPC069-12
- **v002** sprawia, że BIC jest opcjonalny, gdy IBAN znajduje się w Jednolitym Obszarze Płatności w Euro

### Wyodrębnione pola

Wszystkie pola używają prefiksu `girocode_`:

| Pole | Opis |
|------|------|
| `girocode_bic` | BIC beneficjenta (obowiązkowy w v001, opcjonalny w v002 dla EOG) |
| `girocode_creditor_name` | Nazwa beneficjenta |
| `girocode_iban` | IBAN beneficjenta |
| `girocode_amount` | Kwota (dziesiętna) — akceptowane `.` i `,` |
| `girocode_currency` | Waluta (zazwyczaj `EUR`) |
| `girocode_purpose` | Kod celu SEPA |
| `girocode_structured_reference` | Strukturalna referencja wierzyciela (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Swobodny tytuł przelewu |
| `girocode_version` | `001` lub `002` |

### Przykładowa odpowiedź API

Realny przykład (faktura Dr. Meindl u. Partner):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Jak włączyć funkcję

Parsowanie GiroCode jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
