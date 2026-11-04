---
description: "Download een synthetische factuur, workflow-JSON, invoer, verwachtingen en echte testantwoorden."
---

# Workflow-oefenpakket

Gebruik dit pakket bij het [Advanced-praktijkvoorbeeld](advanced-workflow-case-study.md). Het bevat een synthetische factuur, importeerbare workflow, zeven volledige documentinvoeren, onafhankelijke verwachtingen en werkelijk opgeslagen testantwoorden. Technische sleutels en routenamen zijn in alle talen identiek.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Workflow-oefenpakket met voorbeelden en resultaten
{% endfile %}

## Inhoud en formaten

| Bestand | Gebruik |
| --- | --- |
| `training-invoice.pdf` | Synthetische factuur: EUR 1500 netto, EUR 285 belasting, EUR 1785 totaal. Niet betalen. |
| `advanced-workflow.json` | Uitgeschakeld importeren via **Import Workflow**; geen globale variabele, beperkt tot Factuur en het exacte oefennummer. |
| `*-input.json` | Volledige documentgegevens voor **Advanced Test → Custom Data**. |
| `expectations.json` | Verwachte routes, statusmeldingen en totaalresultaten; functionele specificatie, geen Test Manager-uploadbestand. |
| `*-result.json` | Echte Dev-antwoorden met knoopresultaten en meldingen; private organisatiereferenties zijn vervangen. |
| `prepare_inputs.py` | Vervangt de synthetische organisatie op beide vereiste plaatsen. |
| `verify_results.py` | Controleert antwoorden tegen onafhankelijke verwachtingen. Vereist Python 3, geen toegangssleutel. |

## Gebruiken

1. Pak de ZIP uit en lees de meegeleverde instructies.
2. Importeer de workflow in uw testorganisatie en bevestig dat hij uitgeschakeld is.
3. Zoek de ID van uw eigen testorganisatie en voer lokaal uit:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Gebruik bestanden uit `prepared/` in het Advanced-testvenster. Vervang een synthetische document-ID niet door een lopende klantfactuur.
5. Controleer alle zeven gevallen met de [resultatentabel](advanced-workflow-case-study.md). Bedragvariaties zijn bewust gekozen en wijzigen de bijgevoegde factuur niet.

De gegevens bevatten `id`, `org_id`, `doc_type`, `status` en `extracted_data` met `layout.groups`, `fields` en `tables`. De organisatiereferenties bovenaan en in `extracted_data` moeten bij het aangemelde account passen. Een waarde zonder bijbehorende layoutdefinitie wordt mogelijk niet als bestaand documentveld gelezen.

## Reikwijdte

De verwachtingen controleren routes, routetekst, statusmeldingen en afsluitknopen, naast de documentstatus. Dit is niet dezelfde controle als de statusvergelijking van een opgeslagen Test Manager-scenario.

Een geslaagde Advanced-test bevestigt verwerking van de aangeleverde gegevens. Gesimuleerde acties zijn geen echte toewijzing, e-mail of levering. Activering vereist een passende gebeurtenisingang en een afzonderlijk gecontroleerde echte uitvoering. Zie [Wanneer wordt mijn workflow uitgevoerd?](workflow-execution-model.md).

## WF-03: Oefening en acceptatie

Pak v2 uit, pas de organisatie met prepare_inputs.py aan en voer verify_results.py uit. decision-table-setup.json helpt bij configuratie en acceptance-record-template.json is een verslagmodel; geen van beide importeert workflows. Bevestig vóór import de inactieve toestand.

[Leerpad](workflow-learning-path.md)
