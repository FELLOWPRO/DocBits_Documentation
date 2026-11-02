# Wyzwalacz stanu dokumentu

## Tabela `public.document_status_trigger`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `trigger_doc_type`: wewnętrzne
* `trigger_doc_status`: wewnętrzne
* `trigger_url`: wewnętrzne
* `is_active`: boolean
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.document_status_trigger`

### Wprowadzenie

Tabela `public.document_status_trigger` służy do zarządzania statusem dokumentów w organizacji i jego śledzenia. Tabela ta obsługuje wyzwalacze związane z przetwarzaniem dokumentów, prawdopodobnie w systemie przepływów pracy. Zawiera informacje o typach dokumentów i zmianach ich statusu, potencjalnie uruchamiając działania lub przepływy pracy za pośrednictwem określonych adresów URL.

### Opis kolumn

#### id

* **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID, np. `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Znaczenie**: Reprezentuje unikalny identyfikator organizacji.
* **Rola**: Klucz obcy, łączący z jednostką organizacji.
* **Typowa zawartość**: Ciąg UUID, np. `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Znaczenie**: Określa typ dokumentu powiązanego z wyzwalaczem.
* **Rola**: Pole opisowe wskazujące typ dokumentu.
* **Typowa zawartość**: Nazwy typów dokumentów, np. `INVOICE`.

#### trigger\_doc\_status

* **Znaczenie**: Oznacza konkretny status dokumentu, który aktywuje wyzwalacz.
* **Rola**: Pole opisowe określające status dokumentu.
* **Typowa zawartość**: Opisy statusów, np. `approved_pending_second_approval`.

#### trigger\_url

* **Znaczenie**: Adres URL wywoływany, gdy status dokumentu spełnia określone warunki.
* **Rola**: Pole techniczne do automatyzacji przepływów pracy.
* **Typowa zawartość**: Adresy URL, np. `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Znaczenie**: Wskazuje, czy wyzwalacz jest aktualnie aktywny.
* **Rola**: Pole techniczne do zarządzania stanami wyzwalacza.
* **Typowa zawartość**: Wartości logiczne, `True` lub `False`.

#### created\_by

* **Znaczenie**: Identyfikuje użytkownika, który utworzył rekord.
* **Rola**: Klucz obcy do jednostki użytkownika.
* **Typowa zawartość**: Całkowite identyfikatory użytkowników, np. `1`.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole techniczne do audytu i śledzenia zmian.
* **Typowa zawartość**: Znaczniki czasu ze strefą czasową, np. `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne do audytu i śledzenia zmian.
* **Typowa zawartość**: Znaczniki czasu ze strefą czasową; mogą mieć wartość `None`, jeśli rekord nie był modyfikowany.

#### is\_deleted

* **Znaczenie**: Oznacza, czy rekord jest uznawany za usunięty lub nieaktywny.
* **Rola**: Pole techniczne służące do miękkiego usuwania.
* **Typowa zawartość**: Wartości logiczne, `True` lub `False`.

Tabela ta zapewnia uporządkowane podejście do zarządzania statusami dokumentów i powiązanymi wyzwalaczami w systemie przepływów pracy organizacji, dzięki czemu działania mogą być podejmowane automatycznie w miarę przechodzenia dokumentów przez kolejne stany.
