# Configuratie van identiteitsserviceprovider

Het configureren van de Identity Service Provider (IdP) om te integreren met DocBits vereist een paar specifieke stappen. Hier is een gids om dat te doen:

<figure><img src="../../../../.gitbook/assets/docbits_edit_menu_option.png" alt="Docbits Edit Menu Option"><figcaption></figcaption></figure>

**Toegang krijgen tot de IdP-configuratie-interface**

* Log in op uw Identity Service Provider (IdP) als beheerder.
* Navigeer naar de instellingen of configuratie-interface die is gewijd aan het beheren van SAML-integraties.

**De Tenant ID invoeren:**

* Zoek naar het gedeelte dat configuratie voor nieuwe SAML-integraties mogelijk maakt.
* Voer de DocBits Tenant ID in. Deze ID identificeert uw DocBits-account bij de IdP and maakt veilige communicatie tussen de twee systemen mogelijk.

**De vereiste bestanden importeren:**

* DocBits vereist meestal het downloaden van metagegevens of het toevoegen van specifieke configuratiegegevens. Raadpleeg de documentatie van uw IdP om te zien welke stappen vereist zijn.
* Download het DocBits-metagegevensbestand of importeer het in het configuratiemenu van uw IdP. Als alternatief kunt u de vereiste configuratiegegevens handmatig invoeren, afhankelijk van wat uw IdP ondersteunt.

**Integratie-instellingen configureren:**

* Zorg ervoor dat de integratie-instellingen, zoals de SSO-URL, Entity ID and het SAML-certificaat, correct zijn.
* Controleer of de Single Log-Out (SLO) URL and andere vereiste parameters correct zijn geconfigureerd. Deze zijn cruciaal voor een soepele authenticatie and afmelding via SAML.

**Configuratie verifiëren:**

* Neem de tijd om te controleren of alle ingevoerde informatie correct is and of er geen typefouten of onjuiste configuraties zijn.
* Voer tests uit om er zeker van te zijn dat gebruikers succesvol kunnen inloggen op DocBits via SAML and dat Single Log-Out correct werkt.

**Beveiligingsoverwegingen:**

* Zorg ervoor dat alle overgedragen bestanden and configuratiegegevens veilig worden behandeld om datalekken of ongeautoriseerde toegang te voorkomen.
* Bescherm gevoelige informatie zoals SAML-certificaten and inloggegevens tegen ongeautoriseerde toegang and bewaar ze op een veilige locatie.