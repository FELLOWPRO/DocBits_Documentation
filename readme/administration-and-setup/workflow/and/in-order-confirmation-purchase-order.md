# In Order Confirmation Purchase Order

### Compare with Purchase Order:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logic-kaart: Quantity of Unit Price of Discount Match

Deze logic-kaart is ontworpen om automatisch te verifiëren dat de hoeveelheid, eenheidsprijs of korting die in een orderbevestiging is gedetailleerd, overeenkomt met de bijbehorende cijfers in de inkooporder. Deze verificatie zorgt voor consistentie en nauwkeurigheid tussen wat is besteld en wat de leverancier bevestigt te leveren.

#### Triggervoorwaarde

De logica wordt geactiveerd wanneer aan een van de volgende voorwaarden wordt voldaan in een orderbevestiging ten opzichte van de oorspronkelijke inkooporder:

* **Quantity**: De hoeveelheid bestelde items komt overeen met de door de leverancier bevestigde hoeveelheid.
* **Unit Price**: De afgesproken prijs per item komt overeen met de bevestiging van de leverancier.
* **Discount**: Eventuele toegepaste kortingen zijn consistent tussen de inkooporder en de orderbevestiging.

#### Uitkomsten

* **Equals**: Als de hoeveelheid, eenheidsprijs of korting van de orderbevestiging exact overeenkomt met de inkooporder, beschouwt het systeem de bevestiging als geldig en gaat het door met de volgende stappen in het inkoopproces.
* **Not Equal**: Als er een afwijking is in de hoeveelheid, eenheidsprijs of korting, markeert het systeem de orderbevestiging voor handmatige beoordeling. Dit zorgt ervoor dat eventuele afwijkingen worden opgelost voordat er wordt verdergegaan.

#### Voordelen

* **Nauwkeurigheid en consistentie**: Behoudt nauwkeurigheid in het inkoopproces en zorgt ervoor dat betalingen en leveringen op basis van correcte cijfers worden gedaan.
* **Efficiëntie**: Automatiseert het verificatieproces, wat de noodzaak van handmatige controles vermindert en de orderverwerking versnelt.
* **Kostenbeheersing**: Helpt te veel betalen of onjuiste leveringen te voorkomen door afwijkingen vroeg in het proces op te sporen.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Vergelijkingsparameters definiëren**: Stel de specifieke velden (hoeveelheid, eenheidsprijs, korting) in waarop de logic-kaart op een match controleert.
2. **Verificatie automatiseren**: Configureer het systeem om deze details automatisch te vergelijken bij ontvangst van een orderbevestiging.
3. **Waarschuwingen aanpassen**: Bepaal de workflow voor het afhandelen van afwijkingen, inclusief het aanpassen van waarschuwingen voor handmatige beoordeling.

Deze logic-kaart is essentieel om ervoor te zorgen dat de details van een orderbevestiging overeenkomen met de oorspronkelijke inkooporder, wat de integriteit van de inkoopcyclus waarborgt. \`\`
