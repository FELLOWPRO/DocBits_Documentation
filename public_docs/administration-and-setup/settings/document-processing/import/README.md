# Importazione

## Panoramica

Per creare una connessione è necessario un account amministratore. Usa **Import** per configurare l'importazione automatica dei documenti da un server FTP/SFTP, da una casella di posta collegata o dall'indirizzo e-mail in entrata di DocBits. Verifica l'organizzazione e l'ambiente correnti prima di inserire i dettagli della connessione.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-it-20261109.png" alt="Pagina delle impostazioni di importazione con il diagramma Import Pipeline, l'elenco FTP Import con un pulsante New e l'elenco Email Import con un pulsante New"><figcaption><p>La pagina Import: il diagramma Import Pipeline in sola lettura, l'elenco FTP Import e l'elenco Email Import, ciascuno con il proprio pulsante <strong>New</strong>.</p></figcaption></figure>

## Come accedere

1. Vai a **Settings** → **Document Processing** → **Import**.
2. Espandi la sezione richiesta. **FTP Import** e **Email Import** hanno ciascuna il proprio pulsante **New**.

## **Document Settings**

La pagina Import corrente contiene **Import Pipeline**, **FTP Import**, **Email Import** e, se attivata, **Inbound Emails**. I campi per il ritaglio delle pagine, per i termini di pagamento predefiniti e per i modelli di data non sono controlli in questa vista Import.

**Import Pipeline** mostra la topologia di instradamento FTP/SFTP, comprese le regioni di origine e di destinazione. Controlla qualsiasi avviso visualizzato prima di modificare una connessione. La scheda della pipeline **Email** mostra attualmente un messaggio di prossima disponibilità; non visualizza alcun diagramma di elaborazione delle e-mail.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tabella FTP Import con il pulsante New e le colonne per tipo, server, nome utente, porta, sotto-organizzazione e directory"><figcaption><p>Usa New in FTP Import per aggiungere una connessione a un server. In questo esempio le righe delle connessioni esistenti sono oscurate.</p></figcaption></figure>

### Requisiti

* Un server FTP, FTPS o SFTP raggiungibile dal servizio di importazione.
* L'indirizzo del server, il protocollo, la porta, il nome utente e la password forniti dall'amministratore.
* Una directory di importazione e, se è richiesta l'archiviazione, una directory di archivio approvata.

### Aggiungere una nuova connessione

1. Fai clic su **New** in **FTP Import**.
2. Inserisci le impostazioni della connessione. Un nuovo modulo parte con **SFTP** e porta **22**; sostituisci questi valori quando il tuo server usa un altro protocollo o un'altra porta.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Nuovo modulo di connessione FTP con SFTP, porta 22, campi delle directory, impostazioni dei tentativi e Save e Cancel"><figcaption><p>Inserisci i dettagli del server e di accesso, poi controlla directory, instradamento e impostazioni dei tentativi. I campi Password e chiave API sono oscurati; questo esempio non è stato salvato.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** e **Password** identificano e autenticano la connessione al server.
* **Primary Directory** imposta la directory di base. **Import Directory** seleziona la cartella da elaborare; la selezione della cartella diventa disponibile dopo il salvataggio della connessione.
* **Document Type** e **Sub-Organizations** controllano l'assegnazione. **File name matching patterns** limita i nomi di file considerati.
* **Archive after Import** abilita lo spostamento dei file elaborati nella directory di archivio specificata. **Include Subfolder Files** estende l'elaborazione alle sottocartelle.
* **Retry interval (min)**, **Retry duration (hours)** e **Notification emails (comma-separated)** controllano il comportamento dei tentativi e delle notifiche. I valori predefiniti illustrati sono 60 minuti e 48 ore.
* **API Key** usa la chiave di abbonamento all'app esistente dell'organizzazione. L'icona a forma di occhio mostra o nasconde quella chiave; l'icona di copia la copia negli appunti. Questi controlli non creano una nuova chiave. Mantienila riservata; non inserirla in screenshot o messaggi di assistenza.

