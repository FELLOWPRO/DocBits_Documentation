---
description: Obsługa dokumentu elektronicznego INVOIC02 w DocBits
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Międzynarodowe](countries/international.md). Mapowania faktur, zamówień, odpowiedzi i awiz wysyłki są odrębne. Samo przetwarzanie plików nie zapewnia punktu dostępowego Peppol ani łączności z partnerami handlowymi.
{% endhint %}

| Właściwość           | Wartość                 |
| -------------------- | ----------------------- |
| **Kraj / Region**    | Międzynarodowy          |
| **Typy dokumentów**  | Faktura                 |
| **Format**           | EDIFACT                 |
| **Standard**         | UN/EDIFACT INVOIC D.02B |

INVOIC02 to komunikat faktury UN/EDIFACT oparty na wersji katalogu D.02B. EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) to szeroko stosowany standard EDI w logistyce, handlu detalicznym i produkcji. DocBits analizuje strukturę segmentów EDIFACT i wyodrębnia pola nagłówka, pozycji oraz podsumowania.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="Podgląd faktury INVOIC02 w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury INVOIC02</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
