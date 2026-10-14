# Auto accounting

## Tabella `public.auto_accounting`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `supplier_name`: nome del fornitore
* `description`: interno
* `item_number`: interno
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: interno
* `doc_id`: interno

### Analisi e descrizione

## Documentazione tecnica della tabella `public.auto_accounting`

### Introduzione

La tabella `public.auto_accounting` è progettata per gestire e memorizzare i dati contabili relativi a vari fornitori e organizzazioni. La tabella raccoglie informazioni sulle transazioni finanziarie, compresi importi e conti di contabilità generale, essenziali per la rendicontazione e l'analisi finanziaria.

### Descrizione delle colonne

#### id

* **Significato**: un identificatore univoco per ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che rappresenta in modo univoco ogni voce.
* **Nota**: garantisce che ogni record possa essere identificato in modo distinto.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata alla registrazione contabile.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rimanda a un'organizzazione in una tabella padre.
* **Nota**: serve ad associare le registrazioni contabili a specifiche organizzazioni.

#### supplier\_name

* **Significato**: il nome del fornitore coinvolto nella transazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: testo che rappresenta il nome del fornitore, ad esempio "Fellow Consulting AG".
* **Nota**: fornisce informazioni sul fornitore collegato alla transazione.

#### description

* **Significato**: una breve descrizione della transazione o dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: testo che descrive la transazione, ad esempio il nome di un articolo ("apple" o "Peaches").
* **Nota**: utile per comprendere la natura della transazione.

#### item\_number

* **Significato**: identificatore di uno specifico articolo coinvolto nella transazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: potrebbe essere un identificatore di prodotto o SKU, anche se non sono forniti dati di esempio.
* **Nota**: utile per tracciare o referenziare articoli specifici.

#### line\_amount

* **Significato**: l'importo monetario di una specifica riga della transazione.
* **Ruolo**: campo finanziario.
* **Contenuto tipico**: un valore decimale che rappresenta l'importo di una singola riga.
* **Nota**: importante per l'analisi finanziaria dettagliata a livello di riga.

#### total\_amount

* **Significato**: l'importo monetario totale della transazione.
* **Ruolo**: campo finanziario.
* **Contenuto tipico**: un valore decimale che rappresenta l'importo totale della transazione.
* **Nota**: rappresenta la somma di tutti gli importi di riga di una transazione.

#### mapped\_amount

* **Significato**: l'importo che è stato assegnato o mappato a uno specifico conto.
* **Ruolo**: campo finanziario.
* **Contenuto tipico**: un valore decimale che indica quanta parte della transazione è stata assegnata.
* **Nota**: utile per capire come i fondi sono distribuiti tra i conti.

#### ledger\_account

* **Significato**: il numero del conto di contabilità generale su cui è registrata la transazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: testo che rappresenta un numero di conto, ad esempio "2200" o "2500".
* **Nota**: fondamentale ai fini contabili per tracciare dove vengono registrate le transazioni.

#### doc\_id

* **Significato**: un identificatore di un documento o record correlato.
* **Ruolo**: chiave esterna o riferimento.
* **Contenuto tipico**: una stringa UUID o un altro identificatore che rimanda a documenti correlati.
* **Nota**: aiuta ad associare le transazioni a documenti o record specifici per garantirne la tracciabilità.

Questa documentazione offre una panoramica dettagliata della tabella `public.auto_accounting`, descrivendone la struttura e lo scopo di ciascuna colonna, per aiutare sviluppatori e amministratori di database a comprendere e utilizzare i dati in modo efficace.
