---
description: DocBits mit Ihrem Microsoft-Login nutzen, ohne ein (separates) Passwort zu verwenden
---

# Azure SSO

### SAML SSO in Azure AD erstellen

Führen Sie die folgenden Schritte aus, um SAML SSO in Azure AD hinzuzufügen:

*   Wechseln Sie in Azure zu Ihrer \`Azure Active Directory\`-Konsole

    ![Startseite des Azure-Portals mit Azure Active Directory in den Favoriten der linken Navigation](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klicken Sie im linken Bereich auf \`Enterprise applications\`

![Linke Navigation von Azure Active Directory mit der Gruppe Verwalten und dem Eintrag Unternehmensanwendungen](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klicken Sie auf \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Seite Unternehmensanwendungen in Azure Active Directory mit der Liste Alle Anwendungen und der Schaltfläche Neue Anwendung"><figcaption></figcaption></figure>

* Klicken Sie auf \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Dialog Azure AD-Katalog durchsuchen mit den Schaltflächen Eigene Anwendung erstellen und Neue Kataloganwendung anfordern sowie dem Suchfeld Anwendung suchen"><figcaption></figcaption></figure></div>

* Geben Sie einen Namen für Ihre Anwendung ein. Behalten Sie die übrigen Standardauswahlen bei.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Dialog Eigene Anwendung erstellen mit dem Namen MyApplication und der gewählten Option Eine andere Anwendung integrieren, die Sie nicht im Katalog finden"><figcaption></figcaption></figure>

* Klicken Sie auf \`Create\`

### Benutzer der SSO-Konfiguration zuweisen

Weisen Sie als Nächstes der SSO-Konfiguration Benutzer oder Gruppen zu.

**Wichtig**: Sie sollten bereits Benutzer und Gruppen in Azure AD erstellt haben. Falls Sie noch keine Benutzer oder Gruppen haben, erstellen Sie diese jetzt, bevor Sie fortfahren.

* Klicken Sie unter \`Getting Started\` auf \`Assign Users and Groups\`.
* Klicken Sie auf \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Seite Benutzer und Gruppen der Anwendung MyApplication mit den Schaltflächen Benutzer hinzufügen, Bearbeiten, Entfernen und Aktualisieren und der Meldung Keine Anwendungszuweisungen gefunden" width="563"><figcaption></figcaption></figure>

* Wählen Sie die Benutzer und Gruppen aus, die Sie dieser SSO-Konfiguration zuweisen möchten. Diese Benutzer können sich in DocBits (mit SSO) authentifizieren.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Auswahlbereich für Benutzer mit mehreren aufgelisteten Benutzern und dem Abschnitt Ausgewählt"><figcaption></figcaption></figure>

* Klicken Sie auf \`Select\`
* Wenn Sie mit Ihrer Auswahl zufrieden sind, klicken Sie auf \`Assign\`

![Dialog Zuweisung hinzufügen des Mandanten chimdustries mit der Meldung 2 Benutzer ausgewählt und 2 Gruppen ausgewählt](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216).png" alt="Schaltfläche Zuweisen mit grünem Rahmen im Zuweisungsdialog von Azure Active Directory"><figcaption></figcaption></figure></div>

* Wechseln Sie zur Listenansicht \`Groups\` und suchen Sie die zugewiesenen Gruppen.

### SSO in Azure einrichten

Als Nächstes müssen Sie die Einrichtung von Single Sign-On in Azure abschließen.\\

* Klicken Sie im linken Bereich auf \`Single sign-on\`

![Linke Navigation der Unternehmensanwendung MyApplication mit dem Eintrag Einmaliges Anmelden](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klicken Sie auf \`SAML\`

![Seite Einmaliges Anmelden mit der Kachel SAML und dem Text Sichere und zuverlässige Authentifizierung für Anwendungen über das SAML-Protokoll](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klicken Sie auf \`Upload metadata file\`

![Seite SAML-basierte Anmeldung mit den Links Metadatendatei hochladen und Einmaliges Anmelden einrichten](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Laden Sie die DocBits-Datei **metadata.xml** hoch. Sie finden sie im Menü Settings unter **Integration** im Bereich **SSO Service Provider Settings** Ihres DocBits-Kontos.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="SSO-Dienstanbietereinstellungen in DocBits mit der Entitäts-ID, der SLO-URI und der SSO-URI sowie den Schaltflächen Zertifikat herunterladen und Metadaten herunterladen"><figcaption></figcaption></figure>

* Bearbeiten Sie die \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Seite Einmaliges Anmelden mit SAML einrichten mit dem Abschnitt Grundlegende SAML-Konfiguration und den Feldern Bezeichner Entitäts-ID, Antwort-URL, Anmelde-URL, Relay-Status und Abmelde-URL"><figcaption></figcaption></figure>

* Prüfen Sie, ob \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` und \`Logout URL\` richtig befüllt sind.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Grundlegende SAML-Konfiguration in Azure mit den Beschreibungstexten, dem Bezeichner Entitäts-ID auf die SAML-Metadaten-URL des Mandanten und der Antwort-URL als Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Laden Sie die neu erzeugte **Federation Metadata XML** herunter.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Abschnitt SAML-Signaturzertifikat mit dem Status Aktiv, dem Fingerabdruck, dem Ablaufdatum, der Benachrichtigungs-E-Mail und den Download-Links Zertifikat Rohdaten und Verbundmetadaten-XML"><figcaption></figcaption></figure>

* Laden Sie die Datei FederationMetadata.xml in den **Identity Service Provider Settings** Ihres DocBits-Kontos hoch, die Sie im Menü Settings unter **Integration** finden.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Einstellungen des Identitätsdienstanbieters in DocBits mit der Mandanten-ID, den Schaltflächen Datei hochladen und Importieren und dem Eintrag für die vorhandene Datei"><figcaption></figcaption></figure>
