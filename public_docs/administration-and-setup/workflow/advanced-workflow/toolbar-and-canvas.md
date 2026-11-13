# Werkbalk en canvas

## Video: Bouwer en canvas

Maak kennis met Jan en volg zijn uitleg in de echte Nederlandstalige DocBits-interface. Hij controleert het workflowdashboard, de workflowlijst en de licentie en opent daarna een niet-opgeslagen concept in de ontwerper. Stap voor stap geeft hij de workflow een naam, stelt hij de bedragcontrole en twee acties in, plaatst hij de kaarten en verbindt hij beide routes. Daarna laat hij zien hoe je tests voorbereidt met een document of eigen gegevens. Het demoaccount heeft geen Advanced Workflow-abonnement en blokkeert de validatie; het concept blijft niet opgeslagen en inactief.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4) · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.vtt) · [Transcript (tekst)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.txt) · 3:21

| In deze video | Begin |
| --- | --- |
| Maak kennis met de beheerder | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=0) |
| Toegang controleren | [0:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=3) |
| De workflow een naam geven | [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=27) |
| De bedragcontrole instellen | [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=41) |
| De actie Approval toevoegen | [1:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=66) |
| De actie Standard toevoegen | [1:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=86) |
| Kaarten ordenen | [1:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=107) |
| Routes verbinden | [2:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=121) |
| Tests voorbereiden | [2:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=146) |
| Valideren, opslaan en activeren | [2:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=171) |

<details>
<summary>Transcript</summary>

**Maak kennis met de beheerder**

Ik beheer DocBits. We maken een factuurcontrole.

**Toegang controleren**

Ik begin op het workflowdashboard en open de workflowlijst. Daarna controleer ik de licentie. Workflow en Advanced Workflow hebben allebei actieve toegang nodig. Als beide zijn ingeschakeld, biedt Nieuwe workflow ook Advanced Workflow aan. Dit documentatieaccount heeft geen actieve workflowlicentie. Daarom ga ik verder met een niet opgeslagen voorbeeld in de ontwerper.

**De workflow een naam geven**

Ik werk in de echte DocBits-ontwerper. Eerst geef ik het concept een duidelijke naam. We controleren een factuurbedrag en gebruiken twee eenvoudige acties om de mogelijke routes te tonen. Dit voorbeeld blijft onopgeslagen.

**De bedragcontrole instellen**

Ik open het menu om iets toe te voegen en kies een voorwaardekaart. Onder Documentveld kies ik de Docfield-voorwaarde. Als veld vul ik total_amount in. Dan kies ik de vergelijking groter dan. En voer ik duizend in. Gebruik de veldsleutel van uw eigen document. Precies duizend voldoet niet aan deze vergelijking.

**De actie Approval toevoegen**

Nu voeg ik een actiekaart uit de categorie Documentveld toe. Deze actie stelt een documentveld in. Ik gebruik de voorbeeldsleutel approval_route. En vul de waarde Approval in. Dit geeft de route een herkenbare waarde. Een echt goedkeuringsproces heeft eigen bedrijfsacties nodig.

**De actie Standard toevoegen**

Ik voeg een tweede kaart met dezelfde actie toe. Deze actie stelt een documentveld in. Ik gebruik de voorbeeldsleutel approval_route. Dit keer krijgt het voorbeeldveld de waarde Standard. Beide kaarten zijn ingesteld. Er zijn nog verbindingen nodig om te bepalen welke actie wordt uitgevoerd.

**Kaarten ordenen**

Ik sleep de kaarten naar een leesbare indeling. De twee acties komen rechts. De voorwaarde staat in het midden, met Start links. Verplaatsen verandert alleen de positie. Het maakt geen verbinding.

**Routes verbinden**

Ik sleep van de uitgang van Start naar de ingang van de voorwaarde. De succesroute loopt via een blauwe verbinding naar Approval. De oranje route voor een onjuiste voorwaarde loopt naar Standard. De rode foutuitgang is een aparte uitgang voor evaluatiefouten. Hier blijft die zonder verbinding. Bepaal voor een productieworkflow hoe u zulke fouten afhandelt.

