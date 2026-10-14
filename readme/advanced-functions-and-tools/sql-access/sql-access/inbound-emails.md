# Inbound Emails

## Tabella `public.inbound_emails`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `is_active`: boolean
* `email_senders`: interno
* `email_receiver`: interno
* `token`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: interno
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: interno
* `deleted_on`: timestamp with time zone

### Analisi e descrizione

## Documentazione tecnica: tabella `public.inbound_emails`

### Introduzione

La tabella `public.inbound_emails` è progettata per memorizzare e gestire le informazioni sulle e-mail ricevute da un'organizzazione. Tiene traccia dei dettagli di mittente e destinatario, dello stato dell'e-mail e di vari metadati relativi alla creazione, alla modifica e all'eliminazione dei record. Sembra far parte di un sistema di gestione delle e-mail all'interno di un'organizzazione, probabilmente utilizzato per tracciare le comunicazioni e-mail in entrata.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa univoca, probabilmente un UUID, ad es. `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata all'e-mail in entrata.
* **Ruolo**: chiave esterna, collegata a un'altra tabella che contiene i dettagli dell'organizzazione.
* **Contenuto tipico**: una stringa univoca, probabilmente un UUID, ad es. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Significato**: indica se il record dell'e-mail è attualmente attivo.
* **Ruolo**: indicatore di stato.
* **Contenuto tipico**: un valore booleano, `True` o `False`.

#### email\_senders

* **Significato**: memorizza le informazioni sui mittenti dell'e-mail.
* **Ruolo**: campo dati.
* **Contenuto tipico**: una stringa in stile JSON con i dettagli dei mittenti, ad es. `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Significato**: indirizzo e-mail del destinatario principale.
* **Ruolo**: campo dati.
* **Contenuto tipico**: una stringa con un indirizzo e-mail. Nell'esempio è vuota, il che suggerisce un utilizzo facoltativo o variabile.

#### token

* **Significato**: un token associato all'e-mail, possibilmente per l'autenticazione o l'identificazione.
* **Ruolo**: campo di autenticazione o tracciamento.
* **Contenuto tipico**: una stringa lunga generata in modo casuale.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato il record.
* **Ruolo**: chiave esterna, collegata a una tabella di utenti o dipendenti.
* **Contenuto tipico**: un intero che rappresenta l'ID di un utente, ad es. `1`.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo di metadati.
* **Contenuto tipico**: un valore data/ora con informazioni sul fuso orario, ad es. `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Significato**: identificatore dell'utente che ha modificato per ultimo il record.
* **Ruolo**: chiave esterna, collegata a una tabella di utenti o dipendenti.
* **Contenuto tipico**: può essere l'ID di un utente oppure null se non sono state effettuate modifiche.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica del record.
* **Ruolo**: campo di metadati.
* **Contenuto tipico**: un valore data/ora che indica l'ultima modifica, ad es. `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Significato**: indica se il record dell'e-mail è stato contrassegnato come eliminato.
* **Ruolo**: indicatore di stato.
* **Contenuto tipico**: un valore booleano, `True` o `False`.

#### deleted\_by

* **Significato**: identificatore dell'utente che ha contrassegnato il record come eliminato.
* **Ruolo**: chiave esterna, collegata a una tabella di utenti o dipendenti.
* **Contenuto tipico**: può essere l'ID di un utente oppure null se il record non è eliminato.

#### deleted\_on

* **Significato**: timestamp del momento in cui il record è stato contrassegnato come eliminato.
* **Ruolo**: campo di metadati.
* **Contenuto tipico**: un valore data/ora che indica il momento dell'eliminazione, oppure una data predefinita se non applicabile, ad es. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
