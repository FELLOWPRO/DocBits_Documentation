---
description: Obsługa dokumentów elektronicznych FACTURX 1.09 - ZUGFERD 2.5 w DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Francja](countries/france.md). Znacznik XML 1p0 i Factur-X XMP Version 1.0 nie określają wydania publikacji. Zachowaj ogólne oznaczenie, gdy wydanie jest nieznane.
{% endhint %}

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Francja / Niemcy |
| **Typy dokumentów** | Faktura, nota kredytowa |
| **Format** | CII (osadzony w PDF/A-3) |
| **Standard** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Oparty na** | EN 16931 |

Factur-X 1.09 to francuska publikacja odpowiadająca ZUGFeRD 2.5 (wspólna publikacja FeRD/FNFE-MPE, czerwiec 2026). Jej XML CII wykorzystuje bazę UN/CEFACT D22B, która jest wstecznie kompatybilna z D16B, dlatego nadal obowiązuje pełny kontrakt ekstrakcji i transformacji Factur-X 1.08 / ZUGFeRD 2.4. Profil EXTENDED dodaje nowe pola dla środków płatności i BIC, odbiorcy płatności będącego stroną trzecią (faktor) oraz przyczyny zwolnienia z podatku dla rabatów i opłat.

Obsługiwanych jest wszystkie pięć profili: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) i EXTENDED.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Powiązane

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Konfiguracja ZUGFeRD](../zugferd/configuration.md)
- [Mapowanie pól ZUGFeRD](../zugferd/README.md)
- [Obsługiwane dokumenty elektroniczne](./)
