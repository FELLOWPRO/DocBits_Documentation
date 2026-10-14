# O365 Tenant

## App registreren op Azure AD

<mark style="color:red;">**Opmerking**</mark>: De machtigingen kunnen autorisatie van een beheerder vereisen.

1. Meld u aan bij de [Azure Portal](https://portal.azure.com/) met uw inloggegevens.
2. Zoek en open Azure Active Directory (ook wel bekend als Azure AD) vanuit Azure-services.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Selecteer in de sectie **Manage** de optie **App registrations**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Klik in het scherm App registrations op **+ New registration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Het scherm **Register an application** verschijnt. Voer de gebruikersgerichte weergavenaam voor de App in bij **Name**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecteer een van de volgende accounttypen afhankelijk van uw behoeften:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Laat de optie **Redirect URI (optional)** zoals deze is.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Klik op **Register** om de App-registratie te voltooien. Dit brengt u terug naar het scherm van de nieuwe App.
9. Zoek in het App-scherm de **Application (client) ID**. Kopieer deze om te gebruiken bij het configureren van e-mailimport voor **DocBits**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Selecteer in het linkerpaneel **Certificates & secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Klik in het scherm **Certificates & secrets** op de knop **+ New client secret** onder de sectie **Client secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Klik in het dialoogvenster **Add a client secret** op de knop **Add**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Het wordt aanbevolen om een beschrijving in te vullen om dit geheim te identificeren tussen vele (op dit moment is de limiet 2 geheimen per App).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Opmerking**</mark>: Selecteer deze vervaldatum volgens uw bedrijfsbeleid. Zodra deze is verlopen, moet een nieuw client secret worden gemaakt en gespecificeerd voor elke e-mailconfiguratie waarin deze eerder werd gebruikt.

13. Het nieuw gegenereerde client secret zal zichtbaar zijn. Kopieer dit client secret om te gebruiken bij het configureren van e-mailimport voor DocBits.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Belangrijk:** Zorg ervoor dat u het client secret hebt gekopieerd, aangezien het client secret niet opnieuw wordt weergegeven zodra het is gesloten.

14. Selecteer **Authentication** in het linkerpaneel. Dit toont het scherm **Authentication** aan de rechterkant.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Klik in de sectie **Advanced settings** op **Yes** voor **Default client type**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Klik op **Save** om de wijzigingen te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecteer **API permissions** in het linkerpaneel. Dit toont het scherm API-machtigingen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Standaard is de machtiging **User.Read** van **Microsoft Graph** aanwezig, laat deze zoals deze is.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Opmerking**</mark>: Dit is een vereiste machtiging. Als deze machtiging niet beschikbaar is, voeg dan de machtiging toe met de hieronder vermelde stappen voor de machtiging **Mail.ReadWrite**.

19. Klik op **+ Add a permission**. Dit opent het paneel **Request API permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Klik op **Microsoft Graph**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Selecteer uit de twee subcategorieën **App Permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Typ **Mail.ReadWrite** in het zoekvak. Selecteer het selectievakje **Mail.ReadWrite** voor de machtiging.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Dit activeert de knop **Add permissions** onderaan het paneel. Klik op **Add permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Dit voegt de machtiging **Mail.ReadWrite** toe aan de lijst met **Configured permissions** voor de App.

<mark style="color:red;">**Opmerking**</mark>: Beheerdersrechten kunnen vereist zijn. De beheerder zal de App moeten autoriseren voor het gebruik van deze machtigingen. Eenmaal geautoriseerd, wordt de verleende status als volgt aangegeven:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
