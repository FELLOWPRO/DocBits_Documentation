---
hidden: true
---

# Een orderbevestiging vergelijken met een inkooporder

Gebruik **Compare with Purchase Order** in de Workflow Builder wanneer een orderbevestiging moet worden gecontroleerd aan de hand van de bijbehorende inkooporder. Voeg de kaart toe onder **And...** en kies vervolgens de ordergegevens, een operator en wat er met het resultaat moet gebeuren. De onderstaande schermafbeeldingen tonen twee beschikbare kaartversies in de Engelstalige interface. De velden zijn nog plaatshouders; stel ze voor uw eigen workflow in voordat u opslaat.

## Het resultaat naar een veld schrijven

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-write-text.png" alt="Compare with Purchase Order card in the Workflow Builder with Order Data, Operator, Text, Field Name, and Result of condition placeholders." width="563"><figcaption>Versie 2: tekst naar een veld schrijven op basis van het resultaat van de voorwaarde.</figcaption></figure>

Kies **Order Data** uit de orderbevestiging en een **Operator** voor de vergelijking met de inkooporder. Voer de te schrijven **Text** in, selecteer de **Field Name** en kies het **Result of condition** dat het schrijven moet activeren.

## De gegevens vergelijken

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-compare-as.png" alt="Compare with Purchase Order card in the Workflow Builder with Any/All, Order Data, Operator, and Comparison Data placeholders." width="563"><figcaption>Versie 4: geselecteerde gegevens van de orderbevestiging vergelijken met gegevens van de inkooporder.</figcaption></figure>

Kies **Any/All** om te bepalen of aan één of aan alle geselecteerde voorwaarden moet worden voldaan. Selecteer daarna de **Order Data**, **Operator** en **Comparison Data** voor de vergelijking met de inkooporder.

Zie voor de omliggende stappen [Workflow](../../README.md) en [Compare with Purchase Order](README.md).
