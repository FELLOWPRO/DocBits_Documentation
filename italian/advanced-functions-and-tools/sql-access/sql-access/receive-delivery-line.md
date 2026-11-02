# Riga di ricevimento della consegna

## Tabella `public.receive_delivery_line`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `receive_delivery_id`: interno
* `delivery_number`: interno
* `line_number`: interno
* `item_id`: interno
* `description`: interno
* `shipped_quantity`: double precision
* `status`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `deleted_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `purchase_order`: interno
* `sequence_number`: interno
* `sub_org_id`: interno
* `shipped_quantity_unit_code`: interno
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: interno
* `received_quantity`: double precision
* `received_quantity_unit_code`: interno
* `purchase_order_line_number`: interno
* `status_effective_from`: timestamp con fuso orario
* `purchase_order_sub_line_number`: interno
* `invoiced_quantity`: double precision
* `invoice_matching_status`: interno
* `open_quantity`: double precision
* `last_modified_by`: interno
* `deleted_by`: interno

### Analisi e descrizione

## Documentazione della tabella: `public.receive_delivery_line`

### Introduzione

La tabella `public.receive_delivery_line` sembra essere un registro dettagliato delle righe di consegna e di ricevimento associate alle operazioni di logistica e di supply chain di un'organizzazione. Ogni riga della tabella rappresenta una specifica riga di una consegna e riporta dettagli quali la descrizione dell'articolo, le quantità spedite e ricevute e vari campi di stato. La tabella è un componente fondamentale per tracciare il movimento delle merci dalla spedizione al ricevimento, compresa la fatturazione e la gestione degli ordini.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni riga di consegna.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: un identificatore univoco universale (UUID).

#### org\_id

* **Significato**: identificatore dell'organizzazione associata alla consegna.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un UUID che rappresenta l'organizzazione.

#### receive\_delivery\_id

* **Significato**: identificatore che rimanda alla transazione di consegna complessiva.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un UUID associato a una specifica transazione di consegna.

#### delivery\_number

* **Significato**: numero univoco assegnato alla consegna.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: una stringa che rappresenta il numero di consegna.

#### line\_number

* **Significato**: numero di riga specifico all'interno di una consegna.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: stringa numerica che indica la sequenza della riga.

#### item\_id

* **Significato**: identificatore dell'articolo spedito.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: una stringa numerica corrispondente a un articolo.

#### description

* **Significato**: descrizione dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: descrizione testuale dell'articolo, ad es. "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Significato**: quantità dell'articolo che è stata spedita.
* **Ruolo**: campo quantitativo.
* **Contenuto tipico**: un numero decimale che indica la quantità spedita.

#### status

* **Significato**: stato attuale della riga di consegna.
* **Ruolo**: campo di stato.
* **Contenuto tipico**: testo come "Received".

#### created\_by

* **Significato**: identificatore dell'utente o del sistema che ha creato il record.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: intero che rappresenta l'ID di un utente.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: data e ora con fuso orario.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: data e ora con fuso orario.

#### deleted\_on

* **Significato**: timestamp del momento in cui il record è stato contrassegnato come eliminato.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: data e ora con fuso orario, spesso null a meno che il record non sia eliminato.

#### is\_deleted

* **Significato**: indica se il record è contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano, true o false.

#### purchase\_order

* **Significato**: riferimento all'ordine di acquisto associato.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: stringa alfanumerica che rappresenta il numero di un ordine di acquisto.

#### sequence\_number

* **Significato**: numero di sequenza della riga di consegna.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: stringa numerica, spesso null.

#### sub\_org\_id

* **Significato**: identificatore di una sottorganizzazione coinvolta.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: UUID, spesso null.

#### shipped\_quantity\_unit\_code

* **Significato**: unità di misura della quantità spedita.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: codice che rappresenta le unità, ad es. "LBP".

#### packing\_slip\_quantity

* **Significato**: quantità secondo la bolla di accompagnamento (packing slip).
* **Ruolo**: campo quantitativo.
* **Contenuto tipico**: numero decimale, spesso null.

#### packing\_slip\_quantity\_unit\_code

* **Significato**: codice dell'unità per la quantità della bolla di accompagnamento.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: codice che rappresenta le unità, spesso null.

#### received\_quantity

* **Significato**: quantità di articoli effettivamente ricevuta.
* **Ruolo**: campo quantitativo.
* **Contenuto tipico**: numero decimale che indica la quantità ricevuta.

#### received\_quantity\_unit\_code

* **Significato**: codice dell'unità per la quantità ricevuta.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: codice che rappresenta le unità, ad es. "LBP".

#### purchase\_order\_line\_number

* **Significato**: numero di riga all'interno dell'ordine di acquisto.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: stringa numerica.

#### status\_effective\_from

* **Significato**: data e ora a partire dalle quali lo stato è effettivo.
* **Ruolo**: campo di stato.
* **Contenuto tipico**: data e ora con fuso orario, spesso null.

#### purchase\_order\_sub\_line\_number

* **Significato**: numero di sottoriga all'interno dell'ordine di acquisto.
* **Ruolo**: campo di riferimento.
* **Contenuto tipico**: stringa numerica, spesso "000".

#### invoiced\_quantity

* **Significato**: quantità che è stata fatturata.
* **Ruolo**: campo quantitativo.
* **Contenuto tipico**: numero decimale.

#### invoice\_matching\_status

* **Significato**: stato del processo di abbinamento della fattura.
* **Ruolo**: campo di stato.
* **Contenuto tipico**: codice di stato testuale, ad es. "9.0".

#### open\_quantity

* **Significato**: quantità che resta aperta o non ancora elaborata.
* **Ruolo**: campo quantitativo.
* **Contenuto tipico**: numero decimale.

#### last\_modified\_by

* **Significato**: identificatore dell'utente che ha modificato per ultimo il record.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: UUID dell'utente, spesso null.

#### deleted\_by

* **Significato**: identificatore dell'utente che ha contrassegnato il record come eliminato.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: UUID dell'utente, spesso null.
