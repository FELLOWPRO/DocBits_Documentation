# Card SDK Tools

Die Card SDK Tools ermoeglichen es Ihnen, benutzerdefinierte Partner-Karten ueber MCP zu erstellen, zu validieren, zu testen und zu verwalten. Partner-Karten erweitern DocFlow mit benutzerdefinierter Geschaeftslogik, die in Python geschrieben ist.

## Karten-Lebenszyklus

Eine Partner-Karte durchlaeuft folgende Einreichungszustaende (`partner_status`):

| Zustand | Bedeutung | Workflow-Sichtbarkeit |
|-------|---------|---------------------|
| `validating` | Einreichung angenommen; Validierungs-Pipeline laeuft. | Nur einreichende Organisation |
| `validated` | Alle Validierungsstufen bestanden. Wartet auf Admin-Genehmigung. | Nur einreichende Organisation |
| `rejected` | Validierung fehlgeschlagen oder ein Admin hat die Karte abgelehnt. Der Quellcode bleibt zur Pruefung erhalten. | Nur einreichende Organisation |
| `approved` | Admin hat die Karte genehmigt; `enabled = true`. | **Alle Organisationen** |
| `disabled` | Zuvor genehmigte Karte, die ein Admin deaktiviert hat. | Nur einreichende Organisation |
| `deleted` | Soft-geloescht; wird in Einreichungslisten nicht zurueckgegeben. | Ausgeblendet |

{% hint style="warning" %}
**Organisations-Sichtbarkeit:** Eine Partner-Karte steht Workflow-Knoten in `list_cards` erst zur Verfuegung, wenn sie **genehmigt** wurde. Genehmigte Partner-Karten sind fuer jede Organisation auf der Plattform sichtbar -- die Genehmigung ist eine plattformweite Aktivierung, nicht eine pro Organisation. Nicht genehmigte Karten (validating, validated, rejected, disabled) sind nur fuer die Organisation sichtbar, die sie eingereicht hat.
{% endhint %}

Typischer Ablauf:

1. **Erstellen** Sie eine Karte mit `sdk_create_card` oder `sdk_import_github` -- die Validierungs-Pipeline wird ausgefuehrt und die Karte mit `partner_status = validated` (oder `rejected` bei Fehler) gespeichert.
2. **Validieren** Sie mit `sdk_validate_card`, um eine bestehende Karte erneut zu pruefen oder neuen Quellcode ohne Speichern zu testen.
3. **Testen** Sie mit `sdk_test_card`, um die Karte in der Sandbox gegen einen Mock-Kontext auszufuehren.
4. **Genehmigen** Sie mit `sdk_approve_card` (nur Organisations-Admin) -- AST- und Verhaltensvalidierung werden erneut ausgefuehrt, dann werden `partner_status = approved` und `enabled = true` gesetzt.
5. Sobald die Karte genehmigt ist, erscheint sie in `list_cards` fuer jede Organisation und kann von Workflow-Knoten referenziert werden.

## Entwicklungs-Tools

### sdk\_create\_card

