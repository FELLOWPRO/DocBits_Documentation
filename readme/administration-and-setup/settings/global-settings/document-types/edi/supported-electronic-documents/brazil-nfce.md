---
description: Obsługa elektronicznego dokumentu BRAZIL NFC-E w DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Właściwość | Wartość |
|------------|---------|
| **Kraj / Region** | Brazylia |
| **Typy dokumentów** | Faktura konsumencka (Nota Fiscal de Consumidor Eletrônica) |
| **Format** | XML |
| **Standard** | NFC-e 4.0 (detaliczna faktura dla konsumenta końcowego) |
| **Locale** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) jest brazylijską e-fakturą dla sprzedaży detalicznej konsumentom końcowym. Używa tej samej przestrzeni nazw co NF-e (`http://www.portalfiscal.inf.br/nfe`), lecz z kodem modelu 65. Nabywca w NFC-e posiada zazwyczaj numer CPF (indywidualny identyfikator podatkowy) zamiast CNPJ. W przypadku prostych transakcji detalicznych pozycje nie zawierają podatków PIS/COFINS.

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="brazil-nfce-preview.png" alt="Podgląd Brazil NFC-e w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu BRAZIL NFC-E</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy XPath | Uwagi |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Numer Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 z przesunięciem BRT |
| `currency` | Stałe: `BRL` | Zawsze brazylijski real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Łączna wartość NFC-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Suma częściowa produktów |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Łączna kwota podatku ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nazwa sprzedawcy detalicznego |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` lub `CPF` | CNPJ lub CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Imię i nazwisko konsumenta |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` lub `CNPJ` | CPF (osoba fizyczna) lub CNPJ |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `//*[local-name()='det']`

| Kolumna | Względny XPath | Uwagi |
|---|---|---|
| `POSITION` | `@nItem` | Numer sekwencyjny pozycji |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Kod produktu |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Opis produktu |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | Klasyfikacja celna NCM |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Fiskalny kod operacji |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Jednostka miary |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Ilość handlowa |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Cena jednostkowa |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Suma wiersza |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Podatek ICMS na pozycję |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Stawka ICMS (%) |

> NFC-e nie zawiera podatków PIS/COFINS na poziomie pozycji w przypadku prostych transakcji detalicznych.

## Reguła klasyfikacji

DocBits wykrywa dokumenty BRAZIL NFC-E poprzez wzorzec `<mod>65</mod>` wewnątrz przestrzeni nazw `http://www.portalfiscal.inf.br/nfe` w pliku XML.

## Powiązane dokumenty

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Obsługiwane dokumenty elektroniczne](./)
