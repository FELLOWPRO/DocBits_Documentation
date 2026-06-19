# Beslissingsbomen

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Een beslissingsboom maken in DocBits (Voorwaarden, Beleidsregels, Testen & Exporteren)
{% endembed %}

## Overzicht

Beslissingsbomen zijn een krachtige functie die het geautomatiseerd routeren en het besluitvormingsproces mogelijk maakt op basis van vooraf gedefinieerde regels. Deze functie is bijzonder nuttig in complexe omgevingen waar verschillende voorwaarden moeten worden geëvalueerd om de juiste handelwijze te bepalen, zoals het toewijzen van prijzen, het bepalen van hoeveelheden of het routeren van documenten.

#### Belangrijkste componenten

* **Lijst met beslissingsbomen**: Dit is de hoofdinterface waar alle bestaande beslissingsbomen worden weergegeven. Elke beslissingsboom kan worden gekoppeld aan een specifiek documenttype zoals een `INVOICE` of `QUOTE`.
* **Beslissingsboom-ontwerper**: Met deze interface kunt u beslissingsbomen maken en bewerken, waarbij u regels, operatoren en acties kunt definiëren die moeten worden uitgevoerd wanneer aan bepaalde voorwaarden is voldaan.

## Beslissingsboom-interface

#### Lijst met beslissingsbomen

De lijst met beslissingsbomen toont alle geconfigureerde beslissingsbomen. Open deze via **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Lijst met beslissingsbomen"><figcaption><p>De lijst met beslissingsbomen</p></figcaption></figure>

Elke vermelding toont:

| Kolom | Beschrijving |
|--------|-------------|
| **Name** | De naam van de beslissingsboom. Klik erop om de Ontwerper te openen. |
| **Document Type** | Het documenttype waarop de boom van toepassing is (bijv. `INVOICE`, `QUOTE`). |
| **Last Modified By** | De gebruiker die de boom als laatste heeft bewerkt. |
| **Last Modified At** | Tijdstempel van de laatste wijziging. |
| **Actions** | Menu met drie puntjes om de boom te bewerken, kopiëren, exporteren of verwijderen. |

#### Een beslissingsboom maken

1. Klik op **+ Add Decision Tree** in de rechterbovenhoek.
2. Voer een **Name** in en selecteer het **Document Type**.
3. Gebruik de Beslissingsboom-ontwerper (hieronder) om voorwaarden, beleidsregels en resultaten te definiëren.

#### Een beslissingsboom importeren

Klik op **Import Decision Tree** om een eerder geëxporteerd beslissingsboombestand (JSON-formaat) te uploaden. Dit is handig voor het kopiëren van een boom tussen organisaties of omgevingen.

## Beslissingsboom-ontwerper

Met de Beslissingsboom-ontwerper kunt u regels configureren die bepalen hoe beslissingen worden genomen.

### **Componenten van de Beslissingsboom-ontwerper**

* **Regels**: Elke regel bestaat uit voorwaarden en acties.
* **Bron selecteren**: Met deze vervolgkeuzelijst kunt u het bronveld opgeven dat moet worden geëvalueerd.
* **Operator selecteren**: Definieert de logische operator (bijv. `<=`, `>=`, `=`, `!=`) die op het bronveld moet worden toegepast.
* **Resultaat**: Definieert de uitkomst of actie die moet worden uitgevoerd wanneer aan de voorwaarden is voldaan.
* **Nieuwe rij toevoegen**: Hiermee kunt u extra regels aan de beslissingsboom toevoegen.

### Voorbeeld van een beslissingsboomconfiguratie

Deze beslissingsboom evalueert het veld **Total Amount** en wijst het toe aan verschillende groepen op basis van vooraf gedefinieerde voorwaarden. Elke regel vergelijkt het totaalbedrag met een specifieke waarde, en op basis van welke voorwaarde waar is, wordt de bijbehorende **Group** geretourneerd.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Beslissingsboom Voorbeeld Total Amount"><figcaption></figcaption></figure>

