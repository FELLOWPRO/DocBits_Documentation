# Zamówienie zakupu

## Przegląd

To ustawienie włącza sekcję [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/), która staje się dostępna po walidacji dokumentu.

<mark style="color:red;">**Uwaga**</mark>: Dla typu dokumentu **Invoice** muszą być spełnione następujące dodatkowe wymagania:

* Ustawienie **Purchase Order** musi być włączone (jak opisano na tej stronie)
* Faktura musi być typu **Purchase Invoice**
* Musi być obecna **Extracted Table**

## Kroki aktywacji <a href="#activation-steps" id="activation-steps"></a>

1. Przejdź do **Settings → Document Types**.
2. Znajdź kartę typu dokumentu i kliknij ikonę koła zębatego (**More Settings**).
3. Otwórz sekcję **Purchase Order** i włącz **Purchase Order**.

<figure><img src="../../../../../../.gitbook/assets/po-settings-purchase-order-pl-20261031.png" alt="More Settings typu dokumentu Invoice z otwartą sekcją Purchase Order"><figcaption><p>Sekcja <strong>Purchase Order</strong> w <strong>More Settings</strong>. Pierwszy przełącznik włącza dopasowanie zamówień dla typu dokumentu, kolejne je doprecyzowują.</p></figcaption></figure>

## **Funkcjonalność**

Po włączeniu ustawienia sekcja [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/) jest dostępna po walidacji dokumentu.

### Która ilość jest porównywana

To, którą ilość zamówienia porównuje dopasowanie, zależy od **PO match server side**:

* **PO match server side off** – obok przełącznika **Purchase Order** pojawia się lista **Match quantity**. Wybierz **Quantity**, **Received Quantity** lub **Received Delivery Open Quantity**. DocBits porównuje wybraną ilość własnym mechanizmem dopasowania.
* **PO match server side on** – dopasowanie działa według zestawu reguł typu dokumentu, a **Match quantity** jest częścią tych reguł. Wiersz nagłówka sekcji pokazuje wtedy link **Configure PO matching rules**, który otwiera reguły. Zobacz [Purchase Order Matching Rules](purchase-order-matching-rules.md).

{% hint style="info" %}
Zrzut powyżej wykonano z włączonym **PO match server side**, dlatego lista **Match quantity** nie jest widoczna na tym ekranie - ustawia się ją w regułach dopasowania.
{% endhint %}

### Przedpłata przed przyjęciem towaru

Niektóre faktury przychodzą przed towarem. Aby dopasować taką fakturę do ilości zamówionej, a nie otrzymanej, włącz **Allow pre-payment before goods receipt** w tej samej sekcji.

Przełącznik pojawia się tylko wtedy, gdy spełnione są wszystkie trzy warunki:

* typ dokumentu to **Invoice**,
* **Purchase Order** jest włączone,
* a dopasowywana ilość to **Received Quantity**.

Jeśli zmienisz dopasowywaną ilość na inną wartość, przełącznik zniknie z ustawień. Na [PO matching screen](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/) pojawia się wtedy **Match as pre-payment** poniżej **Use Lines Net Amount for Matched Total**, z podpowiedzią *Match on ordered quantity instead of received quantity*. Przełącznik jest wyszarzony i opatrzony notatką, gdy dostawca nie może być zafakturowany przed przyjęciem towaru w ERP.

Dopóki przełącznik jest włączony, ekran odczytuje ilość zamówioną, a nie otrzymaną, dla ręcznych powiązań i dla dopasowanej sumy. Wybór jest zapisywany na dokumencie i **Auto Match** uruchamia się ponownie; jeśli to dopasowanie się nie powiedzie, wybór wraca do poprzedniej wartości.
