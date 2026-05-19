# Card SDK Tools

De Card SDK-tools stellen u in staat om aangepaste partnerkaarten aan te maken, te valideren, te testen en te beheren via MCP. Partnerkaarten breiden DocFlow uit met aangepaste bedrijfslogica geschreven in Python.

## Levenscyclus van kaarten

Een partnerkaart doorloopt de volgende inzendstatussen (`partner_status`):

| Status | Betekenis | Workflow-zichtbaarheid |
|-------|---------|---------------------|
| `validating` | Inzending geaccepteerd; validatie-pipeline loopt. | Alleen inzendende organisatie |
| `validated` | Alle validatiefasen geslaagd. Wacht op goedkeuring van admin. | Alleen inzendende organisatie |
| `rejected` | Validatie mislukt of een admin heeft de kaart afgewezen. De broncode blijft bewaard voor inspectie. | Alleen inzendende organisatie |
| `approved` | Admin heeft de kaart goedgekeurd; `enabled = true`. | **Alle organisaties** |
| `disabled` | Eerder goedgekeurde kaart die een admin heeft gedeactiveerd. | Alleen inzendende organisatie |
| `deleted` | Soft-verwijderd; verschijnt niet in inzendingslijsten. | Verborgen |

{% hint style="warning" %}
**Zichtbaarheid tussen organisaties:** Een partnerkaart is pas beschikbaar voor workflow-knopen in `list_cards` zodra deze is **goedgekeurd**. Goedgekeurde partnerkaarten zijn zichtbaar voor elke organisatie op het platform — goedkeuring is een globale activering, niet een activering per organisatie. Niet-goedgekeurde kaarten (validating, validated, rejected, disabled) zijn alleen zichtbaar voor de organisatie die ze heeft ingezonden.
{% endhint %}

Typische workflow:

1. **Aanmaken** van een kaart met `sdk_create_card` of `sdk_import_github` — voert de validatie-pipeline uit en slaat de kaart op met `partner_status = validated` (of `rejected` bij een fout).
2. **Valideren** met `sdk_validate_card` om een bestaande kaart opnieuw te controleren of nieuwe broncode droog te draaien zonder op te slaan.
3. **Testen** met `sdk_test_card` om de kaart uit te voeren in de sandbox tegen een mock-context.
4. **Goedkeuren** met `sdk_approve_card` (alleen organisatie-admin) — voert AST- en gedragsvalidatie opnieuw uit en stelt vervolgens `partner_status = approved` en `enabled = true` in.
5. Zodra goedgekeurd, verschijnt de kaart in `list_cards` voor elke organisatie en kan deze worden gerefereerd vanuit workflow-knopen.

## Ontwikkeltools

### sdk\_create\_card

