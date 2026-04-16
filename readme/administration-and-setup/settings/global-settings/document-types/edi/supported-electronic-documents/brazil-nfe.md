---
description: Unterstützung für das elektronische Dokument BRAZIL NF-E in DocBits
---

# 🇧🇷 BRAZIL NF-E

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Brasilien |
| **Dokumenttypen** | Rechnung (Nota Fiscal Eletrônica) |
| **Format** | XML |
| **Standard** | NF-e 4.0 (Nota Fiscal Eletrônica — Waren & zwischenstaatlicher Handel) |
| **Locale** | `pt_BR` |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) ist die brasilianische elektronische Rechnung für Waren und den zwischenstaatlichen Handel, reguliert durch SEFAZ. Jede NF-e enthält einen eindeutigen 44-stelligen Zugriffsschlüssel (`chNFe`), detaillierte Produktpositionen und mehrstufige Steuerdaten (ICMS, IPI, PIS, COFINS). DocBits klassifiziert NF-e durch Erkennung des Namensraums `http://www.portalfiscal.inf.br/nfe`.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="brazil-nfe-preview.png" alt="Brazil NF-e Vorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für ein BRAZIL NF-E Dokument</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XPath | Hinweise |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota-Fiscal-Nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 mit BRT-Offset |
| `currency` | Fest: `BRL` | Immer Brasilianischer Real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Gesamtwert der NF-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Gesamtwert der Produkte |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS-Steuergesamtbetrag |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Name des ausstellenden Unternehmens |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` oder `CPF` | CNPJ (14 Stellen) oder CPF (11 Stellen) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Name des empfangenden Unternehmens |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` oder `CPF` | CNPJ oder CPF |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `//*[local-name()='det']`

| Spalte | Relativer XPath | Hinweise |
|---|---|---|
| `POSITION` | `@nItem` | Positionsfolgenummer |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Produktcode |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Produktbeschreibung |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | NCM-Zollklassifizierung |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Fiskalischer Vorgangscode |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Maßeinheit |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Handelsmenge |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Einzelpreis |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Zeilensumme |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS-Steuer pro Position |
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | PIS-Steuer pro Position |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | COFINS-Steuer pro Position |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS-Satz (%) |

## Klassifizierungsregel

DocBits erkennt BRAZIL NF-E Dokumente durch Suche nach der Zeichenkette `http://www.portalfiscal.inf.br/nfe` im XML-Namensraum.

## Verwandte Dokumente
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Unterstützte elektronische Dokumente](./)
