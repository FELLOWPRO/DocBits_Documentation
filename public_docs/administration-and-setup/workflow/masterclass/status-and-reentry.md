---
description: >-
  Gebruik de kaart Wijzig status naar zo dat een statuswijziging dezelfde
  Workflow niet opnieuw start.
---

# Status wijzigen zonder uw Workflow opnieuw te starten

Wanneer een document een nieuwe status krijgt, start DocBits de Workflows die voor die status bedoeld zijn. Daar kan ook de Workflow bij zitten die de status net heeft gewijzigd. Als de voorwaarden daarvan nog kloppen, wordt die Workflow opnieuw uitgevoerd en maakt hij een tweede taak of export aan.

Op deze pagina ziet u hoe u uw Workflow zo instelt dat elk document er maar één keer doorheen gaat.

## De instelling waar het om gaat

De kaart [Wijzig status naar](../then/status/change-status-to.md) zet de nieuwe status. Met de instelling **Trigger-workflows** bepaalt u of deze statuswijziging Workflows mag starten:

* **Onwaar:** er wordt geen Workflow gestart. Kies deze waarde, tenzij een andere Workflow met het document verder moet gaan.
* **WAAR:** DocBits start de Workflows waarvan de voorwaarden kloppen voor het document met zijn nieuwe status. Daar kan ook de Workflow bij zitten die de wijziging heeft gemaakt.

Op de kaartpagina vindt u alle statussen en de kaartversies.

## Welke Workflows starten na een statuswijziging

Als **Trigger-workflows** op **WAAR** staat, bekijkt DocBits elke ingeschakelde Workflow en controleert de voorwaarden voor documenttype en status, bijvoorbeeld een kaart **Documentstatus**. Een Workflow start als het document met zijn nieuwe status aan de voorwaarden voldoet.

Een Workflow die de status niet controleert, klopt voor **elke** status. Wijzigt zo'n Workflow zelf de status, dan start de nieuwe status hem opnieuw.

Zet u een document op de status die het al heeft, dan gebeurt er niets: de status blijft gelijk en er start geen Workflow.

## Voorbeeld: één keer of twee keer uitgevoerd

De regel: zodra uw Workflow zijn werk heeft gedaan, mogen zijn eigen voorwaarden niet meer kloppen.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-nl.png" alt="Twee Workflows, allebei met Trigger-workflows op WAAR. Links: de voorwaarde controleert Type is Factuur en status is Klaar voor validatie. Na de wijziging naar In afwachting van goedkeuring klopt de voorwaarde niet meer, de Workflow wordt niet opnieuw gestart, resultaat 1 taak. Rechts: de voorwaarde controleert alleen Type is Factuur. De nieuwe status start de Workflow een tweede keer, hij maakt een tweede taak en zet opnieuw In afwachting van goedkeuring, wat niets verandert. Resultaat 2 taken." width="800"><figcaption><p>Dezelfde Workflow met en zonder statusvoorwaarde</p></figcaption></figure>

Rechts wordt de Workflow een tweede keer uitgevoerd en maakt hij een dubbele taak. Hij stopt daar alleen omdat de tweede statuswijziging een status zet die het document al heeft.

**Twee Workflows kunnen elkaar starten.** Als de ene Workflow **In afwachting van goedkeuring** zet en een andere het document terugzet op **Klaar voor validatie**, allebei met **WAAR**, dan blijven ze elkaar starten. Geef elke Workflow een voorwaarde op de status waarmee hij begint, en gebruik **WAAR** alleen waar het nodig is.

## Stap voor stap instellen

1. **Gebruik versie 3 van Wijzig status naar.** Oudere versies hebben geen instelling **Trigger-workflows** (zie [Kaartversies](../then/status/change-status-to.md#kaartversies)).
2. **Controleer de beginstatus.** Voeg de **En**-kaart **Documentstatus** toe (onder **En → Status**) en zet die op **Is** **Klaar voor validatie**. Zie [Status van één document Conditie](../and/status/single-document-status-condition.md). Als de status alleen niet laat zien of de stap klaar is, controleer dan ook een veld dat uw Workflow invult wanneer hij klaar is.
3. **Voeg de actie toe**, bijvoorbeeld een taak maken of het document exporteren.
4. **Voeg Wijzig status naar toe** en kies de volgende status, bijvoorbeeld **In afwachting van goedkeuring**.
5. **Kies een waarde voor Trigger-workflows.** Begin met **Onwaar**. Kies alleen **WAAR** als een andere Workflow met de nieuwe status verder moet gaan.
6. **Probeer het met een echt document.** Controleer dat er precies één taak of export is aangemaakt en dat het document de nieuwe status heeft.

{% hint style="info" %}
Tests in de Workflow-ontwerper simuleren de statuswijziging alleen. De status wordt niet opgeslagen en er start geen andere Workflow. Gebruik een echt document om het werkelijke gedrag te zien.
{% endhint %}

## Ingebouwde bescherming

DocBits beperkt de schade als Workflows elkaar steeds opnieuw starten:

* **Eén Workflow-uitvoering tegelijk per document.** Uitvoeringen voor hetzelfde document wachten op elkaar, en elke uitvoering ziet het document zoals de vorige het heeft achtergelaten.
* **Maximaal aantal uitvoeringen.** Standaard wordt dezelfde Workflow hoogstens 50 keer op één document uitgevoerd. Daarna start DocBits hem voor dit document niet meer.

Deze grenzen stoppen de herhaling uiteindelijk, maar tegen die tijd kunnen er al veel taken of exports zijn. Wat het echt voorkomt, is een voorwaarde op de status. Als een dubbele taak of export een echt probleem zou zijn, controleer dan ook vooraf of die er al is, bijvoorbeeld of er al een open taak voor het document bestaat.

## Zie ook

* [Wijzig status naar](../then/status/change-status-to.md): de kaart, de statussen en de versies
* [Status van één document Conditie](../and/status/single-document-status-condition.md): de documentstatus in een voorwaarde controleren
* [Wanneer wordt mijn workflow uitgevoerd?](../workflow-execution-model.md)
* [Overzicht van het leerpad](../workflow-learning-path.md)
