# Card-SDK-Werkzeuge

Mit den Card SDK Tools können Sie benutzerdefinierte Partnerkarten über MCP erstellen, validieren, testen und verwalten. Partnerkarten erweitern DocFlow um benutzerdefinierte, in Python geschriebene Geschäftslogik.

## Lebenszyklus einer Karte

Eine Partnerkarte durchläuft diese Einreichungsstatus (`partner_status`):

| Status | Bedeutung | Sichtbarkeit in Workflows |
|-------|---------|---------------------|
| `validating` | Einreichung angenommen; die Validierungspipeline läuft. | Nur einreichende Organisation |
| `validated` | Alle Validierungsstufen bestanden. Wartet auf die Genehmigung durch einen Admin. | Nur einreichende Organisation |
| `rejected` | Validierung fehlgeschlagen oder ein Admin hat die Karte abgelehnt. Der Quellcode bleibt zur Prüfung erhalten. | Nur einreichende Organisation |
| `approved` | Ein Admin hat die Karte genehmigt; `enabled = true`. | **Alle Organisationen** |
| `disabled` | Zuvor genehmigte Karte, die ein Admin deaktiviert hat. | Nur einreichende Organisation |
| `deleted` | Soft-Delete; wird von Einreichungslisten nicht zurückgegeben. | Ausgeblendet |

{% hint style="warning" %}
**Sichtbarkeit für Organisationen:** Eine Partnerkarte steht Workflow-Knoten in `list_cards` erst zur Verfügung, nachdem sie **genehmigt** wurde. Genehmigte Partnerkarten sind für jede Organisation auf der Plattform sichtbar – die Genehmigung ist eine globale Aktivierung, keine pro Organisation. Nicht genehmigte Karten (validating, validated, rejected, disabled) sind nur für die Organisation sichtbar, die sie eingereicht hat.
{% endhint %}

Typischer Ablauf:

1. **Erstellen** Sie eine Karte mit `sdk_create_card` oder `sdk_import_github` – dies führt die Validierungspipeline aus und speichert die Karte mit `partner_status = validated` (bei einem Fehler mit `rejected`).
2. **Validieren** Sie mit `sdk_validate_card`, um eine vorhandene Karte erneut zu prüfen oder neuen Quellcode ohne Speichern zu testen (Dry-Run).
3. **Testen** Sie mit `sdk_test_card`, um die Karte in der Sandbox gegen einen Mock-Kontext auszuführen.
4. **Genehmigen** Sie mit `sdk_approve_card` (nur Organisations-Admin) – führt die AST- und Verhaltensvalidierung erneut aus und setzt dann `partner_status = approved` und `enabled = true`.
5. Nach der Genehmigung erscheint die Karte in `list_cards` für jede Organisation und kann aus Workflow-Knoten referenziert werden.

## Entwicklungs-Tools

### sdk\_create\_card

