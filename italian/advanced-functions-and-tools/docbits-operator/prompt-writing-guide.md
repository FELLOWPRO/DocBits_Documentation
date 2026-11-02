# Guida alla Scrittura dei Prompts

Questa guida spiega come scrivere prompt efficaci per l'Operatore DocBits. I prompt sono istruzioni passo dopo passo che guidano l'operatore nell'esecuzione di compiti specifici, come la navigazione delle pagine web, l'interazione con gli elementi dell'interfaccia utente e l'inserimento di dati.

## Cosa è un Prompt?

Un prompt è una sequenza di istruzioni scritte in testo che guidano l'operatore nell'esecuzione di un flusso di lavoro. I prompt possono includere comandi come cliccare sui pulsanti, compilare moduli, attendere il caricamento di pagine o elementi e altro ancora.

## Sintassi e Struttura del Prompt

* Ogni istruzione dovrebbe essere scritta come un passaggio numerato.
* Utilizzare un linguaggio chiaro e conciso per descrivere ogni azione.
* Specificare gli elementi dell'interfaccia utente per nome, etichetta o numero di indice per garantire precisione.
* Utilizzare una formattazione coerente per migliorare la leggibilità.

## Utilizzo delle Variabili nei Prompts

Le variabili ti consentono di rendere dinamici i prompt inserendo valori diversi durante l'esecuzione. Invece di inserire valori fissi come date o numeri di documento, utilizza segnaposto all'interno delle parentesi graffe, ad esempio: `{invoice_number}`, `{url}`, o `{purchase_order}`.

Ciò rende i prompt riutilizzabili e adattabili tra diversi flussi di lavoro o set di dati.

### Come Utilizzare le Variabili

* Scrivi le variabili all'interno delle parentesi graffe nel testo del prompt:
  * Inserisci il numero della fattura: {invoice\_number} nel campo 'Numero fattura HP'.
* Ogni variabile deve avere un nome univoco (ad esempio, `invoice_number`, `url`, `document_type`).
* I nomi delle variabili non devono includere spazi o caratteri speciali (gli underscore sono consentiti).
* Per i flussi di lavoro, i nomi delle variabili devono corrispondere esattamente agli ID dei campi del documento per abilitare il mapping automatico dei dati.

## Popup delle Variabili del Prompt

Per aprire il popup delle Variabili del Prompt, clicca sull'icona a **ruota dentata** situata accanto al campo di input del prompt.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Layout e Controlli del Popup

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Campo di Inserimento Chiave:** Inserisci il nome della variabile qui (senza parentesi graffe).
* **Campo di Inserimento Valore:** Inserisci il valore da utilizzare per questa variabile quando il prompt viene eseguito.
* **Salva come Sensibile (Checkbox):** Quando selezionato, questo contrassegna il valore della variabile come sensibile. I valori sensibili sono crittografati e nascosti nei flussi di lavoro per proteggere le informazioni confidenziali dagli utenti non autorizzati.
* **Pulsante Aggiungi (+):** Clicca per aggiungere un'altra riga di input coppia chiave-valore.
* **Icona Elimina (Cestino):** Quando esistono più coppie chiave-valore, tutte le coppie tranne la prima mostrano un'icona di cestino per eliminare quella specifica coppia.
* **Pulsante Cancella:** Reimposta il popup cancellando tutte le coppie chiave-valore e i valori inseriti.
* **Pulsante Salva:** Salva tutte le variabili definite e i loro valori per il prompt corrente.
