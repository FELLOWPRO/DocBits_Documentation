# ZATCA Fatoora (Arabia Saudita)

## Panoramica

**ZATCA Fatoora** è il QR code di fatturazione elettronica imposto dall'Autorità Zakat, Fiscale e Doganale dell'Arabia Saudita. Da **dicembre 2021 (Fase 1)** ogni fattura B2C emessa nel Regno deve riportare un QR Fatoora con i cinque campi principali della fattura; da **gennaio 2023 (Fase 2)** il QR contiene inoltre un involucro di firma crittografica. DocBits decodifica entrambe le fasi e restituisce ogni campo di pagamento della Fase 1 come proprietà dedicata nella risposta API del documento.

### Panoramica della funzione

ZATCA Fatoora utilizza un formato **TLV binario** (1 byte per l'ID tag, 1 byte per la lunghezza, valore) racchiuso in **Base64**. Tutto il testo è UTF-8, quindi i nomi di venditori in arabo vengono decodificati correttamente. L'estrattore espone i tag 1–5 della Fase 1 come campi strutturati e — quando presenti — i tag 6–9 della Fase 2 come stringhe Base64 per strumenti di compliance a valle. **La verifica di firma e hash è deliberatamente fuori dall'ambito**; spetta agli stack dedicati di compliance di fatturazione elettronica.

#### Vantaggi principali

* **Copertura obbligatoria di compliance**: ogni fattura B2C saudita viene analizzata.
* **Supporto arabo**: i nomi di venditori UTF-8 viaggiano senza re-encoding.
* **Fase 1 e Fase 2**: entrambe le fasi vengono rilevate; la fase è esposta nell'output.
* **Involucro Fase 2 preservato**: hash, firma, chiave pubblica e firma del certificato sono mantenuti come stringhe Base64 per gli strumenti di compliance.

***

### Rilevazione

- TLV binario racchiuso in Base64 (tag 1–9, 1 byte di ID tag + 1 byte di lunghezza + valore)
- Rilevazione fase: `zatca_phase = 1` quando sono presenti solo i tag 1–5; `zatca_phase = 2` quando sono presenti anche i tag 6–9

### Schema dei tag TLV

| Tag | Fase | Contenuto |
|-----|------|-----------|
| 1 | 1 | Nome del venditore (UTF-8, supporta arabo) |
| 2 | 1 | Numero di registrazione IVA |
| 3 | 1 | Timestamp della fattura (ISO 8601) |
| 4 | 1 | Totale fattura |
| 5 | 1 | Totale IVA |
| 6 | 2 | Hash della fattura XML (Base64) |
| 7 | 2 | Firma digitale (Base64) |
| 8 | 2 | Chiave pubblica (Base64) |
| 9 | 2 | Firma del certificato (Base64) |

### Campi estratti

Tutti i campi utilizzano il prefisso `zatca_`:

| Campo | Descrizione |
|-------|-------------|
| `zatca_seller_name` | Nome del venditore (UTF-8) |
| `zatca_vat_number` | Numero di registrazione IVA |
| `zatca_invoice_timestamp` | Data/ora della fattura |
| `zatca_invoice_total` | Totale fattura (decimale) |
| `zatca_vat_total` | Totale IVA (decimale) |
| `zatca_phase` | `1` (Fase 1) o `2` (Fase 2) |
| `zatca_invoice_hash` | Hash della fattura XML — solo Fase 2, Base64 |
| `zatca_signature` | Firma digitale — solo Fase 2, Base64 |
| `zatca_public_key` | Chiave pubblica — solo Fase 2, Base64 |
| `zatca_certificate_signature` | Firma del certificato — solo Fase 2, Base64 |

{% hint style="info" %}
**Fuori dall'ambito**: DocBits non verifica né la firma crittografica, né l'hash, né la catena di certificati. Questa verifica è una responsabilità di compliance dedicata e deve essere gestita da uno stack di fatturazione elettronica certificato ZATCA.
{% endhint %}

### Esempio di risposta API (Fase 1)

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

### Come abilitare la funzione

Il parsing ZATCA Fatoora è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
