---
description: DocBits mit Ihrem Microsoft-Login nutzen, ohne ein (separates) Passwort zu verwenden
---

# Azure SSO

### SAML SSO in Azure AD erstellen

Führen Sie die folgenden Schritte aus, um SAML SSO in Azure AD hinzuzufügen:

*   Wechseln Sie in Azure zu Ihrer \`Azure Active Directory\`-Konsole

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klicken Sie im linken Bereich auf \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klicken Sie auf \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Klicken Sie auf \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Geben Sie einen Namen für Ihre Anwendung ein. Behalten Sie die übrigen Standardauswahlen bei.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Klicken Sie auf \`Create\`

### Benutzer der SSO-Konfiguration zuweisen

Weisen Sie als Nächstes der SSO-Konfiguration Benutzer oder Gruppen zu.

**Wichtig**: Sie sollten bereits Benutzer und Gruppen in Azure AD erstellt haben. Falls Sie noch keine Benutzer oder Gruppen haben, erstellen Sie diese jetzt, bevor Sie fortfahren.

* Klicken Sie unter \`Getting Started\` auf \`Assign Users and Groups\`.
* Klicken Sie auf \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Wählen Sie die Benutzer und Gruppen aus, die Sie dieser SSO-Konfiguration zuweisen möchten. Diese Benutzer können sich in DocBits (mit SSO) authentifizieren.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Klicken Sie auf \`Select\`
* Wenn Sie mit Ihrer Auswahl zufrieden sind, klicken Sie auf \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216).png" alt=""><figcaption></figcaption></figure></div>

* Wechseln Sie zur Listenansicht \`Groups\` und suchen Sie die zugewiesenen Gruppen.

### SSO in Azure einrichten

Als Nächstes müssen Sie die Einrichtung von Single Sign-On in Azure abschließen.\\

* Klicken Sie im linken Bereich auf \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klicken Sie auf \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klicken Sie auf \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Laden Sie die DocBits-Datei **metadata.xml** hoch. Sie finden sie im Menü Settings unter **Integration** im Bereich **SSO Service Provider Settings** Ihres DocBits-Kontos.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Bearbeiten Sie die \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Prüfen Sie, ob \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` und \`Logout URL\` richtig befüllt sind.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Laden Sie die neu erzeugte **Federation Metadata XML** herunter.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Laden Sie die Datei FederationMetadata.xml in den **Identity Service Provider Settings** Ihres DocBits-Kontos hoch, die Sie im Menü Settings unter **Integration** finden.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
