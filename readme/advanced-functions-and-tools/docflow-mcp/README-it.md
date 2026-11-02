# DocFlow MCP

DocFlow espone un server **Model Context Protocol (MCP)** che consente agli assistenti AI di gestire workflow e card partner in modo programmatico. Qualsiasi client compatibile con MCP -- Claude Code, Claude Desktop, OpenAI Codex o integrazioni personalizzate -- puo' connettersi e utilizzare questi strumenti.

## Cosa Puoi Fare?

Con DocFlow MCP puoi:

- **Elencare, creare, aggiornare ed eliminare** workflow avanzati
- **Testare i workflow** con documenti reali o fittizi
- **Costruire card personalizzate** usando il Partner Card SDK
- **Validare, testare, approvare e gestire** le sottomissioni di card partner
- **Importare card** direttamente da repository GitHub

## Panoramica degli Strumenti

DocFlow MCP raggruppa i propri strumenti nelle seguenti categorie. La maggior parte degli strumenti Workflow e Card SDK rispecchia endpoint REST esistenti -- consulta li' la documentazione dell'API. Le categorie seguenti coprono la superficie specifica di MCP e i concetti di workflow necessari per usarla.

### Gestione Workflow

| Strumento | Descrizione |
|------|-------------|
| `list_workflows` | Elenca tutti i workflow dell'organizzazione corrente |
| `get_workflow` | Ottiene i dettagli di un workflow specifico tramite ID |
| `create_advanced_workflow` | Crea un nuovo workflow avanzato con nodi e archi |
| `update_advanced_workflow` | Aggiorna un workflow avanzato esistente |
| `delete_workflow` | Elimina un workflow tramite ID |

### Test dei Workflow

| Strumento | Descrizione |
|------|-------------|
| `test_advanced_workflow` | Testa l'esecuzione di un workflow avanzato, opzionalmente con un documento |
| `list_test_scenarios` | Elenca tutti gli scenari di test dei workflow |
| `list_cards` | Elenca le card / azioni di workflow disponibili |

### Gestione Card SDK

| Strumento | Descrizione |
|------|-------------|
| `sdk_list_submissions` | Elenca tutte le sottomissioni di card partner |
| `sdk_get_submission_status` | Ottiene lo stato di validazione di una sottomissione |
| `sdk_approve_card` | Approva una card partner validata (admin) |
| `sdk_reject_card` | Rifiuta una sottomissione di card partner (admin) |
| `sdk_delete_submission` | Disattiva o elimina una sottomissione (admin) |
| `sdk_list_cards_picker` | Elenca tutte le card abilitate con i flag di ruolo |

### Sviluppo Card SDK

| Strumento | Descrizione |
|------|-------------|
| `sdk_create_card` | Crea una nuova card partner dal codice sorgente |
| `sdk_validate_card` | Esegue la pipeline di validazione senza salvare |
| `sdk_test_card` | Esegue una card in un ambiente sandbox |
| `sdk_import_github` | Importa un'app partner da GitHub |

## Come Iniziare

1. [Configura il tuo client MCP](setup-and-configuration.md)
2. Scopri i [Workflow Tools](workflow-tools.md)
3. Esplora i [Card SDK Tools](card-sdk-tools.md)
4. Segui gli [Esempi](examples.md) end-to-end

{% hint style="info" %}
DocFlow MCP utilizza il trasporto **Streamable HTTP**. L'endpoint del server e' `/v3/mcp/` sull'host DocFlow (ad es. `https://docflow.docbits.com/v3/mcp/`). Vedi [Configurazione & Setup](setup-and-configuration.md) per l'elenco completo delle URL.
{% endhint %}
