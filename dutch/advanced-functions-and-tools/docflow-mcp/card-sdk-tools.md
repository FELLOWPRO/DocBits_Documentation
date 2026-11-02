# Card-SDK-hulpmiddelen

De Card SDK-tools stellen u in staat om aangepaste partnerkaarten aan te maken, te valideren, te testen en te beheren via MCP. Partnerkaarten breiden DocFlow uit met aangepaste bedrijfslogica geschreven in Python.

## Levenscyclus van kaarten

Een partnerkaart doorloopt de volgende inzendingsstatussen (`partner_status`):

| Status | Betekenis | Zichtbaarheid in workflows |
|-------|---------|---------------------|
| `validating` | Inzending geaccepteerd; de validatiepijplijn wordt uitgevoerd. | Alleen de indienende organisatie |
| `validated` | Alle validatiefasen zijn geslaagd. Wacht op goedkeuring door een beheerder. | Alleen de indienende organisatie |
| `rejected` | Validatie mislukt, of een beheerder heeft de kaart afgewezen. De broncode blijft bewaard ter inspectie. | Alleen de indienende organisatie |
| `approved` | De beheerder heeft de kaart goedgekeurd; `enabled = true`. | **Alle organisaties** |
| `disabled` | Eerder goedgekeurde kaart die een beheerder heeft gedeactiveerd. | Alleen de indienende organisatie |
| `deleted` | Soft-deleted; wordt niet meer getoond in inzendingslijsten. | Verborgen |

{% hint style="warning" %}
**Zichtbaarheid per organisatie:** Een partnerkaart is pas beschikbaar voor workflownodes in `list_cards` nadat deze is **goedgekeurd**. Goedgekeurde partnerkaarten zijn zichtbaar voor elke organisatie op het platform — goedkeuring is een globale activering, geen activering per organisatie. Niet-goedgekeurde kaarten (validating, validated, rejected, disabled) zijn alleen zichtbaar voor de organisatie die ze heeft ingediend.
{% endhint %}

Typische werkwijze:

1. **Aanmaken** van een kaart met `sdk_create_card` of `sdk_import_github` — voert de validatiepijplijn uit en slaat de kaart op met `partner_status = validated` (of `rejected` bij een fout).
2. **Valideren** met `sdk_validate_card` om een bestaande kaart opnieuw te controleren of nieuwe broncode te testen zonder op te slaan.
3. **Testen** met `sdk_test_card` om de kaart in de sandbox uit te voeren met een gesimuleerde context.
4. **Goedkeuren** met `sdk_approve_card` (alleen organisatiebeheerder) — voert de AST- en gedragsvalidatie opnieuw uit en zet vervolgens `partner_status = approved` en `enabled = true`.
5. Na goedkeuring verschijnt de kaart in `list_cards` voor elke organisatie en kan deze worden gebruikt in workflownodes.

## Ontwikkeltools

### sdk\_create\_card

