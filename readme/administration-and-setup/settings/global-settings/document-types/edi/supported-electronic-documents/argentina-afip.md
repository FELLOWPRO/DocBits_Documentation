---
description: Supporto dei documenti elettronici ARGENTINA AFIP in DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Proprietà               | Valore                                                                     |
| ----------------------- | -------------------------------------------------------------------------- |
| **Paese / Regione**     | Argentina                                                                  |
| **Tipi di documento**   | Fattura                                                                    |
| **Formato**             | XML                                                                        |
| **Standard**            | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Impostazioni locali** | `es_AR`                                                                    |

Lo standard ARGENTINA AFIP è il formato di fattura elettronica dell'autorità fiscale federale argentina (AFIP). I documenti vengono identificati tramite `<tipoComprobante>`, ad esempio il tipo `001` = Factura A. Ogni fattura contiene un numero CAE (Código de Autorización Electrónica) e un codice a barre per la convalida AFIP.

## Stato del supporto

| Componente          | Stato       |
| ------------------- | ----------- |
| Anteprima           | ✅ Supportata |
| Estrazione dei campi | ✅ Supportata |
| Trasformazione      | ✅ Supportata |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Anteprima di una fattura ARGENTINA AFIP in DocBits"><figcaption><p>Anteprima predefinita di DocBits per una fattura ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits          | Elemento XML di origine                              | Note                                                         |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Formattato come `PPPP-NNNNNNNN`                              |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                              |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                              |
| `currency`             | Fisso: `ARS`                                         | Sempre peso argentino                                        |
| `total_amount`         | `<totales>/<total>`                                  |                                                              |
| `net_amount`           | `<totales>/<netoGravado>` oppure `<subtotal>`        |                                                              |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                              |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                              |
| `supplier_id`          | `<emisor>/<CUIT>` oppure `<cabecera>/<CUIT>`         | CUIT = codice fiscale argentino                              |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                              |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                              |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                              |
| `supplier_country`     | Fisso: `AR`                                          |                                                              |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                              |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                              |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                              |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                              |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                              |
| `buyer_country`        | Fisso: `AR`                                          |                                                              |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Di solito vuoto: i documenti AFIP raramente contengono dati bancari |
| `bic`                  | `<PAYMENT/BIC>`                                      | Di solito vuoto                                              |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Di solito vuoto                                              |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Di solito vuoto                                              |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso della riga: `<items>/<item>`

| Colonna       | Attributo / Elemento di origine | Note                                         |
| ------------- | ------------------------------- | -------------------------------------------- |
| `POSITION`    | attributo `@numero`             | Numero progressivo della riga                |
| `DESCRIPTION` | `<descripcion>`                 |                                              |
| `QUANTITY`    | `<cantidad>`                    |                                              |
| `UNIT`        | `<unidadMedida>`                | Codice unità AFIP (ad es. `7` = unità)       |
| `UNIT_PRICE`  | `<precioUnitario>`              |                                              |
| `VAT_RATE`    | `<alicuotaIVA>`                 | ad es. `21.00` per l'IVA standard argentina  |
| `VAT`         | `<importeIVA>`                  |                                              |
| `NET_AMOUNT`  | `<subtotal>`                    | Totale della riga al netto delle imposte     |

## Regola di classificazione

DocBits riconosce i documenti ARGENTINA AFIP tramite il seguente pattern regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Il tipo `001` corrisponde alla **Factura A** (fattura per acquirenti registrati ai fini IVA). Gli altri tipi di comprobante sono gestiti dallo standard ARGENTINA FACTURA ELECTRONICA.

## Correlati

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Documenti elettronici supportati](./)
