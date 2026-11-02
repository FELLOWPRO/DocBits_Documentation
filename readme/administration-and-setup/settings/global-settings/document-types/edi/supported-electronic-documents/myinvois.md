---
description: Obsługa dokumentu elektronicznego MYINVOIS w DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Malezja](countries/malaysia.md). Sprawdzona ścieżka ekstrakcji opiera się na XML. Platforma krajowa przyjmuje też JSON, ale nie potwierdza to obsługi importu JSON w tym mapowaniu DocBits.
{% endhint %}

| Właściwość           | Wartość                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| **Kraj / Region**    | Malezja                                                                  |
| **Typy dokumentów**  | Faktura, Nota kredytowa, Nota debetowa, Faktura wystawiona przez nabywcę |
| **Format**           | UBL 2.1 XML                                                       |
| **Standard**         | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)                             |

MyInvois to malezyjski system e-fakturowania prowadzony przez Urząd Skarbowy (LHDN). Obowiązuje od sierpnia 2024 roku dla dużych przedsiębiorstw i wymaga przesyłania wszystkich faktur do portalu MyInvois w celu walidacji oraz nadania unikalnego identyfikatora. System wykorzystuje UBL 2.1 i obsługuje zarówno format XML, jak i JSON.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="Podgląd faktury MyInvois w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury MyInvois z Malezji</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
