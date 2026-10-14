# Validatieregels

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Validatie-instellingen en geaccepteerde versies"><figcaption><p>Validatie-instellingen en geaccepteerde XRechnung-versies</p></figcaption></figure>

De pagina **Validatieregels** (**E-documenten → Regels**) bepaalt hoe DocBits binnenkomende e-facturen valideert. Ze is gebaseerd op de officiële **KoSIT XRechnung + ZUGFeRD**-regelset plus de interne bevindingscodes van de validator, en laat u de ernst van elke regel voor uw organisatie overschrijven.

## Validatie-instellingen

De kaart **Validatie-instellingen** toont uw huidige validatieprofiel (bijvoorbeeld *B2G — Public Sector Receiver*). Klik op **Antwoorden bewerken** om de installatiewizard opnieuw uit te voeren en de standaard te wijzigen waartegen u valideert.

## Geaccepteerde XRechnung-versies

De gate **Geaccepteerde XRechnung-versies** somt elke XRechnung-versie op. Vink de versies aan die u accepteert — documenten waarvan de CustomizationID buiten deze lijst valt, worden vóór elke andere controle afgewezen met `VAL-VERSION-NOT-ALLOWED`. Een lege lijst betekent "alles accepteren". Elke versie is gemarkeerd met **current**, **deprecated** of **EOL** samen met de releasedatum.

## Geaccepteerde profielen en het ernstmodel

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Geaccepteerde profielen en ernstlegenda"><figcaption><p>Geaccepteerde profielen en wat elke ernst betekent</p></figcaption></figure>

Kies welke **profielen** u accepteert (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) met **Alles accepteren** / **Wissen** en daarna **Opslaan**.

Elke validatieregel heeft een **ernst** die bepaalt wat er gebeurt wanneer ze afgaat:

| Ernst | Effect |
|-------|--------|
| **FATAL** | Stopt de verwerking onmiddellijk. Geen volgende laag wordt gecontroleerd; het document gaat naar Fout. |
| **ERROR** | Het document wordt afgewezen. Andere bevindingen op hetzelfde document worden nog steeds getoond; de leveranciersmelding (indien ingeschakeld) wordt geactiveerd. |
| **WARNING** | Verschijnt in het validatierapport, maar het document gaat normaal door de pijplijn. |
| **INFO** | Alleen auditlog. Geen zichtbaar effect voor de gebruiker en geen afwijzing. |

## De ernst van regels overschrijven

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="De validatieregeltabel"><figcaption><p>De volledige regeltabel met ernst-overschrijving per regel</p></figcaption></figure>

De regeltabel somt elke validatieregel op (in totaal meer dan 1.600). Filter op **Laag (Layer)**, **Profiel** of **Versie**, of zoek op code of veld. Voor elke regel kunt u de **Ernst** in de vervolgkeuzelijst overschrijven om ze af te stemmen op het beleid van uw organisatie — bijvoorbeeld een regel van `ERROR` naar `WARNING` verlagen zodat ze het document niet langer afwijst.
