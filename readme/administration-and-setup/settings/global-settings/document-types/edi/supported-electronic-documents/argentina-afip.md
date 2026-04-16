---
description: Obsługa dokumentów elektronicznych ARGENTINA AFIP w DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Właściwość | Wartość |
|------------|---------|
| **Kraj / Region** | Argentyna |
| **Typy dokumentów** | Faktura |
| **Format** | XML |
| **Standard** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Język** | `es_AR` |

Standard ARGENTINA AFIP to format faktury elektronicznej argentyńskiego federalnego urzędu skarbowego (AFIP). Dokumenty są identyfikowane przez `<tipoComprobante>` — np. typ `001` = Factura A. Każda faktura zawiera numer CAE (Código de Autorización Electrónica) i kod kreskowy do walidacji AFIP.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="argentina-afip-preview.png" alt="Podgląd faktury ARGENTINA AFIP w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Format: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Stały: `ARS` | Zawsze Peso argentyńskie |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` lub `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` lub `<cabecera>/<CUIT>` | CUIT = argentyński numer podatkowy |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Stały: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Stały: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Zazwyczaj puste |
| `bic` | `<PAYMENT/BIC>` | Zazwyczaj puste |
| `payment_terms` | `<PAYMENT_TERMS>` | Zazwyczaj puste |
| `purchase_order` | `<PURCHASE_ORDER>` | Zazwyczaj puste |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `<items>/<item>`

| Kolumna | Atrybut / Element źródłowy | Uwagi |
|---|---|---|
| `POSITION` | Atrybut `@numero` | Numer pozycji |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | Kod jednostki AFIP (np. `7` = jednostka) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | np. `21.00` dla standardowego argentyńskiego VAT |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Suma wiersza przed opodatkowaniem |

## Reguła klasyfikacji

DocBits wykrywa dokumenty ARGENTINA AFIP za pomocą wzorca regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

## Powiązane

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Obsługiwane dokumenty elektroniczne](./)
