# Mastergegevensinstellingen

## Overzicht

In de sectie Mastergegevensinstellingen van de **Velden**-instellingen voor een specifiek Documenttype kunt u stamgegevenskoppelingen naar velden die worden gebruikt bij veldvalidatie bekijken en configureren, met behulp van gegevens uit [**Stamgegevens opzoeken**](../../../document-processing/master-data-lookup.md).

Deze koppelingen definiëren hoe stamgegevens worden toegepast op individuele velden tijdens validatie. Deze pagina biedt een gedetailleide handleiding voor het configureren en beheren van deze koppelingen.

## **Toegang tot** Mastergegevensinstellingen **Instellingen**

Om toegang te krijgen tot de instellingen voor Mastergegevensinstellingen:

1.  Ga naar **Instellingen → Globale instellingen → Documenttypen**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Selecteer het gewenste **Documenttype** en klik op **Velden**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Klik op **Mastergegevensinstellingen**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Stamgegevens opzoeken

In de sectie **Stamgegevens opzoeken** kunt u opzoekconfiguraties maken op basis van uw stamgegevens om te gebruiken als veldkoppelingen tijdens veldvalidatie.

### Standaardvermeldingen

In de sectie **Stamgegevens opzoeken** worden bepaalde standaardvermeldingen geleverd door **DocBits**. Deze vermeldingen:

* Kunnen niet worden bewerkt of verwijderd
* Kunnen worden gedeactiveerd als ze niet nodig zijn

Standaardvermeldingen zijn duidelijk gemarkeerd met een **Default** tag voor eenvoudige identificatie.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Opzoekconfiguratie maken**

Om een nieuwe opzoekconfiguratie voor stamgegevens te maken:

1. Ga naar de sectie **Stamgegevens opzoeken**.
2.  Klik rechtsboven op **Opzoekconfiguratie maken**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Configureer de volgende opties:
   * **Zoeknaam**\
     De naam van de opzoekconfiguratie.
   * **Naam van opzoekdataset**\
     Selecteer de dataset die voor deze opzoekconfiguratie moet worden gebruikt.
   * **Conflictbehandelaar**\
     Een conflict betekent dat de zoekopdracht meer dan één record heeft gevonden. Deze instelling bepaalt wat er dan gebeurt:
     * **Best Score** – Gebruikt de vermelding die met de meeste velden overeenkomt. Laat het veld nooit leeg en kan daardoor het verkeerde record kiezen.
     * **Return None** – Laat het veld leeg, zodat een gebruiker het juiste record kiest.
     * **Return First** – Gebruikt de eerste gevonden waarde.
   *   **Contexttype**

       Specificeert waar in het document de opzoekconfiguratie wordt toegepast. Kies tussen:

       **HEADER**

       De opzoekfunctie wordt gebruikt in veldvalidatie. Configureer het volgende:

       * **Alles matchen**\
         Wanneer ingeschakeld, moet een record met **alle** gebruikte velden overeenkomen. Wanneer uitgeschakeld (standaard) is **één** overeenkomend veld genoeg, wat een langere lijst oplevert.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       De opzoekfunctie wordt binnen een documenttabel gebruikt. Configureer het volgende:

       * **Contextdetail**\
         Selecteer de specifieke tabel waarop de opzoekfunctie moet worden toegepast.
       * **Alles matchen**\
         Wanneer ingeschakeld, moet een record met **alle** gebruikte velden overeenkomen. Wanneer uitgeschakeld (standaard) is **één** overeenkomend veld genoeg, wat een langere lijst oplevert.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Alles matchen** en de **Conflictbehandelaar** werken samen en bepalen of een leverancier automatisch wordt herkend. De installatiepagina legt beide uit met voorbeelden:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Klik op **Opslaan** om de opzoekconfiguratie te maken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Acties voor bestaande opzoekconfiguratie

Om een bestaande opzoekconfiguratie te beheren, klikt u op de drie puntjes rechtsboven in de configuratie die u wilt wijzigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

De volgende acties zijn beschikbaar:

* **Activeren / Deactiveren**\
  Wissel de status van de opzoekconfiguratie.
  * Actieve configuraties zijn gemarkeerd met een **Actief** tag.
  * Inactieve configuraties zijn gemarkeerd met een **Inactief** tag.
