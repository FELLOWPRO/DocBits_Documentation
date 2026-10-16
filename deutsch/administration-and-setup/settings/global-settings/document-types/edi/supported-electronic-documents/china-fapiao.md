---
description: Unterstützung für China Fapiao (FAPIAO, E-FAPIAO, Allgemeine Mehrwertsteuerrechnung, Spezielle Mehrwertsteuerrechnung) elektronische Dokumente in DocBits
---

# 🇨🇳 China Fapiao

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | China |
| **Dokumenttypen** | General VAT Invoice (普通发票), Special VAT Invoice (专用发票), E-Fapiao |
| **Format** | XML |
| **Standard** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |

Fapiao (发票) ist der chinesische Steuerrechnungsstandard, der unter der Aufsicht der State Taxation Administration (STA / 国家税务总局) ausgestellt wird. Alle Fapiao-Dokumente teilen den Namespace `urn:china:tax:fapiao:1.0`. DocBits erkennt den Fapiao-Typ automatisch über das Element `fapiao_type` und leitet zu den entsprechenden Extraktionsregeln weiter:

| fapiao_type-Wert | Dokumenttyp |
|-------------------|--------------|
| 普通发票 | General VAT Invoice (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Special VAT Invoice (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Supported |
| Feldextraktion | ✅ Supported |
| Transformation | ✅ Supported |

## Standardvorschau

<figure><img src="china-fapiao-preview.png" alt="Vorschau einer China Fapiao General VAT Invoice in DocBits"><figcaption><p>Standard DocBits-Vorschau für eine China Fapiao General VAT Invoice (普通发票)</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | XML-Quellelement | Hinweise |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Fapiao-Nummer — 8 Ziffern (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Ausstellungsdatum (ISO 8601) |
| `currency` | Fest: `CNY` | Immer Chinesischer Yuan Renminbi |
| `total_amount` | `total/total_with_tax` | Gesamtbetrag inkl. MwSt. (价税合计) |
| `net_amount` | `total/total_amount` | Nettobetrag exkl. MwSt. (金额) |
| `tax_amount` | `total/total_tax` | Gesamter MwSt.-Betrag (税额) |
| `supplier_name` | `seller/name` | Name des Verkäuferunternehmens (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | Steuernummer des Verkäufers — 18 Zeichen (纳税人识别号) |
| `supplier_address` | `seller/address` | Adresse des Verkäufers |
| `supplier_country` | Fest: `CN` | Immer China |
| `iban` | `seller/bank_account` | Bankkontonummer des Verkäufers |
| `buyer_name` | `buyer/name` | Name des Käuferunternehmens (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | Steuernummer des Käufers (纳税人识别号) |
| `buyer_address` | `buyer/address` | Adresse des Käufers |
| `buyer_country` | Fest: `CN` | Immer China |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `items/item`

| Spalte | XML-Quellelement | Hinweise |
|---|---|---|
| `POSITION` | `seq` | Positionsfolgenummer |
| `DESCRIPTION` | `name` + `spec` | Artikelbezeichnung und Spezifikation (verknüpft) |
| `QUANTITY` | `quantity` | Menge |
| `UNIT` | `unit` | Maßeinheit (z. B. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Einzelpreis exkl. MwSt. |
| `VAT_RATE` | `tax_rate` | MwSt.-Satz in % (typischerweise 6 %, 9 % oder 13 %) |
| `VAT` | `tax_amount` | MwSt.-Betrag pro Position |
| `NET_AMOUNT` | `amount` | Positionsgesamt exkl. MwSt. |

## Klassifikationsregeln

DocBits erkennt China Fapiao-Dokumente durch Abgleich des XML-Namespace und des `fapiao_type`:

| Elektronischer Dokumenttyp | Muster |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

Das Wurzelelement ist `<fapiao>` mit dem Namespace `urn:china:tax:fapiao:1.0`. Die Klassifikation verwendet das Prinzip **First-Match-Wins**, sortiert nach Musterlänge (längste zuerst).

## Siehe auch

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
