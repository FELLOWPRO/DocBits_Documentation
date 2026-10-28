# Gegevensopslag, bewaartermijnen en verwijdering

Uw gegevens zijn bij DocBits in goede handen. Wij laten DocBits draaien in twee regio's, **Frankfurt am Main (EU)** en **San Francisco (VS)**, en u bepaalt in uw instellingen hoe lang documenten bij ons blijven. Deze pagina behandelt opslaglocaties, bewaartermijnen en verwijdering.

**Documentatie per: 28 oktober 2026.**

## In één oogopslag

- **U kiest de regio:** Frankfurt voor klanten in de EU, San Francisco voor klanten in de VS.
- **Uw gegevens blijven in uw regio.** EU-gegevens worden gehost in Frankfurt, VS-gegevens in San Francisco. Gegevens worden niet tussen regio's gemengd.
- **U bepaalt hoe lang uw documenten worden bewaard** onder **Document Processing → Verloop van documenten** ([naar de instelling](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Tijdelijke OCR-bestanden** worden na 90 minuten automatisch verwijderd.
- **Wij helpen u graag:** ons team beantwoordt vragen en verwijderingsverzoeken via **compliance@fellowpro.com**.

## Waar worden uw gegevens opgeslagen?

| Regio | Voor wie | Locatie | Gebruikte diensten |
| --- | --- | --- | --- |
| **EU** | Alle klanten in de EU | **Frankfurt am Main, Duitsland** | DigitalOcean Kubernetes (regio `fra1`) met beheerde PostgreSQL-, OpenSearch- en Valkey-databases (`fra1`), plus DigitalOcean Spaces voor bestandsopslag |
| **VS** | Klanten in de VS | **San Francisco, VS** | DigitalOcean Kubernetes (regio `sfo2`) met beheerde PostgreSQL-, OpenSearch- en Valkey-databases (`sfo2`) |

**Back-ups in de EU:** Frankfurt is de primaire back-uplocatie en Amsterdam (Nederland) de secundaire, zodat uw back-upkopieën ook binnen de EU blijven.

**Gekoppelde systemen:** Als u documenten exporteert naar uw ERP, Infor IDM of een ander doelsysteem, worden die kopieën daar opgeslagen volgens de regels van dat systeem en op de locatie van dat systeem. Dat blijft in uw eigen handen.

## Hoe lang worden gegevens bewaard?

| Soort gegevens | Bewaartermijn |
| --- | --- |
| **Geüploade documenten en geëxtraheerde gegevens** | Door u bepaald via [Verloop van documenten](../administration-and-setup/settings/document-processing/documents-expiry.md) (zie hieronder). |
| **Tijdelijke OCR-bestanden** | Automatisch opgeruimd na **90 minuten**. Dit geldt alleen voor tijdelijke OCR-opslag, niet voor uw document in DocBits. |
| **Voor klanten toegankelijke logboeken** (te bekijken onder [Activiteitenlogboek](../administration-and-setup/settings/log-settings/README.md)) | **30 dagen** |
| **Interne logboeken** | **3 maanden** |
| **Dagelijkse database-back-ups (beheerd)** | **7 dagen**; oudere back-ups worden automatisch verwijderd. |
| **Extra dagelijkse back-ups (SnapShooter)** | Voor productie- en sandbox-databases; de bewaartermijn wordt per omgeving vastgesteld. |
| **Cookies en browseropslag** | Varieert per doel, zie [Cookies en browseropslag](cookies-and-browser-storage.md). |

Daarnaast maken wij dagelijkse, wekelijkse, driemaandelijkse en jaarlijkse back-ups. De exacte bewaartermijnen voor deze soorten back-ups voor uw omgeving delen wij op verzoek graag met u.

## Zo stelt u de bewaartermijn van uw documenten in

Open in de instellingen **Document Processing → Verloop van documenten**. Er zijn twee instellingen:

- **Delete document after:** hoe lang documenten worden bewaard.
- **Delete finished document after:** hoe lang afgeronde, volledig verwerkte en geëxporteerde documenten worden bewaard.

De opties zijn **Default**, **48 Hours**, **1 Week**, **2 Weeks** en **4 Weeks**. **Default** past de standaardwaarde van het systeem toe. Wilt u een vaste termijn, kies dan gewoon een van de looptijden. Alle details vindt u in de [handleiding Verloop van documenten](../administration-and-setup/settings/document-processing/documents-expiry.md).

## Wat gebeurt er wanneer gegevens worden verwijderd?

Verloop van documenten verwijdert uw documenten automatisch na de door u gekozen termijn. Dit staat los van het opruimen van tijdelijke OCR-bestanden, het verlopen van logboeken en de bewaring van back-ups.

Goed om te weten:

- **Back-ups verlopen volgens hun eigen schema.** Het verwijderen van een document in het live-systeem verwijdert back-upkopieën dus niet direct, maar pas wanneer de betreffende back-upperiode afloopt.
- **Geëxporteerde kopieën zijn van u.** Wanneer DocBits een document verwijdert, blijft de kopie in uw ERP of archief bestaan. Stem de bewaartermijn daar af op uw eigen eisen.

## Vragen of verwijderingsverzoeken? Wij staan voor u klaar

Voor informatie over uw implementatie of een verwijderingsverzoek kunt u ons schrijven via **compliance@fellowpro.com**. Vermeld daarbij uw organisatie, de betreffende omgeving, het soort gegevens en de omvang die u nodig heeft. Stuur ons alstublieft geen wachtwoorden of API-sleutels.

Wij bevestigen ook graag:

- Uw actieve regio en de effectieve bewaarinstellingen, inclusief de standaardwaarde van het systeem.
- Wanneer de verwijdertermijn begint en hoe vaak het opruimen plaatsvindt.
- De reikwijdte van de verwijdering voor documenten, geëxtraheerde gegevens, zoekindexen en afgeleide gegevens.
- Locaties en bewaartermijnen van alle soorten back-ups, ook na afloop van het contract.

## Meer beveiligingsinformatie

- [Beveiliging en naleving: locaties, logboeken en bewaring](security-and-compliance-faq.md)
- [Versleuteling van opgeslagen gegevens en reikwijdte van back-ups](encryption-at-rest.md)
- [Veilige opslag van inloggegevens](secure-storage-of-credentials.md)
- [Cookies en browseropslag](cookies-and-browser-storage.md)
