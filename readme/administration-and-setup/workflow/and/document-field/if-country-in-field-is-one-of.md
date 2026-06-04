# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

Deze workflow-kaart is ontworpen om te evalueren of een opgegeven land, dat zich in een aangewezen veld bevindt, deel uitmaakt van een vooraf gedefinieerde lijst van landen. Op basis van deze evaluatie kan de workflow doorgaan met een true- of false-voorwaarde. Hij helpt processen te automatiseren waarbij acties afhangen van de vraag of het land voorkomt in een set toegestane of beperkte landen.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Geeft het documentveld op waar de landnaam of -code is opgeslagen.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het veld met de landgegevens binnen het document.&#x20;
2. **Operator**
   * **Beschrijving:** Definieert of het land in het veld deel moet uitmaken van een vooraf gedefinieerde lijst van landen.
   * **Opties:**
     * **Is:** Het land moet in de lijst van opgegeven landen zijn opgenomen om de voorwaarde true te maken.
     * **Is Not:** Het land mag niet in de lijst van opgegeven landen zijn opgenomen om de voorwaarde true te maken.
3. **Countries**
   * **Beschrijving:** Geeft de lijst van landen op waarmee het geselecteerde land wordt vergeleken.
   * **Detail:** Dit is een door komma's gescheiden lijst van landen. De vergelijking controleert of het land in het veld in deze lijst is opgenomen.
4. **Continue Condition**
   * **Beschrijving:** Definieert het resultaat van de vergelijking. Als het land aan de voorwaarde voldoet, gaat de workflow verder met de opgegeven Boolean-waarde.
   * **Opties:**
     * **True:** De workflow gaat verder als de voorwaarde overeenkomt.
     * **False:** De workflow gaat verder als de voorwaarde niet overeenkomt.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem evalueert of het in het veld opgegeven land deel uitmaakt van de lijst van vooraf gedefinieerde landen. Bij deze evaluatie wordt de landnaam of -code vergeleken met de opgegeven lijst.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Als het land in het veld deel uitmaakt van de opgegeven lijst van landen, gaat de workflow verder met de true-voorwaarde. Dit kan verdere acties triggeren, zoals het omleiden van documenten naar de juiste afdeling, het toepassen van specifieke verwerkingsregels of het inschakelen van regiospecifieke functies.
  * **False-voorwaarde:**\
    Als het land niet overeenkomt met de lijst, gaat de workflow verder met de false-voorwaarde. Hiermee kunnen alternatieve acties worden uitgevoerd of kan de workflow worden gestopt, afhankelijk van de systeemopzet.

## **Opzet en configuratie:**

* Gebruikers configureren de kaart door het documentveld met het land te selecteren en de lijst van landen op te geven waarmee wordt vergeleken. De operator wordt vervolgens uit een dropdownlijst gekozen om te definiëren of het land wel of niet deel moet uitmaken van de opgegeven lijst van landen. Ten slotte stellen gebruikers de doorgaan-voorwaarde (true of false) in, die de volgende stap in de workflow bepaalt.

## **Conclusie:**

De workflow-kaart "Country in Field Comparison with List" is een waardevol hulpmiddel voor het automatiseren van acties op basis van de vraag of een land deel uitmaakt van een vooraf gedefinieerde groep. Door de landgegevens te vergelijken met een lijst van toegestane of beperkte landen verbetert deze kaart de workflow-efficiëntie en zorgt hij ervoor dat systeemprocessen de juiste geografische regels volgen.
