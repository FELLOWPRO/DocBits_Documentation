# Workflow Logs

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
