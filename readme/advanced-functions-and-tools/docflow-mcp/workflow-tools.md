# Narzedzia przepływow pracy

DocFlow MCP udostępnia narzędzia do zarządzania zaawansowanymi przepływami pracy i ich testowania, a także narzędzia do odczytu logów przepływów pracy i zarządzania zmiennymi przepływów pracy.

{% hint style="info" %}
**Nazwy narzędzi przez bramę DocBits MCP.** Gdy łączysz się przez ujednolicony DocBits MCP (`api.docbits.com/v3/mcp`), każde narzędzie DocFlow ma przedrostek `docflow_`: `list_workflows` nazywa się `docflow_list_workflows`, a `run_workflow_with_assertions` to `docflow_run_workflow_with_assertions`. Parametry są identyczne. Poniższe nazwy to podstawowe nazwy DocFlow.

Przepływy pracy są **tworzone i edytowane w projektancie DocFlow** w aplikacji webowej. MCP je odczytuje, testuje, uruchamia i usuwa; nie tworzy ani nie modyfikuje grafów przepływów pracy.
{% endhint %} Narzędzia SDK kart mają własną stronę, patrz [Narzędzia SDK Kart](card-sdk-tools.md).

## list\_workflows

Wyswietla wszystkie przepływy pracy dla biezacej organizacji.

**Parametry:** Brak

**Przykladowa odpowiedz:**

```json
[
  {
    "id": "a1b2c3d4-...",
    "name": "Invoice Approval",
    "version": 3,
    "enabled": true,
    "doc_types": ["INVOICE"],
    "workflow_type": "advanced",
    "created_on": "2025-01-15 10:30:00",
    "last_modified_on": "2025-03-20 14:22:00"
  }
]
```

## get\_workflow

Pobiera szczegoly konkretnego przepływu pracy, w tym jego strukture wezlow i krawedzi.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy |

**Przykladowa odpowiedz:**

```json
{
  "id": "a1b2c3d4-...",
  "name": "Invoice Approval",
  "version": 3,
  "enabled": true,
  "doc_types": ["INVOICE"],
  "workflow_type": "advanced",
  "description": "Routes invoices based on amount",
  "advanced_config": {
    "nodes": [
      {"node_id": "when-1", "node_type": "when", "label": "Amount > 1000"},
      {"node_id": "then-1", "node_type": "then", "label": "Send for Approval"}
    ],
    "edges": [
      {"source_node_id": "when-1", "target_node_id": "then-1"}
    ]
  }
}
```

## delete\_workflow

Usuwa przepływ pracy po ID (miekkie usuwanie).

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do usuniecia |

**Przykladowa odpowiedz:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Testuje wykonanie zaawansowanego przepływu pracy. Opcjonalnie mozna podac ID dokumentu, aby przetestowac z prawdziwym dokumentem.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID zaawansowanego przepływu pracy |
| `doc_id` | string | Nie | UUID dokumentu do testowania |

**Przykladowa odpowiedz:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-...",
  "execution_time": 0.234,
  "workflow_result": "completed",
  "node_results": {
    "when-1": {"status": "success", "output": true},
    "then-1": {"status": "success"}
  },
  "logs": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "status": "success",
      "error": null,
      "duration_ms": 12
    }
  ]
}
```

## list\_test\_scenarios

Wyswietla wszystkie scenariusze testowe przepływow pracy dla organizacji.

**Parametry:** Brak

**Przykladowa odpowiedz:**

```json
[
  {
    "id": "scenario-uuid",
    "name": "Invoice over 1000 EUR",
    "workflow_id": "a1b2c3d4-...",
    "enabled": true,
    "status": "passed",
    "last_run": "2025-03-20 14:00:00"
  }
]
```

## list\_cards

Wyswietla wszystkie dostepne karty przepływow pracy z ich warunkami i konfiguracja.

**Parametry:** Brak

**Przykladowa odpowiedz:**

```json
[
  {
    "id": "card-uuid",
    "text": "Document Type Is",
    "card_type": "document_type_is",
    "card_version": 1,
    "category": "Document",
    "when_condition": true,
    "and_condition": false,
    "then_condition": false
  },
  {
    "id": "card-uuid-2",
    "text": "Send Email Notification",
    "card_type": "send_email",
    "card_version": 1,
    "category": "Communication",
    "when_condition": false,
    "and_condition": false,
    "then_condition": true
  }
]
```

{% hint style="info" %}
Karty posiadaja flagi rol: `when_condition` (wyzwalacz), `and_condition` (dodatkowy warunek) i `then_condition` (akcja). Uzyj ich, aby okreslic, w jakich typach wezlow mozna uzyc danej karty.
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

Ustawia zmienne przepływu pracy, uruchamia zaawansowany przepływ pracy prawdziwym wykonawcą i sprawdza wynik względem bazy danych. Zmienne są prawdziwymi zapisami, nie atrapami; używaj tego narzędzia do testów integracyjnych przepływu pracy z poziomu asystenta.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do uruchomienia |
| `doc_id` | string | Nie | Dokument, na którym ma zostać uruchomiony przepływ pracy |
| `seed_variables` | array | Nie | Zmienne do utworzenia lub zaktualizowania przed uruchomieniem; zmienne typu dokument mogą wskazywać `doc_id` przez `value` |
