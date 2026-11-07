# Modifica ed eliminazione delle colonne

Le caselle controllano valori obbligatori, modificabilità e visibilità. Use AI si configura separatamente nel menu a tre stati spiegato sotto.

Tutto, tranne il titolo, si modifica direttamente nell'elenco; non esiste una finestra di modifica.

**Dove:** Settings → Document Processing → Document Types → Colonne della Tabella

## Attivare o disattivare un flag

Spunta o togli la spunta alla casella nella riga. La modifica viene salvata immediatamente (*Successfully saved*).

| Flag | Attivo | Disattivo |
|---|---|---|
| **Obbligatoria** | L'approvazione è bloccata finché la colonna è vuota in una qualsiasi riga; la schermata di validazione evidenzia la cella. | Le celle vuote sono ammesse. |
| **Read Only** | Il valore viene mostrato ma non può essere sovrascritto. Usalo per i valori che provengono da una ricerca o da uno script. | Gli utenti possono modificare la cella. |
| **Hidden** | La colonna scompare dalla schermata di validazione e dall'esportazione. I suoi dati vengono conservati. | La colonna viene mostrata ed esportata. |


{% hint style="info" %}
I flag hanno effetto sui documenti caricati o riavviati **dopo** la modifica. I documenti aperti mantengono la tabella attuale finché non vengono riavviati.
{% endhint %}

## Rinominare il titolo

Fai clic sull'icona di traduzione nella colonna *Azioni* (*Aggiorna chiave di traduzione*), inserisci la nuova etichetta e conferma. L'icona info accanto mostra quale etichetta è attualmente in uso e da dove proviene. Cambia solo l'etichetta; il *Nome colonna* tecnico resta lo stesso, quindi script, mappature di esportazione e regole addestrate continuano a funzionare.

## Modificare il tipo o la tabella

Non è possibile. Nascondi la colonna (o eliminala se è una colonna personalizzata) e aggiungine una nuova con il tipo corretto.

## Eliminare una colonna

L'azione di eliminazione è disponibile solo per le colonne create dalla tua organizzazione. Le colonne predefinite non possono essere eliminate: nascondile.

1. Apri il menu a tre punti nella colonna *Azioni* e scegli **Delete**. La voce non compare per le colonne predefinite.
2. Conferma.

Cosa succede:

* La colonna viene rimossa dalla configurazione. I documenti elaborati **da questo momento in poi** non la hanno più.
* I documenti già estratti mantengono la colonna e i suoi valori finché non vengono riavviati.
* Le regole addestrate che mappavano questa colonna continuano a funzionare per le altre colonne; la mappatura della colonna eliminata viene ignorata.
* Se la colonna è referenziata in una mappatura di esportazione o in uno script, rimuovi il riferimento; altrimenti l'esportazione o lo script fallisce con un errore di colonna mancante.

## Annullare un'eliminazione

Una colonna eliminata non può essere ripristinata dall'elenco. Aggiungila di nuovo con lo stesso titolo: il nome tecnico deriva dal titolo, quindi una colonna creata con lo stesso titolo riceve lo stesso *Nome colonna* e le mappature esistenti tornano a corrispondere.

## Use AI: Predefinito, Sì o No

Aprire le [colonne di tabella](README.md) del tipo di documento e della tabella corretti. **Utilizzare l'IA (Use AI)** è un menu a tre stati, non una casella. La modifica viene salvata immediatamente.

| Scelta attuale | Effetto sullo schema base |
| --- | --- |
| **Default · richiesto** oppure **Default · non richiesto** | Usa la selezione DocBits per quel tipo e nome di colonna. Predefinito non significa sempre attivo né sempre disattivo. |
| **Yes · richiesto** | Richiede esplicitamente la colonna configurata all'AI. |
| **No · non richiesto** | La esclude dallo schema base anche se normalmente viene richiesta. |

Tornare a **Default** rimuove la scelta esplicita. Una nuova colonna personalizzata normalmente non appartiene alla selezione AI predefinita: scegliere **Yes** per richiederla. Le colonne AI predefinite non coincidono con tutte le colonne fornite. Verificare effetto indicato e anteprima.

**Obbligatoria**, **Read Only** e **Hidden** controllano completezza, modificabilità e visibilità; non sostituiscono la scelta AI. **No** non elimina la colonna né cancella valori e non impedisce a regole, script o altre fonti di compilarla. Addestramento del fornitore e tag AI possono ampliare la richiesta effettiva: risolvere anche lì eventuali contraddizioni. L'interruttore non sostituisce automaticamente un risultato basato soltanto su regole.

[Structured Output per le tabelle](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
