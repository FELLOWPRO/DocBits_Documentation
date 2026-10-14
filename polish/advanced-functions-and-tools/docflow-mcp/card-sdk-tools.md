# Narzędzia SDK Kart

Narzedzia Card SDK pozwalaja tworzyc, walidowac, testowac i zarzadzac niestandardowymi kartami partnerskimi przez MCP. Karty partnerskie rozszerzaja DocFlow o niestandardowa logike biznesowa napisana w Pythonie.

## Cykl zycia karty

```
Create → Validate → Test → Approve → Use in Workflows
```

1. **Utworz** karte za pomoca `sdk_create_card` lub `sdk_import_github`
2. **Zwaliduj** za pomoca `sdk_validate_card` (5-etapowa walidacja)
3. **Przetestuj** za pomoca `sdk_test_card` (wykonanie w srodowisku sandbox)
4. **Zatwierdz** za pomoca `sdk_approve_card` (wymagany administrator)
5. Karta jest teraz dostepna w `list_cards` i moze byc uzywana w przepływach pracy

## Narzedzia deweloperskie

### sdk\_create\_card

Tworzy nowa karte partnerska z kodu zrodlowego i manifestow. Uruchamia pelna 5-etapowa walidacje i zapisuje karte w bazie danych. Karta rozpoczyna w stanie oczekujacym i wymaga zatwierdzenia administratora, aby ja aktywowac.

**Parametry:**

| Parametr        | Typ    | Wymagany | Opis                                                             |
| --------------- | ------ | -------- | ---------------------------------------------------------------- |
| `app_manifest`  | object | Tak      | Manifest aplikacji z id, name, version, informacjami o partnerze |
| `card_manifest` | object | Tak      | Manifest karty z id, title, entry\_point, class\_name, args      |
| `card_type`     | string | Tak      | `action` lub `condition`                                         |
| `source_code`   | string | Tak      | Kod zrodlowy Python (musi rozszerzac `PartnerCard`)              |
| `test_code`     | string | Tak      | Kod testow Pytest dla karty                                      |
| `locales`       | object | Nie      | Tlumaczenia lokalizacji, np. `{"en": {...}, "de": {...}}`        |

**Przyklad manifestu aplikacji:**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Przyklad manifestu karty:**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Przyklad kodu zrodlowego:**

```python
from api.sdk.base import PartnerCard
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context):
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}"
            )
        return CardResult(
            status=CardStatus.FAILURE,
            message=f"Amount {total} below threshold {threshold}"
        )
```

**Przykladowa odpowiedz:**

```json
{
  "success": true,
  "cards": ["amount-threshold"],
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_validate\_card

Uruchamia 5-etapowa walidacje karty partnerskiej bez zapisywania. Dwa tryby:

* **Tryb A** — Walidacja istniejacej karty po ID
* **Tryb B** — Walidacja nowego kodu zrodlowego inline

**Parametry:**

| Parametr        | Typ    | Wymagany | Opis                              |
| --------------- | ------ | -------- | --------------------------------- |
| `card_id`       | string | Nie      | UUID istniejacej karty (Tryb A)   |
| `app_manifest`  | object | Nie      | Manifest aplikacji (Tryb B)       |
| `card_manifest` | object | Nie      | Manifest karty (Tryb B)           |
| `card_type`     | string | Nie      | `action` lub `condition` (Tryb B) |
| `source_code`   | string | Nie      | Kod zrodlowy Python (Tryb B)      |
| `test_code`     | string | Nie      | Kod testow (Tryb B)               |

{% hint style="info" %}
Podaj albo sam `card_id` (Tryb A), albo `app_manifest` + `card_manifest` + `source_code` razem (Tryb B).
{% endhint %}

**Etapy walidacji:**

1. **Struktura** — Weryfikuje uklad plikow, schemat manifestu, wymagane pliki
2. **Analiza AST** — Sprawdza skladnie Pythona, hierarchie klas, sygnatury metod
3. **Zaleznosci** — Waliduje importy wzgledem dozwolonych modulow
4. **Testy** — Uruchamia zestaw testow karty
5. **Behawioralna** — Wykonuje karte w srodowisku sandbox, aby sprawdzic zachowanie w czasie wykonania

### sdk\_test\_card

Wykonuje karte partnerska w srodowisku sandbox z symulowanym kontekstem. Uzywa tego samego modelu bezpieczenstwa co produkcja (ograniczone wbudowane funkcje, biala lista importow, limit czasu 10 sekund).

**Parametry:**

| Parametr       | Typ    | Wymagany | Opis                                       |
| -------------- | ------ | -------- | ------------------------------------------ |
| `card_id`      | string | Nie      | UUID istniejacej karty (Tryb A)            |
| `source_code`  | string | Nie      | Kod zrodlowy do testowania inline (Tryb B) |
| `class_name`   | string | Nie      | Nazwa klasy do testowania inline (Tryb B)  |
| `variables`    | object | Nie      | Zmienne przekazywane do konstruktora karty |
| `mock_context` | object | Nie      | Symulowany kontekst wykonania              |

**Pola symulowanego kontekstu:**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

**Przykladowa odpowiedz:**

```json
{
  "success": true,
  "status": "CardStatus.SUCCESS",
  "message": "Amount 1500.00 exceeds threshold 1000",
  "data": {},
  "logs": ["Checking threshold...", "Amount exceeds threshold"]
}
```

### sdk\_import\_github

Importuje aplikacje partnerska z repozytorium GitHub. Klonuje repozytorium, odczytuje `app.json` i importuje wszystkie karty znalezione w katalogu `.docflowcompose`.

**Parametry:**

| Parametr     | Typ    | Wymagany | Opis                                                 |
| ------------ | ------ | -------- | ---------------------------------------------------- |
| `github_url` | string | Tak      | URL HTTPS GitHub (np. `https://github.com/org/repo`) |
| `branch`     | string | Nie      | Galaz do klonowania (domyslnie: `main`)              |
| `token`      | string | Nie      | Token GitHub dla prywatnych repozytoriow             |

