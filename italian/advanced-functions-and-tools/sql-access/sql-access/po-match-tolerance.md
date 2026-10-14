# PO match tolerance

## Tabella `public.po_match_tolerance`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `item_number`: interno
* `supplier_item_number`: interno
* `description`: interno
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: interno
* `quantity_tolerance_type`: interno

### Analisi e descrizione

## Documentazione tecnica della tabella `public.po_match_tolerance`

### Introduzione

La tabella `public.po_match_tolerance` è progettata per gestire e memorizzare i livelli di tolleranza associati ai processi di abbinamento degli ordini di acquisto (PO matching). Si tratta in genere degli scostamenti ammessi nei prezzi unitari e nelle quantità tra merce ordinata e merce ricevuta. Ogni voce della tabella rappresenta le impostazioni di tolleranza per articoli specifici, contribuendo potenzialmente a garantire coerenza e accuratezza nei processi di approvvigionamento delle organizzazioni.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni voce della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni record di impostazione della tolleranza.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata alle impostazioni di tolleranza.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rimanda all'organizzazione nel sistema.

#### item\_number

* **Significato**: il numero di articolo specifico per il quale sono definite le impostazioni di tolleranza.
* **Ruolo**: identificatore aziendale.
* **Contenuto tipico**: una stringa che rappresenta il codice o il numero dell'articolo nell'inventario dell'organizzazione.

#### supplier\_item\_number

* **Significato**: il numero di articolo fornito dal fornitore.
* **Ruolo**: identificatore aziendale.
* **Contenuto tipico**: una stringa che può essere `None` se non fornita, e rappresenta il codice o il numero dell'articolo del fornitore.

#### description

* **Significato**: una descrizione testuale dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa con i dettagli sull'articolo, che può essere `None`.

#### unit\_price\_tolerance

* **Significato**: la variazione ammessa nel prezzo unitario dell'articolo.
* **Ruolo**: regola aziendale.
* **Contenuto tipico**: un valore numerico che indica la tolleranza percentuale o assoluta nel prezzo unitario.

#### quantity\_tolerance

* **Significato**: la variazione ammessa nella quantità dell'articolo.
* **Ruolo**: regola aziendale.
* **Contenuto tipico**: un valore numerico che indica la tolleranza percentuale o assoluta nella quantità.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato la voce.
* **Ruolo**: campo di audit/registrazione.
* **Contenuto tipico**: un intero che in genere fa riferimento all'ID di un utente nel sistema.

#### created\_on

* **Significato**: il timestamp di creazione della voce.
* **Ruolo**: campo di audit/registrazione.
* **Contenuto tipico**: un valore data/ora con fuso orario che indica la data e l'ora di creazione.

#### last\_modified\_on

* **Significato**: il timestamp dell'ultima modifica della voce.
* **Ruolo**: campo di audit/registrazione.
* **Contenuto tipico**: un valore data/ora con fuso orario che indica quando il record è stato aggiornato per l'ultima volta, che può essere `None` se non modificato.

#### is\_deleted

* **Significato**: indica se la voce è stata eliminata logicamente.
* **Ruolo**: indicatore tecnico/di eliminazione logica (soft delete).
* **Contenuto tipico**: un valore booleano in cui `False` significa attiva e `True` significa eliminata logicamente.

#### unit\_price\_tolerance\_type

* **Significato**: definisce il tipo di tolleranza sul prezzo unitario (ad es. percentuale o valore assoluto).
* **Ruolo**: regola aziendale.
* **Contenuto tipico**: una stringa, spesso 'value', che indica il tipo di misura della tolleranza.

#### quantity\_tolerance\_type

* **Significato**: definisce il tipo di tolleranza sulla quantità (ad es. percentuale o valore assoluto).
* **Ruolo**: regola aziendale.
* **Contenuto tipico**: una stringa, spesso 'value', che indica il tipo di misura della tolleranza.

Questa documentazione offre una panoramica dettagliata di ciascun campo della tabella `public.po_match_tolerance`, fornendo indicazioni sui loro possibili contenuti e ruoli nel contesto della gestione degli ordini di acquisto.
