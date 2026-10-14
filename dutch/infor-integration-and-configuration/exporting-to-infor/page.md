# Page

## **Overzicht:**

\
Deze gids leidt je door het installatieproces om ervoor te zorgen dat belastingcodes correct worden geëxporteerd van DocBits naar LN.

## **Enkele Belastingcodes**

### **Stap 1: Lijst met waarden instellen**

1. Ga naar **Instellingen** -> **Documentverwerking** -> **Lijst met waarden**.
2. Klik op **Nieuw**.
3. Maak een lijst met de naam `Tax_Country` en klik op **Opslaan**.
4. Maak de volgende drie extra lijsten aan:
   * `Tax_Code_Full`
   * `Tax_Code_Reduced`
   * `Tax_Code_Free`
5. Klik op een van de nieuw aangemaakte lijsten om deze te openen. Druk vervolgens op de knop **Rij toevoegen** om een nieuwe rij toe te voegen.
6. Voer de gewenste respectieve waarden in van **LN** en druk op **Opslaan** om de wijzigingen op te slaan.
   * Als je meerdere waarden hebt, kun je op **Meer waarden toevoegen** klikken om ze toe te voegen.
   * **OPMERKING:** Je kunt de belastingcodes in LN vinden onder: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

### **Stap 2: Velden toevoegen in DocBits**

1. Navigeer naar **Instellingen** -> **Algemene Instellingen** -> **Documenttypen**.
2. Kies het menu **Velden** dat overeenkomt met het documenttype waarin je de velden wilt toevoegen.
3. Onder **Belastingdetails**, maak zes nieuwe velden aan als volgt:

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Naam</strong></td><td><strong>Titel</strong></td><td><strong>Veldtype</strong></td><td><strong>Lijst met waarden</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

4. Na het opslaan van elk veld, klik op **Instellingen opslaan** om de wijzigingen toe te passen.

### **Stap 3: Lay-out bewerken**

1. Ga naar **Instellingen** -> **Algemene Instellingen** -> **Documenttypen**.
2. Open het menu **Bewerk lay-out** voor het documenttype dat je wilt bewerken.
3. Selecteer de juiste **Documentherkomst** waarvoor je de belastingcodes wilt toepassen.
4. Scroll naar beneden naar de sectie **Tax Details**.
5. Breid het dropdownmenu **Vormelementen** uit.
6. In de sectie **Tax Details** gebruik je de **Horizontal Separator Tool**. Sleep en laat deze vallen tussen de subsecties binnen de belastingsectie om ze duidelijk te scheiden en verwarring te verminderen.
7. Breid het dropdownmenu **Formuliervelden** uit.
8. Zoek naar **Tax Country** en sleep het veld naar het respectieve gebied.
9. Zoek naar **Tax Code** en sleep het veld naar het bijbehorende gebied.
10. Sla de sjabloon op.

### Stap 4: Controleer of alles werkte

Na het uploaden van een nieuw document in DocBits met de juiste documentinstellingen geselecteerd, zou je nu in staat moeten zijn om de belastingcodes te selecteren die je in stap 1 aan de lijsten hebt toegevoegd.

## Meerdere Belastingcodes

### **Stap 1: Lijst met waarden instellen**

1. Ga naar **Instellingen** -> **Documentverwerking** -> **Lijst met waarden**.
2. Klik op **Nieuw**.
3. Maak een lijst met de naam `Tax_Country` en klik op **Opslaan**.
4. Maak de volgende drie extra lijsten aan:
   * `Tax_Code_Full`
   * `Tax_Code_Reduced`
   * `Tax_Code_Free`
5. Klik op een van de nieuw aangemaakte lijsten om deze te openen. Druk vervolgens op de knop **Rij toevoegen** om een nieuwe rij toe te voegen.
6. Voer de gewenste respectieve waarden in van **LN** en druk op **Opslaan** om de wijzigingen op te slaan.
   * Als je meerdere waarden hebt, kun je op **Meer waarden toevoegen** klikken om ze toe te voegen.
   * **OPMERKING:** Je kunt de belastingcodes in LN vinden onder: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

### **Stap 2: Velden toevoegen in DocBits**

