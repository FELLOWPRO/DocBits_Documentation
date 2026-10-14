# Canali PDP/PPF obbligatori – PEPPOL solo come trasporto per la fatturazione elettronica 2026 in Francia

## PDP o PPF obbligatori per le fatture elettroniche B2B nazionali

In base all'obbligo di fatturazione elettronica 2026 in Francia, le aziende non possono affidarsi esclusivamente alla rete PEPPOL per scambiare fatture B2B nazionali. La legge richiede che tutte le fatture tra imprese francesi titolari di partita IVA transitino attraverso una piattaforma privata certificata (PDP) oppure attraverso il portale pubblico di fatturazione dello Stato (PPF) per soddisfare i [requisiti](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) ￼ di legge. In altre parole, le imprese non invieranno più le fatture direttamente ai clienti: dovranno trasmetterle tramite una piattaforma di fatturazione elettronica approvata (una PDP) o tramite il [portale](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) ￼ governativo. Questo garantisce che l'amministrazione fiscale riceva i dati richiesti in tempo reale. Il semplice scambio di fatture tramite PEPPOL senza il coinvolgimento di una PDP/PPF accreditata non soddisferebbe gli obblighi di segnalazione e trasmissione previsti.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Introduzione all'offerta di servizio

La modalità API consente agli utenti di accedere a tutte le funzionalità a loro disposizione dagli strumenti IT già implementati nelle strutture dei partner. Esistono due metodi di integrazione:

### ·       Integrazione nei sistemi informativi (IS):

Le API vengono integrate direttamente nei sistemi informativi o nei software gestionali delle parti che emettono e ricevono fatture o dei loro operatori di dematerializzazione (OD). Gli utenti possono così accedere direttamente alle funzionalità della soluzione e ai relativi aggiornamenti dai loro abituali strumenti IT, interni o offerti dal proprio OD.

Le API possono inoltre essere integrate nell'IS delle PDP per offrire loro maggiore flessibilità (rispetto alla modalità EDI), con alcune API dedicate al loro utilizzo.

### ·       Integrazione in software di terze parti:

Gli editori potranno offrire software basati sulle API. A seconda della modalità scelta dall'editore, la connessione potrà essere effettuata dall'editore stesso o dal cliente durante l'installazione o la distribuzione nel proprio IS. Questo software di terze parti integrerà il sistema informativo del cliente aggiungendo uno strato di comunicazione verso il PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL utilizzato solo come livello di interoperabilità

La Francia adotta PEPPOL come parte della propria infrastruttura, ma solo come livello di trasporto all'interno del quadro delle PDP, non come percorso di conformità indipendente.  L'amministrazione fiscale francese (DGFiP) sta diventando la Peppol Authority per standardizzare il modo in cui le PDP si [interconnettono](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) . Tutte le PDP certificate devono interconnettersi tramite la rete PEPPOL per lo scambio delle [fatture](https://nymus.be/fr/facturation-electronique-en-france/) .  Ciò significa che PEPPOL faciliterà l'interoperabilità tra le piattaforme autorizzate, senza sostituire la necessità di tali piattaforme.  In pratica, un'azienda può utilizzare PEPPOL solo operando tramite una PDP (o il PPF che agisce nel suo ruolo limitato) che usa PEPPOL per inviare o ricevere fatture. Ciò è stato confermato dalle indicazioni ufficiali: il portale pubblico si concentra sulla raccolta dei dati, mentre la distribuzione delle fatture avverrà esclusivamente tramite le PDP, che si avvarranno di reti come [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) per lo [scambio](https://nymus.be/fr/facturation-electronique-en-france/) .

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Connessione di un hub:

L'hub fornisce ai propri clienti una soluzione web o applicativa che consente di effettuare le varie chiamate API. **È quindi l'hub che effettua le chiamate API per conto di tutti i suoi clienti**. In questo caso, ogni partner deve disporre di un account tecnico, ma solo l'hub necessita di un'applicazione su PISTE e di una connessione al PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Fonte: l'articolo 91 della Legge di bilancio francese 2024 (sintetizzato da EY) prevede che le fatture elettroniche siano inviate tramite una PDP certificata o il portale statale .  Gli aggiornamenti dell'amministrazione fiscale francese chiariscono ulteriormente che, dopo le riforme del 2024, le imprese devono utilizzare una PDP registrata per la fatturazione elettronica B2B (il PPF non fungerà più da piattaforma di scambio gratuita) .  PEPPOL viene implementato per collegare queste PDP, non come canale alternativo al di fuori del sistema . Ciò conferma che l'uso della sola rete PEPPOL non è sufficiente: la conformità al regime di fatturazione elettronica 2026 in Francia richiede l'integrazione con il PPF o con una PDP certificata, con PEPPOL che funge solo da rete di consegna sottostante tra tali piattaforme.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
