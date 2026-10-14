# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om item-ID's tussen een inkooporder en een gerelateerd document te vergelijken om ervoor te zorgen dat de juiste items zijn opgenomen. De kaart evalueert of het item-ID in de inkooporder overeenkomt met het item-ID in het document. Deze vergelijking kan acties triggeren als er afwijkingen worden gevonden, wat ervoor zorgt dat de items in het document overeenkomen met de inkooporder.

## **Onderdelen van de kaart:**

1. **Any / All:**
   * **Beschrijving**: Definieert of de voorwaarde van toepassing is op elke of alle gevallen van item-ID-vergelijkingen.
   * **Opties**:
     * **Any**: Aan de voorwaarde is voldaan als een item-ID in de inkooporder overeenkomt met het item-ID in het document.
     * **All**: Aan de voorwaarde is alleen voldaan als alle item-ID's in de inkooporder overeenkomen met de item-ID's in het document.
2. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde voor het vergelijken van het item-ID op de inkooporder met het item-ID op het document.
   * **Opties**:
     * **Equals (=)**: Verifieert of het item-ID in de inkooporder exact overeenkomt met het item-ID in het document.
     * **Not Equals (≠)**: Zorgt ervoor dat het item-ID in de inkooporder niet overeenkomt met het item-ID in het document.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem vergelijkt het item-ID in de inkooporder met het item-ID in het document op basis van de geselecteerde operator. Als de vergelijkingsvoorwaarde true is (bijv. item-ID's komen wel of niet overeen), gaat de workflow dienovereenkomstig verder.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de voorwaarde true oplevert (bijv. het item-ID in de inkooporder is gelijk aan het item-ID in het document), gaat de workflow verder met de true-actie (bijv. goedkeuring of verdere verwerking).
  * **False-voorwaarde**: Als de voorwaarde false oplevert (bijv. het item-ID in de inkooporder komt niet overeen met het item-ID in het document), gaat de workflow niet verder.

## **Opzet en configuratie:**

* Gebruikers configureren de kaart door het item-ID in zowel de inkooporder als het document te selecteren. Vervolgens kiezen ze de juiste operator (Equals of Not Equals) om te definiëren hoe de item-ID's worden vergeleken. Ten slotte selecteren gebruikers of de voorwaarde van toepassing is op elke of alle item-ID's in de vergelijking.

## **Voorbeeldscenario:**

* Een factuur vermeldt een item met ID "ABC123" en de gerelateerde inkooporder bevat ook een item met ID "ABC123". Met de operator "Equals" vergelijkt de kaart het item-ID in het document met het item-ID in de inkooporder. Omdat de item-ID's overeenkomen, gaat de workflow zonder problemen verder

## **Conclusie:**

De workflow-kaart "Item ID Comparison" zorgt ervoor dat de item-ID's in documenten overeenkomen met die in inkooporders. Dit helpt afwijkingen in itemvermeldingen te voorkomen en zorgt ervoor dat de juiste items volgens de inkooporder worden verwerkt. De mogelijkheid om op basis van elke of alle gevallen te vergelijken, biedt flexibiliteit in verschillende gebruikssituaties, wat de nauwkeurigheid en efficiëntie van inkoopworkflows verbetert.
