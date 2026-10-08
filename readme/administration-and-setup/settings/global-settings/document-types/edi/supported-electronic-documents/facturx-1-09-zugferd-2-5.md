---
description: Obsługa dokumentu elektronicznego FACTURX 1.09 - ZUGFERD 2.5 w DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Francja / Niemcy |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | CII (osadzony PDF/A-3) |
| **Standard** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Na podstawie** | EN 16931 |

Factur-X 1.09 to francuskie wydanie równoważne ZUGFeRD 2.5 (wspólne wydanie FeRD/FNFE-MPE, czerwiec 2026). Jego XML CII korzysta z bazy UN/CEFACT D22B, zgodnej wstecz z D16B, więc pełny kontrakt ekstrakcji i transformacji Factur-X 1.08 / ZUGFeRD 2.4 pozostaje aktualny. Profil EXTENDED dodaje nowe pola dotyczące środków płatności i kodu BIC, odbiorcę trzeciego (faktora) oraz przyczynę zwolnienia podatkowego dla opustów/narzutów.

Wszystkie pięć profili jest obsługiwanych: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) i EXTENDED.

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
