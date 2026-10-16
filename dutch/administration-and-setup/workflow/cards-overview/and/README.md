# And

Gebruik een **And**-kaart om te bepalen of een workflow na de **When**-trigger moet doorgaan. Voeg de controles toe die u nodig hebt vóór de **Then**-actie. Elke kaart toont velden die u moet invullen, zoals **Operator**, **Field Name** of **Value**; de schermafbeeldingen tonen de beschikbare kaartsjablonen, geen ingevulde regels.

Selecteer in de **Workflow Builder** onder **And...** de optie **Add Card**. Kies links een categorie, of typ een kaartnaam in **Search Card**. Selecteer een kaartvoorbeeld om het aan de workflow toe te voegen. U kunt door de voorbeeldlijst scrollen om meer kaarten te zien. Gebruik **×** om de keuzelijst te sluiten zonder een andere kaart te kiezen. Sla de workflow op nadat u de kaarten hebt geconfigureerd. Zie [Workflow](../../) voor de omliggende stappen **When**, **And** en **Then**.

## Compare with Purchase Order

Gebruik deze kaarten om order- of factuurgegevens te vergelijken met een inkooporder, zoals eenheidsprijs, toegezegde leverdatum, kosten of hoeveelheid. Kies de velden, de operator en eventuele tolerantie die de geselecteerde kaart vraagt. Zie [Compare with Purchase Order](compare-with-purchase-order/) voor de afzonderlijke kaarten.

<figure><img src="../../../../.gitbook/assets/and-category-po-comparison-en.png" alt="English And card picker with Compare with Purchase Order selected; visible previews include unit price, delivery date, charges, and quantity comparisons."><figcaption><p>Categorie Compare with Purchase Order in de Engelstalige Sandbox.</p></figcaption></figure>

## Document Field

Kies deze categorie om een selectievakje of veldstatus te controleren, een veld met een waarde te vergelijken of twee velden met elkaar te vergelijken. Vul de plaatshouders **Field Name** en **Operator** in op de gekozen kaart. Sommige vergelijkingen vragen ook om een tolerantie. Zie [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/and-category-document-field-en.png" alt="English And card picker with Document Field selected; visible previews check a checkbox, field status, field values, and two-field comparisons."><figcaption><p>Document Field-controles gebruiken waarden uit het huidige document.</p></figcaption></figure>

## Date & Time

Gebruik **Date & Time** om een datum of tijd met een bereik te vergelijken, of om **Today** met een gekozen datum te vergelijken. Selecteer de **Operator** en de datumwaarden in de kaart. Zie [Date & Time](date-and-time/).

<figure><img src="../../../../.gitbook/assets/and-category-date-time-en.png" alt="English And card picker with Date &#x26; Time selected; two previews compare a date or time with a range and compare Today with a Date."><figcaption><p>Date &#x26; Time biedt een bereikcontrole en een controle ten opzichte van vandaag.</p></figcaption></figure>

## Document

Gebruik deze kaarten wanneer een workflow afhankelijk moet zijn van het **documenttype** of de **suborganisatie**. Kies het type of de organisatie die in de kaart wordt genoemd. Zie [Document](document/).

<figure><img src="../../../../.gitbook/assets/and-category-document-en.png" alt="English And card picker with Document selected; previews check the document type and membership in a sub-organization."><figcaption><p>Documentvoorwaarden controleren het type of de suborganisatie.</p></figcaption></figure>

## Logic

Deze categorie bevat controles met een beslissingstabel, een HTTPS-respons, modulebeschikbaarheid, een geoffreerde artikelprijs, een kanswaarde of twee waarden. Open de specifieke kaart en vul de genoemde plaatshouders in; de HTTPS-kaart vraagt bijvoorbeeld om een URL, een methode en een geaccepteerde statuscode. Zie [Logic](logic/).

<figure><img src="../../../../.gitbook/assets/and-category-logic-en.png" alt="English And card picker with Logic selected; previews include decision table, HTTPS request, module active, quoted price, chance, and value comparison cards."><figcaption><p>Logic biedt verschillende soorten voorwaarden; kies het type dat bij uw regel past.</p></figcaption></figure>

## Status

Gebruik **Status** om te controleren of een document een gekozen status heeft of dat de status in een geselecteerde set valt. Kies de **Operator** en de **Status** in de kaart. Zie [Status](status/).

<figure><img src="../../../../.gitbook/assets/and-category-status-en.png" alt="English And card picker with Status selected; two previews compare Document status with a Status or a set of statuses."><figcaption><p>Statusvoorwaarden controleren de huidige status van het document.</p></figcaption></figure>

## Table

Deze kaarten onderzoeken rijen van documenttabellen. De zichtbare opties omvatten datumcontroles, tekstpatronen, houdbaarheid en vergelijkingen tussen kolommen. Selecteer de **Table name** en **Column Name** voordat u een operator of patroon kiest. Zie [Table](table/).

<figure><img src="../../../../.gitbook/assets/and-category-table-en.png" alt="English And card picker with Table selected; visible previews include date, regex pattern, shelf life, and table-column comparisons."><figcaption><p>Tabelvoorwaarden gebruiken rijen en kolommen uit een documenttabel.</p></figcaption></figure>

## Compare with Quote Price

Gebruik deze kaarten om een artikel te vergelijken met geoffreerde prijsgegevens. De zichtbare keuzes betreffen artikel-ID, leverancierstype, artikel-ID van de leverancier, eenheidsprijs en maateenheid. De **Operator** en de gegevensplaatshouders hangen af van de kaart die u selecteert.

<figure><img src="../../../../.gitbook/assets/and-category-quote-price-en.png" alt="English And card picker with Compare with Quote Price selected; five previews cover item ID, supplier type, supplier item ID, unit price, and unit of measure."><figcaption><p>Compare with Quote Price is een aparte categorie in de huidige kaartkeuzelijst.</p></figcaption></figure>

## Assignee

Gebruik **Assignee** wanneer de voorwaarde afhangt van de toegewezen gebruiker of groep. Kies of u wilt vergelijken met één gebruiker of groep of met een geselecteerde set. Zie [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/and-category-assignee-en.png" alt="English And card picker with Assignee selected; previews compare the assigned user or group with one or several choices."><figcaption><p>Assignee-voorwaarden controleren de gebruiker of groep die aan het document is toegewezen.</p></figcaption></figure>
