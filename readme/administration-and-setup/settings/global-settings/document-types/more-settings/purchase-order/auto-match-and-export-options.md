# Opzioni di Auto Match & Export

Tre impostazioni alla fine della scheda **Ordine di acquisto** decidono chi vede le scorciatoie per la corrispondenza PO e quali documenti possono essere esportati automaticamente dopo una corrispondenza. Si applicano a un tipo di documento alla volta.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-it.png" alt="La scheda Ordine di acquisto delle impostazioni del tipo di documento con tutte le opzioni PO"><figcaption><p>La scheda Ordine di acquisto. Le tre opzioni descritte di seguito sono le ultime tre righe.</p></figcaption></figure>

## Consenti esportazione automatica per linee di ordine di acquisto non abbinabili

L'esportazione automatica dopo la corrispondenza PO richiede normalmente un documento **completamente abbinato**. Quando questo interruttore è attivo, possono essere esportati automaticamente anche i documenti con lo stato **Nessuna linea PO abbinabile**. Questo stato significa che l'ordine di acquisto non ha righe a cui la fattura può essere abbinata.

* **Disattivato (predefinito):** vengono esportati automaticamente solo i documenti completamente abbinati.
* **Attivato:** vengono esportati automaticamente i documenti completamente abbinati e i documenti senza linee PO abbinabili.

L'interruttore ha effetto solo quando i documenti vengono esportati automaticamente, ad esempio con [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) o con una scheda di esportazione DocFlow. Non cambia il modo in cui le righe vengono abbinate.

## Corrispondenza automatica ed esportazione visibili a

Lo schermo di corrispondenza PO contiene l'azione **Auto Match & Export**. Abbina il documento e lo esporta subito dopo la corrispondenza. Questa impostazione controlla chi ottiene l'azione:

| Valore | Chi vede l'azione |
| ------ | ----------------- |
| **Solo amministratore** (predefinito) | Gli amministratori |
| **Tutti gli utenti** | Ogni utente che può aprire lo schermo di corrispondenza PO |

Gli amministratori vedono sempre l'azione. L'impostazione non attiva la funzione. Il modulo [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) deve essere attivo per l'organizzazione.

## Utilizzare l'importo netto delle linee per il totale corrispondente visibile a

Lo schermo di corrispondenza PO può calcolare il **Totale abbinato** a partire dall'**Importo netto** delle righe di fattura abbinate, invece di calcolarlo in altro modo. Questa impostazione controlla chi può attivare questo calcolo:

| Valore | Chi vede l'interruttore |
| ------ | ----------------------- |
| **Solo amministratore** (predefinito) | Gli amministratori |
| **Tutti gli utenti** | Ogni utente che può aprire lo schermo di corrispondenza PO |

Quando l'interruttore è attivo, il Totale abbinato utilizza direttamente i valori dell'Importo netto delle righe di fattura abbinate.
