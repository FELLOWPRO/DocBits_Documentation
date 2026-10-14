# Il Nostro Sistema di Priorità dei Documenti

Nel nostro sistema di elaborazione dei documenti, gestiamo un grande volume di documenti provenienti da più clienti ogni giorno. Per garantire che i documenti di ogni cliente vengano elaborati in modo tempestivo, abbiamo implementato un sofisticato sistema di priorità. Questo sistema regola dinamicamente le priorità in base al numero di documenti in attesa che un cliente ha, garantendo **equitá** e **efficienza**. Approfondiamo come funziona questo sistema di priorità e quando il contatore delle attività viene azzerato.

**Concetti Chiave del Sistema di Priorità**

Il nostro sistema di priorità ruota attorno a pochi concetti chiave:

1. **Documenti in Attesa**: Questo è un conteggio dei documenti che un cliente ha inviato ma che devono ancora essere elaborati.
2. **Intervallo di Reset**: Il sistema azzera periodicamente il conteggio dei documenti in attesa a zero per garantire che nessun cliente possa monopolizzare le risorse di elaborazione indefinitamente.

**Come Viene Determinata la Priorità**

Ecco una spiegazione passo dopo passo di come viene determinata la priorità per l'elaborazione dei documenti:

1. **Monitoraggio dei Documenti in Attesa**: Ogni cliente ha un conteggio dei documenti in attesa. Questo conteggio ci aiuta a sapere quanti documenti stanno aspettando di essere elaborati per ciascun cliente.
2. **Reset del Conteggio**: Per mantenere l'equità, azzeriamo il conteggio dei documenti in attesa a zero se è trascorso un certo periodo di tempo (l'intervallo di reset) dall'ultimo aggiornamento. Questo intervallo è impostato a 1500 secondi (o 25 minuti) per impostazione predefinita.
3. **Aggiornamento del Conteggio**: Se l'intervallo di reset non è trascorso, riduciamo il conteggio dei documenti in attesa di uno ogni volta che controlliamo, simulando l'elaborazione di un documento.
4. **Impostazione delle Priorità**: La priorità per l'elaborazione delle attività si basa sul numero di documenti in attesa. Meno documenti in attesa ci sono, maggiore è la priorità, il che significa che quelle attività verranno elaborate prima. Abbiamo soglie specifiche per assegnare i livelli di priorità da 1 (priorità più alta) a 9 (priorità più bassa).

**Livelli di Priorità**

I livelli di priorità sono assegnati in base al conteggio dei documenti in attesa come segue:

* **Priorità 9**: Se il conteggio dei documenti in attesa è inferiore a -20
* **Priorità 8**: Se il conteggio dei documenti in attesa è inferiore a -14
* **Priorità 7**: Se il conteggio dei documenti in attesa è inferiore a -12
* **Priorità 6**: Se il conteggio dei documenti in attesa è inferiore a -10
* **Priorità 5**: Se il conteggio dei documenti in attesa è inferiore a -8
* **Priorità 4**: Se il conteggio dei documenti in attesa è inferiore a -6
* **Priorità 3**: Se il conteggio dei documenti in attesa è inferiore a -4
* **Priorità 2**: Se il conteggio dei documenti in attesa è inferiore a -2
* **Priorità 1**: Se il conteggio dei documenti in attesa è maggiore o uguale a -2

{% hint style="info" %}
In termini più semplici, man mano che il numero di documenti in attesa aumenta, il livello di priorità diminuisce, il che significa che quei documenti vengono elaborati più tardi rispetto ad altri con priorità più elevate.
{% endhint %}

**Quando il Contatore Viene Azzerato**

Il contatore dei documenti in attesa viene azzerato a zero se è trascorso più dell'intervallo di reset (**1500** secondi) dall'ultimo aggiornamento. Questo meccanismo garantisce che nessun cliente possa accumulare documenti in attesa all'infinito e monopolizzare le risorse del sistema. Azzerando periodicamente il contatore, garantiamo che ogni cliente ottenga una giusta quota di tempo di elaborazione.
