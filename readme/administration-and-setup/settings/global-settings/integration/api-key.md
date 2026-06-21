# Chiave API

<figure><img src="https://lh7-us.googleusercontent.com/ulCymk1gu-de14qTaFfJwTEmAUp7DY000A40P3nTgRIb7pYXolCbh_GPJvRib5haIH75dPFewY5tJQ0xNbGP3wdSOgCxu7gdVBwlvxkHFcP_3HM3R15zuuBOZM2jEdFxlp2CpV1VDfktmLFSSw4BuLs" alt=""><figcaption></figcaption></figure>

### Chiave API

* **Chiave:** Questo è l'identificatore univoco utilizzato dalle applicazioni esterne per accedere all'API di DocBits. È fondamentale per autenticare le richieste effettuate a DocBits da altri software.
* Da qui è possibile eseguire azioni come visualizzare, rigenerare o copiare la chiave API, a seconda delle esigenze specifiche e dei protocolli di sicurezza.

### Impostazioni del provider di servizi SSO (Single Sign-On)

* **Entity ID:** Questo è l'identificatore di DocBits come provider di servizi nella configurazione SSO. Identifica DocBits in modo univoco all'interno del framework SSO.
* **URL SLO (Single Logout):** L'URL a cui vengono inviate le sessioni SSO per disconnettersi contemporaneamente da tutte le applicazioni collegate tramite SSO.
* **URL SSO: L'URL** utilizzato per avviare il processo di single sign-on.
* Sono disponibili azioni come "Scarica certificato" e "Scarica metadati" per ottenere i certificati di sicurezza necessari e le informazioni sui metadati utilizzati nella configurazione e nella manutenzione dell'integrazione SSO.

{% hint style="info" %}
Vedi Configurazione SSO
{% endhint %}

### Impostazioni del provider di servizi di identità

* Tenant ID: Potrebbe essere utilizzato quando DocBits si integra con servizi cloud che richiedono un identificatore tenant per gestire i dati e le configurazioni di accesso specifici dell'azienda che utilizza DocBits.
* Carica file: Consente all'amministratore di caricare file di configurazione o altri file necessari che facilitano l'integrazione con un provider di identità.
* Configura: Un pulsante per applicare o aggiornare le impostazioni dopo aver apportato modifiche o caricato nuove configurazioni.
