# Narzędzia przepływów pracy

DocFlow MCP udostępnia narzędzia do zarządzania zaawansowanymi przepływami pracy i ich testowania, a także narzędzia do odczytu logów przepływów pracy i zarządzania zmiennymi przepływów pracy.

{% hint style="info" %}
**Nazwy narzędzi przez bramę DocBits MCP.** Gdy łączysz się przez ujednolicony DocBits MCP (`api.docbits.com/v3/mcp`), każde narzędzie DocFlow ma przedrostek `docflow_`: `list_workflows` nazywa się `docflow_list_workflows`, a `run_workflow_with_assertions` to `docflow_run_workflow_with_assertions`. Parametry są identyczne. Poniższe nazwy to podstawowe nazwy DocFlow.

Przepływy pracy są **tworzone i edytowane w projektancie DocFlow** w aplikacji webowej. MCP je odczytuje, testuje, uruchamia i usuwa; nie tworzy ani nie modyfikuje grafów przepływów pracy.
{% endhint %} Narzędzia Card SDK mają własną stronę, patrz [Narzędzia Card SDK](card-sdk-tools.md).

## list\_workflows

Wyświetla wszystkie przepływy pracy bieżącej organizacji.

**Parametry:** Brak

## get\_workflow

Pobiera szczegóły konkretnego przepływu pracy, w tym strukturę jego węzłów i krawędzi.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy |

## delete\_workflow

Usuwa przepływ pracy według ID (miękkie usunięcie).

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do usunięcia |

## test\_advanced\_workflow

Testuje wykonanie zaawansowanego przepływu pracy. Opcjonalnie możesz podać ID dokumentu, aby przetestować przepływ na prawdziwym dokumencie.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID zaawansowanego przepływu pracy |
| `doc_id` | string | Nie | UUID dokumentu do testowania |

## list\_test\_scenarios

Wyświetla wszystkie scenariusze testowe przepływów pracy organizacji.

**Parametry:** Brak

## list\_cards

Wyświetla wszystkie dostępne karty przepływów pracy wraz z ich warunkami i konfiguracją.

**Parametry:** Brak

{% hint style="info" %}
Karty mają flagi ról: `when_condition` (wyzwalacz), `and_condition` (dodatkowy warunek) i `then_condition` (akcja). Na ich podstawie ustalisz, w jakich typach węzłów można użyć danej karty.
{% endhint %}

## list\_workflow\_variables

Wyświetla wszystkie zmienne przepływów pracy organizacji wraz z nazwą, typem i bieżącą wartością.

**Parametry:** Brak

## set\_workflow\_variable

Tworzy zmienną przepływu pracy lub aktualizuje jej wartość. Zmienne typu dokument nie mają własnej wartości; ustawia je przepływ pracy w czasie wykonania.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `name` | string | Tak | Nazwa zmiennej |
| `value` | string | Nie | Nowa wartość |
| `var_type` | string | Nie | Typ zmiennej przy tworzeniu (na przykład `string`, `number`, `document`) |

## search\_workflow\_logs

Przeszukuje logi wykonania przepływów pracy, aby ustalić, dlaczego uruchomienia zakończyły się niepowodzeniem, powodzeniem lub niezgodnością warunku.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Nie | Ogranicza do jednego przepływu pracy |
| `doc_id` | string | Nie | Ogranicza do uruchomień dla jednego dokumentu |
| `status` | string | Nie | Status uruchomienia, według którego filtrować |
| `keyword` | string | Nie | Filtr pełnotekstowy logu |
| `include_workflow_data` | boolean | Nie | Dołącza migawkę definicji przepływu pracy dla każdego uruchomienia |
| `limit` / `offset` | integer | Nie | Stronicowanie |

## get\_workflow\_log\_detail

Pełne szczegóły jednego uruchomienia: surowe logi wykonania kart oraz definicja przepływu pracy w postaci z czasu uruchomienia.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `log_id` | string | Tak | ID wpisu logu z `search_workflow_logs` |

## run\_workflow\_with\_assertions

Ustawia zmienne przepływu pracy, uruchamia zaawansowany przepływ pracy prawdziwym wykonawcą i sprawdza wynik względem bazy danych. Zmienne są prawdziwymi zapisami, a nie atrapami; używaj tego narzędzia do testów integracyjnych przepływu pracy z poziomu asystenta.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do uruchomienia |
| `doc_id` | string | Nie | Dokument, na którym ma zostać uruchomiony przepływ pracy |
| `seed_variables` | array | Nie | Zmienne do utworzenia lub zaktualizowania przed uruchomieniem; zmienne typu dokument mogą wskazywać `doc_id` przez `value` |

