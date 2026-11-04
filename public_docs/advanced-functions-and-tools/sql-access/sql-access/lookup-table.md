# Tabella di ricerca

## Tabella `public.lookup_table`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `data_key`: interno
* `rec_id`: interno
* `prop_name`: interno
* `prop_value`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `prop_value_clean`: interno
* `version`: integer
* `deleted_on`: timestamp con fuso orario
* `sub_org_id`: interno

### Analisi e descrizione

## Documentazione tecnica di `public.lookup_table`

### Introduzione

La tabella `public.lookup_table` è progettata per memorizzare i metadati di varie proprietà associate ai dati organizzativi. Funge probabilmente da archivio chiave-valore per diversi attributi relativi a clienti o ad altre entità all'interno dell'organizzazione. La tabella registra informazioni come i nomi delle proprietà, i valori e il contesto (ad es. l'organizzazione e la sottorganizzazione di appartenenza), insieme a dati di audit come i timestamp di creazione e modifica.

### Descrizione delle colonne

#### `id`

* **Significato**: identificatore univoco di ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni voce.

#### `org_id`

* **Significato**: identificatore dell'organizzazione a cui appartengono i dati.
* **Ruolo**: chiave esterna, probabilmente collegata a una tabella delle organizzazioni.
* **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione.

#### `data_key`

* **Significato**: una chiave che rappresenta un dataset o un contesto specifico all'interno dell'organizzazione.
* **Ruolo**: identificatore contestuale per raggruppare proprietà correlate.
* **Contenuto tipico**: stringa alfanumerica che indica una categoria, ad esempio `customer_amier`.

#### `rec_id`

* **Significato**: identificatore di un record specifico all'interno del dataset.
* **Ruolo**: identificatore contestuale, possibilmente una chiave esterna verso un'altra tabella.
* **Contenuto tipico**: stringa alfanumerica oppure null per i record senza un identificatore specifico.

#### `prop_name`

* **Significato**: nome della proprietà o dell'attributo.
* **Ruolo**: campo descrittivo che indica ciò che rappresenta il valore della proprietà.
* **Contenuto tipico**: stringhe come 'Kundennummer', 'Versandanschrift', 'Kundenname', ecc.

#### `prop_value`

* **Significato**: valore della proprietà descritta da `prop_name`.
* **Ruolo**: campo descrittivo che contiene il dato o il valore effettivo.
* **Contenuto tipico**: stringhe o numeri che rappresentano il valore della proprietà.

#### `created_by`

* **Significato**: identificatore dell'utente o del sistema che ha creato il record.
* **Ruolo**: campo tecnico a fini di audit.
* **Contenuto tipico**: intero che rappresenta l'ID di un utente.

#### `created_on`

* **Significato**: timestamp che indica quando il record è stato creato.
* **Ruolo**: campo tecnico a fini di audit.
* **Contenuto tipico**: data e ora con informazioni sul fuso orario.

#### `last_modified_on`

* **Significato**: timestamp che indica l'ultima volta in cui il record è stato modificato.
* **Ruolo**: campo tecnico a fini di audit.
* **Contenuto tipico**: data e ora con informazioni sul fuso orario, potenzialmente null se non modificato.

#### `is_deleted`

* **Significato**: flag che indica se il record è eliminato.
* **Ruolo**: campo tecnico che indica l'eliminazione logica.
* **Contenuto tipico**: valore booleano (`True` o `False`).

#### `prop_value_clean`

* **Significato**: versione pulita o elaborata di `prop_value`.
* **Ruolo**: campo descrittivo per memorizzare un valore normalizzato o standardizzato.
* **Contenuto tipico**: simile a `prop_value`, potenzialmente null se non applicabile.

#### `version`

* **Significato**: numero di versione del record.
* **Ruolo**: campo tecnico per il controllo delle versioni.
* **Contenuto tipico**: intero che rappresenta la versione del record.

#### `deleted_on`

* **Significato**: timestamp che indica quando il record è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico a fini di audit.
* **Contenuto tipico**: data e ora con informazioni sul fuso orario, potenzialmente null se non eliminato.

#### `sub_org_id`

* **Significato**: identificatore di una sottorganizzazione all'interno dell'organizzazione principale.
* **Ruolo**: chiave esterna, potenzialmente collegata a una tabella delle sottorganizzazioni.
* **Contenuto tipico**: una stringa UUID che rappresenta la sottorganizzazione, potenzialmente null se non applicabile.
