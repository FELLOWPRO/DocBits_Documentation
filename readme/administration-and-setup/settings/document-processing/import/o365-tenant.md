# O365 Tenant

## App registreren op Azure AD

<mark style="color:red;">**Opmerking**</mark>: De machtigingen kunnen autorisatie van een beheerder vereisen.

1. Meld u aan bij de [Azure Portal](https://portal.azure.com/) met uw inloggegevens.
2. Zoek en open Azure Active Directory (ook wel bekend als Azure AD) vanuit Azure-services.

![Item Azure Active Directory in de zoekbalk en de servicelijst van de Azure-portal](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Selecteer in de sectie **Manage** de optie **App registrations**.

![Overzichtspagina van Azure Active Directory met de sectie Manage en het item App registrations in het linkermenu](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Klik in het scherm App registrations op **+ New registration**.

![Pagina App registrations met de knop + New registration in de werkbalk](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Het scherm **Register an application** verschijnt. Voer de gebruikersgerichte weergavenaam voor de App in bij **Name**.

![Formulier Register an application met het veld Name en de helptekst voor de weergavenaam](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecteer een van de volgende accounttypen afhankelijk van uw behoeften:

* **Accounts in elke organisatiemap (elke Azure AD map Multitenant) en persoonlijke Microsoft-accounts (bijvoorbeeld Skype, Xbox)**
* **Accounts in elke organisatiemap (elke Azure AD map Multitenant)**

![Lijst Supported account types met de opties voor één tenant, meerdere tenants en persoonlijke Microsoft-accounts](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Laat de optie **Redirect URI (optional)** zoals deze is.

![Formulier Register an application met de ondersteunde accounttypen en de gekozen optie voor meerdere tenants](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Klik op **Register** om de App-registratie te voltooien. Dit brengt u terug naar het scherm van de nieuwe App.
9. Zoek in het App-scherm de **Application (client) ID**. Kopieer deze om te gebruiken bij het configureren van e-mailimport voor **DocBits**.

![Sectie Redirect URI (optional) van het registratieformulier en de knop Register eronder](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Selecteer in het linkerpaneel **Certificates & secrets**:

![Overzichtspagina van de geregistreerde toepassing met Display name, Application (client) ID en de knoppen Delete en Endpoints](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Klik in het scherm **Certificates & secrets** op de knop **+ New client secret** onder de sectie **Client secrets**:

![Item Certificates & secrets in het linkermenu van de geregistreerde toepassing](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Klik in het dialoogvenster **Add a client secret** op de knop **Add**:

![Sectie Client secrets met de beschrijving en de melding dat er nog geen clientgeheimen zijn aangemaakt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Het wordt aanbevolen om een beschrijving in te vullen om dit geheim te identificeren tussen vele (op dit moment is de limiet 2 geheimen per App).

![Dialoogvenster Add a client secret met het veld Description en de verloopopties 1 jaar, 2 jaar en nooit](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Opmerking**</mark>: Selecteer deze vervaldatum volgens uw bedrijfsbeleid. Zodra deze is verlopen, moet een nieuw client secret worden gemaakt en gespecificeerd voor elke e-mailconfiguratie waarin deze eerder werd gebruikt.

13. Het nieuw gegenereerde client secret zal zichtbaar zijn. Kopieer dit client secret om te gebruiken bij het configureren van e-mailimport voor DocBits.

![Tabel Client secrets met het aangemaakte geheim, de vervaldatum en het kopieerpictogram naast de waarde](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Belangrijk:** Zorg ervoor dat u het client secret hebt gekopieerd, aangezien het client secret niet opnieuw wordt weergegeven zodra het is gesloten.

14. Selecteer **Authentication** in het linkerpaneel. Dit toont het scherm **Authentication** aan de rechterkant.

![Item Authentication in het linkermenu van de geregistreerde toepassing](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Klik in de sectie **Advanced settings** op **Yes** voor **Default client type**.

![Pagina Authentication, sectie Advanced settings, met Default client type op Yes voor een openbare client](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Klik op **Save** om de wijzigingen te bevestigen.

![Pagina Authentication met de knoppen Save en Discard in de werkbalk](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecteer **API permissions** in het linkerpaneel. Dit toont het scherm API-machtigingen.

![Item API permissions in het linkermenu van de geregistreerde toepassing](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Standaard is de machtiging **User.Read** van **Microsoft Graph** aanwezig, laat deze zoals deze is.

![Tabel API permissions met de gedelegeerde machtiging User.Read van Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Opmerking**</mark>: Dit is een vereiste machtiging. Als deze machtiging niet beschikbaar is, voeg dan de machtiging toe met de hieronder vermelde stappen voor de machtiging **Mail.ReadWrite**.

19. Klik op **+ Add a permission**. Dit opent het paneel **Request API permissions**.

![Paneel Configured permissions met de knop + Add a permission en een lege lijst met machtigingen](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Klik op **Microsoft Graph**.

![Paneel Request API permissions met het item Microsoft Graph bij de veelgebruikte Microsoft-API's](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Selecteer uit de twee subcategorieën **App Permissions**.

![Paneel met Microsoft Graph-machtigingen en de keuze tussen Delegated permissions en Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Typ **Mail.ReadWrite** in het zoekvak. Selecteer het selectievakje **Mail.ReadWrite** voor de machtiging.

![Paneel Request API permissions met Mail.ReadWrite in de zoekbalk en de bijbehorende Mail-machtiging](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Dit activeert de knop **Add permissions** onderaan het paneel. Klik op **Add permissions**.

![Paneel Request API permissions met het selectievakje Mail.ReadWrite aangevinkt en de knop Add permissions actief](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Dit voegt de machtiging **Mail.ReadWrite** toe aan de lijst met **Configured permissions** voor de App.

<mark style="color:red;">**Opmerking**</mark>: Beheerdersrechten kunnen vereist zijn. De beheerder zal de App moeten autoriseren voor het gebruik van deze machtigingen. Eenmaal geautoriseerd, wordt de verleende status als volgt aangegeven:

![Paneel Configured permissions met de machtiging Mail.ReadWrite en de knop Grant admin consent voor de tenant](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
