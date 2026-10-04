# Bedrijfsinformatie

<figure><img src="../../../../.gitbook/assets/company_information_nl.png" alt="Het formulier Bedrijfsinformatie in de DocBits Sandbox-testorganisatie in het Nederlands"><figcaption><p>Bedrijfsinformatie: bewerk de bedrijfsnaam, het adres, de juridische identificatiegegevens en de contactgegevens en selecteer daarna Opslaan.</p></figcaption></figure>

Op de pagina Bedrijfsinformatie beheert u het bedrijfsprofiel, de voorkeuren en de abonnementsgegevens. De pagina is onderverdeeld in de volgende secties:

## Bedrijfsinformatie

Deze sectie bevat uw belangrijkste bedrijfsgegevens, gegroepeerd in vier gebieden:

### Bedrijfsidentiteit

* **Naam** *(verplicht)*: De juridische naam van uw bedrijf.

### Adres

* **Straat + Nummer**: Het adres van uw bedrijf.
* **Postcode**: De ZIP- of postcode.
* **Stad**: De naam van de stad.
* **Land**: Selecteer uw land in de vervolgkeuzelijst.

### Juridische informatie

* **Bedrijfs-ID**: Een unieke identificatie voor uw bedrijf, gebruikt voor integraties en interne referenties.
* **Belastingnummer**: Uw belastingidentificatienummer voor financiële rapportage.
* **Handelsregister-ID**: Uw handelsregisternummer voor juridische documentatie.

### Contact

* **Officieel telefoonnummer van het bedrijf**: Het primaire telefoonnummer van uw bedrijf.
* **E-mail**: Het belangrijkste e-mailadres voor officiële communicatie.

Klik na het invoeren of bijwerken van velden op **Opslaan** om de wijzigingen toe te passen. De **?**-pictogrammen naast de juridische identificatiegegevens tonen extra velduitleg. Selecteer de sectiekopt om het formulier uit te vouwen of in te vouwen.

## E-maildomeinen

Organisatiebeheerders openen **Instellingen → Bedrijfsinformatie → E-maildomeinen** om de domeinen te beheren die worden gebruikt voor de automatische organisatie-toewijzing. Wanneer iemand inlogt met Microsoft of Google en nog geen lid is van een organisatie, kan DocBits die persoon aan deze organisatie toewijzen als zijn of haar e-mailadres een van de vermelde domeinen gebruikt. Een domein kan slechts aan één organisatie worden toegewezen.

<figure><img src="../../../../.gitbook/assets/company_email_domains_nl.png" alt="De uitgevouwen sectie E-maildomeinen met een lege domeinenlijst, een invoerveld en de knop Domein toevoegen"><figcaption><p>De Nederlandstalige sectie E-maildomeinen voordat een domein wordt toegevoegd. Voer een bedrijfsdomein in en selecteer Domein toevoegen.</p></figcaption></figure>

Voer alleen het domein in, bijvoorbeeld `example.com`, in het invoerveld en selecteer **Domein toevoegen** of druk op Enter. Het eerste domein wordt het primaire domein. Als er meer domeinen zijn vermeld, gebruikt u **Primair maken** bij een andere rij om dit te wijzigen, of het prullenbak-pictogram om een domein te verwijderen. Foutmeldingen, zoals een ongeldig domein, een persoonlijke e-mailprovider of een domein dat ergens anders is toegewezen, verschijnen onder het invoerveld. **Er zijn nog geen domeinen toegewezen** betekent dat deze organisatie geen domeinregel heeft.

Controleer vóór het toevoegen van een domein welke organisatie nieuwe aanmeldingen moet ontvangen. Om bestaande lidmaatschappen te beheren, gaat u verder met [Gebruikers](../groups-users-and-permissions/users/README.md).

## Bedrijfsvoorkeuren

Stel bedrijfsbrede standaardinstellingen in:

* **Datumnotatie**: Kies hoe datums in DocBits worden weergegeven (bijvoorbeeld `%m/%d/%Y`, `%d.%m.%Y`).
* **Bedragnotatie**: Selecteer het nummerformaat voor bedragen (bijvoorbeeld Deutsch voor `1.000,00`, English voor `1,000.00`).
* **Infovenster nieuwe versie**: Schakel in of gebruikers een melding zien wanneer er een nieuwe DocBits-versie verschijnt.

Klik na het aanbrengen van wijzigingen op **Opslaan**.

## App-kleur

Pas de primaire kleur van de DocBits-interface aan. Dit is handig om verschillende omgevingen visueel van elkaar te onderscheiden (bijvoorbeeld dev en productie).

* **Kleur**: Voer een hex-kleurcode in (bijvoorbeeld `#2388AE`) of gebruik de kleurkiezer.
* Klik op **Opslaan** om toe te passen of op **Resetten** om de standaardkleur te herstellen.

## Abonnementsplan

Bekijk uw actieve abonnementsplannen en hun gegevens:

* **Plannaam**: De naam van elk actief plan (bijvoorbeeld DocBits, DocFlow Users, DocSearch).
* **Resterende dagen**: Het aantal dagen tot het plan verloopt.
* **Startdatum / einddatum**: De abonnementsperiode.
* **Aantal gebruikers**: Het totale aantal gebruikers in uw organisatie.
* **Aantal suborganisaties**: Het aantal ingestelde suborganisaties.
* **Aantal leveranciers**: Het aantal geregistreerde leveranciers.

## Abonnementsgebruik

Houd het maandelijkse token- en workflowgebruik in de gaten:

| Kolom | Beschrijving |
|--------|-------------|
| **Type** | Het gebruikstype (Document of Workflow). |
| **Van / Tot** | De datums van de factureringsperiode. |
| **Gebruikte tokens** | Aantal tokens dat in de huidige periode is verbruikt. |
| **Resterende tokens** | Tokens die in de huidige periode nog beschikbaar zijn. |

Gebruik de knop **Selecteren** om op specifieke datumbereiken te filteren.
