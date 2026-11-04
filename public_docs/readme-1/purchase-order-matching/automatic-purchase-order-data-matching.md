# Automatische afstemming van inkooporderdata

Docbits is een geavanceerd systeem dat is ontworpen om de afstemming van inkooporderdata (PO's) met inkomende factuurdocumenten te automatiseren. Deze tool is speciaal ontworpen voor het efficiënt beheren en verwerken van factuurgegevens binnen ERP-systemen. Deze documentatie legt de basis uit van de automatische afstemming door Docbits en definieert de specifieke regels die nodig zijn voor een geslaagde afstemming.

## **Basisprincipes van automatische afstemming in Docbits**

**Gegevensextractie:** Docbits start het proces door relevante gegevens uit gedigitaliseerde factuurdocumenten te extraheren. Doorgaans omvatten deze gegevens de artikelnummers, hoeveelheden en stuksprijzen van elke factuurregel. De nauwkeurigheid van deze extractie is cruciaal, omdat zij de basis vormt voor het daaropvolgende afstemmingsproces.

**Vergelijking met PO-data:** De geëxtraheerde gegevens worden vergeleken met de corresponderende informatie in de opgeslagen inkooporders. Docbits controleert of de artikelnummers, hoeveelheden en prijzen overeenkomen met die in de inkooporders. Voor een geslaagde afstemming moeten de gegevens in de facturen overeenkomen met de gegevens in de inkooporders, rekening houdend met de gedefinieerde tolerantiegrenzen.

**Automatische afstemming:** Op basis van de vergelijkingsresultaten voert Docbits de afstemming uit. Het systeem controleert of de afstemmingscriteria binnen de vastgestelde tolerantiegrenzen liggen. Wanneer aan deze criteria wordt voldaan, wordt de afstemming als geslaagd beschouwd.

**Rapportage:** Na voltooiing van het afstemmingsproces genereert Docbits rapporten die de status van de afstemmingen weergeven. Deze rapporten informeren over succesvol afgestemde facturen en identificeren afwijkingen.

## **Definitie van de afstemmingsregels**

**Artikelnummer:** Het artikelnummer op de factuur moet exact overeenkomen met het artikelnummer in de inkooporder. Er is geen tolerantie voor afwijkingen in de artikelnummers.

**Hoeveelheden:** De hoeveelheid geleverde goederen op de factuur kan binnen een vooraf gedefinieerd tolerantiebereik variëren. Doorgaans kan een tolerantie van ±5% acceptabel zijn om kleine verschillen in de leveringshoeveelheden op te vangen.

**Prijzen:** Prijsafwijkingen zijn toelaatbaar tot een vastgestelde drempel. Een gebruikelijke tolerantie kan ±2% van de prijs bedragen, om kleine verschillen in prijsopgaven te accepteren die voortkomen uit afrondingsverschillen of valutaschommelingen.

## **Afstemmingsstatus:**

* **Volledige afstemming:** Alle gegevenspunten (artikelnummer, hoeveelheid en prijs) liggen binnen de vastgestelde tolerantiegrenzen.
* **Gedeeltelijke afstemming:** Een of meer gegevenspunten wijken af buiten de tolerantiegrenzen, maar de afwijkingen zijn minimaal en vereisen een handmatige controle.
* **Geen afstemming:** Significante afwijkingen in een of meer gegevenspunten, die onmiddellijke correctie of verder onderzoek vereisen.

De nauwkeurige definitie van deze regels en de vaststelling van tolerantiegrenzen zijn cruciaal voor de efficiëntie van de automatische afstemming en de vermindering van handmatige ingrepen. Docbits maakt een flexibele configuratie van deze parameters mogelijk om te voldoen aan de eisen van verschillende bedrijven en branches.
