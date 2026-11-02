# DocBits-releaselevenscyclusstrategie

Met de uitrol van de aankomende minor release R1.1 introduceert DocBits een nieuwe releaselevenscyclusstrategie op basis van twee releasekanalen: VESTA en NOVA.

**NOVA** is het kanaal voor de introductie van nieuwe major en minor releases, zoals **Rx** en **Rx.y**. **VESTA** blijft de bestaande productierelease leveren.

{% hint style="success" %}
**Belangrijk: één URL voor zowel VESTA als NOVA**

Blijf uw gebruikelijke DocBits-applicatie-URL gebruiken. VESTA en NOVA hebben geen afzonderlijke toegangs-URL's: beide releasekanalen zijn bereikbaar via dezelfde standaard-URL die u al gebruikt voor de betreffende omgeving.

Om van kanaal te wisselen, gaat u naar **Settings > Company Information > Release Channel** en selecteert u **VESTA** of **NOVA**. U hoeft niet uit te loggen en opnieuw in te loggen. Uw volgende klik in de applicatie brengt u automatisch naar de release op het geselecteerde kanaal.

Controleer vóór het overstappen of beide kanalen gereed en beschikbaar zijn in uw omgeving, zoals beschreven in [Controleer de beschikbaarheid van de omgeving voordat u overstapt](#belangrijk-controleer-de-beschikbaarheid-van-de-omgeving-voordat-u-overstapt).
{% endhint %}

## Releasekanalen

| Kanaal | Rol in de levenscyclus |
| --- | --- |
| **VESTA** | Levert de huidige productierelease. |
| **NOVA** | Levert de volgende release terwijl deze de fasen van ontwikkeling, testen en beschikbaarheid voor productie doorloopt. Tijdens de parallelle productie bieden NOVA en VESTA beide live productiereleases. |

## Overzicht van de levenscyclus

![Releaselevenscyclus van DocBits VESTA en NOVA in drie fasen](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Elke cyclus bestaat uit drie fasen. Een door FELLOWPRO beheerde rollover brengt vervolgens de NOVA-productierelease naar VESTA en start de volgende cyclus.

| Fase | VESTA | NOVA | Wat dit betekent voor uw organisatie |
| --- | --- | --- | --- |
| **1. Ontwikkeling** | R1.0.x in productie | R1.1 in ontwikkeling | U blijft VESTA gebruiken terwijl de volgende release wordt voorbereid. |
| **2. QA en acceptatietests** | R1.0.x in productie | R1.1 in QA en UAT | U evalueert de komende release in de NOVA-sandbox terwijl het productiewerk op VESTA doorgaat. |
| **3. Parallelle productie** | R1.0.x in productie | R1.1.x in productie | U blijft op VESTA of stapt zelfstandig over naar NOVA wanneer u er klaar voor bent. |

Na de rollover gebruiken alle klanten VESTA R1.1.x en wordt NOVA hergebruikt voor de ontwikkeling van R1.2. Fase 1 begint dan opnieuw met deze bijgewerkte versies.

### Fase 1 — Ontwikkeling

VESTA levert de huidige productierelease, R1.0.x, terwijl de volgende release, R1.1, in NOVA wordt ontwikkeld. Uw organisatie zet haar dagelijkse werkzaamheden gedurende deze hele fase voort op VESTA.

### Fase 2 — QA en acceptatietests

De komende NOVA-release doorloopt kwaliteitsborging (QA) en gebruikersacceptatietests (UAT). U kunt de release evalueren in de NOVA-sandbox om te beoordelen hoe de wijzigingen aansluiten op de workflows van uw organisatie en u voor te bereiden op de ingebruikname.

VESTA R1.0.x blijft tijdens deze fase de productierelease. U kunt voor productiegebruik overstappen op NOVA zodra deze in fase 3 beschikbaar komt.

### Fase 3 — Parallelle productie

VESTA R1.0.x en NOVA R1.1.x zijn beide live productiereleases. Uw organisatie bepaalt of en wanneer zij overstapt op NOVA, op basis van uw behoeften en de resultaten van uw evaluatie in de sandbox.

Om NOVA tijdens deze fase in gebruik te nemen:

1. Evalueer de release in de NOVA-sandbox.
2. Controleer de releaseaankondiging of bevestig bij FELLOWPRO Support dat beide productieomgevingen gereed en beschikbaar zijn om over te stappen.
3. Bepaal wanneer uw organisatie klaar is om de nieuwe release in productie te gebruiken.
4. Ga in DocBits naar **Settings > Company Information > Release Channel** en selecteer **NOVA**.

Tijdens de parallelle productie kunt u ook terugstappen naar VESTA door naar **Settings > Company Information > Release Channel** te gaan en **VESTA** te selecteren.

Het wisselen van kanaal doet u zelf (selfservice). FELLOWPRO bepaalt niet welke klanten naar NOVA moeten overstappen. U kunt VESTA gedurende de gehele parallelle productie blijven gebruiken en de nieuwe release via de daaropvolgende rollover in gebruik nemen.

## Release-rollover en de volgende cyclus

FELLOWPRO beheert de rollover zodra de NOVA-release gereed is om de gemeenschappelijke productierelease te worden en alle klanten de geplande overgang hebben geaccepteerd:

**NOVA R1.1.x → VESTA R1.1.x**

### Voorafgaande aankondiging en acceptatie door klanten

FELLOWPRO kondigt de geplande rollover vooraf per e-mail aan bij alle klanten en vraagt hun acceptatie van de overgang. U wordt uitgenodigd om eventuele bedenkingen of bezwaren aan FELLOWPRO kenbaar te maken, zodat deze vóór de rollover kunnen worden besproken. De rollover en het hergebruik van NOVA vinden pas plaats wanneer de release gereed is en alle klanten de geplande overgang hebben geaccepteerd.

### Wat er verandert bij de rollover

| Wijziging | Resultaat |
| --- | --- |
| **De NOVA-release wordt de VESTA-release** | R1.1.x wordt voor alle klanten de gemeenschappelijke productierelease in VESTA. |
| **De vorige release wordt uitgefaseerd** | R1.0.x wordt buiten gebruik gesteld en is niet langer beschikbaar via een van beide kanalen of op enige andere wijze. |
| **NOVA wordt hergebruikt voor de volgende release** | De ontwikkeling van R1.2 begint in NOVA, waarmee fase 1 van de volgende cyclus start. |

Dezelfde drie fasen herhalen zich vervolgens met de nieuwe versienummers.

Het onderstaande diagram illustreert de hierboven beschreven releasecyclus in meer detail.

![Gedetailleerde releasecyclus van DocBits VESTA en NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Releasefrequentie

De geplande frequentie verschilt tussen major en minor releases die via NOVA worden geïntroduceerd en hotfixes die op de productiereleases in VESTA en NOVA worden toegepast.

#### Major en minor releases via NOVA

FELLOWPRO plant momenteel een cyclus van ongeveer **3–4 maanden voor major en minor releases** die via het NOVA-releasekanaal worden geïntroduceerd, zoals **Rx** en **Rx.y**. Deze schatting geldt voor de hierboven beschreven releaselevenscyclus, inclusief de daaropvolgende rollover naar VESTA en het hergebruik van NOVA voor de volgende release. Zij zegt niets over de frequentie van hotfixes.

Deze termijn weerspiegelt onze huidige planningsschatting; het is geen vast schema, geen maximale cyclusduur en geen garantie voor een release- of rolloverdatum. Het tijdstip van elke rollover en van het hergebruik van NOVA is afhankelijk van zowel **de gereedheid van de release als de acceptatie van de geplande overgang door alle klanten**. Als er extra tijd nodig is om de release gereed te maken, bedenkingen van klanten te behandelen of de acceptatie van elke klant te verkrijgen, wordt de cyclus verlengd en kan deze langer dan vier maanden duren.

FELLOWPRO communiceert elke geplande rollover vooraf. Elke indicatieve planning blijft afhankelijk van het vervuld zijn van deze voorwaarden.

#### Hotfixes in VESTA-productie

Hotfixes voor de VESTA-productierelease worden naar verwachting ongeveer **eenmaal per maand of met iets langere tussenpozen** uitgebracht. Dit is een indicatieve frequentie en geen vast schema of gegarandeerde leveringsdatum.

#### Stabilisatiehotfixes in NOVA-productie

Voor stabilisatiehotfixes in NOVA-productie kan geen algemene frequentie worden opgegeven. NOVA introduceert volledig nieuwe releases, dus het tijdstip en de frequentie van deze hotfixes zijn afhankelijk van de stabilisatiebehoeften van de betreffende release. Ze volgen daarom niet de indicatieve maandelijkse frequentie voor VESTA of de cyclus van 3–4 maanden voor major en minor releases.

## Verantwoordelijkheden en keuzevrijheid van de klant

| Overgang | Wie beheert deze | Wat u kunt verwachten |
| --- | --- | --- |
| **Overstap tussen VESTA en NOVA tijdens fase 3** | Uw organisatie | U evalueert NOVA in de sandbox en kiest of en wanneer u overstapt. Gebruik **Settings > Company Information > Release Channel** om NOVA te selecteren of tijdens de parallelle productie terug te keren naar VESTA. |
| **Rollover van NOVA R1.1.x naar VESTA R1.1.x** | FELLOWPRO | U leest de voorafgaande aankondiging per e-mail, maakt eventuele bedenkingen of bezwaren kenbaar en bevestigt uw acceptatie van de geplande overgang. FELLOWPRO gaat verder zodra de release gereed is en alle klanten hebben geaccepteerd. |

## Belangrijk: controleer de beschikbaarheid van de omgeving voordat u overstapt

Wissel alleen tussen VESTA en NOVA via **Settings > Company Information > Release Channel** wanneer releases parallel beschikbaar zijn en gereed voor gebruik in de **overeenkomstige omgeving op beide kanalen**. Beschikbaarheid in sandbox en productie moet afzonderlijk worden beoordeeld:

- **Sandbox:** U kunt overstappen van VESTA Sandbox naar NOVA Sandbox zodra de nieuwe release gereed en beschikbaar is in NOVA Sandbox, terwijl VESTA Sandbox beschikbaar blijft. Dezelfde gereedheidsvoorwaarde geldt voor het terugstappen.
- **Productie:** U kunt alleen wisselen tussen VESTA Production en NOVA Production zolang beide productiereleases parallel gereed en beschikbaar zijn. Beschikbaarheid in NOVA Sandbox betekent niet dat NOVA Production gereed is voor gebruik.

Overstappen wanneer de overeenkomstige omgeving niet gereed of beschikbaar is, kan uw werkzaamheden verstoren. FELLOWPRO verstuurt releaseaankondigingen per e-mail enkele dagen voordat releases in sandbox of productie beschikbaar komen. Controleer deze aankondigingen voordat u overstapt. Als u niet zeker weet of een overstap beschikbaar of geschikt is voor uw organisatie, neem dan contact op met FELLOWPRO Support voor bevestiging.

**Geplande beschikbaarheidsregeling:** FELLOWPRO werkt aan een Ja/Nee-regeling waarmee Support de instelling Release Channel op alleen-lezen kan zetten of het wisselen van kanaal kan inschakelen, onafhankelijk van een software-uitrol. Zodra deze regeling beschikbaar is, gebruikt Support deze om het wisselen in te schakelen wanneer de overeenkomstige omgevingen gereed zijn en de instelling anders alleen-lezen te houden. Het doel is dat klanten veilig kunnen wisselen tussen VESTA en NOVA wanneer de instelling is ingeschakeld. Zolang deze regeling niet is ingevoerd, mag een bewerkbare instelling alleen niet worden beschouwd als bevestiging dat overstappen gepast is; volg de releaseaankondigingen of bevestig dit bij Support.

## Veelgestelde vragen

### Hoe weten wij of het veilig is om te wisselen tussen VESTA en NOVA?

Controleer de releaseaankondiging voor de omgeving die u wilt gebruiken, of vraag FELLOWPRO Support te bevestigen dat overstappen gepast is. Beide overeenkomstige omgevingen moeten parallel gereed en beschikbaar zijn; gereedheid van de sandbox bevestigt niet de gereedheid van productie. Zie [Belangrijk: controleer de beschikbaarheid van de omgeving voordat u overstapt](#belangrijk-controleer-de-beschikbaarheid-van-de-omgeving-voordat-u-overstapt) hierboven voor de volledige richtlijnen, inclusief de geplande regeling voor het in- of uitschakelen van het wisselen van kanaal.

### Kunnen wij op VESTA blijven terwijl NOVA in productie beschikbaar is?

Ja. Tijdens fase 3 kunt u op VESTA blijven of overstappen op NOVA wanneer uw organisatie er klaar voor is. Bij de daaropvolgende rollover wordt de nieuwe release VESTA en wordt de vorige release uitgefaseerd.

### Hoe stappen wij over op NOVA of terug naar VESTA?

Controleer eerst of de overeenkomstige omgeving gereed en beschikbaar is op beide kanalen, zoals beschreven in [Controleer de beschikbaarheid van de omgeving voordat u overstapt](#belangrijk-controleer-de-beschikbaarheid-van-de-omgeving-voordat-u-overstapt). Beschikbaarheid in de sandbox en in productie staan los van elkaar.

Ga tijdens fase 3 in DocBits naar **Settings > Company Information > Release Channel** en selecteer **NOVA** om de nieuwe productierelease in gebruik te nemen, of **VESTA** om terug te keren naar de huidige VESTA-productierelease. Uw organisatie maakt deze keuze zelfstandig, op basis van haar behoeften en de evaluatie van NOVA in de sandbox. Deze keuze geldt zolang beide releases parallel beschikbaar zijn; de vorige VESTA-release wordt bij de rollover uitgefaseerd.

### Wanneer is NOVA beschikbaar voor productiegebruik?

NOVA wordt in fase 3 een live productierelease, na ontwikkeling en QA/UAT. Tijdens deze fase draaien VESTA en NOVA parallel in productie met verschillende softwareversies.

### Hoe worden wij over de rollover geïnformeerd en kunnen wij bezwaar maken?

FELLOWPRO stuurt alle klanten vooraf een e-mail en vraagt hun acceptatie van de geplande overgang. U wordt uitgenodigd om eventuele bedenkingen of bezwaren bij FELLOWPRO kenbaar te maken. De rollover en het hergebruik van NOVA vinden pas plaats wanneer de release gereed is en alle klanten hun acceptatie hebben gegeven.

### Kunnen wij R1.0.x na de rollover blijven gebruiken?

Nee. R1.0.x wordt bij de rollover buiten gebruik gesteld en is niet langer beschikbaar via een van beide kanalen of op enige andere wijze. R1.1.x wordt voor alle klanten de gemeenschappelijke VESTA-productierelease.

### Wat is het verschil tussen de rollover en onze overstap naar NOVA?

Uw overstap naar NOVA tijdens fase 3 is een keuze die u zelf maakt (selfservice) over het moment waarop u de nieuwe productierelease in gebruik neemt. De rollover is de daaropvolgende overgang die door FELLOWPRO wordt beheerd: NOVA R1.1.x wordt VESTA R1.1.x, de vorige release wordt uitgefaseerd en de volgende cyclus begint.

### Wat gebeurt er met NOVA na de rollover?

NOVA wordt hergebruikt voor de ontwikkeling van de volgende release, in dit voorbeeld R1.2. VESTA levert R1.1.x terwijl NOVA opnieuw de fasen ontwikkeling, QA/UAT en parallelle productie doorloopt.

### Is een major of minor release elke drie tot vier maanden gegarandeerd?

Nee. De frequentie van ongeveer 3–4 maanden voor major en minor releases die via NOVA worden geïntroduceerd, is een huidige planningsschatting, geen gegarandeerd schema en geen maximale duur. Voor de rollover en het hergebruik van NOVA zijn zowel de gereedheid van de release als de acceptatie door alle klanten vereist. Als een van beide voorwaarden meer tijd vergt, wordt de cyclus verlengd en kan deze langer dan vier maanden duren. FELLOWPRO communiceert elke geplande rollover vooraf.
