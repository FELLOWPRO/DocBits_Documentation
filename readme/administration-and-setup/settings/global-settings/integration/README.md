# Integration & SSO

<figure><img src="../../../../.gitbook/assets/integration_sso.png" alt="Integration & SSO"><figcaption><p>La pagina Integration & SSO</p></figcaption></figure>

La pagina Integration & SSO gestisce le chiavi API per l'accesso programmatico, gli ID dell'organizzazione e la configurazione del Single Sign-On (SSO).

## API Key

Gestisci le chiavi API utilizzate per l'accesso programmatico a DocBits.

| Colonna | Descrizione |
|--------|-------------|
| **Key** | Il valore mascherato della chiave API. Clicca sull'icona di copia per copiare la chiave completa. |
| **Name** | Un nome descrittivo per la chiave. |
| **Expires** | Data di scadenza (oppure "Never"). |
| **Last Used** | Quando la chiave è stata usata l'ultima volta. |
| **Status** | Active o Inactive. |
| **Actions** | Menu a tre punti per revocare o eliminare. |

Clicca su **+ Create API Key** per generare una nuova chiave.

## ID

Mostra gli identificatori della tua organizzazione:

| Campo | Descrizione |
|-------|-------------|
| **Org ID** | L'identificatore univoco della tua organizzazione. |
| **Sub Org ID** | L'ID della sotto-organizzazione attualmente selezionata. |

## SSO Service Provider Settings

I valori di configurazione SSO di DocBits necessari per configurare il tuo Identity Provider:

| Campo | Descrizione |
|-------|-------------|
| **Entity ID** | L'URL dei metadati SAML di DocBits. |
| **SLO URL** | L'URL di Single Logout. |
| **SSO URL** | L'URL dell'Assertion Consumer Service. |

Puoi anche usare **Download Certificate** e **Download Metadata** per la configurazione del tuo IdP.

## Identity Service Provider Settings

Configura il tuo Identity Provider (IdP) esterno:

| Campo | Descrizione |
|-------|-------------|
| **Tenant ID** | L'identificatore del tenant del tuo IdP. |
| **Upload file** | Carica il file XML dei metadati del tuo IdP. |

Clicca su **Configure** per salvare le impostazioni del tuo IdP.

* **Maggiore efficienza:** L'integrazione con altri strumenti e servizi può semplificare i flussi di lavoro e aumentare l'efficienza. Ad esempio, i documenti possono essere scambiati automaticamente tra Docbits e un sistema CRM, riducendo l'inserimento manuale e aumentando la produttività
* **Coerenza dei dati:** L'integrazione permette ai dati di essere scambiati senza interruzioni tra sistemi diversi, migliorando la coerenza e l'accuratezza dei dati. Questo evita incoerenze o doppi inserimenti di dati che potrebbero causare errori.
* **Aggiornamenti in tempo reale**: L'integrazione consente aggiornamenti in tempo reale tra piattaforme diverse, in modo che gli utenti abbiano sempre le informazioni più recenti. Questo è particolarmente importante per i processi aziendali critici che richiedono informazioni in tempo reale.
* **Automazione delle attività:** L'integrazione permette di automatizzare le attività di routine, risparmiando tempo e risorse. Ad esempio, le notifiche possono essere attivate automaticamente quando si verifica un determinato evento in un altro sistema, senza bisogno di intervento manuale.
* **Migliore esperienza utente:** Un'integrazione configurata correttamente garantisce un'esperienza utente fluida, perché gli utenti non devono passare da un sistema all'altro per accedere alle informazioni rilevanti. Questo migliora la soddisfazione degli utenti e contribuisce all'efficienza.

Per configurare correttamente le impostazioni di integrazione, è importante comprendere i requisiti dell'organizzazione e assicurarsi che l'integrazione si inserisca senza problemi nei flussi di lavoro e nei processi esistenti. Questo richiede una pianificazione, una configurazione e un monitoraggio accurati dell'integrazione per garantire che funzioni senza intoppi e offra il valore desiderato.