**Tests voorbereiden**

De testknop in de werkbalk opent de keuze van een testdocument. Ik kan een voorbeelddocument kiezen of volledige aangepaste gegevens voorbereiden. Test bedragen boven, onder en precies op duizend. Controleer ook een ontbrekend bedrag. Dit account heeft geen Advanced Workflow-licentie. Ik toon de voorbereiding van een test, geen uitgevoerd resultaat.

**Valideren, opslaan en activeren**

Validatie controleert verbindingen en kaartinstellingen. Bij dit account blokkeert de ontbrekende licentie de validatie. Met een account dat toegang heeft, zou ik uitdrukkelijk op de server opslaan. Daarna controleer ik de activering apart. Vóór de eerste opslag is de schakelaar uitgeschakeld. De aanduiding voor het automatische concept verwijst naar een lokale browserkopie. Die betekent niet dat de workflow opgeslagen of ingeschakeld is.

</details>

[Bekijk alle vijf hoofdstukken](../advanced-workflow-videos.md)

De Advanced Workflow-werkbalk loopt langs de onderkant van het canvas en geeft je alles wat je nodig hebt om de stroom te bouwen, te navigeren en te beheren.

## Werkbalkbedieningen

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4" %}

**Video:** Advanced Workflow-designer: kaarten en paden · 2:20 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Een nieuwe Workflow starten** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=0.25)

Open het Workflow-dashboard en selecteer Nieuwe workflow.

**Kies Geavanceerde workflow** · [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=5.416)

Kies Geavanceerde workflow. De designer opent met een Begin-knooppunt, waar elke flow begint.

**Wanneer, En en Dan** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=12.916)

Voeg kaarten toe met het menu Toevoegen of met een rechtermuisklik op het canvas. De drie kaartcategorieën zijn Wanneer, En en Dan.

**Wanneer: de triggerconditie** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=25.683)

De Wanneer-kaart is de triggerconditie. Ze bepaalt wanneer de Workflow start, bijvoorbeeld voor een bepaald documenttype.

**En: een extra conditie** · [0:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=39.183)

En-kaarten voegen extra condities toe. Ze controleren het document, bijvoorbeeld de status. Het resultaat is succes, of een mislukte conditie.

**Dan: de actiekaart** · [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=52.616)

Dan-kaarten zijn de actiekaarten. Ze wijzigen het document, bijvoorbeeld een veld instellen of het document goedkeuren.

**Slepen om te verbinden** · [1:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=61.616)

Om twee kaarten te verbinden, sleept u van een aansluitpunt rechts op de ene kaart naar de ingang links op de volgende.

**Blauw: Succes** · [1:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=69.983)

Blauw is het succespad. Elke kaart heeft het. De flow neemt het als de kaart klaar is.

**Oranje: Mislukte conditie** · [1:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=77.716)

Oranje is het pad voor een mislukte conditie. Alleen En-kaarten hebben het. De flow neemt het als de conditie niet klopt.

**Rood: Fout** · [1:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=87.75)

Rood is het foutpad. En- en Dan-kaarten hebben het. De flow neemt het als een kaart met een fout mislukt.

**Als-anders met foutafhandeling** · [1:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=96.45)

Samen vormen deze paden een als-anders met foutafhandeling. Succes voert een actie uit, een mislukte conditie een andere, en een fout een terugvaloptie, bijvoorbeeld een taak voor een persoon.

**Eén pad per status** · [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=109.383)

Voor meerdere gevallen koppelt u Documentstatus-kaarten via hun oranje paden. Elke kaart controleert één status, zo krijgt elke status een eigen pad.

