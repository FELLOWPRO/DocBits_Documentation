---
description: Obsługa dokumentu elektronicznego ZUGFERD 2.5 w DocBits
---

# 🇩🇪 ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Niemcy](countries/germany.md). Składnia, wersja publikacji i profil to różne wybory. Nie wnioskuj o publikacji Factur-X na podstawie wspólnego znacznika 1p0.
{% endhint %}

| Właściwość | Wartość |
|----------|-------|
| **Kraj/Region** | Niemcy |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | CII (osadzony w PDF/A-3) lub XML UBL |
| **Standard** | ZUGFeRD 2.5 |
| **Oparty na** | EN 16931 |

ZUGFeRD 2.5 (wspólna publikacja FeRD/FNFE-MPE z czerwca 2026 r.) odpowiada Factur-X 1.09. Jego XML CII wykorzystuje bazę UN/CEFACT D22B, która jest wstecznie zgodna z D16B, dlatego pełny kontrakt ekstrakcji i transformacji ZUGFeRD 2.4 nadal obowiązuje. Profil EXTENDED dodaje nowe pola dla środków płatniczych i BIC, strony trzeciej będącej odbiorcą płatności (faktor) oraz powodu zwolnienia z podatku dla opustów/opłat.

Obsługiwanych jest wszystkie pięć profili: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) i EXTENDED. DocBits klasyfikuje warianty CII i UBL osobno.

## Stan wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Powiązane

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Konfiguracja ZUGFeRD](../zugferd/configuration.md)
- [Mapowanie pól ZUGFeRD](../zugferd/README.md)
- [Obsługiwane dokumenty elektroniczne](./)
