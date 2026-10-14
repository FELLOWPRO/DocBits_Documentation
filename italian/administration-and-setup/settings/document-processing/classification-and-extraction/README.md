# Classificazione ed estrazione

## Panoramica

Nelle impostazioni di **Classificazione ed estrazione** puoi:

* Abilitare la **suddivisione dei documenti** in base ai codici QR
* Configurare la **formattazione degli importi**
* Impostare l'**estrazione delle tabelle**
* Attivare o disattivare l'elaborazione dei file **ZUGFeRD** non supportati
* Definire regole di classificazione speciali
* Monitorare i **modelli AI** addestrati su misura usati nel processo di classificazione

Questa pagina spiega in dettaglio tutte le impostazioni disponibili.

## **Accedere alle impostazioni di Classificazione ed estrazione**

Per accedere alle impostazioni di **Classificazione ed estrazione**, vai su:\
**Impostazioni → Elaborazione del documento → Classificazione ed estrazione**

<figure><img src="../../../../.gitbook/assets/settings_classification_and_extraction.png" alt=""><figcaption></figcaption></figure>

## Suddivisione dei documenti

Nella sezione **Suddivisione dei documenti** puoi configurare se un documento caricato debba essere suddiviso in più documenti ogni volta che su una delle sue pagine compare un **codice a barre**.

Per attivare questa funzione:

1. Vai alla sezione **Suddivisione dei documenti**.
2.  Apri il menu a discesa.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_14.png" alt=""><figcaption></figcaption></figure>
3.  Seleziona **Suddividi per codice a barre/codice QR**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_15.png" alt=""><figcaption></figcaption></figure>

Avrai quindi la possibilità di:

* Selezionare uno o più tipi di codice a barre da rilevare.
*   Specificare un pattern regex a cui il codice a barre deve corrispondere per attivare la suddivisione del documento.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_16.png" alt=""><figcaption></figcaption></figure>

## Formattazione degli importi

Nella sezione **Formattazione degli importi** hai due opzioni:

* **Consenti l'arrotondamento nel confronto degli importi:**\
  Se abilitata, durante il confronto degli importi è ammessa una tolleranza di ±0,5.\
  Se disabilitata, si applica una tolleranza predefinita di ±0,05.
* **Richiedi corrispondenza esatta nel confronto degli importi:**\
  Se abilitata, gli importi devono corrispondere esattamente, senza tolleranza.\
  Se disabilitata, è ammessa una tolleranza di ±0,05.

<mark style="color:red;">**Nota**</mark>: solo una di queste due impostazioni può essere attiva alla volta.

## Estrazione delle tabelle

{% hint style="info" %}
**Prerequisiti per un'estrazione delle tabelle funzionante**

* Il tipo di documento ha delle **colonne della tabella** (Impostazioni → Impostazioni Globali → Tipi di Documento → [Colonne della Tabella](../../global-settings/document-types/table-columns.md)). Senza colonne non c'è nulla in cui estrarre i dati.
* **Estrazione delle tabelle** o **Estrazione AI delle tabelle** è attivata qui sotto, per l'intera organizzazione.
* Il documento ha testo leggibile: l'OCR è stato eseguito, oppure viene usato l'E-Text per i PDF nativi digitali ([Impostazioni OCR](../ocr-settings.md)).
* L'addestramento e i modelli AI sono **per fornitore**. Una tabella addestrata vale solo per i documenti del fornitore su cui è stata addestrata.
{% endhint %}

