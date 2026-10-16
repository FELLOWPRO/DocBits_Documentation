# Esempi

Esempi end-to-end che mostrano come utilizzare insieme gli strumenti eDocs MCP.

## Esempio 1: creare un'anteprima personalizzata per XRechnung

Questo esempio illustra l'intero ciclo di vita di una regola PREVIEW personalizzata:
1. Verificare quali regole esistono già
2. Visualizzare l'anteprima dell'XSLT senza attivarlo
3. Creare la regola personalizzata
4. Aggiornarla a una nuova versione
5. Tornare al valore predefinito

### Passo 1: verificare le personalizzazioni esistenti

Chiama `list_edoc_custom_attributes`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

La risposta mostra due elenchi. Se `custom` è vuoto per l'attributo `PREVIEW`, la tua organizzazione sta attualmente utilizzando il foglio di stile di anteprima predefinito integrato.

### Passo 2: testare l'XSLT prima di crearlo

Chiama `preview_edoc_custom_xslt` con l'ID di un attributo esistente (usane uno predefinito dalla risposta di `list`) e un file XML di esempio codificato in base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Controlla l'output renderizzato per verificare che l'XSLT produca il risultato atteso prima di renderlo definitivo.

### Passo 3: creare la regola personalizzata

Chiama `create_edoc_custom_attribute`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Salva l'`attribute_id` dalla risposta. Da questo momento, ogni fattura XRechnung 2.1 CII elaborata dalla tua organizzazione utilizzerà la tua anteprima personalizzata.

### Passo 4: aggiornare la regola con una nuova versione

In seguito, se vuoi perfezionare l'XSLT, chiama `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Impostando `activate: true` si passa immediatamente alla nuova versione. La versione precedente viene conservata nella cronologia. Imposta `activate: false` per salvarla come bozza e attivarla separatamente.

### Passo 5: tornare al valore predefinito integrato

Se vuoi tornare all'anteprima predefinita, chiama `delete_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

La regola personalizzata viene rimossa e il sistema torna automaticamente al foglio di stile predefinito condiviso. Gli altri clienti non ne sono interessati.

---

## Esempio 2: personalizzare i percorsi di estrazione per EDI

La tua organizzazione riceve fatture EDI con una struttura dei campi non standard. Questo esempio mostra come sostituire i percorsi di estrazione per la tua organizzazione.

### Passo 1: verificare le regole attuali

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Se vedi una voce `EXTRACTION_PATHS` in `default` ma non in `custom`, la tua organizzazione eredita le regole XPath condivise.

### Passo 2: creare i tuoi percorsi di estrazione personalizzati

Chiama `create_edoc_custom_attribute` con il tuo JSON XPath modificato:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Passo 3: verificare con un test a vuoto

Chiama `test_electronic_document` con un file EDI di esempio per confermare che i percorsi di estrazione personalizzati rilevino i valori corretti:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

La risposta include `extracted_fields` e un PNG `preview.image_base64`: controlla entrambi per verificarne la correttezza prima di passare in produzione.

---

## Esempio 3: eseguire una verifica eDoc completa

Prima di rilasciare una modifica, verifica che tutte le fixture eDoc supportate continuino a passare:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

Lo strumento esegue ogni fixture XRechnung attraverso la pipeline e riporta superato/fallito/avviso per ciascuna fixture. Un'esecuzione pulita conferma che le tue personalizzazioni non hanno compromesso altri tipi di documento.

Per testare rapidamente un solo tipo:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Carica fino a 3 fixture ZUGFeRD, attende l'elaborazione e verifica end-to-end classificazione, estrazione e generazione dell'anteprima.
