---
description: DocBits met uw Microsoft-account gebruiken zonder een afzonderlijk wachtwoord
---

# Azure-SSO

### SAML-SSO aanmaken in Azure AD

Voer de volgende stappen uit om SAML-SSO toe te voegen in Azure AD:

*   Open in Azure de console \`Azure Active Directory\`.

    ![Startpagina van de Azure-portal met Azure Active Directory bij de favorieten in de linkernavigatie](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Klik in het linkerpaneel op \`Enterprise applications\`.

![Linkernavigatie van Azure Active Directory met de groep Beheren en het item Bedrijfstoepassingen](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Klik op \`+ New application\`.

<figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_new_app_2.png" alt="Pagina Bedrijfstoepassingen van Azure Active Directory met de lijst Alle toepassingen en de knop Nieuwe toepassing"><figcaption></figcaption></figure>

* Klik op \`+ Create your own application\`.

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_create_own_app_2.png" alt="Venster Azure AD-galerie verkennen met de knoppen Eigen toepassing maken en Nieuwe galerij-app aanvragen en het zoekveld Toepassing zoeken"><figcaption></figcaption></figure></div>

* Voer een naam voor uw toepassing in. Behoud de overige standaardkeuzes.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Venster Eigen toepassing maken met de naam MyApplication en de gekozen optie Een andere toepassing integreren die u niet in de galerij vindt"><figcaption></figcaption></figure>

* Klik op \`Create\`.

### Gebruikers toewijzen aan de SSO-configuratie

Wijs vervolgens gebruikers of groepen toe aan de SSO-configuratie.

**Belangrijk**: maak eerst gebruikers en groepen aan in Azure AD. Als die nog ontbreken, maakt u ze aan voordat u doorgaat.

* Klik onder \`Getting Started\` op \`Assign Users and Groups\`.
* Klik op \`+ Add user\`.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Pagina Gebruikers en groepen van de toepassing MyApplication met de knoppen Gebruiker toevoegen, Bewerken, Verwijderen en Bijwerken en de melding Geen toepassingstoewijzingen gevonden" width="563"><figcaption></figcaption></figure>

* Selecteer de gebruikers en groepen die u aan deze SSO-configuratie wilt toewijzen. Deze gebruikers kunnen zich met SSO aanmelden bij DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Selectiepaneel voor gebruikers met meerdere gebruikers in de lijst en de sectie Geselecteerd"><figcaption></figcaption></figure>

* Klik op \`Select\`.
* Klik op \`Assign\` wanneer de selectie klopt.

![Venster Toewijzing toevoegen van de tenant chimdustries met de melding 2 gebruikers geselecteerd en 2 groepen geselecteerd](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_groups.png" alt="Knop Toewijzen met een groene rand in het toewijzingsvenster van Azure Active Directory"><figcaption></figcaption></figure></div>

* Open de lijstweergave \`Groups\` en zoek de toegewezen groepen.

### SSO instellen in Azure

Voltooi vervolgens de configuratie voor eenmalige aanmelding in Azure.\\

* Klik in het linkerpaneel op \`Single sign-on\`.

![Linkernavigatie van de bedrijfstoepassing MyApplication met het item Eenmalige aanmelding](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Klik op \`SAML\`.

![Pagina Eenmalige aanmelding met de tegel SAML en de tekst Veilige en betrouwbare verificatie voor toepassingen via het SAML-protocol](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Klik op \`Upload metadata file\`.

![Pagina Aanmelding op basis van SAML met de koppelingen Metadatabestand uploaden en Eenmalige aanmelding instellen](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload het DocBits-bestand **metadata.xml**. U vindt dit in uw DocBits-account in het instellingenmenu **Integration**, onder **SSO Service Provider Settings**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Instellingen van de SSO-serviceprovider in DocBits met de Entity ID, de SLO-URI en de SSO-URI en de knoppen Certificaat downloaden en Metagegevens downloaden"><figcaption></figcaption></figure>

* Bewerk \`Basic SAML Configuration\`.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Pagina Eenmalige aanmelding met SAML instellen met de sectie Basisconfiguratie voor SAML en de velden Id Entiteits-ID, Antwoord-URL, Aanmeldings-URL, Relaystatus en Afmeldings-URL"><figcaption></figcaption></figure>

* Controleer of \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` en \`Logout URL\` correct zijn ingevuld.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Basisconfiguratie voor SAML in Azure met de beschrijvingsteksten, de Id Entiteits-ID ingesteld op de SAML-metagegevens-URL van de tenant en de Antwoord-URL als Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Download het nieuw gegenereerde bestand **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sectie SAML-ondertekeningscertificaat met de status Actief, de vingerafdruk, de vervaldatum, het meldings-e-mailadres en de downloadkoppelingen Certificaat onbewerkt en Federatiemetagegevens-XML"><figcaption></figcaption></figure>

* Upload FederationMetadata.xml naar **Identity Service Provider Settings** in uw DocBits-account, in het instellingenmenu **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Instellingen van de identiteitsserviceprovider in DocBits met de Tenant-ID, de knoppen Bestand uploaden en Importeren en de vermelding van het bestaande bestand"><figcaption></figcaption></figure>
