# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/docbits_single_assigned_user.png" alt="DocBits Single Assigned Gebruiker"><figcaption></figcaption></figure>

**Doel**

Deze workflow-kaart faciliteert bewerkingen op basis van de toewijzing van een taak of document aan één enkele, specifieke gebruiker. Met een directe voorwaardelijke-logicabenadering beheert hij workflows die gerichte gebruikersbetrokkenheid vereisen, en zorgt zo voor precisie in gebruikersgebaseerde taakafhandeling.

**Onderdelen van de kaart**

1. **Operator**
   * **Beschrijving**: Geeft de logica op die op de gebruikerstoewijzing wordt toegepast.
   * **Opties**:
     * **IS**: Triggert de bewerking als de toegewezen gebruiker van het document of de taak overeenkomt met de opgegeven gebruiker.
     * **IS NOT**: Triggert de bewerking als de toegewezen gebruiker niet overeenkomt met de opgegeven gebruiker.
2. **User**
   * **Beschrijving**: Maakt de selectie mogelijk van één enkele gebruiker waarmee de toegewezen gebruiker wordt vergeleken.
   * **Detail**: Dit betreft een eenvoudig dropdown- of autoaanvulveld waarin telkens één gebruiker kan worden geselecteerd.

**Functionaliteit**

* **Identificatie van gebruikerstoewijzing**: Identificeert de gebruiker die momenteel aan een specifieke taak of document is toegewezen.
* **Voorwaarde-evaluatie**:
  * Voor de **IS**-operator controleert de kaart of de toegewezen gebruiker dezelfde is als de geselecteerde gebruiker.
  * Voor de **IS NOT**-operator verifieert hij dat de toegewezen gebruiker anders is dan de geselecteerde gebruiker.
* **Actie-uitvoering**:
  * **True-voorwaarde**: Als de toewijzing aan de ingestelde voorwaarde voldoet (IS of IS NOT), triggert hij vooraf gedefinieerde acties, zoals het doorgaan met goedkeuringen, het starten van verdere taken, het verzenden van meldingen of andere gerelateerde workflows.
  * **False-voorwaarde**: Als niet aan de voorwaarde wordt voldaan, kan het systeem de taak omleiden, deze ter beoordeling vasthouden of alternatieve vooraf gedefinieerde acties triggeren.

**Gebruikersinteracties**

* **Opzet en configuratie**: Gebruikers stellen de kaart in door een operator te kiezen en een gebruiker uit het gebruikersveld te selecteren. Deze opzet moet eenvoudig zijn, zodat de gebruiker gemakkelijk te selecteren en te configureren is.
* **Monitoring en rapportage**: Biedt hulpmiddelen om de prestaties van de kaart te monitoren, zoals het volgen van welke taken door specifieke gebruikerstoewijzingen worden getriggerd en de uitkomsten van deze triggers.
* **Foutafhandeling en meldingen**: Biedt mechanismen om gebruikers te waarschuwen als taken onjuist worden toegewezen of als er operationele fouten optreden door toewijzingsproblemen.

#### Conclusie

De workflow-kaart "Single Assigned User Condition" is essentieel voor nauwkeurig, gebruikersspecifiek document- en taakbeheer binnen een ERP-systeem. Hij vereenvoudigt workflows door zich te richten op individuele gebruikerstoewijzingen, en zorgt er zo voor dat acties alleen worden uitgevoerd wanneer dat passend is, op basis van de rol en verantwoordelijkheden van de gebruiker. Het duidelijk documenteren van deze kaart helpt gebruikers de toepassing ervan te begrijpen, zodat ze hem effectief in hun dagelijkse werkzaamheden kunnen implementeren en beheren. Deze documentatie zorgt ervoor dat alle potentiële gebruikers het doel van de kaart gemakkelijk kunnen begrijpen en hem naadloos in hun workflows kunnen integreren.
