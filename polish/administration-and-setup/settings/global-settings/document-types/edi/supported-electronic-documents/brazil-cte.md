---
description: Obsługa dokumentów elektronicznych BRAZIL CT-E w DocBits
---

# 🇧🇷 BRAZIL CT-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Brazylia](countries/brazil.md). Są to różne rodziny dokumentów. Skonfigurowana wersja NFS-e nie certyfikuje każdego schematu gminnego ani każdego krajowego układu faktury za usługi.
{% endhint %}

| Właściwość           | Wartość                                                   |
| -------------------- | --------------------------------------------------------- |
| **Kraj / Region**    | Brazylia                                                  |
| **Typy dokumentów**  | Faktura transportowa (Conhecimento de Transporte Eletrônico) |
| **Format**           | XML                                                       |
| **Standard**         | CT-e 3.0 (elektroniczny list przewozowy dla frachtu/transportu) |
| **Język**            | `pt_BR`                                                   |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) to brazylijski elektroniczny dokument transportowy wystawiany przez firmy logistyczne i spedycyjne. Dokumentuje usługę transportową, wartość ładunku, gminy początkową i docelową (`cMunIni` / `cMunFim`) oraz cenę frachtu (`vTPrest`). W przeciwieństwie do NF-e, CT-e używa `cteProc` jako elementu głównego i odwołuje się do powiązanych dokumentów NF-e.

## Status obsługi

| Komponent        | Status         |
| ---------------- | -------------- |
| Podgląd          | ✅ Obsługiwane |
| Ekstrakcja pól   | ✅ Obsługiwane |
| Transformacja    | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/brazil-cte-preview.png" alt="Podgląd Brazil CT-e w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu BRAZIL CT-E</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits    | Źródłowy XPath                                         | Uwagi                              |
| --------------- | ------------------------------------------------------ | ---------------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nCT']`        | Numer CT-e                         |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`      | ISO 8601 z przesunięciem BRT       |
| `currency`      | Stały: `BRL`                                           | Zawsze real brazylijski            |
| `total_amount`  | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Całkowita wartość usługi frachtowej |
| `net_amount`    | `//*[local-name()='vPrest']/*[local-name()='vRec']`    | Kwota do otrzymania                |
| `tax_amount`    | `//*[local-name()='ICMS']//*[local-name()='vICMS']`    | ICMS od usługi transportowej       |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`     | Nazwa przewoźnika (transportadora) |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']`      | CNPJ przewoźnika                   |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`     | Nazwa odbiorcy (destinatário)      |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CNPJ']`      | CNPJ odbiorcy                      |

> CT-e nie zawiera tabeli pozycji — usługa transportowa jest pojedynczą opłatą na poziomie dokumentu.

## Reguła klasyfikacji

DocBits wykrywa dokumenty BRAZIL CT-E na podstawie:

```
http://www.portalfiscal.inf.br/cte
```

w przestrzeni nazw XML (element główny `<cteProc>`).

## Powiązane

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Obsługiwane dokumenty elektroniczne](./)
