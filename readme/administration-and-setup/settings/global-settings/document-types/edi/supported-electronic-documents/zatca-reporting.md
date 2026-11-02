---
description: Obsługa dokumentu elektronicznego ZATCA REPORTING w DocBits
---

# 🇸🇦 ZATCA REPORTING

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Arabia Saudyjska](countries/saudi-arabia.md). Te oznaczenia opisują różne procesy i warianty faktur. Parsowanie nie dowodzi podpisywania, zatwierdzania ani raportowania przez ZATCA.
{% endhint %}

| Właściwość           | Wartość                               |
| -------------------- | ------------------------------------- |
| **Kraj/Region**      | Arabia Saudyjska                      |
| **Typy dokumentów**  | Faktura raportowana                   |
| **Format**           | UBL 2.1 XML                           |
| **Standard**         | ZATCA Reporting (integracja fazy 2)   |

ZATCA Reporting to tryb integracji fazy 2, w którym standardowe faktury VAT są raportowane do platformy ZATCA w ciągu 24 godzin od wystawienia. Raportowana faktura zawiera podpis kryptograficzny, kod QR oraz identyfikator UUID nadany przez portal Fatoorah organu ZATCA.

## Stan wsparcia

| Komponent        | Status        |
| ---------------- | ------------- |
| Podgląd          | ✅ Obsługiwany |
| Ekstrakcja pól   | ✅ Obsługiwany |
| Transformacja    | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/zatca-reporting-preview.png" alt="Podgląd faktury ZATCA Reporting w DocBits"><figcaption><p>Domyślny podgląd DocBits dla saudyjskiej faktury ZATCA Reporting</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
