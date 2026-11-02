# Assegnare il documento al destinatario

La scheda mostrata è la **versione 2**. I campi visibili sono **Destinatario** e **Utente** come ripiego. Non identifica il destinatario come una scelta universale fra Disponente e Acquirente.

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-1b1b68dfdcad-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

## Configurazione

Seleziona la fonte del destinatario e un utente di ripiego valido per l’organizzazione. La scheda assegna il **documento** quando il workflow raggiunge l’azione e soddisfa le condizioni configurate. L’assegnazione non equivale alla creazione di un’attività né a un’approvazione.

Se il destinatario non può essere risolto, verifica l’uso del ripiego configurato nella versione in uso. Non esiste qui una prova di assegnazione garantita: anche l’utente di ripiego deve essere valido e lo stato del documento deve consentire l’operazione. Non presumere che il ripiego sia automaticamente un amministratore.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

In un’organizzazione di prova configura la fonte del destinatario e l’utente sintetico `Demo Reviewer A` come ripiego. Verifica separatamente un destinatario risolvibile e uno non risolvibile, controllando assegnazione finale e log del workflow.

L’immagine mostra campi non configurati. Questo è un esempio da eseguire e verificare nella propria organizzazione di test; durante la revisione non è stata eseguita alcuna assegnazione.
