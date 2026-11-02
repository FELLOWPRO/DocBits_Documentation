---
description: Jak ręcznie zaimportować Receive Delivery BOD do DocBits przez API
---

# Importowanie Przyjęć Towarów (Receive Delivery BOD)

Przyjęcia towarów zwykle trafiają do DocBits automatycznie przez przepływ danych ION. Ta strona opisuje, jak wysłać **Receive Delivery BOD** ręcznie — przydatne, gdy chcesz ponownie zaimportować przyjęcie, wczytać partię, która nigdy nie dotarła, albo przetestować mapowanie pól przed włączeniem automatycznego przepływu.

## Dwa sposoby wysłania tego samego BOD

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-endpoints.png)

| Endpoint | Kiedy go użyć |
| --- | --- |
| `/import/receive_delivery_bod` | Masz BOD jako **plik XML** i chcesz go przesłać. |
| `/import/receive_delivery_bod_xml` | Chcesz wysłać **treść XML** w żądaniu zamiast pliku. BOD trzeba opakować w JSON, więc nadaje się to do krótkiego XML albo do innego systemu wywołującego API — dla pełnego BOD ręcznie lepiej przesłać plik. |

Oba są opisane poniżej. Kroki 1 i 2 są takie same w obu przypadkach.

## Zanim zaczniesz

Będziesz potrzebować:

* **Klucza API.** Zobacz [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md), jeśli jeszcze go nie masz.
* **BOD** — pliku XML `SyncReceiveDelivery`, albo jego treści.
* **Swojego Org ID**, z **Settings → Integration & SSO**, z sekcji **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** pokazuje tę suborganizację, która jest wybrana w nagłówku. Przy wybranym **CROSS** — widoku obejmującym wszystkie suborganizacje — pokazuje tę samą wartość co **Org ID**. Przełącz się najpierw na konkretną suborganizację, jeśli potrzebujesz jej ID.

Jeśli nie importujesz do konkretnej suborganizacji, zostaw pole `sub_org_id` puste.
{% endhint %}

## Instrukcje krok po kroku

### 1. Otwórz link API

Otwórz interfejs testowy API dla środowiska i regionu, z którymi pracujesz:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Sandbox API (Stany Zjednoczone)](https://us.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Stany Zjednoczone)](https://us.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)

Rozwiń wybrany endpoint, klikając w niego.

{% hint style="info" %}
Używaj regionu, w którym hostowana jest Twoja organizacja — tego samego, przez który logujesz się do DocBits. Środowiska europejskie i amerykańskie są rozdzielone, więc import wysłany do niewłaściwego regionu nie pojawi się w Twojej organizacji.

Adresy bez przedrostka regionu — `api.docbits.com` i `sandbox.api.docbits.com` — wskazują na Europę. Spotkasz je w starszej dokumentacji i w istniejących konfiguracjach; to to samo środowisko co adresy `eu.` powyżej.
{% endhint %}

### 2. Autoryzacja

Wszystko w sekcji **import** jest zablokowane, dopóki się nie autoryzujesz. Trzeba podać dwie rzeczy: swoją organizację i swój klucz API.

* Kliknij **ikonę kłódki** po prawej stronie endpointu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-lock.png)

* Otworzy się okno **Available authorizations** z dwoma wpisami.
* Wklej swoje **Org ID** w **X-ORG-ID** i kliknij **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Przewiń do **X-API-KEY**, wklej swój klucz API i kliknij **Authorize**. W DocBits znajdziesz go w **Settings → Integration & SSO**, w sekcji **API Key**, albo możesz [utworzyć nowy klucz](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#tworzenie-klucza-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Kliknij **Close**.

{% hint style="info" %}
Wklej sam klucz — nie wpisuj przed nim `Bearer`. Obie autoryzacje pozostają ustawione, dopóki nie przeładujesz strony albo nie klikniesz **Logout**.
{% endhint %}

### 3. Wypełnij pola

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-rd.png)

Kliknij **Try it out**, a następnie wypełnij formularz wybranego endpointu.

#### Przesyłanie pliku — `/import/receive_delivery_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-form.png)

