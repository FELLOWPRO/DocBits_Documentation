---
description: Hash delle password, archiviazione delle chiavi API, TLS, accesso alle credenziali e recupero degli account in DocBits.
---

# Archiviazione sicura delle credenziali

DocBits gestisce le password di accesso, le chiavi API DocBits, le informazioni degli account e le credenziali dei sistemi collegati in base al loro scopo. Questa pagina descrive la protezione e le modalità di recupero dell'accesso per ciascuna categoria.

## Password di accesso

DocBits memorizza le password di accesso come **hash unidirezionali con salt**. L'autenticazione verifica la password inserita rispetto all'hash memorizzato. La password originale non viene conservata in una forma che consenta di decifrarla e recuperarla.

Gli amministratori e il supporto DocBits non possono quindi recuperare la password esistente in chiaro dall'hash memorizzato. Se un utente dimentica la password, deve reimpostarla per tornare ad accedere tramite password.

### Reimpostazione della password

1. Selezionare **Ha dimenticato la password?** nella schermata di accesso.
2. Inserire l'indirizzo email associato all'account.
3. Aprire il link di reimpostazione inviato a quell'indirizzo.
4. Impostare una nuova password e utilizzarla per accedere.

I link di reimpostazione hanno una scadenza. Se un link è scaduto, richiederne uno nuovo. La procedura imposta una nuova password e non rivela quella precedente. Per le istruzioni complete, consultare [Ottenere l'accesso ed effettuare il login](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

Gli account con SSO o passkey configurati possono utilizzare quel metodo di accesso alternativo. Con SSO, il recupero della password è gestito dal provider di identità. Vedere [Autenticazione a due fattori](two-factor-authentication.md).

## Chiavi API DocBits

Le chiavi create tramite la **Gestione delle chiavi API** vengono mostrate per intero una sola volta, al momento della creazione. DocBits memorizza un hash unidirezionale della chiave e un breve prefisso identificativo. Il prefisso e i metadati rimangono visibili nell'elenco di gestione; la chiave originale completa non può essere recuperata dal suo hash.

Né gli amministratori né il supporto DocBits possono consultare la chiave completa dopo la creazione. Se una chiave viene persa, revocarla e crearne una sostitutiva. Ogni chiave può avere una data di scadenza ed essere revocata separatamente. Vedere [Gestione delle chiavi API](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Dati degli account e credenziali dei sistemi collegati

Nomi, indirizzi email, ruoli e stato degli account sono informazioni che gli amministratori autorizzati dell'organizzazione possono consultare e gestire. Sono distinte dal segreto utilizzato per l'autenticazione. Vedere [Utenti](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Le credenziali fornite per i sistemi collegati, come un account di servizio ERP, una casella email o un server SFTP, sono anch'esse distinte da una password DocBits o da una chiave API emessa da DocBits. Un connettore può aver bisogno del segreto utilizzabile per autenticarsi al sistema esterno. L'archiviazione e i controlli di accesso devono quindi essere valutati per ciascun connettore.

L'impossibilità di recuperare una password o una chiave API DocBits memorizzata come hash **non** significa che tutte le informazioni degli account o tutti i segreti di integrazione siano inaccessibili al fornitore. Qualsiasi garanzia sull'accesso del personale alle credenziali di integrazione richiede la conferma dei relativi controlli operativi di accesso.

## Crittografia dei dati in transito

Gli endpoint pubblici DocBits elencati di seguito supportano **TLS 1.2 e TLS 1.3** tramite HTTPS. Le verifiche del **16 ottobre 2026** hanno confermato il rifiuto di TLS 1.0 e TLS 1.1.

| Endpoint | Scopo | Versioni TLS verificate |
| --- | --- | --- |
| `app.docbits.com` | Applicazione web | TLS 1.2 e TLS 1.3 |
| `auth.docbits.com` | Servizio di autenticazione | TLS 1.2 e TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 e TLS 1.3 |

### Quali tipi di crittografia sono supportati per i dati in transito?

| Domanda | Risposta per gli endpoint pubblici sopra indicati |
| --- | --- |
| TLS 1.1 è supportato? | **No.** Le connessioni che utilizzano TLS 1.1 vengono rifiutate. |
| TLS 1.2 è supportato? | **Sì.** |
| TLS 1.3 è supportato? | **Sì.** |

I seguenti metodi di crittografia sono stati negoziati con successo su **tutti e tre gli endpoint**, in test con convalida dei certificati eseguiti il 16 ottobre 2026:

| Metodo di crittografia | Lunghezza della chiave simmetrica | Versioni TLS verificate |
| --- | --- | --- |
| AES-128-GCM | 128 bit | TLS 1.2 e TLS 1.3 |
| AES-256-GCM | 256 bit | TLS 1.2 e TLS 1.3 |
| ChaCha20-Poly1305 | 256 bit | TLS 1.3 |

Questi metodi forniscono crittografia autenticata, proteggendo la riservatezza e l'integrità dei dati in transito. Il metodo negoziato dipende dalle capacità e dalla configurazione del client e del server. Le lunghezze indicate si riferiscono alle chiavi simmetriche per la cifratura dei dati, indipendentemente dalle dimensioni delle chiavi dei certificati. Le suite crittografiche TLS 1.2 testate utilizzano ECDHE per lo scambio di chiavi effimere.

La verifica copre le connessioni a questi endpoint pubblici, incluse quelle di client o altri server. Non determina le impostazioni di protocollo o crittografia di ogni connessione interna tra servizi, connessione a database, endpoint regionale o integrazione esterna. Tali connessioni richiedono una conferma per lo specifico ambiente e la specifica integrazione.

## Crittografia delle informazioni degli account archiviate

L'hashing delle password e delle chiavi API è una misura distinta dalla crittografia di database, volumi di archiviazione, oggetti e backup. I controlli descritti non dimostrano che ogni nome utente, campo dell'account o segreto di integrazione sia cifrato singolarmente, né che tutti i dati archiviati utilizzino un determinato algoritmo di crittografia.

Per un requisito che comprenda tutte le informazioni degli account dei clienti, richiedere a FELLOWPRO AG una dichiarazione specifica per l'ambiente che copra gli archivi di dati e i backup pertinenti, i metodi di crittografia, la gestione delle chiavi e l'accesso del personale. Un modello di hosting cloud o serverless, da solo, non dimostra queste proprietà.

## Risposta a un questionario di sicurezza del cliente

Il testo seguente descrive l'ambito confermato:

> Le password di accesso a DocBits sono memorizzate come hash unidirezionali con salt. Gli amministratori e il supporto DocBits non possono recuperare la password originale in chiaro dall'hash memorizzato. Gli utenti che dimenticano la password devono impostarne una nuova tramite la procedura di reimpostazione via email per tornare ad accedere con una password. SSO o passkey configurati offrono modalità di accesso alternative.
>
> Le chiavi create tramite la Gestione delle chiavi API DocBits vengono mostrate una sola volta e memorizzate come hash unidirezionali. Né gli amministratori né il supporto DocBits possono recuperare la chiave completa in seguito. Le chiavi perse devono essere revocate e sostituite.
>
> Gli endpoint pubblici dell'applicazione web, dell'autenticazione e dell'API DocBits sopra indicati supportano HTTPS con TLS 1.2 e TLS 1.3; TLS 1.0 e TLS 1.1 sono stati rifiutati nelle verifiche del 16 ottobre 2026. Sono stati verificati AES-128-GCM con 128 bit e AES-256-GCM con 256 bit con TLS 1.2 e TLS 1.3, oltre a ChaCha20-Poly1305 con 256 bit con TLS 1.3. Questa dichiarazione copre le connessioni a tali endpoint. La crittografia di tutte le informazioni degli account archiviate e dei backup, la protezione di ogni connessione interna tra server e l'accesso del personale alle credenziali delle integrazioni esterne richiedono una conferma separata per l'ambiente interessato.
