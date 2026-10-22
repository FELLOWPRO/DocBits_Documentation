---
description: "Diagnoseer workflowproblemen met gebeurtenissen, invoergegevens, gekozen routes en werkelijke resultaten."
---

# Workflowproblemen systematisch onderzoeken

Begin met één betrokken uitvoering. Noteer organisatie en omgeving, workflownaam en opgeslagen revisie, documentreferentie, tijdstip en tijdzone en de exacte knoopmelding. Gebruik in testantwoorden ook `execution_id`. Deel geen toegangssleutels of onbeschermde klantgegevens in bewijsmateriaal.

## Van symptoom naar controle

| Symptoom | Bewijs zoeken | Corrigeren en opnieuw testen |
| --- | --- | --- |
| Geen uitvoering | Licentie, module, activering, tijdfilters en gebeurtenis | Corrigeer ingang en filters; herhaal de echte gebeurtenis. Handmatige Start bewijst die niet. |
| Actie blijft grijs | Resultaat van voorganger en verbonden uitgang | Volg de werkelijk gekozen route. Een overgeslagen knoop is niet zelf mislukt. |
| Oranje voorwaarde | Gelezen veldsleutel, type, waarde en operator | Onderscheid negatief resultaat en evaluatiefout. Test onder, op en boven de grens. |
| Rode knoop | Eerste foutmelding en benodigde invoer | Corrigeer gegevens of configuratie; herhaal fout- en succesgeval. |
| Wait ALL gaat niet verder | Elke bron en het verbonden resultaat | Vereis geen elkaar uitsluitende routes samen. Toon een mogelijke route voor elke vereiste bron. |
| Dubbele taken of exports | Herhaalde runs, gebeurtenissen, statussen en Run Workflow | Beperk voorwaarden en overgangen; test tweemaal hetzelfde geval. Controleer passende bescherming tegen gelijktijdige verwerking in het ontvangende proces. |
| Variabele beïnvloedt andere workflows | Gedeelde organisatievariabele | Controleer afhankelijkheden. Wijzigingen worden onafhankelijk van het canvas bewaard; test betrokken workflows opnieuw. |
| Test geslaagd, effect ontbreekt | Wat is vergeleken of gesimuleerd? | Controleer toewijzing op het document, taak in het taakgebied en ontvangst op de bestemming. Alleen status is onvoldoende. |
| Export gestart, niets ontvangen | Exportgeschiedenis, antwoord en gegevens ontvanger | Onderzoek vóór herhalen; controleer of de eerste aanvraag al verwerkt is. |

## Meldingen begrijpen

In het [Advanced-voorbeeld](advanced-workflow-case-study.md) gaat een ontbrekend bedrag via rood naar gegevenscorrectie. De afhandeling en OR kunnen slagen terwijl het totaal de oorspronkelijke fout houdt. Een normaal onware bedragvoorwaarde gaat via oranje en kan succesvol de standaardroute afronden.

Twee verbindingen van één bron zijn geen twee onafhankelijke goedkeuringen. Samenvoegingen beoordelen verbonden resultaten van hun bronnen. Controleer de volledige route: een deeltest vanaf een middelste knoop kan vereiste voorgangers overslaan.

## De correctie aantonen

1. Bewaar de oorspronkelijke bevinding en functionele verwachting.
2. Wijzig gegevens of configuratie gericht. Pas verwachtingen alleen aan als de eis verandert.
3. Herhaal foutgeval, positief geval en betrokken grenzen met het [oefenpakket](workflow-training-kit.md).
4. Sla de regel op en controleer de activering afzonderlijk.
5. Vergelijk een nieuwe echte uitvoering met de oude. Oude logs blijven hun oorspronkelijke revisie beschrijven.

Leg oorzaak, correctie, aangetoond resultaat en resterende beperkingen vast. Scheid wachttijd en uitvoeringstijd: een lange totale duur identificeert niet vanzelf een trage knoop.

## WF-04: Oefening en acceptatie

Begin met invalid-number. Bewaar de eerste amount-fout en resultaat error. Herhaal met above en vergelijk nieuw bewijs. Behoud het oude foutverslag; geslaagde foutafhandeling is onvoldoende.

[Leerpad](workflow-learning-path.md)

## Kaarttests herhalen met een expliciete scope

In de onderzochte Dev-ontwerper schakelde het herhalen van een test vanaf een gekozen knoop naar de hele graaf. Open de contextmenutest van de bedoelde kaart opnieuw en controleer welke knopen werkelijk zijn bezocht. Een resultaat met zes knopen bewijst geen losse leegtecontrole. De teller voor mislukte acties kan ook een niet vervulde voorwaarde omvatten: lees tevens uitgang, logmelding en totaalresultaat.
