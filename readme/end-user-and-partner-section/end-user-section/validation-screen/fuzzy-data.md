# Vage Gegevens

### **Overzicht**

Met Vage Gegevens-velden (Fuzzy Data) kunnen gebruikers gerelateerde velden invullen op basis van benaderende overeenkomsten uit masterdata. Deze velden herkent u aan een **blauw pictogram** naast het veld.

<figure><img src="../../../.gitbook/assets/fuzzy_data_field_icon.png" alt="Pictogram van een Vage Gegevens-veld"><figcaption></figcaption></figure>

### **Functionaliteit**

#### **Wat doen Vage Gegevens-velden?**

* Ze vullen gerelateerde velden in op basis van hun waarde of invoer.
* De drie standaardvelden die Vage Gegevens gebruiken zijn:
  * **Purchase Order**
  * **Supplier**
  * **Vendor ID**

#### **Vage Gegevens-velden gebruiken**

1. **Een inkooporder selecteren**
   *   Als u op het **blauwe pictogram** naast het veld Purchase Order klikt, opent een **selectievenster**.


       <figure><img src="../../../.gitbook/assets/fuzzy_data_selection_window.png" alt="Selectievenster voor Vage Gegevens"><figcaption></figcaption></figure>
   * Dit venster bevat een tabel met alle inkooporders uit de **masterdata-opzoektabel**.
   * Als u de optie **"Display all columns"** inschakelt, worden aanvullende details getoond.
   * Selecteer een **Purchase Order** en klik op **Proceed**:
     * Als het systeem een inkooporder in het document vindt, filtert het hier automatisch op.
     * Als er geen overeenkomst wordt gevonden, kunt u **eigen filters maken** om de juiste inkooporder te vinden.
     * U kunt meerdere filters toevoegen; als u **"Match all filters"** inschakelt, moet aan alle voorwaarden worden voldaan.
     * Beschikbare filteropties:
       * **Smart**
       * **Contains**
       * **Exact**
       * **Starts with**
       * **Ends with**
   * Met een knop naast **Proceed** kunnen gebruikers een **nieuwe taak/melding aanmaken**.
2. **Een leverancier of Vendor ID selecteren**
   * Het proces is hetzelfde als bij inkooporders.
   * Het verschil is dat de velden **Supplier en Vendor ID de leveranciersmasterdatatabel gebruiken** in plaats van de masterdatatabel voor inkooporderkoppen.

#### **Aanwijzing bij ingevulde velden**

* Als een veld is ingevuld met Vage Gegevens in plaats van uit het document te zijn geëxtraheerd, verschijnt een **klein hint- of infopictogram**. Dit geeft aan dat de gegevens **niet uit het document zijn geëxtraheerd**, maar op basis van masterdata zijn ingevuld.

### **Configuratie door de beheerder**

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md" %}
[fuzzy-data-configuration-with-list-of-values.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md)
{% endcontent-ref %}



{% embed url="https://www.youtube.com/watch?v=vT5HuGjAYV0" %}
