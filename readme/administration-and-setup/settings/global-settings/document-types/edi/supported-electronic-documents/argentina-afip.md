---
description: ARGENTINA AFIP ondersteuning voor elektronische documenten in DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Argentinië |
| **Documenttypen** | Factuur |
| **Formaat** | XML |
| **Standaard** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Taal** | `es_AR` |

De ARGENTINA AFIP-standaard is het elektronische factuurformaat van de Argentijnse federale belastingdienst (AFIP). Documenten worden geïdentificeerd door `<tipoComprobante>` — bijv. type `001` = Factura A. Elke factuur bevat een CAE-nummer (Código de Autorización Electrónica) en een streepjescode voor AFIP-validatie.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="argentina-afip-preview.png" alt="ARGENTINA AFIP factuurvoorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een ARGENTINA AFIP Factura A factuur</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Formaat: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Vast: `ARS` | Altijd Argentijnse Peso |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` of `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` of `<cabecera>/<CUIT>` | CUIT = Argentijns belastingnummer |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Vast: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Vast: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Meestal leeg |
| `bic` | `<PAYMENT/BIC>` | Meestal leeg |
| `payment_terms` | `<PAYMENT_TERMS>` | Meestal leeg |
| `purchase_order` | `<PURCHASE_ORDER>` | Meestal leeg |

### Regeltabel (`INVOICE_TABLE`)

Rijpad: `<items>/<item>`

| Kolom | Bron-attribuut / element | Opmerkingen |
|---|---|---|
| `POSITION` | `@numero` attribuut | Positienummer |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | AFIP-eenheidscode (bijv. `7` = eenheid) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | bijv. `21.00` voor standaard Argentijns BTW |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Regeltotaal voor belasting |

## Classificatieregel

DocBits detecteert ARGENTINA AFIP-documenten via het regex-patroon:

```
<tipoComprobante>001\s*</tipoComprobante>
```

## Gerelateerd

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Ondersteunde elektronische documenten](./)