Usa **Cancel** o l'icona di chiusura per uscire da un nuovo modulo di connessione senza salvarlo.

3. Controlla i valori e fai clic su **Save** quando la connessione è pronta per essere creata.
4. Nel menu **Actions** della riga salvata, scegli **Activate** quando le importazioni sono autorizzate a essere eseguite.

### Azioni per FTP

Il menu **Actions** della connessione salvata offre:

* **Test Connection**: contatta il server configurato per verificare la connessione.
* **Connection Logs**: esamina i tentativi di connessione e gli errori.
* **Activate/Deactivate**: attiva o interrompe l'elaborazione automatica per questa connessione.
* **Edit**: modifica la sua configurazione.
* **Delete**: rimuove la connessione.

Il test, l'attivazione, la modifica e l'eliminazione agiscono su una connessione reale. Verifica la riga e l'organizzazione selezionate prima di usarli.

## **Email Import**

Una casella di posta collegata è distinta dall'indirizzo e-mail in entrata di DocBits descritto nel tutorial seguente. Scegli il metodo adatto al tuo processo.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tabella Email Import con New, l'icona del registro di importazione e le colonne di configurazione della casella"><figcaption><p>Usa New per una connessione a una casella di posta oppure l'icona del registro per esaminare le importazioni. Le righe delle connessioni esistenti e il link informativo sono oscurati.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: vengono importati solo i documenti con i seguenti tipi di file:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Come vengono riconosciuti gli allegati**

Oltre alle estensioni di file elencate sopra, DocBits identifica un documento anche dal suo **contenuto effettivo del file** (firma del file), non solo dal tipo di contenuto dichiarato dal sistema di posta mittente. Questo è rilevante per le e-mail **inoltrate**: i server di posta e i gateway intermedi rietichettano spesso un allegato con un tipo generico (`application/octet-stream`) invece che, ad esempio, `application/pdf` o `application/xml`. DocBits riconosce e importa comunque correttamente questi allegati.

* I messaggi `.eml` **inoltrati** e gli allegati Outlook **`winmail.dat`** (TNEF) vengono scompattati e i documenti in essi contenuti vengono importati.
* **Codifica XML:** quando una fattura XML viene rietichettata con un tipo generico (`application/octet-stream`), DocBits la riconosce dalla sua dichiarazione `<?xml`, tollerando un byte-order mark (BOM) iniziale **UTF-8** o **UTF-16** (LE/BE) — attualmente solo queste codifiche BOM vengono rilevate automaticamente dal contenuto. Un allegato che mantiene un nome di file `.xml` viene importato indipendentemente dalla sua codifica.
* **Ignorati:** le immagini inline che accompagnano un'e-mail (loghi di firma / immagini incorporate — PNG, JPG, GIF, BMP) vengono saltate silenziosamente e **non** vengono conteggiate come importazioni non riuscite.

Se un allegato non può essere importato e l'opzione **“Reply to this email if import can not be done”** è attivata per l'indirizzo in entrata, viene notificato l'indirizzo di risposta configurato.
{% endhint %}

### Aggiungere una nuova connessione IMAP

1. Fai clic su **New** in **Email Import** e seleziona **IMAP** sotto **Protocol**.
2. In **Email Server Setup**, inserisci il nome del server, la porta, la cifratura, il nome utente, l'indirizzo e-mail e la password. Usa i valori richiesti dal tuo provider di posta; il valore 993 visualizzato è un esempio di porta, non un'impostazione completata.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="IMAP Email Server Setup con protocollo, server, porta, cifratura, credenziali dell'account e Next"><figcaption><p>Completa i campi richiesti del server e dell'account prima di Next. L'area della password è oscurata; in questo esempio non è stata inviata alcuna credenziale della casella di posta.</p></figcaption></figure>