1. Navigeer naar **Instellingen** -> **Algemene Instellingen** -> **Documenttypen**.
2. Kies het menu **Velden** dat overeenkomt met het documenttype waarin je de velden wilt toevoegen.
3. Onder **Belastingdetails**, maak zes nieuwe velden aan als volgt:

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Naam</strong></td><td><strong>Titel</strong></td><td><strong>Veldtype</strong></td><td><strong>Waarde</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

4. Na het opslaan van elk veld, klik op **Instellingen opslaan** om de wijzigingen toe te passen.

### **Stap 3: Lay-out bewerken**

1. Ga naar **Instellingen** -> **Algemene Instellingen** -> **Documenttypen**.
2. Open het menu **Bewerk lay-out** voor het documenttype dat je wilt bewerken.
3. Selecteer de juiste **Documentherkomst** waarvoor je de belastingcodes wilt toepassen.
4. Scroll naar beneden naar de sectie **Tax Details**.
5. Breid het dropdownmenu **Vormelementen** uit.
6. In de sectie Tax Details gebruik je de **Sub Group** Tool. Sleep en laat deze vallen naast een bestaand veld.
7. Om je subgroep een naam te geven, klik op de subgroep en voer je gewenste naam in het **Label** veld in.
8. Sleep en laat de velden die bij deze groep horen in het **Sub Group** veld vallen.
9. Breid het dropdownmenu **Velden** uit.
10. Zoek naar **Tax** en sleep de respectieve velden, zoals **Tax Country** en **Tax Code**, naar de bijbehorende subgroep.
11. Herhaal stappen 5 tot en met 10 2 keer om de volgende staat te bereiken:
12. Sla de sjabloon op.

### Stap 4: Controleer of alles werkte en resulterende wijzigingen

Na het uploaden van een nieuw document in DocBits met de juiste documentinstellingen geselecteerd, kun je de belastingcodes selecteren die je in stap 1 hebt toegevoegd en meerdere belastingcodes toevoegen die in stap 3 zijn geconfigureerd.

* Het document begint met drie verschillende secties: één voor belasting volledige bedragen, één voor belasting verlaagde bedragen en één voor belastingvrije bedragen.
* Door op de plusknop binnen een sectie te klikken, wordt een duplicaat gemaakt, zodat meerdere indieningen tegen het geselecteerde belastingtarief mogelijk zijn.
* Secties kunnen worden verwijderd door op de verwijderknop te klikken.
* Totale bedragen worden berekend als een som van alle secties.
* Validatie van het totale bedrag wordt aangepast op basis van alle belastingsecties.
* Scripts voor nieuwe secties kunnen alleen worden toegepast nadat velden aan de weergave zijn toegevoegd.

### Opmerking voor LN:

In **LN** wordt de USt-positie ingevuld op basis van het positiem nummer uit het dropdownmenu Tax Code/Tax Country. Alleen het positiem nummer wordt verzonden voor export.

#### **Export Mapping**

Om de belastingregel aan de kostenregel te koppelen:

1. Voeg `TaxLine` toe aan de **InvoiceCostFields** lijst.
2. Voeg de volgende invoer toe, volgens het onderstaande voorbeeld:\
   `ICF_TaxLine = TF_position`

**Voorbeeld:**

```
InvoiceCostFields=TaxLine,LineNumber,LedgerAccount,DebitCredit,Amount,TransactionReference,Dimension1,Dimension2,Dimension3,Dimension4,Dimension5,Dimension6,Dimension7,Dimension8,Dimension9,Dimension10,Dimension11,Dimension12
ICF_LineNumber=auto
ICF_TaxLine=TF_position
ICF_LedgerAccount=TF_ledger_account
ICF_DebitCredit=invoice_type
ICF_Amount=TF_amount
ICF_Dimension1=TF_dimension_1
ICF_Dimension2=TF_dimension_2
ICF_Dimension3=TF_dimension_3
ICF_Dimension4=TF_dimension_4
ICF_Dimension5=TF_dimension_5
ICF_Dimension6=TF_dimension_6
ICF_Dimension7=TF_dimension_7
ICF_Dimension8=TF_dimension_8
ICF_Dimension9=TF_dimension_9
ICF_Dimension10=TF_dimension_10
ICF_Dimension11=TF_dimension_11
ICF_Dimension12=TF_dimension_12
ICF_Quantity1=TF_quantity
ICF_Quantity2=TF_quantity2
ICF_TransactionReference=TF_Buchungsreferenz
```
