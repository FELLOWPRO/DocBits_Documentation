---
description: DocBits met uw Microsoft-account gebruiken zonder een afzonderlijk wachtwoord
---

# Azure-SSO

### SAML-SSO aanmaken in Azure AD

Voer de volgende stappen uit om SAML-SSO toe te voegen in Azure AD:

*   Open in Azure de console \`Azure Active Directory\`.

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klik in het linkerpaneel op \`Enterprise applications\`.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klik op \`+ New application\`.

<figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_new_app_2.png" alt="Nieuwe toepassing voor Azure-SSO aanmaken in DocBits"><figcaption></figcaption></figure>

* Klik op \`+ Create your own application\`.

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_create_own_app_2.png" alt="Eigen toepassing voor Azure-SSO aanmaken in DocBits"><figcaption></figcaption></figure></div>

* Voer een naam voor uw toepassing in. Behoud de overige standaardkeuzes.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Klik op \`Create\`.

### Gebruikers toewijzen aan de SSO-configuratie

Wijs vervolgens gebruikers of groepen toe aan de SSO-configuratie.

**Belangrijk**: maak eerst gebruikers en groepen aan in Azure AD. Als die nog ontbreken, maakt u ze aan voordat u doorgaat.

* Klik onder \`Getting Started\` op \`Assign Users and Groups\`.
* Klik op \`+ Add user\`.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Selecteer de gebruikers en groepen die u aan deze SSO-configuratie wilt toewijzen. Deze gebruikers kunnen zich met SSO aanmelden bij DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Klik op \`Select\`.
* Klik op \`Assign\` wanneer de selectie klopt.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_groups.png" alt="Groepen voor Azure-SSO in DocBits"><figcaption></figcaption></figure></div>

* Open de lijstweergave \`Groups\` en zoek de toegewezen groepen.

### SSO instellen in Azure

Voltooi vervolgens de configuratie voor eenmalige aanmelding in Azure.\\

* Klik in het linkerpaneel op \`Single sign-on\`.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klik op \`SAML\`.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klik op \`Upload metadata file\`.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload het DocBits-bestand **metadata.xml**. U vindt dit in uw DocBits-account in het instellingenmenu **Integration**, onder **SSO Service Provider Settings**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Bewerk \`Basic SAML Configuration\`.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Controleer of \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` en \`Logout URL\` correct zijn ingevuld.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Download het nieuw gegenereerde bestand **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Upload FederationMetadata.xml naar **Identity Service Provider Settings** in uw DocBits-account, in het instellingenmenu **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
