# Elemento di costo dell’addebito aggiuntivo

## Tabella `public.additional_charge_costing_element`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `costing_element`: interno
* `description`: interno
* `charge_type`: interno
* `distribution_method`: interno
* `distribution_type`: interno
* `created_by`: intero
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: booleano
* `deleted_on`: timestamp con fuso orario
* `sub_org_id`: interno
* `charge_count`: intero
* `charge_icon`: interno
* `charge_category`: interno
* `charge_sequence_number`: intero
* `charge_operator`: intero
* `last_modified_by`: interno
* `deleted_by`: interno

### Analisi e descrizione

## Documentazione della tabella: `public.additional_charge_costing_element`

### Introduzione

La tabella `public.additional_charge_costing_element` è progettata per gestire e memorizzare informazioni sui vari elementi di costo per spese aggiuntive all'interno di un'organizzazione. Include dati sul tipo di spese, sul modo in cui vengono ripartite e metadati amministrativi come i dettagli di creazione e modifica. Questa tabella viene probabilmente utilizzata per la gestione finanziaria e operativa di un'organizzazione, con particolare attenzione ai costi aggiuntivi che devono essere monitorati e analizzati.

### Descrizione delle colonne

#### id

* **Significato**: questa colonna memorizza un identificatore univoco per ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa alfanumerica univoca che identifica ogni record di elemento di costo.

#### org\_id

* **Significato**: l'identificatore dell'organizzazione a cui appartiene questo elemento di costo.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un UUID che rappresenta l'organizzazione.

#### costing\_element

* **Significato**: un identificatore o codice dell'elemento di costo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa alfanumerica che rappresenta lo specifico elemento di costo.

#### description

* **Significato**: una descrizione testuale dell'elemento di costo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una breve spiegazione testuale dell'elemento di costo.

#### charge\_type

* **Significato**: il tipo di spesa associato a questo elemento di costo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un codice o un breve testo che indica il tipo di spesa.

#### distribution\_method

* **Significato**: metodo con cui viene ripartita la spesa.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un codice o un breve testo che indica il metodo di ripartizione.

#### distribution\_type

* **Significato**: tipo di ripartizione della spesa.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un codice o un breve testo che indica il tipo di ripartizione.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato il record.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: un intero che rappresenta l'ID utente.

#### created\_on

* **Significato**: timestamp che indica quando è stato creato il record.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica apportata al record.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.

#### is\_deleted

* **Significato**: indica se il record è contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano (`True` o `False`).

#### deleted\_on

* **Significato**: timestamp di quando il record è stato contrassegnato come eliminato.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario oppure `None` se non eliminato.

#### sub\_org\_id

* **Significato**: identificatore di una sotto-organizzazione collegata all'elemento di costo.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un UUID che rappresenta la sotto-organizzazione.

#### charge\_count

* **Significato**: il numero di spese associate all'elemento di costo.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un intero che rappresenta il numero di spese.

#### charge\_icon

* **Significato**: icona o simbolo associato alla spesa.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta l'icona, probabilmente un percorso o un identificatore.

#### charge\_category

* **Significato**: la categoria a cui appartiene la spesa.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta la categoria della spesa.

#### charge\_sequence\_number

* **Significato**: numero di sequenza per ordinare le spese.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un intero utilizzato per mettere in sequenza le spese.

#### charge\_operator

* **Significato**: identificatore dell'operatore responsabile della spesa.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un intero che rappresenta l'ID dell'operatore.

#### last\_modified\_by

* **Significato**: identificatore dell'utente che ha modificato per ultimo il record.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: una stringa che rappresenta l'ID utente, potenzialmente `None` se non è mai stato modificato.

#### deleted\_by

* **Significato**: identificatore dell'utente che ha contrassegnato il record come eliminato.
* **Ruolo**: campo amministrativo.
* **Contenuto tipico**: una stringa che rappresenta l'ID utente, potenzialmente `None` se non eliminato.
