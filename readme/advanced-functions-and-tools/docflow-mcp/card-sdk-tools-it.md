# Strumenti Card SDK

Gli strumenti Card SDK ti permettono di creare, validare, testare e gestire card partner personalizzate tramite MCP. Le card partner estendono DocFlow con logica di business personalizzata scritta in Python.

## Ciclo di Vita delle Card

Una card partner attraversa i seguenti stati di sottomissione (`partner_status`):

| Stato | Significato | Visibilita' nei workflow |
|-------|---------|---------------------|
| `validating` | Sottomissione accettata; la pipeline di validazione e' in esecuzione. | Solo organizzazione che ha sottomesso |
| `validated` | Tutte le fasi di validazione superate. In attesa di approvazione admin. | Solo organizzazione che ha sottomesso |
| `rejected` | Validazione fallita, oppure un admin ha rifiutato la card. Il codice sorgente viene conservato per l'ispezione. | Solo organizzazione che ha sottomesso |
| `approved` | L'admin ha approvato la card; `enabled = true`. | **Tutte le organizzazioni** |
| `disabled` | Card precedentemente approvata che un admin ha disattivato. | Solo organizzazione che ha sottomesso |
| `deleted` | Soft-deleted; non viene restituita dalle liste di sottomissione. | Nascosta |

{% hint style="warning" %}
**Visibilita' tra organizzazioni:** una card partner e' disponibile per i nodi di workflow in `list_cards` solo dopo essere stata **approvata**. Le card partner approvate sono visibili a ogni organizzazione sulla piattaforma -- l'approvazione e' un'attivazione globale, non per singola organizzazione. Le card non approvate (validating, validated, rejected, disabled) sono visibili solo all'organizzazione che le ha sottomesse.
{% endhint %}

Flusso tipico:

1. **Crea** una card con `sdk_create_card` o `sdk_import_github` -- esegue la pipeline di validazione e memorizza la card con `partner_status = validated` (o `rejected` in caso di errore).
2. **Valida** con `sdk_validate_card` per rivedere una card esistente o per testare a vuoto nuovo codice sorgente senza salvarlo.
3. **Testa** con `sdk_test_card` per eseguire la card nella sandbox contro un contesto fittizio.
4. **Approva** con `sdk_approve_card` (solo admin dell'organizzazione) -- riesegue le validazioni AST e comportamentale, poi imposta `partner_status = approved` ed `enabled = true`.
5. Una volta approvata, la card appare in `list_cards` per ogni organizzazione e puo' essere referenziata dai nodi di workflow.

## Strumenti di Sviluppo

### sdk\_create\_card

Crea una nuova card partner dal codice sorgente e dai manifesti. Esegue l'intera pipeline di validazione (vedi [Fasi di Validazione](#sdk_validate_card) piu' avanti) e salva la card nel database. La card si trova nello stato `validated` e richiede l'approvazione di un admin prima di poter essere usata nei workflow.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `app_manifest` | object | Si | Manifesto dell'app con id, nome, versione, info partner |
| `card_manifest` | object | Si | Manifesto della card con id, titolo, entry\_point, class\_name, args |
| `card_type` | string | Si | `action` o `condition` |
| `source_code` | string | Si | Codice sorgente Python (deve estendere `PartnerCard`) |
| `test_code` | string | Si | Codice di test Pytest per la card |
| `locales` | object | No | Traduzioni per le localizzazioni, es. `{"en": {...}, "de": {...}}` |

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
`CardStatus` ha tre valori che si mappano direttamente sugli archi del workflow:

| Status | Arco preso | Da usare per |
|--------|------------|------------|
| `SUCCESS` | `success` | La card ha avuto successo -- vale sia per le condizioni che per le azioni. |
| `FAILED` | `failed_condition` | **Solo card di condizione.** La condizione e' stata valutata come false -- il workflow prende il ramo "else". Le card di azione non hanno un handle `failed_condition`, quindi restituire `FAILED` da un'azione lascia l'esecuzione senza una via di uscita. |
| `ERROR` | `error` | Un errore di runtime inatteso (eccezione). Vale sia per le condizioni che per le azioni. |

