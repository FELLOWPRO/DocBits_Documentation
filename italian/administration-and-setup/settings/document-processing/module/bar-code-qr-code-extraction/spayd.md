# SPAYD / Short Payment Descriptor (Ceco)

## Panoramica

**SPAYD** (Short Payment Descriptor), noto anche come **SPD**, è il QR code di pagamento standard definito dall'Associazione Bancaria Ceca. Viene stampato su praticamente ogni fattura aziendale ceca ed è utilizzato parzialmente anche in Slovacchia. DocBits decodifica i payload SPAYD e restituisce l'istruzione di pagamento completa — inclusi i simboli specifici cechi (variable, specific, constant) — nella risposta API del documento.

### Panoramica della funzione

Un payload SPAYD è una lista di coppie chiave:valore separate da asterischi. I valori sono percent-encoded, quindi i nomi di destinatari e messaggi in UTF-8 vengono preservati. DocBits supporta la variante comune `ACC` (IBAN più BIC opzionale, separati da `+`), `ALT-ACC` (IBAN alternativi, separati da virgole) e preserva tutte le chiavi specifiche di fornitori sconosciuti in un campo dedicato (`spayd_raw_pairs`), in modo che i consumatori a valle non perdano dati.

#### Vantaggi principali

* **Copertura completa dei pagamenti cechi**: IBAN/BIC e i simboli VS/SS/KS vengono estratti in campi dedicati.
* **Sicuro in Unicode**: nomi di destinatari e messaggi UTF-8 percent-encoded viaggiano integri.
* **Compatibile in avanti**: le chiavi sconosciute sono preservate in `spayd_raw_pairs`.

***

### Rilevazione

- Prefisso magico: `SPD*1.0*`
- Il payload è una lista separata da `*` di coppie `KEY:value`, p. es. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- I valori sono **percent-encoded** (RFC 3986)
- `ACC` può contenere `IBAN+BIC` (separati da `+`); `ALT-ACC` contiene IBAN alternativi separati da virgole

### Campi estratti

Tutti i campi utilizzano il prefisso `spayd_`:

| Campo | Descrizione |
|-------|-------------|
| `spayd_iban` | IBAN principale (da `ACC`) |
| `spayd_bic` | BIC (da `ACC`, se presente) |
| `spayd_alt_ibans` | Lista degli IBAN alternativi (da `ALT-ACC`) |
| `spayd_amount` | Importo (decimale, da `AM`) |
| `spayd_currency` | Valuta (da `CC`, solitamente `CZK`) |
| `spayd_variable_symbol` | Simbolo variabile (`VS`) — numero fattura/riferimento |
| `spayd_specific_symbol` | Simbolo specifico (`SS`) |
| `spayd_constant_symbol` | Simbolo costante (`KS`) |
| `spayd_recipient_name` | Nome del destinatario (da `RN`) |
| `spayd_due_date` | Data di scadenza (da `DT`, `YYYYMMDD`) |
| `spayd_message` | Messaggio libero (da `MSG`) |
| `spayd_raw_pairs` | Coppie `KEY:value` sconosciute o specifiche di fornitori, conservate inalterate |

### Esempio di risposta API

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

### Come abilitare la funzione

Il parsing SPAYD è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
