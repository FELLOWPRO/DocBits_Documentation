# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze kaart is ontworpen om acties op documenten te beheren afhankelijk van hun type, waarbij eenvoudige voorwaardelijke logica (is/is not) wordt gebruikt om specifieke workflows te triggeren of te voorkomen. Dit maakt nauwkeurige controle mogelijk over hoe verschillende soorten documenten binnen het ERP-systeem worden verwerkt.

## **Onderdelen van de kaart:**

1. **Operator**
   * **Beschrijving**: Bepaalt de voorwaardelijke logica die op de documenttypen wordt toegepast.
   * **Opties**:
     * **is**: De bewerking wordt getriggerd als het type van het document overeenkomt met een van de opgegeven typen in de lijst.
     * **is not**: De bewerking wordt getriggerd als het type van het document met geen van de vermelde typen overeenkomt.
2. **Document Types List**
   * **Beschrijving**: Geeft een lijst op van documenttypen waarop de voorwaarde van toepassing is.
   * **Detail**: Dit omvat een verscheidenheid aan documenttypen, zoals "Invoice", "Purchase Order", enz., op basis waarvan de voorwaarde (is/is not) wordt geëvalueerd.

## Functionaliteit:

* **Voorwaarde-evaluatie:** Het systeem controleert of het documenttype overeenkomt met de operatorvoorwaarde (is of is not) ten opzichte van de opgegeven lijst van documenttypen.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Als het documenttype aan de opgegeven voorwaarde voldoet (ofwel is, ofwel is not in de lijst), gaat de workflow verder. Dit kan processen triggeren zoals documentgoedkeuringen, specifieke validaties of routeringsacties.
  * **False-voorwaarde:**\
    Als het documenttype niet aan de voorwaarde voldoet, worden alternatieve acties uitgevoerd, zoals het afkeuren van het document of het stoppen van de workflow.

## Opzet en configuratie:

* Gebruikers configureren de kaart door het documenttypeveld te selecteren en de operator (is of is not) te definiëren. Vervolgens geven ze de lijst van documenttypen op waarmee wordt vergeleken. De opzet is eenvoudig en bestaat uit dropdownmenu's voor de veld- en operatorselectie en een veld voor het invoeren van de lijst van documenttypen.

## Conclusie:

De workflow-kaart "Document Type Condition" speelt een cruciale rol bij het beheren van documentgebaseerde bewerkingen met precisie en flexibiliteit. Door eenvoudige voorwaardelijke logica te gebruiken, helpt hij ervoor te zorgen dat documenten op de juiste manier worden verwerkt, wat de efficiëntie en naleving verbetert. Het duidelijk documenteren van deze kaart helpt gebruikers te begrijpen hoe ze deze effectief kunnen implementeren en benutten, waardoor het een waardevol onderdeel van de documentatie van uw ERP-systeem wordt.
