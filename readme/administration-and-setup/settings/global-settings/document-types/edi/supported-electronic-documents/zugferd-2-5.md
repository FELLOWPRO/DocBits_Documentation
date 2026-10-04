---
description: Obsługa dokumentu elektronicznego ZUGFERD 2.5 w DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Niemcy |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | CII (osadzony PDF/A-3) lub XML UBL |
| **Standard** | ZUGFeRD 2.5 |
| **Na podstawie** | EN 16931 |

ZUGFeRD 2.5 (wspólne wydanie FeRD/FNFE-MPE z czerwca 2026) jest odpowiednikiem Factur-X 1.09. Jego XML CII korzysta z bazy UN/CEFACT D22B, zgodnej wstecz z D16B, więc pełny kontrakt ekstrakcji i transformacji ZUGFeRD 2.4 pozostaje aktualny. Profil EXTENDED dodaje nowe pola dotyczące środków płatności i kodu BIC, odbiorcę trzeciego (faktora) oraz przyczynę zwolnienia podatkowego dla opustów/narzutów.

Wszystkie pięć profili jest obsługiwanych: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) i EXTENDED. DocBits klasyfikuje warianty CII i UBL osobno.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Powiązane

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Konfiguracja ZUGFeRD](../zugferd/configuration.md)
- [Mapowanie pól ZUGFeRD](../zugferd/README.md)
- [Obsługiwane dokumenty elektroniczne](./)
