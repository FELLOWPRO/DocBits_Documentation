

De kaarten van deze categorie in de **Add Card**-kiezer van de Workflow Builder:

<figure><img src="../../../.gitbook/assets/workflow_cards_when.png" alt="Workflow Builder card category"><figcaption><p>De kaarten van deze categorie.</p></figcaption></figure>
---
hidden: true
---

# Wanneer

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKwAT37pCkZRziNLyWMsL%252Fimage.png%3Falt%3Dmedia%26token%3Db95d040f-e9e6-496d-97cd-d2c8f1c30d60\&width=768\&dpr=4\&quality=100\&sign=c323483b\&sv=2)

#### Begrip van de "Wanneer" in Workflow Configuraties

**Doel van "Wanneer"**

* De "Wanneer" sectie in een workflow configuratie definieert de triggercondities die een bepaalde workflow-actie initiëren. Deze condities zijn gebaseerd op gespecificeerde criteria met betrekking tot documentattributen of gebruikersactiviteiten binnen het ERP-systeem.

**Hoe Het Werkt**

* In jouw interface lijkt "Wanneer" een startpunt te zijn waar gebruikers verschillende triggerkaarten kunnen selecteren. Elke kaart specificeert condities waaronder daaropvolgende acties (gedefinieerd in de "En" sectie) zullen worden uitgevoerd.

**Document Type Condities Kaarten**

* De kaarten met het documentpictogram weergegeven in de screenshot zijn variaties van "Document Type" condities, die worden gebruikt om workflows te activeren op basis van het type document dat wordt verwerkt. Hier is een uitleg van elk type conditiekaart dat wordt getoond:
  * **Document type (Operator) een van (Type)**: Deze kaart activeert een actie wanneer het type van een document overeenkomt met een van de gespecificeerde types in een lijst. De operator kan opties bevatten zoals "is" of "is niet," waardoor inclusieve of exclusieve condities mogelijk zijn.
  * **Document type (Operator) (Type)**: Deze eenvoudigere variant activeert op basis van een enkele documenttypeconditie. Het zou typisch controleren of het documenttype "is" of "is niet" een specifiek type is, zonder de optie om uit meerdere types te selecteren.
  *

**Celery Beat**

* De kaart met het klokpictogram in de screenshot is een "Celery Beat" conditie, die wordt gebruikt om workflows te activeren op basis van datum en tijd.

#### Instellen van een "Wanneer" Triggerkaart

1. **Selectie van Conditietype**: Gebruikers beginnen met het selecteren van een conditietype dat relevant is voor de workflow die ze willen automatiseren. In dit geval zijn documenttypes het focuspunt.
2. **Definiëren van de Operator**: Gebruikers moeten de logische operator beslissen, zoals "is" of "is niet," die de basis vormt voor het vergelijken van daadwerkelijke documenttypes met de gedefinieerde condities.
3. **Specificeren van Documenttypes**: Afhankelijk van de kaart kunnen gebruikers één of meerdere documenttypes selecteren die de workflow zullen activeren wanneer documenten van die types worden verwerkt.
4. **Het Trigger Finaliseren**: Zodra de conditie is ingesteld, vormt het de basis voor het activeren van specifieke acties die zijn gedefinieerd in de workflow. Als een document aan de ingestelde conditie voldoet, zullen de gedefinieerde acties automatisch worden geïnitieerd.

#### Praktische Toepassing

In de praktijk zijn deze triggerkaarten cruciaal voor het automatiseren van processen zoals goedkeuringen, meldingen of enige procedure die afhankelijk is van het type document dat wordt behandeld. Bijvoorbeeld, als een documenttype "is" een "Factuur," en het voldoet aan de voorwaarden die zijn ingesteld in de "Wanneer" kaart, zou de workflow automatisch het document kunnen routeren voor betalingsverwerking.

Deze opstelling zorgt ervoor dat workflows niet alleen efficiënt zijn, maar ook zijn afgestemd op de specifieke operationele behoeften van de organisatie, waardoor handmatig toezicht wordt verminderd en documentverwerkingsprocessen worden versneld.

Samengevat, het "Wanneer" deel van jouw workflowconfiguratie draait om het instellen van het podium voor geautomatiseerde acties op basis van specifieke, vooraf gedefinieerde condities. Het is een krachtig instrument om ervoor te zorgen dat jouw ERP-systeem dynamisch reageert op de behoeften van het bedrijf, waardoor zowel productiviteit als nauwkeurigheid in documentbeheer worden verbeterd.
