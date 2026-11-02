# Workflow Pattern Guides

**Versie:** 1.0 **Laatst Bijgewerkt:** 23 oktober 2025

***

## Overzicht

Deze map bevat uitgebreide gidsen voor workflowpatronen die demonstreren hoe meerdere workflowkaarten kunnen worden gecombineerd om veelvoorkomende bedrijfsscenario's op te lossen. Elk patroon biedt stapsgewijze implementatie-instructies, complete voorbeelden en beste praktijken.

**Wat zijn Workflowpatronen?**

Workflowpatronen zijn bewezen, herbruikbare oplossingen voor veelvoorkomende uitdagingen bij documentverwerking. In plaats van helemaal opnieuw te beginnen, kunt u deze patronen als sjablonen gebruiken en aanpassen aan uw specifieke behoeften.

***

## De Workflow Builder in een oogopslag

Elk patroon op deze pagina wordt samengesteld in de **Workflow Builder**. U bereikt deze via **Workflow Dashboard → Workflowlijst → Workflow Toevoegen** (of door een bestaande workflow te openen). Het dashboard toont u de uitvoeringsgeschiedenis en slaag-/faalpercentages voor al uw workflows:

Het tabblad **Workflowlijst** toont elke workflow met het bijbehorende type, de uitvoeringsvolgorde en de trigger. Gebruik **Workflow Toevoegen** om een nieuwe aan te maken, of klik op een workflow om deze in de builder te openen:

Een workflow wordt opgebouwd uit drie groepen kaarten — **When** (de trigger), **And** (aanvullende voorwaarden) en **Then** (de acties die worden uitgevoerd). Het onderstaande voorbeeld wordt geactiveerd op facturen die bij een suborganisatie horen en wijst deze toe aan een gebruiker:

Klik in een willekeurige groep op **Add Card** om de kaartbibliotheek te openen. Kaarten zijn geordend per categorie (Compare with Purchase Order, Partner Cards, Document Field, Date & Time, Document, Logic, Status, Table, Assignee, …) zodat u het bouwblok kunt vinden dat elk patroon nodig heeft:

***

## Beschikbare Patronen

### 1. [API Integratie Patroon](api-integration-pattern.md)

**Complexiteit:** Gemiddeld | **Insteltijd:** 45-60 minuten

Leer hoe u DocBits integreert met externe API's om gegevens uit externe systemen op te halen, te valideren en op te slaan.

**Gebruiksscenario's:**

* Real-time prijzen ophalen uit externe systemen
* Leveranciersinformatie valideren tegen masterdatabases
* Productdetails opzoeken uit catalogussystemen
* Wisselkoersen ophalen van valutadiensten
* Adressen verifiëren met geocodingdiensten

**Gebruikte Kaarten:** CALL\_API, CONDITION\_HTTPS\_REQUEST\_STATUS, ACTION\_SET\_FIELD\_TO\_TEXT, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Bekijk Volledig Patroon →**](api-integration-pattern.md)

***

### 2. [Taakbeheer Patroon](task-management-pattern.md)

**Complexiteit:** Laag-Gemiddeld | **Insteltijd:** 30-45 minuten

Beheers de kunst van het creëren, toewijzen, volgen en beheren van taken binnen DocBits workflows voor goedkeurings- en beoordelingsprocessen.

**Gebruiksscenario's:**

* Goedkeuringsworkflows creëren
* Beoordelingstaken toewijzen aan gebruikers
* Uitzonderingen afhandelen die menselijke tussenkomst vereisen
* Problemen escaleren naar managers
* Goedkeuringsketens op meerdere niveaus creëren
* Taakvoltooiing en deadlines volgen

**Gebruikte Kaarten:** tasks\_create, ACTION\_ASSIGN\_TO\_USER, ACTION\_SEND\_EMAIL\_TO\_GROUPS, CONDITION\_TASK\_STATUS

[**Bekijk Volledig Patroon →**](task-management-pattern.md)

***

### 3. [PO Matching Patroon](po-matching-pattern.md)

**Complexiteit:** Gemiddeld-Hoog | **Insteltijd:** 60-90 minuten

