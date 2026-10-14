# Documents

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `batch_id`: wewnętrzne
* `doc_path`: wewnętrzne
* `doc_type`: typ DOC
* `status`: wewnętrzne
* `message`: text
* `export_attempts`: integer
* `last_attempted_on`: timestamp with time zone
* `next_attempt_on`: timestamp with time zone
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `task_id`: wewnętrzne
* `filename`: wewnętrzne
* `assigned_on`: timestamp with time zone
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: text
* `doc_language`: język
* `is_trimmed`: boolean
* `doc_origin`: pochodzenie dokumentu
* `doc_locale`: ustawienia regionalne dokumentu
* `is_doc2landing_doc`: boolean
* `extraction_time`: double precision
* `export_time`: double precision
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: wewnętrzne
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: timestamp with time zone
* `lock_renewed_on`: timestamp with time zone
* `lock_key`: wewnętrzne
* `last_saved_by`: integer
* `last_saved_on`: timestamp with time zone
* `document_version`: integer
* `lock_session_key`: wewnętrzne
* `sub_org_id`: wewnętrzne
* `doc_source`: wewnętrzne
* `sub_doc_type`: wewnętrzne
* `assigned_to_group`: wewnętrzne
* `status_changed_on`: timestamp with time zone
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: wewnętrzne
* `doc_start_page`: integer
* `doc_classification_class`: wewnętrzne
* `celery_task_token`: wewnętrzne
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: timestamp with time zone
* `exception_details`: text
* `has_annotated_version`: boolean
* `po_match_status`: wewnętrzne
* `tr_ocr_extracted_data`: text
* `pending_workflow_execution`: boolean
* `extracted_document_id`: wewnętrzne
* `extracted_supplier_id`: wewnętrzne
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: wewnętrzne
* `extracted_data_basic`: jsonb
* `celery_task_queue`: wewnętrzne
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.documents`

## Wprowadzenie

Tabela `public.documents` służy do przechowywania metadanych i informacji o przetwarzaniu związanych z obsługą dokumentów w organizacji oraz do zarządzania nimi. Obejmuje to śledzenie statusu dokumentu, prób przetwarzania, języka i innych szczegółów administracyjnych. Tabela została zaprojektowana tak, aby wspierać klasyfikację dokumentów, przepływ pracy przetwarzania i przypisania do użytkowników, dzięki czemu stanowi integralną część systemu zarządzania dokumentami.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego dokumentu.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID reprezentujący dokument.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący organizację.

### batch_id
- **Znaczenie**: Identyfikator wsadu (batch), w którym przetworzono dokument.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący wsad.

### doc_path
- **Znaczenie**: Ścieżka pliku, w której przechowywany jest dokument.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Ścieżka do pliku dokumentu, np. `documents/{id}/{id}.pdf`.

### doc_type
- **Znaczenie**: Typ przechowywanego dokumentu (np. faktura).
- **Rola**: Klasyfikacja dokumentu.
- **Typowa zawartość**: Ciąg znaków, np. `INVOICE`.

### status
- **Znaczenie**: Bieżący status przetwarzania dokumentu.
- **Rola**: Wskaźnik przepływu pracy.
- **Typowa zawartość**: Ciąg znaków wskazujący status, np. `ready_for_validation`.

### message
- **Znaczenie**: Informacje o stanie przetwarzania dokumentu lub błędach.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Tekst opisujący błędy lub komunikaty związane z przetwarzaniem dokumentu.

### export_attempts
- **Znaczenie**: Liczba prób eksportu dokumentu.
- **Rola**: Śledzenie przetwarzania.
- **Typowa zawartość**: Liczba całkowita określająca liczbę prób eksportu.

### last_attempted_on
- **Znaczenie**: Znacznik czasu ostatniej próby przetworzenia lub wyeksportowania dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### next_attempt_on
- **Znaczenie**: Zaplanowany znacznik czasu następnej próby przetworzenia lub wyeksportowania dokumentu.
- **Rola**: Pole harmonogramu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### assigned_to
- **Znaczenie**: Identyfikator użytkownika przypisanego do tego dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył lub przesłał dokument.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia lub przesłania dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### is_deleted
- **Znaczenie**: Wskazuje, czy dokument został oznaczony jako usunięty.
- **Rola**: Flaga usunięcia logicznego.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### task_id
- **Znaczenie**: Identyfikator zadania powiązanego z przetwarzaniem dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący zadanie.

### filename
- **Znaczenie**: Oryginalna nazwa pliku dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Nazwa pliku, np. `document.pdf`.

### assigned_on
- **Znaczenie**: Znacznik czasu przypisania dokumentu do użytkownika.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### pages
- **Znaczenie**: Liczba stron w dokumencie.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita określająca liczbę stron.

### auto_processed
- **Znaczenie**: Wskazuje, czy dokument został przetworzony automatycznie.
- **Rola**: Flaga statusu przetwarzania.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### exception_info
- **Znaczenie**: Informacje o wyjątkach napotkanych podczas przetwarzania.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Tekst opisujący wyjątki przetwarzania.

### doc_language
- **Znaczenie**: Język treści dokumentu.
- **Rola**: Klasyfikacja językowa.
- **Typowa zawartość**: Kod języka ISO, np. `en`, `de`.

### is_trimmed
- **Znaczenie**: Wskazuje, czy dokument został przycięty.
- **Rola**: Flaga modyfikacji dokumentu.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### doc_origin
- **Znaczenie**: Pochodzenie dokumentu, potencjalnie wskazujące kraj lub system źródłowy.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Kod kraju lub identyfikator pochodzenia, np. `DE`.

### doc_locale
- **Znaczenie**: Ustawienia regionalne dokumentu, wskazujące język i region.
- **Rola**: Klasyfikacja ustawień regionalnych.
- **Typowa zawartość**: Ciąg ustawień regionalnych, np. `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Znaczenie**: Wskazuje, czy dokument jest powiązany z określonym przepływem przetwarzania (Doc2Landing).
- **Rola**: Flaga przepływu pracy.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### extraction_time
- **Znaczenie**: Czas potrzebny na wyodrębnienie danych z dokumentu.
- **Rola**: Metryka wydajności.
- **Typowa zawartość**: Wartość double precision reprezentująca czas ekstrakcji.

