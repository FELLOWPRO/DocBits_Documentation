# Strumenti per i Workflow

DocFlow MCP espone strumenti per la gestione e il test dei workflow avanzati, oltre a strumenti per la lettura dei log dei workflow e la gestione delle variabili di workflow. Gli strumenti Card SDK hanno una pagina dedicata -- vedi [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Elenca tutti i workflow dell'organizzazione corrente.

**Parametri:** Nessuno

## get\_workflow

Ottiene i dettagli di un workflow specifico, inclusa la struttura di nodi e archi.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Si | UUID del workflow |

## create\_advanced\_workflow

Crea un nuovo workflow avanzato con nodi e archi.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `name` | string | Si | Nome del workflow (3-126 caratteri) |
| `description` | string | No | Descrizione opzionale |
| `nodes` | array | Si | Array di nodi del workflow |
| `edges` | array | Si | Array di archi che collegano i nodi |

### Struttura dei Nodi

Ogni nodo richiede:

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| `node_id` | string | Identificatore univoco del nodo |
| `node_type` | string | Vedi i tipi di nodo qui sotto |
| `position` | object | `{x: number, y: number}` posizione sul canvas |
| `label` | string | Etichetta di visualizzazione |
| `card` | object | Configurazione della card (obbligatoria per `when`, `and`, `then` -- vedi sotto) |

**Tipi di nodo:**

| Tipo | Card richiesta | Scopo |
|------|------------------|---------|
| `start` | Nessuna card | Nodo trigger -- punto di ingresso del workflow |
| `when` | Card di condizione | Condizione di trigger (anche punto di ingresso valido) |
| `and` | Card di condizione | Gate aggiuntivo di condizione dopo un `when` |
| `or` | Nessuna card | Nodo di diramazione -- prosegue se uno qualsiasi dei rami in ingresso ha successo |
| `then` | Card di azione | Azione da eseguire |
| `delay` | Nessuna card | Nodo di attesa -- mette in pausa l'esecuzione per una durata configurata |
| `all` | Nessuna card | Nodo di unione -- attende tutti i rami in ingresso |
| `any` | Nessuna card | Nodo di unione -- prosegue al primo ramo in ingresso |
| `note` | Nessuna card | Nota / annotazione; non viene eseguita |

### Struttura degli Archi

Ogni arco richiede:

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| `edge_id` | string | Identificatore univoco dell'arco |
| `source_node_id` | string | ID del nodo sorgente |
| `target_node_id` | string | ID del nodo destinazione |
| `source_handle` | string | `success`, `error` o `failed_condition` (opzionale) |
| `target_handle` | string | `input` (opzionale) |

**Source handle:**

- `success` -- preso quando il nodo sorgente ha successo (disponibile su ogni nodo eseguibile).
- `failed_condition` -- preso quando una card di condizione `when` o `and` viene valutata come false.
- `error` -- preso quando un nodo `and` o `then` solleva un errore.

### Configurazione della Card

Le card definiscono cosa fa un nodo. Usa `list_cards` o `sdk_list_cards_picker` per ottenere le card disponibili.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
Devi fornire solo `id`, `card_type`, `version` e `variables` per ogni card. Il server arricchisce automaticamente le card con i metadati di visualizzazione (svg, text, category) dal database.
{% endhint %}

**Esempio di Richiesta:**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Aggiorna un workflow avanzato esistente. Puoi aggiornare qualsiasi combinazione di nome, descrizione, nodi e archi.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Si | UUID del workflow da aggiornare |
| `name` | string | No | Nuovo nome |
| `description` | string | No | Nuova descrizione |
| `nodes` | array | No | Nuovi nodi (sostituisce tutti i nodi esistenti) |
| `edges` | array | No | Nuovi archi (sostituisce tutti gli archi esistenti) |

## delete\_workflow

Elimina un workflow tramite ID (soft delete).

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Si | UUID del workflow da eliminare |

## test\_advanced\_workflow

Testa l'esecuzione di un workflow avanzato. Opzionalmente fornisci un ID documento per testare con un documento reale.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Si | UUID del workflow avanzato |
| `doc_id` | string | No | UUID di un documento con cui testare |

## list\_test\_scenarios

Elenca tutti gli scenari di test dei workflow per l'organizzazione.

**Parametri:** Nessuno

## list\_cards

Elenca tutte le card di workflow disponibili con le loro condizioni e configurazione.

**Parametri:** Nessuno

{% hint style="info" %}
Le card hanno flag di ruolo: `when_condition` (trigger), `and_condition` (condizione aggiuntiva) e `then_condition` (azione). Usali per determinare in quali tipi di nodo una card puo' essere utilizzata.
{% endhint %}
