# Calcolo AI per i supplementi di aumento dei costi

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-2dff6d842a5a-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## Quando utilizzare questa carta

Utilizzare questa azione per richiedere il calcolo del supplemento materiale ed energetico MTZ/ETZ configurato per il documento corrente. Preparare innanzitutto i dati del documento e la configurazione del servizio di calcolo richiesti dalla propria organizzazione.

## Configurazione effettiva

La carta visualizzata non ha input per Fattore di Incremento Costo, Campo Costo Base o Campo Supplemento. Delega il calcolo al servizio configurato. Non cercare questi controlli della carta inesistenti né assumere una formula percentuale fissa dal nome della carta.

## Risultato e verifica

Una risposta di servizio riuscita contrassegna la carta come riuscita. Un timeout o una risposta non riuscita producono un errore della scheda. Ispezionare il registro della carta e i dati di sovrapprezzo risultanti del documento; il solo successo della chiamata non documenta un importo particolare.

Nella modalità di test della carta, la chiamata viene saltata e viene simulato il successo. Ciò è utile per testare la struttura del flusso di lavoro, ma non dimostra che il servizio sia stato eseguito o che sia stato calcolato un eventuale sovrapprezzo.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Richiedere il calcolo del supplemento materiale/energia configurato per una fattura preparata.

**Configurazione:** Utilizza fattura sintetica `DEMO-001` con i dati richiesti dal servizio MTZ/ETZ configurato. Aggiungi questa azione dopo le condizioni di convalida del documento.

**Risultato atteso e controesempio:** Una risposta di servizio riuscita contrassegna la carta con successo; un timeout o una risposta non riuscita producono un errore della scheda. Esaminare separatamente i campi del documento e il risultato del calcolo. La modalità di test della carta simula il successo e non chiama il servizio, quindi non può dimostrare un reale risultato di sovrapprezzo.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
