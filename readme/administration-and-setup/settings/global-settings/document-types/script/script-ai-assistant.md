# AI-assistent in de scripteditor

De scripteditor heeft een ingebouwde **AI-assistent** die DocBits-scripts voor je schrijft en uitlegt. Je beschrijft in gewone taal wat het script moet doen en de assistent antwoordt met Python-code die je naar de editor kunt kopiëren.

{% hint style="info" %}
De AI-assistent maakt deel uit van **DocNet**. Je organisatie heeft een actief DocNet-abonnement nodig om hem te gebruiken. Zie [Abonnement](../../subscription-plan/README.md) en [Module](../../../document-processing/module/README.md).
{% endhint %}

## De assistent openen

1. Ga naar **Instellingen → Documenttypen**, open het documenttype en klik op **Scripts**.
2. Klik op **Nieuw**, of open een bestaande scriptversie als voorlopige versie.
3. Klik op het robotpictogram naast de scriptnaam. Het paneel **AI-assistent** opent aan de rechterkant van de editor.

## Wat de assistent weet

Bij elke vraag stuurt DocBits de assistent het volgende:

* de **scriptingreferentie** (de functies die worden beschreven in [Scripts in DocBits](scripting-in-docbits/README.md)),
* het **documenttype** van het script,
* het **huidige script** uit de editor,
* de **veldnamen en tabelkolommen** die je organisatie voor dit documenttype gebruikt.

Dankzij de veldnamen gebruikt de assistent je echte velden, bijvoorbeeld `invoice_date` of `purchase_order`, in `get_field_value()` en `set_field_value()`.

## Een script schrijven met de assistent

1. Typ je verzoek in het vak onderaan het paneel, bijvoorbeeld: *Stel de valuta in op EUR als die leeg is.*
2. Druk op **Enter** of klik op het verzendpictogram. Het antwoord verschijnt stap voor stap.
3. Klik op het kopieerpictogram (tooltip **Kopie naar de redactie**) naast een codeblok om de code in de scripteditor te plaatsen.
4. Controleer de code, geef het script een naam en sla het op als voorlopige versie.

Vervolgvragen werken in hetzelfde paneel. Plak een foutmelding of vraag *Waarom stelt dit script de vervaldatum niet in?* en de assistent kijkt naar het huidige script in de editor.

## Controleer het resultaat altijd

{% hint style="warning" %}
De assistent kan fouten maken. Lees de gegenereerde code, controleer of de veldnamen overeenkomen met je documenttype en test het script met een testdocument voordat je het activeert. Zie [Scripts testen](testing-scripts.md).
{% endhint %}

Scripts worden alleen uitgevoerd met de goedgekeurde scriptfuncties. Als een script een functie aanroept die niet bestaat, weigert DocBits het met de melding *Unknown function*.

## Gebruik en limieten

* Elk antwoord toont onder de reactie het aantal gebruikte tokens (invoer, uitvoer en totaal).
* Het gebruik wordt geregistreerd als DocNet-gebruik van je organisatie.
* DocBits weigert het verzoek als het DocNet-abonnement ontbreekt (*DocNet subscription required*), is verlopen (*DocNet subscription expired*) of het quotum is opgebruikt (*DocNet quota exhausted*).

## Gerelateerde pagina's

* [Scripts maken en bewerken](creating-and-editing-scripts.md)
* [Veldfuncties](scripting-in-docbits/field-functions.md)
* [Voorbeeldscripts](scripting-in-docbits/sample-scripts/README.md)
* [Scripts activeren en beheren](script-activation-and-management.md)
