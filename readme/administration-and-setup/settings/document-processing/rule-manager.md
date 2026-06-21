# Regelbeheer

Dit document biedt een uitgebreide uitleg van de conflictoplossingsregels die in het DocBits-factuursysteem worden gebruikt. Deze regels zijn ontworpen om automatisch afwijkingen tussen factuurgegevens en inkooporderdata (PO) af te handelen en een nauwkeurige financiële afstemming te garanderen. Het systeem past deze regels toe om factuurregels, kosten en belastingen te verwerken en genereert waar nodig passende aanpassingen of notities.

**Structuur van de regels**

1. **Metadata**\
   • **version:** Identificeert de versie van het mapping-bestand.\
   • **revision:** Revisienummer om wijzigingen bij te houden.\
   • **author:** Geeft de maker van het mapping-bestand aan.\
   • **description:** Een korte beschrijving van het doel van het bestand.\
   • **created\_at & updated\_at:** Tijdstempels voor de creatie en de laatste update van het bestand.
2. **Exportconfiguratie**\
   De sectie exportconfiguratie definieert de toewijzing tussen de gegevensvelden in het systeem en de corresponderende velden in de exportbestanden.\
   • **Header:** Definieert de koptekstvelden voor de geëxporteerde factuurgegevens.\
   • **Tax Lines:** Geeft de velden voor belastingregels in de export aan.\
   • **Order Header Charges:** Wijst velden toe die verband houden met aanvullende kosten op het niveau van de orderkop.\
   • **Receipt Lines:** Wijst velden toe voor afzonderlijke regelitems in een ontvangstbewijs.\
   • **Order Line Charges:** Definieert de velden voor kosten die betrekking hebben op specifieke orderregels.\
   • **Cost Lines:** Geeft velden aan voor kostenverdelingsregels.\
   • **Debit Note & Credit Note:** Definieert velden voor het aanmaken van debet- en creditnota's in geval van afwijkingen.
3. **Conflictoplossingsregels**\
   Deze regels behandelen afwijkingen tussen factuurgegevens en de corresponderende inkoopordergegevens. Elke regel bestaat uit meerdere componenten:\
   • **Name:** De beschrijvende naam van de regel, die het type van de behandelde afwijking aangeeft.\
   • **Section:** Geeft aan op welk deel van de factuur (bijv. receipt\_lines, line\_charges) de regel wordt toegepast.\
   • **Active:** Booleaanse waarde (true of false) die aangeeft of de regel momenteel actief is.\
   • **Match Criteria:** Voorwaarden die de regel activeren, gebaseerd op vergelijkingen tussen de werkelijke factuurgegevens en de verwachte inkoopordergegevens.\
   • **Actions:** Definieert wat het systeem moet doen wanneer de regel wordt geactiveerd, inclusief het aanpassen van waarden, het toepassen van kosten of het genereren van credit-/debetnota's.

**Gemeenschappelijke elementen in de regels**

**Vergelijkingsoperatoren**\
Deze operatoren definiëren hoe de werkelijke factuurwaarden worden vergeleken met de verwachte inkooporderwaarden:\
• gelijk aan\
• groter dan\
• groter dan of gelijk aan\
• kleiner dan\
• kleiner dan of gelijk aan\
• binnen de tolerantie\
• buiten de tolerantie



**Goedkeuringsstatus**\
Geeft aan of een afwijking is goedgekeurd of niet:\
• goedgekeurd\
• afgewezen\
• willekeurig

**Actietypen**\
Definieert specifieke maatregelen die genomen moeten worden wanneer een afwijking wordt vastgesteld:\
• Ontvangstregel\
• Kostenregel\
• Kopkosten\
• Regelkosten\
• Belastingregel\
• Debetnota Ontvangstregel\
• Debetnota Kostenregel\
• Debetnota Kopkosten\
• Debetnota Regelkosten\
• Creditnota Ontvangstregel\
• Creditnota Kostenregel\
• Creditnota Kopkosten\
• Creditnota Regelkosten\
• Creditnota Belastingregel

