# Belastingcodes exporteren naar LN

## **Overzicht:**

\
Deze handleiding leidt u door het installatieproces om ervoor te zorgen dat belastingcodes correct vanuit DocBits naar LN worden geëxporteerd.



## **Enkele belastingcodes**

### **Stap 1: Lijst met waarden instellen**

1.  Ga naar **Instellingen** -> **Documentverwerking** -> **Lijst met waarden**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-nl.png" alt="Waardenlijsten in DocBits; de namen van organisatiespecifieke lijsten zijn afgeschermd."><figcaption><p>Waardenlijsten in DocBits; de namen van organisatiespecifieke lijsten zijn afgeschermd.</p></figcaption></figure>
2.  Klik op **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="Pagina Lijst met waarden met de bestaande lijsten en de knop New"><figcaption>Lijst met waarden met de bestaande lijsten</figcaption></figure>
3.  Maak een lijst met de naam `Tax_Country` en klik op **Save**.



    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Venster Nieuwe lijst met de naam Tax_Country" width="375"><figcaption>Lijst Tax_Country aanmaken</figcaption></figure>
4.  Maak de volgende drie extra lijsten aan:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Full"><figcaption>Lijst Tax_Code_Full aanmaken</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Reduced"><figcaption>Lijst Tax_Code_Reduced aanmaken</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Free"><figcaption>Lijst Tax_Code_Free aanmaken</figcaption></figure></div>
5.  Klik op een van de nieuw aangemaakte lijsten om deze te openen. Klik vervolgens op de knop **Add Row** om een nieuwe rij toe te voegen.



    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina Lijst met waarden met de knop Add Row onder de geopende lijst"><figcaption>Een rij aan de geopende lijst toevoegen</figcaption></figure>
6.  Voer de gewenste bijbehorende waarden uit **LN** in en klik op **Save** om de wijzigingen op te slaan.

    * Als u meerdere waarden hebt, kunt u op **Add More Values** klikken om ze toe te voegen.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Venster Waarden aanmaken met een LN-belastingcode in het veld Naam"><figcaption>LN-belastingcode in het veld Naam invoeren</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-nl.png" alt="Formulier voor een nieuwe waarde met suborganisatie, synoniemen en vertalingen. Er is geen waarde ingevoerd of opgeslagen; de taalselectie betreft de vertaling van de waarde."><figcaption><p>Formulier voor een nieuwe waarde met suborganisatie, synoniemen en vertalingen. Er is geen waarde ingevoerd of opgeslagen; de taalselectie betreft de vertaling van de waarde.</p></figcaption></figure></div>

    * **OPMERKING:** U vindt de belastingcodes in LN onder: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, sessie Belastingcodes per land voor Oostenrijk met de kolommen Belastingcode en Soort belasting"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Stap 2: Velden toevoegen in DocBits**

1.  Ga naar **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-nl.png" alt="Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd."><figcaption><p>Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd.</p></figcaption></figure>
2.  Kies het menu **Fields** van het documenttype waaraan u de velden wilt toevoegen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Documenttypen met het menu Velden onder elk documenttype"><figcaption>Menu Velden van het documenttype openen</figcaption></figure>
3.  Maak onder **VAT & Amounts** zes nieuwe velden aan, als volgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Tabblad Velden met de groep Btw en bedragen en de knop Nieuw aanmaken"><figcaption>Tabblad Velden: groep Btw en bedragen</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Naam</strong></td><td><strong>Titel</strong></td><td><strong>Veldtype</strong></td><td><strong>Lijst met waarden</strong></td></tr><tr><td><code>tax_country</code></td><td>Belasting land</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Belastingland verlaagd</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Belastingland Gratis</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Belastingcode</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Belastingwet verlaagd</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Belastingcode gratis</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Venster Documentveldgegevens voor tax_country met veldtype Dropdown en lijst Tax_Country"><figcaption>Veld tax_country: Dropdown, lijst Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Venster Documentveldgegevens voor tax_country_2 met titel Tax Country Reduced"><figcaption>Veld tax_country_2: Dropdown, lijst Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Venster Documentveldgegevens voor tax_country_3 met titel Tax Country Free"><figcaption>Veld tax_country_3: Dropdown, lijst Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Venster Documentveldgegevens voor tax_code_without_country met lijst Tax_Code_Full"><figcaption>Veld tax_code_without_country: Dropdown, lijst Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Venster Documentveldgegevens voor tax_code_without_country_2 met lijst Tax_Code_Reduced"><figcaption>Veld tax_code_without_country_2: Dropdown, lijst Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Venster Documentveldgegevens voor tax_code_without_country_3 met lijst Tax_Code_Free"><figcaption>Veld tax_code_without_country_3: Dropdown, lijst Tax_Code_Free</figcaption></figure></div>

