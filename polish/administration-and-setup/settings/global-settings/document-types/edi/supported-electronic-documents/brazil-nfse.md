---
description: Obsługa dokumentów elektronicznych BRAZIL NFS-E w DocBits
---

# 🇧🇷 BRAZIL NFS-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Brazylia](countries/brazil.md). Są to różne rodziny dokumentów. Skonfigurowana wersja NFS-e nie certyfikuje każdego schematu gminnego ani każdego krajowego układu faktury za usługi.
{% endhint %}

| Właściwość           | Wartość                                                              |
| -------------------- | -------------------------------------------------------------------- |
| **Kraj / Region**    | Brazylia                                                             |
| **Typy dokumentów**  | Faktura za usługi (Nota Fiscal de Serviços Eletrônica)               |
| **Format**           | XML                                                                  |
| **Standard**         | NFS-e 2.04 (krajowy standard ABRASF dla miejskich faktur za usługi)  |
| **Język**            | `pt_BR`                                                              |

NFS-e (Nota Fiscal de Serviços Eletrônica) to brazylijska faktura elektroniczna za usługi, wystawiana na poziomie gminy. DocBits obsługuje schemat standardu ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais). Dokumenty NFS-e używają innej struktury XML niż NF-e: głównym podatkiem jest ISS (Imposto Sobre Serviços), a nie ICMS, a dostawca i nabywca nazywają się `PrestadorServico` / `TomadorServico`. Element `Discriminacao` zawiera dowolny opis usługi.

## Status obsługi

| Komponent        | Status         |
| ---------------- | -------------- |
| Podgląd          | ✅ Obsługiwane |
| Ekstrakcja pól   | ✅ Obsługiwane |
| Transformacja    | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/brazil-nfse-preview.png" alt="Podgląd Brazil NFS-e w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu BRAZIL NFS-E</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits    | Źródłowy XPath                                                        | Uwagi                              |
| --------------- | --------------------------------------------------------------------- | ---------------------------------- |
| `invoice_id`    | `//*[local-name()='Numero']`                                          | Numer NFS-e                        |
| `invoice_date`  | `//*[local-name()='DataEmissao']`                                     | Data wystawienia w ISO 8601        |
| `currency`      | Stały: `BRL`                                                          | Zawsze real brazylijski            |
| `total_amount`  | `//*[local-name()='ValorServicos']`                                   | Wartość brutto usług               |
| `net_amount`    | `//*[local-name()='ValorLiquidoNfse']`                                | Wartość netto po odliczeniach      |
| `tax_amount`    | `//*[local-name()='ValorIss']`                                        | ISS (miejski podatek od usług)     |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Nazwa usługodawcy                  |
| `supplier_id`   | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']`        | CNPJ usługodawcy                   |
| `buyer_name`    | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']`   | Nazwa usługobiorcy                 |
| `buyer_id`      | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']`          | CNPJ usługobiorcy                  |

> NFS-e opisuje pojedynczą usługę w elemencie `Discriminacao`, a nie pozycje faktury. Tabela `INVOICE_TABLE` nie jest ekstrahowana.

## Reguła klasyfikacji

DocBits wykrywa dokumenty BRAZIL NFS-E na podstawie przestrzeni nazw:

```
http://www.abrasf.org.br/nfse.xsd
```

## Powiązane

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [Obsługiwane dokumenty elektroniczne](./)
