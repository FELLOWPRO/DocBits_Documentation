# Strategia del ciclo di vita delle release di DocBits

DocBits utilizza due canali di release, **VESTA** e **NOVA**, per introdurre nuove release e concedere alla Sua organizzazione il tempo di valutarle prima dell'adozione. Durante la fase di produzione parallela, è Lei a scegliere se e quando passare alla nuova release. FELLOWPRO gestisce poi il rollover che la rende la release di produzione comune per tutti i clienti.

I numeri di versione utilizzati in questa guida, R1.0.x, R1.1.x e R1.2, sono puramente esemplificativi. Lo stesso ciclo di vita si ripete con le release successive; `x` rappresenta gli aggiornamenti all'interno di una serie di release.

## Canali di release

| Canale    | Ruolo nel ciclo di vita                                                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VESTA** | Fornisce l'attuale release di produzione.                                                                                                                                                    |
| **NOVA**  | Fornisce la release successiva durante le fasi di sviluppo, test e disponibilità in produzione. Durante la produzione parallela, NOVA e VESTA offrono entrambi release di produzione attive. |

## Panoramica del ciclo di vita

![Ciclo di vita delle release di DocBits in tre fasi con VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Ogni ciclo è composto da tre fasi. Un rollover gestito da FELLOWPRO porta quindi la release di produzione NOVA in VESTA e avvia il ciclo successivo.

| Fase                             | VESTA                | NOVA                 | Cosa significa per la Sua organizzazione                                                           |
| -------------------------------- | -------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| **1. Sviluppo**                  | R1.0.x in produzione | R1.1 in sviluppo     | Continuare a utilizzare VESTA mentre viene preparata la release successiva.                        |
| **2. QA e test di accettazione** | R1.0.x in produzione | R1.1 in QA e UAT     | Valutare la release in arrivo nella sandbox NOVA mentre il lavoro di produzione prosegue su VESTA. |
| **3. Produzione parallela**      | R1.0.x in produzione | R1.1.x in produzione | Restare su VESTA oppure passare autonomamente a NOVA quando si è pronti.                           |

Dopo il rollover, tutti i clienti utilizzano VESTA R1.1.x e NOVA viene riutilizzato per lo sviluppo di R1.2. La fase 1 ricomincia con queste versioni aggiornate.

### Fase 1 — Sviluppo

VESTA fornisce l'attuale release di produzione, R1.0.x, mentre la release successiva, R1.1, viene sviluppata in NOVA. Durante questa fase, la Sua organizzazione prosegue le proprie attività quotidiane su VESTA.

### Fase 2 — QA e test di accettazione

La release NOVA in arrivo attraversa le fasi di quality assurance (QA, garanzia della qualità) e user acceptance testing (UAT, test di accettazione da parte degli utenti). Può valutarla nella sandbox NOVA per verificare in che modo le modifiche si adattano ai processi della Sua organizzazione e prepararsi all'adozione.

Durante questa fase, VESTA R1.0.x rimane la release di produzione. Potrà passare a NOVA per l'uso in produzione non appena sarà disponibile nella fase 3.

### Fase 3 — Produzione parallela

VESTA R1.0.x e NOVA R1.1.x sono entrambe release di produzione attive. La Sua organizzazione decide se e quando passare a NOVA, in base alle proprie esigenze e ai risultati della valutazione nella sandbox.

Per adottare NOVA durante questa fase:

1. Valuti la release nella sandbox NOVA.
2. Decida quando la Sua organizzazione è pronta a utilizzarla in produzione.
3. Passi da VESTA a NOVA tramite l'impostazione **Release Channel** nell'applicazione DocBits.

Questo passaggio è in modalità self-service. FELLOWPRO non stabilisce quali clienti debbano passare a NOVA. Può continuare a utilizzare VESTA per tutta la durata della produzione parallela e adottare la nuova release con il rollover successivo.

## Rollover della release e ciclo successivo

FELLOWPRO gestisce il rollover non appena la release NOVA è pronta a diventare la release di produzione comune e l'accettazione della transizione pianificata è stata ottenuta da tutti i clienti:

**NOVA R1.1.x → VESTA R1.1.x**

### Annuncio anticipato e accettazione da parte dei clienti

FELLOWPRO annuncia in anticipo il rollover pianificato a tutti i clienti via e-mail e richiede la loro accettazione della transizione. La invitiamo a contattare FELLOWPRO per eventuali dubbi od obiezioni, in modo che possano essere discussi prima del rollover. Il rollover e il riutilizzo di NOVA avvengono solo quando la release è pronta e tutti i clienti hanno accettato la transizione pianificata.

### Cosa cambia con il rollover

| Modifica                                              | Risultato                                                                                             |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **La release NOVA diventa la release VESTA**          | R1.1.x diventa la release di produzione comune in VESTA per tutti i clienti.                          |
| **La release precedente viene ritirata**              | R1.0.x viene dismessa e non è più disponibile in nessuno dei due canali né con qualsiasi altro mezzo. |
| **NOVA viene riutilizzato per la release successiva** | In NOVA inizia lo sviluppo di R1.2, avviando la fase 1 del ciclo successivo.                          |

Le stesse tre fasi si ripetono quindi con i nuovi numeri di versione.

Il diagramma seguente illustra in maggiore dettaglio il ciclo di release descritto sopra.

![Ciclo di release dettagliato di DocBits con VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Cadenza delle release

FELLOWPRO prevede attualmente un ciclo di release di circa **3–4 mesi**. Questo intervallo rappresenta la nostra attuale stima di pianificazione; non costituisce un calendario fisso, una durata massima del ciclo né una garanzia di una data di release o di rollover.

La tempistica di ciascun rollover e del riutilizzo di NOVA dipende sia **dalla disponibilità della release sia dall'accettazione della transizione pianificata da parte di tutti i clienti**. Se è necessario più tempo per rendere la release pronta, affrontare i dubbi dei clienti o ottenere l'accettazione di ogni cliente, il ciclo verrà esteso e potrà durare più di quattro mesi.

FELLOWPRO comunica in anticipo ciascun rollover pianificato. Qualsiasi tempistica indicativa resta subordinata al soddisfacimento di queste condizioni.

## Responsabilità e scelta del cliente

| Transizione                                     | Chi la gestisce       | Cosa aspettarsi                                                                                                                                                                                                                                            |
| ----------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passaggio da VESTA a NOVA durante la fase 3** | La Sua organizzazione | Valutare NOVA nella sandbox e scegliere se e quando effettuare il passaggio tramite l'impostazione Release Channel dell'applicazione.                                                                                                                      |
| **Rollover di NOVA R1.1.x in VESTA R1.1.x**     | FELLOWPRO             | Prendere visione dell'annuncio anticipato via e-mail, segnalare eventuali dubbi od obiezioni e confermare l'accettazione della transizione pianificata. FELLOWPRO procede quando la release è pronta e tutti i clienti hanno dato la propria accettazione. |

## Domande frequenti

### Possiamo restare su VESTA mentre NOVA è disponibile in produzione?

Sì. Durante la fase 3, può restare su VESTA o passare a NOVA quando la Sua organizzazione è pronta. Con il rollover successivo, la nuova release diventa VESTA e la release precedente viene ritirata.

### Come passiamo a NOVA?

Quando NOVA è disponibile in produzione, utilizzi l'impostazione **Release Channel** nell'applicazione DocBits. La Sua organizzazione effettua questa scelta in modo autonomo, in base alle proprie esigenze e alla valutazione della release nella sandbox NOVA.

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

### È garantita una nuova release ogni tre-quattro mesi?

No. La cadenza approssimativa di 3–4 mesi è un'attuale stima di pianificazione, non un calendario garantito né una durata massima. Il rollover e il riutilizzo di NOVA richiedono sia la disponibilità della release sia l'accettazione da parte di tutti i clienti. Se una delle due condizioni richiede più tempo, il ciclo verrà esteso e potrà superare i quattro mesi. FELLOWPRO comunica in anticipo ciascun rollover pianificato.
