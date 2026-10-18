# Workflow Logs

## Video

Deze twee video’s gebruiken lesdiagrammen die als illustraties zijn aangeduid.

### De juiste uitvoering vinden

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/nl.vtt) · 1:49

<details>
<summary>Transcriptie</summary>

**Open het documentlogboek**

Kies in het documentdashboard Workflow Logs onder Acties. Workflowtoegang moet ingeschakeld zijn. Deze logboeken horen bij het gekozen document. Ontwerpertests en gebeurtenis- of activiteitenlogboeken van de organisatie staan hier los van.

**Lees de tellers**

Blauw telt uitvoeringen in de huidige resultaten, rood fouten, geel onware voorwaarden en groen successen. De tellers beschrijven uitvoeringen, geen workflowdefinities of knooppunten. Filters kunnen deze aantallen wijzigen.

**Kies de exacte uitvoering**

Elke rij toont workflownaam, aanmaaktijd, duur in seconden en resultaat. Eén workflow kan meermaals voor hetzelfde document draaien. Vergelijk tijdstempels. Een korte uitvoering kan door afronding nul komma nul nul seconden tonen.

**Beperk de resultaten**

Zoek een workflow met Zoeken. Het afstelpictogram opent sorteerrichting, sorteercriterium, status en begin- en einddatum. Sorteer op naam of aanmaaktijd. Voer datums in als jaar, maand, dag en selecteer Toepassen.

**Controleer pagina’s en filters**

Gebruik paginering voor oudere resultaten. Filters wissen laadt de lijst zonder filterkeuzes. Wis de zoektekst afzonderlijk. Controleer bij lege resultaten document, datums en status. Een lege lijst bewijst geen uitvoeringsfout.

**Bijzondere toestanden**

Een banner en blokkeerpictogram tonen de uitvoeringslimiet van het document. Onderzoek herhaalde triggers voordat u limieten wijzigt. Een DocOperator-videodownload verschijnt alleen bij een bestaande opname; die opname hoort bij de uitvoering.

</details>

### Knooppunten volgen en onderzoeken

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.vtt) · 1:43

<details>
<summary>Transcriptie</summary>

**Vouw een uitvoering uit**

Vouw de workflowrij uit. Een geavanceerde uitvoering toont de graaf links en meldingen rechts; een standaardworkflow toont een reeks kaarten. De gegevens beschrijven die uitvoering en kunnen afwijken van de huidige ontwerper.

**Selecteer een knooppunt**

Verschuif of vergroot de graaf en klik op een knooppunt. Card Logs toont de meldingen. Wait ALL en Wait ANY kunnen ook knooppuntmeldingen hebben. Lees de melding samen met het gekozen knooppunt en tijdstempel.

**Onderscheid de uitkomsten**

Groen betekent succes, oranje een onware voorwaarde, rood een fout, grijs overgeslagen. Een overgeslagen knooppunt is niet uitgevoerd. Controleer eerst of een andere tak werd gekozen of een vereiste ingang van de samenvoeging ontbreekt.

**Volg de eerste afwijking**

Volg de werkelijke route vanaf de ingang. Bekijk oranje bij een onware bedragcontrole. Lees bij een fout de melding en volg rood. Foutafhandeling kan slagen terwijl de gehele uitvoering de oorspronkelijke fout blijft melden.

**Onderzoek samenvoegingen**

Controleer bij Wait ALL elke bron en verbonden uitkomst. Zoek bij ANY of OR een passende bron. Twee uitgangen van één knooppunt zijn geen onafhankelijke goedkeuringen. Een oranje voorwaarderesultaat kan bedoeld zijn.

**Corrigeer en controleer**

Noteer workflownaam, documentverwijzing, tijdstempel, knooppunt en exacte melding. Corrigeer instellingen of gegevens en test een herhaalbaar scenario. Sla op en controleer activering. Vergelijk een nieuwe uitvoering met de oude; eerdere logboeken beschrijven eerder gedrag.

</details>

## **Overzicht**

De **Workflow Logs** stellen gebruikers in staat om te analyseren welke workflows zijn uitgevoerd voor een document, de uitvoeringsresultaten te begrijpen en in te zoomen op details op voorwaardeniveau voor debugging of validatie.

## **Toegang tot Workflow Logs**

Om toegang te krijgen tot workflowlogs:

1. Navigeer naar het **Dashboard**.
2. Klik op het **Actiemenu** (pictogram met drie stippen) naast het gewenste document.
3. Selecteer **Workflow Logs** in het menu.
   * <mark style="color:red;">**Opmerking**</mark>**:** De workflowfunctie moet ingeschakeld zijn om deze optie te kunnen gebruiken.
4.  Een **zijpaneel** wordt geopend met een samenvatting van uitgevoerde workflows.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Onderdelen van het Workflow Logs Paneel**

#### **1. Workflow Samenvattingsaantallen**

Boven aan het logboekpaneel:

* **Blauw**: Totaal aantal uitgevoerde workflows.
* **Rood**: Workflows die eindigden in **fouten**.
* **Geel**: Workflows die **niet zijn voltooid** vanwege voorwaardemismatches.
* **Groen**: Succesvol **uitgevoerde** workflows.

#### **2. Workflow Uitvoertabel**

Elke rij in de tabel vertegenwoordigt één workflow-uitvoering en bevat:

* **Workflownaam**
* **Tijdstempel** (Gemaakt op)
* **Uitvoertijd** (in seconden)
* **Resultaatpictogram**:
  * Groen vinkje: Workflow succesvol uitgevoerd.
  * Rood kruis: Workflow uitgevoerd met een fout.
  * Oranje streepje: Uitvoering werd gestopt omdat een voorwaarde niet werd voldaan.

Door op de **pijl** aan de linkerkant van elke rij te klikken, wordt de **workflow detailweergave** uitgebreid.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Workflow Detailweergave**

Door op een specifieke workflowrij te klikken, wordt het **gedetailleerde uitvoeringslogboek** geopend, met:

#### **Voorwaarde Evaluatie**

* **Wanneer...** blok: Initiële voorwaarde.
* **En...** blok(ken): Aanvullende voorwaarden.
* **Dan...** blok(ken): Acties uitgevoerd wanneer aan alle voorwaarden is voldaan.

Elke voorwaardelijn toont:

* **Groen vinkje**: Voorwaarde was voldaan.
* **Oranje streepje**: Voorwaarde was niet voldaan.
* **Rood kruis**: Voorwaarde mislukte **wegens een fout**

### **Belangrijke Gedragsopmerking**

Als een voorwaarde in een workflow **niet wordt voldaan**, stopt het systeem met het evalueren van verdere workflowkaarten binnen die workflow. Dit gedrag voorkomt onnodige verwerking. Als visuele indicator wordt de kaart die **niet aan de voorwaarde voldeed** weergegeven in **grijs**, en alle **volgende kaarten** in dezelfde workflow zullen ook **grijs** verschijnen, wat aangeeft dat ze **niet zijn uitgevoerd**.
