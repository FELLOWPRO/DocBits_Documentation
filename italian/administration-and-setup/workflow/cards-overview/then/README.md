# Then

Una carta **Then** indica al workflow cosa fare dopo il trigger **When** e le eventuali condizioni **And**. In **Costruttore di flussi di lavoro**, seleziona **Aggiungi scheda** sotto **Allora...**. Scegli una categoria a sinistra oppure digita un nome in **Scheda di ricerca**. Seleziona un'anteprima di carta per aggiungerla, compila i campi mostrati sulla carta e salva il workflow. Scorri all'interno del selettore per vedere altre carte. Seleziona **×** per chiuderlo senza aggiungere una carta. Vedi [Flusso di lavoro](../../) per la sequenza completa.

Le anteprime qui sotto mostrano le azioni disponibili, non impostazioni già completate. Scegli l'azione che corrisponde al risultato che vuoi ottenere.

## Campo del documento

Imposta o inverte una casella di controllo, inserisci un testo in un campo oppure copia un campo in un altro. Scegli i nomi dei campi e il valore richiesti dalla carta. Vedi [Campo del documento](document-field/).

<figure><img src="../../../../.gitbook/assets/then-category-document-field-it.png" alt="Selettore di carte Then in italiano con Campo del documento selezionato; le anteprime mostrano le azioni su casella di controllo, testo e copia del campo."><figcaption><p>Modifica un campo o copiane il contenuto.</p></figcaption></figure>

## Documento

Scegli **Approvare il documento** o **Rifiutare il documento** quando il workflow deve prendere questa decisione. Usa prima una condizione **And** se l'approvazione deve dipendere da un controllo. Vedi [Documento](document/).

<figure><img src="../../../../.gitbook/assets/then-category-document-it.png" alt="Selettore di carte Then in italiano con Documento selezionato; sono visibili le anteprime Approvare il documento e Rifiutare il documento."><figcaption><p>Approva o rifiuta il documento corrente.</p></figcaption></figure>

## Logica

Usa queste carte per convertire valori tra formato numerico, testo e booleano, oppure per leggere un valore da JSON. Scegli i campi di input e output sulla carta selezionata.

<figure><img src="../../../../.gitbook/assets/then-category-logic-it.png" alt="Selettore di carte Then in italiano con Logica selezionato; le anteprime visibili convertono tipi di dati e leggono valori da JSON."><figcaption><p>Trasforma i valori per un passaggio successivo del workflow.</p></figcaption></figure>

## Stato

Scegli **Cambiare lo stato in** per portare il documento a uno stato selezionato. La carta può anche attivare un altro workflow. Vedi [Stato](status/).

<figure><img src="../../../../.gitbook/assets/then-category-status-it.png" alt="Selettore di carte Then in italiano con Stato selezionato; l&#x27;anteprima Cambiare lo stato in include un campo di stato e un trigger di workflow opzionale."><figcaption><p>Porta il documento a un altro stato.</p></figcaption></figure>

## Prompts e scripts

Scegli questa categoria per eseguire uno script di prompt DocOperator. Seleziona lo script e le variabili richiesti dalla carta. La carta offre anche impostazioni di esecuzione come i tentativi.

<figure><img src="../../../../.gitbook/assets/then-category-prompts-scripts-it.png" alt="Selettore di carte Then in italiano con Prompts e scripts selezionato; è visibile un&#x27;anteprima di script di prompt DocOperator."><figcaption><p>Esegui uno script di prompt DocOperator configurato.</p></figcaption></figure>

## Esportazione

Avvia un'esportazione, esporta con una configurazione scelta oppure metti in coda un'esportazione finale. Scegli la configurazione di esportazione e l'opzione per le attività in sospeso mostrata sulla tua carta. Vedi [Esportazione](export/).

<figure><img src="../../../../.gitbook/assets/then-category-export-it.png" alt="Selettore di carte Then in italiano con Esportazione selezionato; le anteprime mostrano esportazione iniziale, con configurazione, in coda e alternativa."><figcaption><p>Scegli quando e come viene esportato il documento.</p></figcaption></figure>

## Compito

Crea un compito o una notifica e assegnalo a un utente o a un gruppo. Inserisci titolo, descrizione, priorità e impostazioni di notifica richiesti dalla carta. Alcune carte assegnano in sequenza. Vedi [Compito](task/).

<figure><img src="../../../../.gitbook/assets/then-category-task-it.png" alt="Selettore di carte Then in italiano con Compito selezionato; le anteprime visibili creano o assegnano compiti e notifiche."><figcaption><p>Crea lavoro di follow-up per una persona o un gruppo.</p></figcaption></figure>

## Email

Invia un'e-mail usando un modello selezionato, verso destinatari oppure verso gruppi. Scegli il modello e la destinazione sulla carta.

<figure><img src="../../../../.gitbook/assets/then-category-email-it.png" alt="Selettore di carte Then in italiano con Email selezionato; le anteprime inviano un&#x27;e-mail con modello a destinatari o gruppi."><figcaption><p>Invia un'e-mail con modello.</p></figcaption></figure>

## Tabella

Modifica le voci o calcola i valori in una tabella del documento. Seleziona la tabella, le colonne, l'operatore e la colonna dei risultati richiesti dalla carta. Vedi [Tabella](table/).

<figure><img src="../../../../.gitbook/assets/then-category-table-it.png" alt="Selettore di carte Then in italiano con Tabella selezionato; le anteprime modificano le voci e calcolano le colonne dei risultati."><figcaption><p>Aggiorna o calcola i dati della tabella.</p></figcaption></figure>

## Cessionario

Assegna il documento a un utente, un gruppo, un destinatario o una sub-organizzazione. Alcune carte usano un campo o una tabella decisionale e offrono un ripiego. Scegli la destinazione giusta e il ripiego sulla carta selezionata. Vedi [Cessionario](assignee/).

<figure><img src="../../../../.gitbook/assets/then-category-assignee-it.png" alt="Selettore di carte Then in italiano con Cessionario selezionato; le anteprime visibili assegnano un utente, un destinatario, un gruppo o un contatto fornitore."><figcaption><p>Invia il documento alla persona o al gruppo responsabile successivo.</p></figcaption></figure>

## Azione

Esegui un altro workflow, invia una richiesta HTTPS, chiama un'API oppure usa la carta di calcolo dell'incremento dei costi. Queste azioni possono influire su altri sistemi; chiedi all'amministratore quale endpoint e quali impostazioni usare. Vedi [Azione](action/).

<figure><img src="../../../../.gitbook/assets/then-category-action-it.png" alt="Selettore di carte Then in italiano con Azione selezionato; le anteprime mostrano Esegui il flusso di lavoro, richiesta HTTPS, chiamata API e calcolo dell&#x27;incremento dei costi."><figcaption><p>Avvia un altro workflow o un'azione di integrazione.</p></figcaption></figure>
