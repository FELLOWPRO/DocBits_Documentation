---
description: Podrška za CHILE DTE elektronske dokumente u DocBits-u
---

# 🇨🇱 CHILE DTE

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Čile |
| **Tipovi dokumenata** | Faktura (Factura), Kreditna napomena, Terećna napomena, Otpremnica |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Lokalizacija** | `es_CL` |

DTE (Documento Tributario Electrónico) je čileanski standard elektronskih poreskih dokumenata koji reguliše Servicio de Impuestos Internos (SII). Svi DTE dokumenti dele prostor imena `http://www.sii.cl/SiiDte`. DocBits automatski detektuje DTE kod tipa (`TipoDTE`) i usmerava na odgovarajuća pravila ekstrakcije:

| Kod tipa | Tip dokumenta |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="chile-dte-preview.png" alt="Pregled Chile DTE Factura u DocBits-u"><figcaption><p>Podrazumevani DocBits pregled za CHILE DTE FACTURA (tip 33)</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| Polje DocBits | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `Folio` | Broj folija dokumenta |
| `invoice_date` | `FchEmis` | Datum emisije ISO 8601 |
| `due_date` | `FchVenc` | Rok plaćanja |
| `currency` | Fiksno: `CLP` | Uvek čileanski pezo |
| `total_amount` | `MntTotal` | Ukupan iznos sa PDV-om |
| `net_amount` | `MntNeto` | Neto oporezivi iznos |
| `tax_amount` | `IVA` | Iznos PDV-a (standardna stopa 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Naziv kompanije izdavaoca |
| `supplier_id` | `RUTEmisor` | RUT izdavaoca (npr. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adresa izdavaoca |
| `supplier_city` | `CiudadOrigen` | Grad izdavaoca |
| `supplier_country` | Fiksno: `CL` | Uvek Čile |
| `buyer_name` | `RznSocRecep` | Naziv kompanije primaoca |
| `buyer_id` | `RUTRecep` | RUT primaoca |
| `buyer_address` | `DirRecep` | Adresa primaoca |
| `buyer_city` | `CiudadRecep` | Grad primaoca |
| `buyer_country` | Fiksno: `CL` | Uvek Čile |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `Detalle`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `NroLinDet` | Redni broj linije |
| `DESCRIPTION` | `NmbItem` | Naziv stavke |
| `QUANTITY` | `QtyItem` | Količina |
| `UNIT` | `UnmdItem` | Jedinica mere |
| `UNIT_PRICE` | `PrcItem` | Jedinična cena bez PDV-a |
| `VAT_RATE` | `TasaIVA` (iz zaglavlja) | Stopa PDV-a u % (obično 19%) |
| `VAT` | Izračunato | PDV po liniji |
| `NET_AMOUNT` | `MontoItem` | Ukupno po liniji |

## Pravila klasifikacije

DocBits detektuje Chile DTE dokumente podudaranjem XML prostora imena i `TipoDTE`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Element omotač je `<EnvioDTE>`, a svaki DTE je umotan u `<DTE><Documento>`.

## Srodni sadržaj

- [Trenutno podržani standardi e-faktura](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
