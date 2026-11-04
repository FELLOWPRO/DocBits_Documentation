---
description: Ondersteuning voor elektronische documenten Finland TEAPPSXML in DocBits
---

# 🇫🇮 Finland TEAPPSXML

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Finland |
| **Documenttypen** | Factuur, Creditnota |
| **Formaat** | XML |
| **Standaard** | TEAPPSXML 3.0 (Tieto / Finse banksector) |
| **Landinstelling** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) is een Finse elektronische factuurstandaard die voornamelijk wordt gebruikt in de bank- en financiële sector. Het rootelement is `<TEAPPSXML>` met de naamruimte `urn:TEAPPSXML:3.0`. DocBits detecteert TEAPPSXML-documenten door de aanwezigheid van `xmlns="urn:TEAPPSXML:"` in het rootelement.

Het TEAPPSXML-formaat gebruikt elementnamen in hoofdletters en een platte structuur met afzonderlijke secties `<SENDER>`, `<RECEIVER>`, `<INVOICE>` en `<PAYMENTINFO>`. Het Finse bedrijfs-ID-formaat (Y-tunnus) is `1234567-8`, en btw-nummers gebruiken het voorvoegsel `FI` (bijv. `FI12345678`).

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="finland-teappsxml-preview.png" alt="Finland TEAPPSXML factuurvoorbeeld in DocBits"><figcaption><p>Standaardvoorbeeld in DocBits voor een Finland TEAPPSXML-factuur</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Factuurnummer |
| `invoice_date` | `INVOICE/INVOICEDATE` | Uitgifte datum (JJJJ-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Vervaldatum betaling (JJJJ-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Berichttype (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Valutacode (doorgaans `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Betalingsreferentienummer |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Finse betalingsreferentie (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Nettobedrag excl. btw |
| `tax_amount` | `INVOICE/TOTALVAT` | Totaal btw-bedrag |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Totaalbedrag incl. btw |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Betaalmethode (bijv. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Naam verzenderbedrijf |
| `supplier_id` | `SENDER/ID` | Fins bedrijfs-ID (Y-tunnus, bijv. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Btw-nummer (bijv. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Adres verzender |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Stad van verzender |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Postcode verzender |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | ISO-landcode (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | BIC-code bank verzender |
| `buyer_name` | `INVOICE/BUYER/NAME` | Naam kopersbedrijf |
| `buyer_id` | `INVOICE/BUYER/ID` | Fins bedrijfs-ID van koper |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Kopersadres |
| `buyer_city` | `INVOICE/BUYER/CITY` | Stad van koper |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Postcode koper |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | ISO-landcode (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN begunstigde |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | BIC-code begunstigde |

### Regeltabel (`INVOICE_TABLE`)

Rijpad: `INVOICE/LINES/LINE`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `LINENUMBER` | Volgordegetal regel |
| `DESCRIPTION` | `ARTICLENAME` | Artikelnaam / -omschrijving |
| `QUANTITY` | `QUANTITY` | Gefactureerde hoeveelheid |
| `UNIT` | `UNIT` | Maateenheid (bijv. `KPL` = stuk) |
| `UNIT_PRICE` | `UNITPRICE` | Stukprijs excl. btw |
| `VAT_RATE` | `VATRATE` | Btw-tarief in % (standaard 25,5%) |
| `VAT` | Berekend | Btw-bedrag per regel |
| `NET_AMOUNT` | `LINEAMOUNT` | Regeltotaal excl. btw |

## Classificatieregel

DocBits detecteert TEAPPSXML-documenten door het `xmlns`-attribuut op het rootelement `<TEAPPSXML>` te matchen:

| Type elektronisch document | Patroon |
|--------------------------|---------|
| TEAPPSXML | `xmlns` bevat `urn:TEAPPSXML:` |

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Finland Finvoice](./finland-finvoice.md)
- [Ondersteunde elektronische documenten](./)
