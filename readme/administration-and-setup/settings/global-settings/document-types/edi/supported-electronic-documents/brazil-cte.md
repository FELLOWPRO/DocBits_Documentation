---
description: Unterstützung für das elektronische Dokument BRAZIL CT-E in DocBits
---

# 🇧🇷 BRAZIL CT-E

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Brasilien |
| **Dokumenttypen** | Transportrechnung (Conhecimento de Transporte Eletrônico) |
| **Format** | XML |
| **Standard** | CT-e 3.0 (elektronischer Fracht-/Transportfrachtbrief) |
| **Locale** | `pt_BR` |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) ist das brasilianische elektronische Transportdokument, das von Logistik- und Frachtunternehmen ausgestellt wird. Es dokumentiert den Transportdienst, den Frachtwert, die Herkunfts-/Zielgemeinden und den Frachtpreis (`vTPrest`). Im Gegensatz zur NF-e verwendet CT-e `cteProc` als Wurzelelement.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="brazil-cte-preview.png" alt="Brazil CT-e Vorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für ein BRAZIL CT-E Dokument</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XPath | Hinweise |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | CT-e-Nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 mit BRT-Offset |
| `currency` | Fest: `BRL` | Immer Brasilianischer Real |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Gesamtwert des Transportdienstes |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Zu empfangender Betrag |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS auf Transportdienst |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Name des Frachtführers |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | CNPJ des Frachtführers |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Name des Empfängers |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | CNPJ des Empfängers |

> CT-e enthält keine Positionstabelle — der Transportdienst ist eine einzelne Gebühr auf Dokumentebene.

## Klassifizierungsregel
DocBits erkennt BRAZIL CT-E über `http://www.portalfiscal.inf.br/cte` im XML-Namensraum.

## Verwandte Dokumente
- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Unterstützte elektronische Dokumente](./)
