# Narzedzia przepływow pracy

DocFlow MCP udostepnia narzedzia do zarzadzania i testowania zaawansowanych przepływow pracy, a takze narzedzia do odczytu logow przepływow pracy oraz zarzadzania zmiennymi przepływow. Narzedzia Card SDK znajduja sie na osobnej stronie — zobacz [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Wyswietla wszystkie przepływy pracy biezacej organizacji.

**Parametry:** Brak

## get\_workflow

Pobiera szczegoly konkretnego przepływu pracy wraz z jego struktura wezlow i krawedzi.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy |

## create\_advanced\_workflow

Tworzy nowy zaawansowany przepływ pracy z wezlami i krawedziami.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `name` | string | Tak | Nazwa przepływu pracy (3-126 znakow) |
| `description` | string | Nie | Opcjonalny opis |
| `nodes` | array | Tak | Tablica wezlow przepływu pracy |
| `edges` | array | Tak | Tablica krawedzi laczacych wezly |

### Struktura wezlow

Kazdy wezel wymaga:

| Pole | Typ | Opis |
|-------|------|-------------|
| `node_id` | string | Unikalny identyfikator wezla |
| `node_type` | string | Zobacz typy wezlow ponizej |
| `position` | object | `{x: number, y: number}` pozycja na kanwie |
| `label` | string | Etykieta wyswietlana |
| `card` | object | Konfiguracja karty (wymagana dla `when`, `and`, `then` — zobacz ponizej) |

**Typy wezlow:**

| Typ | Karta wymagana | Cel |
|------|------------------|---------|
| `start` | Brak karty | Wezel wyzwalacza — punkt wejscia przepływu pracy |
| `when` | Karta warunku | Warunek wyzwalacza (rowniez prawidlowy punkt wejscia) |
| `and` | Karta warunku | Dodatkowa bramka warunku po `when` |
| `or` | Brak karty | Wezel rozgalezienia — przechodzi dalej, jesli ktoraskolwiek z galezi przychodzacych powiedzie sie |
| `then` | Karta akcji | Akcja do wykonania |
| `delay` | Brak karty | Wezel oczekiwania — wstrzymuje wykonanie na skonfigurowany czas |
| `all` | Brak karty | Wezel laczacy — czeka na wszystkie galezie przychodzace |
| `any` | Brak karty | Wezel laczacy — przechodzi dalej z pierwsza galezia przychodzaca |
| `note` | Brak karty | Notatka / adnotacja; nie wykonywana |

### Struktura krawedzi

Kazda krawedz wymaga:

| Pole | Typ | Opis |
|-------|------|-------------|
| `edge_id` | string | Unikalny identyfikator krawedzi |
| `source_node_id` | string | ID wezla zrodlowego |
| `target_node_id` | string | ID wezla docelowego |
| `source_handle` | string | `success`, `error` lub `failed_condition` (opcjonalny) |
| `target_handle` | string | `input` (opcjonalny) |

**Uchwyty zrodlowe:**

- `success` — wybrany, gdy wezel zrodlowy zakonczy sie sukcesem (dostepny w kazdym wykonywalnym wezle).
- `failed_condition` — wybrany, gdy karta warunku `when` lub `and` zostanie oceniona jako false.
- `error` — wybrany, gdy wezel `and` lub `then` zglosi blad.

### Konfiguracja karty

Karty definiuja, co robi wezel. Uzyj `list_cards` lub `sdk_list_cards_picker`, aby uzyskac dostepne karty.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
Wystarczy podac `id`, `card_type`, `version` i `variables` dla kazdej karty. Serwer automatycznie wzbogaca karty o metadane wyswietlania (svg, text, category) z bazy danych.
{% endhint %}

**Przyklad zadania:**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Aktualizuje istniejacy zaawansowany przepływ pracy. Mozesz zaktualizowac dowolna kombinacje nazwy, opisu, wezlow i krawedzi.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do zaktualizowania |
| `name` | string | Nie | Nowa nazwa |
| `description` | string | Nie | Nowy opis |
| `nodes` | array | Nie | Nowe wezly (zastepuje wszystkie istniejace wezly) |
| `edges` | array | Nie | Nowe krawedzie (zastepuje wszystkie istniejace krawedzie) |

## delete\_workflow

Usuwa przepływ pracy po ID (miekkie usuniecie).

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID przepływu pracy do usuniecia |

## test\_advanced\_workflow

Testuje wykonanie zaawansowanego przepływu pracy. Opcjonalnie podaj ID dokumentu, aby testowac z rzeczywistym dokumentem.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `workflow_id` | string | Tak | UUID zaawansowanego przepływu pracy |
| `doc_id` | string | Nie | UUID dokumentu, z ktorym testowac |

## list\_test\_scenarios

Wyswietla wszystkie scenariusze testowe przepływow pracy dla organizacji.

**Parametry:** Brak

## list\_cards

Wyswietla wszystkie dostepne karty przepływow pracy wraz z ich warunkami i konfiguracja.

**Parametry:** Brak

{% hint style="info" %}
Karty maja flagi rol: `when_condition` (wyzwalacz), `and_condition` (dodatkowy warunek) i `then_condition` (akcja). Uzyj ich, aby okreslic, w ktorych typach wezlow mozna uzywac danej karty.
{% endhint %}