**Oczekiwana struktura repozytorium:**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

**Przykladowa odpowiedz:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Narzedzia zarzadzania

### sdk\_list\_submissions

Wyswietla wszystkie zgloszenia kart partnerskich dla biezacej organizacji.

**Parametry:** Brak

**Przykladowa odpowiedz:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Amount Threshold Check",
    "partner_app_id": "com.acme.invoice-tools",
    "partner_status": "validated",
    "version": "1.0.0",
    "card_type": "condition",
    "enabled": false,
    "submitted_at": "2025-03-20T10:00:00"
  }
]
```

### sdk\_get\_submission\_status

Pobiera status walidacji i raport dla konkretnego zgloszenia karty partnerskiej.

**Parametry:**

| Parametr  | Typ    | Wymagany | Opis                    |
| --------- | ------ | -------- | ----------------------- |
| `card_id` | string | Tak      | UUID karty partnerskiej |

**Przykladowa odpowiedz:**

```json
{
  "card_id": "card-uuid",
  "status": "validated",
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_approve\_card

Zatwierdza zwalidowana karte partnerska i aktywuje ja do uzycia w przepływach pracy. Karta jest rejestrowana w rejestrze runtime i staje sie dostepna w `list_cards`.

**Parametry:**

| Parametr  | Typ    | Wymagany | Opis                    |
| --------- | ------ | -------- | ----------------------- |
| `card_id` | string | Tak      | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnien administratora organizacji. Karta musi byc w stanie `validated` lub `rejected`.
{% endhint %}

### sdk\_reject\_card

Odrzuca zgloszenie karty partnerskiej i dezaktywuje ja.

**Parametry:**

| Parametr  | Typ    | Wymagany | Opis                    |
| --------- | ------ | -------- | ----------------------- |
| `card_id` | string | Tak      | UUID karty partnerskiej |
| `reason`  | string | Nie      | Powod odrzucenia        |

{% hint style="warning" %}
Wymaga uprawnien administratora organizacji.
{% endhint %}

### sdk\_delete\_submission

Dezaktywuje lub usuwa zgloszenie karty partnerskiej. Odrzucone lub wylaczone karty sa fizycznie usuwane z bazy danych. Aktywne karty sa najpierw dezaktywowane.

**Parametry:**

| Parametr  | Typ    | Wymagany | Opis                    |
| --------- | ------ | -------- | ----------------------- |
| `card_id` | string | Tak      | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnien administratora organizacji.
{% endhint %}

### sdk\_list\_cards\_picker

Wyswietla wszystkie wlaczone, nieoznaczone jako przestarzale karty z flagami rol. Przydatne do okreslania, ktore karty moga byc uzywane w jakich typach wezlow podczas budowania przepływow pracy.

**Parametry:** Brak

**Przykladowa odpowiedz:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Document Type Is",
    "category": "Document",
    "card_type": "document_type_is",
    "is_when": true,
    "is_and": false,
    "is_then": false,
    "is_partner_card": false
  }
]
```
