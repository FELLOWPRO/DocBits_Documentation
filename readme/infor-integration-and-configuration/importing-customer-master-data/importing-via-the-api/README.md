---
description: Ręczne wysyłanie danych głównych do DocBits przez API
---

# Importowanie przez API

Dane główne zwykle trafiają do DocBits automatycznie przez przepływ danych ION. Strony w tej sekcji opisują, jak wysłać te same dane ręcznie za pomocą interfejsu testowego API — przydatne, gdy chcesz ponownie zaimportować rekord, wczytać coś, co nigdy nie dotarło, albo wypróbować nowe mapowanie pól przed włączeniem automatycznego przepływu.

Każda strona przebiega według tych samych pięciu kroków: otwórz link API dla swojego środowiska, autoryzuj się za pomocą Org ID i klucza API, wypełnij formularz, wykonaj żądanie i sprawdź, czy dane dotarły.

* [Importowanie Dostawców (Supplier BOD)](supplier-bod.md)
* [Importowanie Zamówień Zakupu (Purchase Order BOD)](purchase-order-bod.md)
* [Importowanie Przyjęć Towarów (Receive Delivery BOD)](receive-delivery-bod.md)
* [Importowanie Danych Głównych z XML](master-data-xml.md)

## Czego potrzebujesz

* **Klucza API** — zobacz [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Swojego Org ID** — w **Settings → Integration & SSO**, w sekcji **ID**.
* **Samych danych**, jako pliku XML lub jako treści XML, którą można wkleić.

{% hint style="warning" %}
Import zapisuje bezpośrednio w danych głównych Twojej organizacji. Przed wykonaniem sprawdź, na które środowisko, region i organizację wskazujesz.
{% endhint %}
