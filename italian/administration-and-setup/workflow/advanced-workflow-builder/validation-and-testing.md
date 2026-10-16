# Validazione e Testing

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
