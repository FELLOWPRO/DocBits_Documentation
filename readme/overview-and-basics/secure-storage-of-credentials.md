---
description: Wachtwoordhashes, opslag van API-sleutels, TLS, toegang tot inloggegevens en accountherstel in DocBits.
---

# Veilige opslag van inloggegevens

DocBits behandelt inlogwachtwoorden, DocBits-API-sleutels, accountgegevens en inloggegevens voor gekoppelde systemen volgens hun doel. Deze pagina beschrijft de bescherming en het herstel van toegang voor elke categorie.

## Inlogwachtwoorden

DocBits slaat inlogwachtwoorden op als **eenrichtingshashes met salt**. Bij het aanmelden wordt het ingevoerde wachtwoord gecontroleerd aan de hand van de opgeslagen hash. Het oorspronkelijke wachtwoord wordt niet opgeslagen in een vorm die kan worden ontsleuteld en teruggehaald.

Beheerders en DocBits-support kunnen het bestaande wachtwoord in leesbare vorm dus niet uit de opgeslagen wachtwoordhash ophalen. Als een gebruiker het wachtwoord vergeet, moet het worden gereset om weer met een wachtwoord te kunnen inloggen.

### Wachtwoord resetten

1. Selecteer **Wachtwoord vergeten** op het inlogscherm.
2. Voer het e-mailadres in dat aan het account is gekoppeld.
3. Open de resetlink die naar dat adres is verzonden.
4. Stel een nieuw wachtwoord in en log daarmee in.

Resetlinks verlopen. Vraag een nieuwe link aan als de vorige is verlopen. Met de procedure stelt u een nieuw wachtwoord in; het oude wordt niet getoond. Zie [Toegang krijgen en inloggen](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md) voor de volledige instructies.

Accounts waarvoor SSO of een passkey is ingesteld, kunnen die alternatieve inlogmethode gebruiken. Bij SSO verzorgt de identiteitsprovider het wachtwoordherstel. Zie [Tweefactorauthenticatie](two-factor-authentication.md).

## DocBits-API-sleutels

Sleutels die via **API-sleutelbeheer** worden aangemaakt, worden slechts één keer volledig getoond: bij het aanmaken. DocBits slaat een eenrichtingshash van de sleutel en een kort herkenningsvoorvoegsel op. Het voorvoegsel en de metadata blijven zichtbaar in de beheerlijst; de oorspronkelijke volledige sleutel kan niet uit de hash worden teruggehaald.

