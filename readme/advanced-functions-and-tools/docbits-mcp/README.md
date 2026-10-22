# DocBits MCP

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/docbits-mcp-admin/v1/pl.mp4" %}

DocBits udostępnia serwer **Model Context Protocol (MCP)**, który pozwala asystentom AI pracować z Twoimi dokumentami, ekstrakcją, wyszukiwaniem, analityką i konfiguracją — bezpośrednio z czatu lub sesji programistycznej. Połączyć się może dowolny klient zgodny z MCP: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** lub dowolna niestandardowa integracja.

Serwer jest zamontowany w API DocBits pod adresem `/v3/mcp` i obejmuje zakresem Twoją organizację — każde wywołanie jest wykonywane z uprawnieniami użytkownika (lub klucza API), który nawiązał połączenie.

{% hint style="info" %}
**Endpoint — użyj swojego regionu (EU lub US):**

- Produkcja (EU) — `https://eu.api.docbits.com/v3/mcp`
- Produkcja (US) — `https://us.api.docbits.com/v3/mcp`

Pełną macierz hostów oraz sposób logowania przez OAuth znajdziesz w artykule [Konfiguracja](setup-and-configuration.md).
{% endhint %}

## Co możesz zrobić?

Dzięki DocBits MCP asystent może w Twoim imieniu:

- **Znajdować i czytać dokumenty** — wyświetlać listę, wyszukiwać (pełnotekstowo i po polach), otwierać dokument, odczytywać jego status, logi, obrazy stron i podgląd eksportu
- **Pracować na wyodrębnionych danych** — odczytywać wyodrębnione pola i tabele, poprawiać wartości pól, wyodrębniać tabele za pomocą AI, walidować, zatwierdzać i eksportować do Twojego ERP
- **Odpytywać pulpit** — uruchamiać zapytania do pulpitu w języku naturalnym, porównywać tryby wyszukiwania i sprawdzać możliwości wyszukiwania
- **Pobierać analitykę** — podsumowania dla zarządu, wskaźniki powodzenia, trendy wolumenu, najczęstsze typy dokumentów i szczegóły oczekujących zadań
- **Obsługiwać e-faktury (eDocs)** — wyświetlać typy dokumentów elektronicznych, testować i weryfikować e-dokumenty, zarządzać niestandardowymi atrybutami ekstrakcji
- **Zarządzać danymi podstawowymi** — dodawać lub aktualizować dane podstawowe dostawców, uruchamiać wyszukiwanie dostawców, importować BOD faktur dostawców, utrzymywać mapowania warunków płatności i rabatów
- **Odczytywać i zmieniać konfigurację** — preferencje organizacji, typy dokumentów, ustawienia pól, użytkowników i pamięć podręczną
- **Sprawdzać stan** — kondycja API i Celery, bieżący użytkownik i informacje o API

## Przegląd narzędzi

DocBits MCP grupuje znacznie ponad sto narzędzi w poniższych kategoriach (dokładna liczba rośnie z każdym wydaniem; Twój asystent wyświetla aktualny zestaw). Większość odpowiada istniejącym endpointom REST DocBits — szczegóły żądań i odpowiedzi znajdziesz w [Referencji API](../../README.md). Asystent automatycznie wybiera właściwe narzędzie na podstawie Twojej prośby; tabele stanowią mapę dostępnych możliwości.

### Dokumenty i przetwarzanie

| Narzędzie | Opis |
|------|-------------|
| `list_documents` | Wyświetla dokumenty organizacji (z możliwością filtrowania) |
| `get_document` / `get_document_by_name` | Otwiera dokument według ID lub nazwy pliku |
| `upload_document` | Przesyła nowy dokument do przetworzenia |
| `get_document_status` | Bieżący status dokumentu w potoku |
| `get_document_logs` | Wpisy logu przetwarzania dokumentu |
| `query_org_logs` | Przegląda stronami logi usług organizacji |
| `restart_document` | Ponownie uruchamia potok przetwarzania |
| `delete_document` | Usuwa dokument |
| `get_pending_documents_count` | Ile dokumentów czeka na walidację |

### Ekstrakcja i walidacja

| Narzędzie | Opis |
|------|-------------|
| `get_extracted_fields` / `get_document_fields` | Odczytuje wyodrębnione pola nagłówka |
| `get_extracted_tables` | Odczytuje wyodrębnione tabele pozycji |
| `get_document_for_validation` / `get_next_document` | Otwiera dokument tak, jak robi to ekran walidacji; pobiera kolejny z kolejki |
| `get_page_image` | Obraz strony do kontroli wizualnej |
| `update_document_fields` | Poprawia lub ustawia wartości pól |
| `validate_document` | Uruchamia reguły walidacji pól |
| `approve_document` | Zatwierdza zwalidowany dokument |
| `validate_and_export` | Waliduje, a następnie eksportuje do ERP |
| `get_export_preview` | Podgląd ładunku eksportu przed wysłaniem |

