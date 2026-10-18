---
description: Obsługa dokumentu elektronicznego MEXICO CFDI 4.0 w DocBits
---

# 🇲🇽 MEXICO CFDI 4.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Meksyk](countries/mexico.md). Sprawdź przestrzeń nazw, wersję i TipoDeComprobante. Sama ujemna kwota nie identyfikuje noty kredytowej; parsowanie nie certyfikuje zatwierdzenia SAT.
{% endhint %}

| Właściwość           | Wartość                                            |
| -------------------- | -------------------------------------------------- |
| **Kraj / Region**    | Meksyk                                             |
| **Typy dokumentów**  | Faktura, Nota kredytowa, Potwierdzenie płatności   |
| **Format**           | XML                                                |
| **Standard**         | CFDI 4.0 (Comprobante Fiscal Digital por Internet) |

CFDI 4.0 to aktualna wersja meksykańskiego standardu cyfrowego dowodu podatkowego, obowiązkowa od stycznia 2023 roku. Wymaga podania nazwy odbiorcy i jego reżimu podatkowego (régimen fiscal), dodaje pole eksportu oraz zawiera zaktualizowaną pieczęć cyfrową i łańcuch certyfikatów SAT.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-4-0-preview.png" alt="Podgląd faktury Mexico CFDI 4.0 w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Mexico CFDI 4.0</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
