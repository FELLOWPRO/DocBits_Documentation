---
description: Jak ręcznie zaimportować Purchase Order BOD do DocBits przez API
---

# Importowanie Zamówień Zakupu (Purchase Order BOD)

Zamówienia zakupu zwykle trafiają do DocBits automatycznie przez przepływ danych ION. Ta strona opisuje, jak wysłać **Purchase Order BOD** ręcznie — przydatne, gdy chcesz ponownie zaimportować zamówienie, wczytać partię, która nigdy nie dotarła, albo przetestować nowe mapowanie przed włączeniem automatycznego przepływu.

## Dwa sposoby wysłania tego samego BOD

Są dwa endpointy i robią to samo. Jedyna różnica polega na tym, jak przekazujesz BOD:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-endpoints.png)

| Endpoint | Kiedy go użyć |
| --- | --- |
| `/import/purchase_order_bod` | Masz BOD jako **plik XML** i chcesz go przesłać. |
| `/import/purchase_order_bod_xml` | Chcesz wysłać **treść XML** w żądaniu zamiast pliku. BOD trzeba opakować w JSON, więc nadaje się to do krótkiego XML albo do innego systemu wywołującego API — dla pełnego BOD ręcznie lepiej przesłać plik. |

Oba są opisane poniżej. Kroki 1 i 2 są takie same w obu przypadkach.

## Zanim zaczniesz

Będziesz potrzebować:

* **Klucza API.** Zobacz [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md), jeśli jeszcze go nie masz.
* **BOD** — pliku XML `SyncPurchaseOrder`, albo jego treści.
* **Swojego Org ID**, jeśli importujesz do organizacji innej niż ta, do której należy Twój klucz.

Aby znaleźć Org ID, przejdź do **Settings → Integration & SSO** i otwórz sekcję **ID**. Kliknij ikonę kopiowania obok pola.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** pokazuje tę suborganizację, która jest wybrana w nagłówku. Przy wybranym **CROSS** — widoku obejmującym wszystkie suborganizacje — pokazuje tę samą wartość co **Org ID**, dlatego oba pola na zrzucie powyżej są zgodne. Przełącz się najpierw na konkretną suborganizację, jeśli potrzebujesz jej ID.

Jeśli nie importujesz do konkretnej suborganizacji, zostaw pole `sub_org_id` puste.
{% endhint %}

## Instrukcje krok po kroku

### 1. Otwórz link API

Otwórz interfejs testowy API dla środowiska i regionu, z którymi pracujesz:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Sandbox API (Stany Zjednoczone)](https://us.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Stany Zjednoczone)](https://us.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)

Rozwiń wybrany endpoint, klikając w niego.

{% hint style="info" %}
Używaj regionu, w którym hostowana jest Twoja organizacja — tego samego, przez który logujesz się do DocBits. Środowiska europejskie i amerykańskie są rozdzielone, więc import wysłany do niewłaściwego regionu nie pojawi się w Twojej organizacji.

Adresy bez przedrostka regionu — `api.docbits.com` i `sandbox.api.docbits.com` — wskazują na Europę. Spotkasz je w starszej dokumentacji i w istniejących konfiguracjach; to to samo środowisko co adresy `eu.` powyżej.
{% endhint %}

### 2. Autoryzacja

Wszystko w sekcji **import** jest zablokowane, dopóki się nie autoryzujesz. Trzeba podać dwie rzeczy: swoją organizację i swój klucz API.

* Kliknij **ikonę kłódki** po prawej stronie endpointu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-swagger-lock.png)

* Otworzy się okno **Available authorizations** z dwoma wpisami.
* Wklej swoje **Org ID** w **X-ORG-ID** i kliknij **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

* Wpis pokazuje teraz **Authorized** i ukrywa wartość.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Przewiń do **X-API-KEY**, wklej swój klucz API i kliknij **Authorize**. W DocBits znajdziesz go w **Settings → Integration & SSO**, w sekcji **API Key**, albo możesz [utworzyć nowy klucz](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#tworzenie-klucza-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Kliknij **Close**.

{% hint style="info" %}
Wklej sam klucz — nie wpisuj przed nim `Bearer`. Obie autoryzacje pozostają ustawione, dopóki nie przeładujesz strony albo nie klikniesz **Logout**.
{% endhint %}

### 3. Wypełnij pola

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-po.png)

Kliknij **Try it out**, a następnie wypełnij formularz wybranego endpointu.

#### Przesyłanie pliku — `/import/purchase_order_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-form.png)

