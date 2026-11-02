# Strategia del ciclo di vita delle release di DocBits

Con il rollout della prossima release minore R1.1, DocBits introdurrà una nuova strategia del ciclo di vita delle release basata su due canali di release: VESTA e NOVA.

**NOVA** è il canale per l'introduzione di nuove release maggiori e minori, come **Rx** e **Rx.y**. **VESTA** continua a fornire l'attuale release di produzione.

{% hint style="success" %}
**Importante: un unico URL per VESTA e NOVA**

Continui a utilizzare il consueto URL dell'applicazione DocBits. VESTA e NOVA non hanno URL di accesso separati: entrambi i canali di release sono accessibili tramite lo stesso URL standard che Lei già utilizza per l'ambiente corrispondente.

Per cambiare canale, vada su **Settings > Company Information > Release Channel** e selezioni **VESTA** o **NOVA**. Non è necessario disconnettersi e accedere nuovamente. Il Suo clic successivo nell'applicazione La porta automaticamente alla release del canale selezionato.

Prima di effettuare il passaggio, verifichi che entrambi i canali siano pronti e disponibili nel Suo ambiente, come spiegato in [Verificare la disponibilità degli ambienti prima del passaggio](#importante-verificare-la-disponibilita-degli-ambienti-prima-del-passaggio).
{% endhint %}

## Canali di release

| Canale | Ruolo nel ciclo di vita |
| --- | --- |
| **VESTA** | Fornisce l'attuale release di produzione. |
| **NOVA** | Fornisce la release successiva mentre procede attraverso le fasi di sviluppo, test e disponibilità in produzione. Durante la produzione parallela, NOVA e VESTA offrono entrambi release di produzione attive. |

## Panoramica del ciclo di vita

![Ciclo di vita delle release di DocBits in tre fasi con VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Ogni ciclo è composto da tre fasi. Un rollover gestito da FELLOWPRO porta quindi la release di produzione NOVA in VESTA e avvia il ciclo successivo.

| Fase | VESTA | NOVA | Cosa significa per la Sua organizzazione |
| --- | --- | --- | --- |
| **1. Sviluppo** | R1.0.x in produzione | R1.1 in sviluppo | Continuare a utilizzare VESTA mentre viene preparata la release successiva. |
| **2. QA e test di accettazione** | R1.0.x in produzione | R1.1 in QA e UAT | Valutare la release in arrivo nella sandbox NOVA mentre il lavoro di produzione prosegue su VESTA. |
| **3. Produzione parallela** | R1.0.x in produzione | R1.1.x in produzione | Restare su VESTA oppure passare autonomamente a NOVA quando si è pronti. |

Dopo il rollover, tutti i clienti utilizzano VESTA R1.1.x e NOVA viene riutilizzato per lo sviluppo di R1.2. La fase 1 ricomincia con queste versioni aggiornate.

### Fase 1 — Sviluppo

VESTA fornisce l'attuale release di produzione, R1.0.x, mentre la release successiva, R1.1, viene sviluppata in NOVA. Durante questa fase, la Sua organizzazione prosegue le proprie attività quotidiane su VESTA.

### Fase 2 — QA e test di accettazione

La release NOVA in arrivo attraversa le fasi di quality assurance (QA, garanzia della qualità) e user acceptance testing (UAT, test di accettazione da parte degli utenti). Può valutarla nella sandbox NOVA per verificare in che modo le modifiche si adattano ai processi della Sua organizzazione e prepararsi all'adozione.

Durante questa fase, VESTA R1.0.x rimane la release di produzione. Potrà passare a NOVA per l'uso in produzione non appena sarà disponibile nella fase 3.

### Fase 3 — Produzione parallela

VESTA R1.0.x e NOVA R1.1.x sono entrambe release di produzione attive. La Sua organizzazione decide se e quando passare a NOVA, in base alle proprie esigenze e ai risultati della valutazione nella sandbox.

Per adottare NOVA durante questa fase:

1. Valuta la release nella sandbox NOVA.
2. Consulti l'annuncio della release o chieda conferma al supporto FELLOWPRO che entrambi gli ambienti di produzione siano pronti e disponibili per il passaggio.
3. Decida quando la Sua organizzazione è pronta a utilizzare la nuova release in produzione.
4. In DocBits, vada su **Settings > Company Information > Release Channel** e selezioni **NOVA**.

Durante la produzione parallela, può anche tornare a VESTA andando su **Settings > Company Information > Release Channel** e selezionando **VESTA**.

Il cambio di canale è in modalità self-service. FELLOWPRO non stabilisce quali clienti debbano passare a NOVA. Può continuare a utilizzare VESTA per tutta la durata della produzione parallela e adottare la nuova release con il rollover successivo.

## Rollover della release e ciclo successivo

FELLOWPRO gestisce il rollover non appena la release NOVA è pronta a diventare la release di produzione comune e l'accettazione della transizione pianificata è stata ottenuta da tutti i clienti:

**NOVA R1.1.x → VESTA R1.1.x**

### Annuncio anticipato e accettazione da parte dei clienti

FELLOWPRO annuncia in anticipo il rollover pianificato a tutti i clienti via e-mail e richiede la loro accettazione della transizione. La invitiamo a contattare FELLOWPRO per eventuali dubbi od obiezioni, in modo che possano essere discussi prima del rollover. Il rollover e il riutilizzo di NOVA avvengono solo quando la release è pronta e tutti i clienti hanno accettato la transizione pianificata.

### Cosa cambia con il rollover

| Modifica | Risultato |
| --- | --- |
| **La release NOVA diventa la release VESTA** | R1.1.x diventa la release di produzione comune in VESTA per tutti i clienti. |
| **La release precedente viene ritirata** | R1.0.x viene dismessa e non è più disponibile in nessuno dei due canali né con qualsiasi altro mezzo. |
| **NOVA viene riutilizzato per la release successiva** | In NOVA inizia lo sviluppo di R1.2, avviando la fase 1 del ciclo successivo. |

Le stesse tre fasi si ripetono quindi con i nuovi numeri di versione.

Il diagramma seguente illustra in maggiore dettaglio il ciclo di release descritto sopra.

![Ciclo di release dettagliato di DocBits con VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Cadenza delle release

La cadenza prevista differisce tra le release maggiori e minori introdotte tramite NOVA e gli hotfix applicati alle release di produzione in VESTA e NOVA.

#### Release maggiori e minori tramite NOVA

FELLOWPRO prevede attualmente un ciclo di circa **3–4 mesi per le release maggiori e minori** introdotte tramite il canale di release NOVA, come **Rx** e **Rx.y**. Questa stima si applica al ciclo di vita delle release descritto sopra, incluso il successivo rollover in VESTA e il riutilizzo di NOVA per la release successiva. Non descrive la frequenza degli hotfix.

Questo intervallo rappresenta la nostra attuale stima di pianificazione; non costituisce un calendario fisso, una durata massima del ciclo né una garanzia di una data di release o di rollover. La tempistica di ciascun rollover e del riutilizzo di NOVA dipende sia **dalla disponibilità della release sia dall'accettazione della transizione pianificata da parte di tutti i clienti**. Se è necessario più tempo per rendere la release pronta, affrontare i dubbi dei clienti o ottenere l'accettazione di ogni cliente, il ciclo verrà esteso e potrà durare più di quattro mesi.

FELLOWPRO comunica in anticipo ciascun rollover pianificato. Qualsiasi tempistica indicativa resta subordinata al soddisfacimento di queste condizioni.

#### Hotfix nella produzione VESTA

Gli hotfix per la release di produzione VESTA sono previsti approssimativamente **una volta al mese, oppure a intervalli leggermente più lunghi**. Si tratta di una cadenza indicativa e non di un calendario fisso né di una data di consegna garantita.

#### Hotfix di stabilizzazione nella produzione NOVA

Per gli hotfix di stabilizzazione nella produzione NOVA non è possibile specificare una cadenza generale. NOVA introduce release completamente nuove, quindi la tempistica e la frequenza di questi hotfix dipendono dalle esigenze di stabilizzazione della singola release. Non seguono pertanto la cadenza mensile indicativa di VESTA né il ciclo di 3–4 mesi delle release maggiori e minori.

## Responsabilità e scelta del cliente

| Transizione | Chi la gestisce | Cosa aspettarsi |
| --- | --- | --- |
| **Passaggio tra VESTA e NOVA durante la fase 3** | La Sua organizzazione | Valutare NOVA nella sandbox e scegliere se e quando effettuare il passaggio. Utilizzi **Settings > Company Information > Release Channel** per selezionare NOVA o tornare a VESTA durante la produzione parallela. |
| **Rollover di NOVA R1.1.x in VESTA R1.1.x** | FELLOWPRO | Prendere visione dell'annuncio anticipato via e-mail, segnalare eventuali dubbi od obiezioni e confermare l'accettazione della transizione pianificata. FELLOWPRO procede quando la release è pronta e tutti i clienti hanno dato la propria accettazione. |

## Importante: verificare la disponibilità degli ambienti prima del passaggio

Passi da VESTA a NOVA (e viceversa) tramite **Settings > Company Information > Release Channel** solo quando le release sono disponibili in parallelo e pronte per l'uso nell'**ambiente corrispondente su entrambi i canali**. La disponibilità in sandbox e in produzione deve essere valutata separatamente:

- **Sandbox:** può passare da VESTA Sandbox a NOVA Sandbox non appena la nuova release è pronta e disponibile in NOVA Sandbox, mentre VESTA Sandbox rimane disponibile. Lo stesso requisito di disponibilità vale per il passaggio inverso.
- **Produzione:** può passare tra VESTA Production e NOVA Production solo finché entrambe le release di produzione sono pronte e disponibili in parallelo. La disponibilità in NOVA Sandbox non significa che NOVA Production sia pronta per l'uso.

Effettuare il passaggio quando l'ambiente corrispondente non è pronto o disponibile può compromettere la Sua operatività. FELLOWPRO invia e-mail di annuncio delle release alcuni giorni prima che le release diventino disponibili in sandbox o in produzione. Consulti questi annunci prima di effettuare il passaggio. Se non è sicuro che un passaggio sia disponibile o opportuno per la Sua organizzazione, contatti il supporto FELLOWPRO per una conferma.

**Controllo di disponibilità pianificato:** FELLOWPRO sta lavorando a un controllo Yes/No che consentirà al supporto di rendere l'impostazione Release Channel di sola lettura oppure di abilitare il cambio di canale indipendentemente da un deployment del software. Quando questo controllo sarà disponibile, il supporto lo utilizzerà per abilitare il passaggio quando gli ambienti corrispondenti sono pronti e per mantenere altrimenti l'impostazione di sola lettura. L'obiettivo è consentire ai clienti di passare in sicurezza tra VESTA e NOVA quando l'impostazione è abilitata. Fino all'introduzione di questo controllo, un'impostazione modificabile da sola non deve essere considerata una conferma che il passaggio sia opportuno; segua gli annunci delle release oppure chieda conferma al supporto.

## Domande frequenti

### Come sappiamo se è sicuro passare tra VESTA e NOVA?

Consulti l'annuncio della release per l'ambiente che intende utilizzare, oppure chieda al supporto FELLOWPRO di confermare che il passaggio sia opportuno. Entrambi gli ambienti corrispondenti devono essere pronti e disponibili in parallelo; la disponibilità in sandbox non conferma la disponibilità in produzione. Per le indicazioni complete, incluso il controllo pianificato per abilitare o disabilitare il cambio di canale, veda sopra [Importante: verificare la disponibilità degli ambienti prima del passaggio](#importante-verificare-la-disponibilita-degli-ambienti-prima-del-passaggio).

### Possiamo restare su VESTA mentre NOVA è disponibile in produzione?

Sì. Durante la fase 3, può restare su VESTA o passare a NOVA quando la Sua organizzazione è pronta. Con il rollover successivo, la nuova release diventa VESTA e la release precedente viene ritirata.

### Come passiamo a NOVA o torniamo a VESTA?

Per prima cosa, verifichi che l'ambiente corrispondente sia pronto e disponibile su entrambi i canali, come spiegato in [Verificare la disponibilità degli ambienti prima del passaggio](#importante-verificare-la-disponibilita-degli-ambienti-prima-del-passaggio). La disponibilità in sandbox e quella in produzione sono distinte.

Durante la fase 3, vada su **Settings > Company Information > Release Channel** in DocBits e selezioni **NOVA** per adottare la nuova release di produzione, oppure **VESTA** per tornare all'attuale release di produzione VESTA. La Sua organizzazione effettua questa scelta in modo autonomo, in base alle proprie esigenze e alla valutazione di NOVA nella sandbox. Questa scelta vale finché entrambe le release sono disponibili in parallelo; la precedente release VESTA viene ritirata con il rollover.

### Quando è disponibile NOVA per l'uso in produzione?

NOVA diventa una release di produzione attiva nella fase 3, dopo lo sviluppo e QA/UAT. Durante questa fase, VESTA e NOVA sono in produzione in parallelo con versioni software diverse.

### Come veniamo informati del rollover e possiamo sollevare obiezioni?

FELLOWPRO invia un'e-mail anticipata a tutti i clienti e richiede l'accettazione della transizione pianificata. La invitiamo a sottoporre a FELLOWPRO eventuali dubbi od obiezioni. Il rollover e il riutilizzo di NOVA avvengono solo quando la release è pronta e l'accettazione è stata ottenuta da tutti i clienti.

### Possiamo continuare a utilizzare R1.0.x dopo il rollover?

No. R1.0.x viene dismessa al momento del rollover e non è più disponibile in nessuno dei due canali né con qualsiasi altro mezzo. R1.1.x diventa la release di produzione VESTA comune per tutti i clienti.

### In cosa differisce il rollover dal nostro passaggio a NOVA?

Il Suo passaggio a NOVA durante la fase 3 è una scelta self-service su quando adottare la nuova release di produzione. Il rollover è la transizione successiva gestita da FELLOWPRO: NOVA R1.1.x diventa VESTA R1.1.x, la release precedente viene ritirata e inizia il ciclo successivo.

### Cosa succede a NOVA dopo il rollover?

NOVA viene riutilizzato per lo sviluppo della release successiva, R1.2 in questo esempio. VESTA fornisce R1.1.x mentre NOVA attraversa nuovamente le fasi di sviluppo, QA/UAT e produzione parallela.

### È garantita una nuova release maggiore o minore ogni tre-quattro mesi?

No. La cadenza approssimativa di 3–4 mesi per le release maggiori e minori introdotte tramite NOVA è un'attuale stima di pianificazione, non un calendario garantito né una durata massima. Il rollover e il riutilizzo di NOVA richiedono sia la disponibilità della release sia l'accettazione da parte di tutti i clienti. Se una delle due condizioni richiede più tempo, il ciclo verrà esteso e potrà superare i quattro mesi. FELLOWPRO comunica in anticipo ciascun rollover pianificato.