Erstellt eine neue Partnerkarte aus Quellcode und Manifesten. Führt die vollständige Validierungspipeline aus (siehe [Validierungsstufen](#sdk_validate_card) unten) und speichert die Karte in der Datenbank. Die Karte landet im Status `validated` und benötigt die Genehmigung eines Admins, bevor sie in Workflows verwendet werden kann.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `app_manifest` | object | Ja | App-Manifest mit id, name, version, Partnerinformationen |
| `card_manifest` | object | Ja | Karten-Manifest mit id, title, entry\_point, class\_name, args |
| `card_type` | string | Ja | `action` oder `condition` |
| `source_code` | string | Ja | Python-Quellcode (muss `PartnerCard` erweitern) |
| `test_code` | string | Ja | Pytest-Testcode für die Karte |
| `locales` | object | Nein | Übersetzungen, z. B. `{"en": {...}, "de": {...}}` |

**Beispiel für ein App-Manifest:**

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

**Beispiel für ein Karten-Manifest:**

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

| Status | Genommene Kante | Verwendung |
|--------|------------|------------|
| `SUCCESS` | `success` | Karte war erfolgreich – gilt für Bedingungen und Aktionen. |
| `FAILED` | `failed_condition` | **Nur Bedingungskarten.** Die Bedingung wurde als falsch ausgewertet – der Workflow nimmt den „Else“-Zweig. Aktionskarten haben keinen `failed_condition`-Anschluss; gibt eine Aktion `FAILED` zurück, hat die Ausführung keinen Weg mehr. |
| `ERROR` | `error` | Ein unerwarteter Laufzeitfehler (Exception). Gilt für Bedingungen und Aktionen. |

Kurz gesagt: Aktionen geben `SUCCESS` oder `ERROR` zurück; Bedingungen können zusätzlich `FAILED` zurückgeben.
{% endhint %}

### sdk\_validate\_card

Führt die Validierungspipeline für eine Partnerkarte aus, ohne zu speichern. Zwei Modi:

- **Modus A** – Eine vorhandene Karte anhand der ID validieren
- **Modus B** – Neuen Quellcode inline validieren

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Nein | UUID einer vorhandenen Karte (Modus A) |
| `app_manifest` | object | Nein | App-Manifest (Modus B) |
| `card_manifest` | object | Nein | Karten-Manifest (Modus B) |
| `card_type` | string | Nein | `action` oder `condition` (Modus B) |
| `source_code` | string | Nein | Python-Quellcode (Modus B) |
| `test_code` | string | Nein | Testcode (Modus B) |

{% hint style="info" %}
Geben Sie entweder nur `card_id` an (Modus A) oder `app_manifest` + `card_manifest` + `source_code` zusammen (Modus B).
{% endhint %}

**Validierungsstufen:**

1. **Structure** – Prüft das Dateilayout, das Manifest-Schema (`app.json`, `.docflowcompose/flow/...`) und ob die deklarierten Einstiegspunkte existieren.
2. **Locales** – Gleicht die in der Karte verwendeten Übersetzungsschlüssel mit den Dateien `locales/<lang>.json` ab; schlägt fehl, wenn ein Schlüssel in einer deklarierten Sprache fehlt.
3. **AST Analysis** – Durchläuft jede `.py`-Datei unter `src/` und prüft auf verbotene Imports, gefährliche Aufrufe sowie Anforderungen an Klassenhierarchie und Methodensignaturen.
4. **Dependencies** – Validiert, dass alle Imports auf erlaubte Module aus der SDK-Whitelist verweisen.
5. **Tests** – Führt die pytest-Suite der Karte mit reduzierten rlimits aus.
6. **Behavioral** – Führt die Karte in der Produktions-Sandbox gegen einen minimalen Mock-Kontext aus, um das Laufzeitverhalten zu bestätigen.

Die Stufen laufen der Reihe nach; die erste fehlschlagende Stufe bricht die übrigen ab. Stufe 6 (Behavioral) wird bei der Genehmigung erneut ausgeführt, als zusätzliche Sicherheitsprüfung, bevor die Karte aktiviert wird.

### sdk\_test\_card

Führt eine Partnerkarte in einer Sandbox-Umgebung mit einem Mock-Kontext aus. Die Sandbox erzwingt eingeschränkte Builtins, eine kuratierte Import-Allowlist, ein Ausführungs-Timeout und reduzierte Prozess-Ressourcenlimits – dieselben Einschränkungen, unter denen eine Karte nach der Genehmigung läuft.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Nein | UUID einer vorhandenen Karte (Modus A) |
| `source_code` | string | Nein | Quellcode für Inline-Tests (Modus B) |
| `class_name` | string | Nein | Klassenname für Inline-Tests (Modus B) |
| `variables` | object | Nein | Variablen, die an den Konstruktor der Karte übergeben werden |
| `mock_context` | object | Nein | Mock-Ausführungskontext |

**Felder des Mock-Kontexts:**

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

Das Tool liefert `execution_success` (ob die Sandbox die Karte vollständig ausgeführt hat – ein Timeout, ein Import-Verstoß oder eine ausgelöste Exception setzt den Wert auf `false`), `card_status` (der von `execute()` selbst zurückgegebene `CardStatus`), die `message` und `data` der Karte, die erfassten `logs` sowie `execution_time_ms`.

### sdk\_import\_github

Importiert eine Partner-App aus einem GitHub-Repository. Klont das Repository, liest `app.json` und importiert alle im Verzeichnis `.docflowcompose` gefundenen Karten.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `github_url` | string | Ja | GitHub-HTTPS-URL (z. B. `https://github.com/org/repo`) |
| `branch` | string | Nein | Zu klonender Branch (Standard: `main`) |
| `token` | string | Nein | GitHub-Token für private Repositories |

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

Listet alle Partnerkarten-Einreichungen der aktuellen Organisation auf.

**Parameter:** Keine

### sdk\_get\_submission\_status

Ruft den Validierungsstatus und den Bericht für eine bestimmte Partnerkarten-Einreichung ab.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partnerkarte |

### sdk\_approve\_card

Genehmigt eine validierte Partnerkarte und aktiviert sie. Die Genehmigung führt die AST- und Verhaltensvalidierung als zusätzliche Sicherheitsprüfung erneut aus, setzt `partner_status = approved` und `enabled = true` und registriert die Karte in der Laufzeit-Registry. Nach der Genehmigung erscheint die Karte in `list_cards` für **jede Organisation**, nicht nur für die einreichende.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partnerkarte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen. Die Karte muss sich im Status `validated` befinden. Abgelehnte Karten müssen erneut hochgeladen und erneut validiert werden, bevor sie genehmigt werden können.
{% endhint %}

### sdk\_reject\_card

Lehnt eine Partnerkarten-Einreichung ab und deaktiviert sie.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partnerkarte |
| `reason` | string | Nein | Grund der Ablehnung |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen.
{% endhint %}

### sdk\_delete\_submission

Löscht eine Partnerkarten-Einreichung per Soft-Delete, unabhängig von ihrem aktuellen Status. Setzt `partner_status = deleted`, `enabled = false` und `deprecated = true`. Die Zeile bleibt zu Prüfzwecken erhalten, wird aber in Einreichungslisten und in `list_cards` ausgeblendet.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `card_id` | string | Ja | UUID der Partnerkarte |

{% hint style="warning" %}
Erfordert Organisations-Admin-Berechtigungen.
{% endhint %}

### sdk\_list\_cards\_picker

Listet alle aktivierten, nicht veralteten Karten mit Rollen-Flags auf. Nützlich, um beim Erstellen von Workflows zu bestimmen, welche Karten in welchen Knotentypen verwendet werden können.

**Parameter:** Keine

## Aktuelle Fähigkeiten & Roadmap

Das Partner Card SDK wird schrittweise ausgerollt. Hier sehen Sie, worauf sich Ihre Karte heute verlassen kann und was noch umgesetzt wird:

| Fähigkeit | Status |
|------------|--------|
| **Feldbedingungen** – Dokumentfelder aus `context.document_fields` lesen und in Bedingungskarten anhand ihrer Werte verzweigen | ✅ Implementiert |
| **Ausgehende HTTP-Anfragen** – externe Dienste aus einer Karte heraus aufrufen | 🚧 Wird derzeit hinzugefügt |
| **Erweiterte Dokumentinformationen** – zusätzliche Dokument-Metadaten (über `document_id`, `document_type` und `document_fields` hinaus) im `ExecutionContext` | 🚧 Wird derzeit hinzugefügt |
| **Hilfsfunktionen für Datenbanktabellen-Lookups** – integrierte Helfer zum Lesen aus DocBits-Stammdaten-/Lookup-Tabellen innerhalb einer Karte | 📅 Geplant für 1.1 |
| **Quellcode-Ansicht für Partnerkarten** – schreibgeschützte Ansicht des eingereichten Partnerkarten-Codes in der DocBits-Oberfläche, damit Admins prüfen können, was sie genehmigen | 📅 Geplant für 1.1 |

{% hint style="info" %}
Benötigt Ihre Karte eine Fähigkeit, die noch in Arbeit ist, schlägt die Validierung fehl (verbotener Import, fehlendes Kontextattribut oder Sandbox-Einschränkung), bis der entsprechende Teil bereitgestellt wird. Diese Seite wird aktualisiert, sobald eine Fähigkeit ausgeliefert wird.
{% endhint %}

{% hint style="danger" %}
**Partnerkarten führen Code von Dritten aus – Nutzung auf eigenes Risiko.**

Über das Partner Card SDK hochgeladene Karten werden von DocBits nur **teilweise validiert**. Die Validierungspipeline prüft Struktur, Locales, Imports, AST-Muster, Abhängigkeiten, die eigenen Tests der Karte und einen Verhaltens-Smoke-Test in der Sandbox – sie stellt **keine** vollständige Sicherheitsprüfung und keine funktionale Garantie für die Geschäftslogik der Karte dar.

Sobald ein Organisations-Admin eine Partnerkarte genehmigt, steht sie jeder Organisation auf der Plattform zur Verfügung und läuft in der Produktions-Sandbox mit echten Dokumenten. Das Genehmigen und Aktivieren einer Partnerkarte ist daher eine ausdrückliche Vertrauensentscheidung des genehmigenden Admins. DocBits übernimmt keine Haftung für Datenverlust, falsches Routing, offengelegte Informationen oder sonstige Folgen, die durch eine von Ihnen installierte oder genehmigte Partnerkarte verursacht werden.

Sind Sie nicht der ursprüngliche Autor der Karte, prüfen Sie den Quellcode (und nutzen Sie, sobald 1.1 verfügbar ist, die Quellcode-Ansicht für Partnerkarten), bevor Sie sie genehmigen.
{% endhint %}
