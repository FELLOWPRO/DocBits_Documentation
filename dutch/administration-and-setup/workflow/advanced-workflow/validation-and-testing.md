# Validatie & Testen

## Video: Variabelen, tests en activering

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

## Validate

Klik op de **Validate**-knop (het check-circle-pictogram, of druk op <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validatie controleert de graaf op problemen — niet-verbonden nodes, ontbrekende configuratie en ongeldige verbindingen — en wijst ze aan zodat u ze kunt oplossen voordat de workflow op echte documenten wordt uitgevoerd.

## Test

Klik op de **Test**-knop (het play-pictogram, of druk op <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) om de huidige flow tegen een voorbeeld uit te voeren en te zien hoe deze zich gedraagt, zonder live documenten te beïnvloeden. Dit is de snelste manier om een wijziging die u zojuist op het canvas hebt gemaakt te controleren.

## Wanneer welke gebruiken

- **Validate / Test in de builder** (deze pagina) — directe feedback terwijl u de flow ontwerpt.
- **[Test Manager](../test-manager.md)** — sla het scenario op zodat u het later opnieuw kunt uitvoeren (en samen met al uw andere scenario's) om regressies na toekomstige wijzigingen op te sporen.

## Volgende stappen

- Bekijk de nodetypen en verbindingen in [Nodes](nodes.md).
- Bekijk alle werkbalk- en canvasknoppen in [Werkbalk & Canvas](toolbar-and-canvas.md).
