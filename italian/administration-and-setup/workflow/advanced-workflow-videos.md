---
description: "Cinque capitoli in italiano sui workflow avanzati e sui log, con sottotitoli e trascrizioni."
---

# Video di Advanced Workflow

Impara a creare, provare e diagnosticare un workflow avanzato. I cinque capitoli hanno narrazione in italiano.

I primi tre capitoli mostrano il vero designer DocBits con bozze dimostrative. L’anteprima della ricerca mostra l’elaborazione reale dei documenti e i comandi dei registri con risultati vuoti. Il capitolo di diagnosi usa ancora diagrammi didattici identificati come illustrazioni.

Ogni video include sottotitoli WebVTT e una trascrizione espandibile.

1. [Costruttore e canvas](#builder-and-canvas) · 1:52
2. [Nodi e percorsi](#nodes-and-routes) · 1:53
3. [Variabili, test e attivazione](#variables-tests-and-activation) · 1:53
4. [Trovare l’esecuzione pertinente](#find-the-relevant-execution) · 1:53
5. [Seguire i nodi e diagnosticare](#trace-nodes-and-diagnose) · 1:51

## Costruttore e canvas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.vtt) · 1:52

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

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.vtt) · 1:53

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

Segui il workflow di fatture collegato nel vero designer DocBits. Apri Variabili, confronta i tipi e il riferimento al documento, individua Convalida, prepara test con documenti o dati personalizzati e identifica Salva e attivazione. Le scene di test mostrano la configurazione di dati di esempio; non mostrano un risultato eseguito.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/it.vtt) · 1:56

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

**Preparare e verificare gli scenari di test**

Prepara test separati sopra, sotto ed esattamente a mille, oltre ai dati mancanti. Dopo l’esecuzione, controlla messaggi e durate: verde indica successo, arancione falso, rosso errore e grigio saltato. Ripeti i test dopo le correzioni. Usa il gestore test per scenari ripetibili.

**Salva prima di attivare**

Il salvataggio automatico conserva una bozza locale circa ogni trenta secondi dopo modifiche. Salva esplicitamente sul server. Attiva dopo il primo salvataggio. Verifica lo stato nell’elenco prima di attendere esecuzioni automatiche.

</details>

## Trovare l’esecuzione pertinente {#find-the-relevant-execution}

{% hint style="info" %}
Anteprima da provare: schermate reali DocBits con azioni del documento, flusso dei documenti, tempi dei passaggi, registri vuoti e filtri di stato e data. Il documento non ha un’esecuzione Advanced Workflow salvata. Questa anteprima non include ancora righe di esecuzione, paginazione o diagnosi dei nodi.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.vtt) · 1:48

<details>
<summary>Trascrizione</summary>

**Iniziare dal documento**

Nel dashboard dei documenti, apri il menu delle azioni e scegli Flusso dei documenti. La cronologia reale mostra importazione e OCR. Apri un passaggio per esaminare i tempi di attesa e di elaborazione. Questi passaggi sono distinti dai nodi Advanced Workflow.

**Leggere i contatori reali**

Qui vedi i registri dei workflow dello stesso documento. Il blu indica il totale, il rosso gli errori, il giallo le condizioni non soddisfatte e il verde i successi. Questo documento dimostrativo non ha esecuzioni registrate. Tutti e quattro i contatori mostrano quindi zero.

**Controllare le colonne delle esecuzioni**

Le colonne mostrano nome del workflow, data di creazione, durata e risultato. Distingui le esecuzioni ripetute dal timestamp. Questo documento non ha una riga da aprire.

**Aprire i filtri di stato**

L’icona dei filtri apre il menu reale. Ordina per nome o data di creazione, in ordine crescente o decrescente. Lo stato offre successo, condizione non soddisfatta ed errore.

**Scegliere le date e cancellare i filtri**

Scegli un periodo con le date di inizio e fine o il calendario. Il formato è anno, mese e giorno. Applicare richiede i risultati. Cancella i filtri reimposta la selezione. Svuota la ricerca separatamente.

**Anteprima: manca un’esecuzione salvata**

Questa anteprima permette di controllare l’accesso al documento, i dettagli di elaborazione e i comandi dei registri. Manca ancora un’esecuzione Advanced Workflow salvata per mostrare righe reali, paginazione, percorsi e messaggi dei nodi. Questi risultati non sono simulati nel video.

</details>

## Seguire i nodi e diagnosticare {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.vtt) · 1:51

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
