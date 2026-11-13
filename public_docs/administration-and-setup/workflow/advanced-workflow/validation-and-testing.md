# Validazione e Testing

## Video: Variabili, test e attivazione

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

[Guarda i cinque capitoli](../advanced-workflow-videos.md)

Mentre costruisci un Workflow Avanzato, due controlli nella barra degli strumenti ti permettono di verificarlo senza uscire dal builder. Servono per *verifiche rapide durante la costruzione*; per test salvati e ripetibili, usa il [Test Manager](../test-manager.md).

## Convalidare

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.mp4" %}

**Video:** Convalidare un Workflow · 0:53 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Convalida controlla la struttura** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.mp4#t=0.25)

Prima di salvare, fai clic su Convalida nella barra degli strumenti. Controlla come è costruito il Workflow: se una scheda Quando lo avvia, se ogni scheda è collegata e se i percorsi hanno senso. I problemi compaiono sopra l'area di lavoro.

**Clic sul messaggio: ecco la scheda** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.mp4#t=16.816)

Fai clic su un messaggio per andare alla scheda a cui si riferisce. Qui la scheda di assegnazione non è collegata, quindi non verrebbe mai eseguita. Collegala.

**Nessun messaggio: il Workflow è valido** · [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.mp4#t=29.016)

Convalida di nuovo. Quando non resta nulla, il Workflow è valido e puoi salvarlo.

**Prima convalidare, poi testare** · [0:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/it.mp4#t=36.183)

Il salvataggio fa gli stessi controlli, ma salva il Workflow anche se restano problemi, quindi convalida prima. La convalida non controlla i tuoi dati né le impostazioni nelle schede. Per vedere cosa fa un Workflow con un documento reale, testalo.

</details>

Fai clic sul controllo **Validate** (l'icona con il cerchio e la spunta, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validazione controlla il grafo alla ricerca di problemi — nodi non collegati, configurazione mancante e connessioni non valide — e li segnala così puoi correggerli prima che il workflow venga eseguito su documenti reali.

## Test

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4" %}

**Video:** Testare un Workflow · 1:47 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Testare prima di attivare** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=0.25)

Testa un Workflow prima di attivarlo. Un test esegue ciò che c'è ora sull'area di lavoro, anche le modifiche non salvate. Azioni come assegnare o esportare sono solo simulate, quindi il documento resta com'è.

**Testare l'intero Workflow** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=14.45)

Ecco un Workflow non ancora salvato. Per testare l'intero Workflow, fai clic su Testa il flusso di lavoro nella barra degli strumenti.

**Scegliere un documento di prova** · [0:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=24.65)

Scegli il documento per il test. I Workflow che non hanno bisogno di un documento si possono testare anche senza. Cerca il documento per nome, selezionalo e fai clic su Test.

**Leggere il risultato sull'area di lavoro** · [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=37.183)

Il test segue il percorso del documento. Questa fattura non è in attesa di approvazione, quindi la scheda E finisce con una condizione non riuscita e il percorso arancione prosegue fino alla scheda di assegnazione. I percorsi non presi sono in grigio, e il banner in alto mostra il risultato e la durata del test.

**Dettagli per ogni scheda** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=58.35)

Fai clic su Dettagli per vedere ogni scheda con risultato e messaggio. Ripeti il test lo esegue di nuovo dopo una modifica.

**Testare una singola scheda** · [1:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=67.516)

Per testare una singola scheda, passaci sopra e fai clic sul pulsante play. Puoi anche fare clic destro sulla scheda e scegliere Test da questo nodo. Il test parte da questa scheda, con la stessa scelta del documento.

**Il badge mostra i dettagli** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=83.316)

Vengono eseguite solo questa scheda e quelle successive. Passa sopra il badge per vedere il risultato della scheda. Modifica la scheda e testa di nuovo finché fa ciò che ti aspetti.

**Cosa significano i colori** · [1:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/it.mp4#t=95.283)

In breve: verde significa successo, arancione una condizione non riuscita e rosso un errore. Le schede non eseguite sono sbiadite e hanno un badge grigio.

</details>

Fai clic sul controllo **Test** (l'icona di riproduzione, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) per eseguire il flusso corrente su un campione e osservare come si comporta, senza incidere sui documenti live. È il modo più rapido per fare un controllo di base su una modifica appena apportata sul canvas.

## Quando usare l'uno o l'altro

- **Validate / Test nel builder** (questa pagina) — feedback immediato mentre progetti il flusso.
- **[Test Manager](../test-manager.md)** — salva lo scenario così puoi rieseguirlo in seguito (e insieme a tutti gli altri tuoi scenari) per individuare regressioni dopo modifiche future.

## Prossimi passi

- Rivedi i tipi di nodo e le connessioni in [Nodi](nodes.md).
- Consulta tutti i controlli della barra degli strumenti e del canvas in [Toolbar e Canvas](toolbar-and-canvas.md).
