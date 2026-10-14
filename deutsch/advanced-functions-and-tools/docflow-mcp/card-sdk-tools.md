# Card SDK Tools

Die Card SDK Tools ermoeglichen es Ihnen, benutzerdefinierte Partner-Karten ueber MCP zu erstellen, zu validieren, zu testen und zu verwalten. Partner-Karten erweitern DocFlow mit benutzerdefinierter Geschaeftslogik, die in Python geschrieben ist.

## Karten-Lebenszyklus

```
Erstellen → Validieren → Testen → Genehmigen → In Workflows verwenden
```

1. **Erstellen** Sie eine Karte mit `sdk_create_card` oder `sdk_import_github`
2. **Validieren** Sie mit `sdk_validate_card` (5-stufige Validierung)
3. **Testen** Sie mit `sdk_test_card` (Sandbox-Ausfuehrung)
4. **Genehmigen** Sie mit `sdk_approve_card` (Admin erforderlich)
5. Die Karte ist nun in `list_cards` verfuegbar und kann in Workflows verwendet werden

## Entwicklungs-Tools

### sdk\_create\_card

Eine neue Partner-Karte aus Quellcode und Manifesten erstellen. Fuehrt die vollstaendige 5-stufige Validierung durch und speichert die Karte in der Datenbank. Die Karte beginnt im Status "ausstehend" und erfordert eine Admin-Genehmigung zur Aktivierung.

**Parameter:**

| Parameter       | Typ    | Erforderlich | Beschreibung                                                   |
| --------------- | ------ | ------------ | -------------------------------------------------------------- |
| `app_manifest`  | object | Ja           | App-Manifest mit id, name, version, Partner-Info               |
| `card_manifest` | object | Ja           | Karten-Manifest mit id, title, entry\_point, class\_name, args |
| `card_type`     | string | Ja           | `action` oder `condition`                                      |
| `source_code`   | string | Ja           | Python-Quellcode (muss `PartnerCard` erweitern)                |
| `test_code`     | string | Ja           | Pytest-Testcode fuer die Karte                                 |
| `locales`       | object | Nein         | Uebersetzungen, z.B. `{"en": {...}, "de": {...}}`              |

**App-Manifest-Beispiel:**

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

**Karten-Manifest-Beispiel:**

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

**Quellcode-Beispiel:**

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

**Beispielantwort:**

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

5-stufige Validierung einer Partner-Karte ohne Speichern ausfuehren. Zwei Modi:

* **Modus A** -- Eine bestehende Karte anhand der ID validieren
* **Modus B** -- Neuen Quellcode inline validieren

**Parameter:**

| Parameter       | Typ    | Erforderlich | Beschreibung                           |
| --------------- | ------ | ------------ | -------------------------------------- |
| `card_id`       | string | Nein         | UUID einer bestehenden Karte (Modus A) |
| `app_manifest`  | object | Nein         | App-Manifest (Modus B)                 |
| `card_manifest` | object | Nein         | Karten-Manifest (Modus B)              |
| `card_type`     | string | Nein         | `action` oder `condition` (Modus B)    |
| `source_code`   | string | Nein         | Python-Quellcode (Modus B)             |
| `test_code`     | string | Nein         | Testcode (Modus B)                     |

{% hint style="info" %}
Geben Sie entweder nur `card_id` an (Modus A) oder `app_manifest` + `card_manifest` + `source_code` zusammen (Modus B).
{% endhint %}

**Validierungsstufen:**

1. **Struktur** -- Ueberprueft Dateilayout, Manifest-Schema, erforderliche Dateien
2. **AST-Analyse** -- Prueft Python-Syntax, Klassenhierarchie, Methodensignaturen
3. **Abhaengigkeiten** -- Validiert Imports gegen erlaubte Module
4. **Tests** -- Fuehrt die Testsuite der Karte aus
5. **Verhalten** -- Fuehrt die Karte in der Sandbox aus, um das Laufzeitverhalten zu pruefen

### sdk\_test\_card