Implementeer uitgebreide workflows voor het matchen van inkooporders om facturen te valideren tegen inkooporders met op tolerantie gebaseerde routering.

**Gebruiksscenario's:**

* Facturen valideren tegen inkooporders
* Prijsfouten detecteren vóór betaling
* Hoeveelheidsverschillen identificeren
* Inkoopcontroles afdwingen
* Dubbele betalingen voorkomen
* Driewegmatching automatiseren

**Gebruikte Kaarten:** PURCHASE\_ORDER\_FULL\_MATCH, CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE, CONDITION\_DOC\_TO\_PO\_QUANTITY, CONDITION\_DOC\_TO\_PO\_TAX\_LINES

[**Bekijk Volledig Patroon →**](po-matching-pattern.md)

***

### 4. [Beslissingslogica Patroon](decision-logic-pattern.md)

**Complexiteit:** Gemiddeld | **Insteltijd:** 30-45 minuten

Implementeer complexe beslissingsbomen en voorwaardelijke routeringslogica om documenten via verschillende paden te verwerken op basis van bedrijfsregels.

**Gebruiksscenario's:**

* Documenten routeren op basis van bedragdrempels
* Verschillende regels toepassen voor verschillende documenttypen
* Goedkeuringslogica op meerdere niveaus implementeren
* Complexe bedrijfsbeleidsregels afhandelen
* Dynamische routering creëren op basis van meerdere criteria
* Goedkeuringsmatrices implementeren

**Gebruikte Kaarten:** CONDITION\_DOC\_FIELD\_AMOUNT, CONDITION\_DOC\_TYPE\_IS\_ISNOT, CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT, ACTION\_ASSIGN\_TO\_USER

[**Bekijk Volledig Patroon →**](decision-logic-pattern.md)

***

### 5. [Gegevenstransformatie Patroon](data-transformation-pattern.md)

**Complexiteit:** Gemiddeld | **Insteltijd:** 30-45 minuten

Transformeer, bereken, formatteer en verrijk documentgegevens om voor te bereiden op export, berekeningen uit te voeren en formaten te standaardiseren.

**Gebruiksscenario's:**

* Totalen, subtotalen, belastingen berekenen
* Valuta's of eenheden converteren
* Datums, getallen, tekst formatteren
* Waarden afleiden uit bestaande velden
* Gegevens verrijken uit externe bronnen
* Gegevensformaten standaardiseren
* Berekeningen valideren

**Gebruikte Kaarten:** ACTION\_CALCULATE\_FIELD, ACTION\_SET\_FIELD\_TO\_TEXT, ACTION\_COPY\_FIELD\_VALUE, CALL\_API, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Bekijk Volledig Patroon →**](data-transformation-pattern.md)

***

## Gids voor Patroonselectie

### Op Complexiteit

| Complexiteit       | Patronen                                                                                                                                                                                          | Beste Voor                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Laag-Gemiddeld** | [Taakbeheer](task-management-pattern.md)                                                                                                                                                          | Beginners, eenvoudige workflows             |
| **Gemiddeld**      | <p><a href="api-integration-pattern.md">API Integratie</a><br><a href="decision-logic-pattern.md">Beslissingslogica</a><br><a href="data-transformation-pattern.md">Gegevenstransformatie</a></p> | Gemiddelde gebruikers, standaard workflows  |
| **Gemiddeld-Hoog** | [PO Matching](po-matching-pattern.md)                                                                                                                                                             | Geavanceerde gebruikers, complexe validatie |

***

### Op Gebruiksscenario

| Ik Moet...                          | Gebruik Dit Patroon                                             |
| ----------------------------------- | --------------------------------------------------------------- |
| Integreren met externe systemen     | [API Integratie Patroon](api-integration-pattern.md)            |
| Goedkeuringsworkflows creëren       | [Taakbeheer Patroon](task-management-pattern.md)                |
| Valideren tegen inkooporders        | [PO Matching Patroon](po-matching-pattern.md)                   |
| Routeren op basis van voorwaarden   | [Beslissingslogica Patroon](decision-logic-pattern.md)          |
| Gegevens berekenen en transformeren | [Gegevenstransformatie Patroon](data-transformation-pattern.md) |