Puoi estrarre le tabelle dai documenti abilitando **Estrazione delle tabelle** oppure **Estrazione AI delle tabelle**. Una tabella addestrata (sia basata sull'AI che manuale) è sempre collegata a un fornitore specifico.

**Estrazione delle tabelle:** attiva l'estrazione delle tabelle basata su regole. Le tabelle vengono addestrate per fornitore nella schermata di validazione (*Vai alla vista di estrazione delle tabelle*).\
Maggiori informazioni sull'addestramento [qui](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Estrazione AI delle tabelle:** usa l'AI per estrarre la tabella di qualsiasi fornitore senza addestramento. Se i risultati per un fornitore non sono abbastanza accurati, addestra la tabella di quel fornitore; le regole salvate hanno quindi la precedenza sull'AI per quel fornitore.

**Usa Estrazione delle tabelle Vision (AI):** l'AI legge l'immagine della pagina invece del livello di testo. Aiuta con i documenti scansionati e con le tabelle prive di una chiara struttura testuale; è più lenta.

**Usa Estrazione strutturata (AI):** l'AI restituisce la tabella in una struttura fissa che corrisponde direttamente alle colonne della tabella configurate. Consigliata quando le intestazioni delle colonne sui documenti variano molto.

**Estrazione della tabella per l'elemento di costo:** se abilitata, DocBits può estrarre gli elementi di costo dalle tabelle a livello di riga e classificarli di conseguenza.\
Spiegazione dettagliata disponibile [qui](table-extraction-for-costing-element.md).

**Estrazione automatica del codice fiscale:** se abilitata, il sistema compila automaticamente il campo **Codice fiscale** nella schermata di validazione, a condizione che sia configurato un campo per il codice fiscale.\
Maggiori informazioni su questa impostazione [qui](auto-extract-tax-code.md).

**Salva regole di estrazione (solo Admin):** solo gli amministratori possono fare clic su *Salva regole* nell'addestramento della tabella. Attivala quando gli utenti continuano a salvare regole che compromettono l'estrazione di un fornitore.

**Modello AI:** seleziona il livello AI usato per l'estrazione delle tabelle: **Fast** (predefinito), **Full** (massima precisione, più lento) o **Nexus** (terzo livello opzionale). La tabella sotto il selettore mostra:

* Quali **fornitori** usano quale modello AI
* Se usano l'E-Text
* Le opzioni per eliminare una voce o reimpostare i dati di addestramento

Questa impostazione è spiegata in dettaglio [qui](ai-model.md).

### Perché la tabella appare diversa da fornitore a fornitore?

Tutto ciò che DocBits apprende su una tabella viene memorizzato **per fornitore**:

* **Regole salvate** (addestramento della tabella): posizione della tabella e mappatura delle sue colonne sul layout di quel fornitore.
* **Tag della tabella AI e regole di formattazione**: i suggerimenti che l'utente ha salvato per la tabella AI di quel fornitore.
* **Modello AI specifico per fornitore**: il livello scelto per quel fornitore in *Altre impostazioni* nella schermata di validazione.

Quindi il fornitore A con regole salvate mostra una tabella deterministica nella scheda *Tabella estratta* della schermata di validazione, mentre il fornitore B senza regole riceve la *Tabella estratta dall'AI*. Per far comportare il fornitore B come A, addestra una volta la tabella di B. Per reimpostare un fornitore, elimina le sue regole nella schermata di validazione oppure reimposta i suoi dati di addestramento nella tabella del Modello AI.

### Chiavi delle preferenze

Ogni interruttore di questa sezione viene memorizzato come preferenza dell'organizzazione. Usa la chiave quando imposti il valore tramite l'API (`/preferences/set_preference`), uno script o il DocBits MCP (`get_preference` / `set_preference`).

| Impostazione (etichetta UI) | Chiave della preferenza | Valori |
|---|---|---|
| Estrazione delle tabelle | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| Estrazione AI delle tabelle | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Usa Estrazione delle tabelle Vision (AI) | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` |
| Usa Estrazione strutturata (AI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Estrazione della tabella per l'elemento di costo | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Estrazione automatica del codice fiscale | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Salva regole di estrazione (solo Admin) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| Modello AI | `AI_MODEL` | `gpt-5.4-mini` (Fast), `gpt-5.5` (Full), `qwen3.8-max` (Nexus) |
| Versione dell'estrazione delle tabelle (finestra di conferma) | `TBL_EXT_VERSION` | stringa di versione |
| Impostazioni OCR → Usa i dati AI per le tabelle se disponibili | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| Impostazioni OCR → Usa E-Text se disponibile | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Note:

* Le preferenze booleane vengono memorizzate come stringhe `true` / `false`; una chiave mai impostata vale `false`. Se invii `1` o `0`, DocBits memorizza `true` / `false`.
* `AI_MODEL` non impostato significa **Fast**.
* La modifica di una chiave ha effetto sui documenti elaborati in seguito. Riavvia un documento per estrarlo di nuovo con la nuova impostazione.
* Le scelte per fornitore (E-Text, modello AI, regole salvate) non sono preferenze dell'organizzazione; si impostano nella schermata di validazione in *Altre impostazioni* su un documento di quel fornitore.

## Documento elettronico

**Elabora PDF ZUGFeRD non supportati:** se abilitata, le versioni **ZUGFeRD** non supportate vengono elaborate come PDF standard e l'XML incorporato viene ignorato.

L'elenco delle versioni **ZUGFeRD** supportate è disponibile [qui](../../global-settings/document-types/edi/zugferd/README.md).

## **Regole di classificazione**

Nella sezione **Regole di classificazione** puoi definire pattern **regex** e criteri specifici per aiutare il sistema a classificare automaticamente i documenti durante l'elaborazione.

Per accedere a questa sezione, fai clic sulla scheda **Regole di classificazione** in cima alla pagina.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_1.png" alt=""><figcaption></figcaption></figure>

### **Aggiungere una nuova regola di classificazione**

Per creare una nuova regola:

1.  Fai clic su **Aggiungi** in alto a destra.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_2.png" alt=""><figcaption></figcaption></figure>
2. Compila i seguenti campi:
   * **Pattern**: il pattern regex che il sistema deve cercare per attivare la classificazione.
   * **Tipo**: dove cercare il pattern (ad esempio **Codice a barre**).
   * **Sotto-organizzazione** _(facoltativo)_: specifica a quale sotto-organizzazione si applica la regola.
   * **Tipo di documento**: definisce il tipo di documento da assegnare quando il pattern corrisponde.
   *   **Sottotipo di documento** _(facoltativo)_: specifica un sottotipo per una classificazione più dettagliata.

       <figure><img src="../../../../.gitbook/assets/classification_and_extraction_3.png" alt=""><figcaption></figcaption></figure>
3.  Fai clic su **Salva** per salvare la regola di classificazione.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt=""><figcaption></figcaption></figure>

### **Modificare una regola di classificazione**

Per modificare una regola esistente:

1.  Fai clic sui tre punti nella colonna **Azioni**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt=""><figcaption></figcaption></figure>
2.  Seleziona **Modifica**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_6.png" alt=""><figcaption></figcaption></figure>
3. Apporta le modifiche desiderate.
4.  Fai clic su **Salva** per applicare gli aggiornamenti.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt=""><figcaption></figcaption></figure>

### **Eliminare una regola di classificazione**

Per eliminare una regola:

1.  Fai clic sui tre punti nella colonna **Azioni**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt=""><figcaption></figcaption></figure>
2.  Seleziona **Elimina**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_7.png" alt=""><figcaption></figcaption></figure>

## Modelli AI

La sezione **Modelli AI** mostra tutti i modelli addestrati su misura che sono stati ottimizzati specificamente per le tue esigenze.

### Accedere alla sezione Modelli AI

Per aprire questa sezione, fai clic sulla scheda **Modelli AI** in cima alla pagina.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_8.png" alt=""><figcaption></figcaption></figure>

### Categorie di modelli

I modelli sono organizzati in categorie. Sotto il nome di ogni categoria è indicato il numero di modelli che contiene.\
Fai clic su una categoria per vederne i dettagli.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_9.png" alt=""><figcaption></figcaption></figure>

In cima alla pagina della categoria selezionata trovi le informazioni principali su ogni modello:

* **Tipo**: il tipo di modello.
* **Solo prima pagina**: indica se il modello elabora solo la prima pagina di un documento.
* **Versione**: il numero di versione del modello.

### Tabella dei modelli

Tutti i modelli di una categoria sono elencati in una tabella che include le seguenti informazioni:

* **Nome**: il nome del modello.
* **Modello successivo**: il modello che elaborerà ulteriormente l'output del modello corrente.
* **Tipo di documento**: il tipo di documento principale assegnato dal modello durante la classificazione.
* **Sottotipi di documento**: i sottotipi in cui il documento viene ulteriormente classificato.
* **Priorità**: il livello di priorità che determina la posizione del modello nella coda di classificazione.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_11.png" alt=""><figcaption></figcaption></figure>

### Modificare un modello

Per modificare un modello:

1.  Fai clic sull'icona a forma di penna nella colonna **Azioni** accanto al modello che vuoi modificare.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_10.png" alt=""><figcaption></figcaption></figure>
2. Aggiorna i campi disponibili:
   * **Modello successivo**: seleziona il modello che deve elaborare l'output del modello corrente.
   * **Tipo di documento**: scegli il tipo di documento con cui il modello deve classificare l'input.
3.  Fai clic su **Salva** per applicare le modifiche.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_12.png" alt=""><figcaption></figcaption></figure>
