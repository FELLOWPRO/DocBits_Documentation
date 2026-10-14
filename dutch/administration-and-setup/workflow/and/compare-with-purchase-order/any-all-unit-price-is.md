# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart wordt gebruikt om de eenheidsprijs in een document te vergelijken met de eenheidsprijs in een inkooporder, om ervoor te zorgen dat de prijzen binnen de gedefinieerde tolerantieniveaus overeenkomen. De vergelijking kan acties triggeren als de eenheidsprijs niet aan de verwachtingen voldoet. **Version 4** voegt meer flexibiliteit toe door gebruikers verschillende entiteiten voor vergelijking te laten kiezen, wat een dieper controleniveau biedt over de prijs- en inkoopprocessen.

## **Onderdelen van de kaart:**

1. **Any / All:**
   * **Beschrijving**: Definieert of de voorwaarde van toepassing is op elke of alle gevallen waarin de eenheidsprijs wordt vergeleken.
   * **Opties**:
     * **Any**: Aan de voorwaarde is voldaan als een eenheidsprijs aan de opgegeven vergelijkingsvoorwaarde voldoet.
     * **All**: Aan de voorwaarde is alleen voldaan als alle eenheidsprijzen aan de opgegeven vergelijkingsvoorwaarde voldoen.
2. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde voor het vergelijken van de eenheidsprijs met de opgegeven waarde.
   * **Opties**:
     * **Equals (=)**: Verifieert of de eenheidsprijs overeenkomt met de opgegeven waarde.
     * **Not Equals (≠)**: Zorgt ervoor dat de eenheidsprijs verschilt van de opgegeven waarde.
     * **Greater Than (>)**: Verifieert of de eenheidsprijs groter is dan de opgegeven waarde.
     * **Greater or Equals (≥)**: Verifieert of de eenheidsprijs groter dan of gelijk is aan de opgegeven waarde.
     * **Lesser Than (<)**: Verifieert of de eenheidsprijs kleiner is dan de opgegeven waarde.
     * **Lesser or Equals (≤)**: Verifieert of de eenheidsprijs kleiner dan of gelijk is aan de opgegeven waarde.

## **Aanvullende onderdelen in Version 4:**

**Comparison Type:**

* **Beschrijving**: Maakt het mogelijk dat gebruikers kiezen welke entiteiten naast de eenheidsprijs worden vergeleken.
* **Opties**:
  * **Purchase Order to Document**: Vergelijkt de eenheidsprijs in de inkooporder met de eenheidsprijs in het document.
  * **Received to Document**: Vergelijkt de ontvangen hoeveelheid met de eenheidsprijs in het document.
  * **Purchase Order to Received**: Vergelijkt de eenheidsprijs in de inkooporder met de ontvangen hoeveelheid.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem vergelijkt de eenheidsprijs in het document met de eenheidsprijs in de inkooporder (of een andere geselecteerde entiteit, in Version 4) op basis van de geselecteerde operator. Als de vergelijking true is, gaat de workflow verder volgens de volgende stappen, waarbij goedkeuring wordt getriggerd of het proces wordt gestopt.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de voorwaarde true oplevert (bijv. de eenheidsprijs in het document is groter dan de opgegeven waarde), gaat de workflow verder met de true-actie (bijv. goedkeuring, documentverwerking).
  * **False-voorwaarde**: Als de voorwaarde false oplevert (bijv. de eenheidsprijs in het document voldoet niet aan de vergelijking), gaat de workflow niet verder.

## **Opzet en configuratie:**

* **Version 3-opzet:** Gebruikers configureren de kaart door de eenheidsprijs in het document te selecteren, de juiste operator te kiezen om te definiëren hoe de eenheidsprijs met de opgegeven waarde wordt vergeleken, en de waarde in te stellen waarmee wordt vergeleken. Daarnaast selecteren gebruikers of de voorwaarde van toepassing is op elke of alle gevallen van de eenheidsprijsvergelijking.
* **Version 4-opzet:** In Version 4 hebben gebruikers de aanvullende optie om de Comparison Type te selecteren. Hiermee kunnen ze de te vergelijken entiteiten definiëren, zoals Purchase Order to Document, Received to Document of Purchase Order to Received. Dit vergroot de flexibiliteit van de kaart om eenheidsprijzen in complexere scenario's te vergelijken.

## **Voorbeeldscenario:**

*   **Version 3-voorbeeld:**&#x20;

    Een factuur toont een eenheidsprijs van $50. De gerelateerde inkooporder heeft een eenheidsprijs van $45. De kaart vergelijkt de twee eenheidsprijzen met de operator "Greater Than". Omdat de eenheidsprijs in het document ($50) groter is dan de eenheidsprijs in de inkooporder ($45), triggert de workflow de true-voorwaarde (bijv. het document ter beoordeling verzenden).
* **Version 4-voorbeeld:**\
  Een factuur toont een eenheidsprijs van $50 en de gerelateerde inkooporder autoriseerde een eenheidsprijs van $45. Daarnaast is de ontvangen hoeveelheid 60 eenheden. De kaart vergelijkt de ontvangen hoeveelheid met de eenheidsprijs van het document met de operator "Greater Than". Omdat de ontvangen hoeveelheid (60) groter is dan de eenheidsprijs ($50), triggert de workflow de true-voorwaarde en wordt het document gemarkeerd voor verdere beoordeling.

## **Conclusie:**

Version 3 van de workflow-kaart "Unit Price Comparison" is ontworpen om ervoor te zorgen dat eenheidsprijzen in documenten overeenkomen met die in inkooporders, en triggert acties op basis van gedefinieerde voorwaarden. Version 4 breidt deze functionaliteit uit met complexere vergelijkingsopties, zoals het vergelijken van inkooporders met documenten, ontvangen hoeveelheden met documenten en inkooporders met ontvangen hoeveelheden. Deze toegevoegde flexibiliteit stelt organisaties in staat geavanceerdere prijs- en inkoopscenario's af te handelen, wat de controle en nauwkeurigheid in hun workflows verbetert.
