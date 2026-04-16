---
description: Ondersteuning voor CHILE DTE elektronische documenten in DocBits
---

# 🇨🇱 CHILE DTE

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Chili |
| **Documenttypen** | Factuur, Creditnota, Debetnota, Afleveringsbon |
| **Formaat** | XML |
| **Standaard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) is de Chileense standaard voor elektronische fiscale documenten, gereguleerd door de Servicio de Impuestos Internos (SII). Alle DTE-documenten delen de namespace `http://www.sii.cl/SiiDte`. DocBits detecteert automatisch het DTE-typecode (`TipoDTE`) en routeert naar de juiste extractieregels:

| Typecode | Documenttype |
|-----------|--------------|
| 33 | Factura Electrónica (Factuur) |
| 34 | Factura No Afecta o Exenta (Vrijgestelde factuur) |
| 52 | Guía de Despacho (Afleveringsbon) |
| 56 | Nota de Débito (Debetnota) |
| 61 | Nota de Crédito (Creditnota) |

| Ondersteuningsstatus |  |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="chile-dte-preview.png" alt="Voorbeeld van Chile DTE-factuur in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een CHILE DTE FACTURA (type 33)</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `Folio` | Folionummer van het document |
| `invoice_date` | `FchEmis` | Emissiedatum ISO 8601 |
| `due_date` | `FchVenc` | Vervaldatum |
| `currency` | Vast: `CLP` | Altijd Chileense peso |
| `total_amount` | `MntTotal` | Totaalbedrag inclusief btw |
| `net_amount` | `MntNeto` | Netto belastbaar bedrag |
| `tax_amount` | `IVA` | BTW-bedrag (standaardtarief 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Bedrijfsnaam afzender |
| `supplier_id` | `RUTEmisor` | RUT van de afzender (bijv. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adres van de afzender |
| `supplier_city` | `CiudadOrigen` | Stad van de afzender |
| `supplier_country` | Vast: `CL` | Altijd Chili |
| `buyer_name` | `RznSocRecep` | Bedrijfsnaam ontvanger |
| `buyer_id` | `RUTRecep` | RUT van de ontvanger |
| `buyer_address` | `DirRecep` | Adres van de ontvanger |
| `buyer_city` | `CiudadRecep` | Stad van de ontvanger |
| `buyer_country` | Vast: `CL` | Altijd Chili |

### Regeltabel (`INVOICE_TABLE`)

Regelpad: `Detalle`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `NroLinDet` | Regelnummer |
| `DESCRIPTION` | `NmbItem` | Omschrijving van het artikel |
| `QUANTITY` | `QtyItem` | Hoeveelheid |
| `UNIT` | `UnmdItem` | Maateenheid |
| `UNIT_PRICE` | `PrcItem` | Eenheidsprijs exclusief btw |
| `VAT_RATE` | `TasaIVA` (uit de kop) | BTW-tarief in % (meestal 19%) |
| `VAT` | Berekend | BTW per regel |
| `NET_AMOUNT` | `MontoItem` | Regeltotaal |

## Classificatieregels

DocBits detecteert Chile DTE-documenten door de XML-namespace en `TipoDTE` te vergelijken:

| Elektronisch documenttype | Patroon |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Het envelop-element is `<EnvioDTE>` en elke DTE is verpakt in `<DTE><Documento>`.

## Zie ook

- [Momenteel ondersteunde e-facturatiestandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
