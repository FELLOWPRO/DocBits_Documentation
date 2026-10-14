# PagoPA

## Panoramica

**PagoPA** è lo standard QR code di pagamento della Pubblica Amministrazione italiana. Ogni fattura emessa da un ente della PA italiana (comuni, università, sanità, autorità fiscali) riporta un codice QR PagoPA. DocBits decodifica il payload e restituisce i quattro campi di pagamento obbligatori nella risposta API del documento.

### Panoramica della funzione

I payload PagoPA sono compatti e rigidamente strutturati: esattamente **cinque campi separati da pipe** su un'unica riga. Gli importi sono codificati in **centesimi** (intero) e vengono automaticamente convertiti in euro decimali dall'estrattore. Gli zeri iniziali del `codice_avviso` (avviso di pagamento a 18 cifre) sono preservati — non deve mai essere interpretato come intero, poiché è un identificativo a larghezza fissa.

#### Vantaggi principali

* **Copertura obbligatoria** per le fatture della PA italiana: `codice_avviso` e codice fiscale del creditore vengono estratti in campi dedicati.
* **Gestione numerica sicura**: il `codice_avviso` a 18 cifre conserva gli zeri iniziali; l'importo in centesimi è esposto anche come euro decimale.

***

### Rilevazione

- Prefisso magico: `PAGOPA|002|`
- Esattamente **5 campi separati da pipe** dopo il prefisso: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Solo EUR** — nessun'altra valuta è valida secondo la specifica

### Campi estratti

Tutti i campi utilizzano il prefisso `pagopa_`:

| Campo | Descrizione |
|-------|-------------|
| `pagopa_codice_avviso` | Avviso di pagamento a 18 cifre — zeri iniziali preservati (stringa) |
| `pagopa_fiscal_code_creditor` | Codice fiscale del creditore a 11 cifre (stringa) |
| `pagopa_amount_cents` | Importo in centesimi (intero) |
| `pagopa_amount` | Importo in euro (decimale, derivato da `pagopa_amount_cents`) |
| `pagopa_auth` | Indicatore auth/versione opzionale dal payload |

### Esempio di risposta API

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Come abilitare la funzione

Il parsing PagoPA è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
