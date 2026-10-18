---
description: Ondersteuning voor het elektronische document ARGENTINA FACTURA ELECTRONICA in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Argentinië](countries/argentina.md). De classificatievermelding voor creditnota’s heeft in de onderzochte status geen eigen extractiebundel. Controleer de daadwerkelijk gebruikte toewijzing en test een echt creditnotavoorbeeld.
{% endhint %}

| Eigenschap           | Waarde                                                                  |
| -------------------- | ----------------------------------------------------------------------- |
| **Land / regio**     | Argentinië                                                              |
| **Documenttypes**    | Factuur                                                                 |
| **Formaat**          | XML                                                                     |
| **Standaard**        | Argentina Factura Electrónica (AFIP-comprobante-types buiten Factura A) |
| **Locale**           | `es_AR`                                                                 |

ARGENTINA FACTURA ELECTRONICA omvat de bredere set Argentijnse elektronische AFIP-documenten naast Factura A (type 001). Hieronder vallen andere comprobante-types zoals Factura B (type 006), Factura C (type 011), Nota de Crédito (type 003) en andere varianten. DocBits herkent het documenttype automatisch aan `<tipoComprobante>` en past de bijbehorende extractie toe.

## Ondersteuningsstatus

| Component        | Status        |
| ---------------- | ------------- |
| Voorbeeld        | ✅ Ondersteund |
| Veldextractie    | ✅ Ondersteund |
| Transformatie    | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Voorbeeld van Argentina Factura Electronica in DocBits"><figcaption><p>Standaardvoorbeeld in DocBits van een ARGENTINA FACTURA ELECTRONICA-document</p></figcaption></figure>

## Veldmapping

### Headervelden

| DocBits-veld     | Bron-XML-elementen                                                        | Opmerkingen                                  |
| ---------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Meerdere XPath-terugvalopties voor variantschema's |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                              |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                              |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, terugval: `ARS`                        |                                              |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                              |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                              |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                              |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                              |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = Argentijns belastingnummer            |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                              |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                              |
| `iban`           | `//PAYMENT/IBAN`                                                          | Meestal leeg                                 |
| `bic`            | `//PAYMENT/BIC`                                                           | Meestal leeg                                 |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Meestal leeg                                 |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Meestal leeg                                 |

### Tabel met regelitems (`INVOICE_TABLE`)

Rijpad: `<items>/<item>`, `<Items>/<Item>` of `<Detalle>/<Linea>`

| Kolom         | Bronattribuut / -element                | Opmerkingen          |
| ------------- | --------------------------------------- | -------------------- |
| `POSITION`    | `@numero`, `<numero>` of `position()`   | Volgnummer van het item |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                      |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                      |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                      |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | bijv. `21.00`        |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                      |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Regeltotaal          |

## Classificatieregel

DocBits herkent ARGENTINA FACTURA ELECTRONICA-documenten aan de afwezigheid van de Factura A-markering: documenten met `<tipoComprobante>`-waarden anders dan `001` (bijv. `003`, `006`, `011`) worden naar deze standaard doorgestuurd.

## Gerelateerd

* [ARGENTINA AFIP](argentina-afip.md)
* [Ondersteunde elektronische documenten](./)
