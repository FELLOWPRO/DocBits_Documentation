# Fellow kv table column rule

## Tabela `public.fellow_kv_table_column_rule`

### Kolumny

* `id`: wewnętrzne
* `docType`: wewnętrzne
* `tableName`: wewnętrzne
* `dlfName`: wewnętrzne
* `multi_line`: boolean
* `filterID1`: wewnętrzne
* `filterID2`: wewnętrzne
* `filterID3`: wewnętrzne
* `tfidf_doc_id`: wewnętrzne
* `tfidf_id`: wewnętrzne
* `valuePattern`: wewnętrzne
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeric
* `normalizedY1`: numeric
* `normalizedX0`: numeric
* `normalizedX1`: numeric
* `width`: integer
* `height`: integer
* `patternLeft`: wewnętrzne
* `patternRight`: wewnętrzne
* `patternAbove`: wewnętrzne
* `patternBelow`: wewnętrzne
* `wordLeft`: wewnętrzne
* `wordAbove`: wewnętrzne
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID organizacji
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_new`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.fellow_kv_table_column_rule`

### Wprowadzenie

Tabela `public.fellow_kv_table_column_rule` służy do przechowywania reguł i wzorców przetwarzania lub ekstrakcji danych z dokumentów. Wynika to z obecności pól takich jak `docType`, `tableName`, `dlfName` oraz różnych pól związanych ze wzorcami i współrzędnymi. Tabela umożliwia stosowanie reguł do różnych typów dokumentów, co pozwala rozpoznawać wzorce i wyodrębniać dane z dokumentów ustrukturyzowanych, takich jak faktury lub umowy.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdej reguły.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciągi UUID.
* **Uwaga**: Niezbędny do jednoznacznej identyfikacji każdego wiersza.

#### docType

* **Znaczenie**: Typ dokumentu, do którego odnosi się reguła.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Typy dokumentów, takie jak 'INVOICE', 'CONTRACT'.
* **Uwaga**: Pomaga kategoryzować reguły według typu dokumentu.

#### tableName

* **Znaczenie**: Nazwa tabeli, w której stosowana jest reguła.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Nazwy tabel, takie jak 'INVOICE\_TABLE'.
* **Uwaga**: Wskazuje kontekst, w którym stosowana jest reguła.

#### dlfName

* **Znaczenie**: Nazwa konkretnego pola lub kolumny w dokumencie.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Nazwy pól, takie jak 'COUNTRY\_ORIGIN'.
* **Uwaga**: Określa docelowe pole ekstrakcji danych.

#### multi\_line

* **Znaczenie**: Wskazuje, czy reguła dotyczy tekstu wielowierszowego.
* **Rola**: Flaga logiczna.
* **Typowa zawartość**: `True` lub `False`.
* **Uwaga**: Przydatne przy obsłudze pól tekstowych wielowierszowych.

#### filterID1, filterID2, filterID3

* **Znaczenie**: Filtry lub warunki stosowania reguły.
* **Rola**: Pola opisowe lub warunkowe.
* **Typowa zawartość**: Prawdopodobnie ciągi znaków reprezentujące warunki filtrowania.
* **Uwaga**: Służą do doprecyzowania stosowania reguły na podstawie określonych warunków.

#### tfidf\_doc\_id, tfidf\_id

* **Znaczenie**: Identyfikatory związane z przetwarzaniem TF-IDF.
* **Rola**: Role zbliżone do klucza obcego lub identyfikatory.
* **Typowa zawartość**: Ciągi UUID.
* **Uwaga**: Prawdopodobnie związane z analizą tekstu i ekstrakcją cech.

#### valuePattern

* **Znaczenie**: Wzorzec regex do ekstrakcji wartości.
* **Rola**: Pole wzorca.
* **Typowa zawartość**: Wyrażenia regularne.
* **Uwaga**: Definiuje wzorzec używany do identyfikacji i wyodrębniania wartości.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Znaczenie**: Współrzędne definiujące obszar ograniczający (bounding box) do ekstrakcji.
* **Rola**: Pola współrzędnych.
* **Typowa zawartość**: Liczby całkowite reprezentujące położenie w pikselach.
* **Uwaga**: Definiują interesujący obszar w dokumencie do ekstrakcji danych.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Znaczenie**: Znormalizowane współrzędne do ekstrakcji.
* **Rola**: Pola współrzędnych.
* **Typowa zawartość**: Wartości numeryczne reprezentujące położenie proporcjonalne.
* **Uwaga**: Używane do definiowania obszarów niezależnie od rozdzielczości.

#### width, height

* **Znaczenie**: Wymiary obszaru zdefiniowanego przez współrzędne.
* **Rola**: Pola wymiarów.
* **Typowa zawartość**: Wartości całkowite.
* **Uwaga**: Pomagają określić rozmiar obszaru ekstrakcji.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Znaczenie**: Wzorce kontekstowe otaczające docelowe dane.
* **Rola**: Pola wzorców.
* **Typowa zawartość**: Wyrażenia regularne.
* **Uwaga**: Dostarczają kontekstu, gdzie dane znajdują się względem innego tekstu.

#### wordLeft, wordAbove

* **Znaczenie**: Konkretne słowa znajdujące się w pobliżu docelowych danych.
* **Rola**: Pola kontekstowe.
* **Typowa zawartość**: Konkretne słowa lub frazy.
* **Uwaga**: Pomagają doprecyzować wyszukiwanie docelowych danych na podstawie pobliskich słów.

#### ruleWeight

* **Znaczenie**: Waga lub priorytet reguły.
* **Rola**: Pole wagi lub priorytetu.
* **Typowa zawartość**: Wartości całkowite.
* **Uwaga**: Wyższe wartości mogą oznaczać wyższy priorytet lub większe znaczenie.

#### user\_id

* **Znaczenie**: Identyfikator użytkownika, który utworzył lub zmodyfikował regułę.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Wartości całkowite.
* **Uwaga**: Łączy regułę z konkretnym użytkownikiem.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z regułą.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciągi UUID.
* **Uwaga**: Powiązuje regułę z organizacją.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia reguły.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową.
* **Uwaga**: Przydatne do śledzenia historii utworzenia reguły.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji reguły.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową lub `None`.
* **Uwaga**: Rejestruje zmiany reguły w czasie.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy reguła została oznaczona jako usunięta.
* **Rola**: Flaga logiczna.
* **Typowa zawartość**: `True` lub `False`.
* **Uwaga**: Służy do miękkiego usuwania reguł.

#### is\_new

* **Znaczenie**: Wskazuje, czy reguła została niedawno utworzona.
* **Rola**: Flaga logiczna.
* **Typowa zawartość**: `True` lub `False`.
* **Uwaga**: Pomaga identyfikować niedawno dodane reguły.
