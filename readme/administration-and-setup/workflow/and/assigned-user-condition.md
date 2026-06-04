# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/docbits_assigned_user_cond.png" alt="DocBits Assigned Gebruiker Cond"><figcaption></figcaption></figure>

**Doel**

Deze workflow-kaart beheert de uitvoering van bewerkingen op basis van de vraag of een taak of document is toegewezen aan een bepaalde gebruiker of groep gebruikers. Hij gebruikt voorwaardelijke logica om specifieke acties te triggeren of te voorkomen, waardoor hij ideaal is voor workflows die een gebruikersspecifieke afhandeling vereisen.

**Onderdelen van de kaart**

1. **Operator**
   * **Beschrijving**: Definieert de logische voorwaarde die op de gebruikerstoewijzing wordt toegepast.
   * **Opties**:
     * **IS**: Triggert de bewerking als de toegewezen gebruiker van het document of de taak overeenkomt met een gebruiker in de opgegeven lijst.
     * **IS NOT**: Triggert de bewerking als de toegewezen gebruiker van het document of de taak niet overeenkomt met een gebruiker in de opgegeven lijst.
2. **User List**
   * **Beschrijving**: Een lijst of selectie van gebruikers om mee te vergelijken met de toegewezen gebruiker.
   * **Detail**: Deze lijst kan een of meerdere gebruikers bevatten, waardoor de kaart zowel enkelvoudige als meervoudige gebruikersvoorwaarden effectief kan verwerken. De selectie kan worden gemaakt via selectievakjes, een meerkeuze-dropdown of vergelijkbare UI-elementen.

**Functionaliteit**

* **Identificatie van gebruikerstoewijzing**: Identificeert automatisch de gebruiker of gebruikers die aan een bepaalde taak of document binnen het ERP-systeem zijn toegewezen.
* **Voorwaarde-evaluatie**:
  * Met de **IS**-operator controleert de kaart of de toegewezen gebruiker zich onder de gebruikers in de User List bevindt.
  * Met de **IS NOT**-operator zorgt de kaart ervoor dat de toegewezen gebruiker zich niet onder de vermelde gebruikers bevindt.
* **Actie-uitvoering**:
  * **True-voorwaarde**: Als de gebruikerstoewijzing aan de voorwaarde voldoet (IS of IS NOT), worden relevante acties getriggerd, zoals meldingen, het starten van taken, goedkeuringen of andere workflow-stappen.
  * **False-voorwaarde**: Als niet aan de voorwaarde wordt voldaan, kan het document of de taak via een andere routing verlopen, of kunnen alternatieve acties worden opgegeven.

**Gebruikersinteracties**

* **Opzet en configuratie**: Gebruikers configureren de kaart door een operator te kiezen en de relevante gebruikers uit de User List op te geven. De opzet moet gebruiksvriendelijk en intuïtief zijn om selecties uit potentieel grote gebruikersbestanden mogelijk te maken.
* **Monitoring en rapportage**: Het ERP-systeem moet functionaliteit bieden om de door deze kaart getriggerde bewerkingen te monitoren en erover te rapporteren, met inzicht in de nauwkeurigheid van toewijzingen en de procesefficiëntie.
* **Foutafhandeling en meldingen**: Gebruikers moeten opties hebben om waarschuwingen of meldingen te ontvangen als er problemen zijn met de toewijzingen, zoals niet-toegewezen taken of fouten in de gebruikersselectie.

#### Conclusie

De workflow-kaart "Assigned User Condition" is een essentieel hulpmiddel voor het beheren van document- en taakworkflows die afhankelijk zijn van gebruikerstoewijzingen. Door voorwaarden toe te staan op basis van de vraag of een taak of document aan specifieke gebruikers is toegewezen, zorgt hij ervoor dat workflows alleen worden getriggerd door de juiste gebruikersinteracties, wat zowel de verantwoording als de taakafstemming binnen teams verbetert. Het duidelijk documenteren van deze kaart helpt gebruikers het belang ervan te begrijpen en hem effectief in hun workflows te integreren, wat zorgt voor soepele en efficiënte bewerkingen die zijn afgestemd op gebruikersrollen en -verantwoordelijkheden.
