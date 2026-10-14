---
description: Supporto per i documenti elettronici China Fapiao (FAPIAO, E-FAPIAO, Fattura IVA generale, Fattura IVA speciale) in DocBits
---

# 🇨🇳 China Fapiao

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | China |
| **Tipi di documento** | General VAT Invoice (普通发票), Special VAT Invoice (专用发票), E-Fapiao |
| **Formato** | XML |
| **Standard** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |

Fapiao (发票) è lo standard di fattura fiscale cinese emesso sotto l'autorità della State Taxation Administration (STA / 国家税务总局). Tutti i documenti Fapiao condividono il namespace `urn:china:tax:fapiao:1.0`. DocBits rileva automaticamente il tipo di Fapiao tramite l'elemento `fapiao_type` e instrada verso le regole di estrazione appropriate:

| Valore fapiao_type | Tipo di documento |
|-------------------|--------------|
| 普通发票 | General VAT Invoice (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Special VAT Invoice (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supported |
| Estrazione campi | ✅ Supported |
| Trasformazione | ✅ Supported |

## Anteprima predefinita

<figure><img src="china-fapiao-preview.png" alt="Anteprima China Fapiao General VAT Invoice in DocBits"><figcaption><p>Anteprima predefinita DocBits per una China Fapiao General VAT Invoice (普通发票)</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Numero Fapiao — 8 cifre (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Data di emissione (ISO 8601) |
| `currency` | Fisso: `CNY` | Sempre yuan renminbi cinese |
| `total_amount` | `total/total_with_tax` | Importo totale IVA inclusa (价税合计) |
| `net_amount` | `total/total_amount` | Importo netto IVA esclusa (金额) |
| `tax_amount` | `total/total_tax` | Importo IVA totale (税额) |
| `supplier_name` | `seller/name` | Nome dell'azienda venditrice (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | Codice fiscale del venditore — 18 caratteri (纳税人识别号) |
| `supplier_address` | `seller/address` | Indirizzo del venditore |
| `supplier_country` | Fisso: `CN` | Sempre Cina |
| `iban` | `seller/bank_account` | Numero di conto bancario del venditore |
| `buyer_name` | `buyer/name` | Nome dell'azienda acquirente (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | Codice fiscale dell'acquirente (纳税人识别号) |
| `buyer_address` | `buyer/address` | Indirizzo dell'acquirente |
| `buyer_country` | Fisso: `CN` | Sempre Cina |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso della riga: `items/item`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `seq` | Numero di sequenza della riga |
| `DESCRIPTION` | `name` + `spec` | Descrizione e specifica dell'articolo (concatenate) |
| `QUANTITY` | `quantity` | Quantità |
| `UNIT` | `unit` | Unità di misura (es. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Prezzo unitario IVA esclusa |
| `VAT_RATE` | `tax_rate` | Aliquota IVA in % (tipicamente 6%, 9% o 13%) |
| `VAT` | `tax_amount` | Importo IVA per riga |
| `NET_AMOUNT` | `amount` | Totale della riga IVA esclusa |

## Regole di classificazione

DocBits rileva i documenti China Fapiao confrontando il namespace XML e il `fapiao_type`:

| Tipo di documento elettronico | Modello |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

L'elemento radice è `<fapiao>` con il namespace `urn:china:tax:fapiao:1.0`. La classificazione usa il principio **primo risultato vincente**, ordinato per lunghezza del modello (il più lungo prima).

## Vedi anche

- [Standard di e-fatturazione attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
