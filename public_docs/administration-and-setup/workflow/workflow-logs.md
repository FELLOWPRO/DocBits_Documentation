# Workflowlogboeken

Voor gesproken uitleg over de geavanceerde logweergave bekijkt u [De juiste uitvoering vinden](advanced-workflow-builder/videos.md#find-the-relevant-execution) en [Knooppunten volgen en onderzoeken](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Beide hoofdstukken zijn beschikbaar in het Engels en het Duits, met ondertitelbestanden en transcripties.

## **Overzicht**

Met de **Workflow Logs** kunnen gebruikers analyseren welke workflows voor een document zijn uitgevoerd, de uitvoeringsresultaten begrijpen en inzoomen op details op voorwaardenniveau voor foutopsporing of validatie.

## **Toegang tot Workflow Logs**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Video:** De workflowlogboeken lezen · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transcriptie</summary>

**De workflowlogboeken openen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Elk document bewaart de logboeken van de workflows die erop liepen. Open in het documentdashboard de acties van een document en kies Workflow Logs.

**Uitvoeringen en hun resultaten** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

Bovenaan ziet u hoeveel uitvoeringen er waren en hoeveel ervan eindigden met een fout, een niet-vervulde voorwaarde of succes. Daaronder staat elke uitvoering met de workflow, de tijd, de duur en het resultaat.

**Het pad van één uitvoering** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Sleep de scheidingslijn naar links om de logboeken meer ruimte te geven. Klik dan op een uitvoering om het pad te zien dat ze volgde. Elke kaart toont haar resultaat: groen voor succes, oranje voor een niet-vervulde voorwaarde, rood voor een fout. Hier eindigde de And-kaart met een niet-vervulde voorwaarde, dus de Then-kaart erna liep niet.

**Waarom een kaart zo eindigde** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Selecteer een kaart om haar logboek te lezen. Dat zegt wat de kaart vergeleek en waarom ze zo eindigde. Hier is het document klaar voor validatie, maar de kaart verwacht een nog openstaande tweede goedkeuring.

**Een fout en de oorzaak** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Een uitvoering die met een fout eindigt, toont de falende kaart in rood. Hier kon de And-kaart het bezorgadres niet uit het document lezen. Ontbrekende gegevens zijn altijd een fout, dus de Then-kaart erna liep niet.

**Uitvoeringen vinden** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Bij veel uitvoeringen gebruikt u de zoekfunctie om een workflow op naam te vinden, en de filterknop om de lijst op status of datum te beperken.

**Melding over de uitvoeringslimiet** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Bovenaan verschijnt een melding wanneer een workflow op dit document zijn uitvoeringslimiet heeft bereikt. De video over uitvoeringslimieten legt dat uit.

</details>

Om toegang te krijgen tot de workflowlogboeken:

1. Navigeer naar het **Dashboard**.
2. Klik op het **Actions menu** (pictogram met drie stippen) naast het gewenste document.
3. Selecteer **Workflow Logs** in het menu.
   * <mark style="color:red;">**Note**</mark>: De functie Workflow moet zijn ingeschakeld om deze optie te kunnen gebruiken.
4.  Er opent een **side panel** met een samenvatting van de uitgevoerde workflows.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Een logboek als eigen pagina openen**

Het side panel bedekt de documentenlijst. Voor een document waarvan u de workflow langere tijd onderzoekt, opent u hetzelfde logboek als volledige pagina: selecteer het pictogram voor een nieuw venster in de kop van het paneel. De pagina heeft het adres `/workflows/logs/<document id>`, zodat u haar in een tweede browservenster kunt openhouden of het adres naar een collega kunt sturen die toegang heeft tot het document.

De pagina toont dezelfde samenvattingstellers, dezelfde tabel met uitgevoerde workflows en dezelfde detailweergave als het paneel.

## **Naar een ander document schakelen**

Op de volledige pagina vindt een zoekveld boven de lijst een document op naam of op ID. De resultaten tonen de uploaddatum, de toegewezene en de status van elk document, zodat u documenten met vergelijkbare namen kunt onderscheiden. Als u een resultaat selecteert, wordt het workflowlogboek geladen en komt het document in het adres. De zoekopdracht bestrijkt de documenten van uw organisatie die u volgens uw rechten mag zien; als er niets overeenkomt, meldt DocBits dat onder het veld in plaats van een lege lijst te tonen.

## **Onderdelen van het Workflow Logs Paneel**

#### **1. Samenvattingstellers van de workflows**

Boven aan het logboekpaneel:

* **Blauw**: Totaal aantal uitgevoerde workflows.
* **Rood**: Workflows die eindigden met **fouten**.
* **Geel**: Workflows die **niet zijn voltooid** door niet-vervulde voorwaarden.
* **Groen**: Succesvol **uitgevoerde** workflows.

#### **2. Tabel met workflowuitvoeringen**

Elke rij in de tabel staat voor één workflowuitvoering en bevat:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (in seconden)
* **Result Icon**:
  * Groen vinkje: Workflow succesvol uitgevoerd.
  * Rood kruis: Workflow uitgevoerd met een fout.
  * Oranje streepje: Uitvoering is gestopt omdat niet aan een voorwaarde was voldaan

Als u op de **pijl** links van een rij klikt, wordt de **workflowdetailweergave** uitgevouwen.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Workflowdetailweergave**

Als u op een specifieke workflowrij klikt, wordt het **gedetailleerde uitvoeringslogboek** geopend, met:

#### **Evaluatie van voorwaarden**

* **When...**-blok: Initiële voorwaarde.
* **And...**-blok(ken): Aanvullende voorwaarden.
* **Then...**-blok(ken): Acties die worden uitgevoerd wanneer aan alle voorwaarden is voldaan.

Elke voorwaarderegel toont:

* **Groen vinkje**: Voorwaarde was vervuld.
* **Oranje streepje**: Voorwaarde was niet vervuld.
* **Rood kruis**: Voorwaarde is **door een fout** mislukt

### **Belangrijke opmerking over het gedrag**

Als een voorwaarde in een workflow **niet is vervuld**, **stopt het systeem met het evalueren van alle volgende workflowkaarten** binnen die workflow. Dit gedrag voorkomt onnodige verwerking\
Als visuele indicator wordt de kaart die **niet aan de voorwaarde voldeed** in **grijs** weergegeven, en alle **volgende kaarten** in dezelfde workflow verschijnen ook **grijs**, wat aangeeft dat ze **niet zijn uitgevoerd**.
