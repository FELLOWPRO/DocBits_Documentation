---
description: Supporto per documenti elettronici AUSTRIA EBINTERFACE in DocBits
---
# 🇦🇹 AUSTRIA EBINTERFACE
| Proprietà | Valore |
|-----------|--------|
| **Paese / Regione** | Austria |
| **Tipi di documento** | Fattura, Nota di credito |
| **Formato** | XML |
| **Standard** | ebInterface (versioni 4.3 – 6.1) |
| **Locale** | `de_AT` |

ebInterface è lo standard austriaco per la fatturazione elettronica gestito dalla Camera Economica Federale Austriaca (WKÖ — Wirtschaftskammer Österreich). Definisce un formato XML strutturato per le fatture elettroniche utilizzato principalmente nelle transazioni B2G (business-to-government) e B2B in Austria. DocBits supporta tutte le versioni dalla 4.3 alla 6.1, ognuna identificata dal proprio namespace XML.

## Stato del supporto
| Componente | Stato |
|------------|-------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita
<figure><img src="austria-ebinterface-preview.png" alt="Anteprima fattura Austria ebInterface in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura AUSTRIA EBINTERFACE</p></figcaption></figure>

## Mappatura dei campi
### Campi intestazione
| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Numero fattura |
| `invoice_date` | `eb:InvoiceDate` | Data in formato ISO 8601 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Data di scadenza del pagamento |
| `delivery_date` | `eb:Delivery/eb:Date` | Data di consegna |
| `currency` | `@eb:InvoiceCurrency` | Attributo radice, sempre `EUR` per AT |
| `total_amount` | `eb:TotalGrossAmount` | Totale lordo IVA inclusa |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Base imponibile netta |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Importo IVA |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Riferimento ordine d'acquisto |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Condizioni di pagamento in testo libero |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Ragione sociale del fornitore |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | UID austriaco (es. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Indirizzo del fornitore |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Città del fornitore |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | CAP del fornitore |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | Codice paese ISO |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | Email del fornitore |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN del fornitore |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Ragione sociale del destinatario |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID del destinatario |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Indirizzo del destinatario |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Città del destinatario |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | CAP del destinatario |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | Codice paese ISO |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN per il pagamento |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC per il pagamento |

### Tabella righe (`INVOICE_TABLE`)
Percorso riga: `eb:Details/eb:ItemList/eb:ListLineItem`
| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | Indice sequenziale | Numero riga a partire da 1 |
| `DESCRIPTION` | `eb:Description` | Descrizione del prodotto/servizio |
| `QUANTITY` | `eb:Quantity` | Quantità numerica |
| `UNIT` | `eb:Quantity/@eb:Unit` | Codice unità (es. `STK` = pezzo) |
| `UNIT_PRICE` | `eb:UnitPrice` | Prezzo unitario IVA esclusa |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Aliquota IVA in % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Importo IVA per riga |
| `NET_AMOUNT` | `eb:LineItemAmount` | Totale riga IVA esclusa |

## Regole di classificazione
| Versione | Namespace |
|----------|-----------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Tutte le versioni condividono l'elemento radice `<eb:Invoice>` con il rispettivo URI di namespace.

## Correlati
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Documenti elettronici supportati](./)
