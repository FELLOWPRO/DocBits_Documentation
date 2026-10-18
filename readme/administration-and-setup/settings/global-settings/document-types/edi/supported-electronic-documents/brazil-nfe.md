---
description: Obsługa dokumentów elektronicznych BRAZIL NF-E w DocBits
---

# 🇧🇷 BRAZIL NF-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Brazylia](countries/brazil.md). Są to różne rodziny dokumentów. Skonfigurowana wersja NFS-e nie certyfikuje każdego schematu gminnego ani każdego krajowego układu faktury za usługi.
{% endhint %}

| Właściwość           | Wartość                                                         |
| -------------------- | --------------------------------------------------------------- |
| **Kraj / Region**    | Brazylia                                                        |
| **Typy dokumentów**  | Faktura (Nota Fiscal Eletrônica)                                |
| **Format**           | XML                                                             |
| **Standard**         | NF-e 4.0 (Nota Fiscal Eletrônica — towary i handel międzystanowy) |
| **Język**            | `pt_BR`                                                         |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) to brazylijska faktura elektroniczna dla towarów i handlu międzystanowego, regulowana przez SEFAZ. Każda NF-e zawiera unikalny 44-cyfrowy klucz dostępu (`chNFe`), szczegółowe pozycje produktów oraz wielopoziomowe dane podatkowe (ICMS, IPI, PIS, COFINS). DocBits klasyfikuje NF-e, wykrywając przestrzeń nazw `http://www.portalfiscal.inf.br/nfe`.

## Status obsługi

| Komponent        | Status         |
| ---------------- | -------------- |
| Podgląd          | ✅ Obsługiwane |
| Ekstrakcja pól   | ✅ Obsługiwane |
| Transformacja    | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Podgląd Brazil NF-e w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu BRAZIL NF-E</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits    | Źródłowy XPath                                             | Uwagi                                 |
| --------------- | ---------------------------------------------------------- | ------------------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Numer Nota Fiscal                     |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 z przesunięciem BRT          |
| `currency`      | Stały: `BRL`                                               | Zawsze real brazylijski               |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Całkowita wartość NF-e                |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Całkowita wartość produktów           |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | Suma podatku ICMS                     |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Nazwa firmy wystawcy                  |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` lub `CPF` | CNPJ (14 cyfr) lub CPF (11 cyfr)     |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Nazwa firmy odbiorcy                  |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CNPJ']` lub `CPF` | CNPJ lub CPF                         |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `//*[local-name()='det']`

| Kolumna         | Względny XPath                                                                  | Uwagi                          |
| --------------- | ------------------------------------------------------------------------------- | ------------------------------ |
| `POSITION`      | `@nItem`                                                                        | Numer kolejny pozycji          |
| `ITEM_CODE`     | `*[local-name()='prod']/*[local-name()='cProd']`                                | Kod produktu                   |
| `DESCRIPTION`   | `*[local-name()='prod']/*[local-name()='xProd']`                                | Opis produktu                  |
| `NCM_CODE`      | `*[local-name()='prod']/*[local-name()='NCM']`                                  | Klasyfikacja celna NCM         |
| `CFOP_CODE`     | `*[local-name()='prod']/*[local-name()='CFOP']`                                 | Kod fiskalny operacji          |
| `UNIT`          | `*[local-name()='prod']/*[local-name()='uCom']`                                 | Jednostka miary                |
| `QUANTITY`      | `*[local-name()='prod']/*[local-name()='qCom']`                                 | Ilość handlowa                 |
| `UNIT_PRICE`    | `*[local-name()='prod']/*[local-name()='vUnCom']`                               | Cena jednostkowa               |
| `TOTAL_AMOUNT`  | `*[local-name()='prod']/*[local-name()='vProd']`                                | Suma pozycji                   |
| `ICMS_AMOUNT`   | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']`     | Podatek ICMS dla pozycji       |
| `PIS_AMOUNT`    | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']`       | Podatek PIS dla pozycji        |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Podatek COFINS dla pozycji     |
| `VAT_RATE`      | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']`     | Stawka ICMS (%)                |

## Reguła klasyfikacji

DocBits wykrywa dokumenty BRAZIL NF-E, sprawdzając obecność ciągu:

```
http://www.portalfiscal.inf.br/nfe
```

w przestrzeni nazw XML (`mod=55` dla NF-e i `mod=65` dla NFC-e są rozróżniane osobno).

## Powiązane

* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Obsługiwane dokumenty elektroniczne](./)
