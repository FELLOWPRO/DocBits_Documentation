---
description: Come importare i dati anagrafici direttamente in DocBits.
---

# Dati anagrafici personalizzati

#### Attivazione dei dati anagrafici personalizzati <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Dalla Dashboard vai su Impostazioni → Elaborazione documenti → Modulo.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-it.png" alt="Moduli di integrazione dei documenti, inclusi i dati anagrafici personalizzati e DocBits Operator. Nessun modulo è stato attivato durante la cattura."><figcaption><p>Moduli di integrazione dei documenti, inclusi i dati anagrafici personalizzati e DocBits Operator. Nessun modulo è stato attivato durante la cattura.</p></figcaption></figure></div>

In Modulo, attiva Custom Master Data premendo il cursore come mostrato di seguito.

<div align="left"></div>

#### Panoramica della funzionalità <a href="#feature-overview" id="feature-overview"></a>

Per aggiungere i tuoi dati anagrafici in DocBits, vai su Master Data Lookup nelle Impostazioni.

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-it.png" alt="Ricerca dei dati anagrafici: sorgenti e tabella dei fornitori, con i valori dell’organizzazione nascosti."><figcaption><p>Ricerca dei dati anagrafici: sorgenti e tabella dei fornitori, con i valori dell’organizzazione nascosti.</p></figcaption></figure></div>

Fai clic su “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="Pagina delle impostazioni di Master Data Lookup con i lookup Additional charge Costing Element, Purchase order, Purchase order Header e Supplier" width="375"><figcaption></figcaption></figure></div>

Potrai quindi scegliere se creare un Template o un Endpoint.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="Pannello Custom Master Data con i pulsanti Create Template e Create Endpoint" width="375"><figcaption></figcaption></figure></div>

#### Creare un Template <a href="#create-a-template" id="create-a-template"></a>

Il primo passaggio consiste nello scegliere se utilizzare il file ION API della tua organizzazione oppure OAuth2, e inserire i dati necessari.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="Passaggio Select Preset della procedura guidata di Master Data Lookup con la domanda What API do you want to use e le opzioni ION API e OAUTH2" width="375"><figcaption></figcaption></figure></div>

Successivamente configureremo i preset. Qui inserirai il nome della tabella dei dati anagrafici e l'URL della chiamata API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Passaggio Configure Preset della procedura guidata di Master Data Lookup con Preset Name, Application Type, campo GET URL e le schede PARAMS, HEADERS, AUTHORIZATION e BODY" width="375"><figcaption></figcaption></figure></div>

Dovrai quindi inserire il percorso JSON utilizzando la notazione a punti; per ulteriori informazioni sulla notazione a punti fai clic [qui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Infine, dovrai mappare i dati sulle colonne che desideri creare, come nell'esempio seguente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Procedura guidata di Master Data Lookup con Select Table Columns, una risposta JSON a sinistra e le colonne di mapping Column Name, Spaltenwert Name e Test Extraction" width="375"><figcaption></figcaption></figure></div>

Dopo averlo fatto, fai clic su Done affinché i nuovi dati anagrafici vengano creati e popolati.

#### Creare un Endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

Il primo passaggio consiste nello scegliere se utilizzare il file ION API della tua organizzazione, utilizzare OAuth2 oppure lasciare il campo vuoto e inserire i dati necessari.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="Passaggio Select Preset della procedura guidata degli endpoint di Master Data Lookup con Choose a preset for your endpoint e le opzioni BLANK, ION API e OAUTH2" width="375"><figcaption></figcaption></figure></div>

Successivamente configureremo i preset. Qui inserirai il nome della tabella dei dati anagrafici e l'URL della chiamata API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Passaggio Configure Preset della procedura guidata di Master Data Lookup con Preset Name, Application Type, campo GET URL e le schede PARAMS, HEADERS, AUTHORIZATION e BODY" width="375"><figcaption></figcaption></figure></div>

Dovrai quindi inserire il percorso JSON utilizzando la notazione a punti; per ulteriori informazioni sulla notazione a punti fai clic [qui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Infine, dovrai mappare i dati sulle colonne che desideri creare, come nell'esempio seguente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Procedura guidata di Master Data Lookup con Select Table Columns, una risposta JSON a sinistra e le colonne di mapping Column Name, Spaltenwert Name e Test Extraction" width="375"><figcaption></figcaption></figure></div>

Dopo averlo fatto, fai clic su Done affinché i nuovi dati anagrafici vengano creati e popolati.