4.  Klik na het opslaan van elk veld op **Save Settings** om de wijzigingen toe te passen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Tabblad Velden met de knop Save Settings boven de veldlijst"><figcaption>Save Settings om de nieuwe velden toe te passen</figcaption></figure>

### **Stap 3: Lay-out bewerken**

1.  Ga naar **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-nl.png" alt="Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd."><figcaption><p>Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd.</p></figcaption></figure>
2.  Open het menu **Edit Layout** voor het documenttype dat u wilt bewerken.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Documenttypen met de koppeling Lay-out bewerken onder elk documenttype"><figcaption>Lay-out bewerken van het documenttype openen</figcaption></figure>
3.  Selecteer de juiste **Document Origin** waarvoor u de belastingcodes wilt toepassen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder met de keuze van de documentoorsprong en de werkbalk van de sjabloon"><figcaption>Layout Builder: documentoorsprong kiezen</figcaption></figure>
4.  Scroll omlaag naar de sectie **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder met de groep Belastinggegevens en de velden in de elementenboom"><figcaption>Naar de groep Belastinggegevens scrollen</figcaption></figure>
5. Klap het keuzemenu **Form Elements** open.
6.  Gebruik in de sectie **Tax Details** de **Horizontal Separator Tool**. Sleep deze tussen de subsecties binnen de belastingsectie om ze duidelijk van elkaar te scheiden en verwarring te beperken.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt="Layout Builder met het uitgeklapte menu Formulierelementen"><figcaption>Formulierelementen uitklappen</figcaption></figure>
7. Klap het keuzemenu **Form Fields** open.
8.  Zoek naar **Tax Country** en sleep het veld naar het bijbehorende gebied.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt="Layout Builder met het veld Tax Country naar het gebied Belastinggegevens gesleept"><figcaption>Tax Country naar het gebied Belastinggegevens slepen</figcaption></figure>
9.  Zoek naar **Tax Code** en sleep het veld naar het bijbehorende gebied.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt="Layout Builder met het veld Tax Code onder Tax Country geplaatst"><figcaption>Tax Code naar het gebied Belastinggegevens slepen</figcaption></figure>
10. Sla het sjabloon op.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder met de opgeslagen sjabloon en beide belastingvelden in de groep Belastinggegevens"><figcaption>Opgeslagen sjabloon met beide belastingvelden</figcaption></figure>

### Stap 4: Controleren of alles werkt

Nadat u een nieuw document in DocBits hebt geüpload met de juiste documentinstellingen, kunt u nu de belastingcodes selecteren die u in stap 1 aan de lijsten hebt toegevoegd.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Veldvalidatie van een factuur met de gevulde keuzelijsten Tax Country en Tax Code"><figcaption>De nieuwe keuzelijsten in de veldvalidatie</figcaption></figure>

## Meerdere belastingcodes

### **Stap 1: Lijst met waarden instellen**

1.  Ga naar **Instellingen** -> **Documentverwerking** -> **Lijst met waarden**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-nl.png" alt="Waardenlijsten in DocBits; de namen van organisatiespecifieke lijsten zijn afgeschermd."><figcaption><p>Waardenlijsten in DocBits; de namen van organisatiespecifieke lijsten zijn afgeschermd.</p></figcaption></figure>
2.  Klik op **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="Pagina Lijst met waarden met de bestaande lijsten en de knop New"><figcaption>Lijst met waarden met de bestaande lijsten</figcaption></figure>
3.  Maak een lijst met de naam `Tax_Country` en klik op **Save**.



    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Venster Nieuwe lijst met de naam Tax_Country" width="375"><figcaption>Lijst Tax_Country aanmaken</figcaption></figure>
