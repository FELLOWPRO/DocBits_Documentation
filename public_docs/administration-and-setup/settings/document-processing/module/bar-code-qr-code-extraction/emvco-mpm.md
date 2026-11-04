# EMVCo MPM (QR presentato dal commerciante)

## Panoramica

**EMVCo MPM** (Merchant-Presented Mode) è la specifica globale di QR code mantenuta da EMVCo — lo stesso organismo dietro gli standard delle carte con chip e dei pagamenti contactless. Un unico involucro TLV (Tag-Length-Value) è condiviso tra oltre una dozzina di sistemi nazionali di pagamenti istantanei, in modo che un singolo parser copra **Pix** (Brasile), **UPI** (India), **PayNow** (Singapore), **PromptPay** (Thailandia), **QRIS** (Indonesia), **QR Ph** (Filippine), **VietQR** (Vietnam), **FPS** (Hong Kong), **DuitNow** (Malesia), **NETS** (Singapore) e altri ancora.

### Panoramica della funzione

Ogni payload EMVCo MPM condivide lo stesso involucro: inizia con `000201` (Payload Format Indicator = 01) e termina con `6304<CRC>`, dove `<CRC>` è una checksum CRC16-CCITT-FALSE su 4 hex. All'interno, i tag 26–51 codificati in TLV trasportano template di **Merchant Account Info** identificati da un **sotto-tag GUI** — è così che DocBits rileva a quale schema nazionale appartiene il QR. Il CRC viene validato e il risultato esposto come booleano, affinché i commercianti possano rilevare QR manomessi.

#### Vantaggi principali

* **Un estrattore, molti schemi**: un unico parser TLV generico gestisce tutta la famiglia EMVCo MPM.
* **Schemi nazionali identificati**: l'output include uno schema denominato (p. es. `pix`, `upi`, `paynow`), così la logica a valle può ramificarsi in modo pulito.
* **Validità CRC esposta**: `emvmpm_crc16_valid` evidenzia QR manomessi o corrotti.
* **Normalizzazione valuta**: i codici numerici ISO 4217 vengono mappati automaticamente in alpha-3 (20+ valute; i codici non mappati passano inalterati).

***

### Rilevazione

- Forma magica: inizia con `000201` e termina con `6304<4-hex CRC16-CCITT-FALSE>`
- Un decoder TLV generico percorre ogni tag
- Gli schemi nazionali sono identificati tramite il **sotto-tag GUI** nei template Merchant Account Info (tag 26–51)

### Schemi nazionali riconosciuti

| Sotto-tag GUI | Schema | Paese |
|---------------|--------|-------|
| `br.gov.bcb.pix` | **Pix** | Brasile |
| `UPI` | **UPI** | India |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapore |
| `SG.COM.NETS` | **NETS** | Singapore |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonesia |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filippine |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Thailandia |
| `A000000727` | **VietQR** | Vietnam |

I valori GUI/AID non riconosciuti vengono comunque analizzati — l'estrattore ripiega sul set di campi generici EMVCo MPM.

### Campi estratti

Tutti i campi utilizzano il prefisso `emvmpm_`:

| Campo | Descrizione |
|-------|-------------|
| `emvmpm_scheme` | Schema nazionale rilevato (p. es. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) o `generic` |
| `emvmpm_merchant_name` | Nome del commerciante (tag 59) |
| `emvmpm_merchant_city` | Città del commerciante (tag 60) |
| `emvmpm_country_code` | Codice paese ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Importo della transazione (decimale, tag 54) |
| `emvmpm_currency` | Valuta alpha-3 (convertita dal codice numerico del tag 53) |
| `emvmpm_additional_data` | Oggetto annidato: numero fattura, etichetta di riferimento, etichetta del terminale, scopo della transazione (sotto-tag del tag 62) |
| `emvmpm_crc16_valid` | Booleano — `true` se la checksum CRC16 coincide |

### Esempio di risposta API (Pix)

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

### Come abilitare la funzione

Il parsing EMVCo MPM è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