**Het pad naar en vanaf een kaart** · [2:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/nl.mp4#t=120.783)

Klik op een kaart om haar uitvoeringspad te markeren: de kaarten die een document passeert om haar te bereiken, en de kaarten die erna kunnen volgen. Al het andere wordt gedimd. Hier is de taak alleen bereikbaar vanaf de Wanneer-kaart, via het rode foutpad van de Documentstatus-kaart.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4" %}

**Video:** Workflow-beschrijvingen en notities · 1:16 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Leg uw Workflow uit** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=0.25)

Een Workflow met meerdere vertakkingen is beter te onderhouden als hij zichzelf uitlegt. De designer heeft daarvoor twee hulpmiddelen: een beschrijving van de hele Workflow en notities op het canvas.

**Beschrijf de hele Workflow** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=14.383)

Selecteer Beschrijving bewerken in de werkbalk en zeg in een of twee zinnen waarvoor de Workflow dient. De beschrijving wordt bewaard als u de Workflow opslaat.

**Een notitie toevoegen** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=26.416)

Om één stap uit te leggen, rechtsklikt u op het canvas, opent u het menu Toevoegen en kiest u Opmerking. De notitie verschijnt waar u klikte.

**Dubbelklik om te schrijven** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=38.216)

Dubbelklik op de notitie om erin te schrijven, tot vijfhonderd tekens. Klik ernaast als u klaar bent.

**Verplaatsen en vergroten** · [0:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=47.05)

Sleep de notitie naast de kaarten die ze uitlegt, en trek aan de rechteronderhoek om haar groter te maken.

**Geef notities een kleur** · [0:55](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=55.183)

Klik met rechts op een notitie om de kleur te wijzigen. Kleuren helpen notities te groeperen, bijvoorbeeld blauw voor uitleg en rood voor open vragen.

**Notities worden nooit uitgevoerd** · [1:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/nl.mp4#t=66.516)

Notities zijn alleen voor mensen. Ze hangen aan geen enkele kaart en worden nooit uitgevoerd, dus ze veranderen niets aan de Workflow.

</details>

- **+ Add** — open het nodemenu om een node toe te voegen (zie [Nodes](nodes.md)).
- **Undo / Redo** — stap achteruit of vooruit door je wijzigingen.
- **Zoom in / Zoom out** — wijzig het zoomniveau van het canvas.
- **Workflow name** — geef de workflow inline een naam.
- **Edit description** — voeg een beschrijving voor de workflow toe.
- **Variables** — open het [Variables](variables.md)-paneel.
- **Help** — open het dialoogvenster met sneltoetsen en hulp.
- **Validate / Test** — controleer en voer de stroom uit (zie [Validation & Testing](validation-and-testing.md)).
- **Snap to grid** — schakel het uitlijnen van nodes op het raster in of uit voor nette indelingen.
- **Mini-map** — schakel een klein overzichtskaartje in of uit om door grote grafen te navigeren.
- **Save** — sla de workflow op. Een **auto-save**-indicator toont wanneer de stroom voor het laatst automatisch is opgeslagen.

## Sneltoetsen

Druk op <kbd>?</kbd> op het canvas om op elk moment het dialoogvenster met sneltoetsen en hulp te openen.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Dialoogvenster met sneltoetsen en hulp"><figcaption><p>Het dialoogvenster met sneltoetsen en hulp — sneltoetsen, markeren van het uitvoeringspad en verbindingskleuren.</p></figcaption></figure>

| Sneltoets | Actie |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Workflow opslaan |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Workflow valideren |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Workflow testen |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Ongedaan maken / Opnieuw |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Geselecteerde nodes kopiëren / plakken / dupliceren |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Alle nodes selecteren |
| <kbd>Shift</kbd> + Slepen | Nodes selecteren (slepen) |
| <kbd>Cmd/Ctrl</kbd> + Linkerklik | Node toevoegen aan/verwijderen uit selectie |
| Rechterklik | Menu Node toevoegen |
| <kbd>Del</kbd> | Geselecteerde node verwijderen |
| <kbd>?</kbd> | Deze hulp tonen |

## Volgende stappen

- Bouw de stroom met [Nodes](nodes.md) en [Variables](variables.md).
