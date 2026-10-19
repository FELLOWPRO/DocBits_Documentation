# Configurare DocBits con Claude o Codex

Descrivi il risultato desiderato, lascia che l’assistente legga la configurazione, esamina la proposta e applica la modifica concordata. DocBits MCP offre questi strumenti in Claude e Codex con i permessi dell’account DocBits collegato. Le modifiche richiedono i relativi permessi di amministratore.

Questa guida descrive una procedura; non attesta una correzione già eseguita per un cliente né un test di esportazione riuscito.

## 1. Collegarsi all’organizzazione corretta

Scegli regione e ambiente nella [guida agli endpoint e all’accesso](setup-and-configuration.md). I comandi usano la **sandbox UE**: sostituisci l’URL se l’organizzazione di test usa un altro endpoint. Eseguili sul computer dell’assistente, accedi e autorizza l’accesso a DocBits nel browser.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

Nell’app Codex usa le impostazioni MCP o la configurazione condivisa con la CLI sullo stesso computer. In Claude Desktop usa un connettore remoto personalizzato, se il piano lo supporta, con lo stesso endpoint HTTP. Apri una nuova conversazione se gli strumenti non compaiono. Istruzioni attuali: [Codex MCP](https://developers.openai.com/codex/mcp) e [Claude MCP](https://code.claude.com/docs/en/mcp).

```text
Sola lettura. Verifica ambiente e organizzazione DocBits collegati con
get_api_info e get_current_user. Elenca gli strumenti di configurazione.
Mostra ID organizzazione e host API, senza token o frammenti di chiavi.
Non modificare impostazioni e non elaborare documenti.
```

Se l’organizzazione non è ancora risolta, leggi la configurazione pertinente e verifica il `org_id` restituito. Fermati se non è quella prevista. I nomi degli strumenti possono avere un prefisso client/server: usa gli strumenti e gli schemi dei parametri effettivamente annunciati dalla connessione.

## 2. Modificare un’impostazione semplice

```text
Trova con find_setting l’impostazione di estrazione dei codici QR di questa
organizzazione di test. Mostra setting_key esatto e valore attuale.
Se ci sono più risultati, chiedi quale intendo. Se apply_setting supporta
l’impostazione, prepara l’anteprima dell’attivazione. Mostra current_value
e proposed_value; attendi la mia conferma prima di confirm_setting_change.
```

`apply_setting` crea solo un’anteprima. Dopo la conferma di quella proposta specifica, `confirm_setting_change(preview_id)` salva la modifica. Rileggi il valore e conserva `undo_id`: `undo_setting_change` può annullarla entro il termine restituito. Normalmente l’anteprima scade dopo 5 minuti e l’annullamento dopo 15. Se il valore è cambiato o l’anteprima è scaduta, creane e verificane una nuova.

Per modifiche strutturate supportate: `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Leggi prima i tipi di azione disponibili. Se manca un’azione di scrittura supportata, chiedi `app_path` e modifica l’impostazione in DocBits. Non inventare una chiave di preferenza e non sostituire il percorso con una chiamata generica a `set_preference`.

## 3. Analizzare una nota di credito salvata come Invoice

Una trasformazione Custom può produrre sempre `<INVOICE_TYPE>Invoice</INVOICE_TYPE>`, anche se l’XML originale contiene un codice di nota di credito. È lo scenario della [guida diagnostica con video dell’interfaccia reale di DocBits](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Sola lettura. Per XML originale e ID documento forniti, identifica famiglia
eDoc, sintassi, versione/profilo e codice di tipo originale. Elenca attributi
Custom e Default. Leggi TRANSFORMATION ed EXTRACTION_PATHS effettivi e
predefiniti con get_edoc_attribute_source. Registra attribute_id,
active_version e active_value_id e leggi la cronologia.
Segui TypeCode -> XML trasformato -> invoice_type -> campo salvato,
anteprima di esportazione e script successivi. Mostra prove e incertezze.
Non attivare, eliminare, riavviare, approvare o esportare nulla.
```

Usa l’**etichetta esatta del formato rilevato**, senza indovinare la versione ZUGFeRD o Factur-X. Il `doc_type_key` tecnico può restare `INVOICE`; il valore funzionale da analizzare è `invoice_type`.

| Lettura | Strumento MCP |
| --- | --- |
| Attributi Custom e Default | `list_edoc_custom_attributes` |
| Sorgente effettiva o predefinita e ID attivi | `get_edoc_attribute_source`, con `source: "effective"` o `"default"` |
| Cronologia e bozze | `list_edoc_attribute_versions`, con `include_values: true` se necessario |
| Campi salvati, log, anteprima di esportazione | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

La versione attiva oggi non dimostra quale abbia elaborato un documento storico. Se i log non lo chiariscono, conserva questa incertezza. L’anteprima PDF non prova né il tipo salvato né gli importi esportati.

<figure><img src="../../.gitbook/assets/edocs-transformation-it.png" alt="Esempio di sviluppo in sola lettura: editor del sorgente e delle versioni DocBits. Leggi il tuo sorgente effettivo e valore attivo via MCP; l’immagine non mostra una modifica salvata."><figcaption><p>Esempio di sviluppo in sola lettura: editor del sorgente e delle versioni DocBits. Leggi il tuo sorgente effettivo e valore attivo via MCP; l’immagine non mostra una modifica salvata.</p></figcaption></figure>

## 4. Provare la correzione minima senza salvarla

```text
Proponi la modifica minima della nostra trasformazione Custom esistente
affinché 381 produca Credit Note. Conserva le altre mappature e i codici di
nota di credito già supportati. Non classificare 383 o 384 come Credit Note.
Mostra il diff. Prova il candidato sui documenti di test senza salvarlo.
Mostra INVOICE_TYPE trasformato e gli importi pertinenti; specifica quali
verifiche mancano ancora.
```

Per un **attributo esistente della propria organizzazione**, chiama `preview_edoc_custom_xslt` con il candidato completo:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Sostituisci tutti i segnaposto con valori restituiti nelle risposte. XSLT/JSON deve contenere il sorgente completo con corretto escaping JSON. Si usa un documento esistente della stessa organizzazione. Lo strumento restituisce **XML** per `TRANSFORMATION`, campi/tabelle per `EXTRACTION_PATHS` e **PDF** per `PREVIEW`, senza salvare il candidato. Per il confronto con la trasformazione predefinita, prova il suo sorgente come altro candidato con lo stesso attributo Custom e documento.

`compare_edoc_extraction` confronta **EXTRACTION_PATHS** e richiede un attributo personalizzato dei percorsi di estrazione. Non confronta due trasformazioni. Non creare una personalizzazione inutile solo per usare questo strumento.

Se non esiste un attributo Custom, fermati prima di crearlo in produzione: `create_edoc_custom_attribute` crea una prima versione **subito attiva**, senza opzione per la sola bozza. Prepara la nuova personalizzazione in un’organizzazione di test o usa il flusso di creazione/anteprima supportato dall’editor DocBits. Non tentare di modificare globalmente le regole predefinite condivise.

## 5. Salvare una bozza e attivarla esplicitamente

Dopo aver esaminato diff e risultato, rileggi il sorgente attivo. Se è cambiato durante il lavoro, confrontalo di nuovo. Per un attributo Custom esistente usa `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Passa sempre `activate: false` in questa fase: il valore predefinito dello strumento è `true`. Registra l’ID del valore di versione restituito e verifica con `list_edoc_attribute_versions` che la versione precedente resti attiva. Salvare una bozza non modifica l’elaborazione normale.

Dopo i test, l’amministratore conferma organizzazione, attributo, diff e versione specifici. Attiva con `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` è l’**ID del valore della versione**, non il numero di versione o l’ID attributo. Rileggi sorgente effettivo e cronologia per confermare che quel valore sia attivo. eDocs usa questi strumenti direttamente, non il flusso generico delle impostazioni con `preview_id`. Leggi gli ID nell’ambiente di destinazione: quelli della sandbox non sono riutilizzabili in produzione.

## 6. Verificare classificazione, importi ed esportazione

`test_electronic_document` prova la configurazione **attualmente attiva** senza salvare un documento. Non permette di selezionare un candidato o una bozza. Con MCP HTTP remoto invia l’XML originale come `file_content_base64` con `file_name`; il server non può leggere un `file_path` locale del tuo computer. Per provare l’intera elaborazione del candidato, attivalo prima esplicitamente nell’organizzazione di test. L’anteprima XSLT da sola non verifica script successivi o esportazioni.

| Codice originale | Verifica attesa |
| --- | --- |
| 380 | Invoice resta Invoice |
| 381 | La nota di credito diventa Credit Note |
| 261 | Conservare il comportamento di nota di credito se formato/mappatura lo supporta |
| 383 | Una nota di debito non diventa Credit Note solo perché rettifica una fattura |
| 384 | Una fattura corretta non diventa Credit Note solo perché corregge una fattura |

Controlla anche campi personalizzati, righe, totali e impostazione del segno negativo. Elabora un **nuovo documento di test** in un’organizzazione isolata con esportazioni automatiche controllate. Confronta `invoice_type` salvato, dashboard e `get_export_preview`. Un’esportazione reale al sistema di destinazione richiede un test concordato separatamente: né la prova senza persistenza né l’anteprima attestano la consegna all’ERP.

`validate_all_edocs` prova senza persistenza i file di test disponibili sul server; `verify_electronic_documents` **carica ed elabora** i file di test. Non sostituiscono i tuoi documenti rappresentativi e le verifiche successive. Se mancano file o strumenti, usa esempi forniti.

## 7. Ripristinare e trattare separatamente i documenti storici

Per tornare indietro, chiama `activate_edoc_attribute_version` con il precedente `active_value_id` come `draft_id` e verifica il sorgente effettivo. Non eliminare tutta la personalizzazione per correggere un campo: perderesti altre mappature e si applicherebbe il valore predefinito.

Non riavviare in blocco i documenti storici. Il riavvio può cancellare dati estratti e log di esportazione e ripetere approvazioni o esportazioni. Controlla per ogni documento stato dell’esportazione, approvazioni e modifiche manuali prima di decidere.

Per altre configurazioni parti da `find_setting` o `run_config_checks` e chiedi l’azione supportata o il percorso nell’interfaccia. Conserva proposta prima/dopo, risultati dei test, ID dei valori attivi e riferimento di ripristino nel registro della modifica.
