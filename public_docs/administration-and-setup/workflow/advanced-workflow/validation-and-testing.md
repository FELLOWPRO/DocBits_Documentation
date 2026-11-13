# Validatie & Testen

## Video: Variabelen, testen en activering

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.vtt) · 2:00

<details>
<summary>Transcriptie</summary>

**Kies het variabeletype**

Open Variabelen met het accoladesymbool. Kies tekst, getal, ja of nee, of document. Zoek op naam. Een Document-variabele bevat een verwijzing die een specifieke workflowactie instelt; dit formulier accepteert geen documentwaarden.

**Variabelen van de organisatie**

Kies een unieke naam, type en beginwaarde. Aanmaken, wijzigen en verwijderen wordt direct voor de organisatie opgeslagen. Andere workflows kunnen deze waarden delen. Het canvas opslaan of verwerpen maakt variabelewijzigingen niet ongedaan.

**Valideer eerst de structuur**

Selecteer Valideren. Bekijk fouten en waarschuwingen boven het canvas. Klik op een melding om het knooppunt te vinden. Controleer acties, ingangen, uitgangen, cycli en samenvoegingen. Structurele validatie garandeert geen juiste uitvoeringsgegevens.

**Kies de testcontext**

Afspelen op de werkbalk opent de documentkeuze. Kies een document, aangepaste gegevens of een test zonder document voor onafhankelijke kaarten. Afspelen op Start begint direct. Tests gebruiken het huidige canvas, inclusief niet opgeslagen wijzigingen, en simuleren destructieve acties.

**Testscenario’s voorbereiden en controleren**

Maak aparte tests boven, onder en precies op duizend, plus ontbrekende gegevens. Controleer na uitvoering berichten en looptijden: groen betekent geslaagd, oranje onwaar, rood fout en grijs overgeslagen. Test correcties opnieuw. Gebruik Testbeheer voor herhaalbare scenario’s.

**Sla op vóór activering**

Automatisch opslaan bewaart ongeveer elke dertig seconden na wijzigingen een lokale browserversie. Sla expliciet op de server op. Activering vereist de eerste opslag. Controleer de ingeschakelde status in de workflowlijst voordat u automatische uitvoering verwacht.

</details>

[Bekijk alle vijf hoofdstukken](../advanced-workflow-videos.md)

Terwijl u een Advanced Workflow bouwt, kunt u deze met twee knoppen in de werkbalk controleren zonder de builder te verlaten. Deze zijn bedoeld voor *snelle controles tijdens het bouwen* — voor opgeslagen, herhaalbare tests gebruikt u de [Test Manager](../test-manager.md).

## Valideren

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.mp4" %}

**Video:** Een Workflow valideren · 0:52 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Valideren controleert de opbouw van de Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.mp4#t=0.25)

Klik vóór het opslaan op Valideren in de werkbalk. Dat controleert hoe de Workflow is opgebouwd: of een Wanneer-kaart hem start, of elke kaart verbonden is, en of de paden kloppen. Problemen staan boven het canvas.

**Klik op een melding om de kaart te vinden** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.mp4#t=16.05)

Klik op een melding om naar de kaart te springen. Hier is de toewijzingskaart niet verbonden, dus die zou nooit lopen. Verbind haar.

**Geen meldingen: de Workflow is geldig** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.mp4#t=26.25)

Valideer opnieuw. Is er niets meer over, dan is de Workflow geldig en kunt u hem opslaan.

**Eerst valideren, dan testen** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/nl.mp4#t=33.65)

Opslaan doet dezelfde controles, maar slaat de Workflow ook op als er nog problemen zijn, dus valideer eerst. Valideren controleert uw gegevens en de instellingen in de kaarten niet. Om te zien wat een Workflow met een echt document doet, test u hem.

</details>

Klik op de **Validate**-knop (het check-circle-pictogram, of druk op <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validatie controleert de graaf op problemen — niet-verbonden nodes, ontbrekende configuratie en ongeldige verbindingen — en wijst ze aan zodat u ze kunt oplossen voordat de workflow op echte documenten wordt uitgevoerd.

## Test

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4" %}

**Video:** Een Workflow testen · 1:45 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Testen voordat u inschakelt** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=0.25)

Test een Workflow voordat u hem inschakelt. Een test voert uit wat nu op het canvas staat, ook wijzigingen die nog niet zijn opgeslagen. Acties zoals toewijzen of exporteren worden alleen gesimuleerd, dus het document blijft zoals het is.

**De hele Workflow testen** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=16.45)

Hier is een Workflow die nog niet is opgeslagen. Om de hele Workflow te testen, klikt u op Workflow testen in de werkbalk.

**Kies een testdocument** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=25.616)

Kies het document voor de test. Workflows die geen document nodig hebben, kunt u ook zonder testen. Zoek het document op naam, selecteer het en klik op Test.

**Lees het resultaat op het canvas** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=38.316)

De test volgt het pad van het document. Deze factuur wacht niet op goedkeuring, dus de En-kaart eindigt met een mislukte conditie, en het oranje pad gaat verder naar de toewijzingskaart. Niet genomen paden zijn grijs, en de banner bovenaan toont het resultaat en hoe lang de test duurde.

**Details voor elke kaart** · [0:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=57.016)

Klik op Details om elke kaart met resultaat en melding te zien. Hertest voert de test opnieuw uit nadat u iets hebt gewijzigd.

**Eén kaart testen** · [1:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=67.05)

Om één kaart te testen, beweegt u erover en klikt u op de afspeelknop. U kunt ook met rechts op de kaart klikken en Test vanaf dit knooppunt kiezen. De test start bij deze kaart, met dezelfde documentkeuze.

**Beweeg over de badge voor details** · [1:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=81.35)

Alleen deze kaart en de kaarten erna lopen. Beweeg over de badge om het resultaat van de kaart te zien. Wijzig de kaart en test opnieuw tot ze doet wat u verwacht.

**Wat de kleuren betekenen** · [1:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/nl.mp4#t=92.916)

Kortom: groen betekent succes, oranje een mislukte conditie en rood een fout. Kaarten die niet liepen, zijn vervaagd en krijgen een grijze badge.

</details>

Klik op de **Test**-knop (het play-pictogram, of druk op <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) om de huidige flow tegen een voorbeeld uit te voeren en te zien hoe deze zich gedraagt, zonder live documenten te beïnvloeden. Dit is de snelste manier om een wijziging die u zojuist op het canvas hebt gemaakt te controleren.

## Wanneer welke gebruiken

- **Validate / Test in de builder** (deze pagina) — directe feedback terwijl u de flow ontwerpt.
- **[Test Manager](../test-manager.md)** — sla het scenario op zodat u het later opnieuw kunt uitvoeren (en samen met al uw andere scenario's) om regressies na toekomstige wijzigingen op te sporen.

## Volgende stappen

- Bekijk de nodetypen en verbindingen in [Nodes](nodes.md).
- Bekijk alle werkbalk- en canvasknoppen in [Werkbalk & Canvas](toolbar-and-canvas.md).
