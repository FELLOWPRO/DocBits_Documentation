# EMVCo MPM (QR prezentowany przez sprzedawcę)

## Przegląd

**EMVCo MPM** (Merchant-Presented Mode) to globalna specyfikacja kodów QR utrzymywana przez EMVCo — tę samą organizację stojącą za standardami kart chipowych i płatności zbliżeniowych. Jeden opakowujący TLV (Tag-Length-Value) jest współdzielony przez ponad tuzin krajowych systemów płatności natychmiastowych, więc jeden parser obsługuje **Pix** (Brazylia), **UPI** (Indie), **PayNow** (Singapur), **PromptPay** (Tajlandia), **QRIS** (Indonezja), **QR Ph** (Filipiny), **VietQR** (Wietnam), **FPS** (Hongkong), **DuitNow** (Malezja), **NETS** (Singapur) i wiele innych.

### Przegląd funkcji

Każdy payload EMVCo MPM ma tę samą strukturę: zaczyna się od `000201` (Payload Format Indicator = 01) i kończy `6304<CRC>`, gdzie `<CRC>` to 4-znakowa szesnastkowa suma kontrolna CRC16-CCITT-FALSE. Wewnątrz tagi 26–51 zakodowane w TLV niosą szablony **Merchant Account Info** identyfikowane przez **pod-tag GUI** — to właśnie po tym tagu GUI DocBits wykrywa, do jakiego krajowego schematu należy QR. CRC jest walidowany, a wynik udostępniany jako wartość logiczna, dzięki czemu sprzedawcy mogą wykrywać zmanipulowane kody.

#### Kluczowe korzyści

* **Jeden ekstraktor, wiele schematów**: jeden ogólny parser TLV obsługuje całą rodzinę EMVCo MPM.
* **Zidentyfikowane schematy krajowe**: wyjście zawiera nazwany schemat (np. `pix`, `upi`, `paynow`), dzięki czemu logika downstream może czysto się rozgałęziać.
* **Wskazana ważność CRC**: `emvmpm_crc16_valid` ujawnia zmanipulowane lub uszkodzone kody QR.
* **Normalizacja waluty**: numeryczne kody ISO 4217 są automatycznie mapowane do alpha-3 (20+ walut; niemapowane kody numeryczne przechodzą bez zmian).

***

### Wykrywanie

- Magiczny kształt: zaczyna się od `000201` i kończy `6304<4-hex CRC16-CCITT-FALSE>`
- Ogólny dekoder TLV przechodzi przez każdy tag
- Schematy krajowe są identyfikowane przez **pod-tag GUI** w szablonach Merchant Account Info (tagi 26–51)

### Rozpoznane schematy krajowe

| Pod-tag GUI | Schemat | Kraj |
|-------------|---------|------|
| `br.gov.bcb.pix` | **Pix** | Brazylia |
| `UPI` | **UPI** | Indie |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapur |
| `SG.COM.NETS` | **NETS** | Singapur |
| `HK.COM.HKICL.FPS` | **FPS** | Hongkong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonezja |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filipiny |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Tajlandia |
| `A000000727` | **VietQR** | Wietnam |

Nierozpoznane wartości GUI/AID są nadal parsowane — ekstraktor wraca do ogólnego zestawu pól EMVCo MPM.

### Wyodrębnione pola

Wszystkie pola używają prefiksu `emvmpm_`:

| Pole | Opis |
|------|------|
| `emvmpm_scheme` | Wykryty schemat krajowy (np. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) lub `generic` |
| `emvmpm_merchant_name` | Nazwa sprzedawcy (tag 59) |
| `emvmpm_merchant_city` | Miasto sprzedawcy (tag 60) |
| `emvmpm_country_code` | Kod kraju ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Kwota transakcji (dziesiętna, tag 54) |
| `emvmpm_currency` | Waluta alpha-3 (przekonwertowana z numerycznego kodu tag 53) |
| `emvmpm_additional_data` | Zagnieżdżony obiekt: numer rachunku, etykieta referencji, etykieta terminalu, cel transakcji (pod-tagi tag 62) |
| `emvmpm_crc16_valid` | Boolean — `true`, jeśli suma kontrolna CRC16 się zgadza |

### Przykładowa odpowiedź API (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Jak włączyć funkcję

Parsowanie EMVCo MPM jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
