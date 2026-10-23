# La casella di controllo è selezionata

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_checkbox_is_v2-it-it.png" alt="La casella di controllo è selezionata, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni in base allo stato (selezionato o deselezionato) di una casella di controllo all'interno del tuo sistema ERP. Valutando la condizione della casella di controllo, facilita l'attivazione di processi specifici o l'applicazione di determinate regole all'interno dell'applicazione.

## **Componenti della scheda:**

* **Nome campo**
  * **Descrizione:** Specifica il nome del campo casella di controllo che verrà valutato.
  * **Dettaglio:** Deve corrispondere all'identificatore esatto del campo utilizzato nel sistema. Determina lo stato di quale casella di controllo viene monitorato.
* **Booleano**
  * **Descrizione:** Definisce la condizione che attiva il workflow.
  * **Opzioni:**
    * **True:** Il workflow si attiva se la casella di controllo è selezionata.
    * **False:** Il workflow si attiva se la casella di controllo è deselezionata.

#### **Funzionalità:**

* **Rilevamento dello stato:** La scheda monitora continuamente lo stato del campo casella di controllo specificato.
* **Valutazione della condizione:** Il sistema verifica se la casella di controllo è nello stato (selezionato o deselezionato) specificato dalla condizione Boolean.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se lo stato della casella di controllo corrisponde alla condizione Boolean specificata (true per selezionato o false per deselezionato), il sistema avvia le azioni associate. Queste potrebbero includere l'abilitazione o la disabilitazione di campi del modulo, l'attivazione di notifiche, l'avvio di workflow o l'aggiornamento di record.
  * **Condizione falsa:**\
    Se lo stato della casella di controllo non corrisponde alla condizione, possono essere intraprese azioni alternative o nessuna azione, a seconda della configurazione del workflow.

## **Configurazione e impostazione:**

* Gli utenti configurano la scheda selezionando il campo casella di controllo da un elenco di campi disponibili e impostando la condizione Boolean.

## Conclusione:

La scheda di workflow "Checkbox Field Condition" è uno strumento fondamentale per gestire moduli e documenti dinamici all'interno di un sistema ERP, dove gli input dell'utente possono determinare i successivi processi sui dati. Automatizzando le azioni in base allo stato di una casella di controllo, questa scheda migliora l'efficienza del workflow e garantisce che i comportamenti del sistema siano allineati con gli input dell'utente. Una documentazione chiara di questa scheda aiuterà gli utenti a implementarla efficacemente nelle loro operazioni, consentendo un migliore controllo sui comportamenti dei moduli e sulle automazioni dei processi.

**Nota: Non tutti i clienti dispongono della casella di controllo, ma può essere aggiunta se desiderato.**

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Esegui un follow-up solo dopo che è stato impostato un flag di revisione esplicito.

**Configurazione:** Seleziona il campo della casella di controllo `review_complete` e il booleano `true`.

**Risultato atteso e controesempio:** Una casella selezionata passa. Una casella di controllo deselezionata fallisce; non utilizzare un campo mancante come prova del completamento della revisione.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
