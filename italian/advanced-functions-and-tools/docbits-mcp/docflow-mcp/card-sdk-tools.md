# Strumenti Card SDK

Gli strumenti Card SDK ti permettono di creare, validare, testare e gestire schede partner personalizzate tramite MCP. Le schede partner estendono DocFlow con logica di business personalizzata scritta in Python.

## Ciclo di Vita della Scheda

Una scheda partner attraversa questi stati di invio (`partner_status`):

| Stato | Significato | Visibilità nel workflow |
|-------|-------------|-------------------------|
| `validating` | Invio accettato; la pipeline di validazione è in esecuzione. | Solo l'organizzazione che ha inviato |
| `validated` | Tutte le fasi di validazione sono state superate. In attesa dell'approvazione dell'amministratore. | Solo l'organizzazione che ha inviato |
| `rejected` | La validazione non è riuscita oppure un amministratore ha rifiutato la scheda. Il sorgente viene conservato per l'ispezione. | Solo l'organizzazione che ha inviato |
| `approved` | L'amministratore ha approvato la scheda; `enabled = true`. | **Tutte le organizzazioni** |
| `disabled` | Scheda precedentemente approvata che un amministratore ha disattivato. | Solo l'organizzazione che ha inviato |
| `deleted` | Eliminata in modo logico (soft-delete); non viene restituita dagli elenchi degli invii. | Nascosta |

{% hint style="warning" %}
**Visibilità per organizzazione:** Una scheda partner è disponibile per i nodi del workflow in `list_cards` solo dopo essere stata **approvata**. Le schede partner approvate sono visibili a ogni organizzazione della piattaforma — l'approvazione è un'attivazione globale, non per singola organizzazione. Le schede non approvate (validating, validated, rejected, disabled) sono visibili solo all'organizzazione che le ha inviate.
{% endhint %}

Flusso tipico:

1. **Crea** una scheda con `sdk_create_card` o `sdk_import_github` — esegue la pipeline di validazione e memorizza la scheda con `partner_status = validated` (o `rejected` in caso di errore).
2. **Valida** con `sdk_validate_card` per ricontrollare una scheda esistente o per eseguire una prova del nuovo codice sorgente senza salvarlo.
3. **Testa** con `sdk_test_card` per eseguire la scheda nella sandbox con un contesto simulato.
4. **Approva** con `sdk_approve_card` (solo amministratore dell'organizzazione) — riesegue la validazione AST e comportamentale, poi imposta `partner_status = approved` e `enabled = true`.
5. Una volta approvata, la scheda compare in `list_cards` per ogni organizzazione e può essere referenziata dai nodi del workflow.

## Strumenti di Sviluppo

### sdk\_create\_card

Crea una nuova scheda partner a partire dal codice sorgente e dai manifest. Esegue l'intera pipeline di validazione (vedi [Fasi di Validazione](#sdk_validate_card) di seguito) e memorizza la scheda nel database. La scheda viene creata nello stato `validated` e richiede l'approvazione di un amministratore prima di poter essere usata nei workflow.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `app_manifest` | object | Sì | Manifest dell'app con id, nome, versione, informazioni sul partner |
| `card_manifest` | object | Sì | Manifest della scheda con id, titolo, entry\_point, class\_name, args |
| `card_type` | string | Sì | `action` o `condition` |
| `source_code` | string | Sì | Codice sorgente Python (deve estendere `PartnerCard`) |
| `test_code` | string | Sì | Codice di test Pytest per la scheda |
| `locales` | object | No | Traduzioni delle lingue, ad es. `{"en": {...}, "de": {...}}` |

**Esempio di App Manifest:**

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

**Esempio di Card Manifest:**

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
`CardStatus` ha tre valori che corrispondono direttamente ai rami del workflow:

| Stato | Ramo seguito | Quando usarlo |
|-------|--------------|---------------|
| `SUCCESS` | `success` | La scheda è riuscita — vale sia per le condizioni sia per le azioni. |
| `FAILED` | `failed_condition` | **Solo schede di condizione.** La condizione è risultata falsa — il workflow segue il ramo "else". Le schede di azione non hanno un handle `failed_condition`, quindi restituire `FAILED` da un'azione lascia l'esecuzione senza un percorso da seguire. |
| `ERROR` | `error` | Un errore imprevisto in fase di esecuzione (eccezione). Vale sia per le condizioni sia per le azioni. |

In breve: le azioni restituiscono `SUCCESS` o `ERROR`; le condizioni possono restituire anche `FAILED`.
{% endhint %}

### sdk\_validate\_card

Esegue la pipeline di validazione su una scheda partner senza salvarla. Due modalità:

- **Modalità A** — Valida una scheda esistente tramite ID
- **Modalità B** — Valida direttamente nuovo codice sorgente

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | No | UUID di una scheda esistente (Modalità A) |
| `app_manifest` | object | No | Manifest dell'app (Modalità B) |
| `card_manifest` | object | No | Manifest della scheda (Modalità B) |
| `card_type` | string | No | `action` o `condition` (Modalità B) |
| `source_code` | string | No | Codice sorgente Python (Modalità B) |
| `test_code` | string | No | Codice di test (Modalità B) |

{% hint style="info" %}
Fornisci solo `card_id` (Modalità A) oppure `app_manifest` + `card_manifest` + `source_code` insieme (Modalità B).
{% endhint %}

**Fasi di Validazione:**

1. **Structure** — Verifica la struttura dei file, lo schema dei manifest (`app.json`, `.docflowcompose/flow/...`) e che i punti di ingresso dichiarati esistano.
2. **Locales** — Riconcilia le chiavi di traduzione usate nella scheda con i file `locales/<lang>.json`; fallisce se manca una chiave in una lingua dichiarata.
3. **AST Analysis** — Esamina ogni file `.py` in `src/` e controlla import vietati, chiamate pericolose e requisiti di gerarchia delle classi / firma dei metodi.
4. **Dependencies** — Verifica che tutti gli import siano risolti in moduli consentiti dalla whitelist dell'SDK.
5. **Tests** — Esegue la suite pytest della scheda con rlimit ridotti.
6. **Behavioral** — Esegue la scheda nella sandbox di produzione con un contesto simulato minimo per confermarne il comportamento in fase di esecuzione.

Le fasi vengono eseguite in ordine; la prima fase che fallisce interrompe le successive. La fase 6 (Behavioral) viene rieseguita anche al momento dell'approvazione come controllo di difesa in profondità prima che la scheda venga attivata.

### sdk\_test\_card

Esegue una scheda partner in un ambiente sandbox con un contesto simulato. La sandbox impone builtin limitati, una allow-list curata di import, un timeout di esecuzione e limiti ridotti delle risorse di processo — le stesse restrizioni con cui una scheda viene eseguita una volta approvata.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | No | UUID di una scheda esistente (Modalità A) |
| `source_code` | string | No | Codice sorgente per il test inline (Modalità B) |
| `class_name` | string | No | Nome della classe per il test inline (Modalità B) |
| `variables` | object | No | Variabili da passare al costruttore della scheda |
| `mock_context` | object | No | Contesto di esecuzione simulato |

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

Lo strumento restituisce `execution_success` (se la sandbox ha eseguito la scheda fino al termine — un timeout, una violazione degli import o un'eccezione lo impostano a `false`), `card_status` (il `CardStatus` restituito da `execute()` stesso), il `message` e i `data` della scheda, i `logs` catturati e `execution_time_ms`.

### sdk\_import\_github

Importa un'app partner da un repository GitHub. Clona il repository, legge `app.json` e importa tutte le schede trovate nella directory `.docflowcompose`.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `github_url` | string | Sì | URL HTTPS di GitHub (ad es. `https://github.com/org/repo`) |
| `branch` | string | No | Branch da clonare (predefinito: `main`) |
| `token` | string | No | Token GitHub per i repository privati |

**Struttura Attesa del Repository:**

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

Elenca tutti gli invii di schede partner dell'organizzazione corrente.

**Parametri:** Nessuno

### sdk\_get\_submission\_status

Ottiene lo stato di validazione e il report di uno specifico invio di scheda partner.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | Sì | UUID della scheda partner |

### sdk\_approve\_card

Approva una scheda partner validata e la attiva. L'approvazione riesegue la validazione AST e comportamentale come controllo di difesa in profondità, imposta `partner_status = approved` e `enabled = true` e registra la scheda nel registro di runtime. Una volta approvata, la scheda compare in `list_cards` per **ogni organizzazione**, non solo per quella che l'ha inviata.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | Sì | UUID della scheda partner |

{% hint style="warning" %}
Richiede i permessi di amministratore dell'organizzazione. La scheda deve essere nello stato `validated`. Le schede rifiutate devono essere ricaricate e rivalidate prima di poter essere approvate.
{% endhint %}

### sdk\_reject\_card

Rifiuta l'invio di una scheda partner e la disattiva.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | Sì | UUID della scheda partner |
| `reason` | string | No | Motivo del rifiuto |

{% hint style="warning" %}
Richiede i permessi di amministratore dell'organizzazione.
{% endhint %}

### sdk\_delete\_submission

Elimina in modo logico (soft-delete) l'invio di una scheda partner, indipendentemente dal suo stato attuale. Imposta `partner_status = deleted`, `enabled = false` e `deprecated = true`. La riga viene conservata a fini di audit, ma è nascosta dagli elenchi degli invii e da `list_cards`.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|--------------|-------------|
| `card_id` | string | Sì | UUID della scheda partner |

{% hint style="warning" %}
Richiede i permessi di amministratore dell'organizzazione.
{% endhint %}

### sdk\_list\_cards\_picker

Elenca tutte le schede abilitate e non deprecate con i flag di ruolo. Utile per stabilire quali schede possono essere usate in quali tipi di nodo durante la creazione dei workflow.

**Parametri:** Nessuno

## Funzionalità Attuali e Roadmap

Il Partner Card SDK viene rilasciato in modo incrementale. Ecco su cosa può contare oggi la tua scheda e cosa è ancora in fase di integrazione:

| Funzionalità | Stato |
|--------------|-------|
| **Condizioni sui campi** — leggere i campi del documento da `context.document_fields` e ramificare in base ai loro valori all'interno delle schede di condizione | ✅ Implementato |
| **Richieste HTTP in uscita** — chiamare servizi esterni dall'interno di una scheda | 🚧 In fase di aggiunta |
| **Informazioni estese sul documento** — metadati aggiuntivi del documento (oltre a `document_id`, `document_type` e `document_fields`) esposti in `ExecutionContext` | 🚧 In fase di aggiunta |
| **Helper per la ricerca nelle tabelle del database** — helper integrati per leggere dalle tabelle dei dati anagrafici / di lookup di DocBits all'interno di una scheda | 📅 Pianificato per la 1.1 |
| **Visualizzatore del sorgente della scheda partner** — vista in sola lettura del codice della scheda partner inviata nell'interfaccia di DocBits, così gli amministratori possono ispezionare ciò che stanno approvando | 📅 Pianificato per la 1.1 |

{% hint style="info" %}
Se la tua scheda ha bisogno di una funzionalità ancora in corso di sviluppo, la validazione fallirà (import vietato, attributo di contesto mancante o restrizione della sandbox) finché il componente corrispondente non sarà disponibile. Questa pagina verrà aggiornata man mano che ogni funzionalità viene rilasciata.
{% endhint %}

{% hint style="danger" %}
**Le schede partner eseguono codice di terze parti — usale a tuo rischio.**

Le schede caricate tramite il Partner Card SDK sono **validate da DocBits solo in parte**. La pipeline di validazione controlla struttura, locales, import, pattern AST, dipendenze, i test della scheda stessa e un'esecuzione di prova comportamentale nella sandbox — **non** costituisce un audit di sicurezza completo né una garanzia funzionale della logica di business della scheda.

Una volta che un amministratore dell'organizzazione approva una scheda partner, essa diventa disponibile a ogni organizzazione della piattaforma e viene eseguita nella sandbox di produzione su documenti reali. Approvare e abilitare una scheda partner è quindi una decisione di fiducia esplicita da parte dell'amministratore che approva. DocBits non si assume alcuna responsabilità per perdita di dati, instradamento errato, fuga di informazioni o qualsiasi altro esito causato da una scheda partner che scegli di installare o approvare.

Se non sei l'autore originale della scheda, esamina il sorgente (e, quando la 1.1 sarà rilasciata, usa il visualizzatore del sorgente delle schede partner) prima di approvarla.
{% endhint %}
