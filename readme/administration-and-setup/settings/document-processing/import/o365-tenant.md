# O365 Tenant

## App registreren op Azure AD

<mark style="color:red;">**Opmerking**</mark>: De machtigingen kunnen autorisatie van een beheerder vereisen.

1. Meld u aan bij de [Azure Portal](https://portal.azure.com/) met uw inloggegevens.
2. Zoek en open Azure Active Directory (ook wel bekend als Azure AD) vanuit Azure-services.

![Pagina van de Azure-portal met het item Azure Active Directory en de serviczoekbalk](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Selecteer in de sectie **Manage** de optie **App registrations**.

![Overzichtspagina van Azure Active Directory met het menu Manage links open en App registrations gemarkeerd](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Klik in het scherm App registrations op **+ New registration**.

![Scherm App registrations in Azure met de knop New registration in de werkbalk en de lijst met geregistreerde apps](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Het scherm **Register an application** verschijnt. Voer de gebruikersgerichte weergavenaam voor de App in bij **Name**.

![Scherm Register an application in Azure Portal met een leeg veld Name voor de nieuwe app](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecteer een van de volgende accounttypen afhankelijk van uw behoeften:

* **Accounts in elke organisatiemap (elke Azure AD map Multitenant) en persoonlijke Microsoft-accounts (bijvoorbeeld Skype, Xbox)**
* **Accounts in elke organisatiemap (elke Azure AD map Multitenant)**

![Scherm Register an application met de keuzerondjes voor het ondersteunde accounttype voor organisatorische mappen en persoonlijke Microsoft-accounts](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Laat de optie **Redirect URI (optional)** zoals deze is.

![Scherm Register an application met onderaan de ongewijzigde sectie Redirect URI (optional)](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Klik op **Register** om de App-registratie te voltooien. Dit brengt u terug naar het scherm van de nieuwe App.
9. Zoek in het App-scherm de **Application (client) ID**. Kopieer deze om te gebruiken bij het configureren van e-mailimport voor **DocBits**.

![Overzichtspagina van de geregistreerde app met de Display name Ephesoft OAuth2 App en de Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Selecteer in het linkerpaneel **Certificates & secrets**:

![Overzichtspagina van de geregistreerde app met Certificates and secrets geselecteerd in de sectie Manage van het linkerpaneel](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Klik in het scherm **Certificates & secrets** op de knop **+ New client secret** onder de sectie **Client secrets**:

![Scherm Certificates & secrets met de sectie Client secrets en de knop + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Klik in het dialoogvenster **Add a client secret** op de knop **Add**:

![Dialoogvenster Add a client secret met de velden Description en Expires en de knop Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Het wordt aanbevolen om een beschrijving in te vullen om dit geheim te identificeren tussen vele (op dit moment is de limiet 2 geheimen per App).

![Lijst met client secrets met het nieuwe secret en de kolommen beschrijving, Value en Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Opmerking**</mark>: Selecteer deze vervaldatum volgens uw bedrijfsbeleid. Zodra deze is verlopen, moet een nieuw client secret worden gemaakt en gespecificeerd voor elke e-mailconfiguratie waarin deze eerder werd gebruikt.

13. Het nieuw gegenereerde client secret zal zichtbaar zijn. Kopieer dit client secret om te gebruiken bij het configureren van e-mailimport voor DocBits.

![Sectie Client secrets van Certificates & secrets met de gegenereerde geheime waarde Value klaar om te kopiëren](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Belangrijk:** Zorg ervoor dat u het client secret hebt gekopieerd, aangezien het client secret niet opnieuw wordt weergegeven zodra het is gesloten.

14. Selecteer **Authentication** in het linkerpaneel. Dit toont het scherm **Authentication** aan de rechterkant.

![Verificatiescherm van de app-registratie geopend vanuit het linkerpaneel met de platforminstellingen rechts](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Klik in de sectie **Advanced settings** op **Yes** voor **Default client type**.

![Sectie Advanced settings van het Authentication-scherm met de optie Default client type ingesteld op Yes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Klik op **Save** om de wijzigingen te bevestigen.

![Bovenbalk van de app-registratie met de knop Save gemarkeerd na het inschakelen van het standaard clienttype](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecteer **API permissions** in het linkerpaneel. Dit toont het scherm API-machtigingen.

![Vanuit het linkerpaneel geopend scherm API permissions met de geconfigureerde machtigingen voor de app](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Standaard is de machtiging **User.Read** van **Microsoft Graph** aanwezig, laat deze zoals deze is.

![Lijst met geconfigureerde machtigingen met de standaard gedelegeerde machtiging User.Read voor Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Opmerking**</mark>: Dit is een vereiste machtiging. Als deze machtiging niet beschikbaar is, voeg dan de machtiging toe met de hieronder vermelde stappen voor de machtiging **Mail.ReadWrite**.

19. Klik op **+ Add a permission**. Dit opent het paneel **Request API permissions**.

![Deelvenster Request API permissions met Microsoft APIs, APIs my organization uses en de + Add a permission-flow](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Klik op **Microsoft Graph**.

![Paneel Request API permissions met Microsoft Graph gemarkeerd tussen de veelgebruikte Microsoft-API's](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Selecteer uit de twee subcategorieën **App Permissions**.

![Paneel Request API permissions voor Microsoft Graph met de opties Delegated permissions en Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Typ **Mail.ReadWrite** in het zoekvak. Selecteer het selectievakje **Mail.ReadWrite** voor de machtiging.

![Zoekvak voor toepassingsmachtigingen met getypte Mail.ReadWrite en het aangevinkte selectievakje van de machtiging Mail.ReadWrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Dit activeert de knop **Add permissions** onderaan het paneel. Klik op **Add permissions**.

![Paneel Request API permissions met de geselecteerde machtiging Mail.ReadWrite en de knop Add permissions onderaan](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Dit voegt de machtiging **Mail.ReadWrite** toe aan de lijst met **Configured permissions** voor de App.

<mark style="color:red;">**Opmerking**</mark>: Beheerdersrechten kunnen vereist zijn. De beheerder zal de App moeten autoriseren voor het gebruik van deze machtigingen. Eenmaal geautoriseerd, wordt de verleende status als volgt aangegeven:

![Lijst met geconfigureerde machtigingen met de toegevoegde applicatiemachtiging Mail.ReadWrite en de weergegeven verleende status](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
