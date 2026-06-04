# Document Field Comparison

<figure><img src="../../../../.gitbook/assets/docbits_workflow_doc_field_comparison.png" alt="Docbits Workflow Doc Field Comparison"><figcaption></figcaption></figure>

**Doel**

Deze workflow-kaart is ontworpen om automatisch de waarden van twee opgegeven velden binnen een document te vergelijken op basis van een gedefinieerde operator. Hij wordt gebruikt om data-integriteit af te dwingen en ervoor te zorgen dat documentgegevens voldoen aan bedrijfsregels of voorwaarden.

**Onderdelen van de kaart**

1. **Field Names**
   * **Beschrijving**: Geeft de namen op van de twee velden binnen het document die worden vergeleken.
   * **Detail**: Gebruikers moeten de exacte namen van de velden invoeren zoals ze in het systeem verschijnen. Deze velden kunnen elk gegevenstype zijn dat vergelijking ondersteunt, zoals numerieke, datum- of tekstvelden.
2. **Operator**
   * **Beschrijving**: De vergelijkingsoperator die wordt gebruikt om de relatie tussen de waarden van de twee velden te evalueren.
   * **Opties**:
     * **Equal (==)**: Controleert of de waarde van het eerste veld gelijk is aan de waarde van het tweede veld.
     * **Not Equal (!=)**: Controleert of de waarde van het eerste veld niet gelijk is aan de waarde van het tweede veld.
     * **Greater Than (>)**: Controleert of de waarde van het eerste veld groter is dan de waarde van het tweede veld.
     * **Greater Than or Equal (>=)**: Controleert of de waarde van het eerste veld groter dan of gelijk is aan de waarde van het tweede veld.
     * **Less Than (<)**: Controleert of de waarde van het eerste veld kleiner is dan de waarde van het tweede veld.
     * **Less Than or Equal (<=)**: Controleert of de waarde van het eerste veld kleiner dan of gelijk is aan de waarde van het tweede veld.

**Functionaliteit**

* **Veldselectie**: Gebruikers voeren de namen van de twee te vergelijken velden in of selecteren ze. Dit gebeurt doorgaans via een formulier of een dropdownmenu binnen de kaartopzet.
* **Operatorselectie**: Gebruikers kiezen een operator uit een lijst van beschikbare opties die definiëren hoe de velden moeten worden vergeleken.
* **Vergelijkingsuitvoering**:
  * Het systeem leest de waarden uit de opgegeven velden en past de geselecteerde operator toe om de relatie ertussen te evalueren.
  * Op basis van het resultaat van de vergelijking (true of false) kunnen vervolgacties worden getriggerd. Als een vergelijking bijvoorbeeld mislukt, kan het systeem het document markeren voor beoordeling, verdere verwerking blokkeren of verantwoordelijke partijen op de hoogte stellen.

**Gebruikersinteracties**

* **Opzet en configuratie**: Gebruikers configureren de vergelijking door veldnamen in te voeren en een operator te selecteren. Deze opzet moet eenvoudig en begeleid zijn, mogelijk met helptekst of voorbeelden.
* **Monitoring en rapportage**: Het systeem kan feedback geven over de resultaten van vergelijkingen, zoals het loggen van alle gemaakte vergelijkingen, hun uitkomsten en eventuele acties die als reactie op de vergelijkingsresultaten zijn ondernomen.
* **Foutafhandeling en meldingen**: Gebruikers ontvangen waarschuwingen als de vergelijking niet kan worden uitgevoerd (bijv. als een van de velden niet in het document wordt gevonden of niet in een vergelijkbaar formaat is).

#### Conclusie

De workflow-kaart "Document Field Comparison" is essentieel voor het behouden van gegevensnauwkeurigheid en consistentie over documenten heen in een ERP-systeem. Hij helpt controles te automatiseren die anders handmatig, foutgevoelig en tijdrovend zouden zijn, wat de efficiëntie en betrouwbaarheid in de documentverwerking verbetert. Het duidelijk documenteren van deze kaart in de handleiding van uw ERP-systeem helpt gebruikers deze functie effectief te benutten en ervoor te zorgen dat de gegevens over documenten heen consistent blijven en in overeenstemming met bedrijfsregels zijn.