Eine neue Partner-Karte aus Quellcode und Manifesten erstellen. Fuehrt die vollstaendige Validierungs-Pipeline aus (siehe [Validierungsstufen](#sdk_validate_card) weiter unten) und speichert die Karte in der Datenbank. Die Karte landet im Zustand `validated` und benoetigt eine Admin-Genehmigung, bevor sie in Workflows verwendet werden kann.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `app_manifest` | object | Ja | App-Manifest mit id, name, version, Partner-Info |
| `card_manifest` | object | Ja | Karten-Manifest mit id, title, entry\_point, class\_name, args |
| `card_type` | string | Ja | `action` oder `condition` |
| `source_code` | string | Ja | Python-Quellcode (muss `PartnerCard` erweitern) |
| `test_code` | string | Ja | Pytest-Testcode fuer die Karte |
| `locales` | object | Nein | Uebersetzungen, z.B. `{"en": {...}, "de": {...}}` |

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
`CardStatus` hat drei Werte, die direkt auf Workflow-Kanten abgebildet werden:

| Status | Verwendete Kante | Wofuer |
|--------|------------|------------|
| `SUCCESS` | `success` | Karte war erfolgreich -- gilt sowohl fuer Bedingungen als auch fuer Aktionen. |
| `FAILED` | `failed_condition` | **Nur Bedingungskarten.** Die Bedingung wurde als false ausgewertet -- der Workflow nimmt den "else"-Zweig. Aktionskarten haben kein `failed_condition`-Handle, daher fuehrt ein `FAILED` aus einer Aktion zu einem Lauf ohne Ausgang. |
| `ERROR` | `error` | Ein unerwarteter Laufzeitfehler (Exception). Gilt sowohl fuer Bedingungen als auch fuer Aktionen. |

Kurz gesagt: Aktionen geben `SUCCESS` oder `ERROR` zurueck; Bedingungen koennen zusaetzlich `FAILED` zurueckgeben.
{% endhint %}

### sdk\_validate\_card

Die Validierungs-Pipeline auf einer Partner-Karte ausfuehren, ohne sie zu speichern. Zwei Modi:

- **Modus A** -- Eine bestehende Karte per ID validieren
- **Modus B** -- Neuen Quellcode inline validieren

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Nein | UUID einer bestehenden Karte (Modus A) |
| `app_manifest` | object | Nein | App-Manifest (Modus B) |
| `card_manifest` | object | Nein | Karten-Manifest (Modus B) |
| `card_type` | string | Nein | `action` oder `condition` (Modus B) |
| `source_code` | string | Nein | Python-Quellcode (Modus B) |
| `test_code` | string | Nein | Testcode (Modus B) |

{% hint style="info" %}
Geben Sie entweder `card_id` alleine an (Modus A) oder `app_manifest` + `card_manifest` + `source_code` zusammen (Modus B).
{% endhint %}

**Validierungsstufen:**

1. **Structure** -- Prueft das Datei-Layout, das Manifest-Schema (`app.json`, `.docflowcompose/flow/...`) und ob die deklarierten Entry-Points existieren.
2. **Locales** -- Gleicht Uebersetzungs-Keys, die in der Karte verwendet werden, mit den `locales/<lang>.json`-Dateien ab; schlaegt fehl, wenn ein Key in einer deklarierten Sprache fehlt.
3. **AST Analysis** -- Geht jede `.py`-Datei unter `src/` durch und prueft auf verbotene Imports, gefaehrliche Aufrufe und Anforderungen an Klassen-Hierarchie / Methoden-Signaturen.
4. **Dependencies** -- Validiert, dass alle Imports auf erlaubte Module aus der SDK-Allowlist aufloesen.
5. **Tests** -- Fuehrt die pytest-Suite der Karte unter reduzierten rlimits aus.
6. **Behavioral** -- Fuehrt die Karte in der Produktions-Sandbox gegen einen minimalen Mock-Kontext aus, um das Laufzeitverhalten zu bestaetigen.

Die Stufen laufen in dieser Reihenfolge; die erste fehlschlagende Stufe bricht die restlichen ab. Stufe 6 (Behavioral) wird ebenfalls zum Zeitpunkt der Genehmigung als Tiefenverteidigungs-Pruefung erneut ausgefuehrt, bevor die Karte aktiviert wird.

### sdk\_test\_card

Eine Partner-Karte in einer Sandbox-Umgebung mit einem Mock-Kontext ausfuehren. Die Sandbox erzwingt eingeschraenkte Builtins, eine kuratierte Import-Allowlist, ein Ausfuehrungs-Timeout sowie reduzierte Prozess-Ressourcenlimits -- dieselben Einschraenkungen, unter denen eine Karte nach der Genehmigung laeuft.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Nein | UUID einer bestehenden Karte (Modus A) |
| `source_code` | string | Nein | Quellcode fuer Inline-Tests (Modus B) |
| `class_name` | string | Nein | Klassenname fuer Inline-Tests (Modus B) |
| `variables` | object | Nein | Variablen, die an den Karten-Konstruktor uebergeben werden |
| `mock_context` | object | Nein | Mock-Ausfuehrungskontext |

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

Das Tool gibt `execution_success` zurueck (ob die Sandbox die Karte vollstaendig ausfuehren konnte -- ein Timeout, eine Import-Verletzung oder eine ausgeloeste Exception setzen es auf `false`), `card_status` (den von `execute()` selbst zurueckgegebenen `CardStatus`), die `message` und `data` der Karte, die erfassten `logs` sowie `execution_time_ms`.

### sdk\_import\_github

Eine Partner-App aus einem GitHub-Repository importieren. Klont das Repo, liest `app.json` und importiert alle Karten, die im Verzeichnis `.docflowcompose` gefunden werden.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `github_url` | string | Ja | GitHub-HTTPS-URL (z.B. `https://github.com/org/repo`) |
| `branch` | string | Nein | Zu klonender Branch (Standard: `main`) |
| `token` | string | Nein | GitHub-Token fuer private Repos |

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

## Verwaltungs-Tools

### sdk\_list\_submissions

Alle Partner-Karten-Einreichungen fuer die aktuelle Organisation auflisten.

**Parameter:** Keine

### sdk\_get\_submission\_status

Validierungsstatus und Bericht fuer eine bestimmte Partner-Karten-Einreichung abrufen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partner-Karte |

### sdk\_approve\_card

Eine validierte Partner-Karte genehmigen und aktivieren. Die Genehmigung fuehrt AST- und Verhaltensvalidierung als Tiefenverteidigungs-Pruefung erneut aus, setzt `partner_status = approved` und `enabled = true` und registriert die Karte in der Laufzeit-Registry. Sobald genehmigt, erscheint die Karte in `list_cards` fuer **jede Organisation**, nicht nur fuer die einreichende.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partner-Karte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Rechte. Die Karte muss im Zustand `validated` sein. Abgelehnte Karten muessen erneut hochgeladen und erneut validiert werden, bevor sie genehmigt werden koennen.
{% endhint %}

### sdk\_reject\_card

Eine Partner-Karten-Einreichung ablehnen und deaktivieren.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partner-Karte |
| `reason` | string | Nein | Grund fuer die Ablehnung |

{% hint style="warning" %}
Erfordert Organisations-Admin-Rechte.
{% endhint %}

### sdk\_delete\_submission

Eine Partner-Karten-Einreichung soft-loeschen, unabhaengig vom aktuellen Zustand. Setzt `partner_status = deleted`, `enabled = false` und `deprecated = true`. Die Zeile bleibt zu Audit-Zwecken erhalten, wird aber in Einreichungslisten und `list_cards` ausgeblendet.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partner-Karte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Rechte.
{% endhint %}

### sdk\_list\_cards\_picker

Alle aktivierten, nicht veralteten Karten mit Rollen-Flags auflisten. Hilfreich, um zu bestimmen, welche Karten in welchen Knotentypen beim Aufbau von Workflows verwendet werden koennen.

**Parameter:** Keine

## Aktuelle Faehigkeiten & Roadmap

Das Partner Card SDK wird schrittweise eingefuehrt. Hier sehen Sie, worauf Ihre Karte heute zurueckgreifen kann und was gerade erst verkabelt wird:

| Faehigkeit | Status |
|------------|--------|
| **Feld-Bedingungen** -- Dokumentfelder aus `context.document_fields` lesen und in Bedingungskarten anhand ihrer Werte verzweigen | ✅ Implementiert |
| **Ausgehende HTTP-Anfragen** -- externe Dienste aus einer Karte heraus aufrufen | 🚧 Wird derzeit hinzugefuegt |
| **Erweiterte Dokument-Informationen** -- zusaetzliche Dokument-Metadaten (ueber `document_id`, `document_type` und `document_fields` hinaus) auf `ExecutionContext` verfuegbar | 🚧 Wird derzeit hinzugefuegt |
| **Datenbank-Lookup-Helfer** -- eingebaute Helfer zum Lesen aus DocBits-Stammdaten- / Lookup-Tabellen innerhalb einer Karte | 📅 Geplant fuer 1.1 |
| **Partner-Karten-Quellansicht** -- schreibgeschuetzte Ansicht des eingereichten Partner-Karten-Codes in der DocBits-Oberflaeche, damit Admins pruefen koennen, was sie genehmigen | 📅 Geplant fuer 1.1 |

{% hint style="info" %}
Wenn Ihre Karte eine Faehigkeit benoetigt, die noch in Arbeit ist, wird sie die Validierung nicht bestehen (verbotener Import, fehlendes Kontext-Attribut oder Sandbox-Beschraenkung), bis das entsprechende Stueck einsatzbereit ist. Diese Seite wird aktualisiert, sobald eine Faehigkeit ausgeliefert wird.
{% endhint %}

{% hint style="danger" %}
**Partner-Karten fuehren Drittanbieter-Code aus -- Nutzung auf eigene Gefahr.**

Karten, die ueber das Partner Card SDK hochgeladen werden, sind nur **teilweise von DocBits validiert**. Die Validierungs-Pipeline prueft Struktur, Locales, Imports, AST-Muster, Abhaengigkeiten, die eigenen Tests der Karte und einen verhaltensbezogenen Smoke-Run in der Sandbox -- sie stellt **kein** vollstaendiges Security-Audit und keine funktionale Garantie der Geschaeftslogik der Karte dar.

Sobald ein Organisations-Admin eine Partner-Karte genehmigt, steht sie jeder Organisation auf der Plattform zur Verfuegung und laeuft in der Produktions-Sandbox gegen echte Dokumente. Die Genehmigung und Aktivierung einer Partner-Karte ist daher eine ausdrueckliche Vertrauensentscheidung des genehmigenden Admins. DocBits uebernimmt keine Haftung fuer Datenverlust, fehlerhaftes Routing, durchgesickerte Informationen oder andere Folgen, die durch eine Partner-Karte verursacht werden, die Sie installieren oder genehmigen.

Wenn Sie nicht der urspruengliche Autor der Karte sind, pruefen Sie den Quellcode (und sobald 1.1 ausgeliefert wird, die Partner-Karten-Quellansicht), bevor Sie sie genehmigen.
{% endhint %}