L'icona di copia accanto a **Password** copia la password inserita negli appunti. **Cancel** o l'icona di chiusura abbandona questa procedura guidata di nuova connessione senza salvarla.

3. Fai clic su **Next** per aprire **Options**. Scegli se **Merge attached documents** o **Block duplicate filename import**. **Email Notification** abilita un'e-mail di conferma dopo l'importazione; attivala solo quando questo comportamento è desiderato.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="Passaggio IMAP Options con unione degli allegati, filtro dei nomi di file duplicati, notifica e-mail, Back e Next"><figcaption><p>Options separa il comportamento di importazione dalla notifica e-mail. In questo esempio non salvato entrambe le caselle di controllo e l'interruttore di notifica sono disattivati.</p></figcaption></figure>

4. Fai clic su **Next** per aprire **Config**. Seleziona le **Sub-Organizations** richieste, controlla la **API Key** esistente, imposta il destinatario per gli errori di importazione e verifica **Document Routing**. Espandi **Advanced Settings** solo quando il processo richiede opzioni aggiuntive.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="Passaggio IMAP Config con organizzazione, chiave API oscurata, notifiche di errore, instradamento dei documenti, Advanced Settings e Save"><figcaption><p>Config riunisce l'assegnazione dell'organizzazione, la chiave esistente, le notifiche di errore e l'instradamento. La chiave è oscurata e Save non è stato usato.</p></figcaption></figure>

In **Config**, l'icona a forma di occhio mostra o nasconde la **API Key** esistente e **Copy** la copia negli appunti. Nessuno dei due controlli genera una nuova chiave.

5. Fai clic su **Save** quando la configurazione è pronta. Poi usa **Activate** nel menu **Actions** della connessione salvata per avviare l'elaborazione automatica.

Per una connessione IMAP salvata, **Edit** offre opzioni per la cartella e per la gestione successiva all'importazione. Seleziona la cartella di origine e la cartella di destinazione per le e-mail spostate solo dopo che la connessione è stata creata e le cartelle disponibili possono essere caricate.

### Azioni per IMAP

Il menu **Actions** della connessione salvata offre **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** e **Delete**. Il test della connessione contatta la casella di posta configurata; l'attivazione abilita l'elaborazione. Esamina i registri prima di ripetere un'importazione non riuscita.

### Aggiungere una nuova connessione OAuth Office365

1. Fai clic su **New** in **Email Import** e seleziona **OAuth Office365** sotto **Protocol**. Per un'applicazione tenant gestita dall'amministratore, seleziona **OAuth Office365 - Tenant** e segui [O365 Tenant](o365-tenant.md).
2. Controlla **Document Routing** prima dell'autenticazione.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="Configurazione OAuth Office365 con Document Routing e il pulsante Authenticate prima dell'autenticazione Microsoft"><figcaption><p>Seleziona la route prima di Authenticate. Questa vista è precedente all'accesso; non è stata avviata alcuna autenticazione Microsoft.</p></figcaption></figure>

3. Fai clic su **Authenticate** quando la connessione alla casella di posta è autorizzata. Completa l'accesso con codice dispositivo Microsoft usando il codice mostrato da DocBits, poi torna e seleziona **Finish Authentication**.
4. Dopo l'autenticazione, controlla l'organizzazione, la cartella, la casella condivisa, la cartella di spostamento e le opzioni di notifica degli errori offerte per la connessione. Usa **Next** per continuare verso **Config** quando diventa disponibile, poi salva le impostazioni desiderate.
5. Attiva la connessione salvata quando le importazioni automatiche devono essere eseguite. **Import**, dove offerto per una connessione salvata, avvia un'importazione reale; usalo con consapevolezza.

### Azioni per OAuth Office365

Il menu **Actions** della connessione salvata offre **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** e **Delete**. La disattivazione interrompe l'elaborazione automatica; l'eliminazione rimuove la configurazione.

### Import Log

