# Configurazioni di importazione FTP

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `sub_org_id`: interno
* `server_url`: interno
* `username`: interno
* `password`: interno
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `deleted_on`: timestamp con fuso orario
* `port`: integer
* `default_directory`: interno
* `ftp_type`: interno
* `token`: interno
* `file_name_matching_patterns`: interno
* `last_mtime`: interno
* `auth_failed_count`: integer
* `auth_message`: text
* `ignore_certificate`: boolean
* `move_after_import`: boolean
* `destination_directory`: interno
* `import_directory`: interno
* `include_subfolder_content`: boolean

## Analisi e descrizione

```markdown
# Documentazione della tabella FTP Import Configurations

## Introduzione

La tabella `public.ftp_import_configurations` è progettata per memorizzare i dettagli di configurazione dei processi di importazione FTP. Contiene le informazioni necessarie per connettersi ai server FTP, gestire l'autenticazione e controllare le importazioni di file. Supporta i protocolli FTP e SFTP e include campi per i dettagli del server FTP, le credenziali di autenticazione e le impostazioni operative, ad esempio se spostare i file dopo l'importazione e se includere il contenuto delle sottocartelle.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni record di configurazione di importazione FTP.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: formato UUID, ad es. `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Significato**: identificatore dell'organizzazione associata a questa configurazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: formato UUID.

### sub_org_id
- **Significato**: identificatore di una sottorganizzazione, se applicabile.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: formato UUID oppure `null` se non applicabile.

### server_url
- **Significato**: l'URL o l'indirizzo IP del server FTP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: nome di dominio o indirizzo IP, ad es. `sftp.it.doxee.com`.

### username
- **Significato**: nome utente utilizzato per l'autenticazione sul server FTP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: nome utente in chiaro.

### password
- **Significato**: password utilizzata per l'autenticazione sul server FTP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa di password cifrata.

### is_active
- **Significato**: indica se la configurazione è attualmente attiva.
- **Ruolo**: flag di stato.
- **Contenuto tipico**: `True` o `False`.

### created_by
- **Significato**: identificatore dell'utente che ha creato la configurazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: intero che rappresenta l'ID dell'utente.

### created_on
- **Significato**: data e ora di creazione della configurazione.
- **Ruolo**: campo di audit.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario.

### last_modified_on
- **Significato**: data e ora dell'ultima modifica della configurazione.
- **Ruolo**: campo di audit.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario.

### is_deleted
- **Significato**: indica se la configurazione è stata contrassegnata come eliminata.
- **Ruolo**: flag di stato.
- **Contenuto tipico**: `True` o `False`.

### deleted_on
- **Significato**: data e ora in cui la configurazione è stata contrassegnata come eliminata.
- **Ruolo**: campo di audit.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario oppure una data predefinita per i record non eliminati.

### port
- **Significato**: numero di porta utilizzato per connettersi al server FTP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: intero, ad es. `22` per SFTP.

### default_directory
- **Significato**: il percorso della directory predefinita sul server FTP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa con il percorso della directory.

### ftp_type
- **Significato**: tipo di protocollo FTP utilizzato (ad es. FTP, SFTP).
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: `FTP` o `SFTP`.

### token
- **Significato**: token di sicurezza per un'ulteriore autenticazione o identificazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa cifrata o codificata.

### file_name_matching_patterns
- **Significato**: modelli utilizzati per far corrispondere i nomi dei file da importare.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe di modelli oppure `null`.

### last_mtime
- **Significato**: ora dell'ultima modifica dei file, utilizzata per filtrare le importazioni.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa che rappresenta un timestamp oppure `null`.

### auth_failed_count
- **Significato**: contatore dei tentativi di autenticazione falliti.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: intero, ad es. `0` o `5`.

### auth_message
- **Significato**: messaggio che descrive il risultato dell'ultimo tentativo di autenticazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: messaggio di testo oppure `null`.

### ignore_certificate
- **Significato**: indica se la convalida del certificato SSL deve essere ignorata.
- **Ruolo**: flag di stato.
- **Contenuto tipico**: `True` o `False`.

### move_after_import
- **Significato**: indica se i file devono essere spostati al termine dell'importazione.
- **Ruolo**: flag di stato.
- **Contenuto tipico**: `True` o `False`.

### destination_directory
- **Significato**: percorso della directory in cui spostare i file dopo l'importazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa con il percorso della directory oppure `null`.

### import_directory
- **Significato**: percorso della directory da cui vengono importati i file.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa con il percorso della directory oppure `null`.

### include_subfolder_content
- **Significato**: indica se il contenuto delle sottocartelle deve essere incluso nell'importazione.
- **Ruolo**: flag di stato.
- **Contenuto tipico**: `True` o `False`.
```

Questa documentazione offre una comprensione completa di ciascuna colonna della tabella `public.ftp_import_configurations`, spiegandone lo scopo, il ruolo e il contenuto tipico, sulla base dei dati forniti e dei nomi delle colonne.
