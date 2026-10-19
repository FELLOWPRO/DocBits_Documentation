# Advanced Workflow

De **Advanced Workflow** builder is een node-grafiek-editor voor workflows die vertakkingen, parallelle paden en flow-besturing nodig hebben — verder dan de lineaire When/And/Then van de Standard builder. U plaatst nodes op een canvas en verbindt ze om de uitvoeringsstroom te definiëren.

## Video: factuurroutes in DocBits

De video toont een geconfigureerde workflow in de echte DocBits-interface: een bedragcontrole, twee acties, verbindingen en de voorbereiding van testgevallen.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.mp4" %}

[Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.vtt)

De opnamen tonen een niet-opgeslagen demonstratieconcept. `total_amount` en `approval_route` zijn voorbeeldsleutels voor velden. `Approval` en `Standard` geven de routes aan. Stel de bedrijfsacties in die uw proces nodig heeft.

<details>
<summary>Transcript</summary>

**Een factuur met twee routes**

Dit is een echte geavanceerde workflow in DocBits. Een controle van het factuurbedrag leidt naar twee acties. De verbindingen bepalen welke actie wordt uitgevoerd. Het voorbeeld gebruikt een niet-opgeslagen concept en demonstratievelden.

**De bedragcontrole instellen**

Open Toevoegen, kies And en selecteer een voorwaarde voor een documentveld. Stel het bedragveld in, kies Groter dan en voer duizend in. Gebruik de exacte veldsleutel uit uw documentconfiguratie.

**De acties instellen**

Voeg twee Then-kaarten toe. Beide stellen het demonstratieveld approval route in. De ene schrijft Approval, de andere Standard. Deze waarden geven de route aan. Stel voor een productieworkflow uw bedrijfsacties in.

**De resultaatuitgangen verbinden**

Verbind Start met de ingang van de voorwaarde. Verbind de blauwe succesuitgang met Approval en de oranje uitgang voor een onware voorwaarde met Standard. De rode uitgang behandelt evaluatiefouten afzonderlijk. Alleen de positie van een kaart vormt geen route.

**De testgevallen voorbereiden**

Open Testen in de werkbalk. Kies een testdocument of voer de volledige documentgegevens in als JSON. Controleer bedragen boven, onder en precies op duizend, en ontbrekende waarden. Bekijk na de uitvoering de resultaten van de knooppunten.

**Valideren, opslaan en activeren**

Valideer de verbindingen en kaartinstellingen. Sla de workflow expliciet op de server op en controleer de activering afzonderlijk. Automatische browserconcepten vervangen Opslaan niet. Voor uitvoering en logboeken zijn de juiste module en het juiste abonnement nodig.

</details>

## Toegang krijgen

Open de Advanced Workflow-ontwerper vanuit het workflow-gedeelte (het canvas van de advanced builder). U begint bij een **Start**-node en bouwt de flow uit door nodes toe te voegen.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced Workflow node-grafiek-canvas met werkbalk"><figcaption><p>Het Advanced Workflow-canvas — een node-grafiek met zoom-, run-, raster- en opslagbesturing. Geef de workflow een naam in de werkbalk.</p></figcaption></figure>

## Nodes toevoegen

Klik op **+ Add** om het node-menu te openen. Naast de bekende **When**-, **And**- en **Then**-kaarten voegt de advanced builder flow-besturingsnodes toe:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Advanced Workflow Add-menu met node-typen"><figcaption><p>Het <strong>+ Add</strong>-node-menu: When / And / Then plus Wait ALL, Wait ANY, OR en Note.</p></figcaption></figure>

- **When / And / Then** — dezelfde voorwaarde- en actiekaarten als de Standard builder.
- **Wait ALL** — wacht tot *alle* binnenkomende vertakkingen zijn voltooid voordat er wordt verdergegaan.
- **Wait ANY** — ga verder zodra *een* van de binnenkomende vertakkingen is voltooid.
- **OR** — vertak de flow langs alternatieve paden.
- **Note** — een vrije-tekstaantekening op het canvas (heeft geen invloed op de uitvoering).

Voer de flow uit met de afspeelknop, valideer hem en sla op met de opslagknop in de werkbalk.

## Volgende stappen

- Bekijk in het **Cards**-gedeelte wat elke kaart doet.
- Voor eenvoudige lineaire automatiseringen is de **Standard Workflow** builder sneller op te zetten.

[Bekijk alle vijf hoofdstukken](advanced-workflow-videos.md)
