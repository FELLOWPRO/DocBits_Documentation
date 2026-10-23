---
description: DocBits mit Ihrem Microsoft-Login nutzen, ohne ein (separates) Passwort zu verwenden
---

# Azure SSO

### SAML SSO in Azure AD erstellen

Führen Sie die folgenden Schritte aus, um SAML SSO in Azure AD hinzuzufügen:

*   Wechseln Sie in Azure zu Ihrer \`Azure Active Directory\`-Konsole

    ![Navigationsbereich des Azure-Portals mit Favoriten wie Resource groups, All resources und Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klicken Sie im linken Bereich auf \`Enterprise applications\`

![Linker Bereich von Azure Active Directory mit den Einträgen unter Manage: Users, Groups, Roles and administrators und Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klicken Sie auf \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Dialog Add Assignment in Azure mit 2 users selected, 2 groups selected und Select Role auf User eingestellt"><figcaption></figcaption></figure>

* Klicken Sie auf \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Übersichtsmenü der Enterprise Application in Azure mit den Einträgen unter Manage: Properties, Owners, Users and groups, Single sign-on und Provisioning"><figcaption></figcaption></figure></div>

* Geben Sie einen Namen für Ihre Anwendung ein. Behalten Sie die übrigen Standardauswahlen bei.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Dialog Create your own application in Azure mit dem App-Namen MyApplication und den Optionen zur Anwendungsintegration"><figcaption></figcaption></figure>

* Klicken Sie auf \`Create\`

### Benutzer der SSO-Konfiguration zuweisen

Weisen Sie als Nächstes der SSO-Konfiguration Benutzer oder Gruppen zu.

**Wichtig**: Sie sollten bereits Benutzer und Gruppen in Azure AD erstellt haben. Falls Sie noch keine Benutzer oder Gruppen haben, erstellen Sie diese jetzt, bevor Sie fortfahren.

* Klicken Sie unter \`Getting Started\` auf \`Assign Users and Groups\`.
* Klicken Sie auf \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Seite Users and groups für MyApplication in Azure mit den Schaltflächen Add user, Edit und Remove und einer leeren Liste unter Display Name" width="563"><figcaption></figcaption></figure>

* Wählen Sie die Benutzer und Gruppen aus, die Sie dieser SSO-Konfiguration zuweisen möchten. Diese Benutzer können sich in DocBits (mit SSO) authentifizieren.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Auswahlpanel für Benutzer und Gruppen in Azure mit einer Liste von Daniel-Benutzern und einem Panel Selected items"><figcaption></figcaption></figure>

* Klicken Sie auf \`Select\`
* Wenn Sie mit Ihrer Auswahl zufrieden sind, klicken Sie auf \`Assign\`

![Dialog Add Assignment in Azure mit 2 users selected, 2 groups selected und Select Role auf User eingestellt](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216).png" alt="Dialog Create your own application in Azure mit dem App-Namen MyApplication und den Optionen zur Anwendungsintegration"><figcaption></figcaption></figure></div>

* Wechseln Sie zur Listenansicht \`Groups\` und suchen Sie die zugewiesenen Gruppen.

### SSO in Azure einrichten

Als Nächstes müssen Sie die Einrichtung von Single Sign-On in Azure abschließen.\\

* Klicken Sie im linken Bereich auf \`Single sign-on\`

![Übersichtsmenü der Enterprise Application in Azure mit den Einträgen unter Manage: Properties, Owners, Users and groups, Single sign-on und Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klicken Sie auf \`SAML\`

![SAML-Optionskarte in Azure, die eine umfangreiche und sichere Authentifizierung mit dem Security Assertion Markup Language-Protokoll beschreibt](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klicken Sie auf \`Upload metadata file\`

![Panel SAML-based Sign-on in Azure mit Upload metadata file und Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Laden Sie die DocBits-Datei **metadata.xml** hoch. Sie finden sie im Menü Settings unter **Integration** im Bereich **SSO Service Provider Settings** Ihres DocBits-Kontos.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Seite SSO Service Provider Settings mit der Tenant ID, der Entity ID sowie den Feldern SSO Url, SLO Url und Metadata Url"><figcaption></figcaption></figure>

* Bearbeiten Sie die \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Bildschirm „Single Sign-On mit SAML einrichten“ mit der Basic SAML Configuration und den Feldern Identifier, Reply URL, Sign on URL und Logout Url"><figcaption></figcaption></figure>

* Prüfen Sie, ob \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` und \`Logout URL\` richtig befüllt sind.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Editor für Basic SAML Configuration in Azure mit den Feldern Identifier, Reply URL, Sign on URL, Relay State und Logout Url sowie Save"><figcaption></figcaption></figure>

* Laden Sie die neu erzeugte **Federation Metadata XML** herunter.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Abschnitt SAML Signing Certificate in Azure mit Fingerabdruck, Ablaufdatum und Download-Links für Certificate (Raw) und Federation Metadata XML"><figcaption></figcaption></figure>

* Laden Sie die Datei FederationMetadata.xml in den **Identity Service Provider Settings** Ihres DocBits-Kontos hoch, die Sie im Menü Settings unter **Integration** finden.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Dialog „Identity Service Provider Settings“ in DocBits mit der Tenant ID FELLOWPRO_PRD und der Schaltfläche „Upload file“"><figcaption></figcaption></figure>