### Ekstrakcja tabel

Wszystko, co ekran walidacji i ustawienia kolumn tabeli potrafią zrobić z tabelami pozycji. Narzędzia konfiguracyjne zmieniają typy dokumentów organizacji; narzędzia ekstrakcji i korekty działają na jednym dokumencie; narzędzia reguł zapisują to, czego DocBits nauczył się o danym dostawcy.

| Narzędzie | Opis |
|------|-------------|
| `list_tables` / `get_table_config` | Tabele i front typu dokumentu wraz z flagami Wymagane / Tylko do odczytu / Ukryte / Użyj AI |
| `create_table` | Dodaje drugą tabelę pozycji do typu dokumentu |
| `add_table_column` / `delete_table_column` | Dodaje kolumnę tabeli lub ją miękko usuwa |
| `set_ai_table_config` | Przełącza ekstrakcję tabel AI, tryb wizyjny i strukturalny dla organizacji |
| `extract_table_ai` | Uruchamia ekstrakcję tabel AI na dokumencie (tekst lub obraz) |
| `extract_table_only` | Wyodrębnia tabelę bez dotykania pól nagłówka (reguły lub AI) |
| `extract_table_nonai` | Ekstrakcja oparta na regułach ze współrzędnych, które przekażesz — pierwszy krok trenowania tabeli przez API |
| `apply_ai_table_formatting` / `apply_table_feedback` | Zmienia format tabeli AI: ukrywa kolumny, przemapowuje, stosuje opinię użytkownika |
| `remap_table_columns` | Zmienia, która wyodrębniona kolumna zasila którą skonfigurowaną kolumnę |
| `save_table_rules` / `save_table_training_rules` | Zapisuje reguły współrzędnych lub reguły formatowania AI dla dostawcy, aby kolejny dokument był wyodrębniany tak samo |
| `delete_table_training_rules` | Usuwa zapisane reguły dostawcy; kolejny dokument wraca do AI |
| `get_table_extraction_report` / `list_table_report_suppliers` | Raport dla poszczególnych dostawców o sposobie ekstrakcji tabel (reguły, AI, model) wraz z podglądem |
| `compare_table_extraction_models` | Wyodrębnia ten sam dokument dwoma poziomami AI i porównuje tabele |

### Wyszukiwanie i pulpit

| Narzędzie | Opis |
|------|-------------|
| `search_documents` / `search_documents_by_name` | Wyszukiwanie pełnotekstowe i po nazwie pliku |
| `query_document_dashboard` | Zapytanie do pulpitu w języku naturalnym |
| `explain_document_dashboard_query` | Pokazuje, jak zapytanie zostało zinterpretowane |
| `get_search_capabilities` | Które funkcje wyszukiwania są włączone w organizacji |
| `compare_search_modes` | Porównuje wyniki słów kluczowych i wektorowe |
| `diagnose_document_search` | Dlaczego dokument pojawia się lub nie pojawia się dla danego wyszukiwania — klasyczne i pełnotekstowe obok siebie |
| `inspect_document_search_index` | Czy dokument znajduje się w indeksach dokumentów, tekstu i wektorów oraz kiedy każdy z nich został zapisany |
| `get_dashboard_columns` / `set_dashboard_columns` | Odczytuje lub zmienia kolumny wyświetlane na pulpicie dokumentów |

### Touchless Intelligence

Dlaczego dokumenty wymagają udziału człowieka i co zmienić, aby wymagało go mniej z nich. Wszystkie narzędzia tutaj są tylko do odczytu, z wyjątkiem `touchless_apply_change`, które zapisuje dokładnie jedną zmianę ustawienia, wcześniej wyświetloną w podglądzie.

