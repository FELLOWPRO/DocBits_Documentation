---
description: Usare DocBits con il tuo accesso Microsoft senza utilizzare una password (separata)
---

# Azure SSO

### Creare SAML SSO in Azure AD

Esegui i seguenti passaggi per aggiungere SAML SSO in Azure AD:

*   In Azure, vai alla tua console \`Azure Active Directory\`

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Nel pannello a sinistra, fai clic su \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Fai clic su \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Fai clic su \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Inserisci un nome per la tua applicazione. Mantieni le restanti selezioni predefinite.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Fai clic su \`Create\`

### Assegnare gli utenti alla configurazione SSO

Successivamente, assegna utenti o gruppi alla configurazione SSO.

**Importante**: Dovresti aver già creato utenti e gruppi in Azure AD. Se non hai utenti o gruppi, creali ora prima di procedere.

* In \`Getting Started\`, fai clic su \`Assign Users and Groups\`.
* Fai clic su \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Seleziona gli utenti e i gruppi che desideri assegnare a questa configurazione SSO. Questi utenti potranno autenticarsi in DocBits (utilizzando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Fai clic su \`Select\`
* Quando sei soddisfatto della tua selezione, fai clic su \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Vai all'elenco della vista \`Groups\` e trova i gruppi assegnati.

### Configurare SSO in Azure

Successivamente, devi completare la configurazione del single sign-on in Azure.\\

* Nel pannello a sinistra, fai clic su \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Fai clic su \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Fai clic su \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carica il file **metadata.xml** di DocBits, che puoi trovare nel menu Impostazioni **Integrazione** sotto **Impostazioni del provider di servizi SSO** del tuo account DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Modifica la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Verifica che \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` e \`Logout URL\` siano compilati correttamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Scarica il **Federation Metadata XML** appena generato.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Carica il file FederationMetadata.xml nelle **Impostazioni del provider di servizi di identità** del tuo account DocBits, che puoi trovare nel menu Impostazioni **Integrazione**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
