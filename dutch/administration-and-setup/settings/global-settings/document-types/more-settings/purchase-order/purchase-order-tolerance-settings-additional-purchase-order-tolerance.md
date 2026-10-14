# Aankooporder tolerantie-instellingen / Extra aankooporder tolerantie

### **Instelling om Aankooporder Toleranties te configureren**

Ga naar **Instellingen → Algemene Instellingen → Documenttypen → Meer Instellingen → Aankooporder Sectie → PO Tolerantie Instelling**

#### **Hoe Het Werkt**

Wanneer ingeschakeld, stelt deze instelling je in staat om toleranties voor **Hoeveelheid** en/of **Eenheidsprijs** te definiëren. Deze toleranties kunnen worden ingesteld als een percentage of als een vast bedrag. Dit betekent dat een factuur kan afwijken van de aankooporder (PO) binnen het opgegeven tolerantiebereik zonder als een mismatch te worden gemarkeerd, wat flexibiliteit biedt terwijl een naadloze verwerking wordt gegarandeerd.

<mark style="color:red;">**OPMERKING**</mark>: Toleranties werken in beide richtingen; dat wil zeggen, de factuurwaarde kan zowel hoger als lager zijn dan de PO-waarde binnen het toegestane bereik.

#### **Instelling Configureren**

* **Schakel de Instelling In:**
  * Zet de PO Tolerantie Instelling aan met de schakelaar.
* **Configureer Toleranties:**
  * Er verschijnen vier velden:
    * Eén veld voor het **Hoeveelheid Tolerantie Bedrag**.
    * Eén veld voor het **Eenheidsprijs Tolerantie Bedrag**.
  * Achter elk veld is er een dropdownmenu waar je het type tolerantie kunt selecteren:
    * **Percentage:** Geeft een percentage tolerantie aan.
    * **Waarde:** Geeft een vast bedrag aan waar het bedrag van kan afwijken.

<figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_value_fixed_example.jpg" alt="Docbits Po Tolerance Value Fixed Example"><figcaption></figcaption></figure>

#### **Voorbeeldscenario:**

* Stel dat de **Eenheidsprijs Tolerantie** is ingesteld op **5%**.
* De aankooporder bevat twee regels:
  * **Regel 1:** Eenheidsprijs = **$5.00**
  * **Regel 2:** Eenheidsprijs = **$2.00**
* Op de factuur:
  * **Regel 1:** De eenheidsprijs is aangepast naar **$4.80** (**binnen** de 5% tolerantie).
  * **Regel 2:** De eenheidsprijs is aangepast naar **$2.20** (**buiten** de 5% tolerantie).
* **Resultaat:**
  * Regel 1 is **niet gemarkeerd** als een mismatch omdat $4.80 binnen 5% van $5.00 ligt.
  * Regel 2 **is gemarkeerd** als een mismatch omdat $2.20 de toegestane 5% afwijking van $2.00 overschrijdt. De gebruiker moet nu actie ondernemen om de mismatch op te lossen voordat de factuur verder kan worden verwerkt.

<figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_mismatch_example_2.jpg" alt="Docbits Po Tolerance Mismatch Example 2"><figcaption></figcaption></figure>

### Instelling om Extra Aankooporder Tolerantie-instellingen te configureren

Ga naar **Instellingen → Algemene Instellingen → Documenttypen → Meer Instellingen → Aankooporder Sectie → Extra PO Tolerantie Instelling**

#### **Hoe Het Werkt**

Wanneer ingeschakeld, stelt deze instelling je in staat om toleranties voor **Vracht**, **Kosten**, en/of **Belasting** te definiëren. Deze toleranties kunnen worden ingesteld als een percentage of als een vast bedrag, waardoor facturen iets kunnen afwijken van de PO-waarden zonder als mismatches te worden gemarkeerd. Dit biedt extra flexibiliteit en zorgt ervoor dat kleine verschillen de workflow niet onderbreken.

<mark style="color:red;">**OPMERKING**</mark>: Net als de standaard tolerantie-instellingen, zijn deze toleranties van toepassing in beide richtingen—waardoor verhogingen of verlagingen binnen de ingestelde limieten zijn toegestaan.

#### **Instelling Configureren**

* **Schakel de Instelling In:**
  * Zet de Extra PO Tolerantie Instelling aan met de schakelaar.
* **Configureer Toleranties:**
  * Zes velden worden zichtbaar:
    * Eén veld voor de tolerantiebedragen voor **Vracht**, **Kosten**, en **Belasting**.
  * Elk veld heeft een bijbehorend dropdownmenu waar je het type tolerantie kunt kiezen:
    * **Percentage:** De tolerantie wordt gedefinieerd als een percentage.
    * **Waarde:** De tolerantie wordt gedefinieerd als een vast bedrag.

<figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_value_fixed_def.jpg" alt="Docbits Po Tolerance Value Fixed Def"><figcaption></figcaption></figure>

