# DocFlow MCP

DocFlow espone un server **Model Context Protocol (MCP)** che consente agli assistenti AI di gestire workflow e card partner in modo programmatico. Qualsiasi client compatibile con MCP -- Claude Code, Claude Desktop, OpenAI Codex o integrazioni personalizzate -- puo' connettersi e utilizzare questi strumenti.

## Cosa Puoi Fare?

Con DocFlow MCP puoi:

- **Elencare, creare, aggiornare ed eliminare** workflow avanzati
- **Testare workflow** con documenti reali o simulati
- **Creare card personalizzate** utilizzando il Partner Card SDK
- **Validare, testare, approvare e gestire** le sottomissioni di card partner
- **Importare card** direttamente da repository GitHub

## Panoramica degli Strumenti

DocFlow MCP fornisce **18 strumenti** suddivisi in quattro categorie:

### Gestione dei Workflow

| Strumento | Descrizione |
|------|-------------|
| `list_workflows` | Elenca tutti i workflow dell'organizzazione corrente |
| `get_workflow` | Ottieni i dettagli di un workflow specifico tramite ID |
| `delete_workflow` | Elimina un workflow tramite ID |

### Test dei Workflow

| Strumento | Descrizione |
|------|-------------|
| `test_advanced_workflow` | Testa l'esecuzione di un workflow avanzato con documento opzionale |
| `list_test_scenarios` | Elenca tutti gli scenari di test dei workflow |
| `list_cards` | Elenca le card/azioni disponibili per i workflow |

### Gestione Card SDK

| Strumento | Descrizione |
|------|-------------|
| `sdk_list_submissions` | Elenca tutte le sottomissioni di card partner |
| `sdk_get_submission_status` | Ottieni lo stato di validazione di una sottomissione |
| `sdk_approve_card` | Approva una card partner validata (admin) |
| `sdk_reject_card` | Rifiuta una sottomissione di card partner (admin) |
| `sdk_delete_submission` | Disattiva o elimina una sottomissione (admin) |
| `sdk_list_cards_picker` | Elenca tutte le card abilitate con flag di ruolo |

### Sviluppo Card SDK

| Strumento | Descrizione |
|------|-------------|
| `sdk_create_card` | Crea una nuova card partner dal codice sorgente |
| `sdk_validate_card` | Esegui la validazione in 5 fasi senza salvare |
| `sdk_test_card` | Esegui una card in un ambiente sandbox |
| `sdk_import_github` | Importa un'app partner da GitHub |

## Per Iniziare

1. [Configura il tuo client MCP](setup-and-configuration.md)
2. Scopri gli [Strumenti per i Workflow](workflow-tools.md)
3. Esplora gli [Strumenti Card SDK](card-sdk-tools.md)
4. Segui gli [Esempi](examples.md) completi

{% hint style="info" %}
DocFlow MCP utilizza il trasporto **Streamable HTTP**. L'endpoint del server e' `/api/mcp/` sul tuo host API DocBits.
{% endhint %}
