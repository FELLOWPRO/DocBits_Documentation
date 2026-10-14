# Standard Workflow

Il builder **Standard Workflow** è l'editor lineare basato su schede per automatizzare l'elaborazione dei documenti. Un workflow è composto da tre gruppi di schede — **When** (il trigger), **And** (condizioni aggiuntive) e **Then** (le azioni da eseguire). Quando un documento soddisfa le condizioni When/And, le azioni Then vengono eseguite automaticamente.

## Come accedere

Apri **Workflow Dashboard → Workflow List**, quindi clicca su **Add Workflow** per creare un nuovo workflow Standard, oppure clicca su un workflow esistente per modificarlo.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List con tipo, ordine di esecuzione e trigger"><figcaption><p>La Workflow List — ogni riga è un workflow che puoi aprire, attivare/disattivare o modificare.</p></figcaption></figure>

## Il modello When / And / Then

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Canvas Standard Workflow con schede When, And e Then"><figcaption><p>Il canvas Standard Workflow. Questo esempio si attiva sulle fatture in una sotto-organizzazione e le assegna a un utente.</p></figcaption></figure>

- **When** — il trigger che avvia il workflow (es. *Il tipo di documento è Fattura*).
- **And** — condizioni aggiuntive che devono essere anch'esse vere (es. *Il documento fa parte di una sotto-organizzazione*). Lascia vuoto per eseguire a ogni corrispondenza della scheda When.
- **Then** — le azioni da eseguire (es. *Assegna il documento all'utente*, crea un'attività, chiama un'API, invia un'email).

## Aggiungere schede

Clicca su **Add Card** in qualsiasi gruppo per aprire la libreria delle schede. Le schede sono organizzate per categoria così puoi trovare il blocco di base di cui hai bisogno:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Libreria Add Card raggruppata per categoria"><figcaption><p>La libreria <strong>Add Card</strong> — schede di condizione, schede di confronto, schede di azione e altro, raggruppate per categoria.</p></figcaption></figure>

Salva con **Save Workflow**, oppure salva il layout come template riutilizzabile con **Save Template**.

## Prossimi passi

- Scopri cosa fa ogni scheda nella sezione **Cards**.
- Combina le schede in soluzioni collaudate con le **Workflow Pattern Guides**.
- Per flussi con ramificazioni e percorsi paralleli (Wait ALL / Wait ANY / OR), usa il builder **Advanced Workflow**.