4.  Maak de volgende drie extra lijsten aan:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Full"><figcaption>Lijst Tax_Code_Full aanmaken</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Reduced"><figcaption>Lijst Tax_Code_Reduced aanmaken</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Venster Nieuwe lijst met de naam Tax_Code_Free"><figcaption>Lijst Tax_Code_Free aanmaken</figcaption></figure></div>
5.  Klik op een van de nieuw aangemaakte lijsten om deze te openen. Klik vervolgens op de knop **Add Row** om een nieuwe rij toe te voegen.



    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina Lijst met waarden met de knop Add Row onder de geopende lijst"><figcaption>Een rij aan de geopende lijst toevoegen</figcaption></figure>
6.  Voer de gewenste bijbehorende waarden uit **LN** in en klik op **Save** om de wijzigingen op te slaan.

    * Als u meerdere waarden hebt, kunt u op **Add More Values** klikken om ze toe te voegen.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Venster Waarden aanmaken met een LN-belastingcode in het veld Naam"><figcaption>LN-belastingcode in het veld Naam invoeren</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-nl.png" alt="Formulier voor een nieuwe waarde met suborganisatie, synoniemen en vertalingen. Er is geen waarde ingevoerd of opgeslagen; de taalselectie betreft de vertaling van de waarde."><figcaption><p>Formulier voor een nieuwe waarde met suborganisatie, synoniemen en vertalingen. Er is geen waarde ingevoerd of opgeslagen; de taalselectie betreft de vertaling van de waarde.</p></figcaption></figure></div>

    * **OPMERKING:** U vindt de belastingcodes in LN onder: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, sessie Belastingcodes per land voor Oostenrijk met de kolommen Belastingcode en Soort belasting"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Stap 2: Velden toevoegen in DocBits**

1.  Ga naar **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-nl.png" alt="Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd."><figcaption><p>Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd.</p></figcaption></figure>
2.  Kies het menu **Fields** van het documenttype waaraan u de velden wilt toevoegen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Documenttypen met het menu Velden onder elk documenttype"><figcaption>Menu Velden van het documenttype openen</figcaption></figure>
3.  Maak onder **VAT & Amounts** zes nieuwe velden aan, als volgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Tabblad Velden met de groep Btw en bedragen en de knop Nieuw aanmaken"><figcaption>Tabblad Velden: groep Btw en bedragen</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Naam</strong></td><td><strong>Titel</strong></td><td><strong>Veldtype</strong></td><td><strong>Waarde</strong></td></tr><tr><td><code>tax_country</code></td><td>Belasting land</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Belastingland verlaagd</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Belastingland Gratis</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Belastingcode</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Belastingwet verlaagd</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Belastingcode gratis</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Venster Documentveldgegevens voor tax_country met veldtype Dropdown en lijst Tax_Country"><figcaption>Veld tax_country: Dropdown, lijst Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Venster Documentveldgegevens voor tax_country_2 met titel Tax Country Reduced"><figcaption>Veld tax_country_2: Dropdown, lijst Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Venster Documentveldgegevens voor tax_country_3 met titel Tax Country Free"><figcaption>Veld tax_country_3: Dropdown, lijst Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Venster Documentveldgegevens voor tax_code_without_country met lijst Tax_Code_Full"><figcaption>Veld tax_code_without_country: Dropdown, lijst Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Venster Documentveldgegevens voor tax_code_without_country_2 met lijst Tax_Code_Reduced"><figcaption>Veld tax_code_without_country_2: Dropdown, lijst Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Venster Documentveldgegevens voor tax_code_without_country_3 met lijst Tax_Code_Free"><figcaption>Veld tax_code_without_country_3: Dropdown, lijst Tax_Code_Free</figcaption></figure></div>

4.  Klik na het opslaan van elk veld op **Save Settings** om de wijzigingen toe te passen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Tabblad Velden met de knop Save Settings boven de veldlijst"><figcaption>Save Settings om de nieuwe velden toe te passen</figcaption></figure>

### **Stap 3: Lay-out bewerken**