Een nieuwe partnerkaart aanmaken vanuit broncode en manifesten. Voert de volledige validatie-pipeline uit (zie [Validatiefasen](#sdk_validate_card) hieronder) en slaat de kaart op in de database. De kaart komt in de status `validated` terecht en vereist goedkeuring van een admin voordat deze in workflows kan worden gebruikt.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `app_manifest` | object | Ja | App-manifest met id, naam, versie, partnerinfo |
| `card_manifest` | object | Ja | Kaartmanifest met id, titel, entry\_point, class\_name, args |
| `card_type` | string | Ja | `action` of `condition` |
| `source_code` | string | Ja | Python-broncode (moet `PartnerCard` uitbreiden) |
| `test_code` | string | Ja | Pytest-testcode voor de kaart |
| `locales` | object | Nee | Lokale vertalingen, bijv. `{"en": {...}, "de": {...}}` |

**Voorbeeld van app-manifest:**

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

**Voorbeeld van kaartmanifest:**

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

**Voorbeeld van broncode:**

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
`CardStatus` heeft drie waarden die rechtstreeks gemapt worden op workflow-kanten:

| Status | Genomen kant | Te gebruiken voor |
|--------|------------|------------|
| `SUCCESS` | `success` | Kaart geslaagd — geldt voor zowel condities als acties. |
| `FAILED` | `failed_condition` | **Alleen conditiekaarten.** De conditie werd als false geëvalueerd — de workflow neemt de "else"-tak. Actiekaarten hebben geen `failed_condition`-handle, dus het terugsturen van `FAILED` vanuit een actie laat de uitvoering zonder uitweg. |
| `ERROR` | `error` | Een onverwachte runtimefout (exception). Geldt voor zowel condities als acties. |

Kort samengevat: acties retourneren `SUCCESS` of `ERROR`; condities kunnen daarnaast `FAILED` retourneren.
{% endhint %}

### sdk\_validate\_card

De validatie-pipeline uitvoeren op een partnerkaart zonder deze op te slaan. Twee modi:

- **Modus A** — Een bestaande kaart valideren op ID
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
Geef ofwel `card_id` alleen op (Modus A) of `app_manifest` + `card_manifest` + `source_code` samen (Modus B).
{% endhint %}

**Validatiefasen:**

1. **Structure** — Verifieert de bestandsstructuur, het manifest-schema (`app.json`, `.docflowcompose/flow/...`) en of de gedeclareerde entry points bestaan.
2. **Locales** — Stemt vertaalsleutels die in de kaart worden gebruikt af op de `locales/<lang>.json`-bestanden; faalt als een sleutel ontbreekt in een gedeclareerde taal.
3. **AST Analysis** — Loopt elk `.py`-bestand onder `src/` door en controleert op verboden imports, gevaarlijke aanroepen en vereisten voor klassehiërarchie / methode-signaturen.
4. **Dependencies** — Valideert dat alle imports oplossen naar toegestane modules uit de SDK-allowlist.
5. **Tests** — Voert de pytest-suite van de kaart uit onder gereduceerde rlimits.
6. **Behavioral** — Voert de kaart uit in de productie-sandbox tegen een minimale mock-context om runtime-gedrag te bevestigen.

Fasen lopen in volgorde; de eerste falende fase sluit de overige kort. Fase 6 (Behavioral) wordt ook opnieuw uitgevoerd op het moment van goedkeuring als defense-in-depth-controle voordat de kaart wordt geactiveerd.

### sdk\_test\_card

Een partnerkaart uitvoeren in een sandbox-omgeving met een mock-context. De sandbox dwingt beperkte builtins, een gecureerde import-allowlist, een uitvoeringstime-out en gereduceerde proceslimieten af — dezelfde beperkingen waaronder een kaart draait nadat deze is goedgekeurd.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Nee | UUID van bestaande kaart (Modus A) |
| `source_code` | string | Nee | Broncode voor inline test (Modus B) |
| `class_name` | string | Nee | Klassenaam voor inline test (Modus B) |
| `variables` | object | Nee | Variabelen die aan de constructor van de kaart worden doorgegeven |
| `mock_context` | object | Nee | Mock-uitvoeringscontext |

**Velden van de mock-context:**

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

De tool retourneert `execution_success` (geeft aan of de sandbox de kaart tot het einde heeft uitgevoerd — een time-out, importschending of opgeworpen exception zet dit op `false`), `card_status` (de `CardStatus` die door `execute()` zelf wordt geretourneerd), de `message` en `data` van de kaart, de opgenomen `logs` en `execution_time_ms`.

### sdk\_import\_github

Een partner-app importeren vanuit een GitHub-repository. Kloont de repo, leest `app.json` en importeert alle kaarten gevonden in de map `.docflowcompose`.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `github_url` | string | Ja | GitHub HTTPS-URL (bijv. `https://github.com/org/repo`) |
| `branch` | string | Nee | Te klonen branch (standaard: `main`) |
| `token` | string | Nee | GitHub-token voor privé-repo's |

**Verwachte repository-structuur:**

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

Alle inzendingen van partnerkaarten voor de huidige organisatie opvragen.

**Parameters:** Geen

### sdk\_get\_submission\_status

Validatiestatus en rapport opvragen voor een specifieke inzending van een partnerkaart.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

### sdk\_approve\_card

Een gevalideerde partnerkaart goedkeuren en activeren. Goedkeuring voert AST- en gedragsvalidatie opnieuw uit als defense-in-depth-controle, stelt `partner_status = approved` en `enabled = true` in en registreert de kaart in het runtime-register. Eenmaal goedgekeurd verschijnt de kaart in `list_cards` voor **elke organisatie**, niet alleen voor de inzendende organisatie.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatie-adminrechten. De kaart moet zich in de status `validated` bevinden. Afgewezen kaarten moeten opnieuw worden geüpload en gevalideerd voordat ze kunnen worden goedgekeurd.
{% endhint %}

### sdk\_reject\_card

Een inzending van een partnerkaart afwijzen en deactiveren.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |
| `reason` | string | Nee | Reden voor afwijzing |

{% hint style="warning" %}
Vereist organisatie-adminrechten.
{% endhint %}

### sdk\_delete\_submission

Een inzending van een partnerkaart soft-verwijderen, ongeacht de huidige status. Stelt `partner_status = deleted`, `enabled = false` en `deprecated = true` in. De rij blijft bewaard voor auditdoeleinden, maar wordt verborgen uit inzendingslijsten en `list_cards`.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `card_id` | string | Ja | UUID van de partnerkaart |

{% hint style="warning" %}
Vereist organisatie-adminrechten.
{% endhint %}

### sdk\_list\_cards\_picker

Alle ingeschakelde, niet-verouderde kaarten met rolvlaggen opvragen. Handig om te bepalen welke kaarten in welke knooptypen kunnen worden gebruikt bij het opbouwen van workflows.

**Parameters:** Geen

## Huidige mogelijkheden & roadmap

De Partner Card SDK wordt stapsgewijs uitgerold. Hier ziet u waar uw kaart vandaag op kan vertrouwen en wat nog in de maak is:

| Mogelijkheid | Status |
|------------|--------|
| **Veldvoorwaarden** — documentvelden lezen uit `context.document_fields` en op basis van hun waarden vertakken in conditiekaarten | ✅ Geïmplementeerd |
| **Uitgaande HTTP-verzoeken** — externe diensten aanroepen vanuit een kaart | 🚧 Wordt momenteel toegevoegd |
| **Uitgebreide documentinformatie** — aanvullende document-metadata (naast `document_id`, `document_type` en `document_fields`) blootgesteld op `ExecutionContext` | 🚧 Wordt momenteel toegevoegd |
| **Helpers voor database-tabel-lookups** — ingebouwde helpers om te lezen uit DocBits master-data- / lookup-tabellen vanuit een kaart | 📅 Gepland voor 1.1 |
| **Bronviewer voor partnerkaarten** — alleen-lezen weergave van de ingezonden broncode van de partnerkaart in de DocBits-interface, zodat admins kunnen inspecteren wat zij goedkeuren | 📅 Gepland voor 1.1 |

{% hint style="info" %}
Als uw kaart een mogelijkheid nodig heeft die nog in ontwikkeling is, zal deze de validatie niet doorstaan (verboden import, ontbrekend context-attribuut of sandbox-beperking) totdat het bijbehorende onderdeel beschikbaar is. Deze pagina wordt bijgewerkt zodra elke mogelijkheid wordt uitgebracht.
{% endhint %}

{% hint style="danger" %}
**Partnerkaarten voeren code van derden uit — gebruik op eigen risico.**

Kaarten die via de Partner Card SDK worden geüpload, worden slechts **gedeeltelijk door DocBits gevalideerd**. De validatie-pipeline controleert structuur, locales, imports, AST-patronen, dependencies, de eigen tests van de kaart en een gedrags-smoke-uitvoering in de sandbox — het vormt **geen** volledige security-audit en geen functionele garantie van de bedrijfslogica van de kaart.

Zodra een organisatie-admin een partnerkaart goedkeurt, wordt deze beschikbaar voor elke organisatie op het platform en draait deze in de productie-sandbox tegen echte documenten. Het goedkeuren en inschakelen van een partnerkaart is daarom een expliciete vertrouwensbeslissing van de goedkeurende admin. DocBits aanvaardt geen aansprakelijkheid voor gegevensverlies, onjuiste routing, gelekte informatie of enige andere gevolgen die worden veroorzaakt door een partnerkaart die u kiest te installeren of goed te keuren.

Als u niet de oorspronkelijke auteur van de kaart bent, beoordeel dan de broncode (en, zodra 1.1 wordt uitgebracht, gebruik de bronviewer voor partnerkaarten) voordat u deze goedkeurt.
{% endhint %}
