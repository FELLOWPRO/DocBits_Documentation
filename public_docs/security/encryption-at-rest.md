---
description: Crittografia a riposo di DocBits su DigitalOcean, inclusi database, Spaces e copertura dei backup.
---

# Crittografia dei dati a riposo

DocBits utilizza DigitalOcean Managed Databases e DigitalOcean Spaces. La verifica del **16 ottobre 2026** ha confermato servizi gestiti PostgreSQL, OpenSearch e Valkey per la produzione UE a Francoforte. Le [FAQ su sicurezza e conformità](security-and-compliance-faq.md) documentano l’uso di Spaces per l’archiviazione.

Questa pagina descrive le misure di crittografia pubblicate da DigitalOcean per questi servizi. Le installazioni locali e le copie archiviate in altri sistemi richiedono una valutazione propria.

## Metodi di crittografia e ambito

| Servizio di archiviazione | Crittografia a riposo | Copertura |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | Crittografia dell’intero volume con LUKS; `aes-xts-plain64:sha256` con 512 bit di materiale di chiave XTS | I volumi sottostanti del servizio di database, inclusi i dati memorizzati su tali volumi. È una protezione a livello di archiviazione, non una dichiarazione di crittografia separata per ogni campo. |
| Backup di Managed Databases | AES-256 in modalità CTR, con HMAC-SHA256 per l’integrità; chiavi per file protette con RSA-3072 | Backup creati dal servizio di database gestito. Esportazioni e copie aggiuntive richiedono una verifica separata. |
| DigitalOcean Spaces | Crittografia dell’intero disco con AES-XTS a 256 bit | Dati sui dischi fisici di archiviazione. È distinta dalla crittografia opzionale per oggetto o lato client. |
| DigitalOcean Volumes, se utilizzati | Crittografia LUKS del cluster di archiviazione | Dati su questi volumi di archiviazione a blocchi; gli snapshot dei volumi ereditano la crittografia. |

XTS utilizza due chiavi AES. I 512 bit di materiale combinato di chiave XTS del servizio di database gestito corrispondono a due chiavi AES da 256 bit (AES-256-XTS), non a un algoritmo AES con una chiave da 512 bit.

I dettagli su database e backup provengono dal [modello di sicurezza di Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). Il [modello di sicurezza di Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) conferma la crittografia a riposo; il [modello di sicurezza di App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) specifica AES-XTS a 256 bit per i dischi fisici di Spaces. Le [funzionalità di Volumes](https://docs.digitalocean.com/products/volumes/details/features/) documentano la copertura di volumi e snapshot.

## Gestione delle chiavi e accesso autorizzato

DigitalOcean gestisce la crittografia dell’infrastruttura descritta. Per Managed Databases, documenta una chiave generata casualmente per ogni istanza e volume, eliminata alla distruzione dell’istanza. I backup dei database gestiti utilizzano una chiave casuale per file, protetta da una coppia di chiavi RSA specifica del servizio.

La crittografia dell’archiviazione protegge i dati sui supporti. Le applicazioni e gli utenti autorizzati del database possono continuare a leggere i dati tramite il servizio. Questo non dimostra che il personale del fornitore non possa accedere alle informazioni degli account, né che ogni campo sia cifrato a livello applicativo. L’hashing delle password e delle chiavi API è una misura separata; vedere [Archiviazione sicura delle credenziali](secure-storage-of-credentials.md).

Spaces supporta anche [SSE-C con chiavi fornite dal cliente](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Questa funzionalità opzionale non dimostra che DocBits utilizzi SSE-C o chiavi di crittografia gestite dal cliente.

## Crittografia dei backup

I backup creati da DigitalOcean Managed Databases sono cifrati con AES-256-CTR e protetti dalle modifiche non rilevate tramite HMAC-SHA256. Le chiavi di crittografia dei singoli file sono protette da RSA-3072. Gli snapshot dei volumi ereditano la crittografia del volume DigitalOcean sottostante. Queste informazioni descrivono le funzioni di backup dei servizi gestiti indicati.

## Tipi di crittografia a riposo

Di seguito sono riepilogati i principali metodi di crittografia dei servizi indicati:

> DocBits utilizza DigitalOcean Managed Databases e Spaces. I dati dei database gestiti sono cifrati a riposo a livello di intero volume tramite LUKS con AES-256-XTS (512 bit di materiale combinato di chiave XTS). I backup dei database gestiti utilizzano AES-256-CTR con protezione dell’integrità HMAC-SHA256 e RSA-3072 per proteggere le chiavi di crittografia dei singoli file. Spaces utilizza la crittografia dell’intero disco con AES-XTS a 256 bit sui supporti fisici.
>
> Queste misure a livello di archiviazione coprono i dati sui volumi e dischi protetti; non implicano la crittografia separata di ogni campo del database. DigitalOcean gestisce le chiavi di crittografia dell’infrastruttura. Questa dichiarazione comprende i servizi gestiti indicati.
