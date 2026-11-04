# Konfiguracja wyszukiwania przez REST API

## Tabela `public.rest_api_lookup_configurations`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `data_key`: internal
* `url`: internal
* `method`: internal
* `params`: text
* `headers`: text
* `body`: text
* `body_type`: internal
* `authentication_type`: internal
* `authentication_json`: text
* `data_base_path`: internal
* `column_paths`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_on`: znacznik czasu ze strefą czasową
* `is_template`: boolean
* `is_dynamic`: boolean

### Analiza i opis

## Dokumentacja techniczna: tabela `public.rest_api_lookup_configurations`

### Wprowadzenie

Tabela `public.rest_api_lookup_configurations` służy do przechowywania konfiguracji wyszukiwań (lookup) przez REST API w organizacji. Tabela zawiera podstawowe informacje potrzebne do wykonywania żądań API, w tym szczegóły dotyczące punktów końcowych, metod uwierzytelniania oraz konfiguracji żądań i odpowiedzi. Wydaje się być używana do dynamicznego tworzenia wywołań API i analizowania ich wyników.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego wpisu konfiguracji.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciągi UUID, takie jak `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Uwaga**: Jest to unikalny klucz służący do identyfikacji konkretnej konfiguracji wyszukiwania API.

#### org\_id

* **Znaczenie**: Identyfikator organizacji, do której należy konfiguracja.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciągi UUID reprezentujące identyfikatory organizacji.
* **Uwaga**: Łączy konfigurację z organizacją.

#### sub\_org\_id

* **Znaczenie**: Identyfikator podorganizacji w ramach organizacji głównej.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciągi UUID reprezentujące identyfikatory podorganizacji.
* **Uwaga**: Umożliwia dalszą szczegółowość w ramach organizacji.

#### data\_key

* **Znaczenie**: Etykieta lub klucz identyfikujący dane albo punkt końcowy API.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Tekst opisowy, taki jak `bank_codes`.
* **Uwaga**: Służy do rozróżniania różnych typów danych lub punktów końcowych.

#### url

* **Znaczenie**: Adres URL punktu końcowego API, który ma zostać wywołany.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciągi URL, takie jak `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Uwaga**: Reprezentuje punkt końcowy, do którego wysyłane jest żądanie HTTP.

#### method

* **Znaczenie**: Metoda HTTP używana w żądaniu API.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Popularne metody HTTP, takie jak `GET`.
* **Uwaga**: Określa typ wykonywanego żądania HTTP.

#### params

* **Znaczenie**: Parametry, które mają zostać dołączone do żądania API.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: JSON lub pary klucz-wartość (często `None`, jeśli nie są używane).
* **Uwaga**: Zawiera dynamiczne parametry żądania.

#### headers

* **Znaczenie**: Nagłówki HTTP, które mają zostać dołączone do żądania.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Dane JSON lub tekstowe (często `None`, jeśli nie są używane).
* **Uwaga**: Służy do dołączania dodatkowych metadanych do żądania.

#### body

* **Znaczenie**: Treść (body) żądania HTTP.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Dane JSON lub inne zserializowane dane (często `None`, jeśli nie są używane).
* **Uwaga**: Zawiera ładunek dla żądań POST/PUT.

#### body\_type

* **Znaczenie**: Określa format treści żądania.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Typy MIME, takie jak `application/json`.
* **Uwaga**: Wskazuje typ zawartości treści żądania.

#### authentication\_type

* **Znaczenie**: Typ uwierzytelniania używanego w żądaniu API.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Metody uwierzytelniania, takie jak `ionapi`.
* **Uwaga**: Określa sposób uwierzytelniania żądania.

#### authentication\_json

* **Znaczenie**: Szczegóły konfiguracji uwierzytelniania w formacie JSON.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Ciągi JSON z informacjami o uwierzytelnianiu.
* **Uwaga**: Zawiera dane uwierzytelniające i szczegóły punktu końcowego uwierzytelniania.

#### data\_base\_path

* **Znaczenie**: Ścieżka w odpowiedzi API, z której mają być wyodrębniane dane.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Wyrażenia ścieżki JSON, takie jak `$[results][0][records]`.
* **Uwaga**: Służy do analizowania danych odpowiedzi API.

#### column\_paths

* **Znaczenie**: Mapuje pola danych na kolumny do ekstrakcji.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Ciągi JSON mapujące pola odpowiedzi API na nazwy kolumn.
* **Uwaga**: Ułatwia ekstrakcję danych z odpowiedzi API.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył konfigurację.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Identyfikatory całkowite, takie jak `1`.
* **Uwaga**: Śledzi twórcę wpisu konfiguracji.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia konfiguracji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znaczniki czasu, takie jak `2024-01-24T09:14:24.788788Z`.
* **Uwaga**: Wskazuje datę i godzinę utworzenia.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znaczniki czasu (często `None`, jeśli nie modyfikowano).
* **Uwaga**: Rejestruje czas ostatniej aktualizacji.

#### is\_deleted

* **Znaczenie**: Flaga wskazująca, czy konfiguracja została oznaczona jako usunięta.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartości logiczne, takie jak `False`.
* **Uwaga**: Służy do miękkiego usuwania konfiguracji.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia konfiguracji jako usuniętej.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znaczniki czasu (często wartość zastępcza, jeśli nie usunięto).
* **Uwaga**: Rejestruje, kiedy konfiguracja została oznaczona jako usunięta.

#### is\_template

* **Znaczenie**: Wskazuje, czy konfiguracja służy jako szablon.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartości logiczne, takie jak `True`.
* **Uwaga**: Identyfikuje szablony do ponownego użycia.

#### is\_dynamic

* **Znaczenie**: Określa, czy konfiguracja jest dynamiczna.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartości logiczne, takie jak `False`.
* **Uwaga**: Określa, czy konfiguracja dostosowuje się do zmieniających się danych.