*   **Duplicaat**\
    Na het invoeren van een naam en op **Klaar** te klikken, wordt een kopie van de geselecteerde opzoekconfiguratie gemaakt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Bewerking/Weergave**\
  Hiermee kunt u de geselecteerde opzoekconfiguratie wijzigen.\
  Klik na het aanbrengen van uw wijzigingen op **Opslaan** om ze toe te passen.\
  <mark style="color:red;">**Opmerking**</mark>: Standaard-opzoekconfiguraties kunnen alleen worden bekeken, niet bewerkt. De **Bewerking**-optie wordt vervangen door **Weergave**.
*   **Verwijderen**\
    Verwijdert de geselecteerde opzoekconfiguratie permanent na bevestiging.\
    <mark style="color:red;">**Opmerking**</mark>: Alleen configuraties zonder de **Default** tag kunnen worden verwijderd.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Nieuw veld creëren

Om een nieuw veld aan uw opzoekconfiguratie toe te voegen:

1. Open de gewenste opzoekconfiguratie.
2.  Klik rechtsboven op **Creëren**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Configureer de benodigde opties.
   * **Opzoekveld**\
     Het veld dat zal worden doorzocht binnen de geselecteerde opzoekdataset.
   * **Validatieveld**\
     Het veld dat wordt weergegeven tijdens veldvalidatie.
   * **Bovenliggend veld** (optioneel)\
     Dit veld wordt gebruikt om de juistheid van de waarde in het **Validatieveld** te valideren door te waarborgen dat deze overeenkomt met de corresponderende bovenliggende vermelding in de opzoekdataset.
   * **Zoekoperator** (optioneel)\
     Kies hoe **DocBits** zoekt naar overeenkomsten in de opzoekdataset:
     * **Smart** – _(Standaard)_ Negeert spaties en leestekens en zoekt de term **ergens** in het veld. "Meier" vindt daarom ook "Meier Bau GmbH".
     * **Bevat** – Zoekt naar vermeldingen die de exacte term ergens in het veld bevatten.
     * **Eindigt met** – Zoekt naar vermeldingen die eindigen met de opgegeven term.
     * **Exact** – Zoekt naar een exacte overeenkomst van de volledige waarde.
     * **Begint met** – Zoekt naar vermeldingen die beginnen met de opgegeven term.
   * **Automatische trigger** (optioneel)\
     Wanneer ingeschakeld, zal DocBits automatisch alle velden in de opzoekconfiguratie invullen zodra dit veld is ingevuld.
   *   **Zoekbaar** (optioneel)\
       Wanneer ingeschakeld, kunnen gebruikers tijdens veldvalidatie handmatig naar stamgegevens zoeken **en** doet het veld mee aan de automatische zoekopdracht. Laat het uitgevinkt als het veld het automatische resultaat niet mag beïnvloeden.



       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)



       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Klik op **Opslaan** om het nieuwe veld te maken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Acties voor bestaand veld

Om een bestaand veld te beheren, klikt u op de drie puntjes in de kolom **Acties** naast het veld dat u wilt wijzigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

De volgende acties zijn beschikbaar:

* **Bewerking/Weergave**\
  Hiermee kunt u het geselecteerde veld wijzigen.\
  Klik na het aanbrengen van uw wijzigingen op **Opslaan** om ze toe te passen.\
  <mark style="color:red;">**Opmerking**</mark>: Standaardvelden kunnen alleen worden bekeken, niet bewerkt. In deze gevallen verschijnt de optie **Bewerking** als **Weergave**.
*   **Verwijderen**\
    Verwijdert het geselecteerde veld permanent na bevestiging.\
    <mark style="color:red;">**Opmerking**</mark>: Alleen velden zonder de **Default** tag kunnen worden verwijderd.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## LOV-stamgegevens

De sectie **LOV-stamgegevens** maakt het mogelijk om dropdown-configuraties te maken met waarden uit uw stamgegevens. Deze dropdowns kunnen op zichzelf staand zijn of afhankelijk van andere dropdowns, waardoor dynamische filtering en cascaderende selecties mogelijk zijn tijdens veldvalidatie.

### Lov Lookup-configuratie maken

Een lov lookup-configuratie definieert hoe dropdown-opties worden gehaald uit een stamgegevenstabel en hoe die waarden worden weergegeven en ingevuld in documentvelden.

**Zo maakt u een nieuwe Lov Lookup-configuratie:**

