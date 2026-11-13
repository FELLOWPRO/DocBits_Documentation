---
description: "P1: Toewijzing, taken en opeenvolgende goedkeuring onderscheiden"
---

# P1: Toewijzing, taken en opeenvolgende goedkeuring onderscheiden

Een **documenttoewijzing** bepaalt de huidige verantwoordelijkheid. Een **taak** is een afzonderlijke werkopdracht. Een **melding** informeert. Geen daarvan is al persoonlijke goedkeuring. Een groep toewijzen bewijst evenmin instemming van alle groepsleden.

Opeenvolgende kaarten verzamelen ontvangers en goedkeuringsvolgorde. Het voorbeeld gebruikt A met volgorde 10 en B met 20. De onderzochte afronding begint met de kleinste waarde. De overdracht aan B volgt uit de verwerkte gebruikersbeslissing in het goedkeuringsproces; een Wait-knoop in de ontwerper doet deze overdracht niet zelf.

Vermijd directe toewijzing in dezelfde uitvoering wanneer u de eerste opeenvolgende ontvanger verwacht: de afronding kan die eerste toewijzing overslaan nadat het document direct is toegewezen. Configureer bij taken `task_type`, prioriteit, ontvanger en `send_email` afzonderlijk. Houd e-mail tijdens oefeningen uitgeschakeld.

Zakelijke acceptatie vereist A→goedkeuren→B→goedkeuren, afwijzing door A, ontbrekende ontvanger en herhaalde activering. Afwijzing moet de afsluitende export verhinderen; een onopgeloste ontvanger mag niet als voltooide goedkeuring verschijnen. Controleer documentverantwoordelijkheid en taken afzonderlijk. De simulatie bewijst geen werkelijke overdracht tussen gebruikers.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4" %}

**Video:** Goedkeuring in twee stappen met beslissingstabellen · 3:00 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Twee stappen, twee beslissingstabellen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=0.25)

Een goedkeuring in twee stappen: eerst de goedkeurders die een beslissingstabel teruggeeft, daarna een eindgroep die altijd als laatste komt. Twee beslissingstabellen: de ene geeft gebruikers terug, de andere een groep.

**Eén keten: tabel, toewijzing, tabel, toewijzing** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=14.683)

Zet elke toewijzingskaart direct achter haar eigen beslissingstabel, in één keten: tabel, toewijzing, tabel, toewijzing. Beide tabellen bewaren wat ze teruggeven.

**Elke toewijzing direct na haar tabel** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=27.95)

Een Workflow bewaart alleen het laatste resultaat van een beslissingstabel. Elke toewijzingskaart leest het als ze draait, dus moet ze draaien voordat de volgende tabel het vervangt.

**Prioriteiten bepalen de volgorde** · [0:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=40.15)

De volgorde van de goedkeuringen komt uit de prioriteiten, niet uit de volgorde van de kaarten: het laagste getal krijgt het document eerst. Geef de eindgroep het hoogste getal.

**Test: goedkeurders, dan de groep** · [0:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=53.95)

De test toont elke kaart als geslaagd. De eerste toewijzingskaart zet de twee goedkeurders in de wachtrij, de tweede de eindgroep. Aan het einde van de run geeft één laatste toewijzing het document aan de eerste van hen.

**Naast elkaar: werkt niet** · [1:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=82.016)

Deze opzet werkt niet. Twee paden naast elkaar zien er hetzelfde uit, maar de Workflow voert ze stap voor stap uit: eerst beide tabellen, dan beide toewijzingskaarten.

**Goedkeurders kwijt - zonder fout** · [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=94.05)

De test voert eerst beide tabellen uit, dan beide toewijzingskaarten. Beide lezen het resultaat van de tweede tabel: de groep komt twee keer in de wachtrij en de goedkeurders gaan verloren. Elke kaart toont toch succes, niets waarschuwt u. Gebruik de keten.

**Een vaste laatste goedkeurder: prioriteit 99** · [2:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=124.183)

In een Standard Workflow kan een vaste goedkeurder altijd als laatste komen: wijs de gebruikers van de tabel toe en voeg dan een kaart toe die één gebruiker met een hoge prioriteit toewijst, bijvoorbeeld 99.

**Prioriteiten van de tabel lager houden** · [2:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=137.983)

De prioriteiten van de tabel moeten onder dat getal blijven. Vindt de tabel niemand, dan stopt de Workflow bij de tabelkaart en wordt niemand toegewezen. Een gebruiker die beide teruggeven, wordt twee keer gevraagd.

**Controleren in een test** · [2:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/nl.mp4#t=151.883)

Een Standard Workflow test één kaart tegelijk, dus test dezelfde kaarten in een Advanced Workflow. De eerste toewijzingskaart zet de goedkeurders van de tabel in de wachtrij, de tweede voegt de vaste gebruiker toe. Hun prioriteiten zetten hem achteraan.

</details>

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
