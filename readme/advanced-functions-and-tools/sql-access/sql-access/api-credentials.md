# Credenziali API

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `sub_org_id`: interno
* `title`: interno
* `credentials_type`: interno
* `credentials_json`: testo
* `created_by`: intero
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: booleano
* `deleted_on`: timestamp con fuso orario
* `last_modified_by`: interno
* `deleted_by`: interno

## Analisi e descrizione

```markdown
# Documentazione della tabella: `public.api_credentials`

## Introduzione

La tabella `public.api_credentials` è progettata per memorizzare e gestire le informazioni sulle credenziali API. Questa tabella è fondamentale affinché le organizzazioni gestiscano in modo sicuro i propri dati di autenticazione API, garantendo che i vari servizi possano interagire tra loro con le credenziali corrette. Include informazioni sul tipo di credenziali, sull'organizzazione a cui appartengono e metadati relativi alla loro creazione e modifica.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni voce della tabella.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: un identificatore univoco universale (UUID) che rappresenta uno specifico insieme di credenziali API.

### org_id
- **Significato**: identificatore dell'organizzazione proprietaria delle credenziali.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: un UUID che rimanda al record dell'organizzazione in un'altra tabella.

### sub_org_id
- **Significato**: identificatore di una sotto-organizzazione all'interno dell'organizzazione principale.
- **Ruolo**: chiave esterna (facoltativa).
- **Contenuto tipico**: può contenere un UUID che rimanda a una sotto-organizzazione, oppure `None`.

### title
- **Significato**: un titolo descrittivo per le credenziali API.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa come "supplier_auth" che indica lo scopo o l'uso delle credenziali.

### credentials_type
- **Significato**: specifica il tipo di credenziali memorizzate.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa come "ionapi" che indica il formato o il protocollo utilizzato dalle credenziali.

### credentials_json
- **Significato**: un oggetto JSON contenente informazioni dettagliate sulle credenziali.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: una stringa JSON con diverse coppie chiave-valore che descrivono i parametri di autenticazione.

### created_by
- **Significato**: ID utente della persona che ha creato il record delle credenziali.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un intero che rappresenta l'ID utente.

### created_on
- **Significato**: timestamp che indica quando sono state create le credenziali.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore datetime con fuso orario, ad es. `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Significato**: timestamp che indica l'ora dell'ultima modifica delle credenziali.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore datetime con fuso orario, oppure `None` se non sono mai state modificate.

### is_deleted
- **Significato**: flag che indica se le credenziali sono contrassegnate come eliminate.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore booleano, dove `False` indica credenziali attive.

### deleted_on
- **Significato**: timestamp che indica quando le credenziali sono state contrassegnate come eliminate.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore datetime con fuso orario, oppure `None` se non eliminate.

### last_modified_by
- **Significato**: identificatore dell'utente che ha modificato per ultimo le credenziali.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: una stringa di caratteri che rappresenta l'ID dell'utente, oppure `None`.

### deleted_by
- **Significato**: identificatore dell'utente che ha contrassegnato le credenziali come eliminate.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: una stringa di caratteri che rappresenta l'ID dell'utente, oppure `None`.
```
