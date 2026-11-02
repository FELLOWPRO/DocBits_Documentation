# De instelling van het logistieke bedrijf controleren bij afwijkingen in goederenontvangst

Bij grootschalige inkoopprocessen kunnen gegevens afwijken van wat u verwacht. U kunt bijvoorbeeld de volgende foutmelding zien:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

De bovenstaande oorspronkelijke Engelstalige foutmelding blijft letterlijk behouden, inclusief de voorbeeldnummers. Zij meldt dat een goederenontvangst of ontvangstpositie niet is gevonden; controleer daarbij het genoemde logistieke bedrijf.

Dit soort meldingen wijst vaak op ontbrekende of afwijkende informatie in de configuratie van het logistieke bedrijf. Het logistieke bedrijf is een belangrijk onderdeel van ERP-systemen, vooral bij complexe toeleveringsketens met meerdere juridische of logistieke entiteiten.

**Waarom gebeurt dit?**

In omgevingen met meerdere entiteiten moet elke transactie, zoals inkopen, goederen ontvangen of betalingen starten, aan het juiste logistieke bedrijf worden toegewezen. Dit bedrijf bepaalt welk magazijn, distributiecentrum of onderdeel van het netwerk verantwoordelijk is voor de order en afhandeling. Een verkeerd bedrijfsnummer kan vervolgprocessen verstoren, zoals de controle van goederenontvangsten of de afhandeling van automatische incasso's.

## **Belangrijke controles:**

### 1. Het toegewezen logistieke bedrijf controleren:

Controleer in de stamgegevens of het genoemde logistieke bedrijf (hier <mark style="color:red;">XXXX</mark>) de juiste entiteit voor deze order is. Is <mark style="color:red;">XXXX</mark> de juiste bedrijfscode voor inkopen bij deze leverancier of voor deze productlijn?

### 2. De inkooporderinstellingen controleren:

Controleer of het logistieke bedrijf van de inkooporder aansluit op de bedoelde ontvangstlocatie. Bij een inconsistente inrichting kan een order onder het ene bedrijf zijn aangemaakt terwijl de goederen onder een ander bedrijf worden ontvangen.

### 3. Goederenontvangst en magazijngegevens vergelijken:

Controleer of goederenontvangst WE0000293 in het magazijn van het juiste bedrijf is geboekt. Hoort het magazijn bij een ander logistiek bedrijf, dan moet u mogelijk de configuratie corrigeren of een overdracht naar de juiste entiteit verwerken.

### 4. Integratie en consistentie van stamgegevens controleren:

Integraties tussen modules zoals Inkoop, Magazijnbeheer en Financiën vereisen consistente codes. Controleer of het logistieke bedrijf in alle relevante modules op dezelfde wijze is gedefinieerd.

### 5. Documentatie en ondersteuning raadplegen:

Raadpleeg bij aanhoudende problemen de systeemdocumentatie of het ERP-ondersteuningsteam. Zij kunnen de bedrijfsconfiguratie controleren en bepalen of aanvullende instellingen nodig zijn.

