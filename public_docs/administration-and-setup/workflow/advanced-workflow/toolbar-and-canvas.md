# Barra degli strumenti e canvas

## Video: Costruttore e canvas

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

[Guarda i cinque capitoli](../advanced-workflow-videos.md)

La barra degli strumenti dell'Advanced Workflow scorre lungo la parte inferiore del canvas e ti offre tutto ciò di cui hai bisogno per costruire, navigare e gestire il flusso.

## Controlli della barra degli strumenti

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4" %}

**Video:** Designer di Advanced Workflow: schede e percorsi · 2:25 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Iniziare un nuovo Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=0.25)

Apri la Dashboard del flusso di lavoro e seleziona Nuovo flusso di lavoro.

**Scegliere Flusso di lavoro avanzato** · [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=5.983)

Scegli Flusso di lavoro avanzato. Il designer si apre con un nodo di inizio, da cui parte ogni Workflow.

**Quando, E e Poi** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=13.55)

Aggiungi schede con il menu Aggiungi o con un clic destro sull'area di lavoro. Le tre categorie di schede sono Quando, E e Poi.

**Quando: la condizione di attivazione** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=25.95)

La scheda Quando è la condizione di attivazione. Decide quando parte il Workflow, per esempio per un certo tipo di documento.

**E: una condizione in più** · [0:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=39.45)

Le schede E aggiungono altre condizioni. Controllano il documento, per esempio il suo stato. Il risultato è un successo o una condizione non riuscita.

**Poi: la scheda di azione** · [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=52.883)

Le schede Poi sono le schede di azione. Cambiano il documento, per esempio impostano un campo o approvano il documento.

**Trascinare per collegare** · [1:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=61.583)

Per collegare due schede, trascina da un punto a destra di una scheda all'ingresso a sinistra della scheda successiva.

**Blu: successo** · [1:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=69.383)

Il blu è il percorso del successo. Ce l'ha ogni scheda. Il Workflow lo prende quando la scheda termina.

**Arancione: condizione non riuscita** · [1:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=78.216)

L'arancione è il percorso della condizione non riuscita. Ce l'hanno solo le schede E. Il Workflow lo prende quando la condizione non è soddisfatta.

**Rosso: errore** · [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=89.383)

Il rosso è il percorso di errore. Ce l'hanno le schede E e Poi. Il Workflow lo prende quando una scheda fallisce con un errore.

**Se-altrimenti con gestione degli errori** · [1:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=99.816)

Insieme questi percorsi formano un se-altrimenti con gestione degli errori. Il successo esegue un'azione, una condizione non riuscita un'altra, e un errore un'alternativa, per esempio un'attività per una persona.

**Un percorso per ogni stato** · [1:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=114.016)

Per più casi, collega le schede Stato del documento tramite i loro percorsi di condizione non riuscita. Ogni scheda controlla uno stato, così ogni stato ha il suo percorso.

**Il percorso verso una scheda e da essa** · [2:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/it.mp4#t=126.616)

Fai clic su una scheda per evidenziarne il percorso di esecuzione: le schede che un documento attraversa per raggiungerla e quelle che possono seguirla. Tutto il resto si attenua. Qui l'attività si raggiunge solo dalla scheda Quando, tramite il percorso di errore rosso della scheda di stato.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4" %}

**Video:** Descrizioni e note del Workflow · 1:11 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Spiegare il Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=0.25)

Un Workflow con più rami è più facile da mantenere quando si spiega da solo. Il designer ha due strumenti per questo: una descrizione dell'intero Workflow e note sull'area di lavoro.

**Descrivere l'intero Workflow** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=13.483)

Seleziona Modifica descrizione nella barra degli strumenti e scrivi in una o due frasi a cosa serve il Workflow. La descrizione viene salvata quando salvi il Workflow.

**Aggiungere una nota** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=25.383)

Per spiegare un singolo passo, fai clic destro sull'area di lavoro, apri il menu di aggiunta e scegli Nota. La nota compare dove hai fatto clic.

**Doppio clic per scrivere** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=35.583)

Fai doppio clic sulla nota per scriverci, fino a cinquecento caratteri. Fai clic accanto quando hai finito.

**Spostare e ridimensionare** · [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=43.783)

Trascina la nota accanto alle schede che spiega e tira il suo angolo in basso a destra per ingrandirla.

**Dare un colore alle note** · [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=50.716)

Fai clic destro su una nota per cambiarne il colore. I colori aiutano a raggruppare le note, per esempio blu per le spiegazioni e rosso per le domande aperte.

**Le note non vengono mai eseguite** · [1:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/it.mp4#t=62.05)

Le note sono solo per le persone. Non sono collegate a nessuna scheda e non vengono mai eseguite, quindi non cambiano ciò che fa il Workflow.

</details>

- **+ Add** — apre il menu nodi per aggiungere un nodo (vedi [Nodi](nodes.md)).
- **Undo / Redo** — torna indietro o avanti tra le tue modifiche.
- **Zoom in / Zoom out** — cambia il livello di zoom del canvas.
- **Workflow name** — assegna un nome al workflow direttamente in linea.
- **Edit description** — aggiungi una descrizione per il workflow.
- **Variables** — apre il pannello [Variabili](variables.md).
- **Help** — apre la finestra delle scorciatoie da tastiera e dell'aiuto.
- **Validate / Test** — controlla ed esegui il flusso (vedi [Validazione e test](validation-and-testing.md)).
- **Snap to grid** — attiva o disattiva l'allineamento dei nodi alla griglia per layout ordinati.
- **Mini-map** — attiva o disattiva una piccola mappa di panoramica per navigare grafi di grandi dimensioni.
- **Save** — salva il workflow. Un indicatore di **auto-save** mostra quando il flusso è stato salvato automaticamente l'ultima volta.

## Scorciatoie da tastiera

Premi <kbd>?</kbd> sul canvas per aprire in qualsiasi momento la finestra delle scorciatoie e dell'aiuto.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Finestra delle scorciatoie da tastiera e dell'aiuto"><figcaption><p>La finestra delle scorciatoie da tastiera e dell'aiuto — scorciatoie, evidenziazione del percorso di esecuzione e colori dei collegamenti.</p></figcaption></figure>

| Scorciatoia | Azione |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Salva workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Valida workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Testa workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Annulla / Ripeti |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Copia / Incolla / Duplica i nodi selezionati |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Seleziona tutti i nodi |
| <kbd>Shift</kbd> + Trascina | Seleziona i nodi (trascinamento) |
| <kbd>Cmd/Ctrl</kbd> + Clic sinistro | Aggiungi/rimuovi un nodo dalla selezione |
| Clic destro | Menu di aggiunta nodi |
| <kbd>Del</kbd> | Elimina il nodo selezionato |
| <kbd>?</kbd> | Mostra questo aiuto |

## Passi successivi

- Costruisci il flusso con [Nodi](nodes.md) e [Variabili](variables.md).
