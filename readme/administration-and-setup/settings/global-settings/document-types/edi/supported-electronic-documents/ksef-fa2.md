---
description: Obsługa dokumentu elektronicznego KSEF FA2 w DocBits
---

# 🇵🇱 KSEF FA2

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Polska](countries/poland.md). FA2 i FA3 mają różne struktury. Potwierdź schemat źródłowy i przetestuj właściwe mapowanie; parsowanie nie przesyła faktury do KSeF.
{% endhint %}

| Właściwość           | Wartość                         |
| -------------------- | ------------------------------- |
| **Kraj / Region**    | Polska                          |
| **Typy dokumentów**  | Faktura, Faktura korygująca     |
| **Format**           | XML                             |
| **Standard**         | KSeF FA(2)                      |

KSeF FA2 to druga wersja schematu Krajowego Systemu e-Faktur. Definiuje strukturę XML faktur ustrukturyzowanych, w tym dane sprzedawcy i nabywcy, pozycje, stawki VAT oraz warunki płatności, zgodnie z wymogami polskiego prawa podatkowego.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Podgląd faktury KSeF FA(2) w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury KSeF FA(2) z Polski</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
