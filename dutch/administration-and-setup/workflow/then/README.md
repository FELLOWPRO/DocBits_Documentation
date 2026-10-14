# Then: kies een actiekaart

Een **Then**-kaart geeft aan wat een workflow moet doen na de **When**-trigger en eventuele **And**-voorwaarden. Selecteer in de **Workflow Builder** **Kaart toevoegen** onder **Dan...**. Kies links een categorie of typ een naam in **Zoekkaart**. Selecteer een kaartvoorbeeld om het toe te voegen, vul de velden in die op de kaart staan, en sla de workflow op. Scroll binnen de kiezer om meer kaarten te zien. Selecteer **×** om te sluiten zonder een kaart toe te voegen. Zie [Workflow](../README.md) voor de volledige volgorde.

De voorbeelden hieronder tonen beschikbare acties, geen voltooide instellingen. Kies de actie die past bij het resultaat dat u wilt.

## Document Field

Zet een selectievakje aan of uit, plaats tekst in een veld, of kopieer de inhoud van het ene veld naar het andere. Kies de veldnamen en waarden die de kaart vraagt. Zie [Document Field](document-field/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-field-nl.png" alt="Nederlandse Then-kaartkiezer met Documentveld geselecteerd; voorbeelden tonen selectievakje omkeren, tekst instellen en veld kopiëren."><figcaption>Wijzig een veld of kopieer de inhoud ervan.</figcaption></figure>

## Document

Kies **Het document goedkeuren** of **Het document afwijzen** wanneer de workflow die beslissing moet nemen. Gebruik eerst een **And**-voorwaarde als de goedkeuring van een controle moet afhangen. Zie [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-nl.png" alt="Nederlandse Then-kaartkiezer met Document geselecteerd; de voorbeelden Het document goedkeuren en Het document afwijzen zijn zichtbaar."><figcaption>Keur het huidige document goed of wijs het af.</figcaption></figure>

## Logica

Gebruik deze kaarten om waarden tussen getal-, tekst- en booleaanse formaten om te zetten, of om een waarde uit JSON te lezen. Kies de invoer- en uitvoervelden op de geselecteerde kaart.

<figure><img src="../../../.gitbook/assets/then-category-logic-nl.png" alt="Nederlandse Then-kaartkiezer met Logica geselecteerd; zichtbare voorbeelden zetten datatypen om en lezen waarden uit JSON."><figcaption>Zet waarden om voor een latere workflowstap.</figcaption></figure>

## Status

Kies **Change Status** om het document naar een gekozen status te verplaatsen. De kaart kan ook een andere workflow triggeren. Zie [Status](status/README.md).

<figure><img src="../../../.gitbook/assets/then-category-status-nl.png" alt="Nederlandse Then-kaartkiezer met Status geselecteerd; het voorbeeld Change Status bevat een statusveld en een optionele workflow-trigger."><figcaption>Verplaats het document naar een andere status.</figcaption></figure>

## Prompts en scripts

Kies deze categorie om een DocOperator-prompts script uit te voeren. Selecteer het script en de variabelen die de kaart vraagt. De kaart biedt ook uitvoerinstellingen zoals pogingen om opnieuw te proberen.

<figure><img src="../../../.gitbook/assets/then-category-prompts-scripts-nl.png" alt="Nederlandse Then-kaartkiezer met Prompts en scripts geselecteerd; één DocOperator-prompts script-voorbeeld is zichtbaar."><figcaption>Voer een geconfigureerd DocOperator-prompts script uit.</figcaption></figure>

## Exporteren

Start een export, exporteer met een gekozen configuratie, of zet een definitieve export in de wachtrij. Kies de exportconfiguratie en de optie voor openstaande taken die op uw kaart staat. Zie [Export](export/README.md).

<figure><img src="../../../.gitbook/assets/then-category-export-nl.png" alt="Nederlandse Then-kaartkiezer met Exporteren geselecteerd; voorbeelden tonen start, geconfigureerde, wachtrij- en alternatieve export."><figcaption>Kies wanneer en hoe het document wordt geëxporteerd.</figcaption></figure>

## Taak

Maak een taak of melding en wijs deze toe aan een gebruiker of groep. Voer de titel, beschrijving, prioriteit en meldingsinstellingen in die de kaart vraagt. Sommige kaarten wijzen sequentieel toe. Zie [Task](task/README.md).

<figure><img src="../../../.gitbook/assets/then-category-task-nl.png" alt="Nederlandse Then-kaartkiezer met Taak geselecteerd; zichtbare voorbeelden maken of wijzen taken en meldingen toe."><figcaption>Maak opvolgwerk voor een persoon of groep.</figcaption></figure>

## E-mail

Verstuur een e-mail met een gekozen sjabloon, naar ontvangers of naar groepen. Kies het sjabloon en de bestemming op de kaart.

<figure><img src="../../../.gitbook/assets/then-category-email-nl.png" alt="Nederlandse Then-kaartkiezer met E-mail geselecteerd; voorbeelden sturen een e-mail met sjabloon naar ontvangers of groepen."><figcaption>Verstuur een e-mail met sjabloon.</figcaption></figure>

## Tafel

Wijzig vermeldingen of bereken waarden in een documenttabel. Selecteer de tabel, kolommen, operator en resultaatkolom die de kaart vraagt. Zie [Table](table/README.md).

<figure><img src="../../../.gitbook/assets/then-category-table-nl.png" alt="Nederlandse Then-kaartkiezer met Tafel geselecteerd; voorbeelden wijzigen vermeldingen en berekenen resultaatkolommen."><figcaption>Werk tabelgegevens bij of bereken ze.</figcaption></figure>

## Cessionaris

Wijs het document toe aan een gebruiker, groep, ontvanger of sub-organisatie. Sommige kaarten gebruiken een veld of beslistabel en bieden een fallback. Kies de juiste bestemming en fallback op de geselecteerde kaart. Zie [Assignee](assignee/README.md).

<figure><img src="../../../.gitbook/assets/then-category-assignee-nl.png" alt="Nederlandse Then-kaartkiezer met Cessionaris geselecteerd; zichtbare voorbeelden wijzen een gebruiker, ontvanger, groep of leverancierscontact toe."><figcaption>Routeer het document naar de volgende verantwoordelijke persoon of groep.</figcaption></figure>

## Actie

Voer een andere workflow uit, stuur een HTTPS-verzoek, roep een API aan, of gebruik de kaart voor de berekening van kostenverhogingstoeslagen. Deze acties kunnen andere systemen beïnvloeden; vraag uw beheerder welk eindpunt en welke instellingen te gebruiken. Zie [Action](action/README.md).

<figure><img src="../../../.gitbook/assets/then-category-action-nl.png" alt="Nederlandse Then-kaartkiezer met Actie geselecteerd; voorbeelden tonen Werkstroom uitvoeren, HTTPS-verzoek, API-aanroep en berekening kostenverhogingstoeslag."><figcaption>Start een andere workflow of integratie-actie.</figcaption></figure>
