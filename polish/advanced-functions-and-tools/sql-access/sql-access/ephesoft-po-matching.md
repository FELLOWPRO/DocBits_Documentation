# Ephesoft PO matching

## Tabela `public.ephesoft_po_matching`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_id`: wewnętrzne
* `doc_type`: typ DOC
* `ephesoft_doc_id`: wewnętrzne
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.ephesoft_po_matching`

### Wprowadzenie

Tabela `public.ephesoft_po_matching` służy do przechowywania danych związanych z dopasowywaniem zamówień zakupu do dokumentów, takich jak faktury, przetwarzanych przez system Ephesoft, oraz do zarządzania nimi. Tabela rejestruje różne szczegóły dotyczące dokumentów, procesu ich ekstrakcji oraz statusu dopasowania do zamówień zakupu.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli, prawdopodobnie reprezentujący konkretny przetworzony dokument lub transakcję.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Uniwersalnie unikalny identyfikator (UUID) w formacie ciągu znaków, np. `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem lub transakcją.
* **Rola**: Klucz obcy, prawdopodobnie łączący z tabelą organizacji.
* **Typowa zawartość**: UUID w formacie ciągu znaków, np. `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Znaczenie**: Identyfikator dokumentu przetwarzanego przez system.
* **Rola**: Klucz obcy, łączący z tabelą dokumentów lub podobną.
* **Typowa zawartość**: UUID w formacie ciągu znaków, np. `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Znaczenie**: Typ przetwarzanego dokumentu, wskazujący jego charakter (np. INVOICE).
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków wskazujący typ dokumentu, np. `INVOICE`.

#### ephesoft\_doc\_id

* **Znaczenie**: Identyfikator używany przez system Ephesoft do śledzenia dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Krótki ciąg znaków, prawdopodobnie identyfikator, np. `DOC1`.

#### extracted\_data

* **Znaczenie**: Dane JSON zawierające informacje wyodrębnione z dokumentu, w tym pola, tabele i metadane.
* **Rola**: Pole przechowywania danych dla wyodrębnionej zawartości dokumentu.
* **Typowa zawartość**: Struktura JSON ze szczegółami, takimi jak typ dokumentu, pola, tabele i metadane.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika lub systemu, który utworzył rekord.
* **Rola**: Klucz obcy, prawdopodobnie łączący z tabelą użytkowników.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika, np. `1`.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole techniczne służące do śledzenia rekordu.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową, np. `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne służące do śledzenia rekordu.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową; może mieć wartość null, jeśli rekord nie był modyfikowany od utworzenia.

#### is\_deleted

* **Znaczenie**: Flaga wskazująca, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne służące do miękkiego usuwania.
* **Typowa zawartość**: Wartość logiczna, `true`, jeśli rekord jest usunięty, w przeciwnym razie `false`.