| Narzędzie | Opis |
|------|-------------|
| `touchless_get_summary` | Karta wyników touchless organizacji: ile dokumentów przeszło bez ingerencji, według okresu i segmentu |
| `touchless_list_segments` | Wartości, według których możesz segmentować liczby (dostawca, typ dokumentu, …) |
| `touchless_rank_supplier_opportunities` | Dostawcy uszeregowani według tego, ile pracy ręcznej powodują |
| `touchless_diagnose_supplier` | Dlaczego dokumenty jednego dostawcy zatrzymują się u człowieka |
| `touchless_get_issue_cluster` | Jeden powtarzający się problem i dokumenty, których dotknął |
| `touchless_get_document_trace` | Pełna historia touchless jednego dokumentu |
| `touchless_explain_pipeline` | Gdzie w potoku zatrzymał się dokument lub klaster |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Dlaczego dopasowanie PO się powiodło lub nie, wraz z zestawem reguł i obliczeniami tolerancji |
| `touchless_get_recommendations` | Co zmienić, a nie tylko co poszło nie tak |
| `touchless_list_change_proposals` | Zmiany ustawień, które zwiększyłyby wskaźnik touchless, wraz z oczekiwanym wzrostem |
| `touchless_preview_change` | Próbne uruchomienie jednej propozycji: nic nie jest zapisywane |
| `touchless_apply_change` | Stosuje jedną wyświetloną w podglądzie propozycję w organizacji |
| `touchless_verify_change` | Ile okazała się warta wprowadzona zmiana |

### Analityka i BI

| Narzędzie | Opis |
|------|-------------|
| `get_executive_summary` | Najważniejsze KPI organizacji |
| `get_success_rates` | Wskaźniki touchless / straight-through |
| `get_volume_trends` | Wolumen dokumentów w czasie |
| `get_top_document_types` | Najczęstsze typy dokumentów |
| `get_pending_tasks_detail` | Szczegóły zaległej pracy |

### Dokumenty elektroniczne (e-faktury)

| Narzędzie | Opis |
|------|-------------|
| `list_electronic_document_types` | Obsługiwane formaty e-faktur (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document` | Klasyfikuje i wyodrębnia przykładowy e-dokument |
| `verify_electronic_documents` / `validate_all_edocs` | Weryfikuje ekstrakcję e-dokumentów |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Zarządza niestandardowymi atrybutami ekstrakcji |

### Dane podstawowe

| Narzędzie | Opis |
|------|-------------|
| `upsert_vendor_master_data` | Tworzy lub aktualizuje dane podstawowe dostawcy |
| `trigger_supplier_lookup` | Wzbogaca dokument o dane podstawowe dostawcy |
| `import_supplier_invoice_bod` | Importuje BOD faktury dostawcy |
| `get_supplier_invoice` | Odczytuje zapisane dane faktury dostawcy (BOD) według faktury, dostawcy lub dokumentu |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Utrzymuje mapowania obliczeń |

### Konfiguracja, administracja i stan

| Narzędzie | Opis |
|------|-------------|
| `get_preferences` / `get_preference` / `set_preference` | Odczytuje i zmienia preferencje organizacji |
| `list_document_types` / `get_field_settings` | Sprawdza konfigurację typów dokumentów i pól |
| `list_users` | Wyświetla użytkowników organizacji |
| `clear_org_cache` | Czyści pamięć podręczną konfiguracji |
| `check_api_health` / `check_celery_health` | Stan usług |
| `get_current_user` / `get_api_info` | Tożsamość i metadane API |

## Następne kroki

- [**Konfiguracja**](setup-and-configuration.md) — połącz Claude Code, Gemini CLI lub Codex (przez logowanie lub klucz API)
- [**Przykłady**](examples.md) — rzeczywiste zadania, o które klienci proszą asystenta
- [**Dokumenty elektroniczne (eDocs)**](../edocs-mcp/README.md) — szczegółowe omówienie narzędzi eDoc: sprawdzanie i testowanie przetwarzania e-faktur oraz zarządzanie niestandardowymi regułami ekstrakcji i podglądu (ten sam endpoint, to samo logowanie)
- [**Przepływy pracy i karty (DocFlow)**](../docflow-mcp/README.md) — zarządzanie zaawansowanymi przepływami pracy i kartami partnerskimi

{% hint style="info" %}
**Jeden MCP do wszystkiego.** Narzędzia eDoc oraz **Przepływy pracy i karty (DocFlow)** działają na **tym samym** endpoincie `api.docbits.com/v3/mcp` z tym samym logowaniem DocBits. Narzędzia DocFlow pojawiają się tam z prefiksem `docflow_` (na przykład `docflow_list_workflows`); strona DocFlow opisuje je pod ich nazwami bez prefiksu. Bezpośrednie połączenie z hostem DocFlow nadal jest możliwe, ale nie jest już konieczne.
{% endhint %}

[Konfigurowanie DocBits przez Claude lub Codex](configuration-with-claude-or-codex.md): połączenie, prompty, podglądy, wersjonowane zmiany, kontrole i cofnięcie.
