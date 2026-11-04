---
description: DocBits gebruiken met uw Microsoft-login zonder een (apart) wachtwoord te gebruiken
---

# Azure SSO

### SAML SSO maken in Azure AD

Voer de volgende stappen uit om SAML SSO toe te voegen in Azure AD:

*   Ga in Azure naar uw `Azure Active Directory`-console

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klik in het linkerpaneel op `Enterprise applications`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klik op `+ New application`

<figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_new_app.png" alt="Docbits Azure Sso New App"><figcaption></figcaption></figure>

* Klik op `+ Create your own application`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_create_own_app.png" alt="Docbits Azure Sso Create Own App"><figcaption></figcaption></figure></div>

* Voer een naam in voor uw applicatie. Behoud de overige standaardselecties.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Klik op `Create`

### Gebruikers toewijzen aan de SSO-configuratie

Wijs vervolgens gebruikers of groepen toe aan de SSO-configuratie.

**Belangrijk**: U moet al gebruikers en groepen hebben aangemaakt in Azure AD. Als u nog geen gebruikers of groepen heeft, maak deze dan aan voordat u verdergaat.

* Klik onder `Getting Started` op `Assign Users and Groups`.
* Klik op `+ Add user`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Selecteer de gebruikers en groepen die u aan deze SSO-configuratie wilt toewijzen. Deze gebruikers kunnen worden geauthenticeerd in DocBits (met behulp van SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Klik op `Select`
* Wanneer u tevreden bent met uw selectie, klikt u op `Assign`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Ga naar de lijstweergave `Groups` en zoek de toegewezen groepen.

### SSO instellen in Azure

Vervolgens moet u het instellen van single-sign-on in Azure voltooien.

* Klik in het linkerpaneel op `Single sign-on`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klik op `SAML`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klik op `Upload metadata file`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload de DocBits **metadata.xml**, die u kunt vinden in het menu Instellingen **Integratie** onder **Instellingen SSO-serviceprovider** van uw DocBits-account.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Bewerk de `Basic SAML Configuration`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Controleer of de `Entity ID`, `ACS URL`, `Sign on URL` and `Logout URL` correct zijn ingevuld.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Download de nieuw gegenereerde **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Upload de FederationMetadata.xml in de **Instellingen identiteitsserviceprovider** van uw DocBits-account, die u kunt vinden in het menu Instellingen **Integratie**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
