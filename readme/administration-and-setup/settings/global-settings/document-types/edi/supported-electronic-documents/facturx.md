---
description: Obsługa dokumentów elektronicznych FACTURX w DocBits
---

# 🇫🇷 FACTURX

| Właściwość           | Wartość                  |
| -------------------- | ------------------------ |
| **Kraj / Region**    | Francja / Niemcy         |
| **Typy dokumentów**  | Faktura, nota kredytowa  |
| **Format**           | CII (osadzony w PDF/A-3) |
| **Standard**         | Factur-X                 |
| **Oparty na**        | EN 16931                 |

Factur-X to francuska implementacja francusko-niemieckiego standardu faktur hybrydowych. Osadza ustrukturyzowane dane XML CII w dokumencie PDF/A-3, umożliwiając fakturowanie zarówno czytelne dla człowieka, jak i przetwarzane maszynowo. DocBits automatycznie wykrywa wersję i profil Factur-X na podstawie osadzonego XML.

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
* [Mapowanie pól ZUGFeRD](../zugferd/versions/)
* [Obsługiwane dokumenty elektroniczne](./)
