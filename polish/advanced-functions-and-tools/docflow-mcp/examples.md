# Przykłady

Kompletne przykłady end-to-end pokazujace, jak uzywac narzedzi DocFlow MCP razem.

## Przykład 1: Utworzenie niestandardowej karty i uzycie jej w przepływie pracy

Ten przykład przeprowadza przez pełny cykl zycia: utworzenie karty partnerskiej, walidacja, testowanie, zatwierdzenie i zbudowanie przepływu pracy, ktory jej uzywa.

### Krok 1: Utworzenie karty

Wywolaj `sdk_create_card`:

```json
{
  "app_manifest": {
    "id": "com.example.invoice-tools",
    "name": "Invoice Tools",
    "version": "1.0.0",
    "partner": {
      "id": "example-partner",
      "name": "Example Corp"
    }
  },
  "card_manifest": {
    "id": "high-value-check",
    "title": {"en": "High Value Invoice Check"},
    "entry_point": "src/high_value.py",
    "class_name": "HighValueCheck",
    "args": [
      {
        "id": "threshold",
        "title": {"en": "Amount Threshold"},
        "type": "number",
        "required": true
      }
    ]
  },
  "card_type": "condition",
  "source_code": "from api.sdk.base import PartnerCard\nfrom api.sdk.result import CardResult, CardStatus\n\nclass HighValueCheck(PartnerCard):\n    def execute(self, context):\n        threshold = float(self.variables.get('threshold', 1000))\n        total = float(context.document_fields.get('total_amount', 0))\n        if total > threshold:\n            return CardResult(status=CardStatus.SUCCESS, message=f'High value: {total}')\n        return CardResult(status=CardStatus.FAILURE, message=f'Below threshold: {total}')",
  "test_code": "def test_high_value():\n    assert True  # Basic test"
}
```

Zapisz `card_id` z odpowiedzi — bedziesz go potrzebowac w kolejnych krokach.

### Krok 2: Walidacja karty

Wywolaj `sdk_validate_card` z ID karty:

```json
{
  "card_id": "returned-card-uuid"
}
```

Przejrzyj raport walidacji. Wszystkie 5 etapow powinno przejsc pomyslnie.

### Krok 3: Testowanie karty

Wywolaj `sdk_test_card` z symulowanym kontekstem dokumentu:

```json
{
  "card_id": "returned-card-uuid",
  "variables": {"threshold": "1000"},
  "mock_context": {
    "document_type": "INVOICE",
    "document_fields": {
      "total_amount": "2500.00",
      "currency": "EUR"
    }
  }
}
```

Sprawdz, czy odpowiedz pokazuje `CardStatus.SUCCESS`.

### Krok 4: Zatwierdzenie karty

Wywolaj `sdk_approve_card` (wymaga uprawnien administratora):

```json
{
  "card_id": "returned-card-uuid"
}
```

Karta jest teraz aktywna i dostepna do uzycia w przepływach pracy.

### Krok 5: Zbudowanie przepływu pracy z karta

Otwórz **projektanta DocFlow** w aplikacji webowej, utwórz zaawansowany przepływ pracy i dodaj zatwierdzoną kartę jako węzeł, na przykład wyzwalacz *Document Received*, kartę *High Value Check* i węzeł *Approval* dla gałęzi `true`. Grafy przepływów pracy tworzy się i edytuje w projektancie; MCP ich nie tworzy.

Po powrocie do asystenta potwierdź, że przepływ pracy istnieje, i odczytaj jego strukturę:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id z list_workflows>"
}
```

### Krok 6: Testowanie przepływu pracy

Wywolaj `test_advanced_workflow`:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Przejrzyj logi wykonania, aby sprawdzic, czy kazdy wezel wykonal sie poprawnie.

---

## Przykład 2: Budowanie przepływu pracy z wbudowanymi kartami

Ten przykład tworzy przepływ pracy uzywajac wylacznie wbudowanych kart (bez potrzeby tworzenia niestandardowych kart).

### Krok 1: Odkrywanie dostepnych kart

Wywolaj `sdk_list_cards_picker`, aby zobaczyc wszystkie dostepne karty z ich flagami rol:

```json
// Response includes cards like:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

Filtruj wedlug roli:
- `is_when: true` — Uzyj w wezlach WHEN (wyzwalacze)
- `is_and: true` — Uzyj w wezlach AND (dodatkowe warunki)
- `is_then: true` — Uzyj w wezlach THEN (akcje)

### Krok 2: Utworzenie przepływu pracy

```json
{
  "name": "Invoice Document Type Router",
  "description": "When document is an invoice, apply validation",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 250, "y": 50},
      "label": "Document is Invoice",
      "card": {
        "id": "doc-type-card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "and-1",
      "node_type": "and",
      "position": {"x": 250, "y": 200},
      "label": "Amount > 1000",
      "card": {
        "id": "amount-card-uuid",
        "card_type": "field_value_check",
        "version": 1,
        "variables": [
          {"id": "field-var", "data": "total_amount", "data_type": "string"},
          {"id": "op-var", "data": ">", "data_type": "string"},
          {"id": "val-var", "data": "1000", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 250, "y": 350},
      "label": "Set Status to Review",
      "card": {
        "id": "status-card-uuid",
        "card_type": "set_document_status",
        "version": 1,
        "variables": [
          {"id": "status-var", "data": "review", "data_type": "string"}
        ]
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "and-1",
      "source_handle": "success",
      "target_handle": "input"
    },
    {
      "edge_id": "e2",
      "source_node_id": "and-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

Tworzy to przepływ pracy: **WHEN** dokument jest faktura **AND** kwota > 1000 **THEN** ustaw status na przegladanie.

---

## Przykład 3: Import kart z GitHub

Jesli Twoje karty partnerskie znajduja sie w repozytorium GitHub, mozesz je zaimportowac bezposrednio:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Dla prywatnych repozytoriow dolacz token GitHub:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Po imporcie karty przechodza automatyczna walidacje. Sprawdz ich status za pomoca `sdk_list_submissions` i zatwierdz je za pomoca `sdk_approve_card`.
