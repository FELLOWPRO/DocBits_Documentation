---
description: CHILE DTE elektronisches Dokument in DocBits unterstützt
---

# 🇨🇱 CHILE DTE

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | Chile |
| **Dokumenttypen** | Rechnung (Factura), Gutschrift, Belastungsanzeige, Lieferschein |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) ist der chilenische Standard für elektronische Steuerdokumente, reguliert durch den Servicio de Impuestos Internos (SII). Alle DTE-Dokumente nutzen den gemeinsamen Namespace `http://www.sii.cl/SiiDte`. DocBits erkennt automatisch den DTE-Typcode (`TipoDTE`) und leitet zu den entsprechenden Extraktionsregeln weiter:

| Typcode | Dokumenttyp |
|-----------|--------------|
| 33 | Factura Electrónica (Rechnung) |
| 34 | Factura No Afecta o Exenta (Steuerbefreite Rechnung) |
| 52 | Guía de Despacho (Lieferschein) |
| 56 | Nota de Débito (Belastungsanzeige) |
| 61 | Nota de Crédito (Gutschrift) |

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="chile-dte-preview.png" alt="Chile DTE Factura Vorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für eine CHILE DTE FACTURA (Typ 33)</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | XML-Quellelement | Hinweise |
|---|---|---|
| `invoice_id` | `Folio` | Dokument-Folionummer |
| `invoice_date` | `FchEmis` | ISO 8601 Ausstellungsdatum |
| `due_date` | `FchVenc` | Fälligkeitsdatum |
| `currency` | Fest: `CLP` | Immer chilenischer Peso |
| `total_amount` | `MntTotal` | Gesamtbetrag inkl. MwSt. |
| `net_amount` | `MntNeto` | Nettobetrag steuerpflichtig |
| `tax_amount` | `IVA` | MwSt.-Betrag (19% Standardsatz) |
| `supplier_name` | `RznSoc` (Emisor) | Aussteller-Firmenname |
| `supplier_id` | `RUTEmisor` | Aussteller-RUT (z.B. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Aussteller-Straße |
| `supplier_city` | `CiudadOrigen` | Aussteller-Stadt |
| `supplier_country` | Fest: `CL` | Immer Chile |
| `buyer_name` | `RznSocRecep` | Empfänger-Firmenname |
| `buyer_id` | `RUTRecep` | Empfänger-RUT |
| `buyer_address` | `DirRecep` | Empfänger-Straße |
| `buyer_city` | `CiudadRecep` | Empfänger-Stadt |
| `buyer_country` | Fest: `CL` | Immer Chile |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `Detalle`

| Spalte | XML-Quellelement | Hinweise |
|---|---|---|
| `POSITION` | `NroLinDet` | Positionsnummer |
| `DESCRIPTION` | `NmbItem` | Artikelbezeichnung |
| `QUANTITY` | `QtyItem` | Menge |
| `UNIT` | `UnmdItem` | Maßeinheit |
| `UNIT_PRICE` | `PrcItem` | Einzelpreis excl. MwSt. |
| `VAT_RATE` | `TasaIVA` (aus Kopf) | IVA-Satz in % (typisch 19%) |
| `VAT` | Berechnet | MwSt. pro Zeile |
| `NET_AMOUNT` | `MontoItem` | Zeilensumme |

## Klassifikationsregeln

DocBits erkennt Chile DTE-Dokumente durch Übereinstimmung des XML-Namespace und `TipoDTE`:

| Elektronischer Dokumenttyp | Muster |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Das Hüllenelement ist `<EnvioDTE>` und jedes DTE ist in `<DTE><Documento>` eingebettet.

## Siehe auch

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