Usa l'icona del registro in alto a destra in **Email Import** per esaminare le importazioni di tutte le connessioni configurate alla casella di posta. Usa l'azione **Import Log** di una riga salvata per quella connessione. Controlla oggetto, mittente, stato e dettagli degli errori disponibili prima di decidere se ripetere l'importazione.

## Inbound Emails

I due screenshot del tutorial riportati sotto mostrano l'indirizzo in entrata di DocBits e i suoi registri. Questo è distinto dalle connessioni alla casella di posta descritte sopra.

* Usa l'icona di copia accanto a **E-Mail** per copiare l'indirizzo di ricezione visualizzato per l'organizzazione e l'ambiente correnti.
* **Add** inserisce un'altra riga di mittente consentito nel modulo. Scegli il suo mittente e l'eventuale sotto-organizzazione desiderata, poi usa **Save** per rendere permanente la configurazione. Aggiungere una riga da sola non la salva.
* **Logs** apre il registro delle e-mail in entrata. **Errors** filtra gli errori; **Inbound** e **Outbound** selezionano la direzione del messaggio.
* Espandi una riga del registro con il suo chevron per controllare i dettagli degli allegati. L'icona di copia accanto all'ID di tracciamento copia quell'ID per la risoluzione dei problemi. **Original email**, quando disponibile per una riga in entrata, scarica il messaggio originale selezionato come file `.eml`; non ripete l'importazione.

## Video tutorial: Casella di posta e ricerca errori

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/it.mp4" %}
Casella di posta e ricerca errori
{% endembed %}

[Guarda con sottotitoli e capitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/it.html)

Alcune etichette native del prodotto possono rimanere in un'altra lingua. Gli ID tecnici dei campi sono conservati.

In impostazioni e importazione, in questo esempio utilizzo l'indirizzo in entrata di DocBits. Una casella di posta collegata direttamente è un metodo di importazione separato. Per questa formazione lavoro in un'organizzazione demo dedicata con fatture sintetiche. Le notifiche restano disattivate.

Per prima cosa controllo l'indirizzo di ricezione visualizzato e l'ambito. L'indirizzo appartiene esattamente a questa organizzazione e al suo ambiente. Per un'altra azienda o un ambiente di produzione, uso sempre l'indirizzo effettivamente visualizzato lì.

Qui limito la casella al nostro mittente di test approvato. Seleziono l'assegnazione a una sotto-organizzazione solo se appartiene al processo previsto. Salvo l'impostazione e la riapro. Il mittente consentito è stato mantenuto; le e-mail di risposta automatica restano disattivate in questa formazione.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Mittente consentito salvato con le notifiche disattivate"><figcaption><p>Mittente consentito salvato con le notifiche disattivate</p></figcaption></figure>

Per questa formazione, un messaggio di test è stato inviato direttamente all'elaborazione in entrata di DocBits. Questo test non conferma la consegna di e-mail esterne. Nel registro controllo oggetto, mittente e allegato importato corrispondenti. Poi controllo il documento effettivamente creato.

Apro il documento corrispondente e confronto l'allegato PDF con la fattura in DocBits. Nome del file, numero di fattura, fornitore e importo devono corrispondere. Un'importazione riuscita non dice nulla su un'approvazione o su una registrazione ERP.

Un secondo test controllato proviene da un mittente non approvato. Nel registro cerco specificamente questo ingresso in entrata e attivo il filtro degli errori. I dettagli indicano il mittente rifiutato. Controllo la causa usando l'oggetto e l'ID di tracciamento, invece di avviare più volte l'importazione.

In un caso reale, chiarisco prima se questo mittente è persino autorizzato. Una modifica approvata all'elenco dei mittenti viene salvata e controllata di nuovo. Successivamente verifico un nuovo ingresso di test univoco fino al documento creato. Per gli errori tecnici, consegno l'ID di tracciamento e il messaggio di errore concreto.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Importazione non riuscita con allegato, motivo e traccia"><figcaption><p>Importazione non riuscita con allegato, motivo e traccia</p></figcaption></figure>
