# Panel Analityczny

## Przegląd

**Panel Analityczny** zapewnia pełną widoczność wydajności przetwarzania dokumentów. Śledzi, ile czasu dokumenty spędzają na każdym etapie swojej ścieżki — od importu do eksportu — i pomaga identyfikować wąskie gardła, porównywać wydajność między organizacjami, typami dokumentów i dostawcami oraz porównywać wyniki ze **Średnią Globalną DocBits**.

Każdy dokument przechodzi przez wyraźne etapy:

**Nowy** (zaimportowany) → **Działanie** (przetwarzanie) → **Gotowy do walidacji** (oczekujący na sprawdzenie przez użytkownika) → **Oczekujący na zatwierdzenie** (oczekujący na zatwierdzenie) → **Eksport** (zakończony i wyeksportowany)

Czas upływa na każdym etapie — Panel Analityczny mówi dokładnie, **ile** i **gdzie** skupić swoje usprawnienia.

### Dwa typy wąskich gardeł

Panel pomaga rozróżnić między:

* **Wąskie gardła systemowe** — Jak długo DocBits jest zajęty automatycznym przetwarzaniem (OCR i ekstrakcja tekstu, klasyfikacja dokumentów, ekstrakcja pól, walidacja automatyczna). Można optymalizować poprzez konfigurację i zasoby systemowe.
* **Wąskie gardła użytkownika** — Czas spędzony na oczekiwaniu na ręczną walidację i zatwierdzenie (czas oczekiwania w kolejce, ręczna korekta danych, przegląd i walidacja, przepływy pracy zatwierdzania). Można optymalizować poprzez przepływ pracy i alokację zasobów.

## Jak aktywować

Panel Analityczny jest sterowany ustawieniem modułu. Po włączeniu w lewym pasku bocznym pojawia się wpis **Panel Analityczny**.

1. Przejdź do **Ustawienia → Przetwarzanie dokumentów → Moduł → Panel i Analityka**.
2. Włącz opcję **Panel Analityczny**.

<mark style="color:red;">**Notatka**</mark>: Panel Analityczny wymaga **Subskrypcji AI Dashboard**.

<mark style="color:red;">**Notatka**</mark>: Dostęp do Panelu Analitycznego jest ograniczony do użytkowników z uprawnieniami **administratora**.

## Typy przepływów

Wybierz właściwą perspektywę dla swojej analizy. Każdy typ przepływu daje inną perspektywę na te same dane.

| Typ przepływu | Cel | Kluczowe pytanie |
| --- | --- | --- |
| **Status** | Śledzenie cyklu życia dokumentu od importu do eksportu | *„Jaki jest całkowity czas moich dokumentów od importu do eksportu?"* |
| **Przetwarzanie** | Analiza wydajności modułów technicznych | *„Które kroki przetwarzania są wąskimi gardłami?"* |
| **Interakcja użytkownika** | Punkty kontaktu z człowiekiem i czas oczekiwania | *„Jak długo dokumenty oczekują na użytkowników?"* |

Użyj przełącznika **Typ przepływu** u góry panelu, aby przełączać się między perspektywami.

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_types.png" alt="Flow Type Switch"><figcaption></figcaption></figure>

### Przepływ Status

Śledzi ścieżkę dokumentu od **Nowy** do **Wyeksportowany** — przydatne do analizy pełnego cyklu życia.

<figure><img src="../.gitbook/assets/analytics_dashboard_status_flow.png" alt="Status Flow"><figcaption></figcaption></figure>

### Przepływ Przetwarzanie

Analizuje wydajność wszystkich **technicznych modułów przetwarzania** (OCR, klasyfikacja, ekstrakcja, walidacja) — przydatne do identyfikacji wąskich gardeł po stronie systemu.

<figure><img src="../.gitbook/assets/analytics_dashboard_processing_flow.png" alt="Processing Flow"><figcaption></figcaption></figure>

### Przepływ Interakcja użytkownika

