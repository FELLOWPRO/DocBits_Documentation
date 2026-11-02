---
description: Jak importować dane podstawowe bezpośrednio w DocBits.
---

# Własne dane podstawowe

#### Aktywacja własnych danych podstawowych <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Na pulpicie przejdź do Ustawienia → Przetwarzanie dokumentów → Moduł.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-pl.png" alt="Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska."><figcaption><p>Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska.</p></figcaption></figure></div>

W sekcji Moduł aktywuj funkcję Custom Master Data, przesuwając suwak, jak pokazano poniżej.

<div align="left"></div>

#### Przegląd funkcji <a href="#feature-overview" id="feature-overview"></a>

Aby dodać własne dane podstawowe do DocBits, przejdź w Ustawieniach do Master Data Lookup.

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-pl.png" alt="Wyszukiwanie danych podstawowych: źródła i tabela dostawców z ukrytymi wartościami."><figcaption><p>Wyszukiwanie danych podstawowych: źródła i tabela dostawców z ukrytymi wartościami.</p></figcaption></figure></div>

Kliknij „Custom Master Data”

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

Następnie możesz utworzyć szablon (Template) lub punkt końcowy (Endpoint).

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Tworzenie szablonu <a href="#create-a-template" id="create-a-template"></a>

Pierwszym krokiem jest wybór między użyciem pliku ION API Twojej organizacji a użyciem OAuth2 i wprowadzeniem niezbędnych danych.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Następnie skonfigurujemy ustawienia wstępne. Tutaj wprowadzisz nazwę tabeli danych podstawowych oraz adres URL wywołania API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Następnie należy podać ścieżkę JSON w notacji kropkowej. Więcej informacji o notacji kropkowej znajdziesz [tutaj](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Na koniec musisz zmapować dane na kolumny, które chcesz utworzyć, jak w przykładzie poniżej.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Po wykonaniu tych czynności kliknij Done, aby utworzyć i wypełnić nowe dane podstawowe.

#### Tworzenie punktu końcowego <a href="#create-an-endpoint" id="create-an-endpoint"></a>

Pierwszym krokiem jest wybór między użyciem pliku ION API Twojej organizacji, użyciem OAuth2 lub pozostawieniem tego pola pustego i wprowadzeniem niezbędnych danych.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Następnie skonfigurujemy ustawienia wstępne. Tutaj wprowadzisz nazwę tabeli danych podstawowych oraz adres URL wywołania API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Następnie należy podać ścieżkę JSON w notacji kropkowej. Więcej informacji o notacji kropkowej znajdziesz [tutaj](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Na koniec musisz zmapować dane na kolumny, które chcesz utworzyć, jak w przykładzie poniżej.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Po wykonaniu tych czynności kliknij Done, aby utworzyć i wypełnić nowe dane podstawowe.
