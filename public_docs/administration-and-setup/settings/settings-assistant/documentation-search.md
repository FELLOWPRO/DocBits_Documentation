# Come funziona la ricerca nella documentazione

Il Settings Assistant cerca informazioni pertinenti nelle pagine pubbliche su [docs.docbits.com](https://docs.docbits.com). I risultati possono includere il titolo di una pagina, un breve passaggio e un collegamento alla pagina di origine. Apri il collegamento quando ti servono le istruzioni complete o uno screenshot.

## Trovare la pagina giusta

La ricerca combina la corrispondenza di parole con la corrispondenza per significato. Questo aiuta quando la tua domanda usa parole diverse da quelle del titolo di una pagina. L'assistente può anche usare la pagina di impostazioni che stai guardando per rendere la risposta più pertinente.

Se la ricerca per significato non è temporaneamente disponibile, la ricerca nella documentazione può comunque usare la corrispondenza di parole. Una domanda specifica con il nome dell'impostazione è il modo migliore per riprovare.

## Lingue

La ricerca nella documentazione usa attualmente gli indici delle pagine di aiuto in **inglese** e **tedesco**. Se l'interfaccia DocBits usa un'altra lingua, l'assistente ripiega sui risultati della documentazione in inglese. La pagina collegata mostra la propria lingua; verificala prima di seguire passaggi o confrontare screenshot.

## Quando le modifiche diventano cercabili

L'indice di ricerca viene aggiornato quando vengono pubblicate modifiche alla documentazione inglese o tedesca dal repository della documentazione. Una riconciliazione regolare rimuove anche i collegamenti a pagine che non sono più nella navigazione della documentazione. Una pagina appena pubblicata può richiedere un po' di tempo per comparire nell'assistente.

### Panoramica tecnica per gli amministratori

Le pagine di aiuto pubblicate vengono suddivise in sezioni e memorizzate in un **OpenSearch documentation index** dedicato per ogni lingua supportata. Questo indice è separato dagli indici usati per i documenti caricati di un'organizzazione. Quando una pagina cambia, le sezioni invariate possono essere saltate e quelle modificate vengono reindicizzate. Le pagine rimosse vengono cancellate dall'indice della documentazione.

Per una domanda, il servizio combina le corrispondenze per parole chiave con la similarità vettoriale, poi ordina i passaggi più pertinenti. Se il servizio di embedding non è disponibile, la ricerca per parole chiave resta disponibile. Il Settings Assistant riceve collegamenti alle fonti e brevi passaggi da questa ricerca nella documentazione; non legge l'indice dei documenti di un'organizzazione per questo scopo.

Se non riesci a trovare una pagina, cerca direttamente su [docs.docbits.com](https://docs.docbits.com), prova una domanda più precisa o contatta il supporto DocBits.

{% hint style="info" %}
Questa ricerca copre le pagine di aiuto DocBits. La funzione [Fulltext Search](../document-processing/module/fulltext-search.md) cerca nei documenti della tua organizzazione e ha impostazioni proprie.
{% endhint %}

Torna a [usare il Settings Assistant](README.md).
