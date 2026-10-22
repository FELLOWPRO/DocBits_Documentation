---
description: "P0: Status wijzigen en herhaalde uitvoering begrenzen"
---

# P0: Status wijzigen en herhaalde uitvoering begrenzen

**Change Status to** wijzigt de documentstatus. In versie 3 bepaalt `trigger_docflow` of verdere workflowverwerking wordt aangevraagd. Stel dit expliciet in. Ontbreekt het, dan gebruikt de code `true`; versies 1/2 lezen deze schakelaar niet via hetzelfde uitvoeringspad. Controleer de opgeslagen kaartversie.

Begin met `validated_pending_approval` en `trigger_docflow=false`. De status is een technische keuze: een verzonnen `pending_approval` is geen vervanging. Advanced Test simuleert de wijziging. Dit bewijst geen opgeslagen statuswijziging of verwerking van een aangevraagde vervolguitvoering.

Een begrensd bedrijfsproces controleert beginstatus en verwerkingskenmerk, voert de actie uit en gaat naar de volgende toestand. Een herhaald evenement mag niet meer aan de beginvoorwaarde voldoen. Twee gelijktijdige uitvoeringen kunnen echter allebei het oude kenmerk lezen: taken en exportbestemmingen hebben aanvullende controle op duplicaten nodig.

Vergelijk voor acceptatie eerste en tweede echte uitvoering: status, aangevraagde vervolgverwerking en aantal taken of doelregistraties. Wissel niet alleen bij wijze van proef tussen twee statussen. Een statuswijziging verleent geen goedkeuring waarvan de bedrijfsvoorwaarde nog niet is vervuld.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `staus_change` · v3

Identiteit: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | vervolguitvoering aangevraagd ≠ voltooid |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Bewijs en grenzen

Geselecteerde kaart- en knoopresultaten zijn met synthetische gegevens in Advanced Test gecontroleerd. Antwoorden staan in het oefenpakket. Documentacties zijn gesimuleerd en bewijzen geen opgeslagen documentuitvoering of externe aflevering.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
