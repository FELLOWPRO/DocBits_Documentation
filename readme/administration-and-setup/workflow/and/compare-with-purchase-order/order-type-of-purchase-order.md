# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om het ordertype van een inkooporder te vergelijken met een opgegeven waarde. De kaart controleert of het ordertype van de inkooporder aan de opgegeven voorwaarde voldoet (bijv. of het gelijk is aan, niet gelijk is aan, groter is dan of aan een andere voorwaarde voldoet) om ervoor te zorgen dat de inkooporder correct is geclassificeerd. Deze vergelijking kan acties triggeren op basis van specifieke voorwaarden, zoals het omleiden van de order voor verdere beoordeling of goedkeuring als er afwijkingen worden gevonden.

## **Onderdelen van de kaart:**

1. **Any/All:**
   * **Beschrijving**: Definieert of de voorwaarde van toepassing is op elke of alle inkooporders die in de workflow worden geëvalueerd.
   * **Opties**:
     * **Any**: Aan de voorwaarde is voldaan als een van de inkooporders overeenkomt met de opgegeven voorwaarde.
     * **All**: Aan de voorwaarde is alleen voldaan als alle inkooporders aan de opgegeven voorwaarde voldoen.
2. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde die wordt toegepast om het ordertype met een opgegeven waarde te vergelijken.
   * **Opties**:
     * **Equals (=)**: Controleert of het ordertype overeenkomt met de opgegeven waarde.
     * **Not Equals (≠)**: Zorgt ervoor dat het ordertype verschilt van de opgegeven waarde.
3. **Order Type:**
   * **Beschrijving**: Geeft de waarde op waarmee het ordertype van de inkooporder wordt vergeleken.
   * **Detail**: De waarde moet overeenkomen met het ordertype of de classificatie in het systeem.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem evalueert het ordertype van de inkooporder ten opzichte van de opgegeven voorwaarde met behulp van de geselecteerde operator. Als het ordertype overeenkomt (of niet overeenkomt) met de opgegeven waarde, gaat de workflow dienovereenkomstig verder.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de voorwaarde true oplevert (bijv. het ordertype komt overeen met de opgegeven waarde), gaat de workflow verder en worden mogelijk aanvullende acties of verwerkingsstappen getriggerd.
  * **False-voorwaarde**: Als de voorwaarde false oplevert (bijv. het ordertype komt niet overeen met de opgegeven waarde), gaat de workflow niet verder.

## **Opzet en configuratie:**

* Gebruikers configureren de kaart door het ordertypeveld van de inkooporder te selecteren en de operator te kiezen die definieert hoe het ordertype wordt vergeleken. Vervolgens stellen ze de opgegeven waarde in en bepalen ze of de voorwaarde op elke of alle inkooporderregels van toepassing is.

## **Voorbeeldscenario:**

* Een inkooporder heeft het ordertype "Standard". De workflow is geconfigureerd om te controleren of het ordertype "Urgent" is. Met de operator "Equals" vergelijkt de kaart het ordertype en stelt vast dat het niet overeenkomt met de opgegeven waarde, waardoor de workflow de order vanwege de mismatch ter beoordeling verzendt.

## **Conclusie:**

De workflow-kaart "Order Type of Purchase Order" zorgt ervoor dat inkooporders correct worden geclassificeerd volgens hun opgegeven ordertype. Door de vergelijking van ordertypen te automatiseren, kunnen organisaties ervoor zorgen dat inkooporders volgens hun verwachte classificaties worden verwerkt, wat helpt om naleving af te dwingen en inkoopworkflows te stroomlijnen.
