---
description: Obsługa dokumentów elektronicznych BRAZIL NFC-E w DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Właściwość           | Wartość                                                 |
| -------------------- | ------------------------------------------------------- |
| **Kraj / Region**    | Brazylia                                                |
| **Typy dokumentów**  | Faktura konsumencka (Nota Fiscal de Consumidor Eletrônica) |
| **Format**           | XML                                                     |
| **Standard**         | NFC-e 4.0 (faktura konsumencka w handlu detalicznym / punkcie sprzedaży) |
| **Język**            | `pt_BR`                                                 |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) to brazylijska faktura elektroniczna dla sprzedaży detalicznej konsumentom końcowym. Korzysta ze schematu XML NF-e (przestrzeń nazw `nfeProc`), ale używa kodu modelu 65. Dokumenty NFC-e zazwyczaj zawierają dla nabywcy numer CPF (indywidualny identyfikator podatkowy) zamiast CNPJ i nie zawierają PIS/COFINS dla poszczególnych pozycji w prostych transakcjach detalicznych.

## Status obsługi

| Komponent        | Status         |
| ---------------- | -------------- |
| Podgląd          | ✅ Obsługiwane |
| Ekstrakcja pól   | ✅ Obsługiwane |
| Transformacja    | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/brazil-nfce-preview.png" alt="Podgląd Brazil NFC-e w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu BRAZIL NFC-E</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits    | Źródłowy XPath                                             | Uwagi                       |
| --------------- | ---------------------------------------------------------- | --------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Numer Nota Fiscal           |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 z przesunięciem BRT |
| `currency`      | Stały: `BRL`                                               | Zawsze real brazylijski     |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Całkowita wartość NFC-e     |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Suma częściowa produktów    |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | Suma podatku ICMS           |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Nazwa sprzedawcy detalicznego |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` lub `CPF` | CNPJ lub CPF               |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Nazwa konsumenta            |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CPF']` lub `CNPJ` | CPF (osoba fizyczna) lub CNPJ |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `//*[local-name()='det']`

| Kolumna        | Względny XPath                                                              | Uwagi                          |
| -------------- | --------------------------------------------------------------------------- | ------------------------------ |
| `POSITION`     | `@nItem`                                                                    | Numer kolejny pozycji          |
| `ITEM_CODE`    | `*[local-name()='prod']/*[local-name()='cProd']`                            | Kod produktu                   |
| `DESCRIPTION`  | `*[local-name()='prod']/*[local-name()='xProd']`                            | Opis produktu                  |
| `NCM_CODE`     | `*[local-name()='prod']/*[local-name()='NCM']`                              | Klasyfikacja celna NCM         |
| `CFOP_CODE`    | `*[local-name()='prod']/*[local-name()='CFOP']`                             | Kod fiskalny operacji          |
| `UNIT`         | `*[local-name()='prod']/*[local-name()='uCom']`                             | Jednostka miary                |
| `QUANTITY`     | `*[local-name()='prod']/*[local-name()='qCom']`                             | Ilość handlowa                 |
| `UNIT_PRICE`   | `*[local-name()='prod']/*[local-name()='vUnCom']`                           | Cena jednostkowa               |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']`                            | Suma pozycji                   |
| `ICMS_AMOUNT`  | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Podatek ICMS dla pozycji       |
| `VAT_RATE`     | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Stawka ICMS (%)                |

## Reguła klasyfikacji

DocBits wykrywa dokumenty BRAZIL NFC-E na podstawie wzorca `<mod>65</mod>` w dokumencie XML z przestrzenią nazw `http://www.portalfiscal.inf.br/nfe`.

## Powiązane

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Obsługiwane dokumenty elektroniczne](./)