In breve: le azioni restituiscono `SUCCESS` o `ERROR`; le condizioni possono inoltre restituire `FAILED`.
{% endhint %}

### sdk\_validate\_card

Esegue la pipeline di validazione su una card partner senza salvarla. Due modalita':

- **Modalita' A** -- Validare una card esistente tramite ID
- **Modalita' B** -- Validare nuovo codice sorgente in modalita' inline

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID di una card esistente (Modalita' A) |
| `app_manifest` | object | No | Manifesto dell'app (Modalita' B) |
| `card_manifest` | object | No | Manifesto della card (Modalita' B) |
| `card_type` | string | No | `action` o `condition` (Modalita' B) |
| `source_code` | string | No | Codice sorgente Python (Modalita' B) |
| `test_code` | string | No | Codice di test (Modalita' B) |

{% hint style="info" %}
Fornisci `card_id` da solo (Modalita' A) oppure `app_manifest` + `card_manifest` + `source_code` insieme (Modalita' B).
{% endhint %}

**Fasi di Validazione:**

1. **Structure** -- Verifica il layout dei file, lo schema del manifesto (`app.json`, `.docflowcompose/flow/...`) e che gli entry-point dichiarati esistano.
2. **Locales** -- Concilia le chiavi di traduzione utilizzate nella card con i file `locales/<lang>.json`; fallisce se una chiave manca in una lingua dichiarata.
3. **AST Analysis** -- Attraversa ogni file `.py` sotto `src/` e verifica import vietati, chiamate pericolose e requisiti di gerarchia di classi / firma dei metodi.
4. **Dependencies** -- Valida che tutti gli import si risolvano in moduli ammessi dalla allowlist dell'SDK.
5. **Tests** -- Esegue la suite pytest della card con rlimit ridotti.
6. **Behavioral** -- Esegue la card nella sandbox di produzione contro un contesto fittizio minimo per confermare il comportamento a runtime.

Le fasi vengono eseguite in sequenza; la prima fase fallita interrompe le successive. La Fase 6 (Behavioral) viene eseguita nuovamente in fase di approvazione come controllo di difesa in profondita' prima che la card venga attivata.

### sdk\_test\_card

Esegue una card partner in un ambiente sandbox con un contesto fittizio. La sandbox applica builtin limitati, una allowlist curata di import, un timeout di esecuzione e limiti ridotti per le risorse di processo -- gli stessi vincoli sotto cui gira una card una volta approvata.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID di una card esistente (Modalita' A) |
| `source_code` | string | No | Codice sorgente per il test inline (Modalita' B) |
| `class_name` | string | No | Nome della classe per il test inline (Modalita' B) |
| `variables` | object | No | Variabili da passare al costruttore della card |
| `mock_context` | object | No | Contesto di esecuzione fittizio |

**Campi del Mock Context:**

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

Lo strumento restituisce `execution_success` (indica se la sandbox ha eseguito la card fino al termine -- un timeout, una violazione di import o un'eccezione lanciata lo imposta a `false`), `card_status` (il `CardStatus` restituito da `execute()` stesso), il `message` e `data` della card, i `logs` catturati e `execution_time_ms`.

### sdk\_import\_github

Importa un'app partner da un repository GitHub. Clona il repo, legge `app.json` e importa tutte le card trovate nella directory `.docflowcompose`.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `github_url` | string | Si | URL HTTPS di GitHub (es. `https://github.com/org/repo`) |
| `branch` | string | No | Branch da clonare (default: `main`) |
| `token` | string | No | Token GitHub per repo privati |

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

## Strumenti di Gestione

### sdk\_list\_submissions

Elenca tutte le sottomissioni di card partner per l'organizzazione corrente.

**Parametri:** Nessuno

### sdk\_get\_submission\_status

Ottiene lo stato di validazione e il report per una specifica sottomissione di card partner.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | Si | UUID della card partner |

### sdk\_approve\_card

Approva una card partner validata e la attiva. L'approvazione esegue nuovamente la validazione AST e comportamentale come controllo di difesa in profondita', imposta `partner_status = approved` ed `enabled = true` e registra la card nel registro di runtime. Una volta approvata, la card appare in `list_cards` per **ogni organizzazione**, non solo per quella che l'ha sottomessa.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | Si | UUID della card partner |

{% hint style="warning" %}
Richiede privilegi di admin dell'organizzazione. La card deve essere nello stato `validated`. Le card rifiutate devono essere ricaricate e rivalidate prima di poter essere approvate.
{% endhint %}

### sdk\_reject\_card

Rifiuta una sottomissione di card partner e la disattiva.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | Si | UUID della card partner |
| `reason` | string | No | Motivo del rifiuto |

{% hint style="warning" %}
Richiede privilegi di admin dell'organizzazione.
{% endhint %}

### sdk\_delete\_submission

Esegue il soft-delete di una sottomissione di card partner, indipendentemente dallo stato attuale. Imposta `partner_status = deleted`, `enabled = false` e `deprecated = true`. La riga viene conservata a fini di audit, ma viene nascosta dalle liste di sottomissione e da `list_cards`.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `card_id` | string | Si | UUID della card partner |

{% hint style="warning" %}
Richiede privilegi di admin dell'organizzazione.
{% endhint %}

### sdk\_list\_cards\_picker

Elenca tutte le card abilitate e non deprecate con i flag di ruolo. Utile per determinare quali card possono essere usate in quali tipi di nodo durante la costruzione dei workflow.

**Parametri:** Nessuno

## Funzionalita' Attuali & Roadmap

Il Partner Card SDK viene rilasciato in modo incrementale. Ecco cosa puoi usare oggi nella tua card e cosa e' ancora in fase di integrazione:

| Funzionalita' | Stato |
|------------|--------|
| **Condizioni sui campi** -- leggere i campi documento da `context.document_fields` e diramare in base ai loro valori nelle card di condizione | ✅ Implementato |
| **Richieste HTTP in uscita** -- chiamare servizi esterni dall'interno di una card | 🚧 In fase di aggiunta |
| **Informazioni documento estese** -- metadati documento aggiuntivi (oltre a `document_id`, `document_type` e `document_fields`) esposti su `ExecutionContext` | 🚧 In fase di aggiunta |
| **Helper di lookup su tabelle del database** -- helper integrati per leggere dalle tabelle di master-data / lookup di DocBits dall'interno di una card | 📅 Pianificato per 1.1 |
| **Visualizzatore del codice della card partner** -- vista in sola lettura del codice della card partner sottomesso nell'interfaccia DocBits, per consentire agli admin di ispezionare cosa stanno approvando | 📅 Pianificato per 1.1 |

{% hint style="info" %}
Se la tua card necessita di una funzionalita' ancora in corso di sviluppo, la validazione fallira' (import vietato, attributo di contesto mancante o restrizione della sandbox) finche' la parte corrispondente non sara' rilasciata. Questa pagina verra' aggiornata man mano che ogni funzionalita' viene rilasciata.
{% endhint %}

{% hint style="danger" %}
**Le card partner eseguono codice di terze parti -- usale a tuo rischio.**

Le card caricate tramite il Partner Card SDK sono solo **parzialmente validate da DocBits**. La pipeline di validazione verifica struttura, locales, import, pattern AST, dipendenze, i test propri della card e un'esecuzione comportamentale di smoke nella sandbox -- **non** costituisce un audit di sicurezza completo ne' una garanzia funzionale della logica di business della card.

Una volta che un admin dell'organizzazione approva una card partner, questa diventa disponibile per ogni organizzazione sulla piattaforma e viene eseguita nella sandbox di produzione contro documenti reali. Approvare e abilitare una card partner e' quindi una decisione di fiducia esplicita da parte dell'admin che la approva. DocBits non si assume alcuna responsabilita' per perdita di dati, routing errato, informazioni divulgate o qualsiasi altro esito causato da una card partner che scegli di installare o approvare.

Se non sei l'autore originale della card, rivedi il codice sorgente (e, una volta rilasciata la 1.1, utilizza il visualizzatore del codice della card partner) prima di approvarla.
{% endhint %}