Beheerders en DocBits-support kunnen de volledige sleutel na het aanmaken niet opnieuw opzoeken. Als een sleutel verloren gaat, trek deze dan in en maak een vervangende sleutel aan. Elke sleutel kan een vervaldatum hebben en afzonderlijk worden ingetrokken. Zie [API-sleutelbeheer](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Accountgegevens en inloggegevens voor gekoppelde systemen

Namen, e-mailadressen, rollen en accountstatus zijn accountgegevens die bevoegde organisatiebeheerders kunnen bekijken en beheren. Ze staan los van het geheim dat voor authenticatie wordt gebruikt. Zie [Gebruikers](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Inloggegevens voor gekoppelde systemen, zoals een ERP-serviceaccount, een mailbox of een SFTP-server, staan ook los van een DocBits-inlogwachtwoord of een door DocBits uitgegeven API-sleutel. Een connector kan het bruikbare geheim nodig hebben om zich bij het externe systeem te authenticeren. De opslag en toegangscontroles moeten daarom per connector worden beoordeeld.

Dat een inlogwachtwoord of gehashte DocBits-API-sleutel niet kan worden teruggehaald, betekent **niet** dat alle accountgegevens of integratiegeheimen ontoegankelijk zijn voor de leverancier. Iedere toezegging over toegang van medewerkers tot inloggegevens voor integraties vereist bevestiging van de betreffende operationele toegangscontroles.

## Versleuteling tijdens de overdracht

De onderstaande openbare DocBits-eindpunten ondersteunen **TLS 1.2 en TLS 1.3** via HTTPS. Controles op **16 oktober 2026** bevestigden dat TLS 1.0 en TLS 1.1 werden geweigerd.

| Eindpunt | Doel | Geverifieerde TLS-versies |
| --- | --- | --- |
| `app.docbits.com` | Webapplicatie | TLS 1.2 en TLS 1.3 |
| `auth.docbits.com` | Authenticatiedienst | TLS 1.2 en TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 en TLS 1.3 |

### Welke soorten versleuteling worden tijdens de overdracht ondersteund?

| Vraag | Antwoord voor de bovenstaande openbare eindpunten |
| --- | --- |
| Wordt TLS 1.1 ondersteund? | **Nee.** Verbindingen met TLS 1.1 worden geweigerd. |
| Wordt TLS 1.2 ondersteund? | **Ja.** |
| Wordt TLS 1.3 ondersteund? | **Ja.** |

De volgende versleutelingsmethoden zijn op 16 oktober 2026 met succes overeengekomen op **alle drie de eindpunten**, tijdens tests waarbij het certificaat werd gevalideerd:

| Versleutelingsmethode | Lengte van de symmetrische sleutel | Geverifieerde TLS-versies |
| --- | --- | --- |
| AES-128-GCM | 128 bits | TLS 1.2 en TLS 1.3 |
| AES-256-GCM | 256 bits | TLS 1.2 en TLS 1.3 |
| ChaCha20-Poly1305 | 256 bits | TLS 1.3 |

Deze methoden bieden geauthenticeerde versleuteling en beschermen de vertrouwelijkheid en integriteit van gegevens tijdens de overdracht. De overeengekomen methode hangt af van de mogelijkheden en configuratie van client en server. De genoemde bitlengtes betreffen de symmetrische sleutels voor gegevensversleuteling, onafhankelijk van de sleutellengtes van certificaten. De geteste TLS 1.2-ciphersuites gebruiken ECDHE voor de uitwisseling van tijdelijke sleutels.

Deze verificatie dekt verbindingen met deze openbare eindpunten, ook wanneer andere servers ermee verbinden. Ze stelt niet de protocol- of versleutelingsinstellingen vast van elke interne dienstverbinding, databaseverbinding, elk regionaal eindpunt of elke externe integratie. Die verbindingen vereisen bevestiging voor de betreffende omgeving en integratie.

## Versleuteling van opgeslagen accountgegevens

Het hashen van wachtwoorden en API-sleutels is een andere maatregel dan het versleutelen van databases, opslagvolumes, objecten en back-ups. De beschreven maatregelen tonen niet aan dat elke gebruikersnaam, elk accountveld of elk integratiegeheim afzonderlijk wordt versleuteld, of dat alle opgeslagen gegevens een bepaald versleutelingsalgoritme gebruiken.

Voor een eis die alle accountgegevens van klanten omvat, vraagt u FELLOWPRO AG om een verklaring voor de specifieke omgeving over de betrokken gegevensopslag en back-ups, versleutelingsmethoden, sleutelbeheer en toegang van medewerkers. Een cloud- of serverless-hostingmodel op zichzelf toont deze eigenschappen niet aan.

## Antwoord op een beveiligingsvragenlijst van een klant

De volgende tekst beschrijft de bevestigde reikwijdte:

> DocBits-inlogwachtwoorden worden opgeslagen als eenrichtingshashes met salt. Beheerders en DocBits-support kunnen het oorspronkelijke leesbare wachtwoord niet uit de opgeslagen hash ophalen. Gebruikers die hun wachtwoord vergeten, moeten via de resetprocedure per e-mail een nieuw wachtwoord instellen om weer met een wachtwoord te kunnen inloggen. Ingestelde SSO- of passkey-methoden bieden alternatieve inlogmogelijkheden.
>
> Sleutels die via DocBits-API-sleutelbeheer worden aangemaakt, worden slechts één keer getoond en als eenrichtingshashes opgeslagen. Beheerders en DocBits-support kunnen de volledige sleutel daarna niet meer ophalen. Verloren sleutels moeten worden ingetrokken en vervangen.
>
> De hierboven genoemde openbare DocBits-eindpunten voor de webapplicatie, authenticatie en API ondersteunen HTTPS met TLS 1.2 en TLS 1.3; TLS 1.0 en TLS 1.1 werden geweigerd bij de controles van 16 oktober 2026. Geverifieerde methoden zijn AES-128-GCM met 128 bits en AES-256-GCM met 256 bits bij TLS 1.2 en TLS 1.3, en ChaCha20-Poly1305 met 256 bits bij TLS 1.3. Deze verklaring geldt voor verbindingen met die eindpunten. Versleuteling van alle opgeslagen accountgegevens en back-ups, bescherming van elke interne serververbinding en toegang van medewerkers tot inloggegevens voor externe integraties vereisen afzonderlijke bevestiging voor de betreffende omgeving.
