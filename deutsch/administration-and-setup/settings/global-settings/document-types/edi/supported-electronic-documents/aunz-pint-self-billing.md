---
description: Unterstützung für elektronisches Dokument AUNZ PINT SELF-BILLING in DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Eigenschaft | Wert |
|----------|-------|
| **Land/Regio** | Australien / Neuseeland |
| **Dokumenttypen** | Self-Billed-Rechnung |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing ist die Self-Billing-Variante des A-NZ Peppol International Rechnungsmodells. In Self-Billing-Szenarien erstellt der Käufer die Rechnung im Namen des Lieferanten. Dieser Dokumenttyp folgt der gleichen PINT A-NZ-Struktur, jedoch mit vertauschten Parteienrollen — die `AccountingCustomerParty` wird zur Rechnungssteller-Partei und die `AccountingSupplierParty` ist die berechnete Partei.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="aunz-pint-preview.png" alt="AUNZ PINT Self-Billing Rechnungsvorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für eine AUNZ PINT Self-Billing-Rechnung</p></figcaption></figure>

## Feldzuordnung

Die Feldzuordnung ist identisch mit [AUNZ PINT](aunz-pint.md) mit folgendem wesentlichen Unterschied:

- **Parteienrollen sind vertauscht**: Beim Self-Billing ist der Käufer der Rechnungssteller und der Lieferant ist die berechnete Partei
- Die `CustomizationID` enthält `urn:peppol.org:pint:selfbilling-1@aunz` anstelle von `billing-1@aunz`

Für die vollständige Feldzuordnungstabelle siehe [AUNZ PINT](aunz-pint.md#feldzuordnung).

## Klassifikationsregel

DocBits erkennt Self-Billing-Dokumente durch Abgleich der `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Sowohl Self-Billing- als auch reguläre Abrechnungsmuster werden unter dem elektronischen Dokumenttyp `PINT A-NZ` klassifiziert.

## Verwandt

- [AUNZ PINT](aunz-pint.md)
- [Unterstützte elektronische Dokumente](./)