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

### **1. Uniek beleid (Unique Policy)**

Zorgt ervoor dat slechts één enkele regel wordt gematcht. Als er meerdere regels worden gematcht, retourneert de beslissingsboom false.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen)
* **Regel 3**: Total Amount <= 5000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 3000 (komt overeen)

Omdat er meerdere regels overeenkomen (**Regel 2**, **Regel 3**, **Regel 4**, **Regel 5**), retourneert de beslissingsboom **false**, omdat het **Unieke** beleid ervoor zorgt dat slechts één regel kan overeenkomen.

### **2. Eerste beleid (First Policy)**

De eerste overeenkomende regel wordt toegepast en er worden geen verdere regels geëvalueerd.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen) → De beslissingsboom stopt met het evalueren van verdere regels en past **GROUP_2** toe.

### **3. Prioriteitsbeleid (Priority Policy)**

Met deze optie kunt u prioriteiten instellen voor elke regel. Hoe lager het geselecteerde getal, hoe hoger de prioriteit (d.w.z. prioriteit 1 heeft de hoogste prioriteit). Regels worden geëvalueerd op basis van hun prioriteitsvolgorde. De overeenkomende regel met de hoogste prioriteit wordt toegepast.

**Voorbeeld:**

<table><thead><tr><th width="137">Regel</th><th width="110">Prioriteit</th><th width="268">Voorwaarde</th><th>Geretourneerde groep</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Aangezien de prioriteit wordt toegepast in de volgorde **5, 4, 3, 2, 1**, is de overeenkomende regel met de hoogste prioriteit **Regel 5** (**GROUP_5**). De beslissingsboom retourneert **GROUP_5** omdat **Regel 5** de hoogste prioriteit heeft (prioriteit 1).

### **4. Verzamelbeleid (som) (Collect (sum) Policy)**

Dit beleid verzamelt alle overeenkomende regels en telt de resultaten op. Het werkt alleen voor **Return Type Value**.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde waarde |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Voor de invoerwaarde **Total Amount = 3500** zou de evaluatie van de regels als volgt zijn:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen, Return Value = 3)
* **Regel 4**: Total Amount <= 4000 (komt overeen, Return Value = 4)
* **Regel 5**: Total Amount <= 5000 (komt overeen, Return Value = 5)

Omdat het **Verzamel (som)**-beleid wordt toegepast, tellen we de **Return Values** van de overeenkomende regels op, namelijk **3, 4, 5**.

**Het optellen van deze waarden** geeft:

* 5 + 4 + 3 = **12**

Het resultaat dat door de beslissingsboom wordt geretourneerd is dus **12**, wat de som is van alle overeenkomende retourwaarden.

### **5. Verzamelbeleid (min/max/aantal) (Collect (min/max/count) Policy)**

Dit beleid verzamelt alle overeenkomende regels en selecteert ofwel het **minimum**, het **maximum**, of **telt** het aantal voorkomens. Het werkt alleen voor **Return Type Value**.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde waarde |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Als de optie **Collect (min)** is geselecteerd, retourneert het resultaat het **minimum** van de **Return Values** voor de overeenkomende regels.
   * Voor de invoerwaarde **Total Amount = 3500** zou de evaluatie van de regels als volgt zijn:
     * **Regel 1**: Total Amount <= 1000 (komt niet overeen)
     * **Regel 2**: Total Amount <= 2000 (komt niet overeen)
     * **Regel 3**: Total Amount <= 3000 (komt overeen, Return Value = 3)
     * **Regel 4**: Total Amount <= 4000 (komt overeen, Return Value = 4)
     * **Regel 5**: Total Amount <= 5000 (komt overeen, Return Value = 5)
   * De **overeenkomende regels** zijn Regel 3, Regel 4 en Regel 5, met **Return Values** van **3, 4 en 5**.
   * Omdat het **Collect (min)**-beleid wordt toegepast, is het resultaat de **minimale waarde**, namelijk **3**.
   * **Resultaat**: **3**
2. Als de optie **Collect (max)** is geselecteerd, retourneert het resultaat het **maximum** van de **Return Values** voor de overeenkomende regels.
   * Voor dezelfde evaluatie als hierboven is het resultaat:
   * **Resultaat**: **5**
3. Als de optie **Collect (count)** is geselecteerd, telt het resultaat het **aantal overeenkomende regels**.
   * Voor dezelfde evaluatie als hierboven is het resultaat:
   * **Resultaat**: **3** (aangezien 3 regels overeenkwamen).

### **6. Regelvolgordebeleid (Rule Order Policy)**

Dit beleid past regels toe in de volgorde waarin ze in de beslissingsboom verschijnen en retourneert het resultaat van de regel die als eerste overeenkomt.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Gegeven dat de invoerwaarde **Total Amount = 3500** is, zou de evaluatie van de regels als volgt zijn:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Onder **Regelvolgorde** verwerkt de boom de regels in de volgorde waarin ze worden vermeld. De overeenkomende regels zijn dus:

* **Regel 3**: GROUP_3
* **Regel 4**: GROUP_4
* **Regel 5**: GROUP_5

**Resultaat**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Elke regel-beleid (Any Policy)**

Meerdere regels kunnen waar zijn, maar het resultaat van die regels moet hetzelfde zijn.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Als het totaalbedrag **2500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Om **Any** toe te passen, moeten alle overeenkomende regels dezelfde **Return Group** retourneren. Omdat de groepen niet overeenkomen tussen de verschillende regels, is het resultaat **false**.

### **8. Eerste & aangrenzend beleid (First & Adjacent Policy)**

Kiest het resultaat van de regel die aangrenzend is aan de eerste regel die waar is.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen)

Omdat **Regel 2** de eerste regel is die overeenkomt, zou **First & Adjacent** het resultaat van **Regel 3** toepassen: **GROUP_3**.

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
