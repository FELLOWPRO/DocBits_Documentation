# Archiviazione, conservazione ed eliminazione dei dati

I tuoi dati sono in buone mani con DocBits. Gestiamo DocBits in due regioni, **Francoforte sul Meno (UE)** e **San Francisco (USA)**, e nelle impostazioni decidi tu per quanto tempo i documenti restano presso di noi. Questa pagina illustra le sedi di archiviazione, i periodi di conservazione e l'eliminazione.

**Documentazione aggiornata al: 28 ottobre 2026.**

## In sintesi

- **Scegli tu la regione:** Francoforte per i clienti UE, San Francisco per i clienti USA.
- **I tuoi dati restano nella tua regione.** I dati UE sono ospitati a Francoforte, i dati USA a San Francisco. Non c'è alcuna commistione di dati tra le regioni.
- **Decidi tu per quanto tempo vengono conservati i tuoi documenti** in **Elaborazione documenti → Scadenza dei documenti** ([vai all'impostazione](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **I file OCR temporanei** vengono eliminati automaticamente dopo 90 minuti.
- **Siamo felici di aiutarti:** il nostro team risponde a domande e richieste di eliminazione all'indirizzo **compliance@fellowpro.com**.

## Dove sono archiviati i tuoi dati?

| Regione | Per chi | Sede | Servizi utilizzati |
| --- | --- | --- | --- |
| **UE** | Tutti i clienti UE | **Francoforte sul Meno, Germania** | DigitalOcean Kubernetes (regione `fra1`) con database gestiti PostgreSQL, OpenSearch e Valkey (`fra1`), oltre a DigitalOcean Spaces per l'archiviazione dei file |
| **USA** | Clienti USA | **San Francisco, USA** | DigitalOcean Kubernetes (regione `sfo2`) con database gestiti PostgreSQL, OpenSearch e Valkey (`sfo2`) |

**Backup nell'UE:** Francoforte è la sede primaria dei backup e Amsterdam (Paesi Bassi) quella secondaria, quindi anche le tue copie di backup restano all'interno dell'UE.

**Sistemi collegati:** se esporti documenti verso il tuo ERP, Infor IDM o un altro sistema di destinazione, queste copie vengono archiviate lì, secondo le regole e nella sede di quel sistema. Questo rimane sotto il tuo controllo.

## Per quanto tempo vengono conservati i dati?

| Tipo di dati | Conservazione |
| --- | --- |
| **Documenti caricati e dati estratti** | Controllata da te tramite [Scadenza dei documenti](../administration-and-setup/settings/document-processing/documents-expiry.md) (vedi sotto). |
| **File OCR temporanei** | Pulizia automatica dopo **90 minuti**. Vale solo per l'archiviazione OCR temporanea, non per il tuo documento in DocBits. |
| **Log accessibili al cliente** (consultabili in [Registro attività](../administration-and-setup/settings/log-settings/README.md)) | **30 giorni** |
| **Log interni** | **3 mesi** |
| **Backup giornalieri del database (gestiti)** | **7 giorni**; i backup più vecchi vengono rimossi automaticamente. |
| **Backup giornalieri aggiuntivi (SnapShooter)** | Per i database di produzione e sandbox; la conservazione è definita per ogni ambiente. |
| **Cookie e archiviazione del browser** | Varia in base alla finalità, vedi [Cookie e archiviazione del browser](cookies-and-browser-storage.md). |

Eseguiamo inoltre backup giornalieri, settimanali, trimestrali e annuali. Su richiesta, siamo lieti di comunicarti i periodi di conservazione esatti per questi tipi di backup nel tuo ambiente.

## Come impostare la conservazione dei tuoi documenti

Nelle impostazioni, apri **Elaborazione documenti → Scadenza dei documenti**. Ci sono due impostazioni:

- **Delete document after:** per quanto tempo vengono conservati i documenti.
- **Delete finished document after:** per quanto tempo vengono conservati i documenti conclusi, completamente elaborati ed esportati.

Le opzioni sono **Default**, **48 Hours**, **1 Week**, **2 Weeks** e **4 Weeks**. **Default** applica il valore predefinito del sistema. Se desideri un periodo fisso, ti basta scegliere una delle durate. Tutti i dettagli sono nella [guida Scadenza dei documenti](../administration-and-setup/settings/document-processing/documents-expiry.md).

## Cosa succede quando i dati vengono eliminati?

La scadenza dei documenti elimina automaticamente i tuoi documenti allo scadere del periodo scelto. Questo avviene indipendentemente dalla pulizia dei file OCR temporanei, dalla scadenza dei log e dalla conservazione dei backup.

Da sapere:

- **I backup scadono secondo un proprio calendario.** Eliminare un documento nel sistema attivo non rimuove quindi subito le copie di backup, ma solo al termine del rispettivo periodo di backup.
- **Le copie esportate sono tue.** Quando DocBits elimina un documento, la copia nel tuo ERP o archivio rimane. Pianifica lì la conservazione in base alle tue esigenze.

## Domande o richieste di eliminazione? Siamo a tua disposizione

Per informazioni sulla tua installazione o per una richiesta di eliminazione, scrivici a **compliance@fellowpro.com**. Indicaci la tua organizzazione, l'ambiente interessato, il tipo di dati e l'ambito necessario. Non inviarci password o chiavi API.

Siamo inoltre lieti di confermarti:

- La tua regione attiva e le impostazioni di conservazione effettive, incluso il valore predefinito del sistema.
- Quando inizia il periodo di eliminazione e con quale frequenza viene eseguita la pulizia.
- L'ambito dell'eliminazione per documenti, dati estratti, indici di ricerca e dati derivati.
- Sedi e periodi di conservazione di tutti i tipi di backup, anche dopo la fine del contratto.

## Ulteriori informazioni sulla sicurezza

- [DocBits (FELLOWPRO AG) — Questionario sulla Sicurezza e Conformità](security-and-compliance-faq.md)
- [Crittografia dei dati a riposo](encryption-at-rest.md)
- [Archiviazione sicura delle credenziali](secure-storage-of-credentials.md)
- [Cookie e archiviazione del browser](cookies-and-browser-storage.md)
