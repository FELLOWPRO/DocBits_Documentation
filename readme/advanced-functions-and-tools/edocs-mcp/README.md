# eDocs MCP

L'API DocBits espone un server **Model Context Protocol (MCP)** con strumenti per ispezionare e personalizzare l'elaborazione dei documenti elettronici (eDoc). Qualsiasi client compatibile con MCP, come Claude Code, Claude Desktop o integrazioni personalizzate, può collegarsi e utilizzare questi strumenti.

## Cosa puoi fare?

Con gli strumenti eDocs MCP puoi:

- **Ispezionare** come viene classificato qualsiasi tipo di documento elettronico e quali regole di estrazione si applicano
- **Testare** i documenti attraverso l'intera pipeline di elaborazione senza salvarli nel database
- **Creare regole personalizzate** per la tua organizzazione: anteprime XSLT, percorsi di estrazione, trasformazioni
- **Aggiornare** una regola personalizzata con una nuova versione (con o senza attivazione immediata)
- **Eliminare** una regola personalizzata per tornare al valore predefinito integrato
- **Verificare** che tutte le fixture eDoc supportate vengano elaborate correttamente

## Modello di autorizzazione

DocBits include una libreria di regole predefinite integrate, condivise da tutti i clienti. Queste regole predefinite utilizzano l'ID organizzazione riservato `00000000-0000-0000-0000-000000000000`.

**Le regole predefinite non sono modificabili tramite MCP.** Ogni strumento di scrittura controlla l'ID della tua organizzazione prima di effettuare qualsiasi richiesta. Se corrisponde all'organizzazione predefinita, l'operazione viene rifiutata immediatamente: non viene mai eseguita alcuna chiamata API.

I clienti possono creare, modificare o eliminare regole solo **all'interno della propria organizzazione**. Quando per la tua organizzazione esiste una regola personalizzata, questa ha la precedenza su quella predefinita. Eliminando una regola personalizzata, il comportamento predefinito viene ripristinato automaticamente.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Panoramica degli strumenti

### Ispezione (sola lettura)

| Strumento | Descrizione |
|------|-------------|
| `test_electronic_document` | Prova a vuoto l'intera pipeline eDoc (classificazione, estrazione, anteprima) senza salvare |
| `list_electronic_document_types` | Elenca tutti i tipi di eDoc supportati con lo stato di configurazione |
| `get_extraction_rules` | Mostra le regole XPath utilizzate per estrarre i campi di un dato tipo di documento |
| `get_extracted_fields` | Ottiene i campi di intestazione estratti da un documento elaborato |
| `get_extracted_tables` | Ottiene le righe estratte da un documento elaborato |
| `get_preview_pdf` | Recupera il PDF di anteprima generato con XSLT per un documento |
| `get_preview_image` | Recupera l'immagine di una pagina renderizzata di un documento elaborato |
| `extract_edoc_table` | Estrae un file XML/EDI che passi e restituisce i campi come tabella piatta insieme alla regola che ha prodotto ciascuno di essi |
| `compare_edoc_extraction` | Confronta l'estrazione predefinita e quella personalizzata (e, facoltativamente, una regola candidata) su un documento |

### Personalizzazione (a livello di organizzazione, organizzazione predefinita bloccata)

| Strumento | Descrizione |
|------|-------------|
| `list_edoc_custom_attributes` | Elenca le sostituzioni personalizzate della tua organizzazione rispetto ai valori predefiniti integrati per un tipo di documento |
| `create_edoc_custom_attribute` | Crea una nuova regola personalizzata (EXTRACTION_PATHS, TRANSFORMATION o PREVIEW) |
| `update_edoc_custom_attribute` | Aggiunge una nuova versione di una regola personalizzata, con attivazione immediata facoltativa |
| `delete_edoc_custom_attribute` | Elimina una regola personalizzata: il sistema torna automaticamente a quella predefinita |
| `preview_edoc_custom_xslt` | Prova a vuoto una trasformazione XSLT su un documento XML prima di attivarla |
| `get_edoc_attribute_source` | Recupera il sorgente modificabile di un attributo (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) per modificarlo |
| `list_edoc_attribute_versions` | Cronologia delle versioni di un attributo personalizzato: bozze e versione attiva |
| `activate_edoc_attribute_version` | Attiva una versione o una bozza specifica (è così che si torna indietro) |
| `delete_edoc_attribute_draft` | Elimina una bozza che non è mai stata attivata |

### Verifica

| Strumento | Descrizione |
|------|-------------|
| `verify_electronic_documents` | Carica le fixture e verifica end-to-end classificazione, estrazione e anteprima |
| `validate_all_edocs` | Esegue tutte le fixture eDoc in una pipeline di prova a vuoto e segnala i problemi |

## Tipi di attributo

Ogni regola personalizzabile ha un tipo e un formato specifici:

| Nome attributo | Formato | Scopo |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | Espressioni XPath che associano i nodi XML ai campi DocBits |
| `TRANSFORMATION` | XSLT | Foglio di stile applicato all'XML prima dell'estrazione |
| `PREVIEW` | XSLT | Foglio di stile che genera l'anteprima PDF leggibile |
| `STRUCTURE_DESCRIPTOR` | JSON | Mappa della struttura, solo per i documenti EDI |

Lo strumento `create_edoc_custom_attribute` deduce automaticamente il formato corretto dal nome dell'attributo.

## Avvio rapido

### Elencare ciò che la tua organizzazione ha personalizzato

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Restituisce due elenchi: `custom` (le sostituzioni della tua organizzazione) e `default` (le regole condivise che erediti).

### Creare un'anteprima personalizzata per XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Restituisce il nuovo `attribute_id`: conservalo per aggiornamenti ed eliminazione.

### Aggiornare una regola personalizzata esistente

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Crea una nuova versione e la attiva. La versione precedente viene conservata nella cronologia.

### Tornare al valore predefinito

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Rimuove la sostituzione personalizzata. Il sistema torna immediatamente alla regola predefinita integrata.

## Regole di sicurezza

| Azione | Consentita |
|--------|---------|
| Leggere le regole predefinite | ✅ Sì |
| Creare una regola personalizzata per la tua organizzazione | ✅ Sì |
| Aggiornare una regola personalizzata per la tua organizzazione | ✅ Sì |
| Eliminare una regola personalizzata per la tua organizzazione | ✅ Sì |
| Modificare o eliminare le regole predefinite | ❌ **Mai**: bloccato a livello MCP |

Il tentativo di scrivere su `00000000-0000-0000-0000-000000000000` restituisce:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```
