# Automatische Afstemming van Inkoopordergegevens

Docbits is een geavanceerd systeem dat is ontworpen om de afstemming van inkoopordergegevens (PO's) met binnenkomende factuurdocumenten te automatiseren. Deze tool is specifiek ontworpen voor efficiënt beheer en verwerking van factuurgegevens binnen ERP-systemen. Deze documentatie legt de basisprincipes van automatische afstemming via Docbits uit en definieert de specifieke regels die nodig zijn voor succesvolle afstemming.

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice_3.svg" alt="DocBits Aankoop Bestelling Factuur 3"><figcaption></figcaption></figure>

## **Fundamentele Principes van Automatische Afstemming in Docbits**

**Gegevensextractie:** Docbits begint het proces door relevante gegevens uit gedigitaliseerde factuurdocumenten te extraheren. Meestal omvatten deze gegevens artikelnummers, hoeveelheden en eenheidsprijzen van elke factuurregel. De nauwkeurigheid van deze extractie is cruciaal, omdat het de basis vormt voor het daaropvolgende afstemmingsproces.

**Vergelijking met PO-gegevens:** De geëxtraheerde gegevens worden vergeleken met de overeenkomstige informatie in de opgeslagen inkooporders. Docbits controleert of de artikelnummers, hoeveelheden en prijzen overeenkomen met die in de PO's. Voor een succesvolle afstemming moeten de gegevens in de facturen overeenkomen met de gegevens in de inkooporders, rekening houdend met gedefinieerde tolerantiedrempels.

**Automatische Afstemming:** Op basis van de vergelijkingsresultaten voert Docbits de afstemming uit. Het systeem controleert of de afstemmingscriteria binnen de ingestelde tolerantielimieten vallen. Als aan deze criteria wordt voldaan, wordt de afstemming als succesvol beschouwd.

**Rapportage:** Na voltooiing van het afstemmingsproces genereert Docbits rapporten die de status van de afstemmingen tonen. Deze rapporten informeren over succesvol afgestemde facturen en identificeren die met afwijkingen.

## **Definitie van Afstemmingsregels**

**Artikelnummer:** Het artikelnummer op de factuur moet exact overeenkomen met het artikelnummer in de inkooporder. Er is geen tolerantie voor afwijkingen in artikelnummers.

**Hoeveelheden:** De hoeveelheid geleverde goederen op de factuur kan variëren binnen een vooraf gedefinieerd tolerantiebereik. Meestal kan een tolerantie van ±5% acceptabel zijn om rekening te houden met kleine verschillen in leveringshoeveelheden.

**Prijzen:** Prijsafwijkingen zijn toelaatbaar tot een ingestelde drempel. Een gebruikelijke tolerantie kan ±2% van de prijs zijn om kleine verschillen in prijsopgaven te accepteren die voortkomen uit afrondingsverschillen of valutafluctuaties.

## **Afstemmingsstatus:**

* **Volledige Afstemming:** Alle gegevenspunten (artikelnummer, hoeveelheid en prijs) liggen binnen de ingestelde tolerantielimieten.
* **Gedeeltelijke Afstemming:** Een of meer gegevenspunten wijken af buiten de tolerantielimieten, maar de afwijkingen zijn minimaal en vereisen handmatige controle.
* **Geen Afstemming:** Significante afwijkingen in een of meer gegevenspunten die onmiddellijke correctie of verder onderzoek vereisen.

De precieze definitie van deze regels en het instellen van tolerantielimieten zijn cruciaal voor de efficiëntie van de automatische afstemming en de vermindering van handmatige interventies. Docbits biedt flexibele configuratie van deze parameters om te voldoen aan de behoeften van verschillende bedrijven en industrieën.
