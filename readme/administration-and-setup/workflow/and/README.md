# And: een conditiekaart kiezen

Gebruik een **And**-kaart om te bepalen of een workflow doorgaat na de **When**-trigger. Voeg de controles toe die je nodig hebt vóór de **Then**-actie. Elke kaart toont velden om in te vullen, zoals **Operator**, **Veldnaam** of **Waarde**; de schermafbeeldingen tonen de beschikbare kaartsjablonen, geen voltooide regels.

Kies in de **Workflow Builder** **Kaart toevoegen** onder **En....**. Kies links een categorie of typ een kaartnaam in **Zoekkaart**. Selecteer een kaartvoorbeeld om die aan de workflow toe te voegen. Je kunt door de voorbeeldlijst scrollen om meer kaarten te zien. Gebruik **×** om de keuzelijst te sluiten zonder een andere kaart te kiezen. Sla de workflow op nadat je de kaarten hebt ingesteld. Zie [Workflow](../README.md) voor de omringende **When**-, **En**- en **Dan**-stappen.

## Vergelijk met inkooporder

Gebruik deze kaarten om order- of factuurgegevens te vergelijken met een inkooporder, zoals eenheidsprijs, beloofde leverdatum, toeslagen of hoeveelheid. Kies de velden, de operator en eventuele tolerantie die de geselecteerde kaart vraagt. Zie [Vergelijk met inkooporder](compare-with-purchase-order/README.md) voor de losse kaarten.

<figure><img src="../../../.gitbook/assets/and-category-po-comparison-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Vergelijk met inkooporder geselecteerd; zichtbare voorbeelden vergelijken eenheidsprijs, leverdatum, toeslagen en hoeveelheid."><figcaption>Categorie Vergelijk met inkooporder in de Nederlandse Sandbox.</figcaption></figure>

## Documentveld

Kies deze categorie om een selectievakje of veldstatus te controleren, een veld met een waarde te vergelijken of twee velden met elkaar te vergelijken. Vul **Veldnaam** en **Operator** in op de gekozen kaart. Sommige vergelijkingen vragen ook om een tolerantie. Zie [Documentveld](document-field/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-field-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Documentveld geselecteerd; zichtbaar voorbeeld controleert een Docveld met Veldnaam, Operator en Waarde."><figcaption>Documentveld-controles gebruiken waarden uit het huidige document.</figcaption></figure>

## Datum en tijd

Gebruik **Datum en tijd** om een datum of tijd met een bereik te vergelijken, of **Vandaag** met een gekozen datum. Kies de **Operator** en datumwaarden op de kaart. Zie [Datum en tijd](date-and-time/README.md).

<figure><img src="../../../.gitbook/assets/and-category-date-time-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Datum en tijd geselecteerd; de voorbeelden wf_card_date_in_range en wf_card_today_compare_with_date."><figcaption>Datum en tijd biedt een bereikcontrole en een controle tegen vandaag.</figcaption></figure>

## Document

Gebruik deze kaarten als een workflow afhangt van het **documenttype** of de **suborganisatie**. Kies het type of de organisatie die op de kaart wordt genoemd. Zie [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Document geselecteerd; voorbeelden controleren het Documenttype en een Documenttype een van de volgende."><figcaption>Documentcondities controleren type of suborganisatie.</figcaption></figure>

## Logica

Deze categorie bevat controles met een beslistabel, een HTTPS-antwoord, modulebeschikbaarheid, een offerteprijs, een kanswaarde of twee waarden. Open de specifieke kaart en vul de genoemde velden in; bijvoorbeeld de HTTPS-kaart vraagt om een URL, een methode en een geaccepteerde statuscode. Zie [Logica](logic/README.md).

<figure><img src="../../../.gitbook/assets/and-category-logic-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Logica geselecteerd; voorbeelden zijn beslistabel, HTTPS-verzoek, module actief, offerte-prijs, kans en waardevergelijking."><figcaption>Logica biedt verschillende conditietypes; kies degene die bij je regel past.</figcaption></figure>

## Status

Gebruik **Status** om te controleren of een document een gekozen status heeft of of de status in een geselecteerde reeks zit. Kies de **Operator** en **Status** op de kaart. Zie [Status](status/README.md).

<figure><img src="../../../.gitbook/assets/and-category-status-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Status geselecteerd; de voorbeelden wf_card_document_status_is en wf_card_document_status_in_list."><figcaption>Statuscondities controleren de huidige documentstatus.</figcaption></figure>

## Tafel

Deze kaarten onderzoeken tabelrijen van het document. De zichtbare opties zijn datumcontroles, tekstpatronen, houdbaarheid en vergelijkingen tussen kolommen. Kies eerst de **Tabelnaam** en **Kolomnaam** voordat je een operator of patroon kiest. Zie [Tafel](table/README.md).

<figure><img src="../../../.gitbook/assets/and-category-table-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Tafel geselecteerd; zichtbare voorbeelden zijn datumcontrole, regex-patroon, houdbaarheid en kolomvergelijking."><figcaption>Tafelcondities gebruiken rijen en kolommen uit een documenttabel.</figcaption></figure>

## Vergelijk met offerteprijs

Gebruik deze kaarten om een artikel te vergelijken met offertegegevens. De zichtbare keuzes betreffen artikel-ID, leverancierstype, leveranciersartikel-ID, eenheidsprijs en eenheid. De **Operator** en datavelden hangen af van de kaart die je kiest.

<figure><img src="../../../.gitbook/assets/and-category-quote-price-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Vergelijk met offerteprijs geselecteerd; vijf voorbeelden betreffen artikel-ID, leverancierstype, leveranciersartikel-ID, eenheidsprijs en eenheid."><figcaption>Vergelijk met offerteprijs is een aparte categorie in de huidige kaartkiezer.</figcaption></figure>

## Cessionaris

Gebruik **Cessionaris** wanneer de conditie afhangt van de toegewezen gebruiker of groep. Kies of je met één gebruiker of groep wilt vergelijken of met een geselecteerde reeks. Zie [Cessionaris](assignee/README.md).

<figure><img src="../../../.gitbook/assets/and-category-assignee-nl-20261008.png" alt="Nederlandse En-kaartkiezer met Cessionaris geselecteerd; voorbeelden vergelijken toegewezen gebruiker of groep met één of meerdere keuzes."><figcaption>Cessionaris-condities controleren de gebruiker of groep die aan het document is toegewezen.</figcaption></figure>
