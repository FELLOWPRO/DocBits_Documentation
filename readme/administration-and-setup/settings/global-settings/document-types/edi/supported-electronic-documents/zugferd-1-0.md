---
description: Obsługa dokumentu elektronicznego ZUGFERD 1.0 w DocBits
---

# 🇩🇪 ZUGFERD 1.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Niemcy](countries/germany.md). Składnia, wersja publikacji i profil to różne wybory. Nie wnioskuj o publikacji Factur-X na podstawie wspólnego znacznika 1p0.
{% endhint %}

| Właściwość           | Wartość                   |
| -------------------- | ------------------------- |
| **Kraj/Region**      | Niemcy                    |
| **Typy dokumentów**  | Faktura, Nota kredytowa   |
| **Format**           | CII (osadzony w PDF/A-3)  |
| **Standard**         | ZUGFeRD 1.0               |
| **Oparty na**        | Specyfikacja ZUGFeRD 1.0  |

ZUGFeRD 1.0 był pierwotnym niemieckim standardem faktur hybrydowych, wydanym w 2014 roku. Osadza plik XML CII (ZUGFeRD-invoice.xml) w dokumencie PDF/A-3. Ta wersja powstała przed europejską normą EN 16931 i korzysta z własnego systemu profili.

## Stan wsparcia

| Komponent        | Status        |
| ---------------- | ------------- |
| Podgląd          | ✅ Obsługiwany |
| Ekstrakcja pól   | ✅ Obsługiwany |
| Transformacja    | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="Podgląd faktury ZUGFeRD 1.0 w DocBits"><figcaption><p>Domyślny podgląd DocBits dla niemieckiej faktury ZUGFeRD 1.0</p></figcaption></figure>

## Powiązane

* [Konfiguracja ZUGFeRD](../zugferd/)
* [Mapowanie pól ZUGFeRD](../zugferd/README.md)
* [Obsługiwane dokumenty elektroniczne](./)
