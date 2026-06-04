# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/docbits_doc_type_op_one_of.png" alt="DocBits Doc Type Op One Of"><figcaption></figcaption></figure>

**Doel**

Deze kaart is ontworpen om acties op documenten te beheren afhankelijk van hun type, waarbij eenvoudige voorwaardelijke logica (is/is not) wordt gebruikt om specifieke workflows te triggeren of te voorkomen. Dit maakt nauwkeurige controle mogelijk over hoe verschillende soorten documenten binnen het ERP-systeem worden verwerkt.

**Onderdelen van de kaart**

1. **Operator**
   * **Beschrijving**: Bepaalt de voorwaardelijke logica die op de documenttypen wordt toegepast.
   * **Opties**:
     * **is**: De bewerking wordt getriggerd als het type van het document overeenkomt met een van de opgegeven typen in de lijst.
     * **is not**: De bewerking wordt getriggerd als het type van het document met geen van de vermelde typen overeenkomt.
2. **Document Types List**
   * **Beschrijving**: Geeft een lijst op van documenttypen waarop de voorwaarde van toepassing is.
   * **Detail**: Dit kan een verscheidenheid aan documenttypen omvatten, zoals "Invoice", "Purchase Order", "Contract", "Employee Record", enz., op basis waarvan de voorwaarde (is/is not) wordt geëvalueerd.

**Functionaliteit**

* **Documentidentificatie**: Het systeem identificeert eerst het type van elk binnenkomend of bestaand document op basis van vooraf gedefinieerde attributen of metadata.
* **Voorwaarde-evaluatie**:
  * Als de operator **is** is, controleert de kaart of het documenttype in de opgegeven lijst staat.
  * Als de operator **is not** is, controleert de kaart of het documenttype niet in de lijst staat.
* **Actie-triggering**: Afhankelijk van het resultaat van de voorwaarde-evaluatie:
  * **True**: Start de bijbehorende bewerkingen of workflows als aan de voorwaarde wordt voldaan.
  * **False**: Het proces wordt overgeslagen of een alternatieve bewerking wordt getriggerd als niet aan de voorwaarde wordt voldaan.
* **Integratie en automatisering**: Integreert naadloos met andere systeemonderdelen, zodat de documentafhandeling wordt geautomatiseerd en voldoet aan de workflows en beleidsregels van de organisatie.

**Gebruikersinteracties**

* **Configuratie**: Gebruikers moeten de operator opgeven en de documenttypen vermelden bij het opzetten van de kaart. Deze opzet kan interface-elementen zoals dropdowns of selectievakjes omvatten om documenttypen en operatoren te selecteren.
* **Monitoring en aanpassingen**: Gebruikers kunnen de uitkomsten en effectiviteit van deze kaart monitoren via logs en rapporten die door het ERP-systeem worden gegenereerd. Aanpassingen aan de lijst of de operator kunnen worden gemaakt op basis van veranderende zakelijke behoeften.
* **Foutafhandeling en feedback**: Biedt feedbackmechanismen voor fouten die tijdens de bewerking optreden. Gebruikers kunnen waarschuwingen instellen voor wanneer voorwaarden mislukken, wat zorgt voor snelle aandacht voor problemen.

#### Conclusie

De workflow-kaart "Document Type Condition" speelt een cruciale rol bij het beheren van documentgebaseerde bewerkingen met precisie en flexibiliteit. Door eenvoudige voorwaardelijke logica te gebruiken, helpt hij ervoor te zorgen dat documenten op de juiste manier worden verwerkt, wat de efficiëntie en naleving verbetert. Het duidelijk documenteren van deze kaart helpt gebruikers te begrijpen hoe ze deze effectief kunnen implementeren en benutten, waardoor het een waardevol onderdeel van de documentatie van uw ERP-systeem wordt.
