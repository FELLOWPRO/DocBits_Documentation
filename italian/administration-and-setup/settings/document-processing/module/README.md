# Module

<figure><img src="../../../../.gitbook/assets/module_settings.png" alt="Impostazioni Module"><figcaption><p>Pagina delle impostazioni Module</p></figcaption></figure>

La pagina Module ti permette di attivare o disattivare le funzionalità opzionali di DocBits. Ogni sezione raggruppa moduli correlati che possono essere attivati o disattivati.

## Purchase Order

Impostazioni per PO Matching e validazione.

| Impostazione | Descrizione |
|---------|-------------|
| **Auto Export if PO matched 100%** | Esporta automaticamente il documento quando il PO Matching raggiunge il 100%. |
| **PO Dashboard** | Attiva il dashboard degli ordini d'acquisto. Include il campo **PO Date Limit** per limitare i dati degli ordini per data. |
| **PO Shipment Order** | Attiva l'elaborazione degli ordini di spedizione collegati agli ordini d'acquisto. |
| **Shipment Order Dashboard** | Attiva un dashboard dedicato agli ordini di spedizione. |

## Auto Accounting

| Impostazione | Descrizione |
|---------|-------------|
| **Auto Accounting** | Attiva la contabilizzazione automatica dei documenti. Seleziona il tipo di ERP (ad es. LN, M3). |

## Dashboards

| Impostazione | Descrizione |
|---------|-------------|
| **Advance Shipment Dashboard** | Dashboard per il monitoraggio delle attività di spedizione anticipata. |
| **Invoice Dashboard** | Dashboard per il monitoraggio e l'analisi delle fatture. |
| **Full Text Search** | Attiva la ricerca full-text in tutti i documenti. |
| **Analytics Dashboard** | Attiva il dashboard di panoramica analitica. |

## Database Access

| Impostazione | Descrizione |
|---------|-------------|
| **DB Access** | Attiva l'accesso diretto al database per l'organizzazione. |

## AI Dashboard

| Impostazione | Descrizione |
|---------|-------------|
| **AI Document Warehouse** | Analisi del magazzino documentale basata sull'IA. |
| **Dashboard v2** | Dashboard aggiornato con funzionalità migliorate. |
| **Clickhouse Direct Access** | Attiva l'accesso diretto al database Clickhouse. |
| **Supplier Statistics** | Attiva statistiche e report a livello di fornitore. |

## Shipping & Supplier

| Impostazione | Descrizione |
|---------|-------------|
| **Supplier Portal** | Attiva il portale fornitori per la collaborazione con i fornitori. |

## Document Type

| Impostazione | Descrizione |
|---------|-------------|
| **Workflow Builder** | Crea e personalizza i workflow di elaborazione dei documenti. |
| **Annotation Mode** | Consente agli utenti di annotare i documenti nella vista di validazione. |
| **Show Report** | Attiva la generazione di report per i documenti. |
| **Inbound Emails** | Attiva la gestione delle email in entrata per tipo di documento. |
| **Models & Labels** | Gestisci i modelli IA e le etichette per il riconoscimento dei documenti. |
| **Document Script** | Attiva gli script personalizzati per l'elaborazione dei documenti. |
| **Document Scan** | Attiva la funzionalità di scansione dei documenti. |
| **Bar-Code/QR Code Extraction** | Estrae i dati dei codici a barre/QR code dai documenti. Seleziona i tipi di codice supportati. |
| **Custom Master Data** | Attiva i campi personalizzati dei dati anagrafici. |
| **Tasks & Notifications** | Attiva la gestione delle attività e le notifiche. Include l'interruttore **Dashboard Tasks Count**. |
| **DocBits Operator** | Attiva l'automazione del browser DocBits Operator. |
| **DocNet** | Attiva il networking documentale DocNet. |
| **IDM ACL Updater** | Aggiorna le liste di controllo degli accessi (ACL) di Infor Document Management. Carica un file ION-Mapping e configura le associazioni tra Infor-Doctype e ACL. |
| **Barcode Assignment** | Attiva l'assegnazione dei codici a barre ai documenti. |
| **Set Negative Sign For Credit Notes** | Applica automaticamente il segno negativo agli importi delle note di credito. |

## BOD Connection Stream

| Impostazione | Descrizione |
|---------|-------------|
| **BOD Connection Stream** | Attiva l'integrazione BOD (Business Object Document). Mostra lo **Stream Name** usato per la connessione. |

## Analytics

| Impostazione | Descrizione |
|---------|-------------|
| **Use PostgreSQL for Quality Analytics** | Passa da Prometheus (in tempo reale, si azzera a ogni deploy) a PostgreSQL (persistente per 90 giorni, analisi dei trend, campi con le prestazioni peggiori). |

## Vertex Tax Integration

| Impostazione | Descrizione |
|---------|-------------|
| **Vertex Tax Integration** | Attiva il calcolo delle imposte con Vertex. Configura **Base URL**, **Client ID** e **Client Secret**. Usa **Test Connection** per verificare. |
