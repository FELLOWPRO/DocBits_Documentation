# Testbeheer

Met de **Testbeheer** kunt u herbruikbare **testscenario's** voor uw workflows opslaan en samen uitvoeren — zodat u kunt bevestigen dat een workflow nog steeds correct werkt nadat u deze hebt gewijzigd. Het werkt voor zowel Standaard- als Geavanceerde workflows.

Open hem via **Workflowdashboard → Testlijst**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List met testscenario's, status en Run All Tests"><figcaption><p>De Test Manager List — elk opgeslagen scenario toont een geslaagd/mislukt-resultaat.</p></figcaption></figure>

## Wat een testscenario is

Een testscenario legt een workflow, een voorbeeldinvoer en de **verwachte uitkomst** vast. Wanneer u het uitvoert, speelt de Test Manager de workflow opnieuw af tegen die invoer en vergelijkt het resultaat met wat u verwachtte — waardoor de rij **groen** (geslaagd) of **rood** (mislukt) wordt.

## Werken met scenario's

- **Testscenario toevoegen** — maak een nieuw scenario op basis van een workflow en een voorbeelddocument.
- **Alle tests uitvoeren** — voer alle scenario's tegelijk uit en zie in één oogopslag welke workflows nog steeds slagen.
- **Bekijk details** — open een scenario om het resultaat te inspecteren.

<figure><img src="../../.gitbook/assets/prior-u027-nl.png" alt="Details van een testscenario; gegevens zijn afgeschermd."><figcaption><p>Details van een testscenario; gegevens zijn afgeschermd.</p></figcaption></figure>

De detailweergave toont de scenarionaam en **status**, de **workflownaam**, de **uitvoeringstijd** en de **werkelijke** en **geëxtraheerde gegevens** die de uitvoering opleverde — zodat u precies kunt zien waarom een scenario is geslaagd of mislukt.

## Test Manager versus testen in de builder

Dit zijn twee verschillende dingen:

- **Testbeheer** (deze pagina) — *opgeslagen, herhaalbare* scenario's met verwachte uitkomsten, samen uitgevoerd met **Alle tests uitvoeren**. Gebruik dit voor regressietests na wijzigingen.
- **Testen in de builder** — de inline **Valideren**- en **Test**-knoppen in de Advanced Workflow-builder, voor snelle controles terwijl u aan het bouwen bent. Zie [Validatie & Testen](advanced-workflow/validation-and-testing.md).
