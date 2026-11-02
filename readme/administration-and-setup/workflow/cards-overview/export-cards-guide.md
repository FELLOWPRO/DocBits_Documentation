# Schede di esportazione del flusso di lavoro e stato dei documenti

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-11f244132c25-it.png" alt="Schede disponibili nella categoria selezionata. Configurare i campi prima dell’uso. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Schede disponibili nella categoria selezionata. Configurare i campi prima dell’uso. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

Scegli se esportare immediatamente o mettere in coda una configurazione per l'esportazione finale alla fine dell'esecuzione. Queste scelte sono separate dallo stato che il documento dovrebbe avere dopo un'esportazione riuscita.

| Carta | Quando viene eseguita l'esportazione | Impostazioni importanti |
| --- | --- | --- |
| Avvia esportazione con convalida (`EXPORT`) | Avvia l'esportazione utilizzando le impostazioni di esportazione configurate del documento. | Convalida e, dalla v4, Stato dopo l'esportazione. |
| Esporta con configurazione di esportazione (`ACTION_EXPORT_WITH`) | Esporta utilizzando la configurazione selezionata durante l'esecuzione della scheda. | Esporta configurazione, Ignora attività in sospeso e, dalla v3, Stato dopo l'esportazione. |
| Esportazione coda con configurazione (`ACTION_EXPORT_WITH_CONFIG_DEFERRED`) | Raccoglie la configurazione per l'esportazione finale al termine dell'esecuzione. L'aggiunta di una richiesta di esportazione alla coda non dimostra che l'esportazione finale sia riuscita. | Esporta configurazione, Ignora attività in sospeso e, dalla v3, Stato dopo l'esportazione. |
| Esportazione alternativa (`ACTION_ALTERNATE_EXPORT`) | Utilizza il percorso di esportazione alternativo documentato sulla sua carta. | Non dare per scontato che abbia la stessa versione o opzioni di stato delle tre carte sopra. |

## Stato dopo l'esportazione

| Valore | Ciò significa dopo un'esportazione riuscita | Utilizzo tipico |
| --- | --- | --- |
| `finished` | Esportato e chiuso. | L'elaborazione è completata. |
| `exported` | Esportato ma rimane aperto per ulteriori elaborazioni. | È ancora necessario seguire l'approvazione o un altro flusso di lavoro. |

Avvia esportazione v4, Esporta con configurazione di esportazione v3 ed Esportazione in coda v3 offrono questa selezione. Le versioni precedenti mantengono `finished`. Una selezione mancante ritorna a `finished` e viene registrata; un valore non valido viene rifiutato prima dell'esportazione. Una vecchia carta salvata non acquisisce il nuovo comportamento semplicemente perché esiste una nuova versione del modello. Ispezionare la versione della scheda e ripetere il test di eventuali aggiornamenti espliciti.

Le condizioni dello stato del documento e lo stato di modifica offrono anche `exported` nelle versioni contenenti l'aggiornamento dello stato corrispondente. La sola modifica dello stato non esegue un'esportazione. Utilizza il risultato dell'esportazione e i log per stabilire che i dati hanno effettivamente raggiunto la loro destinazione.

## Esportazione immediata con configurazione

1. Aggiungi la carta in Quindi e seleziona una configurazione di esportazione valida.
2. Scegli se ignorare le attività in sospeso. Tienilo disattivato se le attività devono bloccare l'esportazione.
3. Sulla v3 seleziona deliberatamente `finished` o `exported`.
4. Effettuare il test con un documento in stato di elaborazione consentito, quindi controllare il risultato e la destinazione della carta.

Se le attività in sospeso impediscono l'esportazione, la scheda registra un'esportazione rifiutata. Risolvi le attività e organizza l'attivazione del flusso di lavoro previsto o riprova. Questa carta non promette di attendere e riprendere automaticamente. Inoltre, un timeout non prova che il sistema remoto non abbia fatto nulla; controllare la cronologia delle esportazioni prima di ripetere un'operazione che potrebbe creare duplicati.

## Esportazione della coda con configurazione

Aggiungi questa scheda quando l'esportazione deve essere raccolta per la fase finale dell'esecuzione. Seleziona la configurazione, la policy delle attività in sospeso e lo stato dei risultati. La scheda registra la configurazione richiesta; ispezionare separatamente il risultato finale dell'esportazione. Il messaggio di conferma della richiesta in coda non costituisce conferma di una registrazione contabile.

Selezionare ad esempio `exported` quando un'esportazione andata a buon fine deve lasciare il documento disponibile per una successiva approvazione. Selezionare `finished` quando non sono necessarie ulteriori elaborazioni. Ricontrolla lo stato finale e la destinazione dell'esportazione.

## Controlli obbligatori

Testare una configurazione valida, una configurazione mancante, attività in sospeso con entrambe le impostazioni ed entrambi gli stati dei risultati. Testare la versione già utilizzata in un flusso di lavoro esistente prima di modificarla. Per un'esportazione in coda verificare l'esecuzione finale; per un'esportazione immediata verificare il proprio risultato. Esamina i [Registri del flusso di lavoro](../workflow-logs.md) e non confondere una scheda saltata con il successo.

<!-- workflow-card-complete-example-20261021 action_export_with_config_deferred -->

### Esempio di esportazione differita

**Configurazione:** Sulla v3 scegli la configurazione di prova `DEMO_EXPORT`, lascia disattivata Ignora attività in sospeso e seleziona `exported` come stato dopo l'esportazione. Posiziona la carta nel percorso convalidato previsto.

**Risultato atteso e controesempio:** La scheda raccoglie una richiesta di esportazione per la fine dell'esecuzione del flusso di lavoro. Solo l'esecuzione finale riuscita stabilisce che la destinazione ha ricevuto i dati e che il documento rimane aperto come `exported`. Il solo successo di una carta in coda non dimostra l'esportazione; un'attività bloccante non risolta non deve essere trattata come consegna.

Questa è una configurazione di test illustrativa e il risultato atteso; non è stato eseguito. Utilizza dati e destinatari configurati nella tua organizzazione di test.
