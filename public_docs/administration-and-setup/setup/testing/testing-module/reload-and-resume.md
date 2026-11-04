# Ricaricare e riprendere

Alcune cose si possono verificare solo dopo aver ricaricato la pagina, ad esempio che un'impostazione sia ancora presente
dopo un ricaricamento. Il passaggio **Ricarica pagina** ricarica la pagina del browser nel mezzo di un test e il test prosegue
subito dopo.

## Aggiungere un passaggio di ricaricamento

1. Nell'editor dei modelli, selezionare **+ Aggiungi passaggio**, poi il gruppo **Pagina**, quindi **Ricarica pagina**.
2. Posizionare il passaggio nel punto in cui deve avvenire il ricaricamento. I passaggi successivi vengono eseguiti nella pagina ricaricata.

<figure><img src="../../../../.gitbook/assets/testing-32-reload-step-it.png" alt="Il passaggio Ricarica pagina nell'editor dei modelli"><figcaption><p>Il passaggio Ricarica pagina nell'editor dei modelli</p></figcaption></figure>

## Che cosa succede durante un'esecuzione

1. La scheda salva l'avanzamento del test, poi ricarica la pagina.
2. Mentre l'applicazione si riavvia, un banner in alto riporta **Pagina ricaricata, il test prosegue:**, seguito dal
   nome del test. Non chiudere la scheda.
3. La pagina ricaricata riprende l'esecuzione e passa al passaggio successivo. I passaggi precedenti al ricaricamento mantengono i
   propri risultati, il passaggio **Ricarica pagina** viene mostrato come superato e il cronometro del test continua a scorrere durante il ricaricamento.

<figure><img src="../../../../.gitbook/assets/testing-33-resume-banner-it.png" alt="Banner dopo un ricaricamento: Pagina ricaricata, il test prosegue"><figcaption><p>Banner dopo un ricaricamento: Pagina ricaricata, il test prosegue</p></figcaption></figure>

I valori memorizzati vengono conservati durante il ricaricamento, tranne quelli contrassegnati come segreti (vedere
[Passaggi e blocchi predefiniti](steps-and-blocks.md)). Assicurarsi che nessun passaggio dopo il ricaricamento abbia bisogno di un valore segreto.

## Da sapere

* Solo questo passaggio ricarica la pagina senza terminare il test. Se si ricarica o si chiude la scheda manualmente, l'esecuzione termina
  come **Annullato**.
* La pagina deve tornare entro circa due minuti. In caso contrario l'esecuzione termina come **Annullato** o **Non consegnabile**.
* Un test può contenere fino a cinque passaggi di ricaricamento.
* Il test prosegue nella stessa scheda del browser e con lo stesso utente. Se il browser non consente alla scheda di salvare
  l'avanzamento (ad esempio perché l'archiviazione è bloccata), il passaggio di ricaricamento non riesce prima che la pagina venga ricaricata.
* Il test richiede lo schema di modello 1.3, che l'editor imposta quando si aggiunge il passaggio.
