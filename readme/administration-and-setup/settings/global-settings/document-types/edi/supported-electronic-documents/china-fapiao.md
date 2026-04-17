---
description: Unterstützung für CHINA FAPIAO elektronische Dokumente in DocBits
---

# 🇨🇳 CHINA FAPIAO

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | China |
| **Dokumenttypen** | Allgemeine Mehrwertsteuerrechnung, Spezielle Mehrwertsteuerrechnung, E-Fapiao |
| **Format** | XML |
| **Standard** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |
| **XML-Namespace** | `urn:china:tax:fapiao:1.0` |

Fapiao (发票) ist das chinesische System für elektronische Steuerrechnungen, das von der State Taxation Administration (国家税务总局) reguliert wird. Alle Fapiao-Dokumente teilen den XML-Namespace `urn:china:tax:fapiao:1.0`. DocBits erkennt automatisch den Fapiao-Typ und leitet zu den entsprechenden Extraktionsregeln weiter:

| Fapiao-Typ | Code | Beschreibung |
|-----------|------|-------------|
| 普通发票 | General VAT Invoice | Allgemeine Mehrwertsteuerrechnung (普通发票) |
| 专用发票 | Special VAT Invoice | Spezielle Mehrwertsteuerrechnung (专用发票) — abzugsfähig |

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="china-fapiao-preview.png" alt="Vorschau einer China Fapiao-Rechnung in DocBits"><figcaption><p>Standard DocBits-Vorschau für eine CHINA GENERAL VAT INVOICE (普通发票)</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | XML-Quellelement | Hinweise |
|---|---|---|
| `invoice_id` | `fapiao_number` | Rechnungsnummer (8 Ziffern) |
| `invoice_code` | `fapiao_code` | Rechnungscode (10-12 Ziffern) |
| `invoice_date` | `issue_date` | Ausstellungsdatum ISO 8601 |
| `fapiao_type` | `fapiao_type` | Typ: 普通发票 oder 专用发票 |
| `check_code` | `check_code` | Prüfcode (20 Ziffern) |
| `machine_code` | `machine_code` | Steuermaschinennummer |
| `currency` | Fest: `CNY` | Immer chinesischer Yuan |
| `total_amount` | `total_with_tax` | Gesamtbetrag inkl. MwSt (价税合计) |
| `net_amount` | `total_amount` | Nettobetrag (金额) |
| `tax_amount` | `total_tax` | Mehrwertsteuerbetrag (税额) |
| `amount_in_words` | `amount_in_words` | Betrag in chinesischen Zeichen (大写) |
| `supplier_name` | `seller/name` | Name des ausstellenden Unternehmens (销售方) |
| `supplier_id` | `seller/taxpayer_id` | Steuer-ID des Ausstellers (18 Zeichen) |
| `supplier_address` | `seller/address` | Adresse des Ausstellers |
| `supplier_telephone` | `seller/telephone` | Telefon des Ausstellers |
| `supplier_bank_name` | `seller/bank_name` | Bank des Ausstellers |
| `supplier_bank_account` | `seller/bank_account` | Bankkonto des Ausstellers |
| `buyer_name` | `buyer/name` | Name des Empfängerunternehmens (购买方) |
| `buyer_id` | `buyer/taxpayer_id` | Steuer-ID des Empfängers |
| `buyer_address` | `buyer/address` | Adresse des Empfängers |
| `buyer_telephone` | `buyer/telephone` | Telefon des Empfängers |
| `remarks` | `remarks` | Anmerkungen (备注) |
| `issuer` | `issuer` | Aussteller (开票人) |
| `tax_authority` | `tax_authority` | Steuerbehörde (税务机关) |

### Positionstabelle (`INVOICE_TABLE`)

Positionspfad: `items/item`

| Spalte | XML-Quellelement | Hinweise |
|---|---|---|
| `SEQ` | `seq` | Positionsnummer |
| `ITEM_NAME` | `name` | Artikelbezeichnung |
| `SPEC` | `spec` | Spezifikation / Modell |
| `UNIT` | `unit` | Maßeinheit |
| `QUANTITY` | `quantity` | Menge |
| `UNIT_PRICE` | `unit_price` | Einzelpreis netto |
| `AMOUNT` | `amount` | Positionsgesamt netto |
| `TAX_RATE` | `tax_rate` | MwSt-Satz in % (13% oder 9%) |
| `TAX_AMOUNT` | `tax_amount` | MwSt pro Position |

## Klassifikationsregeln

DocBits erkennt China Fapiao-Dokumente durch Abgleich des XML-Namespace und des Fapiao-Typs:

| Elektronischer Dokumenttyp | Muster |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0" version="1.0">` |
| CHINA SPECIAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0"` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA FAPIAO | `<fapiao` (generische Übereinstimmung) |
| CHINA FAPIAO | `税务总局` (Textübereinstimmung) |
| CHINA VAT INVOICE | `<VATInvoice` (Legacy-Format) |

Die Klassifikation verwendet das Prinzip **FIRST MATCH WINS**, sortiert nach Musterlänge (längste zuerst). Das Wurzelelement ist `<fapiao>` mit dem Namespace `urn:china:tax:fapiao:1.0`.

## Siehe auch

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
