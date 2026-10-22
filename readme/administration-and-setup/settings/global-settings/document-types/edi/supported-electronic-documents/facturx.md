---
description: Obsługa dokumentów elektronicznych FACTURX w DocBits
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Francja](countries/france.md). Znacznik XML 1p0 i Factur-X XMP Version 1.0 nie określają wydania publikacji. Zachowaj ogólne oznaczenie, gdy wydanie jest nieznane.
{% endhint %}

| Właściwość           | Wartość                  |
| -------------------- | ------------------------ |
| **Kraj / Region**    | Francja / Niemcy         |
| **Typy dokumentów**  | Faktura, nota kredytowa  |
| **Format**           | CII (osadzony w PDF/A-3) |
| **Standard**         | Factur-X                 |
| **Oparty na**        | EN 16931                 |

Zharmonizowany CII Guideline ID może identyfikować rodzinę i profil, mimo że kilka wydań używa tego samego znacznika 1p0. Factur-X XMP Version 1.0 jest znacznikiem schematu, a nie publikacją taką jak 1.08 czy 1.09. ZUGFeRD XMP może deklarować swoją wersję. Gdy brakuje miarodajnych metadanych, zachowaj ogólny wynik rozpoznania rodziny i potwierdź oryginalny plik z nadawcą.

## Status obsługi

| Komponent        | Status         |
| ---------------- | -------------- |
| Podgląd          | ✅ Obsługiwane |
| Ekstrakcja pól   | ✅ Obsługiwane |
| Transformacja    | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Podgląd faktury Factur-X w DocBits"><figcaption><p>Domyślny podgląd DocBits dla francuskiej faktury Factur-X</p></figcaption></figure>

## Powiązane

* [Konfiguracja ZUGFeRD](../zugferd/)
* [Mapowanie pól ZUGFeRD](../zugferd/README.md)
* [Obsługiwane dokumenty elektroniczne](./)
