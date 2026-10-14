# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

De workflow-kaart "**Assign the Document Sequentially to User/Group Based on Decision Table**" wijst documenten dynamisch toe aan een gebruiker of een groep, afhankelijk van de evaluatie van de decision table. Dit zorgt ervoor dat documenten op de juiste manier worden gerouteerd op basis van vooraf gedefinieerde regels.

## **Onderdelen van de kaart**

1. **Priority (Value)**
   * **Beschrijving**: Geeft het prioriteitsniveau voor toewijzingen op, waarbij lagere getallen een hogere prioriteit vertegenwoordigen.
   * **Detail**: Een numeriek invoerveld waarin de prioriteitswaarde kan worden ingesteld om de toewijzingsvolgorde te bepalen.

## **Functionaliteit**

* **Decision table-evaluatie**:\
  De decision table evalueert vooraf gedefinieerde voorwaarden om te beslissen of het document aan een gebruiker of een groep wordt toegewezen.
* **Documenttoewijzing**:
  * Als de decision table een gebruiker retourneert, wordt het document rechtstreeks aan die gebruiker toegewezen.
  * Als de decision table een groep retourneert, wordt het document sequentieel aan de groep toegewezen, met inachtneming van de opgegeven prioriteitswaarde.

## **Opzet en configuratie**

1. Voeg de kaart **Assign the Document Sequentially** toe aan uw workflow.
2. Configureer het veld **Priority (Value)**:
   * Voer een numerieke waarde in om de toewijzingsprioriteit in te stellen.
3. Sla op en activeer de workflow om de configuratie toe te passen.

## **Conclusie**

De workflow-kaart "**Assign the Document Sequentially to User/Group Based on Decision Table**" zorgt voor efficiënte en dynamische documentroutering. Door beslislogica en prioriteitswaarden te benutten, faciliteert de kaart een nauwkeurige toewijzing aan een gebruiker of een groep, wat documentworkflows stroomlijnt.
