# GiroCode (EPC069-12)

## Panoramica

Il **GiroCode** è il QR code di pagamento SEPA definito dall'European Payments Council nella specifica **EPC069-12**. È lo standard de facto sulle fatture di banche tedesche e austriache (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) e viene emesso anche nei Paesi Bassi, Belgio e Finlandia. DocBits decodifica entrambe le revisioni (**v001** e **v002**) e restituisce il payload SEPA completo nella risposta API del documento.

### Panoramica della funzione

Un GiroCode contiene tutto il necessario per avviare un bonifico SEPA: BIC e IBAN del beneficiario, nome del beneficiario, importo, causale e una referenza strutturata o un testo libero di causale. DocBits normalizza il payload in modo che **gli importi con `.` o `,` come separatore decimale** — una deviazione frequente dai generatori tedeschi rispetto alla specifica — siano accettati senza errori.

#### Vantaggi principali

* **Ampia copertura DE / AT**: tutte le grandi banche retail stampano GiroCode sulle fatture.
* **Entrambe le revisioni supportate**: v001 (BIC obbligatorio) e v002 (BIC opzionale nell'EEA).
* **Tollerante al separatore decimale**: accetta indistintamente `227.01` e `227,01`.

***

### Rilevazione

- Prefisso magico: `BCD\n001` (v001) o `BCD\n002` (v002)
- Payload strutturato per righe secondo la specifica EPC069-12
- **v002** rende opzionale il BIC se l'IBAN appartiene all'Area unica dei pagamenti in euro

### Campi estratti

Tutti i campi utilizzano il prefisso `girocode_`:

| Campo | Descrizione |
|-------|-------------|
| `girocode_bic` | BIC del beneficiario (obbligatorio in v001, opzionale in v002 nell'EEA) |
| `girocode_creditor_name` | Nome del beneficiario |
| `girocode_iban` | IBAN del beneficiario |
| `girocode_amount` | Importo (decimale) — `.` e `,` accettati |
| `girocode_currency` | Valuta (solitamente `EUR`) |
| `girocode_purpose` | Codice di causale SEPA |
| `girocode_structured_reference` | Riferimento strutturato del creditore (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Causale libera |
| `girocode_version` | `001` o `002` |

### Esempio di risposta API

Esempio reale (fattura Dr. Meindl u. Partner):

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

### Come abilitare la funzione

Il parsing GiroCode è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
