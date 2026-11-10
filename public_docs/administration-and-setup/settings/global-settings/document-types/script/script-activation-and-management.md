# Attivazione e gestione degli script

Gli amministratori possono usare gli **Script** per gestire le regole di elaborazione di un tipo di documento. Questa guida mostra dove trovare gli script, come attivarli o disattivarli e come modificare in sicurezza uno script già pubblicato.

## Guida video: gestire gli script

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-manage-scripts/v4/it.mp4" %}
Gestire gli script di un tipo di documento
{% endembed %}

Il video mostra l'elenco degli script con filtro e ordinamento, l'attivazione e la disattivazione, la copia, la cronologia delle versioni e l'eliminazione con conferma.

## Trovare uno script

1. Aprire **Impostazioni → Tipi di Documento**.
2. Nel tipo di documento da gestire, selezionare **Script**. La pagina mostra l'elenco degli script di quel tipo di documento.
3. Cercare per nome oppure usare **Tutti**, **Attivo** e **Inattivo** per restringere l'elenco. L'elenco è ordinato per ordine di esecuzione per impostazione predefinita; i pulsanti di ordinamento nella barra dei filtri passano all'ordine alfabetico (**A-Z** / **Z-A**) o alla data di modifica (le due icone con l'orologio).

Ogni scheda mostra il nome dello script, il suo ordine di esecuzione come badge numerato, l'innesco, la versione e lo stato. La matita apre l'editor; l'icona di copia duplica lo script. **Nuovo** apre l'editor per creare un nuovo script.

<figure><img src="../../../../../.gitbook/assets/dbdc-656-script-scripts-list-it-20261110.png" alt="Elenco degli script del tipo di documento INVOICE con il campo di ricerca, i filtri Tutti, Attivo e Inattivo, i pulsanti di ordinamento e tre schede di script; ogni scheda mostra accanto al nome un badge numerato con l'ordine di esecuzione 10, 20 o 30"><figcaption><p>Il badge numerato su ogni scheda corrisponde all'ordine di esecuzione dello script.</p></figcaption></figure>

## Impostare l'ordine di esecuzione

Il campo **Execution order** stabilisce l'ordine in cui vengono eseguiti gli script: i numeri più bassi vengono eseguiti per primi. Il campo resta etichettato in inglese anche nell'interfaccia italiana.

1. Aprire lo script nell'editor.
2. Immettere un numero intero a partire da 0 nel campo **Execution order**. Lasciare il campo vuoto per mantenere 0.
3. Salvare lo script. Lettere, numeri decimali e numeri negativi vengono rifiutati con un messaggio di errore sul campo e non viene salvato nulla.

Se si modifica l'ordine di esecuzione e poi si attiva una versione, DocBits salva prima lo script e attiva la versione solo se quel salvataggio riesce.

<figure><img src="../../../../../.gitbook/assets/dbdc-656-script-execution-order-field-it-20261110.png" alt="Riga di campi dell'editor dello script con Nome, Tipo di documento, Innesco attivo, il campo Execution order con il valore 10 e la selezione del tipo di documento secondario"><figcaption><p>L'ordine di esecuzione si inserisce nel campo <strong>Execution order</strong>.</p></figcaption></figure>

## Attivare o disattivare uno script

Usare l'interruttore **Attivo/Inattivo** sulla scheda dello script. La modifica viene salvata immediatamente; i conteggi dell'elenco si aggiornano per mostrare il risultato. Uno script inattivo resta disponibile per essere esaminato o modificato, ma non viene eseguito durante l'elaborazione dei documenti.

**Controllare lo stato dopo aver creato uno script.** Nell'interfaccia attuale del Sandbox, salvando un nuovo script viene creata una versione attiva e la scheda risulta **Attivo**. Passarla a **Inattivo** se si tratta solo di una bozza o di un esempio di prova.

<figure><img src="../../../../../.gitbook/assets/dbdc-656-script-card-status-it-20261110.png" alt="Una scheda di script con il badge 10 per l'ordine di esecuzione, l'innesco Dopo l'estrazione, la versione v2, le icone per modificare, copiare ed eliminare e l'interruttore Inattivo"><figcaption><p>A destra della scheda: la matita per modificare, l'icona di copia, il cestino per eliminare e l'interruttore <strong>Attivo/Inattivo</strong>.</p></figcaption></figure>

## Modificare uno script esistente

1. Selezionare la scheda dello script o la sua icona a matita. Una versione pubblicata è di sola lettura, quindi non è possibile scriverci sopra direttamente.
2. In **Cronologia delle versioni**, selezionare l'icona a matita della versione che si vuole modificare. Questo crea una **Bozza** basata su quella versione.
3. Modificare la bozza e selezionare l'icona **Salva**. Prima di salvare, controllare il nome, il tipo di documento, l'innesco e il codice.
4. Provare lo script modificato con documenti rappresentativi in un ambiente di prova. Quando è pronto, selezionare l'icona di spunta della bozza in **Cronologia delle versioni** per rendere quella versione attiva.
5. Tornare all'elenco degli script e controllare l'interruttore **Attivo/Inattivo** della scheda. La versione contrassegnata come **ATTIVO** nella Cronologia delle versioni indica la versione selezionata; l'interruttore della scheda determina se lo script viene eseguito.

<figure><img src="../../../../../.gitbook/assets/dbdc-656-script-published-version-it-20261110.png" alt="Versione pubblicata dello script mostrata come di sola lettura con il messaggio che invita a clonarla come bozza e la Cronologia delle versioni a destra"><figcaption><p>Una versione pubblicata non può essere modificata direttamente. Usare la matita nella Cronologia delle versioni per creare una bozza.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-656-script-editable-draft-it-20261110.png" alt="Bozza modificabile nella Cronologia delle versioni accanto alla versione attiva dello script"><figcaption><p>Salvare e controllare la bozza prima di renderla la versione attiva.</p></figcaption></figure>

Per esempi di script e le funzioni disponibili, vedere [Scripting in DocBits](scripting-in-docbits/README.md).