### export_time
- **Znaczenie**: Czas potrzebny na wyeksportowanie dokumentu.
- **Rola**: Metryka wydajności.
- **Typowa zawartość**: Wartość double precision reprezentująca czas eksportu.

### po_all_matched
- **Znaczenie**: Wskazuje, czy wszystkie zamówienia zakupu powiązane z dokumentem zostały dopasowane.
- **Rola**: Flaga statusu dopasowania.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### restart_allowed
- **Znaczenie**: Wskazuje, czy przetwarzanie dokumentu można uruchomić ponownie.
- **Rola**: Flaga sterowania przepływem pracy.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### table_version
- **Znaczenie**: Wersja struktury tabeli używanej dla dokumentu.
- **Rola**: Kontrola wersji.
- **Typowa zawartość**: Ciąg znaków wskazujący wersję, np. `v3`.

### force_ocr
- **Znaczenie**: Wskazuje, czy dla dokumentu wymuszono przetwarzanie OCR.
- **Rola**: Flaga sterowania przetwarzaniem.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### locked_by
- **Znaczenie**: Identyfikator użytkownika, który zablokował dokument do edycji.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### locked_on
- **Znaczenie**: Znacznik czasu zablokowania dokumentu do edycji.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### lock_renewed_on
- **Znaczenie**: Znacznik czasu ostatniego odnowienia blokady dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### lock_key
- **Znaczenie**: Klucz powiązany z blokadą dokumentu.
- **Rola**: Kontrola blokady.
- **Typowa zawartość**: Ciąg znaków reprezentujący klucz blokady.

### last_saved_by
- **Znaczenie**: Identyfikator użytkownika, który ostatni zapisał dokument.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### last_saved_on
- **Znaczenie**: Znacznik czasu ostatniego zapisu dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### document_version
- **Znaczenie**: Numer wersji dokumentu.
- **Rola**: Śledzenie wersji.
- **Typowa zawartość**: Liczba całkowita reprezentująca wersję dokumentu.

### lock_session_key
- **Znaczenie**: Klucz sesji powiązany z blokadą dokumentu.
- **Rola**: Kontrola blokady.
- **Typowa zawartość**: Ciąg znaków reprezentujący klucz sesji.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji powiązanej z dokumentem.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący podorganizację.

### doc_source
- **Znaczenie**: System źródłowy lub pochodzenie dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków wskazujący źródło, np. `doc2app`.

### sub_doc_type
- **Znaczenie**: Klasyfikacja podtypu dokumentu.
- **Rola**: Klasyfikacja dokumentu.
- **Typowa zawartość**: Ciąg znaków wskazujący podtyp.

### assigned_to_group
- **Znaczenie**: Identyfikator grupy, do której przypisano dokument.
- **Rola**: Śledzenie przypisań.
- **Typowa zawartość**: Ciąg UUID reprezentujący grupę.

### status_changed_on
- **Znaczenie**: Znacznik czasu ostatniej zmiany statusu dokumentu.
- **Rola**: Pole znacznika czasu.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### improve_quality
- **Znaczenie**: Wskazuje, czy do dokumentu stosowane są procesy poprawy jakości.
- **Rola**: Flaga kontroli jakości.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### priority
- **Znaczenie**: Priorytet przetwarzania dokumentu.
- **Rola**: Sterowanie przepływem pracy.
- **Typowa zawartość**: Liczba całkowita wskazująca poziom priorytetu.

### metadata_field
- **Znaczenie**: Pole JSON zawierające metadane związane z dokumentem.
- **Rola**: Przechowywanie metadanych.
- **Typowa zawartość**: Struktura JSON z różnymi polami metadanych.

