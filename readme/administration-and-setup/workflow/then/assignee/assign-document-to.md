# Assegna documento a

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-0e17d9fb5a83-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

## Scopo:

La scheda di workflow **"Assegna documento a \[Utente/gruppo] in base alla tabella decisionale"** assegna dinamicamente i documenti a utenti o gruppi in base all'esito di una **tabella decisionale**. Questa funzionalità garantisce che l'assegnazione dei documenti venga gestita in modo efficiente e coerente sulla base di condizioni predefinite.

## Componenti della scheda:

1. **Utente/Gruppo**
   * **Descrizione:** Specifica l'**utente** o il **gruppo** a cui verrà assegnato il documento.
   * **Dettaglio:** Selezionato in base all'esito della **tabella decisionale**.
2. **Tabella decisionale**
   * **Descrizione:** Una **tabella decisionale** viene utilizzata per determinare l'**utente** o il **gruppo** appropriato per l'assegnazione del documento.
   * **Dettaglio:** Utilizza la decision table definita nella sezione **"e"**.

## Funzionalità:

* **Valutazione della condizione:** La scheda esegue la sua azione solo se sia la sezione **"Quando"** che la sezione **"E"** risultano vere.
* **Assegnazione dinamica del documento:** Il documento viene assegnato all'**utente** o al **gruppo** determinato dalla **tabella decisionale**.

## Configurazione e impostazione:

* **Definisci la tabella decisionale:** Configura la **tabella decisionale** per includere le condizioni che determinano l'**utente** o il **gruppo** di destinazione.
* **Assegna il documento a User/Group:** Il documento verrà assegnato dinamicamente in base all'esito della decision table.

## Conclusione:

La scheda di workflow **"Assegna documento a \[Utente/gruppo] in base alla tabella decisionale"** offre funzionalità di assegnazione dinamica dei documenti basate sulla logica decisionale. Ciò garantisce un'elaborazione accurata ed efficiente indirizzando automaticamente i documenti all'**utente** o al **gruppo** appropriato, migliorando l'automazione del workflow.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Scegliere un assegnatario del documento da una tabella decisionale.

**Configurazione:** Selezionare una tabella decisionale demo la cui regola di corrispondenza restituisce il revisore configurato e scegliere il tipo di assegnatario offerto da questa versione della carta.

**Risultato atteso e controesempio:** L'utente o il gruppo restituito diventa l'assegnatario del documento. Un risultato vuoto della tabella decisionale deve essere diagnosticato separatamente.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
