---
description: Podrška za kolumbijske DIAN elektronske dokumente u DocBitsu (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Kolumbija DIAN

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Colombia |
| **Tipovi dokumenata** | Faktura (Factura Electrónica), Knjižno odobrenje (Nota de Crédito), Documento Soporte |
| **Format** | XML (UBL 2.1) |
| **Standard** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Lokalizacija** | `es_CO` |

Kolumbijski standard elektronskog fakturisanja reguliše **DIAN** (Dirección de Impuestos y Aduanas Nacionales). Zasnovan je na UBL 2.1 sa DIAN-specifičnim proširenjima (`sts:DianExtensions`). DocBits detektuje Colombia DIAN dokumente putem DIAN prostora imena i usmerava ih prema `CustomizationID`:

| CustomizationID | Tip dokumenta |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Knjižno odobrenje) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

DIAN identifikator (**NIT** — Número de Identificación Tributaria) koristi `schemeID="31"` u UBL `CompanyID` elementu.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="colombia-dian-preview.png" alt="Pregled Colombia DIAN Factura Electrónica u DocBitsu"><figcaption><p>Podrazumevani DocBits pregled za COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `cbc:ID` | Broj fakture sa prefiksom (npr. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Datum izdavanja (ISO 8601) |
| `due_date` | `cbc:DueDate` | Rok plaćanja |
| `currency` | `cbc:DocumentCurrencyCode` | Uvek `COP` (Kolumbijski pezos) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Ukupno za plaćanje uklj. PDV |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Neto iznos bez PDV-a |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Ukupan PDV (standardna stopa 19%) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Pravno ime dobavljača |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT dobavljača (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Pravno ime kupca |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT kupca (schemeID=31) |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `cac:InvoiceLine` (ili `cac:CreditNoteLine`)

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `cbc:ID` | Broj reda |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Opis proizvoda ili usluge |
| `QUANTITY` | `cbc:InvoicedQuantity` | Količina sa atributom koda jedinice |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Jedinična cena bez PDV-a |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Ukupno za red bez PDV-a |

## Pravila klasifikacije

DocBits detektuje Colombia DIAN dokumente prema DIAN stringu prostora imena:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

Korijenski element je `<Invoice>` (UBL 2.1) za fakture, `<CreditNote>` za knjižna odobrenja. Svi dokumenti sadrže blok `<sts:DianExtensions>` sa DIAN podacima o autorizaciji (`InvoiceAuthorization`, `CUFE`/`CUDE` UUID, QR kod).

## Povezano

- [Trenutno podržani standardi e-faktura](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
