---
description: "P1: Toewijzing, taken en opeenvolgende goedkeuring onderscheiden"
---

# P1: Toewijzing, taken en opeenvolgende goedkeuring onderscheiden

Een **documenttoewijzing** bepaalt de huidige verantwoordelijkheid. Een **taak** is een afzonderlijke werkopdracht. Een **melding** informeert. Geen daarvan is al persoonlijke goedkeuring. Een groep toewijzen bewijst evenmin instemming van alle groepsleden.

Opeenvolgende kaarten verzamelen ontvangers en goedkeuringsvolgorde. Het voorbeeld gebruikt A met volgorde 10 en B met 20. De onderzochte afronding begint met de kleinste waarde. De overdracht aan B volgt uit de verwerkte gebruikersbeslissing in het goedkeuringsproces; een Wait-knoop in de ontwerper doet deze overdracht niet zelf.

Vermijd directe toewijzing in dezelfde uitvoering wanneer u de eerste opeenvolgende ontvanger verwacht: de afronding kan die eerste toewijzing overslaan nadat het document direct is toegewezen. Configureer bij taken `task_type`, prioriteit, ontvanger en `send_email` afzonderlijk. Houd e-mail tijdens oefeningen uitgeschakeld.

Zakelijke acceptatie vereist A→goedkeuren→B→goedkeuren, afwijzing door A, ontbrekende ontvanger en herhaalde activering. Afwijzing moet de afsluitende export verhinderen; een onopgeloste ontvanger mag niet als voltooide goedkeuring verschijnen. Controleer documentverantwoordelijkheid en taken afzonderlijk. De simulatie bewijst geen werkelijke overdracht tussen gebruikers.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `action_assign_doc_to_user_sequential` · v2

Identiteit: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identiteit: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Goedkeuren → B → Goedkeuren |
| ASSIGN-02 | A → Afwijzen | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Terugvalroute |
| ASSIGN-04 | RUN-1 → RUN-2 | controleer duplicaten |
| ASSIGN-05 | direct + sequential | controleer eerste ontvanger |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
