---
description: Obsługa dokumentów elektronicznych ARGENTINA AFIP w DocBits
---

# 🇦🇷 ARGENTINA AFIP

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Argentyna](countries/argentina.md). Wpis klasyfikacji not kredytowych nie ma dedykowanego pakietu ekstrakcji w sprawdzonym stanie. Zweryfikuj faktycznie używane mapowanie i przetestuj rzeczywisty przykład noty kredytowej.
{% endhint %}

| Właściwość           | Wartość                                                                    |
| -------------------- | -------------------------------------------------------------------------- |
| **Kraj / Region**    | Argentyna                                                                  |
| **Typy dokumentów**  | Invoice                                                                    |
| **Format**           | XML                                                                        |
| **Standard**         | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Ustawienia regionalne** | `es_AR`                                                               |

Standard ARGENTINA AFIP to format faktury elektronicznej argentyńskiego federalnego urzędu skarbowego (AFIP). Dokumenty są identyfikowane za pomocą `<tipoComprobante>` — np. typ `001` = Factura A. Każda faktura zawiera numer CAE (Código de Autorización Electrónica) oraz kod kreskowy do walidacji w AFIP.

## Status obsługi

| Komponent        | Status       |
| ---------------- | ------------ |
| Podgląd          | ✅ Obsługiwany |
| Ekstrakcja pól   | ✅ Obsługiwana |
| Transformacja    | ✅ Obsługiwana |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Podgląd faktury ARGENTINA AFIP w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits           | Źródłowy element XML                                 | Uwagi                                                          |
| ---------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Format: `PPPP-NNNNNNNN`                                        |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                                |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                                |
| `currency`             | Stała wartość: `ARS`                                 | Zawsze peso argentyńskie                                       |
| `total_amount`         | `<totales>/<total>`                                  |                                                                |
| `net_amount`           | `<totales>/<netoGravado>` lub `<subtotal>`           |                                                                |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                                |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                                |
| `supplier_id`          | `<emisor>/<CUIT>` lub `<cabecera>/<CUIT>`            | CUIT = argentyński numer identyfikacji podatkowej              |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                                |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                                |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                                |
| `supplier_country`     | Stała wartość: `AR`                                  |                                                                |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                                |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                                |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                                |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                                |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                                |
| `buyer_country`        | Stała wartość: `AR`                                  |                                                                |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Zwykle puste — dokumenty AFIP rzadko zawierają dane bankowe    |
| `bic`                  | `<PAYMENT/BIC>`                                      | Zwykle puste                                                   |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Zwykle puste                                                   |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Zwykle puste                                                   |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `<items>/<item>`

| Kolumna       | Atrybut / element źródłowy | Uwagi                                        |
| ------------- | -------------------------- | -------------------------------------------- |
| `POSITION`    | atrybut `@numero`          | Numer kolejny pozycji                        |
| `DESCRIPTION` | `<descripcion>`            |                                              |
| `QUANTITY`    | `<cantidad>`               |                                              |
| `UNIT`        | `<unidadMedida>`           | Kod jednostki AFIP (np. `7` = sztuka)        |
| `UNIT_PRICE`  | `<precioUnitario>`         |                                              |
| `VAT_RATE`    | `<alicuotaIVA>`            | np. `21.00` dla standardowego VAT w Argentynie |
| `VAT`         | `<importeIVA>`             |                                              |
| `NET_AMOUNT`  | `<subtotal>`               | Wartość pozycji przed opodatkowaniem         |

## Reguła klasyfikacji

DocBits wykrywa dokumenty ARGENTINA AFIP za pomocą wzorca regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Typ `001` odpowiada **Factura A** (faktura dla nabywców zarejestrowanych jako podatnicy VAT). Pozostałe typy comprobante są obsługiwane przez standard ARGENTINA FACTURA ELECTRONICA.

## Powiązane

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Obsługiwane dokumenty elektroniczne](./)
