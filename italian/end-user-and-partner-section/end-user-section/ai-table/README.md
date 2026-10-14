# Tabella AI

La Tabella estratta dall'AI è la tabella delle voci di riga che DocBits legge con l'AI quando un fornitore non ha regole di tabella addestrate. Compare nella schermata di validazione sotto i campi di intestazione. Questa pagina spiega quando la ottieni, come eseguirla di nuovo e come indirizzare ciò che estrae.

## Quando ottieni la tabella AI

* Un amministratore ha attivato l'**Estrazione AI delle tabelle** (Impostazioni → Elaborazione del documento → Classificazione ed estrazione). Se è disattivata, l'area della tabella mostra *AI Table will display here. Enable in …*.
* Il fornitore **non ha regole salvate**. Non appena qualcuno addestra la tabella del fornitore e fa clic su *Salva regole*, le regole salvate sostituiscono la tabella AI per quel fornitore; le righe compaiono quindi nella scheda *Tabella estratta* invece che nella scheda *Tabella estratta dall'AI*.
* Eccezione: le colonne contrassegnate **Usa AI** nelle impostazioni delle colonne della tabella vengono compilate dall'AI anche per i fornitori con regole salvate, vedi [Usa AI per colonna](#usa-ai-per-colonna).

Quale livello AI legge la tabella (Fast, Full, Nexus) è impostato per organizzazione e può essere sovrascritto per fornitore in *Altre impostazioni* nella schermata di validazione, vedi [Modello di IA specifico per fornitore](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Estrarre di nuovo la tabella AI

Usa questa procedura quando mancano delle righe o una colonna è spostata e vuoi che l'AI riprovi, ad esempio dopo aver aggiunto un [tag](ai-table-tags.md):

1. Aggiungi o modifica i [tag](ai-table-tags.md) nel campo sotto la tabella e fai clic su **Applica**. L'AI ricostruisce la tabella per questo documento con i tuoi tag e le modifiche alle colonne; per il fornitore non viene ancora memorizzato nulla. Se il documento ha righe abbinate a un PO, DocBits avvisa che gli abbinamenti vengono rimossi dalla ricostruzione.
2. Il risultato ti soddisfa? Fai clic su **Salva** (*Salva regole*) in modo che il prossimo documento di questo fornitore venga estratto allo stesso modo.
3. Per ricominciare da capo, fai clic su **Elimina** (*Elimina regole*): DocBits conferma *Rules has been deleted successfully* ed esegue di nuovo l'estrazione AI senza tag o formattazione salvati.

*Elimina regole* rimuove i tag e le regole di formattazione salvati per questo fornitore, non la configurazione delle colonne della tabella. Per estrarre di nuovo l'intero documento (intestazione e tabella) dopo che un amministratore ha modificato impostazioni o colonne, usa invece *Riavvia* nel menu del documento nella dashboard.

## Usa AI per colonna

Ogni colonna della tabella ha un flag **Usa AI** (Impostazioni → Impostazioni Globali → Tipi di Documento → [Colonne della Tabella](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). Con il flag attivo, l'AI compila quella colonna anche quando il fornitore ha regole salvate; le altre colonne continuano a provenire dalle regole. Uso tipico: una colonna di descrizione a testo libero che le regole addestrate acquisiscono male, oppure un valore che si sposta sulla pagina.

Tieni presente che l'AI, in quel caso, deduce la colonna dall'intera riga. Se vi inserisce sistematicamente il valore sbagliato (ad esempio il totale della riga in *Oneri*), il controllo del totale riga fallisce su ogni riga. In tal caso disattiva *Usa AI* per quella colonna, oppure aggiungi un tag che spieghi all'AI cos'è la colonna.

## Estrazione strutturata

Con **Usa Estrazione strutturata (AI)** abilitata nelle impostazioni dell'organizzazione, l'AI restituisce la tabella in una struttura fissa che corrisponde direttamente alle colonne della tabella configurate, invece di copiare le intestazioni delle colonne del fornitore. I nomi delle colonne corrispondono quindi sempre alla tua configurazione; una colonna che il fornitore stampa ma che non hai configurato non viene estratta. Chiedi al tuo amministratore di attivarla quando le intestazioni dei fornitori variano molto e perdi tempo a rimappare.

## Lavorare con la tabella estratta

Ecco le principali funzionalità e le istruzioni per l'uso:

* **Eliminazione delle colonne**: Se determinate colonne nella tabella estratta non sono necessarie, gli utenti possono rimuoverle facilmente facendo clic sull'icona "Elimina colonna" (rappresentata da tre punti verticali) accanto all'intestazione della colonna. Questo aiuta a ripulire la tabella e concentrarsi solo sulle informazioni rilevanti.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Modifica del Formato della Valuta**: Il formato della valuta può essere modificato selezionando il formato desiderato dal menu a discesa accanto al campo "Valuta". Ciò garantisce che i valori della valuta siano visualizzati nel formato preferito, rendendo più facile interpretare e analizzare i dati finanziari.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Mostrare/Nascondere Colonne Non Mappate**: Per impostazione predefinita, nella tabella sono visibili solo le colonne mappate (colonne con dati estratti). Tuttavia, gli utenti possono scegliere di mostrare o nascondere le colonne non mappate facendo clic sul pulsante "Nascondi colonne non mappate" o "Mostra colonne non mappate" in fondo alla tabella. Questa funzionalità è utile quando gli utenti desiderano esaminare tutte le colonne disponibili, anche se attualmente non contengono dati.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Modifica degli Intestazioni della Tabella**: Le intestazioni della tabella (nomi delle colonne) possono essere modificate facendo clic sull'intestazione e inserendo il nome desiderato. Questa funzionalità consente agli utenti di personalizzare i nomi delle colonne per allinearli meglio con la propria terminologia o preferenze, rendendo i dati più leggibili e comprensibili.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Salvare le modifiche**: **Salva** accanto ai tag (tooltip *Salva regole*) memorizza la mappatura delle colonne, le colonne nascoste e i tag attuali per questo fornitore. Il prossimo documento del fornitore viene estratto con queste impostazioni.

Queste funzionalità ti danno il controllo sui dati estratti. Quando lo stesso fornitore richiede ogni volta le stesse correzioni, addestra invece la tabella una volta, vedi [Campi di addestramento Linee/Tabella di addestramento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md): la tabella AI non viene più usata per quel fornitore.
