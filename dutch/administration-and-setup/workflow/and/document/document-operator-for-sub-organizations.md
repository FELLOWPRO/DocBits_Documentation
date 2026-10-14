# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Doel:

Deze workflow-kaart evalueert of een document deel uitmaakt van een specifieke suborganisatie. Op basis van deze evaluatie kan de workflow doorgaan of verschillende acties triggeren, afhankelijk van de vraag of het document al dan niet aan de opgegeven suborganisatie is gekoppeld.

## Onderdelen van de kaart:

1. **Operator**
   * **Beschrijving:** Definieert of het document wel of niet deel moet uitmaken van de opgegeven suborganisatie.
   * **Opties:**
     * **Is:** Het document moet deel uitmaken van de opgegeven suborganisatie om de voorwaarde true te maken.
     * **Is Not:** Het document mag geen deel uitmaken van de opgegeven suborganisatie om de voorwaarde true te maken.
2. **Sub-org**
   * **Beschrijving:** Geeft de suborganisatie op waarmee het document wordt vergeleken.
   * **Detail:** Dit moet overeenkomen met de identifier van de suborganisatie. De vergelijking controleert of het document tot de opgegeven suborganisatie behoort.

## Functionaliteit:

* **Voorwaarde-evaluatie:** Het systeem evalueert of het document deel uitmaakt van de opgegeven suborganisatie. Bij deze evaluatie wordt de suborganisatie van het document vergeleken met die welke door de gebruiker is opgegeven.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Als het document deel uitmaakt van de opgegeven suborganisatie, gaat de workflow verder met de true-voorwaarde. Dit kan verdere acties triggeren, zoals het omleiden van het document naar een specifieke afdeling, het toepassen van suborganisatiespecifieke regels of het inschakelen van functies die op die suborganisatie zijn afgestemd.
  * **False-voorwaarde:**\
    Als het document geen deel uitmaakt van de opgegeven suborganisatie, gaat de workflow verder met de false-voorwaarde. Hiermee kunnen alternatieve acties worden uitgevoerd, zoals het verzenden van meldingen, het stoppen van de workflow of het toepassen van algemene regels buiten het bereik van de suborganisatie.

## Opzet en configuratie:

* Gebruikers configureren de kaart door het documentveld met het document te selecteren en de suborganisatie op te geven waarmee wordt vergeleken. De operator wordt vervolgens uit een dropdownlijst gekozen om te definiëren of het document wel of niet deel moet uitmaken van de opgegeven suborganisatie. Ten slotte stellen gebruikers de doorgaan-voorwaarde (true of false) in, die de volgende stap in de workflow bepaalt.

## Conclusie:

De workflow-kaart "Document in Sub-organization" is een handig hulpmiddel voor het automatiseren van acties op basis van de vraag of een document tot een bepaalde suborganisatie behoort. Door ervoor te zorgen dat documenten volgens suborganisatiespecifieke regels worden verwerkt, verbetert deze kaart de workflow-efficiëntie en zorgt hij ervoor dat acties binnen de juiste organisatorische context worden uitgevoerd.
