# Operatore DocBits

## Panoramica

Il **DocBits Operator** è un assistente di automazione alimentato da intelligenza artificiale progettato per semplificare compiti ripetitivi nei tuoi flussi di lavoro. Gli utenti creano _prompts_ - istruzioni passo dopo passo potenziate con variabili - che guidano l'IA a navigare, inserire dati e fare clic attraverso le interfacce automaticamente. Ciò riduce lo sforzo manuale e velocizza le operazioni di routine.

## Abilitazione del DocBits Operator

Per abilitare il DocBits Operator, seguire questi passaggi:

1. **Naviga nelle Impostazioni**:
   * Dal Dashboard, vai su **Impostazioni**.
   *   Seleziona **Elaborazione Documenti** e quindi scegli **Modulo**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Abilita la Funzionalità**:
   * Scorri verso il basso per individuare l'opzione **DocBits Operator**.
   *   Attiva lo slider per abilitare il **DocBits Operator**.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Accesso all'Interfaccia

*   Una volta abilitata la funzionalità, apri il **DocBits Operator** dal menu di navigazione principale.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Inserimento del Prompt**

In fondo allo schermo, c'è un campo di input denominato _"Inserisci qui il tuo prompt..."_. Qui gli utenti scrivono le istruzioni affinché l'operatore le segua.

Accanto al campo di input ci sono diversi pulsanti di controllo:

* **Variabili del Prompt** – Apre un popup dove è possibile inserire coppie chiave-valore utilizzate nel prompt. Le variabili sono scritte tra parentesi graffe, come `{numero_fattura}` o `{url}`. Questi valori si applicano solo al prompt corrente nel campo di input.
* **Salva Prompt** – Salva il prompt corrente. Scegli di salvarlo come:
  * **Prompt dell'Organizzazione** – Modificabile all'interno della tua organizzazione; include sia il prompt che i valori delle variabili definite.
  * **Prompt Globale** – Condiviso tra tutti i tenant; include solo il prompt e i segnaposto delle variabili (non vengono salvati valori).
* **Cancella Chat** – Cancella la conversazione attuale con l'operatore, ma lascia il prompt nel campo di input invariato. Utile quando si riutilizza o si perfeziona un prompt.

Per una guida dettagliata su come scrivere prompt efficaci, inclusa la sintassi, le variabili e gli esempi, consultare la [**Guida alla Scrittura del Prompt**](prompt-writing-guide.md).

### **2. Navigazione della Barra Laterale**

Usa l'icona in alto a sinistra per aprire o chiudere la barra laterale. La barra laterale mostra i prompt salvati, organizzati in due categorie:

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Prompt dell'Organizzazione**: Modificabili e riutilizzabili all'interno della tua organizzazione.
* **Prompt Globali**: Condivisi tra tutti i tenant. Questi non possono memorizzare variabili e non possono essere modificati o eliminati.
  *   Un prompt globale è comunque modificabile ed eliminabile dall'**organizzazione che lo ha creato**, dove compare sotto i Prompt dell'Organizzazione.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Funzionalità di Ricerca**: una barra di ricerca in alto alla barra laterale consente agli utenti di trovare rapidamente i prompt salvati per nome o parola chiave.
* **Riferimento Icona**: Ogni prompt salvato ha un insieme di icone di azione
  * **Freccia** – Avvia il prompt
  * **Penna** – Modifica il prompt (disponibile solo per i prompt della tua organizzazione)
  * **Cestino** – Elimina il prompt (disponibile solo per i prompt della tua organizzazione)

### 3. Salva Prompt

Cliccando il pulsante **Salva Prompt** si apre un popup dove è possibile salvare il prompt corrente per un uso futuro.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Campi del Popup Salva Prompt**

* **Nome del Prompt:** Inserisci un nome per identificare il prompt.
* **Salva Prompt Pubblicamente (Checkbox):** Quando selezionato, il prompt verrà salvato come **Prompt Globale**. I Prompt Globali sono condivisi tra tutti i tenant e non possono memorizzare **valori** variabili (solo **nomi** variabili).
* **Modifica Variabili:** Apre il [**Popup Variabili del Prompt**](prompt-writing-guide.md) per rivedere o regolare le definizioni delle variabili prima di salvare.

**Azioni**

* **Annulla:** Chiude il popup senza salvare.
* **Salva:** Salva il prompt utilizzando il nome specificato e l'impostazione di visibilità.

### 4. Controlli di Esecuzione del Prompt

Quando un prompt è in esecuzione, gli utenti hanno diverse opzioni di controllo per gestire o intervenire nel processo di esecuzione:

* **Metti in Pausa il Prompt:** Sospende temporaneamente l'esecuzione corrente. Utile se si desidera osservare lo stato attuale o preparare il sistema per i passaggi successivi. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Riprendi il Prompt:** Continua l'esecuzione dal punto in cui è stata messa in pausa. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Annulla il Prompt:** Interrompe completamente l'esecuzione e resetta la sessione. Questo è utile se il prompt deve essere interrotto o riavviato a causa di un comportamento errato o modifiche nell'input.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Prendi il Controllo:** Consente all'utente di intervenire manualmente interagendo direttamente con il sistema. Questo è utile se l'operatore si blocca o interpreta erroneamente un passaggio. Prendere il controllo **mette automaticamente in pausa** il prompt e passa alla modalità manuale fino a quando si sceglie di riprendere o annullare.

### 5. Visualizzazione Dettagli Operatore

Una volta avviato un prompt, diventa disponibile un pulsante aggiuntivo che consente agli utenti di passare a una **visualizzazione dettagliata dell'esecuzione**.\
![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Apri Visualizzazione Dettagli:** Questo pulsante ti porta a una visualizzazione dedicata che mostra, passo dopo passo, cosa sta facendo l'operatore in tempo reale.

Nella visualizzazione dettagli, gli utenti possono:

* Monitorare ogni azione eseguita (ad esempio, clic, input, attese).
* Vedere quale passaggio è attualmente attivo.
* Identificare dove si verificano problemi se il prompt incontra problemi.
* Utilizzare le stesse azioni di **Pausa**, **Riprendi**, **Annulla** e **Prendi il Controllo**.
