---
description: "P0: Run Workflow, doelvoorwaarden en fouten begrijpen"
---

# P0: Run Workflow, doelvoorwaarden en fouten begrijpen

**Run Workflow** roept een workflow via zijn ID aan en wacht op de uitvoering. Een naam volstaat niet. De ontwerper beheert het verborgen ID van de aanroepende workflow; wijzig dat niet als bedrijfsparameter. Het huidige document gaat naar het doel, waar start en voorwaarden opnieuw worden beoordeeld.

De onderzochte expliciete aanroep bereikt ook een **inactief** doel. Inactief betekent dus niet onbereikbaar via Run Workflow. Dev-tests omvatten een eigen inactief oefendoel, zelfaanroep en een onbekend doel-ID. De laatste twee namen Error. Ingebouwde recursie- en ketenlimieten vervangen geen bedrijfsregels tegen herhaalde aanroepen.

Onderscheid organisatievariabelen en documentvelden van resultaten die bij één uitvoering horen. De aanroep geeft niet automatisch alle beslissingstabel- of HTTP-resultaten van de bovenliggende uitvoering door. Spreek de benodigde documentvelden af en controleer hun werkelijke waarden in de volgende kaart.

Een groene aanroep bevestigt niet alle bedrijfsvoorwaarden van het doel: een Advanced-resultaat zonder technische fout geldt als een geslaagde aanroep en kan `failed_condition` omvatten. Bekijk gekozen pad en effect van het doel. Behandel fouten expliciet in de aanroeper; vermijd A→B→A en herhaalde aanroepen van hetzelfde doel.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `run_workflow` · v2

Identiteit: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | aanroep kan slagen; controleer doel |

## Bewijs en grenzen

Geselecteerde kaart- en knoopresultaten zijn met synthetische gegevens in Advanced Test gecontroleerd. Antwoorden staan in het oefenpakket. Documentacties zijn gesimuleerd en bewijzen geen opgeslagen documentuitvoering of externe aflevering.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
