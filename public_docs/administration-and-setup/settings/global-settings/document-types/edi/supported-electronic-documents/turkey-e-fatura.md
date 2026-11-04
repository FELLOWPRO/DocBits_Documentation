---
description: Obsługa dokumentu elektronicznego TURKEY E-FATURA w DocBits
---

# 🇹🇷 TURKEY E-FATURA

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Turcja](countries/turkey.md). Sprawdź profil źródłowy i strukturę dokumentu. Oznaczenie rodziny nie określa każdego wydania UBL-TR ani nie potwierdza dostarczenia przez platformę podatkową.
{% endhint %}

| Właściwość | Wartość |
| ---------- | ------- |
| **Kraj/Region** | Turcja |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | UBL-TR 1.2 XML |
| **Standard** | e-Fatura (GİB - Revenue Administration) |

Turkey e-Fatura to podstawowy standard faktury elektronicznej wymagany przez GİB (Revenue Administration) w transakcjach B2B między zarejestrowanymi podatnikami. Faktury są wymieniane za pośrednictwem zarejestrowanych integratorów i platformy GİB. Format wykorzystuje UBL-TR, czyli zlokalizowaną turecką wersję UBL, z tureckimi polami do identyfikacji podatkowej TCKN/VKN.

## Stan wsparcia

| Komponent | Status |
| --------- | ------ |
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/turkey-e-fatura-preview.png" alt="Podgląd faktury Turkey E-Fatura w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Turkey E-Fatura</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
* [TURKEY E-ARSIV](turkey-e-arsiv.md)
