# And

## "And"-kaarten begrijpen

### **Doel van 'And'-kaarten:**

* **And**-kaarten fungeren als voorwaardekaarten die criteria specificeren waaraan moet worden voldaan om de workflow voort te zetten. Ze werken in feite als logische "AND"-operatoren, wat betekent dat aan alle in deze kaarten opgegeven voorwaarden moet worden voldaan voordat de volgende actie wordt getriggerd.

#### Categorieën van 'And'-kaarten

Uit de schermafbeeldingen blijkt duidelijk dat deze kaarten een breed scala aan voorwaarden bestrijken, waaronder:

* **Compare with Purchase Order**:
  * Voorwaarden met betrekking tot validatie en vergelijking met inkooporders, zoals het vergelijken van leverdata, eenheidsprijzen of verschillen in hoeveelheid. Deze zijn cruciaal om ervoor te zorgen dat transacties overeenkomen met de afgesproken voorwaarden.

<figure><img src="../../../../.gitbook/assets/workflow_and_comparison.png" alt="Workflow And Vergelijking"><figcaption></figcaption></figure>

* **Document Field**:
  * Deze betreffen voorwaarden op basis van specifieke velden binnen documenten, zoals aangevinkte selectievakjes, het vergelijken van veldwaarden, of het waarborgen dat een documentveld binnen een opgegeven tolerantie valt. Dit is met name belangrijk voor data-integriteit en geautomatiseerde controles binnen formulieren of documentbeheersystemen.

<figure><img src="../../../../.gitbook/assets/workflow_and_document_field.png" alt="Workflow And Document Field"><figcaption></figcaption></figure>

* **Document**:
  * Voorwaarden op basis van documentkenmerken, zoals het type of de koppeling aan een bepaalde suborganisatie. Deze voorwaarden kunnen workflows sturen op basis van documentcategorisatie of betrokkenheid van een afdeling.

<figure><img src="../../../../.gitbook/assets/workflow_and_document_type.png" alt="Workflow And Document Type"><figcaption></figcaption></figure>

* **Logic**:
  * Logische voorwaarden die evaluaties kunnen omvatten zoals "Continue with a chance of X%" of het uitvoeren van HTTPS-verzoeken, wat essentieel is voor integraties en probabilistische besluitvorming binnen workflows.

<figure><img src="../../../../.gitbook/assets/workflow_and_logic.png" alt="Workflow And Logica"><figcaption></figcaption></figure>

* **Status**:
  * Deze voorwaarden richten zich op de status van documenten of taken en zorgen ervoor dat alleen items in bepaalde toestanden specifieke workflows triggeren, wat cruciaal is voor statusgestuurd procesbeheer.

<figure><img src="../../../../.gitbook/assets/workflow_and_status.png" alt="Workflow And Status"><figcaption></figcaption></figure>

* **Table**:
  * Deze betreffen voorwaarden op basis van tabelgegevens, zoals het matchen van regex-patronen of het vergelijken van waarden binnen een tabel. Dergelijke voorwaarden zijn essentieel voor het valideren en bewerken van grote datasets.

<figure><img src="../../../../.gitbook/assets/workflow_and_table.png" alt="Workflow And Tabel"><figcaption></figcaption></figure>

* **Assignee**:
  * Voorwaarden op basis van de toegewezenen van een taak of document. Dit zorgt ervoor dat acties alleen worden uitgevoerd wanneer bepaalde gebruikers betrokken zijn, wat de verantwoording en taakspecificiteit verbetert.

<figure><img src="../../../../.gitbook/assets/workflow_and_assignee.png" alt="Workflow And Toegewezene"><figcaption></figcaption></figure>

### Praktische toepassing

Deze "And"-kaarten worden binnen de workflow geconfigureerd om controles en validaties uit te voeren die ervoor zorgen dat het proces zich strikt houdt aan bedrijfsregels en data-integriteitsnormen. Bijvoorbeeld:

* **Een workflow kan een 'And'-kaart gebruiken om te verifiëren dat het totaalbedrag van een factuur overeenkomt met de inkooporder voordat een betaling wordt getriggerd.**
* **Een andere workflow kan een 'And'-kaart gebruiken om ervoor te zorgen dat een document door specifieke teamleden wordt beoordeeld voordat het naar de volgende fase gaat.**

### Conclusie

"And"-kaarten zijn een fundamenteel onderdeel van workflowsystemen die nauwkeurige controle over de procesuitvoering op basis van meerdere voorwaarden vereisen. Ze zorgen ervoor dat elke stap van een workflow alleen wordt voortgezet wanneer aan alle noodzakelijke criteria volledig is voldaan, waardoor complexe beslisbomen binnen bedrijfsprocessen worden geautomatiseerd.

Het correct begrijpen en configureren van deze kaarten is cruciaal om de volledige mogelijkheden van uw workflowbeheersysteem te benutten en zo de efficiëntie, nauwkeurigheid en naleving binnen organisatorische processen te verbeteren.
