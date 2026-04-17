---
description: Supporto per i documenti elettronici CHINA FAPIAO in DocBits
---

# 🇨🇳 CHINA FAPIAO

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Cina |
| **Tipi di documento** | Fattura IVA generale, Fattura IVA speciale, E-Fapiao |
| **Formato** | XML |
| **Standard** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |
| **Namespace XML** | `urn:china:tax:fapiao:1.0` |

Fapiao (发票) è il sistema cinese di fatturazione fiscale elettronica regolato dalla State Taxation Administration (国家税务总局). Tutti i documenti Fapiao condividono il namespace XML `urn:china:tax:fapiao:1.0`. DocBits rileva automaticamente il tipo di Fapiao e instrada verso le regole di estrazione appropriate:

| Tipo di Fapiao | Codice | Descrizione |
|-----------|------|-------------|
| 普通发票 | General VAT Invoice | Fattura IVA generale (普通发票) |
| 专用发票 | Special VAT Invoice | Fattura IVA speciale (专用发票) — detraibile |

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="china-fapiao-preview.png" alt="Anteprima fattura China Fapiao in DocBits"><figcaption><p>Anteprima predefinita DocBits per una CHINA GENERAL VAT INVOICE (普通发票)</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `fapiao_number` | Numero di fattura (8 cifre) |
| `invoice_code` | `fapiao_code` | Codice fattura (10-12 cifre) |
| `invoice_date` | `issue_date` | Data di emissione ISO 8601 |
| `fapiao_type` | `fapiao_type` | Tipo: 普通发票 o 专用发票 |
| `check_code` | `check_code` | Codice di verifica (20 cifre) |
| `machine_code` | `machine_code` | Numero di macchina fiscale |
| `currency` | Fisso: `CNY` | Sempre yuan cinese |
| `total_amount` | `total_with_tax` | Importo totale IVA inclusa (价税合计) |
| `net_amount` | `total_amount` | Importo netto (金额) |
| `tax_amount` | `total_tax` | Importo IVA (税额) |
| `amount_in_words` | `amount_in_words` | Importo in caratteri cinesi (大写) |
| `supplier_name` | `seller/name` | Nome dell'azienda emittente (销售方) |
| `supplier_id` | `seller/taxpayer_id` | Codice fiscale dell'emittente (18 caratteri) |
| `supplier_address` | `seller/address` | Indirizzo dell'emittente |
| `supplier_telephone` | `seller/telephone` | Telefono dell'emittente |
| `supplier_bank_name` | `seller/bank_name` | Banca dell'emittente |
| `supplier_bank_account` | `seller/bank_account` | Conto bancario dell'emittente |
| `buyer_name` | `buyer/name` | Nome dell'azienda destinataria (购买方) |
| `buyer_id` | `buyer/taxpayer_id` | Codice fiscale del destinatario |
| `buyer_address` | `buyer/address` | Indirizzo del destinatario |
| `buyer_telephone` | `buyer/telephone` | Telefono del destinatario |
| `remarks` | `remarks` | Note (备注) |
| `issuer` | `issuer` | Emittente (开票人) |
| `tax_authority` | `tax_authority` | Autorità fiscale (税务机关) |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso della riga: `items/item`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `SEQ` | `seq` | Numero di riga |
| `ITEM_NAME` | `name` | Descrizione dell'articolo |
| `SPEC` | `spec` | Specificazione / modello |
| `UNIT` | `unit` | Unità di misura |
| `QUANTITY` | `quantity` | Quantità |
| `UNIT_PRICE` | `unit_price` | Prezzo unitario netto |
| `AMOUNT` | `amount` | Totale della riga netto |
| `TAX_RATE` | `tax_rate` | Aliquota IVA in % (13% o 9%) |
| `TAX_AMOUNT` | `tax_amount` | IVA per riga |

## Regole di classificazione

DocBits rileva i documenti China Fapiao confrontando il namespace XML e il tipo di Fapiao:

| Tipo di documento elettronico | Modello |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0" version="1.0">` |
| CHINA SPECIAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0"` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA FAPIAO | `<fapiao` (corrispondenza generica) |
| CHINA FAPIAO | `税务总局` (corrispondenza testo) |
| CHINA VAT INVOICE | `<VATInvoice` (formato legacy) |

La classificazione usa il principio **FIRST MATCH WINS** ordinato per lunghezza del modello (il più lungo prima). L'elemento radice è `<fapiao>` con il namespace `urn:china:tax:fapiao:1.0`.

## Vedi anche

- [Standard di e-fatturazione attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
