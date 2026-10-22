---
description: "Leerpad van beginner tot expert"
---

# Leerpad van beginner tot expert

Werk de niveaus op volgorde af. Alleen lezen volstaat niet: elk niveau eindigt met een eigen configuratie, toetsbare verwachting en bewijs. P0 voorkomt fundamentele uitvoeringsfouten; P1 verdiept gegevens, zakelijke besluiten en integraties.

1. [Oriëntatie en uitvoeringsmodel](#level-1)
2. [Uw eerste eigen regel](#level-2)
3. [Velden, types en grenzen](#level-3)
4. [Bedrijfsregels en goedkeuringen](#level-4)
5. [Advanced-besturing en onderliggende workflows](#level-5)
6. [Berekening, integratie en export](#level-6)
7. [Wijzigingen en deskundig beheer](#level-7)

## Vereisten

Gebruik een eigen testorganisatie en synthetisch document. Controleer organisatie, rol, workflowlicentie en Advanced-recht. Houd geïmporteerde oefeningen inactief. Volledige JSON-bestanden zijn voor Advanced Test → Custom Data. Echte goedkeuringen en integraties vereisen afzonderlijke testgebruikers en bestemmingen.

## 1. Oriëntatie en uitvoeringsmodel <a id="level-1"></a>

**Oefening:** Leg organisatie, toegang, When–And–Then en het verschil tussen lineaire regel en Advanced-graaf uit. Onderscheid documentfilter, gebeurtenis, opslaan en activeren.

**Afrondingscriterium:** U kunt uitleggen wanneer de regel wordt meegenomen en welk bewijs simulatie van documentuitvoering onderscheidt.

Lezen en bouwen: [Wanneer wordt mijn workflow uitgevoerd?](workflow-execution-model.md) · [P0: Status wijzigen en herhaalde uitvoering begrenzen](masterclass/status-and-reentry.md).

## 2. Uw eerste eigen regel <a id="level-2"></a>

**Oefening:** Bouw When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Houd deze inactief. Test volledige gegevens voor 999, 1000 en 1000.01. Deze lineaire regel heeft nog geen controleknoop nodig.

**Afrondingscriterium:** REVIEW wordt alleen boven 1000 bereikt. Noteer type, operator en gekozen uitgang. Behandel ontbrekende invoer apart.

Lezen en bouwen: [Advanced-praktijkvoorbeeld: factuurrouting](advanced-workflow-case-study.md) · [Workflow-oefenpakket](workflow-training-kit.md).

## 3. Velden, types en grenzen <a id="level-3"></a>

**Oefening:** Controleer ontbrekend, null, lege tekst, spaties, false, 0 en getallen als tekst. Bereken tolerantie met bestel- en documentreferentie. Vergelijk één tegenover alle werkelijk gekoppelde regels.

**Afrondingscriterium:** Verklaar waar, onwaar en fout vanuit waarde, type, referentie en gegevens. Geen vergelijkbare regel is geen geslaagde goedkeuring.

Lezen en bouwen: [P1: Field is, Docfield is of Compare two Fields kiezen](masterclass/field-conditions.md) · [P1: Referentie voor toleranties en PO-vergelijkingen vastleggen](masterclass/tolerances-and-po.md).

## 4. Bedrijfsregels en goedkeuringen <a id="level-4"></a>

**Oefening:** Configureer twee niet-overlappende bedragregels. Volg het opgeslagen gebruikersresultaat tot de toewijzing. Plan A met volgorde 10 en B met 20, afwijzing en terugvalroute.

**Afrondingscriterium:** Onderscheid verantwoordelijkheid, taak, melding en echte goedkeuring. Accepteer overdracht aan B pas na een verwerkte beslissing van A.

Lezen en bouwen: [P1: Een beslissingstabel tot de toewijzing volgen](masterclass/decision-table-routing.md) · [P1: Toewijzing, taken en opeenvolgende goedkeuring onderscheiden](masterclass/assignment-task-sequential.md).

## 5. Advanced-besturing en onderliggende workflows <a id="level-5"></a>

**Oefening:** Vergelijk ALL, ANY en OR met twee bereikte controles. Bekijk een niet-gekozen tak. Voer de zeven v2-gevallen uit en test Run Workflow met een eigen inactief doel.

**Afrondingscriterium:** Verklaar test/planner-verschillen, brontelling en fouten. V2 bereikt voltooiing zonder vastgelopen OR; controleer een groene aanroep bij het doel.

Lezen en bouwen: [P0: Wait ALL, Wait ANY en OR correct verbinden](masterclass/control-nodes.md) · [P0: Run Workflow, doelvoorwaarden en fouten begrijpen](masterclass/run-workflow.md) · [Advanced-praktijkvoorbeeld: factuurrouting](advanced-workflow-case-study.md).

## 6. Berekening, integratie en export <a id="level-6"></a>

**Oefening:** Vergelijk de hele tabel voor/na, inclusief niet-passende regex en delen door nul. Definieer de echte terugschrijfafspraak van de integratie. Plan export na goedkeuring met eigen testconfiguratie.

**Afrondingscriterium:** Bewijs vervolgwaarden, ontvangst en ERP-verwerking apart. Registreer simulatie of exportaanvraag niet als aflevering.

Lezen en bouwen: [P1: Tabelkolommen berekenen en regex-afhankelijkheid controleren](masterclass/table-calculations.md) · [P1: API-aanroepen en gebruik van antwoorden verifiëren](masterclass/api-response-contract.md) · [P1: Exportvarianten, open taken en eindstatus kiezen](masterclass/export-lifecycle.md).

## 7. Wijzigingen en deskundig beheer <a id="level-7"></a>

**Oefening:** Bewaar een workflow-export en kaartversies vóór wijziging. Herhaal positieve, negatieve, fout- en grensgevallen plus tweede uitvoering. Koppel de eerste fout aan concrete invoer en configuratie.

**Afrondingscriterium:** U kunt wijzigingen accepteren, de configuratie herstellen en een nieuw document met effecten vergelijken. Leg oorzaak, correctie en grenzen vast.

Lezen en bouwen: [Workflowproblemen systematisch onderzoeken](workflow-troubleshooting.md) · [Workflowkaarten begrijpen en configureren](card-reference-standard.md).

## Toets uw kennis

| Vraag | Antwoord |
| --- | --- |
| Is false leeg bij Field is v2? | Ja; getal 0 en tekst "false" zijn niet leeg. |
| Garandeert een groene OR-test de documentuitvoering? | Nee. Niet-bereikte voorgangers worden anders behandeld in test en de onderzochte planner. |
| Kan Run Workflow een inactief doel aanroepen? | Ja, via de onderzochte expliciete aanroep. Controleer wel doelvoorwaarden en resultaat. |
| Maakt HTTP 200 automatisch api.response.cost_center beschikbaar? | Nee. De onderzochte acties bieden dat automatische JSON-uitvoercontract niet. |
| Bewijst een groene test exportontvangst? | Nee. Documentuitvoering, ontvangst en ERP-verwerking vereisen eigen bewijs. |

## De vijf begeleidende handleidingen

Gebruik tijdens de oefeningen: uitvoeringsmodel → reproduceerbaar voorbeeld → oefenpakket → diagnose → kaartreferentie. Dit zijn hulpmiddelen bij de niveaus, geen vijf extra ongecontroleerde opdrachten.

1. [Wanneer wordt mijn workflow uitgevoerd?](workflow-execution-model.md)
2. [Advanced-praktijkvoorbeeld: factuurrouting](advanced-workflow-case-study.md)
3. [Workflow-oefenpakket](workflow-training-kit.md)
4. [Workflowproblemen systematisch onderzoeken](workflow-troubleshooting.md)
5. [Workflowkaarten begrijpen en configureren](card-reference-standard.md)

## Afrondingsverslag

Gebruik acceptance-record-template.json uit het pakket. Noteer scenario, revisie, verwachting, waarneming en bewijssoort. Onderscheid Dev-test, geïsoleerde broncodecontrole, echte documentuitvoering, ontvangst en ERP-verwerking. Laat niet-geteste stappen expliciet open.