Skupia się na **punktach kontaktu z człowiekiem** — czasie oczekiwania w kolejce, ręcznej walidacji, przeglądzie i zatwierdzeniu — przydatne do identyfikacji wąskich gardeł przepływu pracy i obsady kadrowej.

<figure><img src="../.gitbook/assets/analytics_dashboard_user_interaction_flow.png" alt="User Interaction Flow"><figcaption></figcaption></figure>

## Opcje filtrów

Panel obsługuje zaawansowane filtrowanie wielowymiarowe. Wszystkie wykresy, karty i tabele aktualizują się w czasie rzeczywistym na podstawie aktywnych filtrów.

### Wyszukaj

Natychmiast zlokalizuj dowolny dokument według **nazwy** lub **unikalnego identyfikatora**.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_search.png" alt="Search Filter"><figcaption></figcaption></figure>

### Kroki przepływu

Wybierz konkretne kroki, aby skupić swoją analizę. Włączanie/wyłączanie kroków przelicza również metryki czasowe na innych komponentach panelu.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_flow_steps.png" alt="Flow Steps Filter"><figcaption></figcaption></figure>

### Podorganizacja, Typ dokumentu, Dostawca, Grupa

Porównaj wydajność między:

* **Podorganizacjami** — różne jednostki biznesowe lub najemcy
* **Typami dokumentów** — faktury, zamówienia zakupu, dowody dostawy itp.
* **Dostawcami** — aby zidentyfikować, którzy dostawcy powodują najdłuższe czasy przetwarzania
* **Grupami** — aby porównać wydajność między przypisanymi grupami użytkowników (dostępne dla typów przepływów **Status** i **Interakcja użytkownika**)

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_dimensions.png" alt="Sub-Organization, Document Type, Supplier, Group Filters"><figcaption></figcaption></figure>

<mark style="color:red;">**Notatka**</mark>: Filtr **Grupa** dotyczy tylko dokumentów, które są **przypisane bezpośrednio do grupy**. Dokumenty przypisane do indywidualnego użytkownika — nawet jeśli ten użytkownik jest członkiem grupy — **nie są** uwzględniane w wynikach filtra grupy.

### Zakres czasu

Analizuj dowolny okres od **7 dni** do **pełnego roku** lub ustaw **niestandardowy zakres** za pomocą selektora dat.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_time_range.png" alt="Time Range Filter"><figcaption></figcaption></figure>

## Karty kroków przepływu

Każda karta reprezentuje krok przepływu na podstawie wybranego **Typu przepływu**. Karty dostosowują się do Twojego wyboru — pokazując etapy cyklu życia dla *Status*, moduły przetwarzania dla *Przetwarzanie* lub punkty kontaktu z użytkownikiem dla *Interakcja użytkownika*.

Każda karta wyświetla:

* Czasy **Min, Śr, Maks** dla kroku
* Porównanie między **Twoim Śr Czasem** a **Średnią Globalną DocBits** (gdy przełącznik porównania jest włączony)
* Okrąg wyboru, aby **uwzględnić lub wykluczyć** krok z agregowanych obliczeń czasu używanych przez Wykres Średniego Czasu, Wykres Trendu Czasu i Tabelę Danych

Przełącznik **Wybierz wszystko** w nagłówku pozwala uwzględnić lub wykluczyć każdy krok jednocześnie.

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_steps_card.png" alt="Flow Steps Card showing Min, Avg, Max"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_step_toggle.png" alt="Toggle Steps On/Off"><figcaption></figcaption></figure>

### Porównaj ze Średnią Globalną

Przełącznik **Porównaj ze Średnią Globalną** kontroluje, czy Średnia Globalna DocBits jest wyświetlana na kartach i na wykresie. Po włączeniu średni czas na każdej karcie jest oznaczony kolorem:

* **Zielony** — Twój Śr Czas jest równy lub niższy od Średniej Globalnej
* **Pomarańczowy** — Twój Śr Czas jest do **+25%** powyżej Średniej Globalnej
* **Czerwony** — Twój Śr Czas jest **+25%** lub więcej powyżej Średniej Globalnej

