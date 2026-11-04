---
description: Obsługa dokumentu elektronicznego ZATCA SIMPLIFIED w DocBits
---

# 🇸🇦 ZATCA SIMPLIFIED

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Arabia Saudyjska](countries/saudi-arabia.md). Te oznaczenia opisują różne procesy i warianty faktur. Parsowanie nie dowodzi podpisywania, zatwierdzania ani raportowania przez ZATCA.
{% endhint %}

| Właściwość           | Wartość                      |
| -------------------- | ---------------------------- |
| **Kraj/Region**      | Arabia Saudyjska             |
| **Typy dokumentów**  | Uproszczona faktura VAT      |
| **Format**           | UBL 2.1 XML                  |
| **Standard**         | ZATCA Simplified Tax Invoice |

ZATCA Simplified Tax Invoice jest stosowana w transakcjach B2C w Arabii Saudyjskiej, w których łączna kwota (wraz z VAT) nie przekracza 1 000 SAR. W przeciwieństwie do standardowych faktur VAT faktury uproszczone nie wymagają identyfikacji nabywcy, ale muszą zawierać kod QR z zakodowanymi w formacie TLV danymi sprzedawcy, kwotą VAT i znacznikiem czasu.

## Stan wsparcia

| Komponent        | Status        |
| ---------------- | ------------- |
| Podgląd          | ✅ Obsługiwany |
| Ekstrakcja pól   | ✅ Obsługiwany |
| Transformacja    | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/zatca-simplified-preview.png" alt="Podgląd faktury ZATCA Simplified w DocBits"><figcaption><p>Domyślny podgląd DocBits dla saudyjskiej faktury ZATCA Simplified</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
