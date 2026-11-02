---
description: Obsługa dokumentu elektronicznego KSEF w DocBits
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Polska](countries/poland.md). FA2 i FA3 mają różne struktury. Potwierdź schemat źródłowy i przetestuj właściwe mapowanie; parsowanie nie przesyła faktury do KSeF.
{% endhint %}

| Właściwość           | Wartość                                          |
| -------------------- | ------------------------------------------------ |
| **Kraj / Region**    | Polska                                           |
| **Typy dokumentów**  | Faktura, Nota kredytowa, Faktura korygująca      |
| **Format**           | XML                                              |
| **Standard**         | KSeF (Krajowy System e-Faktur)                   |

KSeF to Krajowy System e-Faktur prowadzony przez Ministerstwo Finansów. Stanie się obowiązkowy dla wszystkich polskich podatników VAT. DocBits obsługuje przetwarzanie faktur w wersjach schematu KSeF FA2 i FA3.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Podgląd faktury KSeF w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury KSeF z Polski</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
