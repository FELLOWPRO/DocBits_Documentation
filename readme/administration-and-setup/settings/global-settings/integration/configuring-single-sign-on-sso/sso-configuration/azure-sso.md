---
description: Usare DocBits con il tuo accesso Microsoft senza utilizzare una password (separata)
---

# SSO di Azure

### Creare SAML SSO in Azure AD

Esegui i seguenti passaggi per aggiungere SAML SSO in Azure AD:

*   In Azure, vai alla tua console \`Azure Active Directory\`

    ![Pagina iniziale del portale Azure con Azure Active Directory nei preferiti della navigazione a sinistra](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Nel pannello a sinistra, fai clic su \`Enterprise applications\`

![Navigazione a sinistra di Azure Active Directory con il gruppo Gestisci e la voce Applicazioni aziendali](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Fai clic su \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Pagina Applicazioni aziendali di Azure Active Directory con l'elenco Tutte le applicazioni e il pulsante Nuova applicazione"><figcaption></figcaption></figure>

* Fai clic su \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Finestra Esplora la raccolta Azure AD con i pulsanti Crea la tua applicazione e Richiedi una nuova app della raccolta e il campo di ricerca Cerca applicazione"><figcaption></figcaption></figure></div>

* Inserisci un nome per la tua applicazione. Mantieni le restanti selezioni predefinite.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Finestra Crea la tua applicazione con il nome MyApplication e l'opzione selezionata Integra qualsiasi altra applicazione non presente nella raccolta"><figcaption></figcaption></figure>

* Fai clic su \`Create\`

### Assegnare gli utenti alla configurazione SSO

Successivamente, assegna utenti o gruppi alla configurazione SSO.

**Importante**: Dovresti aver già creato utenti e gruppi in Azure AD. Se non hai utenti o gruppi, creali ora prima di procedere.

* In \`Getting Started\`, fai clic su \`Assign Users and Groups\`.
* Fai clic su \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Pagina Utenti e gruppi dell'applicazione MyApplication con i pulsanti Aggiungi utente, Modifica, Rimuovi e Aggiorna e il messaggio Nessuna assegnazione di applicazione trovata" width="563"><figcaption></figcaption></figure>

* Seleziona gli utenti e i gruppi che desideri assegnare a questa configurazione SSO. Questi utenti potranno autenticarsi in DocBits (utilizzando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Pannello di selezione utenti con diversi utenti elencati e la sezione Selezionati"><figcaption></figcaption></figure>

* Fai clic su \`Select\`
* Quando sei soddisfatto della tua selezione, fai clic su \`Assign\`

![Finestra Aggiungi assegnazione del tenant chimdustries con il messaggio 2 utenti selezionati e 2 gruppi selezionati](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Pulsante Assegna evidenziato con un bordo verde nella finestra di assegnazione di Azure Active Directory"><figcaption></figcaption></figure></div>

* Vai all'elenco della vista \`Groups\` e trova i gruppi assegnati.

### Configurare SSO in Azure

Successivamente, devi completare la configurazione del single sign-on in Azure.\\

* Nel pannello a sinistra, fai clic su \`Single sign-on\`

![Navigazione a sinistra dell'applicazione aziendale MyApplication con la voce Accesso singolo](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Fai clic su \`SAML\`

![Pagina Accesso singolo con il riquadro SAML e il testo Autenticazione sicura e affidabile per le applicazioni tramite il protocollo SAML](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Fai clic su \`Upload metadata file\`

![Pagina Accesso basato su SAML con i collegamenti Carica file di metadati e Configura accesso singolo](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carica il file **metadata.xml** di DocBits, che puoi trovare nel menu Impostazioni **Integrazione** sotto **Impostazioni del provider di servizi SSO** del tuo account DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Impostazioni del provider di servizi SSO in DocBits con l'Entity ID, lo SLO URI e lo SSO URI e i pulsanti Scarica certificato e Scarica metadati"><figcaption></figcaption></figure>

* Modifica la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Pagina Configura accesso singolo con SAML con la sezione Configurazione SAML di base e i campi Identificatore Entity ID, URL di risposta, URL di accesso, Stato di inoltro e URL di disconnessione"><figcaption></figcaption></figure>

* Verifica che \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` e \`Logout URL\` siano compilati correttamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Configurazione SAML di base in Azure con i testi descrittivi, l'Identificatore Entity ID impostato sull'URL dei metadati SAML del tenant e l'URL di risposta come Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Scarica il **Federation Metadata XML** appena generato.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sezione Certificato di firma SAML con lo stato Attivo, l'identificazione personale, la data di scadenza, l'e-mail di notifica e i collegamenti di download Certificato raw e XML dei metadati di federazione"><figcaption></figcaption></figure>

* Carica il file FederationMetadata.xml nelle **Impostazioni del provider di servizi di identità** del tuo account DocBits, che puoi trovare nel menu Impostazioni **Integrazione**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Impostazioni del provider di servizi di identità in DocBits con il Tenant ID, i pulsanti Carica file e Importa e la voce del file esistente"><figcaption></figcaption></figure>
