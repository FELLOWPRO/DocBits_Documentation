---
description: Supporto al documento elettronico Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) in DocBits
---

# 🇪🇨 Ecuador SRI

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Ecuador |
| **Tipi di Documento** | Factura (Fattura), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Formato** | XML |
| **Standard** | SRI (Servicio de Rentas Internas) |
| **Locale** | `es_EC` |

Lo standard di fattura elettronica Ecuador SRI è emesso sotto l'autorità del Servicio de Rentas Internas (SRI), l'autorità fiscale dell'Ecuador. I documenti utilizzano un formato XML proprietario con un elemento radice `<factura id="comprobante" version="X.X.X">`. DocBits rileva automaticamente la versione dall'attributo `version` e il tipo di documento da `codDoc`:

| Attributo version | Tipo di Documento |
|-------------------|---------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Il numero di fattura è un campo composito di tre elementi: `estab-ptoEmi-secuencial` (es. `001-001-000000001`). Il campo `claveAcceso` è una chiave di accesso a 49 cifre emessa dall'SRI per l'autenticazione del documento. L'Ecuador utilizza il **Dollaro USA (USD)** come valuta ufficiale.

## Stato del Supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione Campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima Predefinita

<figure><img src="ecuador-sri-preview.png" alt="Anteprima Ecuador SRI Factura in DocBits"><figcaption><p>Anteprima predefinita DocBits per una Factura Electrónica Ecuador SRI (versione 2.1.0)</p></figcaption></figure>

## Mappatura dei Campi

### Campi di Intestazione

| Campo DocBits | Elemento XML Sorgente | Note |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Composito: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Formato data `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Termine di pagamento (es. `30 dias`) |
| `currency` | Fisso: `USD` | Sempre Dollaro USA (valuta ufficiale dell'Ecuador) |
| `invoice_type` | Fisso: `Factura` | Etichetta tipo documento |
| `net_amount` | `infoFactura/totalSinImpuestos` | Totale netto escluso IVA |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Importo IVA (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Totale incluso IVA |
| `supplier_name` | `infoTributaria/razonSocial` | Ragione sociale dell'emittente |
| `supplier_id` | `infoTributaria/ruc` | RUC — codice fiscale a 13 cifre |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (uguale a supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Indirizzo sede principale dell'emittente |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | Codice metodo di pagamento SRI |
| `buyer_name` | `infoFactura/razonSocialComprador` | Ragione sociale dell'acquirente |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC o CI dell'acquirente |

### Tabella Righe Documento (`INVOICE_TABLE`)

Percorso riga: `detalles/detalle`

| Colonna | Elemento XML Sorgente | Note |
|---|---|---|
| `POSITION` | Indice sequenziale | Numero di riga a partire da 1 |
| `DESCRIPTION` | `descripcion` | Descrizione articolo |
| `QUANTITY` | `cantidad` | Quantità |
| `UNIT_PRICE` | `precioUnitario` | Prezzo unitario escluso IVA |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Aliquota IVA in % (es. 15%) |
| `VAT` | `impuestos/impuesto/valor` | Importo IVA per riga |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Totale riga escluso IVA |

## Regole di Classificazione

DocBits rileva i documenti Ecuador SRI corrispondendo l'elemento radice e l'attributo versione:

| Tipo Documento Elettronico | Pattern |
|--------------------------|---------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (qualsiasi versione) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

L'elemento radice è `<factura>` con `id="comprobante"`. L'attributo `version` determina la versione SRI specifica. La classificazione utilizza il principio **primo-corrispondente-vince**, ordinato per lunghezza del pattern (dal più lungo/specifico al più breve).

## Correlati

- [Standard di Fattura Elettronica Attualmente Supportati](../../currently-supported-e-invoice-standards/)
- [Documenti Elettronici Supportati](./)
