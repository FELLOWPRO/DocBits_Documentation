# Voer de DocOperator-prompt uit (automatiseringsscript)

***

Voeg deze kaart toe aan de groep **Dan** van de Workflow Builder — de acties die worden uitgevoerd zodra de When/And-voorwaarden overeenkomen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

***

## 📌 Versie-informatie

**Huidige versie:** v3 (nieuwste en aanbevolen) **Status:** ✅ Actief

**Versiegeschiedenis:**

* v2 → Originele DocOperator-implementatie
* **v3 → CURRENT** (toegevoegde parameter voor uitvoeringscontrole)
* v4 → Verouderd (functies teruggezet)

**Wat is er veranderd:** v3 heeft de optionele parameter "Voer de prompt uit" toegevoegd voor meer controle. v4 probeerde dit ongedaan te maken, maar werd verouderd.

📖 [Versiegeschiedenis en wijzigingen](../../release.md) | [Volledige kaartdatabase](../../cards-overview/export-cards-guide.md)

***

## Doel

Deze kaart voert een geautomatiseerde browseractie of script uit met behulp van DocOperator. Zie het als een robot die kan communiceren met websites of systemen, precies zoals een mens dat zou doen: klikken op knoppen, formulieren invullen, gegevens extraheren, enz.

**Voorbeeld uit de praktijk:** Uw bedrijf gebruikt een webgebaseerd aankoopsysteem. Deze kaart kan automatisch inloggen, een product zoeken, de beschikbaarheid controleren en de huidige prijs opvragen - allemaal zonder dat iemand dit handmatig hoeft te doen.

***

## Wanneer moet u deze kaart gebruiken?

Gebruik deze kaart wanneer u:

* Automatiseer taken op websites die geen API's hebben
* Gegevens uit webpagina's extraheren
* Formulieren automatisch invullen
* Log in op systemen en haal informatie op
* Automatiseer repetitieve handmatige taken
* Werk samen met oudere systemen die niet zijn geïntegreerd

**Gemeenschappelijke scenario's:**

* Log in op leverancierswebsites en ontvang realtime inventaris
* Vul automatisch formulieren in op externe systemen
* Extraheer gegevens van webpagina's die geen API's bieden
* Controleer de bezorgstatus op koerierswebsites
* Ontvang prijzen van systemen zonder API-toegang

***

## Hoe het werkt

1. **Kaart geactiveerd**: de workflow bereikt deze kaart en er wordt aan de voorwaarden voldaan
2. **Scriptstarts**: DocOperator-bot begint uw automatiseringsscript uit te voeren
3. **Botacties**: de bot voert acties uit zoals klikken, typen, scrollen, extraheren
4. **Gegevensextractie**: Bot verzamelt informatie van webpagina's
5. **Gegevens retourneren**: gegevens komen terug naar DocFlow voor gebruik in volgende kaarten
6. **Time-outafhandeling**: als het script te lang duurt, stopt het en retourneert het wat het heeft

***

## Parameters uitgelegd

### DocOperator-prompt/script

Het automatiseringsscript dat DocOperator precies vertelt wat hij moet doen

**Voorbeeld (gewoon Engels):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variabelen

Gegevens die u IN het script wilt doorgeven

**Voorbeeld:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Deze variabelen kunnen in het script worden gebruikt, zoals:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximale stappen

Hoeveel acties de bot mag uitvoeren

**Typische waarden:**

* Eenvoudige taak (zoals één prijs krijgen): 10-20 stappen
* Gemiddelde complexiteit (formulier invullen + uitpakken): 20-50 stappen
* Complexe workflow (inloggen + zoeken + valideren): 50-100 stappen

**Waarom het ertoe doet:** Voorkomt oneindige lussen en zeer langlopende scripts

### Maximaal aantal nieuwe pogingen

Als de bot een actie mislukt, hoe vaak moet hij het dan opnieuw proberen?

**Voorbeelden:**

* 1: Probeer het een keer, als het niet lukt, ga dan verder
* 3: Probeer het 3 keer voordat je het opgeeft
* 5: Zeer volhardend - probeer 5 keer

***

## Stapsgewijs voorbeeld

### Scenario: Haal leveranciersprijzen op van de website

**Scriptdefinitie:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Doorgegeven variabelen:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script met variabelen:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Verwacht resultaat:**

```
price: 45.50
quantity_available: 500
```

***

## Soorten acties die DocOperator kan uitvoeren

### Navigatie

* Ga naar URL
* Klik op koppelingen
* Druk op knoppen
* Pagina scrollen

### Formulier invullen

* Typ tekst in velden
* Selecteer vervolgkeuzelijsten
* Vink vakjes aan/uit
* Klik op knoppen

### Gegevensextractie

* Tekst van pagina lezen
* Nummers extraheren
* Tabelgegevens ophalen
* Kopieer informatie

### Wachten

* Wacht tot de pagina is geladen
* Wacht tot er elementen verschijnen
* Wacht op dynamische inhoud

### Voorwaardelijke logica

* Als er iets bestaat, doe dit dan
* Als de tekst overeenkomt, dan...
* Tel de resultaten en handel daarnaar

***

## Veelvoorkomende gebruiksscenario's

### 1. Ontvang realtime prijzen

**Scenario:** Leverancier heeft geen API, maar website toont prijzen

**Script:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Controleer de voorraadbeschikbaarheid

**Scenario:** Moet weten of de leverancier voorraad heeft

**Script:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatische formulierinzending

**Scenario:** Moet een formulier invullen op een externe site

**Script:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verificatie van gegevensinvoer

**Scenario:** Controleer gegevensovereenkomsten op twee verschillende systemen

**Script:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Configuratiestappen

### Stap 1: Maak het script

