---
description: India GST E-Rechnung – Unterstützung elektronischer Dokumente in DocBits
---

# 🇮🇳 Indien GST E-Rechnung

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Indien |
| **Dokumenttypen** | Rechnung (INV), Gutschrift (CRN), Lastschrift (DBN) |
| **Format** | XML (`<SignedInvoice>`) |
| **Standard** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Gebietsschema** | `en_IN` |

Die Indien GST E-Rechnung ist der obligatorische elektronische Rechnungsstandard im Rahmen des indischen Goods and Services Tax (GST)-Systems, betrieben von GSTN (GST Network). Unternehmen, die den vorgeschriebenen Umsatzschwellenwert überschreiten, müssen E-Rechnungen über das Invoice Registration Portal (IRP) ausstellen, das die Rechnung signiert und eine **IRN** (Rechnungsreferenznummer – ein 64-Zeichen-SHA-256-Hash) sowie einen QR-Code zurückgibt.

DocBits erkennt GST-E-Rechnungsdokumente anhand des Vorhandenseins von `<SignedInvoice>` als Wurzelelement. Das Format umfasst drei GST-Steuerkomponenten:

| Steuerkomponente | Beschreibung |
|-----------------|--------------|
| IGST | Integrated GST – gilt für zwischenstaatliche Transaktionen |
| CGST | Central GST – gilt für innerstaatliche Transaktionen (Bundeskomponente) |
| SGST | State GST – gilt für innerstaatliche Transaktionen (Staatskomponente) |

Die Steuerpflichtige-Kennung ist die **GSTIN** (Goods and Services Tax Identification Number), ein 15-stelliger alphanumerischer Code im Format `29AABCU9603R1ZM` (2-stelliger Staatscode + 10-stellige PAN + Entitätsnummer + Prüfziffer). Datumsangaben verwenden das Format `TT/MM/JJJJ`.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="india-gst-e-invoice-preview.png" alt="Indien GST E-Rechnung Vorschau in DocBits"><figcaption><p>Standardvorschau von DocBits für eine Indien GST E-Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | XML-Quellelement | Anmerkungen |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Rechnungsnummer |
| `invoice_date` | `Invoice/DocDtls/Dt` | Ausstellungsdatum (`TT/MM/JJJJ`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Rechnung, CRN=Gutschrift, DBN=Lastschrift |
| `currency` | Fest: `INR` | Immer Indische Rupie |
| `net_amount` | `Invoice/ValDtls/AssVal` | Bemessungsgrundlage |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Gesamt-GST-Betrag |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Gesamtrechnungsbetrag inkl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Integrated GST-Betrag |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Central GST-Betrag |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | State GST-Betrag |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Cess-Betrag (falls zutreffend) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Rechtlicher Name des Verkäufers |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | Verkäufer-GSTIN (15 Zeichen, z. B. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Handelsname des Verkäufers |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Adresszeile 1 des Verkäufers |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Stadt / Ort des Verkäufers |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | PIN-Code des Verkäufers |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Staatscode des Verkäufers (2 Stellen) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Rechtlicher Name des Käufers |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | Käufer-GSTIN |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Handelsname des Käufers |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Adresszeile 1 des Käufers |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Stadt / Ort des Käufers |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | PIN-Code des Käufers |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Staatscode des Käufers |
| `irn` | `Irn` | Rechnungsreferenznummer (64-Zeichen-SHA-256-Hash) |
| `ack_number` | `AckNo` | IRP-Bestätigungsnummer |
| `ack_date` | `AckDt` | IRP-Bestätigungsdatum |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `Invoice/ItemList/Item`

| Spalte | XML-Quellelement | Anmerkungen |
|---|---|---|
| `POSITION` | `SlNo` | Zeilenfolgenummer |
| `DESCRIPTION` | `PrdDesc` | Produkt- / Dienstleistungsbeschreibung |
| `QUANTITY` | `Qty` | Berechnete Menge |
| `UNIT` | `Unit` | Maßeinheit (z. B. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Einzelpreis |
| `VAT_RATE` | `GstRt` | GST-Satz in % (z. B. 18 %) |
| `VAT` | `IgstAmt` (oder `CgstAmt` + `SgstAmt`) | GST-Betrag pro Zeile |
| `NET_AMOUNT` | `AssAmt` | Bemessungsgrundlage pro Zeile |

## Klassifizierungsregel

DocBits erkennt Indien GST E-Rechnungsdokumente anhand des Wurzelelements:

| Elektronischer Dokumenttyp | Muster |
|---------------------------|--------|
| INDIA GST E-INVOICE | Wurzelelement enthält `<SignedInvoice` |

## Verwandte Themen

- [Derzeit unterstützte E-Invoice-Standards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