**Regelvoorbeelden**\
**Geval 1, 2, 3:** Hoeveelheid en stuksprijs binnen de tolerantie\
• Doel: Behandelt scenario's waarin zowel de hoeveelheid als de stuksprijs op de factuur binnen de geaccepteerde tolerantiegrenzen liggen ten opzichte van de inkooporder.\
• Actie: Het systeem accepteert de factuurwaarden en berekent het totaalbedrag.

**Geval 4, 5:** Hoeveelheid binnen de tolerantie, stuksprijs buiten de tolerantie (goedgekeurd)\
• Doel: Geldt wanneer de hoeveelheid binnen de tolerantie ligt, maar de stuksprijs buiten de tolerantie ligt en is goedgekeurd.\
• Actie: Het systeem past de stuksprijs aan om overeen te komen met de inkooporder en past de vereiste regelkosten toe.

**Geval 6:** Hoeveelheid binnen de tolerantie, stuksprijs buiten de negatieve tolerantie (afgewezen)\
• Doel: Behandelt gevallen waarin de stuksprijs lager is dan verwacht en buiten het tolerantiebereik ligt, wat tot een afwijzing leidt.\
• Actie: Het systeem past de stuksprijs aan om overeen te komen met de inkooporder, genereert een creditnota voor het verschil en past indien nodig kopkosten toe.

**Behandeling van kosten en belastingen**\
**Kosten per eenheid tolerantie**\
• Regels in deze categorie behandelen afwijkingen bij kosten per eenheid, met specifieke maatregelen, gebaseerd op of de kosten binnen of buiten de tolerantie liggen en of ze zijn goedgekeurd of afgewezen.

**Aanpassingen van belastingregels**\
• Deze regels beheren belastingafwijkingen door de belastingregels aan te passen of door corresponderende credit- of debetnota's te genereren op basis van de verschillen tussen factuur- en inkoopordergegevens.

**Enums en opties**\
• **Enums:** Voorgedefinieerde waardelijsten die consistentie over de regels heen garanderen (bijv. vergelijkingsoperatoren, goedkeuringstypen).\
• **Opties:** Voorgedefinieerde keuzemogelijkheden voor het verwerken van hoeveelheden of stuksprijzen, die flexibiliteit bieden bij de regeldefinitie.

**Uitleg van de screenshots**\
**Screenshot 1:** Interface voor regelbeheer\
Deze screenshot toont de interface voor regelbeheer, waar beheerders alle conflictoplossingsregels kunnen bekijken en beheren. Belangrijke elementen zijn:\
• **Knop Regel toevoegen:** Maakt het toevoegen van nieuwe regels mogelijk.\
• **Regellijst:** Toont alle actieve regels met details zoals naam, sectie en actieve status.\
• **Sectie-dropdown:** Filtert de regels op basis van de sectie waarop ze betrekking hebben (bijv. ontvangstregels, regelkosten).

**Screenshot 2:** Gedetailleerde regelbewerking\
Deze screenshot toont de gedetailleerde weergave van een specifieke regel die wordt bewerkt. Belangrijke elementen zijn:\
• **Criteriagebied:** Definieert de voorwaarden waaronder de regel wordt geactiveerd. Het criterium zou bijvoorbeeld kunnen aangeven dat, wanneer de hoeveelheid en de stuksprijs afwijken van de inkooporder maar binnen de tolerantie liggen, de regel moet worden toegepast.\
• **Actiegebied:** Geeft aan welke maatregelen genomen moeten worden wanneer aan de criteria is voldaan. Dit kan het aanpassen van de factuurregels, het genereren van credit- of debetnota's of het toepassen van aanvullende kosten omvatten.\
• **Documenttype en kostencomponenten:** Stelt de beheerder in staat om specifieke maatregelen toe te wijzen aan documenttypen en kostencomponenten, wat flexibiliteit biedt bij het afhandelen van verschillende scenario's.
