# Configurazione dell'Identity Service Provider

La configurazione dell'Identity Service Provider (IdP) per l'integrazione con DocBits richiede alcuni passaggi specifici. Ecco una guida per eseguirla:

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Accesso all'interfaccia di configurazione dell'IdP**

* Accedere al proprio Identity Service Provider (IdP) come amministratore.
* Passare all'interfaccia delle impostazioni o della configurazione dedicata alla gestione delle integrazioni SAML.

**Inserimento del Tenant ID:**

* Cercare la sezione che consente di configurare nuove integrazioni SAML.
* Inserire il tenant ID di DocBits. Questo ID identifica il proprio account DocBits presso l'IdP e consente la comunicazione sicura tra i due sistemi.

**Importazione dei file richiesti:**

* DocBits di norma richiede di scaricare i metadati o di aggiungere specifici dettagli di configurazione. Consultare la documentazione del proprio IdP per sapere quali passaggi sono necessari.
* Scaricare il file dei metadati di DocBits oppure importarlo nel menu di configurazione del proprio IdP. In alternativa, è possibile inserire manualmente i dettagli di configurazione richiesti, a seconda di ciò che l'IdP supporta.

**Configurazione delle impostazioni di integrazione:**

* Assicurarsi che le impostazioni di integrazione, come l'URL SSO, l'Entity ID e il certificato SAML, siano corrette.
* Verificare che l'URL di Single Log-Out (SLO) e gli altri parametri richiesti siano configurati correttamente. Sono fondamentali per un'autenticazione e una disconnessione tramite SAML senza problemi.

**Verifica della configurazione:**

* Dedicare del tempo a verificare che tutte le informazioni inserite siano corrette e che non vi siano errori di battitura o di configurazione.
* Eseguire dei test per assicurarsi che gli utenti possano accedere a DocBits tramite SAML e che il Single Log-Out funzioni correttamente.

**Considerazioni sulla sicurezza:**

* Assicurarsi che tutti i file trasferiti e i dettagli di configurazione siano gestiti in modo sicuro, per evitare perdite di dati o accessi non autorizzati.
* Proteggere le informazioni sensibili, come i certificati SAML e le credenziali, da accessi non autorizzati e conservarle in un luogo sicuro.
