# Barra degli strumenti e canvas

## Video: Costruttore e canvas

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
