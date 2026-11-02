# Pole

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_type`: internal
* `title`: internal
* `translation_key`: internal
* `hide_label`: boolean
* `input_type`: internal
* `input_size`: internal
* `icon_left`: internal
* `icon_right`: internal
* `icon_above`: internal
* `group_id`: internal
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: internal
* `fuzzy_field`: internal
* `fuzzy_primary_field`: boolean
* `label_align`: internal
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: internal
* `coordinates`: internal
* `normalized_coordinates`: internal
* `threshold`: internal
* `reference_point`: internal
* `checkbox_group`: internal
* `list_of_values`: internal
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `costing_element`: internal
* `erp_field_name`: internal

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.field`

## Wprowadzenie

Tabela `public.field` służy prawdopodobnie do zarządzania metadanymi i konfiguracją różnych pól powiązanych z dokumentami, najpewniej w obszarze ubezpieczeń. Każdy wiersz tabeli wydaje się reprezentować konfigurację konkretnego pola, w tym jego typ, etykietę, ustawienia widoczności oraz inne właściwości określające sposób prezentacji i przetwarzania pola.

## Kolumny

### id
- **Znaczenie**: Unikalny identyfikator każdej konfiguracji pola.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID, który jednoznacznie identyfikuje każdy wpis w tabeli.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z konfiguracją pola.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: UUID odnoszący się do organizacji.

### doc_type
- **Znaczenie**: Określa typ dokumentu, z którym powiązane jest pole.
- **Rola**: Prawdopodobnie klucz obcy lub identyfikator kategorii.
- **Typowa zawartość**: Ciąg w formacie `INSURANCE_DOCUMENTS_<UUID>` wskazujący typ dokumentu.

### is_sub_doc_type_field
- **Znaczenie**: Wskazuje, czy pole jest podtypem typu dokumentu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### profile
- **Znaczenie**: Potencjalnie definiuje profil lub zakres pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Często puste lub krótki opis tekstowy.

### field_name
- **Znaczenie**: Wewnętrzna nazwa pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący nazwę pola w kontekście technicznym (np. `Schadennummer`).

### field_type
- **Znaczenie**: Określa typ danych przechowywanych w polu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Opisowe ciągi znaków, takie jak `STRING`, `AMOUNT`.

### title
- **Znaczenie**: Wyświetlany tytuł pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg wielkimi literami używany do wyświetlania etykiety pola.

### translation_key
- **Znaczenie**: Klucz tłumaczenia na różne języki.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Ciąg małymi literami reprezentujący klucz tłumaczenia.

### hide_label
- **Znaczenie**: Wskazuje, czy etykieta pola ma być ukryta w interfejsie użytkownika.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### input_type
- **Znaczenie**: Określa sposób wprowadzania danych w polu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Może być puste lub zawierać ciągi znaków definiujące typ danych wejściowych.

### input_size
- **Znaczenie**: Określa rozmiar pola wejściowego.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Może być puste lub zawierać ciągi znaków definiujące rozmiar pola.

### icon_left
- **Znaczenie**: Ikona wyświetlana po lewej stronie pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera identyfikatory ikon.

### icon_right
- **Znaczenie**: Ikona wyświetlana po prawej stronie pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera identyfikatory ikon.

### icon_above
- **Znaczenie**: Ikona wyświetlana nad polem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera identyfikatory ikon.

### group_id
- **Znaczenie**: Identyfikator grupy pól, do której należy to pole.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: UUID odnoszący się do grupy pól.

### row_order
- **Znaczenie**: Określa kolejność pola na liście lub w formularzu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Liczba całkowita wskazująca pozycję.

### sort_order
- **Znaczenie**: Określa kolejność sortowania pola.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Liczba całkowita definiująca priorytet sortowania.

### fuzzy_name
- **Znaczenie**: Alternatywna nazwa używana w dopasowywaniu rozmytym.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Często puste lub zawiera ciąg znaków używany do dopasowywania.

### fuzzy_field
- **Znaczenie**: Określa, czy pole jest używane w dopasowywaniu rozmytym.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera ciąg znaków.

### fuzzy_primary_field
- **Znaczenie**: Wskazuje, czy jest to główne pole dopasowywania rozmytego.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### label_align
- **Znaczenie**: Ustawienie wyrównania etykiety pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Często puste lub zawiera informację o wyrównaniu (np. left, right, center).

### calculation_formula
- **Znaczenie**: Formuła używana w obliczeniach dotyczących pola.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Tekst zawierający formułę lub logikę obliczeń.

### clean_field
- **Znaczenie**: Wskazuje, czy dane pola mają podlegać czyszczeniu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### alphanumeric_field
- **Znaczenie**: Określa, czy pole ma akceptować wyłącznie znaki alfanumeryczne.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### placeholder
- **Znaczenie**: Tekst zastępczy pola wejściowego.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Często puste lub zawiera tekst podpowiedzi.

### coordinates
- **Znaczenie**: Dane współrzędnych powiązane z polem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera informacje o współrzędnych.

### normalized_coordinates
- **Znaczenie**: Znormalizowana wersja współrzędnych zapewniająca spójność.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera znormalizowane dane współrzędnych.

### threshold
- **Znaczenie**: Wartość progowa związana z walidacją lub przetwarzaniem pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera wartości progowe.

### reference_point
- **Znaczenie**: Punkt odniesienia używany w obliczeniach lub pozycjonowaniu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Często puste lub zawiera dane punktu odniesienia.

### checkbox_group
- **Znaczenie**: Identyfikator grupujący pola wyboru (checkboxy).
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera identyfikatory grup.

### list_of_values
- **Znaczenie**: Określa listę dozwolonych wartości pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera listę wartości.

### enforce_list_of_values
- **Znaczenie**: Wskazuje, czy lista wartości ma być ściśle egzekwowana.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył wpis pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita odnosząca się do identyfikatora użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia pola.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Data i godzina w UTC.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji pola.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Data i godzina w UTC.

### is_deleted
- **Znaczenie**: Wskazuje, czy pole zostało oznaczone jako usunięte.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### costing_element
- **Znaczenie**: Element kosztowy powiązany z polem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera identyfikatory elementów kosztowych.

### erp_field_name
- **Znaczenie**: Nazwa pola używana w systemach ERP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj puste lub zawiera nazwy pól specyficzne dla ERP.

Niniejsza dokumentacja zawiera szczegółowy przegląd struktury i przeznaczenia każdej kolumny w tabeli `public.field`. Stanowi przewodnik dla programistów, który pomaga zrozumieć model danych i jego zastosowanie w systemie.
```