1. Bepaal wat u wilt bereiken
2. Verdeel het in kleine stapjes
3. Schrijf elke stap duidelijk op
4. Eerst handmatig testen (open de website, doe het zelf)
5. Documenteer precies waarop u klikt, waar u typt en wat u extraheert

### Stap 2: Identificeer variabelen

1. Welke gegevens veranderen tussen documenten?
2. Wat moet er in het script worden doorgegeven?
3. Definieer namen van variabelen
4. Geef op waar variabelen in het script worden gebruikt

### Stap 3: Stel parameters in

* **Maximale stappen**: Gebaseerd op scriptcomplexiteit
* **Maximum aantal nieuwe pogingen**: hoe persistent moet een bot zijn?
* **Time-out**: Hoe lang moet het wachten op pagina's?

### Stap 4: Testen

1. Test met voorbeeldgegevens
2. Controleer of de bot toegang heeft tot de website
3. Controleer of de extractie correct is
4. Controleer of variabelen goed werken

***

## Tips voor het schrijven van scripts

### Duidelijke taal

✅ **Doe:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Niet doen:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Specifieke kiezers

✅ **Doe:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Niet doen:**

```
Click somewhere
Type in a field
```

### Foutafhandeling

✅ **Doe:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Niet doen:**

```
Click "Next" (assumes it's always there)
```

***

## Problemen oplossen

### "Scripttime-out"

**Oorzaak:** Het voltooien van het script duurde te lang

**Oplossingen:**

* [ ] Verminder het aantal acties
* [ ] Verhoog de waarde voor "Maximumstappen".
* [ ] Optimaliseer het script voor snellere uitvoering
* [ ] Vereenvoudig wat u probeert te extraheren

### "Element niet gevonden"

**Oorzaak:** DocOperator kon de door u opgegeven knop/veld niet vinden

**Oplossingen:**

* [ ] Controleer of de knop-/veldnaam precies correct is
* [ ] Controleer of de lay-out van de website is gewijzigd
* [ ] Wachttijd toevoegen voordat u klikt
* [ ] Controleer of de knop alleen onder bepaalde omstandigheden verschijnt

### "Inloggen mislukt"

**Oorzaak:** Authenticatie mislukt

**Oplossingen:**

* [ ] Controleer of gebruikersnaam en wachtwoord correct zijn
* [ ] Controleer of het wachtwoord speciale tekens bevat
* [ ] Controleer of het account niet is vergrendeld
* [ ] Controleer of het inlogproces is gewijzigd

### "Gegevens niet correct geëxtraheerd"

**Oorzaak:** Het script is uitgevoerd, maar heeft verkeerde informatie opgehaald

**Oplossingen:**

* [ ] Controleer of het juiste veld is geselecteerd
* [ ] Controleer of de gegevens zich op de verwachte locatie bevinden
* [ ] Extractielogica handmatig testen
* [ ] Voeg foutopsporingsstappen toe om te verifiëren wat er op de pagina staat

### "Script loopt langzaam"

**Oorzaak:** Te veel stappen of trage website

**Oplossingen:**

* [ ] Verwijder onnodige stappen
* [ ] Optimaliseer wachttijden
* [ ] Controleer de internetverbinding
* [ ] Overweeg of er een API-alternatief bestaat

***

## Beste praktijken

✅ **Doe:**

* Test scripts grondig voordat u ze implementeert
* Houd scripts eenvoudig en doelgericht
* Voeg opmerkingen toe waarin elke stap wordt uitgelegd
* Gebruik betekenisvolle namen van variabelen
* Bewaak de prestaties van scripts
* Zorg voor een terugvalmogelijkheid voor als scripts mislukken

❌ **Niet doen:**

* Extreem lange scripts maken (>100 stappen)
* Zet gevoelige wachtwoorden in logboeken
* Vertrouw op exacte coördinaten (websites veranderen)
* Creëer lussen zonder exitvoorwaarden
* Negeer foutmeldingen

***

## Prestatietips

* **Verwijder ongebruikte stappen** - Elke stap kost tijd
* **Combineer soortgelijke acties** - Groepeer gerelateerde klikken
* **Optimaliseer wachttijden** - Gebruik alleen noodzakelijke vertragingen
* **Cachegegevens** - Haal dezelfde gegevens niet twee keer op
* **Parallelle verwerking** - Voer indien mogelijk meerdere scripts uit

***

## Beveiligingsoverwegingen

⚠️ **Belangrijk:**

* Bewaar geen wachtwoorden in DocFlow
* Gebruik veilige methoden om inloggegevens door te geven
* Registreer geen gevoelige gegevens
* Controleer wat er wordt geëxtraheerd
* Zorg ervoor dat botactiviteit wordt geregistreerd en controleerbaar is

***

## Variabelen Voorbeeld

### Beschikbare variabelen die u kunt gebruiken:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script met variabelen:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Vergelijking: wanneer DocOperator versus API gebruiken

| Situatie              | Gebruik DocOperator | Gebruik API     |
| ---------------------- | --------------- | ----------- |
| Website heeft API        | ❌ Nee            | ✅ Ja       |
| Website is interactief | ✅ Ja           | ❌ Nee        |
| Vereist inloggen         | ✅ Ja           | Hangt ervan af     |
| Heel snel nodig       | ❌ Nee            | ✅ Ja       |
| Complexe werkstroom       | ✅ Ja           | ❌Misschien niet |
| Gegevens veranderen dagelijks     | ✅ Ja           | ✅ Ja       |

***

## Gerelateerde kaarten

* **CALL\_API** - Gebruik in plaats daarvan wanneer API beschikbaar is
* **ACTION\_HTTPS\_REQUEST** - Eenvoudigere verzoeken
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Gebruik geëxtraheerde gegevens
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Controleer de status van het verzoek