| Pole | |
| --- | --- |
| **file** | Wymagane. Kliknij **Choose file** i wybierz swój plik XML `SyncReceiveDelivery`. |
| **org\_id** | Twoje Org ID — ta sama wartość, którą podałeś w **X-ORG-ID** w kroku 2. Ustawienie jej również tutaj sprawia, że żądanie jednoznacznie wskazuje, do której organizacji zapisuje. Musi to być organizacja, do której Twój klucz API ma dostęp; każda inna zostanie odrzucona. |
| **sub\_org\_id** | Potrzebne tylko wtedy, gdy importujesz do konkretnej suborganizacji. |
| **custom\_fields\_mapping** | Opcjonalne. Dodatkowe pola nagłówka. Zobacz [Mapowania pól niestandardowych](#mapowania-pol-niestandardowych) poniżej. |
| **custom\_line\_fields\_mapping** | Opcjonalne. To samo, dla dodatkowych pól w wierszach przyjęcia. |
| **populate\_additional\_info** | Opcjonalne, domyślnie `false`. Ustaw na `true`, aby DocBits pobrał po imporcie dodatkowe informacje o przyjęciu z systemu ERP. Zostaw `false`, chyba że wiesz, że tego potrzebujesz — spowalnia to import. |

{% hint style="warning" %}
**`string` to wartość, a nie symbol zastępczy.** Swagger wypełnia pola opcjonalne słowem `string` i zostanie ono wysłane bez zmian, jeśli je zostawisz — import z `org_id` ustawionym na `string` zakończy się błędem.

Dla każdego pola opcjonalnego, którego nie chcesz używać, wyczyść jego zawartość. Wyczyszczenie włącza pole wyboru **Send empty value** poniżej, które możesz wtedy zaznaczyć.
{% endhint %}

#### Mapowania pól niestandardowych

Oba pola mapowania przyjmują obiekt JSON. **Nazwa po lewej stronie musi być jednym z własnych pól niestandardowych DocBits** — od `custom_field_1` do `custom_field_10` dla przyjęć towarów, dwa razy więcej niż dopuszczają zamówienia zakupu. Każda inna nazwa jest ignorowana bez ostrzeżenia, więc literówka w tym miejscu wygląda dokładnie tak samo jak mapowanie, które nie zadziałało.

Wartość po prawej stronie to XPath, z którego następuje odczyt. Zapisz go bez przedrostków przestrzeni nazw — DocBits dodaje je sam:

```json
{"custom_field_2": "//ReceiveDelivery/ReceiveDeliveryHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Mapowania wierszy używają tych samych nazw `custom_field_1` … `custom_field_10`, ale ich XPath są odczytywane **względem każdego wiersza przyjęcia**, więc zaczynają się od `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Wklejanie XML — `/import/receive_delivery_bod_xml`

<!-- SCREENSHOT: the Try it out form of /import/receive_delivery_bod_xml -->

Ten endpoint nie przyjmuje BOD jako zwykłego wklejenia. Pole **xml** jest obiektem, wstępnie wypełnionym wartością `{"xml": "string"}`. Zastąp `string` treścią swojego BOD, zachowując otaczające cudzysłowy i nawiasy klamrowe:

```json
{
  "xml": "<SyncReceiveDelivery ...>...</SyncReceiveDelivery>"
}
```

{% hint style="warning" %}
BOD znajduje się wewnątrz łańcucha JSON, więc każdy podwójny cudzysłów w XML trzeba poprzedzić znakiem ucieczki jako `\"` — a BOD jest ich pełen. Jeśli wynik nie będzie poprawnym JSON-em, żądanie zakończy się błędem **422** i nic nie zostanie zaimportowane.

Dla prawdziwego BOD jest to żmudne do zrobienia ręcznie, dlatego lepiej **przesłać plik**.
{% endhint %}

Ten endpoint przyjmuje `org_id`, `sub_org_id` i `populate_additional_info`, ale **żadnych mapowań pól** — ani nagłówka, ani wierszy. Jeśli Twoje przyjęcia potrzebują pól niestandardowych, prześlij zamiast tego plik.

{% hint style="warning" %}
Przed wykonaniem sprawdź, na które środowisko i którą organizację wskazujesz. Import zapisuje bezpośrednio w danych głównych tej organizacji.
{% endhint %}

### 4. Wykonaj

Przed wykonaniem sprawdź listę rozwijaną **Servers** na dole formularza. Decyduje ona o tym, do którego środowiska żądanie faktycznie trafi, i może się różnić od strony, którą otworzyłeś.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-execute.png)

Kliknij **Execute**. Udany import zwraca:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-response.png)

Receive delivery BOD są przetwarzane od razu, więc zanim zobaczysz ten komunikat, dane są już na miejscu.

Jeśli coś było nie tak z żądaniem, otrzymasz `"success": false` wraz z komunikatem opisującym problem.

### 5. Sprawdź, czy dane dotarły

* W DocBits przejdź do **Settings → Document Processing → Lookup Master Data**.
* Wybierz po lewej **BOD Input Data**, a następnie otwórz zakładkę z zaimportowanymi danymi.
* Wyszukaj przyjęcie albo zamówienie zakupu, do którego należy.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the goods receipt data shown -->

{% hint style="info" %}
DocBits decyduje, co zrobić z BOD, na podstawie typu zapisanego w jego wnętrzu, a nie na podstawie użytego endpointu importu. Jeśli przez pomyłkę wyślesz tutaj inny BOD, zostanie on zaimportowany jako ten typ, a nie odrzucony — sprawdź więc, czy zakładka, w której znajdujesz dane, jest tą, której oczekiwałeś.
{% endhint %}
