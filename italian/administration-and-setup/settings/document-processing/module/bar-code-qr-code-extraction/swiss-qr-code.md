# Swiss QR Bill

## Panoramica

La **Swiss QR Bill** è lo standard nazionale di bollettino di pagamento che dal 30 giugno 2020 ha sostituito i tradizionali bollettini arancioni e rossi svizzeri. Ogni fattura nazionale svizzera — da fornitori di utenze, assicurazioni o partner commerciali — riporta oggi un codice Swiss QR Bill. DocBits decodifica questi codici automaticamente e rende disponibile ogni campo di pagamento tramite la risposta API.

### Panoramica della funzione

Le Swiss QR Bill seguono lo standard di pagamento **ISO 20022** e vengono emesse in due versioni: **v1.0** (primo rollout) e **v2.0** (attuale). L'estrattore DocBits supporta entrambe. I payload riconosciuti vengono decodificati in un insieme completo di campi — creditore, debitore, IBAN / QR-IBAN, importo, valuta, tipo di riferimento (QRR, SCOR o NON), messaggi strutturati e liberi, e schemi di pagamento alternativi.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Vantaggi principali

* **Nessun inserimento manuale** per le fatture svizzere: IBAN, importo, riferimento e creditore fluiscono direttamente nel documento.
* **Entrambe le versioni coperte**: v1.0 e v2.0 vengono rilevate automaticamente.
* **Tipi di riferimento preservati**: QRR, SCOR e NON vengono mantenuti esattamente come stampati, mantenendo funzionante la riconciliazione a valle.

***

### Rilevazione

- Prefisso magico: `SPC\n0100` (v1.0) o `SPC\n0200` (v2.0)
- Conforme a ISO 20022
- Il parser espone inoltre `alt-schemes` (procedure di pagamento alternative) se presenti

### Campi estratti

Tutti i campi utilizzano il prefisso `swissqr_`:

| Campo | Descrizione |
|-------|-------------|
| `swissqr_account` | IBAN o QR-IBAN del creditore |
| `swissqr_creditor_name` | Nome del creditore |
| `swissqr_creditor_street` | Via / riga di indirizzo del creditore |
| `swissqr_creditor_city` | Città del creditore |
| `swissqr_creditor_postal_code` | CAP del creditore |
| `swissqr_creditor_country` | Paese del creditore (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Nome del debitore (se stampato) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Indirizzo del debitore |
| `swissqr_amount` | Importo (decimale) |
| `swissqr_currency` | Valuta (ISO 4217) — tipicamente `CHF` o `EUR` |
| `swissqr_reference` | Riferimento strutturato (QRR o SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` o `NON` |
| `swissqr_unstructured_message` | Testo libero di causale |
| `swissqr_bill_information` | Informazioni di fatturazione strutturate (S1 / Swico) |
| `swissqr_alt_schemes` | Procedure alternative (se presenti) |

### Esempio di risposta API

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

### Come abilitare la funzione

Il parsing Swiss QR Bill è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
