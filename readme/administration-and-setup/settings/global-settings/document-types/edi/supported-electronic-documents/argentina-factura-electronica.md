---
description: Supporto documenti elettronici ARGENTINA FACTURA ELECTRONICA in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Proprietà | Valore |
|-----------|--------|
| **Paese / Regione** | Argentina |
| **Tipi di documento** | Fattura |
| **Formato** | XML |
| **Standard** | Argentina Factura Electrónica (tipi di comprobante AFIP oltre Factura A) |
| **Lingua** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA copre l'insieme più ampio di documenti elettronici AFIP argentini oltre alla Factura A (tipo 001). Include Factura B (tipo 006), Factura C (tipo 011), Nota de Crédito (tipo 003) e altre varianti.

## Stato del supporto

| Componente | Stato |
|------------|-------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="argentina-factura-electronica-preview.png" alt="Anteprima Argentina Factura Electronica in DocBits"><figcaption><p>Anteprima DocBits predefinita per un documento ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elementi XML sorgente | Note |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Più percorsi XPath di fallback |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `due_date` | `//fechaVencimiento`, `//fechaVtoPago` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, fallback: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `supplier_id` | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |
| `buyer_id` | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID` | |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso riga: `<items>/<item>`, `<Items>/<Item>` o `<Detalle>/<Linea>`

| Colonna | Attributo / Elemento sorgente | Note |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` o `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `VAT` | `<importeIVA>`, `<ImporteIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Regola di classificazione

I documenti con valori `<tipoComprobante>` diversi da `001` vengono instradati a questo standard.

## Correlati

- [ARGENTINA AFIP](argentina-afip.md)
- [Documenti elettronici supportati](./)
