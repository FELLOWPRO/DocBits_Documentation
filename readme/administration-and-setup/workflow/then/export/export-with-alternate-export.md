# Esporta con esportazione alternativa

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## Quando utilizzare questa carta

Utilizzare questa azione Quindi per l'esportazione alternativa configurata sul tipo di documento corrente. Configura e convalida il percorso prima di aggiungere l'azione.

## La configurazione deriva dal tipo di documento

La scheda non dispone di un selettore di configurazione dell'esportazione. Legge se l'esportazione alternativa è abilitata, la configurazione dell'esportazione alternativa e lo stato dopo l'esportazione dalle impostazioni del tipo di documento. Internamente questi sono `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` e `DOC_ALTERNATE_EXPORT_STATUS`.

Un'esportazione alternativa esplicitamente disabilitata produce una condizione non riuscita. Vengono segnalati i dati di attivazione mancanti, la configurazione o lo stato dei risultati anziché sostituire silenziosamente il percorso predefinito. La richiesta di esportazione controlla le attività in sospeso.

## Verificare il risultato

Ispeziona il registro della carta, la cronologia delle esportazioni, lo stato del documento e la destinazione del test autorizzata. Una richiesta, un timeout o un cambiamento di stato da soli non stabiliscono che i dati abbiano raggiunto la destinazione. Controlla la cronologia delle esportazioni prima di ritentare un'operazione che potrebbe creare duplicati.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Esempio di esportazione alternativa

**Configurazione:** Prepara il tipo di documento sintetico `DEMO_INVOICE` con l'esportazione alternativa abilitata, una configurazione di esportazione del test autorizzata e lo stato del risultato desiderato nelle impostazioni del tipo di documento. Aggiungi questa azione Quindi dopo i controlli richiesti. Questa scheda legge quelle impostazioni; non offre un selettore di configurazione di esportazione.

**Risultato previsto e controesempio:** L'azione richiede l'esportazione attraverso quella configurazione alternativa e controlla le attività in sospeso. Verificare separatamente il risultato dell'esportazione e la destinazione del test. La disabilitazione dell'esportazione alternativa provoca una condizione non riuscita; un'impostazione o una configurazione di attivazione assente non indica un'esportazione riuscita. Non eseguire questo esempio su una destinazione contabile.

Questa è una configurazione di test illustrativa e il risultato atteso; non è stato eseguito. Utilizza dati e destinatari configurati nella tua organizzazione di test.
