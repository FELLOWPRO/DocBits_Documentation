---
description: Unterstützung für elektronische CHILE DTE-Dokumente in DocBits
---

# 🇨🇱 CHILE DTE

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Chile |
| **Dokumenttypen** | Rechnung (Factura), Gutschrift, Lastschrift, Lieferschein |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Gebietsschema** | `es_CL` |

DTE (Documento Tributario Electrónico) ist der chilenische Standard für elektronische Steuerdokumente, der vom Servicio de Impuestos Internos (SII) geregelt wird. Alle DTE-Dokumente verwenden den Namespace `http://www.sii.cl/SiiDte`. DocBits erkennt den DTE-Typcode (`TipoDTE`) automatisch und leitet ihn an die entsprechenden Extraktionsregeln weiter:

| Typcode | Dokumenttyp |
|---------|------------|
| 33 | Factura Electrónica (Rechnung) |
| 34 | Factura No Afecta o Exenta (Steuerbefreite Rechnung) |
| 52 | Guía de Despacho (Lieferschein) |
| 56 | Nota de Débito (Lastschrift) |
| 61 | Nota de Crédito (Gutschrift) |

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="chile-dte-preview.png" alt="Chile DTE Factura-Vorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine CHILE DTE FACTURA (Typ 33)</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `Folio` | Folio-Nummer des Dokuments |
| `invoice_date` | `FchEmis` | Ausstellungsdatum nach ISO 8601 |
| `due_date` | `FchVenc` | Fälligkeitsdatum der Zahlung |
| `currency` | Fest: `CLP` | Immer Chilenischer Peso |
| `total_amount` | `MntTotal` | Gesamtbetrag inkl. MwSt. |
| `net_amount` | `MntNeto` | Netto-Steuerbetrag |
| `tax_amount` | `IVA` | MwSt.-Betrag (Normalsatz 19 %) |
| `supplier_name` | `RznSoc` (Emisor) | Name des ausstellenden Unternehmens |
| `supplier_id` | `RUTEmisor` | RUT des Ausstellers (z. B. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Straßenadresse des Ausstellers |
| `supplier_city` | `CiudadOrigen` | Stadt des Ausstellers |
| `supplier_country` | Fest: `CL` | Immer Chile |
| `buyer_name` | `RznSocRecep` | Name des empfangenden Unternehmens |
| `buyer_id` | `RUTRecep` | RUT des Empfängers |
| `buyer_address` | `DirRecep` | Straßenadresse des Empfängers |
| `buyer_city` | `CiudadRecep` | Stadt des Empfängers |
| `buyer_country` | Fest: `CL` | Immer Chile |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `Detalle`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | `NroLinDet` | Laufende Zeilennummer |
| `DESCRIPTION` | `NmbItem` | Artikelname |
| `QUANTITY` | `QtyItem` | Menge |
| `UNIT` | `UnmdItem` | Maßeinheit |
| `UNIT_PRICE` | `PrcItem` | Stückpreis ohne MwSt. |
| `VAT_RATE` | `TasaIVA` (aus Kopf) | IVA-Satz in % (typischerweise 19 %) |
| `VAT` | Berechnet | MwSt. pro Position |
| `NET_AMOUNT` | `MontoItem` | Positionsgesamtbetrag |

## Klassifizierungsregeln

DocBits erkennt Chile-DTE-Dokumente durch Abgleich des XML-Namespace mit `TipoDTE`:

| Elektronischer Dokumenttyp | Muster |
|----------------------------|--------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Das Umschlagselement ist `<EnvioDTE>` und jedes DTE ist in `<DTE><Documento>` eingebettet.

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