***

### Op Industrie/Afdeling

| Industrie/Afdeling        | Aanbevolen Patronen                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Financiën/Boekhouding** | [PO Matching](po-matching-pattern.md), [Taakbeheer](task-management-pattern.md), [Gegevenstransformatie](data-transformation-pattern.md) |
| **Inkoop**                | [PO Matching](po-matching-pattern.md), [Beslissingslogica](decision-logic-pattern.md), [API Integratie](api-integration-pattern.md)      |
| **Operaties**             | [Taakbeheer](task-management-pattern.md), [Beslissingslogica](decision-logic-pattern.md)                                                 |
| **IT/Integratie**         | [API Integratie](api-integration-pattern.md), [Gegevenstransformatie](data-transformation-pattern.md)                                    |
| **Alle Afdelingen**       | [Beslissingslogica](decision-logic-pattern.md), [Taakbeheer](task-management-pattern.md)                                                 |

***

## Hoe Deze Patronen Te Gebruiken

### Stap 1: Kies een Patroon

1. Bekijk de patroonbeschrijvingen hierboven
2. Identificeer welk patroon overeenkomt met uw gebruiksscenario
3. Controleer de complexiteit en geschatte insteltijd
4. Bekijk de sectie "Wanneer te Gebruiken" in de patroongids

### Stap 2: Bekijk Vereisten

Elke patroongids vermeldt:

* Vereiste kennis
* Gerelateerde gidsen om eerst te lezen
* Kaarten die zullen worden gebruikt
* Configuratievereisten

### Stap 3: Volg Stap-voor-Stap Instructies

Elk patroon biedt:

* Compleet workflowvoorbeeld
* Stapsgewijze implementatiegids
* Configuratiesjablonen
* Praktijkvoorbeelden
* Tips voor probleemoplossing

### Stap 4: Pas Aan Naar Uw Behoeften

* Pas het voorbeeld aan uw bedrijfsregels aan
* Pas drempels en toleranties aan
* Wijzig routeringslogica
* Voeg stappen toe/verwijder ze indien nodig
* Test grondig vóór gebruik in productie

### Stap 5: Monitor en Optimaliseer

* Volg workflowprestaties
* Monitor succespercentages
* Verzamel gebruikersfeedback
* Verfijn configuratie
* Documenteer aanpassingen

***

## Patrooncombinaties

Veel praktijkscenario's vereisen het combineren van meerdere patronen:

### Voorbeeld 1: Volledige Factuurverwerking

```
1. API Integratie Patroon → Haal huidige prijzen op
2. Gegevenstransformatie Patroon → Bereken totalen
3. PO Matching Patroon → Valideer tegen PO
4. Beslissingslogica Patroon → Routeer op basis van variantie
5. Taakbeheer Patroon → Maak goedkeuringstaken
```

### Voorbeeld 2: Factuurgoedkeuring Hoge Waarde

```
1. Gegevenstransformatie Patroon → Bereken bedragen
2. Beslissingslogica Patroon → Controleer drempels
3. Taakbeheer Patroon → Goedkeuring op meerdere niveaus
4. API Integratie Patroon → Meld externe systemen
```

### Voorbeeld 3: Afhandeling van Uitzonderingen

```
1. PO Matching Patroon → Detecteer varianties
2. Beslissingslogica Patroon → Classificeer ernst van uitzondering
3. Taakbeheer Patroon → Maak beoordelingstaken
4. Gegevenstransformatie Patroon → Bereken impact
```

***

## Patroonsjablonen

Elk patroon bevat deze gestandaardiseerde secties:

1. **Overzicht** - Wat het patroon doet
2. **Wanneer te Gebruiken** - Geschikte gebruiksscenario's
3. **Compleet Voorbeeld** - Praktijkscenario
4. **Stap-voor-Stap** - Implementatie-instructies
5. **Configuratie** - Kaartconfiguratiesjablonen
6. **Workflow Diagram** - Visuele weergave
7. **Geavanceerde Variaties** - Alternatieve implementaties
8. **Foutafhandeling** - Veelvoorkomende problemen en oplossingen
9. **Testchecklist** - Validatiestappen
10. **Gerelateerde Patronen** - Aanvullende patronen
11. **Gerelateerde Gidsen** - Referentiedocumentatie

