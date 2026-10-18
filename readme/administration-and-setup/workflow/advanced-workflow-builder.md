# Advanced Workflow

Il builder **Advanced Workflow** è un editor a grafo di nodi per i workflow che necessitano di ramificazioni, percorsi paralleli e controllo del flusso — oltre il modello lineare When/And/Then del builder Standard. Disponi i nodi su un canvas e li colleghi per definire il flusso di esecuzione.

## Video: percorsi delle fatture in DocBits

Il video mostra un workflow configurato nella vera interfaccia DocBits: controllo dell’importo, due azioni, collegamenti e preparazione dei casi di test.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/it.vtt)

Le immagini mostrano una bozza dimostrativa non salvata. `total_amount` e `approval_route` sono chiavi di campo di esempio. `Approval` e `Standard` identificano i percorsi. Configura le azioni aziendali necessarie per il tuo processo.

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

## Come accedere

Apri il designer Advanced Workflow dall'area dei workflow (il canvas del builder avanzato). Parti da un nodo **Start** e costruisci il flusso aggiungendo nodi.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Canvas a grafo di nodi Advanced Workflow con barra degli strumenti"><figcaption><p>Il canvas Advanced Workflow — un grafo di nodi con controlli di zoom, esecuzione, griglia e salvataggio. Assegna un nome al workflow nella barra degli strumenti.</p></figcaption></figure>

## Aggiungere nodi

Clicca su **+ Add** per aprire il menu dei nodi. Oltre alle familiari schede **When**, **And** e **Then**, il builder avanzato aggiunge nodi di controllo del flusso:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu Add di Advanced Workflow con i tipi di nodo"><figcaption><p>Il menu dei nodi <strong>+ Add</strong>: When / And / Then più Wait ALL, Wait ANY, OR e Note.</p></figcaption></figure>

- **When / And / Then** — le stesse schede di condizione e azione del builder Standard.
- **Wait ALL** — attende che *tutte* le ramificazioni in ingresso siano completate prima di continuare.
- **Wait ANY** — continua non appena *una qualsiasi* ramificazione in ingresso è completata.
- **OR** — dirama il flusso lungo percorsi alternativi.
- **Note** — un'annotazione di testo libero sul canvas (non influisce sull'esecuzione).

Esegui il flusso con il controllo di riproduzione, validalo e salvalo con il pulsante di salvataggio nella barra degli strumenti.

## Prossimi passi

- Scopri cosa fa ogni scheda nella sezione **Cards**.
- Per automazioni lineari semplici, il builder **Standard Workflow** è più rapido da configurare.
