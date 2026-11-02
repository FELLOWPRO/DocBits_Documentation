# Riga dell’ordine di acquisto

## Tabella `public.purchase_order_line`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `purchase_order_id`: interno
* `purchase_order_number`: interno
* `line_number`: interno
* `item_id`: interno
* `supplier_item_id`: interno
* `description`: interno
* `quantity`: double precision
* `unit_code`: interno
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: interno
* `status`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `deleted_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: text
* `sub_org_id`: interno
* `sub_line_number`: interno
* `unit_price_per`: double precision
* `buyer_id`: interno
* `buyer_name`: interno
* `unit_code_price`: interno
* `geo_code`: interno
* `promised_delivery_date`: timestamp con fuso orario
* `delivery_method`: interno
* `requested_ship_date`: date
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Analisi e descrizione

## Documentazione tecnica della tabella `public.purchase_order_line`

### Introduzione

La tabella `public.purchase_order_line` è progettata per memorizzare informazioni dettagliate su ogni riga di un ordine di acquisto. Contiene vari attributi di una riga d'ordine, come i dettagli dell'articolo, le quantità, i prezzi e gli stati. Questa tabella è essenziale per gestire e tracciare gli ordini di acquisto e il relativo stato di evasione in un contesto organizzativo.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni riga dell'ordine di acquisto.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco la riga dell'ordine di acquisto.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata all'ordine di acquisto.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che fa riferimento a un'organizzazione.

#### purchase\_order\_id

* **Significato**: identificatore dell'ordine di acquisto a cui appartiene la riga.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che fa riferimento a un ordine di acquisto.

#### purchase\_order\_number

* **Significato**: il numero assegnato all'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il numero dell'ordine di acquisto.

#### line\_number

* **Significato**: il numero di riga dell'articolo all'interno dell'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che indica la sequenza della riga nell'ordine di acquisto.

#### item\_id

* **Significato**: identificatore dell'articolo ordinato.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa che rappresenta il codice dell'articolo.

#### supplier\_item\_id

* **Significato**: identificatore dell'articolo specifico del fornitore.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa, può essere null se non fornita dal fornitore.

#### description

* **Significato**: descrizione dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una descrizione testuale dell'articolo.

#### quantity

* **Significato**: il numero di unità ordinate.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che indica la quantità ordinata.

#### unit\_code

* **Significato**: codice che rappresenta l'unità di misura dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta le unità, ad es. 'EA' per pezzo.

#### unit\_price

* **Significato**: prezzo per unità dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che rappresenta il prezzo per unità.

#### total\_amount

* **Significato**: importo totale della riga (quantità \* prezzo unitario).
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che rappresenta l'importo totale.

#### currency

* **Significato**: valuta in cui viene effettuato l'acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il codice della valuta, ad es. 'USD'.

#### status

* **Significato**: stato attuale della riga dell'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che indica lo stato, ad es. 'Received', 'Invoiced'.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato la voce.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un intero che rappresenta l'ID dell'utente.

#### created\_on

* **Significato**: timestamp di creazione della voce.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, può essere null se mai modificata.

#### deleted\_on

* **Significato**: timestamp del momento in cui la voce è stata contrassegnata come eliminata.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, può essere null se non eliminata.

#### is\_deleted

* **Significato**: indica se la voce è stata contrassegnata come eliminata.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano (true/false).

#### open\_quantity

* **Significato**: quantità non ancora ricevuta o fatturata.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico, in genere zero se completamente ricevuta.

#### received\_quantity

* **Significato**: quantità che è stata ricevuta.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che indica la quantità ricevuta.

#### confirmed\_quantity

* **Significato**: quantità confermata dal fornitore.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico, può essere null se non confermata.

#### note

* **Significato**: note aggiuntive relative alla riga dell'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: testo, può includere istruzioni speciali o commenti.

#### sub\_org\_id

* **Significato**: identificatore della sottorganizzazione associata alla riga dell'ordine di acquisto.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa, potenzialmente null se non applicabile.

#### sub\_line\_number

* **Significato**: numero di sottoriga all'interno dell'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta la sequenza della sottoriga.

#### unit\_price\_per

* **Significato**: prezzo unitario di base dell'articolo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che rappresenta il prezzo unitario di base.

#### buyer\_id

* **Significato**: identificatore dell'acquirente responsabile dell'acquisto.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa che rappresenta l'ID dell'acquirente.

#### buyer\_name

* **Significato**: nome dell'acquirente responsabile.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il nome dell'acquirente.

#### unit\_code\_price

* **Significato**: codice unità relativo al prezzo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa, simile a unit\_code.

#### geo\_code

* **Significato**: codice geografico per la consegna.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta una località geografica.

#### promised\_delivery\_date

* **Significato**: data promessa per la consegna.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.

#### delivery\_method

* **Significato**: metodo di consegna della riga dell'ordine di acquisto.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il metodo di consegna.

#### requested\_ship\_date

* **Significato**: data richiesta per la spedizione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore di tipo data.

#### received\_base\_mou\_quantity

* **Significato**: quantità ricevuta nelle unità di misura di base.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che indica la quantità ricevuta nell'unità di misura di base (MOU).

#### extended\_amount

* **Significato**: importo esteso della riga.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un valore numerico che rappresenta l'importo esteso, che può essere uguale a total\_amount se non si applicano sconti o addebiti aggiuntivi.
