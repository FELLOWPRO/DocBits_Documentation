# Integration & SSO

<figure><img src="../../../../.gitbook/assets/integration_sso.png" alt="Integration & SSO"><figcaption><p>Pagina Integration & SSO</p></figcaption></figure>

Op de pagina Integration & SSO beheert u API-sleutels voor programmatische toegang, organisatie-ID's en de configuratie van Single Sign-On (SSO).

## API Key

Beheer de API-sleutels die worden gebruikt voor programmatische toegang tot DocBits.

| Kolom | Beschrijving |
|--------|-------------|
| **Key** | De gemaskeerde waarde van de API-sleutel. Klik op het kopieerpictogram om de volledige sleutel te kopiëren. |
| **Name** | Een beschrijvende naam voor de sleutel. |
| **Expires** | Vervaldatum (of "Never"). |
| **Last Used** | Wanneer de sleutel voor het laatst is gebruikt. |
| **Status** | Active of Inactive. |
| **Actions** | Menu met drie puntjes om in te trekken of te verwijderen. |

Klik op **+ Create API Key** om een nieuwe sleutel te genereren.

## ID

Toont de identificatiegegevens van uw organisatie:

| Veld | Beschrijving |
|-------|-------------|
| **Org ID** | De unieke identificatie van uw organisatie. |
| **Sub Org ID** | De ID van de momenteel geselecteerde suborganisatie. |

## SSO Service Provider Settings

De DocBits SSO-configuratiewaarden die u nodig hebt bij het instellen van uw Identity Provider:

| Veld | Beschrijving |
|-------|-------------|
| **Entity ID** | De SAML-metadata-URL voor DocBits. |
| **SLO URL** | Single Logout-URL. |
| **SSO URL** | Assertion Consumer Service-URL. |

U kunt ook **Download Certificate** en **Download Metadata** gebruiken voor de configuratie van uw IdP.

## Identity Service Provider Settings

Configureer uw externe Identity Provider (IdP):

| Veld | Beschrijving |
|-------|-------------|
| **Tenant ID** | De tenant-ID van uw IdP. |
| **Upload file** | Upload het XML-metadatabestand van uw IdP. |

Klik op **Configure** om uw IdP-instellingen op te slaan.

* **Verhoogde efficiëntie:** Integratie met andere tools en diensten kan workflows stroomlijnen en de efficiëntie verhogen. Documenten kunnen bijvoorbeeld automatisch worden uitgewisseld tussen Docbits en een CRM-systeem, waardoor handmatige invoer wordt verminderd en de productiviteit toeneemt.
* **Gegevensconsistentie:** Integratie maakt het mogelijk om gegevens naadloos uit te wisselen tussen verschillende systemen, wat de gegevensconsistentie en nauwkeurigheid verbetert. Dit voorkomt inconsistenties of dubbele gegevensinvoer die tot fouten kunnen leiden.
* **Realtime updates:** Integratie maakt realtime updates mogelijk tussen verschillende platforms, zodat gebruikers altijd de meest actuele informatie hebben. Dit is vooral belangrijk voor kritieke bedrijfsprocessen die realtime informatie vereisen.
* **Taakautomatisering:** Integratie maakt het mogelijk om routinetaken te automatiseren, wat tijd en middelen bespaart. Meldingen kunnen bijvoorbeeld automatisch worden geactiveerd wanneer een bepaalde gebeurtenis zich in een ander systeem voordoet, zonder dat handmatige tussenkomst nodig is.
* **Verbeterde gebruikerservaring:** Een goed geconfigureerde integratie zorgt voor een naadloze gebruikerservaring, omdat gebruikers niet tussen verschillende systemen hoeven te schakelen om relevante informatie te vinden. Dit verbetert de tevredenheid van gebruikers en draagt bij aan de efficiëntie.

Om de integratie-instellingen goed te configureren, is het belangrijk om de vereisten van de organisatie te begrijpen en ervoor te zorgen dat de integratie naadloos aansluit op bestaande workflows en processen. Dit vereist grondige planning, configuratie en monitoring van de integratie, zodat deze soepel werkt en de gewenste waarde levert.
