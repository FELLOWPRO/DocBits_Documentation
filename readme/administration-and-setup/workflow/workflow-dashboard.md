---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Panel Workflow

Panel Workflow to centralne miejsce do zarządzania i monitorowania wszystkich przepływów pracy w DocBits. Aby uzyskać do niego dostęp, kliknij ikonę **Przepływy pracy** na lewym pasku bocznym.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard with run totals, success and fail rates, the runs chart and recent activity"><figcaption><p>Panel Workflow — łączne liczby uruchomień, wskaźniki sukcesu/niepowodzeń oraz ostatnia aktywność dla każdego przepływu pracy.</p></figcaption></figure>

## Zakładka Panel

Zakładka Panel zapewnia szybki przegląd wydajności przepływów pracy dla wybranego okresu czasu.

### Filtry

- **Data początkowa / Data końcowa** — Wybierz zakres czasowy dla statystyk
- **Nazwa przepływu pracy** — Filtruj według konkretnego przepływu pracy lub wyświetl wszystkie
- **Porównaj** — Porównaj dwa okresy obok siebie
- **Wyczyść** — Zresetuj wszystkie filtry

### Karty statystyk

| Metryka | Opis |
|---|---|
| **Przepływy pracy wykonane dzisiaj** | Łączna liczba uruchomień przepływów pracy dzisiaj |
| **Przepływy pracy utworzone (okres)** | Nowe przepływy pracy utworzone w wybranym zakresie dat |
| **Łączna liczba uruchomień** | Skumulowana liczba wykonań przepływów pracy w danym okresie |
| **Udane uruchomienia** | Liczba uruchomień zakończonych bez błędów |
| **Wskaźnik sukcesu** | Procent udanych uruchomień w stosunku do łącznej liczby uruchomień |
| **Wskaźnik niepowodzeń** | Procent nieudanych uruchomień w stosunku do łącznej liczby uruchomień |

{% hint style="warning" %}
Wysoki wskaźnik niepowodzeń (wyświetlany jako **CRITICAL** na czerwono) wskazuje, że przepływy pracy napotykają błędy. Zbadaj nieudane przepływy pracy, korzystając z dzienników wykonań w [Zaawansowanym Kreatorze Przepływów Pracy](advanced-workflow-builder/).
{% endhint %}

### Wykres uruchomień przepływów pracy

Wykres przedstawia miesięczny podział **udanych** (zielony) i **nieudanych** (czerwony/różowy) uruchomień przepływów pracy, pomagając identyfikować trendy i skoki błędów.

### Ostatnia aktywność

- **Ostatnie testy przepływów pracy** — Pokazuje ostatnie wykonania testów ze statusem powodzenia/niepowodzenia
- **Ostatnie przepływy pracy** — Pokazuje ostatnio utworzone lub zmodyfikowane przepływy pracy

## Zakładka Lista przepływów pracy

Zakładka Lista przepływów pracy wyświetla wszystkie przepływy pracy z możliwością wyszukiwania, sortowania i zarządzania.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Kolumny

| Kolumna | Opis |
|---|---|
| **Status** | Ikona przełącznika — kliknij, aby włączyć/wyłączyć przepływ pracy |
| **Nazwa** | Nazwa przepływu pracy (kliknij, aby otworzyć w Kreatorze Przepływów Pracy) |
| **Typ** | Znacznik wyświetlający `Advanced` dla przepływów wizualnych |
| **Kiedy...** | Podsumowanie warunku wyzwalającego |
| **Zaktualizowano przez** | Użytkownik, który ostatnio zmodyfikował przepływ pracy |
| **Data utworzenia** | Data i godzina utworzenia |
| **Zaktualizowano** | Data i godzina ostatniej modyfikacji |
| **Akcje** | Menu kontekstowe (usuń, duplikuj, eksportuj) |

### Akcje

- **Szukaj** — Filtruj przepływy pracy według nazwy za pomocą paska wyszukiwania
- **+ DODAJ PRZEPŁYW PRACY** — Utwórz nowy przepływ pracy (otwiera [Zaawansowany Kreator Przepływów Pracy](advanced-workflow-builder/))
- **SZABLONY** — Przeglądaj i ładuj zapisane szablony przepływów pracy
- **IMPORTUJ PRZEPŁYW PRACY** — Importuj przepływ pracy z pliku JSON

## Zakładka Lista menedżera testów

Zakładka Lista menedżera testów wyświetla wszystkie konfiguracje testów przepływów pracy i ich wyniki. Użyj jej do ustawiania zautomatyzowanych scenariuszy testowych dla swoich przepływów pracy.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Workflow Test Manager List with test scenarios and Run All Tests"><figcaption><p>Lista menedżera testów — każdy scenariusz pokazuje wynik powodzenia/niepowodzenia; użyj przycisku <strong>Run All Tests</strong>, aby uruchomić je wszystkie ponownie.</p></figcaption></figure>

## Zakładka Licencja

Zakładka Licencja wyświetla aktualny status licencji DocFlow i dostępne funkcje.

## Zakładka Card SDK

Zakładka Card SDK umożliwia tworzenie i zarządzanie niestandardowymi kartami przepływów pracy (kartami partnerskimi), które rozszerzają wbudowane możliwości DocFlow.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### Prześlij ZIP

Prześlij aplikację partnerską jako plik ZIP zawierający:
- `app.json` — Metadane i konfiguracja karty
- `.docflowcompose/flow/` — Pliki definicji karty

Maksymalny rozmiar pliku: **10 MB**. Kliknij **Prześlij i zweryfikuj**, aby przesłać kartę do recenzji.

### Import z GitHub

Importuj karty partnerskie bezpośrednio z repozytorium GitHub zamiast przesyłania pliku ZIP.

### Zgłoszenia

Przeglądaj i zarządzaj wszystkimi zgłoszonymi kartami partnerskimi:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Kolumna | Opis |
|---|---|
| **Nazwa karty** | Nazwa aplikacji partnerskiej i karty |
| **card_type_label** | Typ karty (`Action_card` lub `Condition_card`) |
| **Wersja** | Numer wersji karty |
| **Zgłoszono** | Data zgłoszenia |
| **Status** | Aktualny status recenzji |
| **Akcje** | Dostępne akcje w zależności od statusu |

#### Statusy kart

| Status | Znaczenie | Dostępne akcje |
|---|---|---|
| **Validated** | Karta przeszła walidację | Pobierz, Zatwierdź, Odrzuć |
| **Approved** | Karta jest aktywna i dostępna w przepływach pracy | Pobierz, Wyłącz, Cofnij |
| **Rejected** | Karta nie przeszła recenzji | Usuń |
| **Disabled** | Karta została dezaktywowana | Usuń |

### Pobierz szablon SDK

Kliknij **Pobierz szablon SDK**, aby pobrać szablon startowy do budowania własnych niestandardowych kart. Szablon zawiera wymaganą strukturę plików i przykładowe konfiguracje.

{% hint style="info" %}
Kartami partnerskimi można również zarządzać programowo za pomocą [narzędzi DocFlow MCP](../../../advanced-functions-and-tools/docflow-mcp/). Użyj narzędzi Card SDK MCP, aby tworzyć, walidować, zatwierdzać i testować karty z poziomu IDE lub skryptów automatyzacji.
{% endhint %}
