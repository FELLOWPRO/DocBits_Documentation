# Strumenti SDK Card

Gli strumenti Card SDK ti permettono di creare, validare, testare e gestire card partner personalizzate tramite MCP. Le card partner estendono DocFlow con logica di business personalizzata scritta in Python.

## Ciclo di Vita delle Card

```
Crea → Valida → Testa → Approva → Usa nei Workflow
```

1. **Crea** una card con `sdk_create_card` o `sdk_import_github`
2. **Valida** con `sdk_validate_card` (validazione in 5 fasi)
3. **Testa** con `sdk_test_card` (esecuzione in sandbox)
4. **Approva** con `sdk_approve_card` (richiesto admin)
5. La card e' ora disponibile in `list_cards` e puo' essere utilizzata nei workflow

## Strumenti di Sviluppo

### sdk\_create\_card

Crea una nuova card partner dal codice sorgente e dai manifesti. Esegue la validazione completa in 5 fasi e salva la card nel database. La card inizia in stato di attesa e richiede l'approvazione di un admin per essere attivata.

**Parametri:**

| Parametro       | Tipo   | Obbligatorio | Descrizione                                                          |
| --------------- | ------ | ------------ | -------------------------------------------------------------------- |
| `app_manifest`  | object | Si           | Manifesto dell'app con id, nome, versione, info partner              |
| `card_manifest` | object | Si           | Manifesto della card con id, titolo, entry\_point, class\_name, args |
| `card_type`     | string | Si           | `action` o `condition`                                               |
| `source_code`   | string | Si           | Codice sorgente Python (deve estendere `PartnerCard`)                |
| `test_code`     | string | Si           | Codice di test Pytest per la card                                    |
| `locales`       | object | No           | Traduzioni per le localizzazioni, es. `{"en": {...}, "de": {...}}`   |

**Esempio di Manifesto App:**

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

**Esempio di Manifesto Card:**

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

**Esempio di Codice Sorgente:**

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

**Esempio di Risposta:**

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

Esegui la validazione in 5 fasi su una card partner senza salvare. Due modalita':

* **Modalita' A** -- Valida una card esistente tramite ID
* **Modalita' B** -- Valida nuovo codice sorgente inline

**Parametri:**

| Parametro       | Tipo   | Obbligatorio | Descrizione                             |
| --------------- | ------ | ------------ | --------------------------------------- |
| `card_id`       | string | No           | UUID della card esistente (Modalita' A) |
| `app_manifest`  | object | No           | Manifesto dell'app (Modalita' B)        |
| `card_manifest` | object | No           | Manifesto della card (Modalita' B)      |
| `card_type`     | string | No           | `action` o `condition` (Modalita' B)    |
| `source_code`   | string | No           | Codice sorgente Python (Modalita' B)    |
| `test_code`     | string | No           | Codice di test (Modalita' B)            |

{% hint style="info" %}
Fornisci `card_id` da solo (Modalita' A) oppure `app_manifest` + `card_manifest` + `source_code` insieme (Modalita' B).
{% endhint %}

**Fasi di Validazione:**

1. **Struttura** -- Verifica il layout dei file, lo schema del manifesto, i file richiesti
2. **Analisi AST** -- Controlla la sintassi Python, la gerarchia delle classi, le firme dei metodi
3. **Dipendenze** -- Valida gli import rispetto ai moduli consentiti
4. **Test** -- Esegue la suite di test della card
5. **Comportamentale** -- Esegue la card in sandbox per verificare il comportamento a runtime

### sdk\_test\_card

Esegui una card partner in un ambiente sandbox con un contesto simulato. Utilizza lo stesso modello di sicurezza della produzione (builtin limitati, whitelist degli import, timeout di 10 secondi).

**Parametri:**

| Parametro      | Tipo   | Obbligatorio | Descrizione                                     |
| -------------- | ------ | ------------ | ----------------------------------------------- |
| `card_id`      | string | No           | UUID della card esistente (Modalita' A)         |
| `source_code`  | string | No           | Codice sorgente per test inline (Modalita' B)   |
| `class_name`   | string | No           | Nome della classe per test inline (Modalita' B) |
| `variables`    | object | No           | Variabili da passare al costruttore della card  |
| `mock_context` | object | No           | Contesto di esecuzione simulato                 |

**Campi del Contesto Simulato:**

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

**Esempio di Risposta:**

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

Importa un'app partner da un repository GitHub. Clona il repository, legge `app.json` e importa tutte le card trovate nella directory `.docflowcompose`.

**Parametri:**

| Parametro    | Tipo   | Obbligatorio | Descrizione                                             |
| ------------ | ------ | ------------ | ------------------------------------------------------- |
| `github_url` | string | Si           | URL HTTPS di GitHub (es. `https://github.com/org/repo`) |
| `branch`     | string | No           | Branch da clonare (predefinito: `main`)                 |
| `token`      | string | No           | Token GitHub per repository privati                     |

**Struttura del Repository Attesa:**

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

**Esempio di Risposta:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Strumenti di Gestione

### sdk\_list\_submissions

Elenca tutte le sottomissioni di card partner per l'organizzazione corrente.

**Parametri:** Nessuno

**Esempio di Risposta:**

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

Ottieni lo stato di validazione e il report per una specifica sottomissione di card partner.

**Parametri:**

| Parametro | Tipo   | Obbligatorio | Descrizione             |
| --------- | ------ | ------------ | ----------------------- |
| `card_id` | string | Si           | UUID della card partner |

**Esempio di Risposta:**

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

Approva una card partner validata e attivala per l'utilizzo nei workflow. La card viene registrata nel registro runtime e diventa disponibile in `list_cards`.

**Parametri:**

| Parametro | Tipo   | Obbligatorio | Descrizione             |
| --------- | ------ | ------------ | ----------------------- |
| `card_id` | string | Si           | UUID della card partner |

{% hint style="warning" %}
Richiede permessi di amministratore dell'organizzazione. La card deve essere in stato `validated` o `rejected`.
{% endhint %}

### sdk\_reject\_card

Rifiuta una sottomissione di card partner e disattivala.

**Parametri:**

| Parametro | Tipo   | Obbligatorio | Descrizione             |
| --------- | ------ | ------------ | ----------------------- |
| `card_id` | string | Si           | UUID della card partner |
| `reason`  | string | No           | Motivo del rifiuto      |

{% hint style="warning" %}
Richiede permessi di amministratore dell'organizzazione.
{% endhint %}

### sdk\_delete\_submission

Disattiva o elimina una sottomissione di card partner. Le card rifiutate o disabilitate vengono eliminate fisicamente dal database. Le card attive vengono prima disattivate.

**Parametri:**

| Parametro | Tipo   | Obbligatorio | Descrizione             |
| --------- | ------ | ------------ | ----------------------- |
| `card_id` | string | Si           | UUID della card partner |

{% hint style="warning" %}
Richiede permessi di amministratore dell'organizzazione.
{% endhint %}

### sdk\_list\_cards\_picker

Elenca tutte le card abilitate e non deprecate con flag di ruolo. Utile per determinare quali card possono essere utilizzate in quali tipi di nodo durante la creazione dei workflow.

**Parametri:** Nessuno

**Esempio di Risposta:**

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
