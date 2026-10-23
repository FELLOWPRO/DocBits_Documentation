---
description: Usare DocBits con il tuo accesso Microsoft senza utilizzare una password (separata)
---

# SSO di Azure

### Creare SAML SSO in Azure AD

Esegui i seguenti passaggi per aggiungere SAML SSO in Azure AD:

*   In Azure, vai alla tua console \`Azure Active Directory\`

    ![Riquadro di navigazione del portale di Azure con preferiti come Resource groups, All resources e Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Nel pannello a sinistra, fai clic su \`Enterprise applications\`

![Pannello sinistro di Azure Active Directory con le voci Gestisci Users, Groups, Roles and administrators ed Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Fai clic su \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Finestra di dialogo Add Assignment in Azure con 2 users selected, 2 groups selected e Select Role impostato su User"><figcaption></figcaption></figure>

* Fai clic su \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Menu panoramica dell'applicazione aziendale in Azure con le voci Manage Properties, Owners, Users and groups, Single sign-on e Provisioning"><figcaption></figcaption></figure></div>

* Inserisci un nome per la tua applicazione. Mantieni le restanti selezioni predefinite.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Finestra di dialogo Create your own application in Azure con il nome dell'app MyApplication e le opzioni di integrazione dell'applicazione"><figcaption></figcaption></figure>

* Fai clic su \`Create\`

### Assegnare gli utenti alla configurazione SSO

Successivamente, assegna utenti o gruppi alla configurazione SSO.

**Importante**: Dovresti aver già creato utenti e gruppi in Azure AD. Se non hai utenti o gruppi, creali ora prima di procedere.

* In \`Getting Started\`, fai clic su \`Assign Users and Groups\`.
* Fai clic su \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Pagina Users and groups di MyApplication in Azure con i pulsanti Add user, Edit e Remove e un elenco Display Name vuoto" width="563"><figcaption></figcaption></figure>

* Seleziona gli utenti e i gruppi che desideri assegnare a questa configurazione SSO. Questi utenti potranno autenticarsi in DocBits (utilizzando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Pannello di selezione di utenti e gruppi in Azure con un elenco di utenti Daniel e un pannello Selected items"><figcaption></figcaption></figure>

* Fai clic su \`Select\`
* Quando sei soddisfatto della tua selezione, fai clic su \`Assign\`

![Finestra di dialogo Add Assignment in Azure con 2 users selected, 2 groups selected e Select Role impostato su User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Finestra di dialogo Create your own application in Azure con il nome dell'app MyApplication e le opzioni di integrazione dell'applicazione"><figcaption></figcaption></figure></div>

* Vai all'elenco della vista \`Groups\` e trova i gruppi assegnati.

### Configurare SSO in Azure

Successivamente, devi completare la configurazione del single sign-on in Azure.\\

* Nel pannello a sinistra, fai clic su \`Single sign-on\`

![Menu panoramica dell'applicazione aziendale in Azure con le voci Manage Properties, Owners, Users and groups, Single sign-on e Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Fai clic su \`SAML\`

![Scheda dell'opzione SAML in Azure che descrive un'autenticazione completa e sicura con il protocollo Security Assertion Markup Language](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Fai clic su \`Upload metadata file\`

![Pannello SAML-based Sign-on in Azure con Upload metadata file e Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carica il file **metadata.xml** di DocBits, che puoi trovare nel menu Impostazioni **Integrazione** sotto **Impostazioni del provider di servizi SSO** del tuo account DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Pagina SSO Service Provider Settings con il Tenant ID, l'Entity ID e i campi SSO Url, SLO Url e Metadata Url"><figcaption></figcaption></figure>

* Modifica la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Schermata di configurazione dell'accesso Single Sign-On con SAML che mostra Basic SAML Configuration con Identifier, Reply URL, Sign on URL e Logout Url"><figcaption></figcaption></figure>

* Verifica che \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` e \`Logout URL\` siano compilati correttamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Editor di Basic SAML Configuration in Azure con i campi Identifier, Reply URL, Sign on URL, Relay State e Logout Url oltre a Save"><figcaption></figcaption></figure>

* Scarica il **Federation Metadata XML** appena generato.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sezione SAML Signing Certificate in Azure con impronta digitale, data di scadenza e link di download per Certificate (Raw) e Federation Metadata XML"><figcaption></figcaption></figure>

* Carica il file FederationMetadata.xml nelle **Impostazioni del provider di servizi di identità** del tuo account DocBits, che puoi trovare nel menu Impostazioni **Integrazione**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Finestra di dialogo Identity Service Provider Settings in DocBits con il Tenant ID FELLOWPRO_PRD e il pulsante Upload file"><figcaption></figcaption></figure>
