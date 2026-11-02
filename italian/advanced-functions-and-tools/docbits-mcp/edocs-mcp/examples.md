# Esempi

Trovi i prompt e la procedura di diagnosi, bozza, attivazione e ripristino in [Configurare DocBits con Claude o Codex](../configuration-with-claude-or-codex.md). Gli esempi usano i parametri attuali. Sostituisci tutti i segnaposto con valori della tua organizzazione e usa sorgenti completi con corretto escaping JSON.

## 1. Modificare una regola Custom esistente

Leggi la `TRANSFORMATION` effettiva con `get_edoc_attribute_source`, usando l’etichetta esatta del formato restituita dalla classificazione:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Registra `attribute_id`, `active_value_id`, `active_version` e `value`. Leggi separatamente `source: "default"` per il confronto e la cronologia con `list_edoc_attribute_versions`. I passaggi seguenti presuppongono un attributo Custom esistente della tua organizzazione.

Prova il candidato completo senza salvarlo con `preview_edoc_custom_xslt`. Usa un documento già presente nella stessa organizzazione:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Il risultato è XML trasformato per `TRANSFORMATION`, PDF per `PREVIEW` o campi/tabelle per `EXTRACTION_PATHS`. L’anteprima non seleziona una bozza salvata e non verifica script successivi o esportazioni.

Dopo la verifica di diff e anteprima, rileggi il sorgente attivo e salva una bozza con `update_edoc_custom_attribute`. Specifica `activate: false`; il valore predefinito è `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Dopo i test nell’organizzazione di test e la conferma della modifica specifica, chiama `activate_edoc_attribute_version`. `draft_id` è l’ID del valore di versione. Rileggi il sorgente effettivo. Per tornare indietro usa il precedente `active_value_id` nella stessa chiamata.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Se non esiste un attributo Custom

`create_edoc_custom_attribute` crea una prima versione subito attiva, non una bozza. Prova la nuova personalizzazione in un’organizzazione di test o usa il percorso supportato dall’editor DocBits. Non creare né eliminare personalizzazioni in produzione solo per ottenere un’anteprima. Conserva le mappature necessarie; non modificare globalmente i valori predefiniti condivisi.

## 3. Provare la configurazione attiva

Chiama `test_electronic_document` con l’XML originale codificato in base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Questa prova usa le regole attive senza salvare un documento, non una bozza inattiva. MCP HTTP remoto non può leggere un `file_path` locale del tuo computer. `compare_edoc_extraction` confronta solo Extraction Paths e richiede un attributo personalizzato dei percorsi di estrazione; non confronta trasformazioni.

`validate_all_edocs` prova senza persistenza i file disponibili sul server. `verify_electronic_documents` li carica ed elabora, creando documenti. Nessuno dei due dimostra la consegna all’ERP. Usa esempi rappresentativi, controlla separatamente campi/importi salvati ed esportazione e non riavviare in blocco documenti storici.
