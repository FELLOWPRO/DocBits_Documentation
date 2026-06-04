# Validazione e test

Prima di affidarti a un Advanced Workflow, usa i controlli della barra degli strumenti per confermare che sia corretto e si comporti come previsto.

## Validate

Fai clic sul controllo **validate** (l'icona check-circle, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validazione controlla il grafo alla ricerca di problemi — nodi non collegati, configurazione mancante e collegamenti non validi — così puoi correggerli prima che il workflow venga eseguito su documenti reali.

## Test

Fai clic sul controllo **test** (l'icona play, oppure premi <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) per eseguire il workflow su un campione e vedere come si comporta, senza influire sui documenti attivi.

## Scenari di test

Per controlli ripetibili, salva gli **scenari di test** nel **Test Manager** (vedi la [Dashboard](../workflow-dashboard.md)). Ogni scenario registra un esito atteso e mostra un risultato pass/fail, e **Run All Tests** li riesegue tutti insieme — così puoi confermare che i tuoi workflow continuino a comportarsi correttamente dopo una modifica.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Elenco del Workflow Test Manager con scenari di test e Run All Tests"><figcaption><p>Il Test Manager — scenari salvati con risultati pass/fail e <strong>Run All Tests</strong>.</p></figcaption></figure>

## Passi successivi

- Rivedi i tipi di nodo e i collegamenti in [Nodi](nodes.md).
- Scopri tutti i controlli della barra degli strumenti e del canvas in [Barra degli strumenti e canvas](toolbar-and-canvas.md).
