# Barra degli strumenti e canvas

## Video: Costruttore e canvas

Conosci Roberto e segui la sua spiegazione nell’interfaccia reale di DocBits in italiano. Controlla la dashboard, l’elenco dei workflow e la licenza, poi apre una bozza non salvata nel designer. Passo dopo passo assegna un nome al workflow, configura il controllo dell’importo e due azioni, dispone le schede e collega entrambi i percorsi. Mostra poi come preparare i test con un documento o dati personalizzati. L’account dimostrativo non dispone di un abbonamento Advanced Workflow e blocca la validazione; la bozza rimane non salvata e inattiva.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.vtt) · [Trascrizione (testo)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.txt) · 3:35

| In questo video | Inizio |
| --- | --- |
| Presentazione dell’amministratore | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=0) |
| Controllare l’accesso | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=4) |
| Dare un nome al workflow | [0:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=30) |
| Configurare il controllo importo | [0:46](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=46) |
| Aggiungere l’azione Approval | [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=73) |
| Aggiungere l’azione Standard | [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=94) |
| Disporre le schede | [1:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=116) |
| Collegare i percorsi | [2:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=132) |
| Preparare i test | [2:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=158) |
| Validare, salvare e attivare | [3:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/it.mp4#t=185) |

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
