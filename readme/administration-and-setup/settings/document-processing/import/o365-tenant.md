# O365 Tenant

## App auf Azure AD registrieren

<mark style="color:red;">**Hinweis**</mark>: Die Berechtigungen können eine Autorisierung durch einen Administrator erfordern.

1. Melden Sie sich mit Ihren Anmeldedaten beim [Azure Portal](https://portal.azure.com/) an.
2. Suchen Sie unter Azure-Diensten Azure Active Directory (auch bekannt als Azure AD) und öffnen Sie es.

![Seite des Azure-Portals mit dem Eintrag Azure Active Directory und der Dienstsuchleiste](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Wählen Sie im Abschnitt **Manage** die Option **App registrations**.

![Übersichtsseite von Azure Active Directory mit geöffnetem Manage-Menü links und hervorgehobenem Eintrag App registrations](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Klicken Sie im Bildschirm App registrations auf **+ New registration**.

![Bildschirm App registrations in Azure mit der Schaltfläche New registration in der Symbolleiste und der Liste der registrierten Apps](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Der Bildschirm **Register an application** wird angezeigt. Geben Sie den benutzerseitigen Anzeigenamen für die App unter **Name** ein.

![Bildschirm „Register an application“ im Azure Portal mit leerem Feld Name für die neue App](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Wählen Sie je nach Bedarf einen der folgenden Kontotypen aus:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![Bildschirm Register an application mit den Optionsfeldern für unterstützte Kontotypen für Organisationsverzeichnisse und persönliche Microsoft-Konten](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Lassen Sie die Option **Redirect URI (optional)** wie sie ist.

![Bildschirm Register an application mit unten unverändertem Abschnitt Redirect URI (optional)](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Klicken Sie auf **Register**, um die App-Registrierung abzuschließen. Dies bringt Sie zurück zum Bildschirm für die neue App.
9. Suchen Sie im App-Bildschirm die **Application (client) ID**. Kopieren Sie diese, um sie bei der Konfiguration des E-Mail-Imports für **DocBits** zu verwenden.

![Übersichtsseite der registrierten App mit dem Display name Ephesoft OAuth2 App und der Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Wählen Sie im linken Bereich **Certificates & secrets**:

![Übersichtsseite der registrierten App mit Certificates and secrets im Abschnitt Manage des linken Panels ausgewählt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Klicken Sie im Bildschirm **Certificates & secrets** auf die Schaltfläche **+ New client secret** im Abschnitt **Client secrets**:

![Bildschirm Certificates & secrets mit dem Abschnitt Client secrets und der Schaltfläche + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Klicken Sie im Dialogfeld **Add a client secret** auf die Schaltfläche **Add**:

![Dialog Add a client secret mit den Feldern Description und Expires und der Schaltfläche Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Es wird empfohlen, eine Beschreibung einzugeben, um dieses Secret unter vielen zu identifizieren (derzeit liegt das Limit bei 2 Secrets pro App).

![Liste der Client Secrets mit dem neuen Secret und den Spalten Beschreibung, Value und Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Hinweis**</mark>: Wählen Sie dieses Ablaufdatum gemäß Ihrer Unternehmensrichtlinie. Nach Ablauf muss ein neues Client Secret erstellt und für jede E-Mail-Konfiguration angegeben werden, in der es zuvor verwendet wurde.

13. Das neu generierte Client Secret wird sichtbar. Kopieren Sie dieses Client Secret, um es bei der Konfiguration des E-Mail-Imports für DocBits zu verwenden.

![Bereich Client secrets unter Certificates & secrets mit dem generierten Geheimniswert Value zum Kopieren bereit](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Wichtig:** Stellen Sie sicher, dass Sie das Client Secret kopiert haben, da das Client Secret nicht mehr angezeigt wird, sobald es geschlossen wurde.

14. Wählen Sie im linken Bereich **Authentication**. Dies zeigt den Bildschirm **Authentication** auf der rechten Seite an.

![Authentifizierungsansicht der App-Registrierung, im linken Bereich geöffnet, mit den Plattformeinstellungen auf der rechten Seite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Klicken Sie im Abschnitt **Advanced settings** auf **Yes** für **Default client type**.

![Abschnitt Advanced settings des Authentication-Bildschirms mit der Option Default client type auf Yes gesetzt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Klicken Sie auf **Save**, um die Änderungen zu bestätigen.

![Obere Leiste der App-Registrierung mit hervorgehobener Schaltfläche Save nach dem Aktivieren des Standard-Clienttyps](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Wählen Sie im linken Bereich **API permissions**. Dies zeigt den Bildschirm API permissions an.

![Über den linken Bereich geöffneter Bildschirm „API permissions“ mit den konfigurierten Berechtigungen für die App](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Standardmäßig ist die Berechtigung **User.Read** von **Microsoft Graph** vorhanden, lassen Sie diese wie sie ist.

![Liste der konfigurierten Berechtigungen mit der standardmäßigen delegierten Berechtigung User.Read für Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Hinweis**</mark>: Dies ist eine erforderliche Berechtigung. Wenn diese Berechtigung nicht verfügbar ist, fügen Sie die Berechtigung mit den unten für die Berechtigung **Mail.ReadWrite** genannten Schritten hinzu.

19. Klicken Sie auf **+ Add a permission**. Dies öffnet das Panel **Request API permissions**.

![Bereich Request API permissions mit Microsoft APIs, APIs my organization uses und dem Ablauf von + Add a permission](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Klicken Sie auf **Microsoft Graph**.

![Panel Request API permissions mit dem hervorgehobenen Microsoft Graph unter den häufig verwendeten Microsoft-APIs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Wählen Sie aus den zwei Unterkategorien **App Permissions**.

![Panel Request API permissions für Microsoft Graph mit den Optionen Delegated permissions und Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Geben Sie **Mail.ReadWrite** in das Suchfeld ein. Aktivieren Sie das Kontrollkästchen **Mail.ReadWrite** für die Berechtigung.

![Suchfeld für Anwendungsberechtigungen mit eingegebenem Mail.ReadWrite und aktivierter Checkbox der Berechtigung Mail.ReadWrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Dadurch wird die Schaltfläche **Add permissions** am unteren Rand des Panels aktiviert. Klicken Sie auf **Add permissions**.

![Panel Request API permissions mit der ausgewählten Berechtigung Mail.ReadWrite und der Schaltfläche Add permissions unten](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Dadurch wird die Berechtigung **Mail.ReadWrite** zur Liste der **Configured permissions** für die App hinzugefügt.

<mark style="color:red;">**Hinweis**</mark>: Administratorberechtigungen können erforderlich sein. Der Administrator muss die App für die Verwendung dieser Berechtigungen autorisieren. Nach der Autorisierung wird der gewährte Status wie folgt angezeigt:

![Liste der konfigurierten Berechtigungen mit hinzugefügter Anwendungsberechtigung Mail.ReadWrite und angezeigtem Erteilungsstatus](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
