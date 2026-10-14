---
description: Unterstützung für das elektronische Dokument BRAZIL NFC-E in DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Brasilien |
| **Dokumenttypen** | Verbraucherrechnung (Nota Fiscal de Consumidor Eletrônica) |
| **Format** | XML |
| **Standard** | NFC-e 4.0 (Einzelhandels-/Point-of-Sale-Verbraucherrechnung) |
| **Locale** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) ist die brasilianische elektronische Rechnung für Einzelhandelsverkäufe an Endverbraucher. Sie teilt das NF-e XML-Schema, verwendet jedoch den Modellcode 65. NFC-e Dokumente enthalten in der Regel eine CPF (individuelle Steuernummer) für den Käufer anstelle einer CNPJ.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="brazil-nfce-preview.png" alt="Brazil NFC-e Vorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für ein BRAZIL NFC-E Dokument</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XPath | Hinweise |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota-Fiscal-Nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 mit BRT-Offset |
| `currency` | Fest: `BRL` | Immer Brasilianischer Real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Gesamtwert der NFC-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Zwischensumme der Produkte |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS-Steuergesamtbetrag |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Name des Einzelhändlers |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` oder `CPF` | CNPJ oder CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Name des Verbrauchers |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` oder `CNPJ` | CPF (Einzelperson) oder CNPJ |

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
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS-Satz (%) |

## Klassifizierungsregel
DocBits erkennt BRAZIL NFC-E über `<mod>65</mod>` innerhalb des Namensraums `http://www.portalfiscal.inf.br/nfe`.

## Verwandte Dokumente
- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Unterstützte elektronische Dokumente](./)
