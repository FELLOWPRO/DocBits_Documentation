# Fatturazione elettronica in Francia: piattaforme autorizzate e PEPPOL

## Regole e calendario attuali

Le fatture B2B nazionali francesi comprese nella riforma, tra imprese soggette a IVA, devono essere scambiate tramite una **piattaforma autorizzata (plateforme agréée, PA; già PDP)**. Il **portale pubblico di fatturazione (PPF)** svolge funzioni di elenco pubblico e raccolta dei dati fiscali; non è una piattaforma alternativa per lo scambio di queste fatture.

* **1° settembre 2026:** Tutte le imprese interessate devono poter ricevere fatture elettroniche. Le grandi imprese (GE) e le imprese di dimensioni intermedie (ETI) devono inoltre emetterle e adempiere agli obblighi di e-reporting da questa data.
* **1° settembre 2027:** Gli obblighi di emissione e di e-reporting si applicano alle piccole e medie imprese (PME) e alle microimprese.

L’obbligo applicabile dipende dall’ambito dell’operazione e dalla categoria dell’impresa. Consultare la [guida ufficiale sulle piattaforme autorizzate](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), il [calendario ufficiale](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) e la [risposta ministeriale](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL e interoperabilità

PEPPOL può fornire trasporto e interoperabilità tra sistemi e piattaforme connessi. Il suo utilizzo non sostituisce l’obbligo di ricorrere a una PA per lo scambio delle fatture soggette alla normativa francese. Una sola connessione PEPPOL non dimostra l’adempimento degli obblighi di scambio e trasmissione dei dati.

## Contesto tecnico storico

I sei diagrammi e le descrizioni API seguenti sono conservati come contesto tecnico proveniente da materiale precedente su PPF/PDP. Usano la terminologia e l’architettura passate; non descrivono un’opzione attuale per scambiare le fatture B2B obbligatorie tramite il PPF. Verificare le specifiche attuali delle PA e dei servizi pubblici prima di implementare un’integrazione.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Modello storico dei servizi API

Il modello precedente descriveva l’accesso alle funzioni disponibili dagli strumenti informatici delle organizzazioni partner tramite due metodi:

* **Sistemi informativi (IS):** Le API erano integrate nei sistemi di emittenti, destinatari o operatori di dematerializzazione (OD). Alcune API erano destinate ai sistemi PDP come alternativa all’integrazione EDI.
* **Software di terze parti:** Gli editori potevano aggiungere un livello di comunicazione al sistema del cliente. I precedenti riferimenti a una connessione al PPF appartengono a quel modello storico e non costituiscono un canale attuale di scambio delle fatture.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

### Diagramma storico di interconnessione

Il diagramma illustra il precedente contesto di interconnessione delle piattaforme. Un’implementazione attuale deve rispettare i requisiti delle PA; qui non si afferma un obbligo generale di usare un’unica rete di trasporto per tutti gli scambi.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

### Collegamento storico di un hub

Il modello precedente descriveva una soluzione web o applicativa in cui **l’hub effettuava le chiamate API per conto dei clienti**. Prevedeva un account tecnico per ogni partner e, per l’hub, un’applicazione in PISTE e una connessione al PPF. Sono dettagli di un’architettura storica, non una procedura di integrazione attuale verificata.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>

### Riferimenti storici

Il materiale precedente citava [il vecchio calendario e riepilogo giuridico](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [le specifiche del 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [una panoramica della riforma del 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [il contesto di interconnessione](https://nymus.be/fr/facturation-electronique-en-france/), [il contesto PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) e [il contesto dello scambio](https://nymus.be/fr/facturation-electronique-en-france/). Questi collegamenti e gli ultimi diagrammi sono conservati come contesto storico. Per gli obblighi attuali e la distinzione tra scambio tramite PA e funzioni pubbliche del PPF, utilizzare le fonti ufficiali sopra indicate. Il vecchio riferimento all’articolo 91 della legge finanziaria del 2024 non stabilisce un’opzione attuale di scambio tramite il PPF.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