Een nieuwe partnerkaart aanmaken vanuit broncode en manifesten. Voert de volledige validatiepijplijn uit (zie [Validatiefasen](#sdk_validate_card) hieronder) en slaat de kaart op in de database. De kaart krijgt de status `validated` en vereist goedkeuring van een beheerder voordat deze in workflows kan worden gebruikt.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `app_manifest` | object | Ja | App-manifest met id, naam, versie, partnerinfo |
| `card_manifest` | object | Ja | Kaartmanifest met id, titel, entry\_point, class\_name, args |
| `card_type` | string | Ja | `action` of `condition` |
| `source_code` | string | Ja | Python-broncode (moet `PartnerCard` uitbreiden) |
| `test_code` | string | Ja | Pytest-testcode voor de kaart |
| `locales` | object | Nee | Taalvertalingen, bijv. `{"en": {...}, "de": {...}}` |

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
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` kent drie waarden en deze worden rechtstreeks gekoppeld aan workflowverbindingen:

| Status | Gevolgde verbinding | Gebruik voor |
|--------|------------|------------|
| `SUCCESS` | `success` | De kaart is geslaagd — geldt voor zowel condities als acties. |
| `FAILED` | `failed_condition` | **Alleen conditiekaarten.** De conditie is onwaar — de workflow volgt de "else"-tak. Actiekaarten hebben geen `failed_condition`-aansluiting, dus als een actie `FAILED` retourneert, kan de run nergens meer heen. |
| `ERROR` | `error` | Een onverwachte runtimefout (exception). Geldt voor zowel condities als acties. |

Kortom: acties retourneren `SUCCESS` of `ERROR`; condities kunnen daarnaast `FAILED` retourneren.
{% endhint %}

### sdk\_validate\_card

De validatiepijplijn uitvoeren op een partnerkaart zonder op te slaan. Twee modi:

- **Modus A** — Een bestaande kaart valideren op basis van ID
- **Modus B** — Nieuwe broncode inline valideren

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Nee | UUID van bestaande kaart (Modus A) |
| `app_manifest` | object | Nee | App-manifest (Modus B) |
| `card_manifest` | object | Nee | Kaartmanifest (Modus B) |
| `card_type` | string | Nee | `action` of `condition` (Modus B) |
| `source_code` | string | Nee | Python-broncode (Modus B) |
| `test_code` | string | Nee | Testcode (Modus B) |

{% hint style="info" %}
Geef ofwel alleen `card_id` op (Modus A) of `app_manifest` + `card_manifest` + `source_code` samen (Modus B).
{% endhint %}

**Validatiefasen:**

1. **Structuur** — Controleert de bestandsindeling, het manifestschema (`app.json`, `.docflowcompose/flow/...`) en of de opgegeven entrypoints bestaan.
2. **Locales** — Vergelijkt de in de kaart gebruikte vertaalsleutels met de bestanden `locales/<lang>.json`; mislukt als een sleutel ontbreekt in een opgegeven taal.
3. **AST-analyse** — Doorloopt elk `.py`-bestand onder `src/` en controleert op verboden imports, gevaarlijke aanroepen en eisen aan klassehiërarchie en methodesignaturen.
4. **Afhankelijkheden** — Valideert dat alle imports verwijzen naar toegestane modules uit de SDK-whitelist.
5. **Tests** — Voert de pytest-suite van de kaart uit met verlaagde rlimits.
6. **Gedrag** — Voert de kaart uit in de productiesandbox met een minimale gesimuleerde context om het runtime-gedrag te bevestigen.

De fasen worden op volgorde uitgevoerd; de eerste mislukte fase stopt de overige. Fase 6 (Gedrag) wordt bij goedkeuring opnieuw uitgevoerd als extra veiligheidscontrole voordat de kaart wordt geactiveerd.

### sdk\_test\_card

Een partnerkaart uitvoeren in een sandboxomgeving met een gesimuleerde context. De sandbox hanteert beperkte builtins, een samengestelde allowlist voor imports, een uitvoeringstimeout en verlaagde resourcelimieten voor het proces — dezelfde beperkingen waaronder een kaart draait zodra deze is goedgekeurd.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Nee | UUID van bestaande kaart (Modus A) |
| `source_code` | string | Nee | Broncode voor inline testen (Modus B) |
| `class_name` | string | Nee | Klassenaam voor inline testen (Modus B) |
| `variables` | object | Nee | Variabelen om aan de kaartconstructor door te geven |
| `mock_context` | object | Nee | Gesimuleerde uitvoeringscontext |

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

De tool retourneert `execution_success` (of de sandbox de kaart volledig heeft uitgevoerd — een timeout, importovertreding of gegooide exception zet dit op `false`), `card_status` (de `CardStatus` die `execute()` zelf retourneert), de `message` en `data` van de kaart, de vastgelegde `logs` en `execution_time_ms`.

### sdk\_import\_github

Een partnerapp importeren vanuit een GitHub-repository. Kloont de repository, leest `app.json` en importeert alle kaarten die gevonden worden in de `.docflowcompose`-map.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `github_url` | string | Ja | GitHub HTTPS-URL (bijv. `https://github.com/org/repo`) |
| `branch` | string | Nee | Branch om te klonen (standaard: `main`) |
| `token` | string | Nee | GitHub-token voor privérepositories |

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

## Beheertools

### sdk\_list\_submissions

Alle partnerkaartinzendingen voor de huidige organisatie weergeven.

**Parameters:** Geen

### sdk\_get\_submission\_status

De validatiestatus en het rapport ophalen voor een specifieke partnerkaartinzending.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

### sdk\_approve\_card

Een gevalideerde partnerkaart goedkeuren en activeren. Bij goedkeuring worden de AST- en gedragsvalidatie opnieuw uitgevoerd als extra veiligheidscontrole, wordt `partner_status = approved` en `enabled = true` ingesteld en wordt de kaart geregistreerd in het runtime-register. Na goedkeuring verschijnt de kaart in `list_cards` voor **elke organisatie**, niet alleen voor de indienende organisatie.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten. De kaart moet de status `validated` hebben. Afgewezen kaarten moeten opnieuw worden geüpload en gevalideerd voordat ze kunnen worden goedgekeurd.
{% endhint %}

### sdk\_reject\_card

Een partnerkaartinzending afwijzen en deactiveren.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |
| `reason` | string | Nee | Reden voor afwijzing |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten.
{% endhint %}

### sdk\_delete\_submission

Een partnerkaartinzending soft-deleten, ongeacht de huidige status. Zet `partner_status = deleted`, `enabled = false` en `deprecated = true`. De rij blijft bewaard voor auditdoeleinden, maar is verborgen in inzendingslijsten en `list_cards`.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatiebeheerderrechten.
{% endhint %}

### sdk\_list\_cards\_picker

Alle ingeschakelde, niet-verouderde kaarten met rolvlaggen weergeven. Handig om te bepalen welke kaarten in welke nodetypes kunnen worden gebruikt bij het bouwen van workflows.

**Parameters:** Geen

## Huidige mogelijkheden en roadmap

De Partner Card SDK wordt stapsgewijs uitgerold. Dit is waarop uw kaart vandaag kan rekenen en wat nog wordt aangesloten:

| Mogelijkheid | Status |
|------------|--------|
| **Veldcondities** — documentvelden lezen uit `context.document_fields` en in conditiekaarten vertakken op hun waarden | ✅ Geïmplementeerd |
| **Uitgaande HTTP-verzoeken** — externe services aanroepen vanuit een kaart | 🚧 Wordt momenteel toegevoegd |
| **Uitgebreide documentinformatie** — extra documentmetadata (naast `document_id`, `document_type` en `document_fields`) beschikbaar in `ExecutionContext` | 🚧 Wordt momenteel toegevoegd |
| **Hulpfuncties voor opzoeken in databasetabellen** — ingebouwde hulpfuncties om binnen een kaart stamgegevens- en lookuptabellen van DocBits te lezen | 📅 Gepland voor 1.1 |
| **Bronweergave van partnerkaarten** — alleen-lezenweergave van de ingediende partnerkaartcode in de DocBits-UI, zodat beheerders kunnen inzien wat ze goedkeuren | 📅 Gepland voor 1.1 |

{% hint style="info" %}
Als uw kaart een mogelijkheid nodig heeft die nog in ontwikkeling is, mislukt de validatie (verboden import, ontbrekend contextattribuut of sandboxbeperking) totdat het betreffende onderdeel beschikbaar is. Deze pagina wordt bijgewerkt zodra elke mogelijkheid wordt opgeleverd.
{% endhint %}

{% hint style="danger" %}
**Partnerkaarten voeren code van derden uit — gebruik op eigen risico.**

Kaarten die via de Partner Card SDK worden geüpload, worden slechts **gedeeltelijk door DocBits gevalideerd**. De validatiepijplijn controleert structuur, locales, imports, AST-patronen, afhankelijkheden, de eigen tests van de kaart en een gedragsrun (smoke test) in de sandbox — dit vormt **geen** volledige beveiligingsaudit en ook geen functionele garantie voor de bedrijfslogica van de kaart.

Zodra een organisatiebeheerder een partnerkaart goedkeurt, wordt deze beschikbaar voor elke organisatie op het platform en draait deze in de productiesandbox op echte documenten. Het goedkeuren en inschakelen van een partnerkaart is daarom een expliciete vertrouwensbeslissing van de goedkeurende beheerder. DocBits aanvaardt geen aansprakelijkheid voor gegevensverlies, onjuiste routering, gelekte informatie of enig ander gevolg veroorzaakt door een partnerkaart die u installeert of goedkeurt.

Als u niet de oorspronkelijke auteur van de kaart bent, controleer dan de broncode (en gebruik, zodra 1.1 is uitgebracht, de bronweergave van partnerkaarten) voordat u de kaart goedkeurt.
{% endhint %}
