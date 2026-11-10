---
description: "Cinque capitoli in italiano sui workflow avanzati e sui log, con sottotitoli e trascrizioni."
---

# Video di Advanced Workflow

Tutti e cinque i capitoli includono una narrazione in italiano, un file di sottotitoli e una trascrizione. Il primo mostra la creazione del workflow di esempio passo dopo passo; gli altri approfondiscono i singoli argomenti.

I primi tre capitoli mostrano il vero designer DocBits con bozze dimostrative. L’anteprima della ricerca mostra l’elaborazione reale dei documenti e i comandi dei registri con risultati vuoti. Il capitolo di diagnosi usa ancora diagrammi didattici identificati come illustrazioni.

Ogni video include sottotitoli WebVTT e una trascrizione espandibile.

1. [Costruttore e canvas](#builder-and-canvas) · 3:35
2. [Nodi e percorsi](#nodes-and-routes) · 1:53
3. [Variabili, test e attivazione](#variables-tests-and-activation) · 1:53
4. [Trovare l’esecuzione pertinente](#find-the-relevant-execution) · 1:53
5. [Seguire i nodi e diagnosticare](#trace-nodes-and-diagnose) · 1:51

## Costruttore e canvas {#builder-and-canvas}

Conosci Roberto e segui la sua spiegazione nell’interfaccia reale di DocBits in italiano. Controlla la dashboard, l’elenco dei workflow e la licenza, poi apre una bozza non salvata nel designer. Passo dopo passo assegna un nome al workflow, configura il controllo dell’importo e due azioni, dispone le schede e collega entrambi i percorsi. Mostra poi come preparare i test con un documento o dati personalizzati. L’account dimostrativo non dispone di un abbonamento Advanced Workflow e blocca la validazione; la bozza rimane non salvata e inattiva.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.vtt) · [Trascrizione (testo)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.txt) · 3:35

| In questo video | Inizio |
| --- | --- |
| Presentazione dell’amministratore | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=0) |
| Controllare l’accesso | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=4) |
| Dare un nome al workflow | [0:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=30) |
| Configurare il controllo importo | [0:46](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=46) |
| Aggiungere l’azione Approval | [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=73) |
| Aggiungere l’azione Standard | [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=94) |
| Disporre le schede | [1:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=116) |
| Collegare i percorsi | [2:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=132) |
| Preparare i test | [2:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=158) |
| Validare, salvare e attivare | [3:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v8/it.mp4#t=185) |

<details>
<summary>Trascrizione</summary>

**Presentazione dell’amministratore**

Gestisco DocBits. Creiamo un controllo delle fatture.

**Controllare l’accesso**

Parto dalla dashboard dei workflow e apro l’elenco. Poi controllo la licenza. Workflow e Advanced Workflow richiedono entrambi un accesso attivo. Con entrambi abilitati, Nuovo workflow offre Advanced Workflow. Questo account di documentazione non ha una licenza workflow attiva. Proseguo quindi con un’anteprima non salvata nel designer.

**Dare un nome al workflow**

Lavoro nel vero designer di DocBits. Per prima cosa assegno un nome chiaro alla bozza. Controlleremo l’importo di una fattura e useremo due semplici azioni per mostrare i percorsi possibili. Questa dimostrazione resta non salvata.

**Configurare il controllo importo**

Apro il menu per aggiungere e scelgo una scheda di condizione. Nella categoria Campo documento seleziono la condizione Docfield. Inserisco il campo total_amount. Poi scelgo il confronto maggiore di. E inserisco mille. Usate la chiave del vostro campo documento. Un importo esattamente uguale a mille non soddisfa questo confronto.

**Aggiungere l’azione Approval**

Ora aggiungo una scheda azione dalla categoria Campo documento. L’azione imposta un campo del documento. Uso la chiave dimostrativa approval_route. E inserisco il valore Approval. Questo identifica il percorso. Un processo di approvazione reale richiede le proprie azioni aziendali.

**Aggiungere l’azione Standard**

Aggiungo una seconda scheda con la stessa azione. L’azione imposta un campo del documento. Uso la chiave dimostrativa approval_route. Questa volta il campo dimostrativo riceve il valore Standard. Entrambe le schede sono configurate. Servono ancora le connessioni per stabilire quale azione verrà eseguita.

**Disporre le schede**

Trascino le schede per ottenere una disposizione leggibile. Le due azioni vanno a destra. La condizione sta al centro e Start a sinistra. Spostare una scheda cambia la posizione. Non crea una connessione.

**Collegare i percorsi**

Trascino dall’uscita di Start all’ingresso della condizione. Il percorso di successo arriva ad Approval con una connessione blu. Il percorso arancione per la condizione non soddisfatta arriva a Standard. L’uscita rossa di errore è distinta e serve per gli errori di valutazione. Qui resta scollegata. In un workflow di produzione, decidete come gestire questi errori.

**Preparare i test**

Il pulsante di test nella barra apre la selezione del documento di prova. Posso scegliere un documento dimostrativo oppure preparare dati personalizzati completi. Provate importi superiori, inferiori e uguali a mille. Verificate anche un importo mancante. Questo account non ha una licenza Advanced Workflow. Mostro la preparazione del test, non un risultato eseguito.

**Validare, salvare e attivare**

La validazione controlla connessioni e impostazioni delle schede. Qui la licenza mancante impedisce la validazione. Con un account abilitato salverei esplicitamente sul server. Poi controllerei separatamente l’attivazione. Prima del primo salvataggio l’interruttore è disabilitato. L’indicatore della bozza automatica riguarda una copia locale nel browser. Non significa che il workflow sia salvato o attivato.

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
