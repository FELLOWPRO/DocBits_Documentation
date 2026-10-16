# DocBits-releaselevenscyclusstrategie

**Beschikbaarheid van NOVA R1.1:** Sinds **16 oktober 2026** beschikbaar in de sandbox. De productierelease staat gepland voor **4 november 2026**.

DocBits gebruikt twee releasekanalen, **VESTA** en **NOVA**, om nieuwe releases te introduceren en uw organisatie de tijd te geven deze te evalueren voordat u ze in gebruik neemt. Tijdens de parallelle productie bepaalt u zelf of en wanneer u overstapt op de nieuwe release. FELLOWPRO beheert vervolgens de rollover waarmee deze release de gemeenschappelijke productierelease voor alle klanten wordt.

De versienummers in deze handleiding (R1.0.x, R1.1.x en R1.2) dienen ter illustratie. Dezelfde levenscyclus herhaalt zich bij opeenvolgende releases; `x` staat voor updates binnen een releasereeks.

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
2. Bepaal wanneer uw organisatie klaar is om de release in productie te gebruiken.
3. Stap over van VESTA naar NOVA via de instelling **Release Channel** in de DocBits-applicatie.

Deze overstap voert u zelf uit (selfservice). FELLOWPRO bepaalt niet welke klanten naar NOVA moeten overstappen. U kunt VESTA gedurende de gehele parallelle productie blijven gebruiken en de nieuwe release via de daaropvolgende rollover in gebruik nemen.

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

FELLOWPRO plant momenteel een releasecyclus van ongeveer **3–4 maanden**. Deze termijn weerspiegelt onze huidige planningsschatting; het is geen vast schema, geen maximale cyclusduur en geen garantie voor een release- of rolloverdatum.

Het tijdstip van elke rollover en van het hergebruik van NOVA is afhankelijk van zowel **de gereedheid van de release als de acceptatie van de geplande overgang door alle klanten**. Als er extra tijd nodig is om de release gereed te maken, bedenkingen van klanten te behandelen of de acceptatie van elke klant te verkrijgen, wordt de cyclus verlengd en kan deze langer dan vier maanden duren.

FELLOWPRO communiceert elke geplande rollover vooraf. Elke indicatieve planning blijft afhankelijk van het vervuld zijn van deze voorwaarden.

## Verantwoordelijkheden en keuzevrijheid van de klant

| Overgang | Wie beheert deze | Wat u kunt verwachten |
| --- | --- | --- |
| **Overstap van VESTA naar NOVA tijdens fase 3** | Uw organisatie | U evalueert NOVA in de sandbox en kiest of en wanneer u overstapt via de instelling Release Channel in de applicatie. |
| **Rollover van NOVA R1.1.x naar VESTA R1.1.x** | FELLOWPRO | U leest de voorafgaande aankondiging per e-mail, maakt eventuele bedenkingen of bezwaren kenbaar en bevestigt uw acceptatie van de geplande overgang. FELLOWPRO gaat verder zodra de release gereed is en alle klanten hebben geaccepteerd. |

## Veelgestelde vragen

### Kunnen wij op VESTA blijven terwijl NOVA in productie beschikbaar is?

Ja. Tijdens fase 3 kunt u op VESTA blijven of overstappen op NOVA wanneer uw organisatie er klaar voor is. Bij de daaropvolgende rollover wordt de nieuwe release VESTA en wordt de vorige release uitgefaseerd.

### Hoe stappen wij over op NOVA?

Zodra NOVA in productie beschikbaar is, gebruikt u de instelling **Release Channel** in de DocBits-applicatie. Uw organisatie maakt deze keuze zelfstandig, op basis van haar behoeften en de evaluatie van de release in de NOVA-sandbox.

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

### Is een nieuwe release elke drie tot vier maanden gegarandeerd?

Nee. De frequentie van ongeveer 3–4 maanden is een huidige planningsschatting, geen gegarandeerd schema en geen maximale duur. Voor de rollover en het hergebruik van NOVA zijn zowel de gereedheid van de release als de acceptatie door alle klanten vereist. Als een van beide voorwaarden meer tijd vergt, wordt de cyclus verlengd en kan deze langer dan vier maanden duren. FELLOWPRO communiceert elke geplande rollover vooraf.
