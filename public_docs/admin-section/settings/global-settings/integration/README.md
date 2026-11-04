# Integrazione

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## Chiave API

* **Chiave**: Questo è l'identificatore univoco utilizzato dalle applicazioni esterne per accedere all'API di Docbits. È cruciale per autenticare le richieste fatte a Docbits da altri software.
* Qui è possibile eseguire azioni come visualizzare, rigenerare o copiare la chiave API, a seconda delle esigenze specifiche e dei protocolli di sicurezza.

## Impostazioni del Fornitore di Servizi SSO (Single Sign-On)

* **ID Entità**: Questo è l'identificatore per Docbits come fornitore di servizi nella configurazione SSO. Identifica in modo univoco Docbits all'interno del framework SSO.
* **URL SLO (Single Logout)**: L'URL a cui le sessioni SSO vengono inviate per disconnettersi contemporaneamente da tutte le applicazioni collegate tramite SSO.
* **URL SSO**: L'URL utilizzato per avviare il processo di accesso unico.
* Sono disponibili azioni come "Scarica Certificato" e "Scarica Metadati" per ottenere i certificati di sicurezza necessari e le informazioni sui metadati utilizzati per configurare e mantenere l'integrazione SSO.

{% hint style="info" %}
Vedi [Configurazione SSO](../../../setup/sso-configuration/)
{% endhint %}

## Impostazioni del Fornitore di Servizi di Identità

* **ID Tenant**: Potrebbe essere utilizzato quando Docbits si integra con servizi cloud che richiedono un identificatore del tenant per gestire dati e configurazioni di accesso specifici per l'azienda che utilizza Docbits.
* **Carica file**: Consente all'amministratore di caricare file di configurazione o altri file necessari che facilitano l'integrazione con un fornitore di identità.
* **Configura**: Un pulsante per applicare o aggiornare le impostazioni dopo aver apportato modifiche o caricato nuove configurazioni.