1.  Ga naar **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-nl.png" alt="Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd."><figcaption><p>Documenttypen: kies Velden bij het betreffende type. De ingestelde schakelaars zijn niet gewijzigd.</p></figcaption></figure>
2.  Open het menu **Edit Layout** voor het documenttype dat u wilt bewerken.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Documenttypen met de koppeling Lay-out bewerken onder elk documenttype"><figcaption>Lay-out bewerken van het documenttype openen</figcaption></figure>
3.  Selecteer de juiste **Document Origin** waarvoor u de belastingcodes wilt toepassen.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder met de keuze van de documentoorsprong en de werkbalk van de sjabloon"><figcaption>Layout Builder: documentoorsprong kiezen</figcaption></figure>
4.  Scroll omlaag naar de sectie **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder met de groep Belastinggegevens en de velden in de elementenboom"><figcaption>Naar de groep Belastinggegevens scrollen</figcaption></figure>
5. Klap het keuzemenu **Form Elements** open.
6.  Gebruik in de sectie Tax Details de tool **Sub Group**. Sleep deze naast een bestaand veld.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder met het gereedschap Subgroep in het menu Formulierelementen"><figcaption>Gereedschap Subgroep kiezen</figcaption></figure>
7.  Om uw subgroep een naam te geven, klikt u op de subgroep en voert u de gewenste naam in het veld **Label** in.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder met een nieuwe lege subgroep naast een bestaand veld"><figcaption>Subgroep naast een veld neerzetten</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Eigenschappenpaneel met het veld Label van de nieuwe subgroep"><figcaption>Subgroep een naam geven in het veld Label</figcaption></figure></div>
8.  Sleep de velden die bij deze groep horen naar het veld **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder met de belastingvelden verplaatst naar de nieuwe subgroep"><figcaption>Belastingvelden naar de subgroep verplaatsen</figcaption></figure>
9. Klap het keuzemenu **Fields** open.
10. Zoek naar **Tax** en sleep de betreffende velden, zoals **Tax Country** en **Tax Code**, naar de bijbehorende subgroep.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder met Tax Country en Tax Code in de subgroep"><figcaption>Tax Country en Tax Code in de subgroep</figcaption></figure>
11. Herhaal stap 5 tot en met 10 twee keer om de volgende situatie te bereiken:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder met drie belastingsubgroepen voor vol, verlaagd en vrij tarief"><figcaption>Drie subgroepen voor vol, verlaagd en vrij</figcaption></figure>
12. Sla het sjabloon op.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder met de opgeslagen sjabloon voor meerdere belastingcodes"><figcaption>Sjabloon voor meerdere belastingcodes opslaan</figcaption></figure>

### Stap 4: Controleren of alles werkt en de resulterende wijzigingen

Nadat u een nieuw document in DocBits hebt geüpload met de juiste documentinstellingen, kunt u de in stap 1 toegevoegde belastingcodes selecteren en meerdere belastingcodes toevoegen die in stap 3 zijn geconfigureerd.

* Het document begint met drie afzonderlijke secties: één voor bedragen met volledig tarief (Tax Full), één voor bedragen met verlaagd tarief (Tax Reduced) en één voor belastingvrije bedragen (Tax Free).
* Als u in een sectie op de plusknop klikt, wordt een duplicaat gemaakt, zodat u meerdere regels tegen het geselecteerde belastingtarief kunt invoeren.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Veldvalidatie met drie aparte belastingsecties en de knoppen plus en verwijderen"><figcaption>Drie belastingsecties in de veldvalidatie</figcaption></figure>

* Secties kunt u verwijderen door op de verwijderknop te klikken.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Veldvalidatie met een via de plusknop gedupliceerde belastingsectie"><figcaption>Nog een sectie toevoegen met de plusknop</figcaption></figure>

* De totaalbedragen worden berekend als de som van alle secties.
* De validatie van het totaalbedrag wordt aangepast op basis van alle belastingsecties.
* Scripts voor nieuwe secties kunnen pas worden toegepast nadat de velden aan de weergave zijn toegevoegd.

### Opmerking voor LN:

In **LN** wordt USt Position ingevuld op basis van het positienummer uit het keuzemenu Tax Code/Tax Country. Alleen het positienummer wordt naar de export gestuurd.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN, sessie Belastingregels per externe factuur met de kolom belastingpositie"><figcaption>LN: Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN, sessie Belastingregels per externe factuur met het positienummer"><figcaption>LN: het positienummer wordt als USt Position geëxporteerd</figcaption></figure>

#### **Export Mapping**

Om de Tax Line aan de Cost Line te koppelen:

1. Voeg `TaxLine` toe aan de lijst **InvoiceCostFields**.
2. Voeg het volgende item toe, volgens onderstaand voorbeeld:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="Exportmappingbestand met de vermelding ICF_TaxLine naast de factuurkostenvelden"><figcaption>Exportmapping: ICF_TaxLine = TF_position</figcaption></figure>