Deze beslissingsboom evalueert twee belangrijke voorwaarden om te bepalen welke groep moet worden toegewezen: **Total Amount** en **Warehouse Status**. De boom gebruikt drempelwaarden op basis van het totaalbedrag om te definiëren welke groep wordt geretourneerd, met het aanvullende onderscheid of het magazijn is aangemerkt als "Warehouse Main", "Warehouse Sub" of "Not Warehouse Main".

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Beslissingsboom Voorbeeld Warehouse Status"><figcaption></figcaption></figure>

Elke regel wordt achtereenvolgens geëvalueerd.

## Beslissingsboombeleid

Het Beslissingsboombeleid definieert hoe meerdere regels binnen een beslissingsboom worden verwerkt. U kunt kiezen uit verschillende beleidsregels:

* [Uniek beleid (Unique Policy)](decision-trees/unique-policy.md)
* [Eerste beleid (First Policy)](decision-trees/first-policy.md)
* [Prioriteitsbeleid (Priority Policy)](decision-trees/priority-policy.md)
* [Verzamelbeleid (som) (Collect (sum) Policy)](decision-trees/collect-sum-policy.md)
* [Verzamelbeleid (min/max/aantal) (Collect (min/max/count) Policy)](decision-trees/collect-min-max-count-policy.md)
* [Regelvolgordebeleid (Rule Order Policy)](decision-trees/rule-order-policy.md)
* [Elke regel-beleid (Any Policy)](decision-trees/any-policy.md)
* [Eerste & aangrenzend beleid (First & Adjacent Policy)](decision-trees/first-and-adjacent-policy.md)

## **De beslissingsboom testen**

**Overzicht:**
De beslissingsboom-ontwerper bevat een testfunctie om de logica van de geconfigureerde regels te valideren. Met deze functie kunnen gebruikers de beslissingsboom testen door specifieke invoerwaarden voor de geselecteerde velden op te geven.

**Stappen om de testfunctie te gebruiken:**

1.  **Zoek de testknop:**

    * Zoek in de beslissingsboom-ontwerper de knop **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Beslissingsboom Testknop" width="563"><figcaption></figcaption></figure>
2.  **Open de test-pop-up:**

    * Klik op de knop **Test**.
    * Er verschijnt een pop-upvenster met invoervelden die overeenkomen met de criteria die in de beslissingsboom worden gebruikt.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Beslissingsboom Test-pop-up" width="421"><figcaption></figcaption></figure>
3. **Geef invoerwaarden op:**
   *   Voer waarden in de invoervelden in om een realistisch scenario te simuleren.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Beslissingsboom Testinvoer" width="428"><figcaption></figcaption></figure>
4.  **Evalueer de resultaten:**

    * Nadat u de invoer hebt ingevoerd, verwerkt de boom deze op basis van het gekozen beleid.
    * Het systeem markeert de regel(s) die overeenkomen met de opgegeven invoer.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Beslissingsboom Testresultaat" width="563"><figcaption></figcaption></figure>
5. **Bekijk feedback bij geen overeenkomst:**
   * Als er geen regel wordt gemarkeerd, toont het systeem feedback met uitleg waarom geen enkele regel overeenkwam.
   * Gebruik deze feedback om de invoer aan te passen of de configuratie van de boom te controleren op mogelijke problemen.

## Exporteren en opslaan

* **Save**: Slaat de huidige configuratie van de beslissingsboom op.
* **Export**: Hiermee kunt u de configuratie van de beslissingsboom exporteren, die vervolgens in een andere omgeving kan worden geïmporteerd of voor back-updoeleinden kan worden gebruikt.

## Toepassingsscenario's

* **Goedkeuringsworkflows** — routeer facturen naar verschillende goedkeurders op basis van bedragdrempels (bijvoorbeeld bedragen boven 10.000 vereisen goedkeuring door een manager).
* **Validatieregels** — valideer veldwaarden automatisch en markeer documenten die niet voldoen aan de geconfigureerde criteria.
* **Sequentiële toewijzing** — wijs documenten in een specifieke volgorde toe aan gebruikers op basis van voorwaarden.
