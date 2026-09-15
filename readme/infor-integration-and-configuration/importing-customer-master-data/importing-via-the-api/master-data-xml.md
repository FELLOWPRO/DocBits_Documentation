---
description: Jak zaimportować dane główne z pliku XML do zbioru danych lookup
---

# Importowanie Danych Głównych z XML

Oprócz importów BOD DocBits potrafi wczytać dane główne z **dowolnego pliku XML** do wybranego przez Ciebie zbioru danych lookup. Wskazujesz, do którego zbioru zapisać i z którego XPath ma być odczytana każda kolumna, więc XML w ogóle nie musi mieć formatu BOD.

Używaj tego do danych głównych, które nie przychodzą jako BOD — cenników, miejsc powstawania kosztów, atrybutów artykułów, wszystkiego, co Twój system ERP potrafi wyeksportować jako XML.

## Dwa sposoby wysłania XML

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Kiedy go użyć |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Masz dane jako **plik XML** i chcesz go przesłać. |
| `/master_data_lookup/xml/import_xml_data` | Chcesz **wkleić XML** do żądania. W odróżnieniu od endpointów BOD ten przyjmuje XML jako zwykły tekst — bez opakowania w JSON. |

Oba są opisane poniżej. Kroki 1 i 2 są takie same w obu przypadkach.

## Zanim zaczniesz

Będziesz potrzebować:

* **Klucza API.** Zobacz [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md), jeśli jeszcze go nie masz.
* **XML** — jako pliku albo jako treści, którą można wkleić.
* **Typu danych** — nazwy zbioru danych lookup, do którego ma trafić zapis.
* **Mapowań pól** — który XPath wypełnia którą kolumnę.
* **Swojego Org ID**, z **Settings → Integration & SSO**, z sekcji **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Instrukcje krok po kroku

### 1. Otwórz link API

Otwórz interfejs testowy API dla środowiska i regionu, z którymi pracujesz:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Stany Zjednoczone)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Stany Zjednoczone)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Te endpointy znajdują się w sekcji **master data lookup**, a nie **import**, niżej na stronie.

{% hint style="info" %}
Używaj regionu, w którym hostowana jest Twoja organizacja — tego samego, przez który logujesz się do DocBits. Środowiska europejskie i amerykańskie są rozdzielone, więc import wysłany do niewłaściwego regionu nie pojawi się w Twojej organizacji.
{% endhint %}

### 2. Autoryzacja

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

Autoryzacja działa dokładnie tak jak przy importach BOD: kliknij **ikonę kłódki**, wklej swoje **Org ID** w **X-ORG-ID**, wklej swój klucz API w **X-API-KEY** i kliknij **Authorize** przy każdym z nich.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Wypełnij pola

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Kliknij **Try it out**, a następnie wypełnij formularz.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Pole | |
| --- | --- |
| **data\_type** | Wymagane. Zbiór danych lookup, do którego ma trafić zapis. Jest automatycznie zamieniany na małe litery, więc `PriceList` i `pricelist` to ten sam zbiór. |
| **field\_mappings** | Wymagane. Obiekt JSON łączący każdą kolumnę z XPath, z którego jest odczytywana. Zobacz poniżej. |
| **file** | Wymagane przy `import_xml_file`. Kliknij **Choose file** i wybierz swój XML. |
| **xml** | Wymagane przy `import_xml_data` zamiast pliku — wklej XML jako zwykły tekst. |
| **org\_id** | Twoje Org ID — ta sama wartość, którą podałeś w **X-ORG-ID** w kroku 2. |
| **sub\_org\_id** | Potrzebne tylko wtedy, gdy importujesz do konkretnej suborganizacji. |

#### Mapowania pól

`field_mappings` to obiekt JSON z jednym wpisem na kolumnę. W odróżnieniu od importów BOD, gdzie nazwy są ustalone na `custom_field_1` … `custom_field_5`, tutaj wybierasz je sam:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

Nazwy po lewej stronie stają się kolumnami zbioru danych i zależą wyłącznie od Ciebie. Wartości po prawej muszą odpowiadać strukturze przesyłanego XML — w powyższym przykładzie `//Item/ID` pobiera element `<ID>` wewnątrz każdego `<Item>`. Obie strony są niezależne: powyższe mapowanie wczytuje `<UnitPrice>` do kolumny o nazwie `Price`.

{% hint style="warning" %}
Odrzucane są tylko **nieprawidłowo zbudowane** XPath, z błędem `400` wskazującym pole. XPath, który jest poprawny, ale niczego nie znajduje w Twoim XML, przechodzi bez żadnego sygnału i po prostu pozostawia tę kolumnę pustą — literówka w ścieżce wygląda więc jak import, który się udał, ale zgubił kolumnę. Jeśli to ścieżka `ID` niczego nie znajduje, import zamiast tego kończy się błędem i zgłasza, że dla danego rekordu brakuje kolumny `ID`.
{% endhint %}

{% hint style="warning" %}
**Jedna z kolumn musi nazywać się `ID`.** To ona identyfikuje rekord: ponowny import tych samych danych aktualizuje wiersz o tym ID, zamiast dodawać duplikat. Wielkość liter nie ma znaczenia, więc `ID`, `Id` i `id` działają tak samo, ale nazwa taka jak `ItemID` już się nie liczy — żądanie zostanie odrzucone z `ID_FIELD_IS_MISSING` i nic nie zostanie zapisane.
{% endhint %}

{% hint style="warning" %}
**Jedno żądanie importuje jeden rekord.** Każdy XPath jest odczytywany raz, więc jeśli Twój XML zawiera kilka elementów, wykorzystane zostanie tylko pierwsze dopasowanie każdego z nich. Aby wczytać listę, wyślij po jednym żądaniu na rekord albo użyj importu CSV.
{% endhint %}

#### Wybór typu danych

`data_type` to klucz zbioru danych, do którego zapisujesz. Jest zamieniany na małe litery i przycinany ze spacji, więc `Items` i `items` to ten sam zbiór. Każda nazwa, która nie jest jeszcze zajęta, tworzy Twój własny zbiór — `items_example`, `cost_centres`, `price_list` — a ponowny import do niego go aktualizuje.

{% hint style="danger" %}
Niektóre nazwy nie są wolne: to własne tabele danych głównych DocBits, a import do jednej z nich zapisuje prosto do niej.

| Nazwa | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Odrzucane z `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Przyjmowane i nadpisują prawdziwe dane główne.** Używaj ich tylko wtedy, gdy naprawdę o to Ci chodzi. |

We wszystkich pozostałych przypadkach wybierz własną nazwę.
{% endhint %}

{% hint style="warning" %}
Przed wykonaniem sprawdź, na które środowisko i którą organizację wskazujesz. Import zapisuje bezpośrednio w danych głównych tej organizacji.
{% endhint %}

### 4. Wykonaj

Przed wykonaniem sprawdź listę rozwijaną **Servers** na dole formularza.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Kliknij **Execute**. Udany import zwraca:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

W odróżnieniu od importów BOD te endpointy zgłaszają problemy właściwym statusem błędu, a nie odpowiedzią `200` zawierającą `"success": false` — **400** oznacza, że żądanie zostało odrzucone i nic nie zostało zapisane.

### 5. Sprawdź, czy dane dotarły

* W DocBits przejdź do **Settings → Document Processing → Lookup Master Data**.
* Wybierz po lewej **Imported**, a następnie otwórz zakładkę swojego typu danych.
* Kolumny to nazwy użyte po lewej stronie w `field_mappings`.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
