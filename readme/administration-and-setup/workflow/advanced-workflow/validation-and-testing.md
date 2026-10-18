# Validazione e Testing

## Video: Variabili, test e attivazione

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

[Guarda i cinque capitoli](../advanced-workflow-videos.md)

Mentre costruisci un Workflow Avanzato, due controlli nella barra degli strumenti ti permettono di verificarlo senza uscire dal builder. Servono per *verifiche rapide durante la costruzione*; per test salvati e ripetibili, usa il [Test Manager](../test-manager.md).

## Validate

Fai clic sul controllo **Validate** (l'icona con il cerchio e la spunta, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validazione controlla il grafo alla ricerca di problemi — nodi non collegati, configurazione mancante e connessioni non valide — e li segnala così puoi correggerli prima che il workflow venga eseguito su documenti reali.

## Test

Fai clic sul controllo **Test** (l'icona di riproduzione, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) per eseguire il flusso corrente su un campione e osservare come si comporta, senza incidere sui documenti live. È il modo più rapido per fare un controllo di base su una modifica appena apportata sul canvas.

## Quando usare l'uno o l'altro

- **Validate / Test nel builder** (questa pagina) — feedback immediato mentre progetti il flusso.
- **[Test Manager](../test-manager.md)** — salva lo scenario così puoi rieseguirlo in seguito (e insieme a tutti gli altri tuoi scenari) per individuare regressioni dopo modifiche future.

## Prossimi passi

- Rivedi i tipi di nodo e le connessioni in [Nodi](nodes.md).
- Consulta tutti i controlli della barra degli strumenti e del canvas in [Toolbar e Canvas](toolbar-and-canvas.md).
