---
description: "Cinque capitoli in italiano sui workflow avanzati e sui log, con sottotitoli e trascrizioni."
---

# Video di Advanced Workflow

Impara a creare, provare e diagnosticare un workflow avanzato. I cinque capitoli hanno narrazione in italiano.

I primi tre capitoli mostrano l’interfaccia reale di DocBits. I due capitoli sui log utilizzano diagrammi didattici identificati come illustrazioni. Le schermate mostrano bozze dimostrative non salvate.

Ogni video include sottotitoli WebVTT e una trascrizione espandibile.

1. [Costruttore e canvas](#builder-and-canvas) · 1:52
2. [Nodi e percorsi](#nodes-and-routes) · 1:53
3. [Variabili, test e attivazione](#variables-tests-and-activation) · 1:53
4. [Trovare l’esecuzione pertinente](#find-the-relevant-execution) · 1:53
5. [Seguire i nodi e diagnosticare](#trace-nodes-and-diagnose) · 1:51

## Costruttore e canvas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.vtt) · 1:52

<details>
<summary>Trascrizione</summary>

**Una fattura con due percorsi**

Questo è un vero workflow avanzato in DocBits. Un controllo dell’importo della fattura conduce a due azioni. I collegamenti determinano quale azione viene eseguita. L’esempio utilizza una bozza non salvata e campi dimostrativi.

**Configurare il controllo importo**

Apri Aggiungi, scegli And e seleziona una condizione per un campo del documento. Imposta il campo dell’importo, scegli Maggiore di e inserisci mille. Usa la chiave esatta del campo definita nella configurazione del documento.

**Configurare le azioni**

Aggiungi due schede Then. Entrambe impostano il campo dimostrativo approval route. Una scrive Approval, l’altra Standard. Questi valori identificano il percorso. Configura le azioni aziendali necessarie per un workflow di produzione.

**Collegare le uscite**

Collega Start all’ingresso della condizione. Collega l’uscita blu di successo ad Approval e l’uscita arancione di condizione falsa a Standard. L’uscita rossa gestisce separatamente gli errori di valutazione. La posizione delle schede non crea un percorso.

**Preparare i casi di test**

Apri Test nella barra degli strumenti. Scegli un documento di prova o inserisci i suoi dati completi in formato JSON. Verifica importi superiori, inferiori e uguali a mille, oltre ai valori mancanti. Controlla i risultati dei nodi dopo l’esecuzione.

**Convalidare, salvare e attivare**

Convalida i collegamenti e le impostazioni delle schede. Salva esplicitamente sul server e verifica separatamente l’attivazione. Le bozze automatiche del browser non sostituiscono il salvataggio. Esecuzione e registri richiedono il modulo e l’abbonamento appropriati.

</details>

## Nodi e percorsi {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.vtt) · 1:53

<details>
<summary>Trascrizione</summary>

**Il ruolo di ogni nodo**

Start avvia manualmente. When definisce un evento. Nessuno dei due accetta connessioni in ingresso. And verifica una condizione. Then esegue un’azione. Entrambi i costruttori condividono il catalogo delle schede. Le note spiegano senza essere eseguite.

**Tre risultati distinti**

Trascina un’uscita sull’ingresso successivo. Nel designer, blu significa successo, arancione condizione falsa, rosso errore. And ha tre risultati; Then, successo ed errore. Le viste di esecuzione mostrano il successo in verde.

**Crea un’alternativa**

Verifica se una fattura supera la soglia. Collega blu all’approvazione, arancione all’elaborazione normale e rosso alla gestione errori. Una condizione falsa può continuare sul percorso collegato; non arresta tutti i rami.

**Unisci con Wait ALL**

Wait ALL unisce i rami. Ogni nodo sorgente deve aver seguito un percorso collegato alla giunzione. Collega entrambi i controlli richiesti e l’azione successiva. Un percorso non selezionato non fornisce il risultato necessario.

**Alternative con ANY e OR**

Wait ANY e OR uniscono i rami quando almeno una sorgente segue un percorso collegato. OR richiede due nodi sorgente distinti. Queste giunzioni non creano scelte esclusive né annullano altre azioni. Prova l’intero grafo.

**Mantieni il grafo eseguibile**

I nodi devono essere raggiungibili da un ingresso. Evita cicli e connessioni in ingresso a Start o When. Includi un’azione Then e convalida i percorsi. I nodi Delay importati richiedono una durata positiva; Aggiungi non offre Delay.

</details>

## Variabili, test e attivazione {#variables-tests-and-activation}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/it.vtt) · 1:53

<details>
<summary>Trascrizione</summary>

**Scegli il tipo**

Apri Variabili con le parentesi graffe. Scegli testo, numero, sì o no, oppure documento. Cerca i nomi. Document contiene un riferimento impostato da un’azione dedicata; il modulo non accetta valori di documento.

**Variabili dell’organizzazione**

Scegli nome univoco, tipo e valore iniziale. Creazione, modifica ed eliminazione vengono salvate immediatamente nell’organizzazione. Altri workflow condividono questi valori. Salvare o scartare il canvas non annulla le modifiche alle variabili.

**Convalida la struttura**

Premi Convalida. Esamina errori e avvisi sopra il canvas. Un messaggio individua il nodo. Verifica azioni, ingressi, uscite, cicli e giunzioni. Una struttura valida non garantisce dati corretti.

**Scegli il contesto**

La riproduzione nella barra apre la scelta del documento. Scegli documento, dati personalizzati o test senza documento per schede indipendenti. Start avvia direttamente. I test includono modifiche non salvate e simulano azioni distruttive.

**Esamina i risultati**

Esamina messaggi e durate: verde, successo; arancione, condizione falsa; rosso, errore; grigio, saltato. Correggi e riprova. Usa il gestore dei test per scenari ripetibili: successo, alternative, dati mancanti ed errori.

**Salva prima di attivare**

Il salvataggio automatico conserva una bozza locale circa ogni trenta secondi dopo modifiche. Salva esplicitamente sul server. Attiva dopo il primo salvataggio. Verifica lo stato nell’elenco prima di attendere esecuzioni automatiche.

</details>

## Trovare l’esecuzione pertinente {#find-the-relevant-execution}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/it.vtt) · 1:53

<details>
<summary>Trascrizione</summary>

**Apri i log del documento**

Nel pannello documenti, scegli Workflow Logs dal menu Azioni. L’accesso ai workflow deve essere abilitato. I log riguardano il documento selezionato. I test del designer e i registri di eventi o attività dell’organizzazione sono separati.

**Leggi i contatori**

Blu conta le esecuzioni nei risultati attuali; rosso, gli errori; giallo, le condizioni false; verde, i successi. I contatori rappresentano esecuzioni, non definizioni di workflow o nodi. I filtri possono modificare questi numeri.

**Scegli l’esecuzione esatta**

Ogni riga mostra nome, data di creazione, durata in secondi e risultato. Un workflow può essere eseguito più volte per un documento. Confronta gli orari. Una durata breve può apparire come zero virgola zero zero secondi per arrotondamento.

**Restringi i risultati**

Usa Cerca per trovare un workflow. L’icona delle regolazioni apre direzione e criterio di ordinamento, stato e date iniziale e finale. Ordina per nome o creazione. Inserisci le date come anno, mese, giorno e seleziona Applica.

**Controlla pagine e filtri**

Usa la paginazione per i risultati precedenti. Cancella filtri ricarica l’elenco senza selezioni. Svuota Cerca separatamente. Se mancano risultati, controlla documento, date e stato. Un elenco vuoto non dimostra un errore di esecuzione.

**Stati particolari**

Un avviso e un’icona di blocco indicano il limite di esecuzioni del documento. Esamina gli eventi ripetuti prima di cambiare i limiti. Il download video DocOperator compare solo se esiste una registrazione; riguarda quella esecuzione.

</details>

## Seguire i nodi e diagnosticare {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.vtt) · 1:51

<details>
<summary>Trascrizione</summary>

**Espandi un’esecuzione**

Espandi la riga del workflow. Un’esecuzione avanzata mostra il grafo a sinistra e i messaggi a destra; un workflow standard mostra schede in sequenza. I dati descrivono quell’esecuzione e possono differire dal designer attuale.

**Seleziona un nodo**

Sposta o ingrandisci il grafo, poi seleziona un nodo. Card Logs mostra i messaggi. Anche Wait ALL e Wait ANY possono avere messaggi di nodo. Leggi il messaggio insieme al nodo selezionato e all’orario dell’esecuzione.

**Distingui i risultati**

Verde significa successo; arancione, condizione falsa; rosso, errore; grigio, saltato. Un nodo saltato non è stato eseguito. Prima di modificarlo, verifica se è stato scelto un altro ramo o manca un ingresso alla giunzione.

**Segui la prima divergenza**

Segui il percorso reale dall’ingresso. Per un controllo importo falso, esamina arancione; per un errore, leggi il messaggio e segui rosso. Il gestore errori può riuscire mentre l’esecuzione continua a riportare l’errore originale.

**Verifica le giunzioni**

Per Wait ALL, controlla ogni sorgente e risultato collegato. Per ANY o OR, cerca una sorgente corrispondente. Due uscite dello stesso nodo non sono approvazioni indipendenti. Una condizione arancione può essere intenzionale.

**Correggi e verifica**

Annota workflow, riferimento documento, orario, nodo e messaggio esatto. Correggi configurazione o dati e prova uno scenario ripetibile. Salva e verifica l’attivazione. Confronta una nuova esecuzione con la precedente; i vecchi log conservano il comportamento precedente.

</details>
