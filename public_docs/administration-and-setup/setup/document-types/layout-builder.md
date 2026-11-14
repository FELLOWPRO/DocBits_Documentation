# Lay-outeditor

Gebruik de Lay-outbouwer om de velden en besturingselementen te ordenen die mensen zien wanneer zij een document valideren of goedkeuren. Een lay-out hoort bij één documenttype, één oorsprong en één lay-outtype, dus controleer die drie boven aan de pagina voordat u opslaat.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## De lay-out openen

1. Open **Settings → Document Types**.
2. Selecteer het documenttype dat u wilt bewerken en open **Layout Builder**. Open voor een document-subtype de actie **Layout Builder** van dat subtype.
3. Controleer de kop. De linkerselector is de **origin** (bijvoorbeeld **Default**), gevolgd door **Document Type** (bijvoorbeeld **Invoice**) en **Layout type** (bijvoorbeeld **Field Validation**). Elke selector opent een lijst; een andere vermelding kiezen laadt die lay-out. Is Layout Builder niet beschikbaar, dan moet een beheerder de module mogelijk voor uw organisatie inschakelen.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="De Layout Builder voor een factuur in DocBits, met selectors voor origin, documenttype en lay-outtype, de tabbladen Structure, Fields en Elements, het canvas en het paneel Properties rechts"><figcaption><p>De Layout Builder: de selectors in de kop, de elementlijsten links, het canvas in het midden en het paneel Properties rechts.</p></figcaption></figure>

## Werken met de kop

* **Document Type** en **Layout type** wisselen tussen lay-outs. De pagina herlaadt de lay-out die u kiest.
* Naast **Save** toont DocBits of de lay-out **unsaved changes** heeft. Na het opslaan toont het wanneer de lay-out voor het laatst is opgeslagen.
* **Save** bewaart de lay-out voor het geselecteerde documenttype, de oorsprong en het lay-outtype.
* Het menu **More** (drie stippen) bevat **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** en **Layout settings**. **Auto Generate template** en **Use default template** vervangen een aangepaste lay-out, dus controleer eerst het geselecteerde documenttype en de lay-out. **Edit JSON** is bedoeld voor geavanceerde configuratie en mag alleen worden gebruikt wanneer u de sjabloonindeling begrijpt.
* Verlaat u de pagina met niet-opgeslagen wijzigingen, dan vraagt DocBits of u ze wilt opslaan of wilt verwerpen.

## Onderdelen vinden: Structure, Fields, Elements

De linkerkant heeft drie tabbladen:

| Tab | Waarvoor |
| --- | --- |
| **Structure** | De lay-out als een boom bekijken. Groepen en hun velden staan in de volgorde waarin ze op het canvas verschijnen, met het aantal geplaatste en beschikbare velden. |
| **Fields** | Alle velden die voor het documenttype zijn geconfigureerd, gegroepeerd per veldgroep en standaard ingeklapt. De filter wisselt tussen **All**, **Unused** en **Hidden** velden, en onder het veldlabel staat de technische veldnaam. |
| **Elements** | Presentatie- en interactiebesturingselementen zoals Text, Label, Check Box, scheidingslijnen, tabellen, knoppen en subgroepen. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="Het tabblad Structure van de Layout Builder met de groepen Invoice details, Payment details, Purchase Order en Delivery Details uitgeklapt naar hun velden"><figcaption><p>Het tabblad Structure toont de opgebouwde lay-out als een boom van groepen en velden.</p></figcaption></figure>

Selecteer een item om het toe te voegen, of sleep het naar het canvas. Een groepstitel vertelt de persoon die het document valideert wat in die sectie thuishoort. Maak of hernoem herbruikbare documentvelden eerst in [Document Types](README.md).

## Op het canvas werken

* **Main layout** toont de lay-out van het document zelf. **Table** toont de tabellay-out voor factuurregels.
* **Document** opent of sluit het voorbeelddocument naast het canvas, zodat u de lay-out met een echt document kunt vergelijken.
* Groepen worden als kaarten getekend; de velden in een groep kunnen in rijen worden gerangschikt en verschillende breedtes krijgen.

## De eigenschappen van een element wijzigen

Selecteer een element of een groep op het canvas. **Properties** rechts is altijd zichtbaar en is in secties ingedeeld:

* **Display** – label, veldnaam, labelpositie en elementbreedte.
* **Behaviour** – alleen-lezen, verborgen en tabindex.
* **Values & lists** – de waarden die voor het element worden aangeboden.
* **Automation** – regels die het element vullen of wijzigen.
* **Borders & spacing** – de weergave van het element.

Kies voor de breedte een van de presets (25, 33, 50, 66, 75 of 100 procent) in plaats van een waarde te typen; controleer het resultaat op het canvas. Welke secties en opties verschijnen, hangt af van het geselecteerde element. Zie [Veldeigenschappen configureren](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md) voor meer informatie.

## Knoplabels vertalen

Knoppen zoals **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** en **Reject** halen hun label uit een vertaalsleutel. De viewer toont het label in de taal van de persoon die de lay-out opent. Heeft de sleutel geen tekst voor die taal, dan toont DocBits het label dat in de lay-out is opgeslagen.

* Een losse knop heeft een veld **Translation Key** in **Properties**.
* **Invoice Buttons** groepeert meerdere knoppen. Stel de sleutel voor één onderliggende knop in, of stel één sleutel per kind in de lijst op het paneel van de groep in.

Lay-outs die vóór deze wijziging zijn gebouwd, behouden hun labels: DocBits vult daarvoor de standaardsleutel van elk knoptype in. Lay-outs die met een sleutel worden opgeslagen, behouden die sleutel, ook na een herlading.

## Save and go back to Dashboard

Een knop van het type **Save and go back to Dashboard** bewaart de documentwaarden zoals **Save** en opent daarna het Dashboard. Het type past bij lay-outs waarin een beoordelaar een reeks documenten achter elkaar afwerkt.

* Voeg een knopelement op het canvas toe en kies het type in de **Properties** ervan.
* Mislukt het opslaan, dan blijft de knop op het validatiescherm staan en opent het Dashboard niet, zodat het probleem eerst kan worden verholpen.
* Het label wordt bepaald zoals het label van elke andere knop; zie *Knoplabels vertalen* hierboven.

## Controleren en opslaan

Orden de groepen en velden, controleer de lay-out op het canvas en gebruik **Save** in de kop wanneer het resultaat klopt. Zie [Oorsprongindelingen](origin-layouts.md) voor lay-outs per oorsprong.

{% hint style="info" %}
De schermopnamen tonen synthetische instellingen in de DocBits-testorganisatie met Engels geselecteerd in de applicatie. Tijdens het maken ervan is geen lay-out opgeslagen of vervangen.
{% endhint %}