***

## Hulp Krijgen

### Ondersteuningsbronnen voor Patronen

**Documentatie:**

* [Complete Index Workflowgidsen](../../)
* [Individuele Kaartgidsen](../then/action/)
* [Referentie Conditiekaarten](../condition-cards-complete-guide.md)
* [Workflow Koppelingskaart](../../../../../WORKFLOW_LINKING_MAP.md)

**Aanvullende Bronnen:**

* [Snelle Referentiegids](../../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
* [Release Notes Oktober 2025](../../changelog/2025-10-october.md)
* [Kaartversie Referentie](../../../../docs/card_version.md)

**Contact:**

* Patroonfeedback: docs@docbits.com
* Technische Ondersteuning: support@docbits.com
* Implementatiehulp: consulting@docbits.com

***

## Patroonstatistieken

| Metriek                           | Waarde                |
| --------------------------------- | --------------------- |
| **Totaal Aantal Patronen**        | 5                     |
| **Totaal Aantal Gedekte Kaarten** | 30+                   |
| **Gecombineerde Documentatie**    | \~1.200 regels        |
| **Voorbeeldscenario's**           | 25+                   |
| **Configuratiesjablonen**         | 15+                   |
| **Workflow Diagrammen**           | 5 complete diagrammen |
| **Kruisverwijzingen**             | 87+ interne links     |

***

## Bijdragen aan Patronen

Hebt u een workflowpatroon waar anderen baat bij zouden hebben?

**Richtlijnen voor Bijdragen aan Patronen:**

1. **Documenteer Uw Workflow**
   * Duidelijk bedrijfsscenario
   * Stapsgewijze implementatie
   * Werkende configuratievoorbeelden
   * Praktijktestresultaten
2. **Volg Patroonsjabloon**
   * Gebruik standaard sectiestructuur
   * Voeg alle vereiste elementen toe
   * Geef diagrammen/voorbeelden
   * Voeg gids voor probleemoplossing toe
3. **Indienen voor Beoordeling**
   * E-mail naar: docs@docbits.com
   * Inclusief: Patroonbeschrijving, gebruiksscenario's, implementatiegids
   * We zullen het beoordelen en mogelijk toevoegen aan de officiële documentatie

**Voordelen:**

* Help andere DocBits-gebruikers
* Krijg erkenning in documentatie
* Verbeter algemene productkennisbank
* Ontvang feedback op uw implementatie

***

## Changelog

### Versie 1.0 (23 oktober 2025)

* Initiële release van 5 uitgebreide workflowpatronen
* API Integratie Patroon toegevoegd
* Taakbeheer Patroon toegevoegd
* PO Matching Patroon toegevoegd
* Beslissingslogica Patroon toegevoegd
* Gegevenstransformatie Patroon toegevoegd
* Kruisverwijzingskoppeling geïmplementeerd (87 links)
* Gids voor patroonselectie gemaakt

***

## Volgende Stappen

**Nieuw met Workflowpatronen?**

1. Begin met [Taakbeheer Patroon](task-management-pattern.md) - het makkelijkst te begrijpen
2. Bekijk [Beslissingslogica Patroon](decision-logic-pattern.md) - fundamenteel voor alle workflows
3. Verken [API Integratie Patroon](api-integration-pattern.md) - veelvoorkomende integratiebehoefte

**Klaar om te Implementeren?**

1. Kies uw patroon uit de bovenstaande lijst
2. Lees de volledige patroongids
3. Bekijk vereisten en gerelateerde gidsen
4. Volg stap-voor-stap instructies
5. Test met voorbeelddocumenten
6. Implementeer in productie
7. Monitor en optimaliseer

**Meer Hulp Nodig?**

* Bekijk [Overzicht Workflowdocumentatie](../../)
* Bekijk [Snelle Referentiegids](../../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
* Neem contact op met ondersteuningsteam

***

**Laatst Bijgewerkt:** 23 oktober 2025 **Onderhouden Door:** Documentatieteam **Versie:** 1.0
