---
description: Supporto per documenti elettronici TEAPPSXML della Finlandia in DocBits
---

# 🇫🇮 Finlandia TEAPPSXML

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Finlandia |
| **Tipi di documento** | Fattura, Nota di credito |
| **Formato** | XML |
| **Standard** | TEAPPSXML 3.0 (Tieto / Settore bancario finlandese) |
| **Impostazioni locali** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) è uno standard di fattura elettronica finlandese utilizzato principalmente nel settore bancario e finanziario. L'elemento radice è `<TEAPPSXML>` con lo spazio dei nomi `urn:TEAPPSXML:3.0`. DocBits rileva i documenti TEAPPSXML dalla presenza di `xmlns="urn:TEAPPSXML:"` nell'elemento radice.

Il formato TEAPPSXML utilizza nomi di elementi in maiuscolo e una struttura piatta con sezioni separate `<SENDER>`, `<RECEIVER>`, `<INVOICE>` e `<PAYMENTINFO>`. Il formato dell'ID aziendale finlandese (Y-tunnus) è `1234567-8`, e i numeri IVA utilizzano il prefisso `FI` (es. `FI12345678`).

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="finland-teappsxml-preview.png" alt="Anteprima fattura TEAPPSXML della Finlandia in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura TEAPPSXML della Finlandia</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Numero fattura |
| `invoice_date` | `INVOICE/INVOICEDATE` | Data di emissione (AAAA-MM-GG) |
| `due_date` | `INVOICE/DUEDATE` | Data di scadenza del pagamento (AAAA-MM-GG) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Tipo di messaggio (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Codice valuta (tipicamente `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Numero di riferimento pagamento |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Riferimento di pagamento finlandese (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Importo netto IVA esclusa |
| `tax_amount` | `INVOICE/TOTALVAT` | Importo IVA totale |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Importo totale IVA inclusa |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Metodo di pagamento (es. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Nome della società mittente |
| `supplier_id` | `SENDER/ID` | ID aziendale finlandese (Y-tunnus, es. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Numero IVA (es. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Indirizzo del mittente |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Città del mittente |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | CAP del mittente |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | Codice paese ISO (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Codice BIC della banca del mittente |
| `buyer_name` | `INVOICE/BUYER/NAME` | Nome della società acquirente |
| `buyer_id` | `INVOICE/BUYER/ID` | ID aziendale finlandese dell'acquirente |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Indirizzo dell'acquirente |
| `buyer_city` | `INVOICE/BUYER/CITY` | Città dell'acquirente |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | CAP dell'acquirente |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | Codice paese ISO (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN del beneficiario |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Codice BIC del beneficiario |

### Tabella righe (`INVOICE_TABLE`)

Percorso riga: `INVOICE/LINES/LINE`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `LINENUMBER` | Numero di sequenza riga |
| `DESCRIPTION` | `ARTICLENAME` | Nome / descrizione articolo |
| `QUANTITY` | `QUANTITY` | Quantità fatturata |
| `UNIT` | `UNIT` | Unità di misura (es. `KPL` = pezzo) |
| `UNIT_PRICE` | `UNITPRICE` | Prezzo unitario IVA esclusa |
| `VAT_RATE` | `VATRATE` | Aliquota IVA in % (standard 25,5%) |
| `VAT` | Calcolato | Importo IVA per riga |
| `NET_AMOUNT` | `LINEAMOUNT` | Totale riga IVA esclusa |

## Regola di classificazione

DocBits rileva i documenti TEAPPSXML facendo corrispondere l'attributo `xmlns` sull'elemento radice `<TEAPPSXML>`:

| Tipo documento elettronico | Schema |
|--------------------------|---------|
| TEAPPSXML | `xmlns` contiene `urn:TEAPPSXML:` |

## Correlati

- [Standard di fatturazione elettronica attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Finlandia Finvoice](./finland-finvoice.md)
- [Documenti elettronici supportati](./)
