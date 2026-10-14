# Card SDK Tools

De Card SDK-tools stellen u in staat om aangepaste partnerkaarten aan te maken, te valideren, te testen en te beheren via MCP. Partnerkaarten breiden DocFlow uit met aangepaste bedrijfslogica geschreven in Python.

## Levenscyclus van kaarten

```
Create → Validate → Test → Approve → Use in Workflows
```

1. **Aanmaken** van een kaart met `sdk_create_card` of `sdk_import_github`
2. **Valideren** met `sdk_validate_card` (5-fasen validatie)
3. **Testen** met `sdk_test_card` (uitvoering in sandbox)
4. **Goedkeuren** met `sdk_approve_card` (admin vereist)
5. De kaart is nu beschikbaar in `list_cards` en kan worden gebruikt in workflows

## Ontwikkeltools

### sdk\_create\_card

Een nieuwe partnerkaart aanmaken vanuit broncode en manifesten. Voert volledige 5-fasen validatie uit en slaat de kaart op in de database. De kaart begint in een wachtende status en vereist goedkeuring van een admin om te activeren.

**Parameters:**

| Parameter       | Type   | Vereist | Beschrijving                                                 |
| --------------- | ------ | ------- | ------------------------------------------------------------ |
| `app_manifest`  | object | Ja      | App-manifest met id, naam, versie, partnerinfo               |
| `card_manifest` | object | Ja      | Kaartmanifest met id, titel, entry\_point, class\_name, args |
| `card_type`     | string | Ja      | `action` of `condition`                                      |
| `source_code`   | string | Ja      | Python-broncode (moet `PartnerCard` uitbreiden)              |
| `test_code`     | string | Ja      | Pytest-testcode voor de kaart                                |
| `locales`       | object | Nee     | Taalvertalingen, bijv. `{"en": {...}, "de": {...}}`          |

**Voorbeeld App-manifest:**

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

**Voorbeeld Kaartmanifest:**

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

**Voorbeeld broncode:**

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

**Voorbeeldrespons:**

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

5-fasen validatie uitvoeren op een partnerkaart zonder op te slaan. Twee modi:

* **Modus A** — Een bestaande kaart valideren op basis van ID
* **Modus B** — Nieuwe broncode inline valideren

**Parameters:**

| Parameter       | Type   | Vereist | Beschrijving                       |
| --------------- | ------ | ------- | ---------------------------------- |
| `card_id`       | string | Nee     | UUID van bestaande kaart (Modus A) |
| `app_manifest`  | object | Nee     | App-manifest (Modus B)             |
| `card_manifest` | object | Nee     | Kaartmanifest (Modus B)            |
| `card_type`     | string | Nee     | `action` of `condition` (Modus B)  |
| `source_code`   | string | Nee     | Python-broncode (Modus B)          |
| `test_code`     | string | Nee     | Testcode (Modus B)                 |

{% hint style="info" %}
Geef ofwel alleen `card_id` op (Modus A) of `app_manifest` + `card_manifest` + `source_code` samen (Modus B).
{% endhint %}

**Validatiefasen:**

1. **Structuur** — Controleert bestandsindeling, manifestschema, vereiste bestanden
2. **AST-analyse** — Controleert Python-syntaxis, klassehiërarchie, methodesignaturen
3. **Afhankelijkheden** — Valideert imports tegen toegestane modules
4. **Tests** — Voert de testsuite van de kaart uit
5. **Gedrag** — Voert de kaart uit in een sandbox om runtime-gedrag te controleren

### sdk\_test\_card

Een partnerkaart uitvoeren in een sandboxomgeving met een gesimuleerde context. Gebruikt hetzelfde beveiligingsmodel als productie (beperkte builtins, importwhitelist, 10 seconden timeout).

**Parameters:**

| Parameter      | Type   | Vereist | Beschrijving                                        |
| -------------- | ------ | ------- | --------------------------------------------------- |
| `card_id`      | string | Nee     | UUID van bestaande kaart (Modus A)                  |
| `source_code`  | string | Nee     | Broncode voor inline testen (Modus B)               |
| `class_name`   | string | Nee     | Klassenaam voor inline testen (Modus B)             |
| `variables`    | object | Nee     | Variabelen om aan de kaartconstructor door te geven |
| `mock_context` | object | Nee     | Gesimuleerde uitvoeringscontext                     |

**Velden gesimuleerde context:**

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

**Voorbeeldrespons:**

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

Een partnerapp importeren vanuit een GitHub-repository. Kloont de repository, leest `app.json` en importeert alle kaarten die gevonden worden in de `.docflowcompose`-map.

**Parameters:**

| Parameter    | Type   | Vereist | Beschrijving                                           |
| ------------ | ------ | ------- | ------------------------------------------------------ |
| `github_url` | string | Ja      | GitHub HTTPS-URL (bijv. `https://github.com/org/repo`) |
| `branch`     | string | Nee     | Branch om te klonen (standaard: `main`)                |
| `token`      | string | Nee     | GitHub-token voor privérepositories                    |

**Verwachte repositorystructuur:**

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

**Voorbeeldrespons:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Beheertools

### sdk\_list\_submissions

Alle partnerkaartinzendingen voor de huidige organisatie weergeven.

**Parameters:** Geen

**Voorbeeldrespons:**

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

De validatiestatus en het rapport ophalen voor een specifieke partnerkaartinzending.

**Parameters:**

| Parameter | Type   | Vereist | Beschrijving             |
| --------- | ------ | ------- | ------------------------ |
| `card_id` | string | Ja      | UUID van de partnerkaart |

**Voorbeeldrespons:**

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

Een gevalideerde partnerkaart goedkeuren en activeren voor gebruik in workflows. De kaart wordt geregistreerd in het runtime-register en wordt beschikbaar in `list_cards`.

**Parameters:**

| Parameter | Type   | Vereist | Beschrijving             |
| --------- | ------ | ------- | ------------------------ |
| `card_id` | string | Ja      | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten. De kaart moet de status `validated` of `rejected` hebben.
{% endhint %}

### sdk\_reject\_card

Een partnerkaartinzending afwijzen en deactiveren.

**Parameters:**

| Parameter | Type   | Vereist | Beschrijving             |
| --------- | ------ | ------- | ------------------------ |
| `card_id` | string | Ja      | UUID van de partnerkaart |
| `reason`  | string | Nee     | Reden voor afwijzing     |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten.
{% endhint %}

### sdk\_delete\_submission

Een partnerkaartinzending deactiveren of verwijderen. Afgewezen of uitgeschakelde kaarten worden fysiek uit de database verwijderd. Actieve kaarten worden eerst gedeactiveerd.

**Parameters:**

| Parameter | Type   | Vereist | Beschrijving             |
| --------- | ------ | ------- | ------------------------ |
| `card_id` | string | Ja      | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten.
{% endhint %}

### sdk\_list\_cards\_picker

Alle ingeschakelde, niet-verouderde kaarten met rolvlaggen weergeven. Handig om te bepalen welke kaarten in welke nodetypes kunnen worden gebruikt bij het bouwen van workflows.

**Parameters:** Geen

**Voorbeeldrespons:**

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
