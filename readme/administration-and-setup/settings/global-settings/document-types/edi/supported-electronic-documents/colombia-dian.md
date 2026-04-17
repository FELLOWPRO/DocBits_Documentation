---
description: Supporto per documenti elettronici colombiani DIAN in DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Colombia DIAN

| Proprietà | Valore |
|-----------|--------|
| **Paese / Regione** | Colombia |
| **Tipi di documento** | Fattura (Factura Electrónica), Nota di credito (Nota de Crédito), Documento Soporte |
| **Formato** | XML (UBL 2.1) |
| **Standard** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Lingua/Paese** | `es_CO` |

Lo standard colombiano di fatturazione elettronica è regolamentato dalla **DIAN** (Dirección de Impuestos y Aduanas Nacionales). Si basa su UBL 2.1 con estensioni specifiche della DIAN (`sts:DianExtensions`). DocBits rileva i documenti Colombia DIAN tramite il namespace DIAN e li instrada in base alla `CustomizationID`:

| CustomizationID | Tipo di documento |
|-----------------|------------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Nota di credito) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

L'identificatore DIAN (**NIT** — Número de Identificación Tributaria) utilizza `schemeID="31"` nell'elemento UBL `CompanyID`.

## Stato del supporto

| Componente | Stato |
|------------|-------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="colombia-dian-preview.png" alt="Anteprima della Factura Electrónica Colombia DIAN in DocBits"><figcaption><p>Anteprima predefinita DocBits per una COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numero fattura con prefisso (es. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Data di emissione (ISO 8601) |
| `due_date` | `cbc:DueDate` | Data di scadenza del pagamento |
| `currency` | `cbc:DocumentCurrencyCode` | Sempre `COP` (Peso colombiano) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Importo totale IVA inclusa |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Importo netto IVA esclusa |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Importo IVA totale (aliquota standard 19%) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Ragione sociale del fornitore |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT del fornitore (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Ragione sociale dell'acquirente |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT dell'acquirente (schemeID=31) |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso riga: `cac:InvoiceLine` (o `cac:CreditNoteLine`)

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `cbc:ID` | Numero di riga |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descrizione del prodotto o servizio |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantità con attributo codice unità |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Prezzo unitario IVA esclusa |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Totale riga IVA esclusa |

## Regole di classificazione

DocBits rileva i documenti Colombia DIAN tramite la stringa del namespace DIAN:

| Tipo di documento elettronico | Schema |
|-------------------------------|--------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

L'elemento radice è `<Invoice>` (UBL 2.1) per le fatture e `<CreditNote>` per le note di credito. Tutti i documenti includono un blocco `<sts:DianExtensions>` con i dati di autorizzazione DIAN (`InvoiceAuthorization`, UUID `CUFE`/`CUDE`, codice QR).

## Correlati

- [Standard di fatturazione elettronica supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
