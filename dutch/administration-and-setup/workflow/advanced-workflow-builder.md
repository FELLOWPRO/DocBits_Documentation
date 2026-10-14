# Advanced Workflow

De **Advanced Workflow** builder is een node-grafiek-editor voor workflows die vertakkingen, parallelle paden en flow-besturing nodig hebben — verder dan de lineaire When/And/Then van de Standard builder. U plaatst nodes op een canvas en verbindt ze om de uitvoeringsstroom te definiëren.

{% embed url="https://youtu.be/EeNFVR6z7G8" %}
Advanced Workflow Designer
{% endembed %}

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
