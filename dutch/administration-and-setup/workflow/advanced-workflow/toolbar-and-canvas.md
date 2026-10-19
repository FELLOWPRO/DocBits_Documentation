# Toolbar & Canvas

## Video: Bouwer en canvas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.vtt) · 1:38

<details>
<summary>Transcriptie</summary>

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

[Bekijk alle vijf hoofdstukken](../advanced-workflow-videos.md)

De Advanced Workflow-werkbalk loopt langs de onderkant van het canvas en geeft je alles wat je nodig hebt om de stroom te bouwen, te navigeren en te beheren.

## Werkbalkbedieningen

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
