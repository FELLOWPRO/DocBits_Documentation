# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om de leveranciersinformatie op een factuur te vergelijken met de leveranciersinformatie op de gerelateerde inkooporder. De kaart zorgt ervoor dat de leverancier op de factuur overeenkomt met de leverancier op de inkooporder. Deze vergelijking helpt te verifiëren dat de juiste leverancier voor de order factureert en kan acties triggeren op basis van eventuele afwijkingen.

## **Onderdelen van de kaart:**

1. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde voor het vergelijken van de leverancier op de factuur met de leverancier op de inkooporder.
   * **Opties**:
     * **Is**: Controleert of de leverancier op de factuur overeenkomt met de leverancier op de inkooporder.
     * **Is Not**: Zorgt ervoor dat de leverancier op de factuur niet overeenkomt met de leverancier op de inkooporder.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem vergelijkt de leverancier op de factuur met de leverancier op de inkooporder op basis van de geselecteerde operator. Als de vergelijkingsvoorwaarde true is (bijv. de leverancier is hetzelfde of verschillend zoals vereist), gaat de workflow dienovereenkomstig verder.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de voorwaarde true oplevert (bijv. de leverancier op de factuur komt overeen met de leverancier op de inkooporder), gaat de workflow verder zonder fouten te triggeren.
  * **False-voorwaarde**: Als de voorwaarde false oplevert (bijv. de leverancier op de factuur komt niet overeen met de leverancier op de inkooporder), gaat de workflow niet verder.

## **Opzet en configuratie:**

* Gebruikers kiezen de juiste operator ("Is" of "Is Not") om te definiëren hoe de leveranciers worden vergeleken.

## **Voorbeeldscenario:**

* Een factuur vermeldt een leverancier met het ID "SUP123" en de gerelateerde inkooporder vermeldt ook "SUP123" als de leverancier. Met de operator "Is" vergelijkt de kaart de leveranciers en stelt vast dat ze hetzelfde zijn, waardoor de workflow zonder problemen verdergaat.

## **Conclusie:**

De workflow-kaart "Supplier Comparison" zorgt ervoor dat de juiste leverancier voor de inkooporder factureert, wat helpt afwijkingen en fouten in het inkoopproces te voorkomen. Door leveranciersinformatie automatisch te verifiëren, kunnen organisaties hun factuurgoedkeuringsproces stroomlijnen en het risico op fraude of fouten in leveranciersfacturatie verminderen.
