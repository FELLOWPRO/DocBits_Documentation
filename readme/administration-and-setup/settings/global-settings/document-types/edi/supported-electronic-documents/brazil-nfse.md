---
description: Unterstützung für das elektronische Dokument BRAZIL NFS-E in DocBits
---

# 🇧🇷 BRAZIL NFS-E

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Brasilien |
| **Dokumenttypen** | Dienstleistungsrechnung (Nota Fiscal de Serviços Eletrônica) |
| **Format** | XML |
| **Standard** | NFS-e 2.04 (ABRASF-Nationalstandard für kommunale Dienstleistungsrechnungen) |
| **Locale** | `pt_BR` |

NFS-e (Nota Fiscal de Serviços Eletrônica) ist die brasilianische elektronische Rechnung für Dienstleistungen, die auf kommunaler Ebene gemäß dem ABRASF-Standard ausgestellt wird. Die Hauptsteuer ist ISS (Imposto Sobre Serviços). Lieferant/Käufer werden als `PrestadorServico` / `TomadorServico` bezeichnet. Die Dienstleistungsbeschreibung befindet sich im Element `Discriminacao`.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="brazil-nfse-preview.png" alt="Brazil NFS-e Vorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für ein BRAZIL NFS-E Dokument</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XPath | Hinweise |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | NFS-e-Nummer |
| `invoice_date` | `//*[local-name()='DataEmissao']` | ISO 8601 Ausstellungsdatum |
| `currency` | Fest: `BRL` | Immer Brasilianischer Real |
| `total_amount` | `//*[local-name()='ValorServicos']` | Brutto-Dienstleistungswert |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Nettowert nach Abzügen |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (kommunale Dienstleistungssteuer) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Name des Dienstleisters |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | CNPJ des Dienstleisters |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Name des Dienstleistungsnehmers |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | CNPJ des Dienstleistungsnehmers |

> NFS-e beschreibt eine einzelne Dienstleistung im Element `Discriminacao`. Es wird keine `INVOICE_TABLE` extrahiert.

## Klassifizierungsregel
DocBits erkennt BRAZIL NFS-E über `http://www.abrasf.org.br/nfse.xsd` im XML-Namensraum.

## Verwandte Dokumente
- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Unterstützte elektronische Dokumente](./)
