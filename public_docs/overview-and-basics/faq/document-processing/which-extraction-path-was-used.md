# Która ścieżka ekstrakcji została użyta?

Na pytanie "Dlaczego ta tabela tak wygląda?" odpowiada ustalenie, *co* DocBits zrobił dla tego dokumentu: zapisane reguły, tabela AI, który poziom AI i w którym miejscu coś poszło nie tak. Ta strona to lista kontrolna, z której korzystają wsparcie i partnerzy przed zmianą jakiejkolwiek konfiguracji.

## 1. Spójrz na zakładki na ekranie walidacji

Otwórz dokument i spójrz na zakładki nad tabelą pozycji:

| Co widzisz | Ścieżka |
|---|---|
| Wiersze w zakładce **Extracted table** | Ścieżka oparta na regułach. Dostawca ma wytrenowaną tabelę; wiersze pochodzą z zapisanych reguł współrzędnych, a AI nie brało udziału (z wyjątkiem kolumn oznaczonych *Use AI*). |
| Wiersze w zakładce **AI Extracted table**, pole *Tags* poniżej | Ścieżka AI. Żadne zapisane reguły nie pasowały; wiersze utworzyła ekstrakcja tabeli AI, używając poziomu AI organizacji albo poziomu ustawionego dla tego dostawcy w *More settings* → *Supplier-Based AI Model*. |
| Podpowiedź *AI table not found* na zakładce AI | Ścieżka AI została uruchomiona i nie zwróciła niczego dla tego dokumentu. |
| Brak jakichkolwiek zakładek tabeli | Oba ustawienia tabeli są wyłączone dla organizacji, nic nie wyodrębniło tabeli. |
| *No line items yet* | Ścieżka została uruchomiona, ale nie znalazła wierszy (brak czytelnego tekstu, brak tabeli na stronie albo reguły nie pasowały do tego układu). |

Pola nagłówka mają własną etykietę źródła obok wartości: *Extracted using AI*, *Learned from validated AI extraction*, *Extracted using saved rules (FELLOW_KV2)*, *Extracted from electronic document*, *Calculated from vendor master data*. Te etykiety opisują pole nagłówka, nie tabelę.

## 2. Sprawdź konfigurację dostawcy

* **Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja → Model AI**: tabela pod selektorem wymienia każdego dostawcę z zapisanym modelem lub szkoleniem. Dostawca na tej liście z *danymi szkoleniowymi* ma zapisane reguły; *zresetowanie danych szkoleniowych* je usuwa.
* **Ustawienia → Przetwarzanie dokumentów → Ustawienia OCR**: opcje *Use E-Text if available* i *Use AI data for tables* zmieniają tekst, który widzi ekstrakcja. Dostawca może nadpisać E-Text w *More settings* na ekranie walidacji.
* **Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli**: flagi ukryta, wymagana i *Use AI*. Ukryta kolumna nigdy nie jest wypełniana; kolumnę *Use AI* wypełnia AI nawet u dostawców z regułami.

## 3. Odtwórz bez interfejsu (API / MCP)

Z dostępem do API lub MCP możesz zadać te same pytania programowo:

| Pytanie | Narzędzie |
|---|---|
| Czy tę tabelę utworzyło AI? | `get_extracted_tables(doc_id)`: każda tabela ma pole `is_ai_table: true/false`. |
| Co dają reguły, a co daje AI? | `get_table_extraction_report(doc_id, mode="nonai")` i ponownie z `mode="ai"`; raport pokazuje skonfigurowaną strukturę, wyodrębnione wiersze i podgląd strony dla każdej ścieżki. Porównaj oba wyniki. |
| Które kolumny są skonfigurowane i z jakimi flagami? | `get_table_config(doc_type)` |
| Czy poziom AI ma znaczenie? | `compare_table_extraction_models(doc_id)`, uruchamia dwa poziomy na tym samym dokumencie (wymaga dokumentu z numerem dostawcy). |
| Powtórz ekstrakcję na tym dokumencie | `extract_table_ai(doc_id)` (AI) albo `restart_document(doc_id)` (cały potok). |
| Co potok zapisał w logach dla tego dokumentu? | `get_document_logs(doc_id)` |

