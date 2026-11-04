---
description: Obsługa dokumentu elektronicznego MEXICO CFDI 3.3 w DocBits
---

# 🇲🇽 MEXICO CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Sprawdź w przewodniku krajowym ograniczenia wersji, faktycznie używaną konfigurację i film objaśniający dla kraju. [Meksyk](countries/mexico.md). Sprawdź przestrzeń nazw, wersję i TipoDeComprobante. Sama ujemna kwota nie identyfikuje noty kredytowej; parsowanie nie certyfikuje zatwierdzenia SAT.
{% endhint %}

| Właściwość           | Wartość                                            |
| -------------------- | -------------------------------------------------- |
| **Kraj / Region**    | Meksyk                                             |
| **Typy dokumentów**  | Faktura, Nota kredytowa, Potwierdzenie płatności   |
| **Format**           | XML                                                |
| **Standard**         | CFDI 3.3 (Comprobante Fiscal Digital por Internet) |

CFDI 3.3 to poprzednia generacja meksykańskiego standardu cyfrowego dowodu podatkowego, wydawanego przez SAT (Servicio de Administración Tributaria). Choć została zastąpiona przez CFDI 4.0, wiele historycznych faktur nadal korzysta z tej wersji. Zawiera UUID (folio fiscal), identyfikatory RFC oraz obliczenia podatków IEPS/IVA.

## Status obsługi

| Komponent      | Status         |
| -------------- | -------------- |
| Podgląd        | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja  | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="Podgląd faktury Mexico CFDI 3.3 w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Mexico CFDI 3.3</p></figcaption></figure>

## Powiązane

* [Obsługiwane dokumenty elektroniczne](./)
