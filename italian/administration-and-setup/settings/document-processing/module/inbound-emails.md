# Email in entrata

### Panoramica

DocBits può acquisire i documenti direttamente dall'e-mail, senza caricamento manuale. Esistono **due modi** per importare documenti via e-mail, entrambi in **Impostazioni → Elaborazione documenti → Importazione**:

| Metodo | Come funziona | Ideale per |
|--------|---------------|------------|
| **Account di importazione e-mail** | DocBits si connette a una casella di posta di tua proprietà (**IMAP**, **OAuth Office365** o **OAuth Office365 – Tenant**) e importa i documenti che vi trova. | Una casella dedicata che riceve già i tuoi documenti (es. `fatture@tuaazienda.com`). |
| **E-mail inoltrate (Email in entrata)** | DocBits ti fornisce un indirizzo univoco; qualsiasi mittente autorizzato può **inoltrare** documenti ad esso. | L'inoltro occasionale da molti mittenti senza condividere le credenziali della casella. |

Puoi usare ciascun metodo singolarmente o entrambi insieme.

### Metodo 1 — Connettere una casella di posta (Importazione e-mail)

Vai su **Impostazioni → Elaborazione documenti → Importazione** e apri la sezione **Importazione e-mail**. Fai clic su **Nuovo** per aggiungere una connessione a una casella.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Sezione Importazione e-mail con il pulsante Nuovo"><figcaption><p>Nella sezione Importazione e-mail, fai clic su <strong>Nuovo</strong> per connettere una casella di posta.</p></figcaption></figure>

Si apre la procedura guidata di configurazione. Il primo campo, **Protocollo**, determina come DocBits si connette — scegli **IMAP**, **OAuth Office365** o **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Menu a discesa Protocollo con IMAP, OAuth Office365 e OAuth Office365 - Tenant"><figcaption><p>Il menu <strong>Protocollo</strong> offre i tre tipi di connessione.</p></figcaption></figure>

#### IMAP

Per una casella standard, scegli **IMAP** e inserisci i dati del server e le credenziali dell'account:

* **Nome server** e **Porta** (predefinita `993`) del tuo server di posta.
* **Crittografia** — `SSL`, `TLS` o `None`.
* **Nome utente**, **e-mail** e **password** della casella.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="Modulo di connessione IMAP con server, porta, crittografia e credenziali"><figcaption><p>Il modulo IMAP: la connessione al server di posta più le credenziali della casella.</p></figcaption></figure>

#### OAuth Office365

Per una singola casella utente Microsoft 365, scegli **OAuth Office365**. Invece di una password, autorizzi DocBits tramite Microsoft: scegli la destinazione dell'**Instradamento documenti**, quindi fai clic su **Autentica** e completa l'accesso Microsoft.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="Modulo OAuth Office365 con Instradamento documenti e un pulsante Autentica"><figcaption><p>OAuth Office365 si connette tramite l'accesso Microsoft — in DocBits non viene memorizzata alcuna password.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Per connetterti a livello di tenant (organizzazione) tramite una registrazione di app Azure, scegli **OAuth Office365 – Tenant** e inserisci le credenziali Azure: **ID tenant** (Tenant ID), **ID app client** (Client App ID) e **Valore app client** (segreto client). Usa **Prova connessione** per verificare, quindi **Salva**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Configurazione del tenant Azure con ID tenant, ID app client e Valore app client"><figcaption><p>OAuth Office365 – Tenant usa una registrazione di app Azure (ID tenant, ID app client, segreto client).</p></figcaption></figure>

{% hint style="info" %}
L'**Instradamento documenti** decide dove vanno i documenti importati — **DocBits** (la dashboard standard) o **AI Workforce**. Dopo la connessione, i passaggi successivi della procedura guidata ti permettono di scegliere da quale **cartella** importare, una **casella condivisa** facoltativa e se **spostare** le e-mail elaborate in un'altra cartella.
{% endhint %}

### Metodo 2 — Inoltrare e-mail a DocBits (Email in entrata)

Questo metodo richiede prima l'attivazione del modulo **Email in entrata**. Vai su **Impostazioni → Elaborazione documenti → Modulo**, apri la sezione **Tipo di documento**, trova **Email in entrata** e attiva l'interruttore.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Attivazione del modulo Email in entrata"><figcaption><p>Attiva <strong>Email in entrata</strong> in Impostazioni → Elaborazione documenti → Modulo.</p></figcaption></figure>

Una volta attivato, nella sezione **Impostazioni → Elaborazione documenti → Importazione** compare una sezione **Email in entrata**. Contiene tutto il necessario per ricevere documenti inoltrati:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Sezione Email in entrata: indirizzo di importazione, mittenti predefiniti e indirizzo per la notifica di errore"><figcaption><p>La sezione Email in entrata: il tuo indirizzo di importazione, l'elenco dei mittenti predefiniti e l'indirizzo per le notifiche di errore.</p></figcaption></figure>

* **Indirizzo di importazione** — un indirizzo univoco generato dal sistema nel formato `org_id@environment.inbound.docbits.com`. Inoltra o invia documenti a questo indirizzo e DocBits li importa automaticamente. Usa l'icona di copia per ottenerlo.
* **Importa documenti solo da e-mail predefinite** — quando è attivo, vengono accettati solo gli indirizzi dei mittenti elencati qui; le e-mail di chiunque altro vengono ignorate. Per ogni mittente puoi scegliere una **Sotto-organizzazione** (lascia vuoto per assegnarlo all'organizzazione principale). Usa **Aggiungi** per elencare altri mittenti e **Elimina** per rimuoverne uno.
* **Rispondi a questa e-mail se l'importazione non è possibile** — quando è attivo, inserisci un indirizzo da notificare ogni volta che un tentativo di importazione fallisce, così i problemi non passano inosservati.

Fai clic su **Salva** per applicare le modifiche.

{% hint style="info" %}
**Quali allegati vengono importati?** DocBits importa gli allegati di documenti supportati — consulta [Importazione → Importazione e-mail](../import/README.md#email-import) per l'elenco completo dei tipi di file — e decomprime le e-mail `.eml` inoltrate e gli allegati Outlook `winmail.dat` (TNEF) per importare i documenti che contengono. Il riconoscimento si basa anche sul **contenuto effettivo del file**, quindi gli allegati a cui un server di posta di inoltro riassegna un tipo generico (`application/octet-stream`) vengono comunque importati correttamente. Le immagini in linea (loghi della firma / grafica incorporata) vengono ignorate.
{% endhint %}

### Quale metodo scegliere

* **Usa un account di importazione e-mail** quando i documenti arrivano già in una casella dedicata e vuoi che DocBits li recuperi da solo — IMAP per server di posta generici, OAuth Office365 per Microsoft 365.
* **Usa le e-mail inoltrate** quando le persone devono inoltrare documenti all'occorrenza, o quando non vuoi condividere le credenziali della casella con DocBits.
* **Combina entrambi** se alcuni documenti arrivano in una casella fissa mentre altri vengono inoltrati occasionalmente.

{% hint style="info" %}
Limitare i mittenti (Metodo 2) e scegliere la destinazione corretta dell'**Instradamento documenti** (Metodo 1) sono i due modi più comuni per mantenere pulita una pipeline in entrata — solo i documenti che ti aspetti, indirizzati dove desideri.
{% endhint %}
