# Factuurautomatiseringstest met DocBits

## Overzicht

Dit document schetst het testplan voor factuurautomatisering met behulp van DocBits met Infor LN of M3. Het bevat details van testgevallen, testvoorbereiding, uitvoeringsstappen en ondersteuningsprocessen.

## Testgevallen

| ID | Testgeval                                                                          | Beschrijving                                                                                                                                                                                          | Status    |
| -- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1  | Kostenfacturen                                                                     | Facturen zonder inkooporder worden succesvol verwerkt in DocBits en geëxporteerd naar LN als “kostenfactuur”.                                                                                         | TE TESTEN |
| 2  | Inkoopordergerelateerde factuur met perfecte overeenkomst                          | Inkoopordergerelateerde facturen worden succesvol verwerkt in DocBits met een perfecte overeenkomst van factuur naar inkooporder, aangezien artikelnummer, hoeveelheid en eenheidsprijs overeenkomen. | TE TESTEN |
| 3  | Inkoopordergerelateerde facturen met verschillende hoeveelheden                    | Inkoopordergerelateerde facturen worden verwerkt in DocBits, maar in de inkooporderovereenkomstmodule hebben we een mismatch op de hoeveelheid.                                                       | TE TESTEN |
| 4  | Inkoopordergerelateerde facturen met verschillende eenheidsprijzen                 | Inkoopordergerelateerde facturen worden verwerkt in DocBits, maar in de inkooporderovereenkomstmodule hebben we een mismatch op de eenheidsprijs.                                                     | TE TESTEN |
| 5  | Inkoopordergerelateerde facturen met verschillende of niet-bestaande artikelnummer | Inkoopordergerelateerde facturen worden verwerkt in DocBits, maar in de inkooporderovereenkomstmodule hebben we een mismatch of een niet-bestaand artikelnummer.                                      | TE TESTEN |
| 6  | Inkoopordergerelateerde facturen met een mismatch binnen toleranties               | Inkoopordergerelateerde facturen worden verwerkt in DocBits, maar in de inkooporderovereenkomstmodule hebben we een mismatch op hoeveelheid of eenheidsprijs, maar het is binnen de toleranties.      | TE TESTEN |
| 7  | Creditnota's                                                                       | Creditnota's worden succesvol verwerkt in DocBits en geëxporteerd naar LN. Verduidelijk of bedragen met een positief of negatief teken moeten worden geëxporteerd.                                    | TE TESTEN |

## Plan voor Testen met Klant

### 1. Opzetten

* **Initiële Vergadering**: Plan een kick-off vergadering met de klant om het testproces en de doelstellingen uit te leggen.
* **Toegang en Machtigingen**: Zorg ervoor dat de klant alle benodigde toegang heeft tot DocBits en Infor LN of M3 voor testdoeleinden.

### 2. Testvoorbereiding

* **Training**: Bied uitgebreide training aan het team van de klant over hoe DocBits te gebruiken voor factuurverwerking.
* **Documentatie**: Deel gedetailleerde documentatie over de testprocedures, inclusief verwachte resultaten voor elk testgeval.

### 3. Uitvoering van Testgevallen

* **Testomgeving**: Zet een testomgeving op die het productiesysteem van de klant zo nauwkeurig mogelijk nabootst.
* **Stap-voor-Stap Testen**: Werk samen met de klant om elk testgeval uit te voeren, en zorg ervoor dat ze elke stap begrijpen:
  * Verwerk facturen via DocBits.
  * Controleer de output in de inkooporderovereenkomstmodule.
  * Controleer de exportresultaten in LN of M3.

### 4. Probleemoplossing

* **Tracking**: Gebruik een tracking systeem (zoals Jira of een eenvoudige spreadsheet) om eventuele problemen of mismatches die tijdens het testen optreden te registreren.
* **Ondersteuning**: Bied onmiddellijke ondersteuning om problemen op te lossen en eventuele twijfels te verduidelijken.

### 5. Verificatie en Feedback

* **Verificatie**: Verifieer na elk testgeval de resultaten met de klant om de nauwkeurigheid te waarborgen.
* **Feedbackloop**: Verzamel feedback van de klant over het proces en eventuele verbeteringen die nodig zijn.

### 6. Finalisatie

* **Documentatie van Resultaten**: Documenteer de resultaten van elk testgeval en geef een samenvattend rapport aan de klant.
* **Reviewvergadering**: Voer een reviewvergadering uit om de testresultaten en eventuele verdere stappen te bespreken die nodig zijn voordat we live gaan.

### 7. Voorbereiding op Livegang

* **Training Verfrissing**: Bied een opfristraining aan indien nodig.
* **Ondersteuningsplan**: Ontwikkel een ondersteuningsplan voor de initiële livegangfase om een soepele overgang te waarborgen.
