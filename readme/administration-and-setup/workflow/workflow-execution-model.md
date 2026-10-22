---
description: "Maak onderscheid tussen gebeurtenissen, voorwaarden, uitvoeringsvolgorde, tests en activering."
---

# Wanneer wordt mijn workflow uitgevoerd?

Een workflow heeft een aanleiding en passende voorwaarden nodig. **Documenttype is Factuur** selecteert documenten; dit betekent niet dat elke wijziging van een factuur automatisch een nieuwe uitvoering start.

## Van gebeurtenis naar actie

1. Controleer de organisatie, rechten en Workflow-module, plus de Advanced-toegang waar nodig.
2. Bepaal de aanleiding: documentverwerking, een expliciete handmatige aanroep of een ondersteunde gebeurtenistrigger. Gebruik alleen triggers die de kaartcatalogus van uw versie daadwerkelijk aanbiedt.
3. In Standard Workflow moeten When en alle And-voorwaarden overeenkomen. Een onware voorwaarde stopt die lineaire kaartvolgorde.
4. In Advanced Workflow bepalen de ingang en verbonden resultaatuitgangen de route. Een onware And-voorwaarde kan via oranje doorgaan; rood behandelt een evaluatiefout.
5. Controleer het resultaat op de juiste plek: testantwoord, opgeslagen uitvoering, document of ontvangend systeem.

**Start** is een handmatige ingang. Het oefenpakket gebruikt When voor Factuur en het exacte oefenfactuurnummer om aan de huidige interfacevereisten te voldoen. Importeer het uitgeschakeld en test handmatig. Een geslaagde handmatige test bewijst geen automatische uitvoering door een documentgebeurtenis.

## Opslaan, testen en activeren

| Toestand | Betekenis |
| --- | --- |
| Lokaal concept | Een browserkopie vervangt opslaan op de server niet. |
| Opgeslagen | De configuratie bestaat. Controleer activering afzonderlijk: opslaan kan een nieuwe regel al activeren. |
| Advanced-test | Beoordeelt de huidige graaf, inclusief niet-opgeslagen wijzigingen. Documentacties worden gesimuleerd. |
| Geactiveerd | De regel kan bij de passende gebeurtenis worden meegenomen. Test die gebeurtenis afzonderlijk. |

Test Manager en het Advanced-testvenster zijn verschillende uitvoeringsmogelijkheden. Alleen een statusvergelijking bevestigt geen toewijzing, melding of exportontvangst. Controleer de gevolgen van de gekozen testmogelijkheid voordat u echte documenten gebruikt.

## Meerdere workflows en herhaling

Lagere waarden van de **uitvoeringsvolgorde** komen eerst. Workflow 100 kan bijvoorbeeld een veld voorbereiden dat workflow 200 controleert. Gebruik verschillende waarden en bevestig de werkelijk gelezen gegevens in een nieuwe uitvoering. De positie van een Advanced-kaart op het canvas bepaalt de volgorde niet.

**Change Status to → Trigger Workflows** kan een nieuwe uitvoering starten. **Run Workflow** roept een geselecteerde workflow aan. Beide vereisen bewuste voorwaarden; geen van beide garandeert eenmalige uitvoering. Beperk taken en exports via de zakelijke verwerkingsstatus en test expliciet een tweede uitvoering. Een voltooiingsmarkering alleen beschermt niet algemeen tegen gelijktijdige dubbele verwerking.

Ga verder met het [Advanced-praktijkvoorbeeld](advanced-workflow-case-study.md), het [oefenpakket](workflow-training-kit.md) en de [diagnosehandleiding](workflow-troubleshooting.md).

## WF-01: Oefening en acceptatie

Noteer gebeurtenis, filter, activatie en kaartversie. Controleer twee uitvoeringen en volgorde 100/200 met een werkelijk gelezen vervolgveld. Onderscheid verwachte aanvraag en waargenomen uitvoering.

[Leerpad](workflow-learning-path.md)