1. Ga naar de sectie **LOV-stamgegevens**.
2.  Klik rechtsboven op **Lov Lookup-configuratie maken**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Configureer de volgende opties:
   * **Zoek Lov-naam op**\
     De naam van de lov lookup-configuratie.
   * **Naam van Lov-opzoekdataset**\
     Selecteer de stamgegevenstabel die voor deze lov lookup-configuratie moet worden gebruikt.
   *   **Contexttype**\
       Specificeert waar in het document de lov lookup-configuratie wordt toegepast:

       **HEADER**

       De lov lookup-configuratie wordt gebruikt in veldvalidatie. Configureer het volgende:

       * **Zoeklabelveld**\
         Selecteer de kolom waarvan de waarde in de dropdown wordt weergegeven.
       * **Zoekwaardeveld**\
         Selecteer de kolom waarvan de waarde intern wordt opgeslagen en wordt gebruikt voor filtering wanneer een selectie wordt gemaakt. Deze waarde wordt niet aan de gebruiker getoond.
       * **Buitenveld**\
         Definieert het veld in veldvalidatie dat het geselecteerde label uit de dropdown ontvangt.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       De lov lookup-configuratie wordt gebruikt binnen een documenttabel. Configureer het volgende:

       * **Contextdetail**\
         Selecteer de specifieke tabel waar deze lov lookup-configuratie actief moet zijn.
       * **Zoeklabelveld**\
         De kolom waarvan de waarde in de dropdown wordt weergegeven.
       * **Zoekwaardeveld**\
         Selecteer de kolom waarvan de waarde intern wordt opgeslagen en wordt gebruikt voor filtering wanneer een selectie wordt gemaakt. Deze waarde wordt niet aan de gebruiker getoond.
       * **Buitenveld**\
         Specificeert het doeldveld in de tabel waar het geselecteerde label wordt ingevuld.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Klik op **Opslaan** om de lov lookup-configuratie te maken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Acties voor bestaande opzoekconfiguratie

Om een bestaande lov lookup-configuratie te beheren, klikt u op de drie puntjes rechtsboven in de configuratie.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Beschikbare acties:**

* **Activeren / Deactiveren**\
  Wissel de status van de lov lookup-configuratie.
  * **Actief** configuraties zijn gemarkeerd met een **Actief** tag.
  * **Inactief** configuraties zijn gemarkeerd met een **Inactief** tag.
*   **Duplicaat**\
    Na het invoeren van een naam en op **Klaar** te klikken, wordt een kopie van de geselecteerde lov lookup-configuratie gemaakt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Bewerking / Weergave**\
  Wijzig de geselecteerde configuratie. Na het aanbrengen van wijzigingen klikt u op **Opslaan**.
*   **Verwijderen**\
    Verwijdert de configuratie permanent na bevestiging.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Nieuw veld creëren

Binnen elke lov lookup-configuratie kunt u extra velden definiëren als dropdowns die fungeren als voorfilters voor de hoofd-lov-logica.

Deze velden worden geëvalueerd voordat de hoofd-lov-dropdown wordt geladen. Op basis van de in deze velden geselecteerde waarden worden de resultaten van het hoofd-lov-veld dynamisch gefilterd—waardoor afhankelijke dropdowns mogelijk worden.\
Bijvoorbeeld, het selecteren van een land in een voorfilterveld kan de stadsopties in de hoofd-lov-dropdown verfijnen.

Naast het creëren van nieuwe velden kunt u ook bestaande velden als voorfilters gebruiken. Wanneer dit zo is geconfigureerd, zal de geselecteerde waarde in het bestaande veld de hoofd-lov-dropdown automatisch filteren.

**Om een nieuw veld toe te voegen:**

1. Open de gewenste lov lookup-configuratie.
2.  Klik rechtsboven op **Creëren**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Configureer de benodigde opties.

    **Opties voor veldconfiguratie (van toepassing op zowel HEADER- als LINE-contexten):**

    * **Opzoekveld**\
      De kolom die in de geselecteerde dataset wordt doorzocht voor dropdown-waarden.
      * **Filterveld**\
        Specificeert het veld waarvan de waarde wordt gebruikt om de resultaten van de lov lookup-configuratie vooraf te filteren voordat de hoofddropdown wordt gevuld.
      * **Filterwaarde** (optioneel)\
        Voeg statische filters toe om de opzoekresultaten verder te verfijnen.
      * **Vereist**\
        Wanneer ingeschakeld, moet dit veld worden gevuld voordat afhankelijke dropdowns kunnen worden ingevuld.
4.  Klik op **Opslaan** om het nieuwe veld te maken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Acties voor bestaand veld

Om een bestaand veld binnen een lov lookup-configuratie te beheren, klikt u op de drie puntjes in de kolom **Acties** naast het veld.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Beschikbare acties:**

* **Bewerking**\
  Wijzig het geselecteerde veld. Na wijzigingen klikt u op **Opslaan** om toe te passen.
*   **Verwijderen**\
    Verwijdert het veld permanent na bevestiging.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