### doc_classification_label
- **Znaczenie**: Etykieta wskazująca klasyfikację dokumentu.
- **Rola**: Etykieta klasyfikacji.
- **Typowa zawartość**: Ciąg znaków wskazujący klasyfikację, np. `INVOICE`.

### doc_start_page
- **Znaczenie**: Numer strony, na której zaczyna się treść dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita wskazująca stronę początkową.

### doc_classification_class
- **Znaczenie**: Klasa wskazująca szczegółową klasyfikację dokumentu.
- **Rola**: Szczegóły klasyfikacji.
- **Typowa zawartość**: Ciąg znaków wskazujący klasę klasyfikacji.

### celery_task_token
- **Znaczenie**: Token do śledzenia zadania Celery powiązanego z dokumentem.
- **Rola**: Śledzenie zadań.
- **Typowa zawartość**: Ciąg znaków reprezentujący token zadania.

### celery_task_attempt
- **Znaczenie**: Liczba prób wykonania zadania Celery.
- **Rola**: Śledzenie zadań.
- **Typowa zawartość**: Liczba całkowita określająca liczbę prób wykonania zadania.

### celery_task_priority
- **Znaczenie**: Poziom priorytetu zadania Celery.
- **Rola**: Sterowanie zadaniami.
- **Typowa zawartość**: Liczba całkowita wskazująca priorytet zadania.

### has_zugferd
- **Znaczenie**: Wskazuje, czy dokument jest w formacie ZUGFeRD.
- **Rola**: Wskaźnik formatu.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### has_peppol
- **Znaczenie**: Wskazuje, czy dokument jest w formacie PEPPOL.
- **Rola**: Wskaźnik formatu.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### timestamp_for_validation
- **Znaczenie**: Znacznik czasu zwalidowania dokumentu.
- **Rola**: Śledzenie walidacji.
- **Typowa zawartość**: Data i godzina ze strefą czasową.

### exception_details
- **Znaczenie**: Szczegółowe informacje o wyjątkach podczas przetwarzania.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Tekst ze szczegółami wyjątku.

### has_annotated_version
- **Znaczenie**: Wskazuje, czy istnieje wersja dokumentu z adnotacjami.
- **Rola**: Wskaźnik wersji.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### po_match_status
- **Znaczenie**: Status dopasowania zamówienia zakupu.
- **Rola**: Wskaźnik statusu dopasowania.
- **Typowa zawartość**: Ciąg znaków wskazujący status dopasowania.

### tr_ocr_extracted_data
- **Znaczenie**: Dane wyodrębnione z dokumentu za pomocą OCR.
- **Rola**: Przechowywanie danych.
- **Typowa zawartość**: Tekst zawierający wyodrębnione dane.

### pending_workflow_execution
- **Znaczenie**: Wskazuje, czy istnieją oczekujące wykonania przepływu pracy.
- **Rola**: Flaga statusu przepływu pracy.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### extracted_document_id
- **Znaczenie**: Identyfikator wyodrębnionego dokumentu.
- **Rola**: Śledzenie ekstrakcji.
- **Typowa zawartość**: Ciąg UUID reprezentujący wyodrębniony dokument.

### extracted_supplier_id
- **Znaczenie**: Identyfikator wyodrębnionego dostawcy.
- **Rola**: Śledzenie ekstrakcji.
- **Typowa zawartość**: Ciąg UUID reprezentujący wyodrębnionego dostawcę.

### classification_manually_corrected
- **Znaczenie**: Wskazuje, czy klasyfikacja dokumentu została poprawiona ręcznie.
- **Rola**: Flaga statusu klasyfikacji.
- **Typowa zawartość**: Wartość logiczna (True lub False).

### supplier_as_org_id
- **Znaczenie**: Identyfikator dostawcy traktowanego jako organizacja.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący organizację dostawcy.

### extracted_data_basic
- **Znaczenie**: Podstawowe wyodrębnione dane w formacie JSONB.
- **Rola**: Przechowywanie danych.
- **Typowa zawartość**: Struktura JSONB z polami wyodrębnionych danych.

### celery_task_queue
- **Znaczenie**: Nazwa kolejki zadań Celery.
- **Rola**: Zarządzanie zadaniami.
- **Typowa zawartość**: Ciąg znaków wskazujący nazwę kolejki.

### extracted_data
- **Znaczenie**: Dane wyodrębnione z dokumentu w formacie JSONB.
- **Rola**: Przechowywanie danych.
- **Typowa zawartość**: Struktura JSONB z polami wyodrębnionych danych.

### extracted_data_jsonb
- **Znaczenie**: Pole JSONB zawierające szczegółowe wyodrębnione dane.
- **Rola**: Przechowywanie danych.
- **Typowa zawartość**: Struktura JSONB z polami wyodrębnionych danych.

### warnings
- **Znaczenie**: Ostrzeżenia związane z przetwarzaniem dokumentu, przechowywane w formacie JSONB.
- **Rola**: Przechowywanie ostrzeżeń.
- **Typowa zawartość**: Struktura JSONB z komunikatami ostrzeżeń.
```
