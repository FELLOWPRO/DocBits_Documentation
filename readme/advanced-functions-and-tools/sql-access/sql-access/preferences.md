# Preferences

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `pref_key`: interno
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.preferences`

## Introduzione
La tabella `public.preferences` è progettata per memorizzare le impostazioni di configurazione e le preferenze di varie entità organizzative all'interno di un sistema. Ogni voce della tabella rappresenta una specifica chiave di preferenza e il relativo valore, associata a un'organizzazione o a una sottorganizzazione. Questi dati di configurazione possono includere impostazioni relative ai numeri di partita IVA, alle impostazioni di estrazione, all'attivazione dei moduli e altro ancora.

## Descrizione delle colonne

### id
- **Significato**: questa colonna memorizza l'identificatore univoco di ogni voce di preferenza.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni riga, ad es. `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Significato**: questa colonna memorizza l'identificatore dell'organizzazione a cui è associata la preferenza.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID corrispondente a un'organizzazione, simile a `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Significato**: questa colonna rappresenta la chiave o il nome dell'impostazione di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe che rappresentano chiavi di configurazione, come `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Significato**: questa colonna contiene il valore della preferenza corrispondente a `pref_key`.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: varia in base a `pref_key`; ad esempio numeri di partita IVA separati da virgole oppure valori booleani come `true` o `false`.

### created_by
- **Significato**: questa colonna indica l'ID dell'utente che ha creato la voce di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un intero che rappresenta l'ID di un utente, ad es. `1`.

### created_on
- **Significato**: questa colonna registra il timestamp di creazione della preferenza.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario, ad es. `2021-11-09 11:04:18+00`.

### last_modified_on
- **Significato**: questa colonna registra il timestamp dell'ultima modifica della preferenza.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica l'ora dell'ultimo aggiornamento, ad es. `2023-12-04 10:10:26+00`.

### deleted_on
- **Significato**: questa colonna riporta il timestamp del momento in cui la preferenza è stata contrassegnata come eliminata.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: in genere `null`, a meno che la riga non sia contrassegnata per l'eliminazione.

### is_deleted
- **Significato**: questa colonna indica se la preferenza è stata contrassegnata come eliminata.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore booleano, in genere `false`.

### user_id
- **Significato**: questa colonna memorizza l'ID dell'utente associato alla preferenza.
- **Ruolo**: campo descrittivo, potenzialmente una chiave esterna.
- **Contenuto tipico**: un intero oppure `null` se non applicabile.

### sub_org_id
- **Significato**: questa colonna identifica la sottorganizzazione associata alla preferenza.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID oppure `null` se non applicabile.

La tabella `public.preferences` offre un modo flessibile e completo per gestire le impostazioni di configurazione delle diverse entità organizzative, garantendo che le preferenze possano essere adattate dinamicamente e tracciate nel tempo.
```
