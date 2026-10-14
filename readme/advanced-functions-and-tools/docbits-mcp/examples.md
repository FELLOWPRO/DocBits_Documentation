# Przykłady

Po połączeniu DocBits MCP (zobacz [Konfiguracja](setup-and-configuration.md)) rozmawiasz z asystentem zwykłym językiem — to on dobiera dla Ciebie właściwe narzędzia DocBits. Poniżej znajdziesz realistyczne zadania, które wykonują klienci, wraz z przykładowym poleceniem, które możesz wpisać, i narzędziami używanymi przez asystenta w tle.

{% hint style="info" %}
Działa to tak samo w Claude Code, Gemini CLI i Codex — polecenia są pisane językiem naturalnym, a nie komendami.
{% endhint %}

## Przegląd kolejki pracy

> *"Ile dokumentów czeka na walidację i jakiego są typu?"*

Używa `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. Asystent podsumowuje zaległości i może zajrzeć do dowolnego dokumentu.

> *"Pokaż mi faktury, które dziś zakończyły się błędem, i powiedz, dlaczego."*

Używa `search_documents` / `query_document_dashboard` oraz `get_document_logs`, aby znaleźć dokumenty z błędem i wyjaśnić jego przyczynę na podstawie logów.

## Znajdowanie i sprawdzanie dokumentu

> *"Otwórz fakturę INV-2026-00231 i pokaż wyodrębnione pola oraz pozycje."*

Używa `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. Asystent zwraca dane nagłówka i tabelę, a jeśli chcesz zobaczyć źródło, może pobrać obraz strony za pomocą `get_page_image`.

> *"Wyszukaj wszystkie dokumenty od dostawcy 'ACME GmbH' z zeszłego miesiąca powyżej 10 000 €."*

Używa `search_documents` / `query_document_dashboard` z filtrami po polach.

## Poprawianie i zatwierdzanie

> *"W dokumencie 84213 ustaw numer PO na 4500098123 i termin płatności na 2026-07-15, a następnie go zwaliduj."*

Używa `update_document_fields`, a potem `validate_document`. Asystent zgłasza wszelkie błędy walidacji, abyś mógł je poprawić.

> *"Zwaliduj i wyeksportuj dokument 84213 do ERP, ale najpierw pokaż mi podgląd eksportu."*

Używa `get_export_preview`, a po Twoim potwierdzeniu `validate_and_export`.

## Naprawa ekstrakcji tabeli

> *"W tabeli pozycji tego dokumentu dostawy brakuje dwóch wierszy — wyodrębnij ją ponownie za pomocą AI, ukryj kolumnę *Charges* i zapamiętaj to dla tego dostawcy."*

Używa `extract_table_ai`, aby ponownie uruchomić tabelę AI na dokumencie, `apply_ai_table_formatting`, aby ukryć kolumnę, oraz `save_table_training_rules`, aby zapisać wynik dla dostawcy; kolejny dokument dostawy od niego będzie wyodrębniany w ten sam sposób. `get_extracted_tables` pokazuje końcową tabelę. Przydatne w przypadku dokumentów, w których ekstrakcja oparta na regułach pominęła wiersze.

## Analityka i raportowanie

> *"Przygotuj podsumowanie dla zarządu za ten miesiąc: trend wolumenu, wskaźnik touchless i 5 najczęstszych typów dokumentów."*

Używa `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Świetne do szybkiej informacji dla kierownictwa bez otwierania pulpitu.

## E-fakturowanie (eDocs)

> *"Jakie formaty faktur elektronicznych mamy włączone i czy ten plik ZUGFeRD jest wyodrębniany poprawnie?"*

Używa `list_electronic_document_types` oraz `test_electronic_document`, a następnie `verify_electronic_documents`, aby potwierdzić wyodrębnione pola.

## Dane podstawowe i wzbogacanie danych dostawców

> *"Dodaj nowego dostawcę (nazwa, NIP/VAT, IBAN) do danych podstawowych, a potem ponownie uruchom wyszukiwanie dostawcy dla dokumentu 84500."*

Używa `upsert_vendor_master_data` oraz `trigger_supplier_lookup`.

## Zmiany konfiguracji

> *"Włącz ekstrakcję kodów QR dla naszej organizacji i potwierdź, że preferencja jest ustawiona."*

Używa `set_preference` (które automatycznie czyści pamięć podręczną) oraz `get_preference` do potwierdzenia.

> *"Wyświetl nasze typy dokumentów i pokaż ustawienia pól dla 'Invoice'."*

Używa `list_document_types` oraz `get_field_settings`.

## Stan i diagnostyka

> *"Czy API DocBits i proces roboczy przetwarzania działają teraz poprawnie? Jako kto jestem połączony?"*

Używa `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Wskazówki

- **Precyzyjnie wskaż dokument** — ID lub dokładna nazwa pliku działa najszybciej; w przeciwnym razie asystent najpierw wyszuka dokument.
- **Poproś o podgląd przed eksportem** — `get_export_preview` pozwala potwierdzić ładunek dla ERP, zanim `validate_and_export` go wyśle.
- **Obowiązują uprawnienia** — asystent może zrobić tylko to, na co pozwala Twój użytkownik DocBits lub klucz API. Zatwierdzanie i eksport respektują Twoją rolę i ACL.
- **Ostrożność na produkcji** — MCP działa na rzeczywistych danych. W środowiskach klienta/produkcyjnych preferuj akcje odczytu i podglądu oraz potwierdzaj przed zatwierdzeniem, eksportem lub usunięciem.