Narzędzia DocBits MCP są opisane na stronie DocBits MCP w angielskiej wersji dokumentacji.

## 4. Przeczytaj logi

**Ustawienia → Ustawienia logów** (Activity Logging) pokazuje zdarzenia wszystkich usług. W przypadku pytania o tabelę:

* Filtruj po nazwie pliku lub ID dokumentu w polu *Search logs*.
* Użyj filtra *Service*: sama ekstrakcja działa w usłudze ekstrakcji i w workerach Celery, a nie w usłudze `api`. Jeśli widzisz tylko wiersze `api`, rozszerz filtr.
* Normalny przebieg zapisuje kolejno: dokument odebrany → OCR / E-Text → klasyfikacja → ekstrakcja pól → ekstrakcja tabeli (wyszukanie reguł, a gdy żadne nie pasują, AI) → walidacja → zmiana statusu. Krok, którego brakuje lub który zgłasza błąd, to ten, któremu trzeba się przyjrzeć.

## 5. Zdecyduj: konfiguracja, dane czy błąd

| Objaw | Najbardziej prawdopodobne | Następny krok |
|---|---|---|
| Tabela poprawna u dostawcy A, błędna u dostawcy B, ten sam typ dokumentu | Kwestia dostawcy: B nie ma reguł albo ma stare reguły, które już nie pasują do układu B | Wytrenuj raz tabelę dostawcy B (albo usuń reguły B, aby przejęło AI). |
| Tabela błędna u każdego dostawcy od pewnej daty | Zmieniono ustawienie organizacji (poziom AI, ekstrakcja strukturalna, Vision, kolumny tabeli) | Porównaj ustawienia z datą zmiany; uruchom ponownie jeden dokument, aby potwierdzić. |
| Ten sam dokument: ścieżka reguł pusta, ścieżka AI poprawna | Reguły nie pasują do tego wariantu układu | Wytrenuj ponownie z tym dokumentem albo usuń reguły. |
| Ten sam dokument: obie ścieżki puste | Brak czytelnego tekstu (skan bez tekstu OCR, PDF zawierający tylko obraz) | Widok OCR na ekranie walidacji; włącz E-Text, jeśli PDF ma warstwę tekstową; spróbuj innej wersji OCR. |
| Jedna kolumna błędna w każdym wierszu, reszta w porządku | Mapowanie kolumn lub flaga *Use AI* | Ustawienia Kolumny tabeli; zmapuj ponownie w szkoleniu tabeli. |
| Brakuje wierszy przy podziale stron lub po sumie częściowej | Układ, za którym AI lub reguły nie podążyły | Wytrenuj tabelę na dokumencie wielostronicowym; dodaj tag, na przykład *"tabela jest kontynuowana na stronie 2"*. |
| Brak kroku ekstrakcji w logach, dokument utknął w statusie *running* | Infrastruktura (zaległości workerów), nie konfiguracja | Sprawdź oczekujące zadania (`get_pending_tasks_detail` przez MCP) i skontaktuj się ze wsparciem, podając ID dokumentu. |

## Co wysłać do wsparcia

* ID dokumentu i organizację
* Która zakładka zawiera wiersze (Extracted table / AI Extracted table / żadna) oraz używany poziom AI
* Czy dostawca ma zapisane reguły i kiedy zostały ostatnio zapisane
* Jeden przykładowy dokument, na którym działa, i jeden, na którym nie działa, jeśli masz oba

## Powiązane strony

* [Rozwiązywanie problemów z ekstrakcją tabeli](table-extraction-troubleshoot.md): jakość ekstrakcji, OCR, E-Text, komunikaty na tabeli
* [Szkolenie pól linii / Szkolenie tabeli](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Tabela AI](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Ustawienia logów](../../../administration-and-setup/settings/log-settings/README.md)
