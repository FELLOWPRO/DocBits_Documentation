# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om te evalueren of een opgegeven land, dat zich in een aangewezen veld bevindt, deel uitmaakt van een bepaald handels- of politiek gebied (Europese Unie, Schengengebied of NAFTA). Op basis van deze evaluatie kan de workflow doorgaan met een true- of false-voorwaarde, waardoor verdere acties binnen het systeem mogelijk zijn. Hij is met name nuttig voor het automatiseren van regiospecifieke bedrijfsregels, het waarborgen van naleving of het triggeren van specifieke workflows op basis van geografische affiliaties.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Geeft het documentveld op waar de landnaam of -code is opgeslagen.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het veld met de landgegevens binnen het document.&#x20;
2. **Operator**
   * **Beschrijving:** Geeft op of het land in het geselecteerde veld wel of niet moet overeenkomen met de geselecteerde regio of overeenkomst.
   * **Opties:**
     * **Is:** Het land moet deel uitmaken van de geselecteerde overeenkomst (EU, Schengen of NAFTA) om de voorwaarde true te maken.
     * **Is Not:** Het land mag geen deel uitmaken van de geselecteerde overeenkomst om de voorwaarde true te maken.
3. **Country Comparison**
   * **Beschrijving:** Definieert of het land in het veld wordt gecontroleerd ten opzichte van een specifieke politieke of handelsovereenkomst.
   * **Opties:**
     * **European Union:** De kaart controleert of het land lid is van de Europese Unie.
     * **Schengen Area:** De kaart controleert of het land deel uitmaakt van het Schengengebied.
     * **NAFTA:** De kaart controleert of het land lid is van de NAFTA-overeenkomst.
4. **Boolean**
   * **Beschrijving:** Definieert het resultaat van de vergelijking. Als het land aan de voorwaarde voldoet, gaat de workflow verder met de opgegeven Boolean-waarde.
   * **Opties:**
     * **True:** De workflow gaat verder als de voorwaarde overeenkomt.
     * **False:** De workflow gaat verder als de voorwaarde niet overeenkomt.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**
  * Het systeem evalueert of het in het veld opgegeven land deel uitmaakt van de gekozen regio of overeenkomst (EU, Schengengebied of NAFTA) op basis van de geselecteerde operator. Bij deze evaluatie wordt de landnaam of -code vergeleken met een vooraf gedefinieerde lijst van landen die tot elke respectieve groep behoren.
* **Actie-uitvoering:**
  * **True-voorwaarde:** Als het land in het veld overeenkomt met de geselecteerde regio (volgens de operator), gaat de workflow verder met de opgegeven true-voorwaarde. Dit kan verdere acties triggeren, zoals het omleiden van documenten, het toepassen van speciale verwerkingsregels of het inschakelen van regiospecifieke functies.
  * **False-voorwaarde:** Als het land niet overeenkomt met de geselecteerde regio (volgens de operator), gaat de workflow verder met de opgegeven false-voorwaarde, waardoor alternatieve acties kunnen worden uitgevoerd of de workflow kan worden beëindigd, afhankelijk van de systeemopzet.

## **Opzet en configuratie:**&#x20;

* Gebruikers configureren de kaart door het documentveld met het land te selecteren en de regio (Europese Unie, Schengengebied of NAFTA) op te geven. De operator wordt vervolgens uit een dropdownlijst gekozen om te definiëren of het land wel of niet deel moet uitmaken van de geselecteerde regio. Ten slotte stellen gebruikers de doorgaan-voorwaarde (true of false) in, die de volgende stap in de workflow bepaalt.

## **Conclusie:**

De workflow-kaart "Country in Field Comparison" is een essentieel hulpmiddel voor het automatiseren van processen die afhankelijk zijn van geografische regels, zoals naleving van handelsovereenkomsten of politieke affiliaties. Door landgegevens te vergelijken met specifieke regio's zoals de Europese Unie, het Schengengebied of NAFTA, zorgt deze kaart ervoor dat het systeem de juiste verwerkingslogica toepast, wat de efficiëntie verbetert en zorgt voor een nauwkeurige workflow-uitvoering op basis van geografische voorwaarden.