<figure><img src="../.gitbook/assets/analytics_dashboard_global_average_comparison.png" alt="Compare with DocBits Global Average"><figcaption></figcaption></figure>

## Wykres Średniego Czasu

Wykres Średniego Czasu wizualizuje, jak czas przetwarzania jest rozłożony dla wybranych kroków przepływu. Użyj selektora **Grupuj według**, aby porównać między różnymi wymiarami:

* **Kroki przepływu** — zobacz, które kroki zużywają najwięcej czasu
* **Podorganizacja** — zidentyfikuj różnice między jednostkami biznesowymi
* **Typ dokumentu** — porównaj czasy przetwarzania między typami dokumentów
* **Dostawca** — odkryj, którzy dostawcy mają najdłuższe czasy przetwarzania
* **Grupa** — porównaj między przypisanymi grupami użytkowników (tylko typy przepływów Status i Interakcja użytkownika)

Gdy włączone jest **Porównaj ze Średnią Globalną**, wykres wyświetla również Średnią Globalną DocBits do celów porównawczych.

<figure><img src="../.gitbook/assets/analytics_dashboard_average_time_chart.png" alt="Average Time Chart"><figcaption></figcaption></figure>

## Najlepsze dokumenty

Karta **Najlepsze dokumenty** zawiera listę poszczególnych dokumentów pasujących do aktywnego zestawu filtrów, uszeregowanych według łącznego spędzonego czasu.

* Przełącznik **Kolejność sortowania** — przełączanie między **malejącą** (najwolniejsze najpierw) a **rosnącą** (najszybsze najpierw).
* Lista rozwijana **Rozmiar strony** i paginacja — przewracaj zestaw wyników.
* **Ukryj / pokaż** dokument za pomocą ikony oka obok niego — ukryte dokumenty są wykluczone ze wszystkich obliczeń czasu na panelu.
* **Ukryj / pokaż wszystkie** dokumenty w filtrze za pomocą ikony oka w nagłówku.
* **Kliknij dokument** (nazwa pliku lub pasek postępu), aby skopiować jego identyfikator dokumentu do schowka.

<figure><img src="../.gitbook/assets/analytics_dashboard_top_documents.png" alt="Top Documents"><figcaption></figcaption></figure>

## Wykres Trendu Czasu

Śledź trendy wydajności w czasie i wykrywaj anomalie. Wykres Trendu Czasu pokazuje **Śr Czas** aktualnie wybranych kroków przepływu i może być grupowany według:

* **Kroki przepływu** — jedna linia na wybrany krok
* **Podorganizacja**
* **Typ dokumentu**
* **Dostawca**
* **Grupa** (dostępne dla typów przepływów **Status** i **Interakcja użytkownika**)

Ułatwia to wykrycie nagłego skoku dla konkretnego dostawcy lub stopniowego wzrostu dla konkretnego typu dokumentu, zanim stanie się krytycznym problemem.

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend.png" alt="Time Trend Chart"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend_grouped.png" alt="Time Trend Chart Grouped"><figcaption></figcaption></figure>

## Tabela danych

Tabela danych zapewnia pełny dostęp do wszystkich podstawowych danych wierszy dla aktywnego zestawu filtrów.

* **Przeciągnij kolumny do panelu Ukryte kolumny** (po lewej stronie tabeli), aby usunąć je z widoku. Ukryte kolumny są używane do agregacji — czasy **Min / Maks / Śr** są dynamicznie przeliczane na podstawie widocznych kolumn. Przeciągnij żeton z powrotem do tabeli (lub kliknij ikonę **+**), aby przywrócić kolumnę.
* **Sortuj**, klikając nagłówki kolumn, i **zmień kolejność** kolumn przez przeciąganie i upuszczanie.
* **Pobierz CSV** za pomocą przycisku w nagłówku karty — eksportowane są tylko aktualnie widoczne kolumny.

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table.png" alt="Data Table"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_hide_columns.png" alt="Hide Columns to Recalculate Aggregations"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_export.png" alt="Export Data Table as CSV"><figcaption></figcaption></figure>
