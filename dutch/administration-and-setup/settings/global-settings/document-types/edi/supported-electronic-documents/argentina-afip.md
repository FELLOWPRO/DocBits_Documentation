---
description: Ondersteuning voor het elektronische document ARGENTINA AFIP in DocBits
---

# 🇦🇷 ARGENTINA AFIP

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Argentinië](countries/argentina.md). De classificatievermelding voor creditnota’s heeft in de onderzochte status geen eigen extractiebundel. Controleer de daadwerkelijk gebruikte toewijzing en test een echt creditnotavoorbeeld.
{% endhint %}

| Eigenschap           | Waarde                                                                     |
| -------------------- | -------------------------------------------------------------------------- |
| **Land / regio**     | Argentinië                                                                 |
| **Documenttypes**    | Factuur                                                                    |
| **Formaat**          | XML                                                                        |
| **Standaard**        | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Locale**           | `es_AR`                                                                    |

De standaard ARGENTINA AFIP is het elektronische factuurformaat van de Argentijnse federale belastingdienst (AFIP). Documenten worden herkend aan `<tipoComprobante>`, bijvoorbeeld type `001` = Factura A. Elke factuur bevat een CAE-nummer (Código de Autorización Electrónica) en een barcode voor AFIP-validatie.

## Ondersteuningsstatus

| Component        | Status        |
| ---------------- | ------------- |
| Voorbeeld        | ✅ Ondersteund |
| Veldextractie    | ✅ Ondersteund |
| Transformatie    | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Voorbeeld van een Argentijnse AFIP-factuur in DocBits"><figcaption><p>Standaardvoorbeeld in DocBits van een ARGENTINA AFIP Factura A-factuur</p></figcaption></figure>

## Veldmapping

### Headervelden

| DocBits-veld           | Bron-XML-element                                     | Opmerkingen                                        |
| ---------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Opgemaakt als `PPPP-NNNNNNNN`                      |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                    |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                    |
| `currency`             | Vast: `ARS`                                          | Altijd Argentijnse peso                            |
| `total_amount`         | `<totales>/<total>`                                  |                                                    |
| `net_amount`           | `<totales>/<netoGravado>` of `<subtotal>`            |                                                    |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                    |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                    |
| `supplier_id`          | `<emisor>/<CUIT>` of `<cabecera>/<CUIT>`             | CUIT = Argentijns belastingnummer                  |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                    |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                    |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                    |
| `supplier_country`     | Vast: `AR`                                           |                                                    |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                    |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                    |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                    |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                    |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                    |
| `buyer_country`        | Vast: `AR`                                           |                                                    |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Meestal leeg — AFIP-documenten bevatten zelden bankgegevens |
| `bic`                  | `<PAYMENT/BIC>`                                      | Meestal leeg                                       |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Meestal leeg                                       |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Meestal leeg                                       |

### Tabel met regelitems (`INVOICE_TABLE`)

Rijpad: `<items>/<item>`

| Kolom         | Bronattribuut / -element   | Opmerkingen                                   |
| ------------- | -------------------------- | --------------------------------------------- |
| `POSITION`    | attribuut `@numero`        | Volgnummer van het item                       |
| `DESCRIPTION` | `<descripcion>`            |                                               |
| `QUANTITY`    | `<cantidad>`               |                                               |
| `UNIT`        | `<unidadMedida>`           | AFIP-eenheidscode (bijv. `7` = eenheid)       |
| `UNIT_PRICE`  | `<precioUnitario>`         |                                               |
| `VAT_RATE`    | `<alicuotaIVA>`            | bijv. `21.00` voor het standaard Argentijnse btw-tarief |
| `VAT`         | `<importeIVA>`             |                                               |
| `NET_AMOUNT`  | `<subtotal>`               | Regeltotaal vóór belasting                    |

## Classificatieregel

DocBits herkent ARGENTINA AFIP-documenten via het regex-patroon:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Type `001` komt overeen met **Factura A** (factuur aan btw-geregistreerde kopers). Andere comprobante-types worden afgehandeld door de standaard ARGENTINA FACTURA ELECTRONICA.

## Gerelateerd

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Ondersteunde elektronische documenten](./)