| Pole | |
| --- | --- |
| **file** | Wymagane. Kliknij **Choose file** i wybierz swój plik XML `SyncPurchaseOrder`. |
| **org\_id** | Twoje Org ID — ta sama wartość, którą podałeś w **X-ORG-ID** w kroku 2. Ustawienie jej również tutaj sprawia, że żądanie jednoznacznie wskazuje, do której organizacji zapisuje. Musi to być organizacja, do której Twój klucz API ma dostęp; każda inna zostanie odrzucona. |
| **sub\_org\_id** | Potrzebne tylko wtedy, gdy pracujesz z suborganizacjami. W przeciwnym razie zostaw puste. |
| **custom\_fields\_mapping** | Opcjonalne. Wczytuje dodatkowe pola nagłówka z BOD do pól niestandardowych zamówienia. Zobacz [Mapowania pól niestandardowych](#mapowania-pol-niestandardowych) poniżej. |
| **custom\_line\_fields\_mapping** | Opcjonalne. To samo, dla dodatkowych pól w wierszach zamówienia. |

{% hint style="warning" %}
**`string` to wartość, a nie symbol zastępczy.** Swagger wypełnia pola opcjonalne słowem `string` i zostanie ono wysłane bez zmian, jeśli je zostawisz — import z `org_id` ustawionym na `string` zakończy się błędem.

Dla każdego pola opcjonalnego, którego nie chcesz używać, wyczyść jego zawartość. Wyczyszczenie włącza pole wyboru **Send empty value** poniżej, które możesz wtedy zaznaczyć. Na zrzucie powyżej zrobiono tak dla `sub_org_id`.
{% endhint %}

#### Mapowania pól niestandardowych

Oba pola mapowania przyjmują obiekt JSON. **Nazwa po lewej stronie musi być jednym z własnych pól niestandardowych DocBits** — od `custom_field_1` do `custom_field_5` dla zamówień zakupu. Każda inna nazwa jest ignorowana bez ostrzeżenia, więc literówka w tym miejscu wygląda dokładnie tak samo jak mapowanie, które nie zadziałało.

Wartość po prawej stronie to XPath, z którego następuje odczyt. Zapisz go bez przedrostków przestrzeni nazw — DocBits dodaje je sam:

```json
{"custom_field_2": "//PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Mapowania wierszy używają tych samych nazw `custom_field_1` … `custom_field_5`, ale ich XPath są odczytywane **względem każdego wiersza zamówienia**, więc zaczynają się od `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Wklejanie XML — `/import/purchase_order_bod_xml`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-xml-form.png)

Ten endpoint nie przyjmuje BOD jako zwykłego wklejenia. Pole **xml** jest obiektem, wstępnie wypełnionym wartością:

```json
{
  "xml": "string"
}
```

Zastąp `string` treścią swojego BOD, zachowując otaczające cudzysłowy i nawiasy klamrowe:

```json
{
  "xml": "<SyncPurchaseOrder ...>...</SyncPurchaseOrder>"
}
```

{% hint style="warning" %}
BOD znajduje się wewnątrz łańcucha JSON, więc każdy podwójny cudzysłów w XML trzeba poprzedzić znakiem ucieczki jako `\"` — a BOD jest ich pełen (`releaseID="9.2"`, `xmlns="..."`). Jeśli wynik nie będzie poprawnym JSON-em, żądanie zakończy się błędem **422** i nic nie zostanie zaimportowane.

Dla prawdziwego BOD jest to żmudne do zrobienia ręcznie, dlatego lepiej **przesłać plik**. Ten endpoint jest lepszym wyborem, gdy XML jest krótki albo gdy żądanie buduje inny system, który potrafi sam zakodować JSON.
{% endhint %}

Pola `org_id`, `sub_org_id` i `custom_fields_mapping` działają dokładnie tak jak powyżej. Ten endpoint nie ma pola na mapowania wierszy.

{% hint style="warning" %}
Przed wykonaniem sprawdź, na które środowisko i którą organizację wskazujesz. Import zapisuje bezpośrednio w danych głównych tej organizacji.
{% endhint %}

### 4. Wykonaj

Przed wykonaniem sprawdź listę rozwijaną **Servers** na dole formularza. Decyduje ona o tym, do którego środowiska żądanie faktycznie trafi, i może się różnić od strony, którą otworzyłeś.

Kliknij **Execute**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

**Jeśli przesłałeś plik**, odpowiedź brzmi:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-response.png)

```json
{
  "success": true,
  "message": "BOD processing started in the background."
}
```

{% hint style="info" %}
**Oznacza to, że plik został przyjęty, a nie że import się zakończył.** Przesłane pliki zamówień zakupu są przetwarzane w tle, żeby duże zamówienia nie blokowały reszty systemu. Odczekaj chwilę, a potem sprawdź wynik zgodnie z opisem poniżej.
{% endhint %}

**Jeśli wkleiłeś XML**, import wykonuje się natychmiast, a odpowiedź to `"BOD processed successfully."` — zanim ją zobaczysz, dane są już na miejscu.

Jeśli coś było nie tak z żądaniem, otrzymasz `"success": false` wraz z komunikatem opisującym problem. Najczęstsze przyczyny to treść, która nie jest BOD `SyncPurchaseOrder`, oraz Org ID, do którego Twój klucz API nie ma dostępu.

### 5. Sprawdź, czy dane dotarły

* W DocBits przejdź do **Settings → Document Processing → Lookup Master Data**.
* Wybierz po lewej **BOD Input Data**, a następnie otwórz zakładkę **Purchase Order**.
* Wyszukaj numer zamówienia ze swojego BOD.

<!-- SCREENSHOT F: Lookup Master Data with BOD Input Data selected and the Purchase Order tab open -->

Jeśli zamówienie jest na liście, import się powiódł, a zamówienie zakupu jest dostępne do PO matching.

{% hint style="info" %}
DocBits decyduje, co zrobić z BOD, na podstawie typu zapisanego w jego wnętrzu, a nie na podstawie użytego endpointu importu. Jeśli przez pomyłkę wyślesz tutaj supplier BOD, zostanie on zaimportowany jako dane dostawcy, a nie odrzucony — sprawdź więc, czy zakładka, w której znajdujesz dane, jest tą, której oczekiwałeś.
{% endhint %}
