# Lay-outeditor

Gebruik de Lay-outeditor om de velden en besturingselementen te ordenen die mensen zien wanneer ze een document valideren of goedkeuren. Een indeling hoort bij één documenttype, één oorsprong en één indelingstype; controleer deze drie bovenaan de pagina voordat u opslaat.

## De indeling openen

1. Open **Instellingen → Documenttypen**.
2. Selecteer het documenttype dat u wilt bewerken en open de **Lay-outeditor**. Voor een documentsubtype opent u de actie Lay-outeditor van dat subtype.
3. Controleer de kopregel. De linkerkeuzelijst is de **Oorsprong** (bijvoorbeeld **Standaard**), gevolgd door **Documenttype** (bijvoorbeeld **Factuur**) en **Indelingstype** (bijvoorbeeld **Veldvalidatie**). Elke keuzelijst opent een lijst; als u een ander item kiest, wordt die indeling geladen. Is de Lay-outeditor niet beschikbaar, dan moet een beheerder de module mogelijk inschakelen voor uw organisatie.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-nl.png" alt="De Lay-outeditor voor een factuur in DocBits, met de keuzelijsten voor oorsprong, documenttype en indelingstype, de tabbladen Structuur, Velden en Elementen, het indelingscanvas en het paneel Eigenschappen rechts"><figcaption><p>De Lay-outeditor: de keuzelijsten in de kopregel, de elementlijsten links, het canvas in het midden en het paneel Eigenschappen rechts.</p></figcaption></figure>

## Werken met de kopregel

* Met **Documenttype** en **Indelingstype** schakelt u tussen indelingen. De pagina laadt de indeling die u kiest opnieuw.
* Naast **Opslaan** geeft DocBits aan of de indeling **Niet-opgeslagen wijzigingen** bevat. Na het opslaan ziet u wanneer de indeling voor het laatst is opgeslagen.
* **Opslaan** bewaart de indeling voor het geselecteerde documenttype, de oorsprong en het indelingstype.
* Het menu **Meer** (drie puntjes) bevat **Automatisch sjabloon genereren**, **Standaard lay-out toepassen op oorsprongen**, **Standaardsjabloon gebruiken**, **JSON bewerken**, **JSON kopiëren** en **Indelingsinstellingen**. **Automatisch sjabloon genereren** en **Standaardsjabloon gebruiken** vervangen een aangepaste indeling; controleer daarom eerst het geselecteerde documenttype en de indeling. **JSON bewerken** is bedoeld voor geavanceerde configuratie en kunt u alleen gebruiken als u de sjabloonindeling begrijpt.
* Verlaat u de pagina met niet-opgeslagen wijzigingen, dan vraagt DocBits of u ze wilt opslaan of verwerpen.

## Elementen vinden: Structuur, Velden, Elementen

De linkerkant heeft drie tabbladen:

| Tabblad | Waarvoor |
| --- | --- |
| **Structuur** | Bekijk de indeling als een boomstructuur. Groepen en hun velden staan in de volgorde waarin ze op het canvas verschijnen, met het aantal geplaatste en beschikbare velden. |
| **Velden** | Alle voor het documenttype geconfigureerde velden, gegroepeerd per veldgroep en standaard ingeklapt. Het filter schakelt tussen de velden **Alle**, **Ongebruikt** en **Verborgen**, en de technische veldnaam staat onder het label van het veld. |
| **Elementen** | Besturingselementen voor weergave en interactie, zoals Tekst, Label, Selectievakje, scheidingstekens, tabellen, knoppen en subgroepen. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-nl.png" alt="Het tabblad Structuur van de Lay-outeditor met de groepen Factuurgegevens, Betalingsgegevens, Inkooporder en Leveringsgegevens uitgeklapt tot hun velden"><figcaption><p>Het tabblad Structuur toont de opgebouwde indeling als een boom van groepen en velden.</p></figcaption></figure>

Selecteer een item om het toe te voegen of sleep het naar het canvas. De titel van een groep vertelt degene die het document valideert wat er in die sectie hoort. Maak of hernoem herbruikbare documentvelden eerst in [Documenttypen](README.md).

## Werken op het canvas

* **Hoofdlay-out** toont de indeling van het document zelf. **Tabel** toont de tabelindeling die voor regelitems wordt gebruikt.
* **Document** opent of sluit het voorbeelddocument naast het canvas, zodat u de indeling met een echt document kunt vergelijken.
* Groepen worden als kaarten getekend; de velden binnen een groep kunt u in rijen plaatsen en verschillende breedtes geven.

## De eigenschappen van een element wijzigen

Selecteer een element of een groep op het canvas. **Eigenschappen** rechts is altijd zichtbaar en is ingedeeld in secties:

* **Weergave** – label, veldnaam, labelpositie en breedte van het element.
* **Gedrag** – alleen-lezen, verborgen en tabbladindex.
* **Waarden en lijsten** – de waarden die voor het element worden aangeboden.
* **Automatisering** – regels die het element vullen of wijzigen.
* **Randen en afstand** – het uiterlijk van het element.

Kies voor de breedte een van de vooraf ingestelde waarden (25, 33, 50, 66, 75 of 100 procent) in plaats van een waarde te typen, en controleer het resultaat op het canvas. Welke secties en opties verschijnen, hangt af van het geselecteerde element. Zie voor meer details [Veldeigenschappen configureren](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Controleren en opslaan

Orden de groepen en velden, controleer de indeling op het canvas en gebruik **Opslaan** in de kopregel wanneer het resultaat klopt. Zie voor oorsprongspecifieke indelingen [Oorsprongindelingen](origin-layouts.md).

{% hint style="info" %}
De schermafbeeldingen tonen synthetische instellingen in de DocBits-testorganisatie, met Nederlands geselecteerd in de applicatie. Tijdens het maken ervan is geen indeling opgeslagen of vervangen.
{% endhint %}