Eine Partner-Karte in einer Sandbox-Umgebung mit einem Mock-Kontext ausfuehren. Verwendet das gleiche Sicherheitsmodell wie die Produktion (eingeschraenkte Builtins, Import-Whitelist, 10-Sekunden-Timeout).

**Parameter:**

| Parameter      | Typ    | Erforderlich | Beschreibung                            |
| -------------- | ------ | ------------ | --------------------------------------- |
| `card_id`      | string | Nein         | UUID einer bestehenden Karte (Modus A)  |
| `source_code`  | string | Nein         | Quellcode fuer Inline-Tests (Modus B)   |
| `class_name`   | string | Nein         | Klassenname fuer Inline-Tests (Modus B) |
| `variables`    | object | Nein         | Variablen fuer den Karten-Konstruktor   |
| `mock_context` | object | Nein         | Mock-Ausfuehrungskontext                |

**Mock-Kontext-Felder:**

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

**Beispielantwort:**

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

Eine Partner-App aus einem GitHub-Repository importieren. Klont das Repository, liest `app.json` und importiert alle Karten aus dem `.docflowcompose`-Verzeichnis.

**Parameter:**

| Parameter    | Typ    | Erforderlich | Beschreibung                                          |
| ------------ | ------ | ------------ | ----------------------------------------------------- |
| `github_url` | string | Ja           | GitHub-HTTPS-URL (z.B. `https://github.com/org/repo`) |
| `branch`     | string | Nein         | Zu klonender Branch (Standard: `main`)                |
| `token`      | string | Nein         | GitHub-Token fuer private Repositories                |

**Erwartete Repository-Struktur:**

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

**Beispielantwort:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Verwaltungs-Tools

### sdk\_list\_submissions

Alle Partner-Karten-Einreichungen der aktuellen Organisation auflisten.

**Parameter:** Keine

**Beispielantwort:**

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

Den Validierungsstatus und Bericht fuer eine bestimmte Partner-Karten-Einreichung abrufen.

**Parameter:**

| Parameter | Typ    | Erforderlich | Beschreibung           |
| --------- | ------ | ------------ | ---------------------- |
| `card_id` | string | Ja           | UUID der Partner-Karte |

**Beispielantwort:**

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

Eine validierte Partner-Karte genehmigen und fuer die Verwendung in Workflows aktivieren. Die Karte wird in der Laufzeit-Registry registriert und ist in `list_cards` verfuegbar.

**Parameter:**

| Parameter | Typ    | Erforderlich | Beschreibung           |
| --------- | ------ | ------------ | ---------------------- |
| `card_id` | string | Ja           | UUID der Partner-Karte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen. Die Karte muss sich im Status `validated` oder `rejected` befinden.
{% endhint %}

### sdk\_reject\_card

Eine Partner-Karten-Einreichung ablehnen und deaktivieren.

**Parameter:**

| Parameter | Typ    | Erforderlich | Beschreibung             |
| --------- | ------ | ------------ | ------------------------ |
| `card_id` | string | Ja           | UUID der Partner-Karte   |
| `reason`  | string | Nein         | Grund fuer die Ablehnung |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen.
{% endhint %}

### sdk\_delete\_submission

Eine Partner-Karten-Einreichung deaktivieren oder loeschen. Abgelehnte oder deaktivierte Karten werden physisch aus der Datenbank geloescht. Aktive Karten werden zuerst deaktiviert.

**Parameter:**

| Parameter | Typ    | Erforderlich | Beschreibung           |
| --------- | ------ | ------------ | ---------------------- |
| `card_id` | string | Ja           | UUID der Partner-Karte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen.
{% endhint %}

### sdk\_list\_cards\_picker

Alle aktivierten, nicht veralteten Karten mit Rollen-Flags auflisten. Nuetzlich um zu bestimmen, welche Karten in welchen Knotentypen beim Erstellen von Workflows verwendet werden koennen.

**Parameter:** Keine

**Beispielantwort:**

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
