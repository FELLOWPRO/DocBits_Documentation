---
description: Podrška za CHILE DTE elektronska dokumenta u DocBits
---

# 🇨🇱 CHILE DTE

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Čile |
| **Tipovi dokumenata** | Faktura, Knjižni odobrenje, Knjižno zaduženje, Otpremnica |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) je čileanski standard elektronskih fiskalnih dokumenata regulisan od strane Servicio de Impuestos Internos (SII). Svi DTE dokumenti dele namespace `http://www.sii.cl/SiiDte`. DocBits automatski detektuje kod tipa DTE (`TipoDTE`) i usmerava ka odgovarajućim pravilima za ekstrakciju:

| Kod tipa | Tip dokumenta |
|-----------|--------------|
| 33 | Factura Electrónica (Faktura) |
| 34 | Factura No Afecta o Exenta (Oslobođena faktura) |
| 52 | Guía de Despacho (Otpremnica) |
| 56 | Nota de Débito (Knjižno zaduženje) |
| 61 | Nota de Crédito (Knjižno odobrenje) |

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="chile-dte-preview.png" alt="Pregled fakture Chile DTE u DocBits"><figcaption><p>Podrazumevani DocBits pregled za CHILE DTE FACTURA (tip 33)</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `Folio` | Broj folija dokumenta |
| `invoice_date` | `FchEmis` | Datum izdavanja ISO 8601 |
| `due_date` | `FchVenc` | Datum dospijeća |
| `currency` | Fiksno: `CLP` | Uvek čileanski peso |
| `total_amount` | `MntTotal` | Ukupan iznos sa PDV |
| `net_amount` | `MntNeto` | Neto oporezivi iznos |
| `tax_amount` | `IVA` | Iznos PDV (standardna stopa 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Naziv firma izdavaoca |
| `supplier_id` | `RUTEmisor` | RUT izdavaoca (npr. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adresa izdavaoca |
| `supplier_city` | `CiudadOrigen` | Grad izdavaoca |
| `supplier_country` | Fiksno: `CL` | Uvek Čile |
| `buyer_name` | `RznSocRecep` | Naziv firme primaoca |
| `buyer_id` | `RUTRecep` | RUT primaoca |
| `buyer_address` | `DirRecep` | Adresa primaoca |
| `buyer_city` | `CiudadRecep` | Grad primaoca |
| `buyer_country` | Fiksno: `CL` | Uvek Čile |

### Tabela stavki (`INVOICE_TABLE`)

Putanja stavke: `Detalle`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `NroLinDet` | Broj stavke |
| `DESCRIPTION` | `NmbItem` | Opis artikla |
| `QUANTITY` | `QtyItem` | Količina |
| `UNIT` | `UnmdItem` | Jedinica mere |
| `UNIT_PRICE` | `PrcItem` | Jedinična cena bez PDV |
| `VAT_RATE` | `TasaIVA` (iz zaglavlja) | Stopa PDV u % (tipično 19%) |
| `VAT` | Izračunato | PDV po stavci |
| `NET_AMOUNT` | `MontoItem` | Ukupno po stavci |

## Pravila klasifikacije

DocBits detektuje Chile DTE dokumente uparivanjem XML namespace-a i `TipoDTE`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Element koverta je `<EnvioDTE>`, a svaki DTE je umotan u `<DTE><Documento>`.

## Takođe pogledajte

- [Trenutno podržani standardi e-fakturisanja](../../currently-supported-e-invoice-standards/)
- [Podržana elektronska dokumenta](./)
