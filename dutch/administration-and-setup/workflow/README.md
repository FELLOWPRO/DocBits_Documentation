---
description: DocBits Workflow Engine
---

# Workflow

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.42.57.png" alt=""><figcaption></figcaption></figure>

## DocBits Workflow Engine: procesautomatisering eenvoudig gemaakt

### Workflows begrijpen en voorbereiden <a id="workflow-orientation"></a>

Bekijk het echte DocBits-testaccount: acht uitvoeringen op het dashboard, twee opgeslagen workflows met uitvoeringsvolgorde 100/200 en drie geslaagde testscenario’s. De handleiding behandelt ook Standard en Advanced Workflows, licenties, sjablonen en de Card SDK.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4" %}

[Bekijken met ondertiteling](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.html) · [Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.vtt) · [Transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.txt) · 3:11

<details>
<summary>Hoofdstukken en transcript</summary>

| Hoofdstuk | Start |
| --- | --- |
| Maak kennis met de beheerder | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=0.000) |
| Organisatie en toegang | [0:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=1.208) |
| Dashboard en filters | [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=14.333) |
| Workflowlijst | [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=50.750) |
| Uitvoeringsvolgorde | [1:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=67.000) |
| Standard Workflow | [1:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=87.000) |
| Advanced Workflow | [1:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=100.500) |
| Licenties | [1:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=118.542) |
| Sjablonen | [2:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=136.875) |
| Test Manager | [2:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=149.375) |
| Card SDK | [2:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=162.875) |
| Voorbereiding controleren | [2:55](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/nl.mp4#t=175.875) |

**Maak kennis met de beheerder**

Ik beheer DocBits.

**Organisatie en toegang**

Goed, ik controleer eerst de organisatie bovenaan. Deze workflowinstellingen horen bij de geselecteerde organisatie. Voor deze uitleg gebruik ik ons testaccount voor documentatie.

**Dashboard en filters**

Het workflowdashboard geeft het overzicht. Voor dit overzicht heb ik twee trainingsworkflows acht keer handmatig uitgevoerd op een voorbeeldfactuur. Hier zie ik acht uitvoeringen in totaal en zes geslaagde uitvoeringen. Bij twee uitvoeringen was de bedragvoorwaarde niet vervuld. Het succespercentage telt ook deze correct afgeronde controles mee. Ik filter op workflownaam en controleer de periode. De tellers en de grafiek volgen die selectie. Rechts wissel ik tussen opgeslagen workflows en testscenario’s. Uitvoeringen in Test Manager worden apart geteld.

**Workflowlijst**

In de workflowlijst beheer ik elke workflow. Ik controleer de naam, het type Standard of Advanced, de uitvoeringsvolgorde, de trigger en de beschikbare acties. Ik zoek eerst naar een bestaande workflow voordat ik een nieuwe maak.

**Uitvoeringsvolgorde**

De uitvoeringsvolgorde is belangrijk als meerdere workflows hetzelfde document verwerken. Ik controleer welke eerst moet draaien en welke gegevens de volgende nodig heeft. Hier heeft de factuurcontrole volgorde honderd en de volgende controle tweehonderd. Lagere waarden worden eerder uitgevoerd.

**Standard Workflow**

Voor een regel met één pad gebruik ik een standaardworkflow. Wanneer bepaalt de trigger, En voegt voorwaarden toe, en Dan voert acties uit. De kaartbibliotheek bevat de beschikbare bouwstenen.

**Advanced Workflow**

Voor alternatieve routes gebruik ik Advanced Workflow. Dit ontwerpvoorbeeld toont Start en expliciete verbindingen. Succes, een onware voorwaarde en een fout kunnen verschillende routes volgen. De positie van kaarten bepaalt de volgorde niet.

**Licenties**

Onder Licentie controleer ik Workflow en Advanced Workflow afzonderlijk. Beide zijn hier inactief. Het venster toont de beschikbare abonnementen. Ik sluit deze inspectie zonder wijzigingen. Een ontwerpvoorbeeld activeert de workflowengine niet.

**Sjablonen**

Sjablonen bieden een herbruikbaar beginpunt. Ik open de bibliotheek en de optie voor standaardsjablonen. Ik controleer altijd de velden, ontvangers en acties voor mijn eigen proces.

**Test Manager**

Test Manager bewaart testscenario’s voor Standard en Advanced workflows. Na de configuratie voeg ik representatieve invoer en verwachte resultaten toe. Alle tests uitvoeren helpt mij wijzigingen te controleren.

**Card SDK**

Card SDK is voor eigen uitbreidingen. Ontwikkelaars kunnen een sjabloon gebruiken, een pakket uploaden of uit GitHub importeren. Voor normaal beheer begin ik met de bestaande kaartbibliotheek.

**Voorbereiding controleren**

Voordat ik begin, controleer ik de organisatie, toegang, benodigde licentie, documentvelden en het gewenste resultaat. Ik bepaal of een lineaire regel voldoende is. In de volgende video bouwen we stap voor stap een Standard Workflow.

</details>

### Inleiding

Op het gebied van procesautomatisering onderscheidt de DocBits Workflow Engine zich door zijn eenvoudige en intuïtieve aanpak. Deze engine stroomlijnt het aanmaken en beheren van workflows met een duidelijke en eenvoudige, op regels gebaseerde structuur. Het kernprincipe achter het ontwerp is de "Easy When-And-Then"-regel, die het automatiseringsproces opsplitst in drie fundamentele componenten: Trigger, Voorwaarde en Actie. Deze handleiding legt uit hoe elk onderdeel binnen het systeem werkt en hoe ze samenwerken voor naadloze automatisering.

### De "Easy When-And-Then"-regel uitgelegd

De DocBits Workflow Engine werkt volgens een eenvoudig maar krachtig principe dat workflowautomatisering toegankelijk maakt voor gebruikers van alle niveaus. Dit principe is vervat in de "Easy When-And-Then"-regel, die als volgt kan worden uitgesplitst:

#### [Wanneer](./#wanneer-trigger) (Trigger)

* **Definitie**: Het onderdeel "Wanneer" vertegenwoordigt de _Trigger_ van de workflow. Dit is de gebeurtenis of voorwaarde die de uitvoering van de workflow in gang zet. Triggers kunnen uiteenlopende gebeurtenissen zijn, zoals de ontvangst van een nieuwe e-mail, een bepaalde datum en tijd, of het aanmaken van een nieuw document.
* **Voorbeeld**: "Wanneer een nieuw klantformulier wordt ingediend..."

#### [En](./#en-voorwaarde) (Voorwaarde)

* **Definitie**: Het onderdeel "En" introduceert de _Voorwaarde_ waaraan moet worden voldaan voordat de actie kan doorgaan. Voorwaarden fungeren als filters of criteria die de trigger verfijnen, zodat de workflow alleen onder bepaalde omstandigheden wordt uitgevoerd.
* **Voorbeeld**: "...en de klant behoort tot het segment 'Enterprise'..."

#### [Dan](./#dan-actie) (Actie)

* **Definitie**: Ten slotte geeft het onderdeel "Dan" de _Actie_ aan die moet worden uitgevoerd zodra de trigger optreedt en aan de voorwaarde is voldaan. Acties zijn de taken of handelingen die de workflow uitvoert, zoals het versturen van een e-mail, het bijwerken van een database of het aanmaken van een taak in een projectmanagementtool.
* **Voorbeeld**: "...wijs de lead dan toe aan het enterprise-verkoopteam en stuur een welkomstmail."

### Componenten combineren voor krachtige automatiseringen

Door deze drie componenten, Trigger, Voorwaarde en Actie, te combineren, kunnen gebruikers met de DocBits Workflow Engine zeer op maat gemaakte en efficiënte workflows opbouwen. Deze modulaire aanpak maakt het instellen van automatiseringen niet alleen eenvoudiger, maar biedt ook de flexibiliteit om complexe workflows te maken die een breed scala aan taken en processen aankunnen.

### Conclusie

De "Easy When-And-Then"-regel van de DocBits Workflow Engine laat zien hoe sterk de engine zich richt op een gebruiksvriendelijk platform voor procesautomatisering. Door automatisering op te splitsen in de essentiële elementen Trigger, Voorwaarde en Actie, kunnen gebruikers workflows eenvoudiger bedenken, opbouwen en beheren. Of u nu nieuw bent met workflowautomatisering of een ervaren professional, de DocBits Workflow Engine biedt een efficiënte en toegankelijke tool om de productiviteit te verhogen en bedrijfsprocessen te stroomlijnen.

## Leerpad van beginner tot expert

[Leerpad van beginner tot expert](workflow-learning-path.md). Werk de niveaus op volgorde af. Alleen lezen volstaat niet: elk niveau eindigt met een eigen configuratie, toetsbare verwachting en bewijs. P0 voorkomt fundamentele uitvoeringsfouten; P1 verdiept gegevens, zakelijke besluiten en integraties.
