---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Workflow Dashboard

Het Workflow Dashboard is uw centrale hub voor het beheren en monitoren van alle workflows in DocBits. Open het door op het **Workflows**-pictogram in de linkerzijbalk te klikken.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard met uitvoeringstotalen, slaag- en faalpercentages, de uitvoeringsgrafiek en recente activiteit"><figcaption><p>Het Workflow Dashboard — uitvoeringstotalen, slaag-/faalpercentages en recente activiteit voor elke workflow.</p></figcaption></figure>

## Dashboard Tabblad

Het Dashboard-tabblad biedt een overzicht in een oogopslag van workflowprestaties voor een geselecteerde tijdsperiode.

### Filters

- **Startdatum / Einddatum** — Selecteer het tijdsbereik voor statistieken
- **Workflow Naam** — Filter op een specifieke workflow of bekijk alles
- **Vergelijken** — Vergelijk twee tijdsperiodes naast elkaar
- **Wissen** — Reset alle filters

### Statistiekkaarten

| Metriek | Beschrijving |
|---|---|
| **Vandaag uitgevoerde workflows** | Totaal aantal workflowuitvoeringen vandaag |
| **Aangemaakte workflows (periode)** | Nieuwe workflows aangemaakt binnen het geselecteerde datumbereik |
| **Totaal aantal uitvoeringen** | Cumulatieve workflowuitvoeringen over de periode |
| **Succesvolle uitvoeringen** | Aantal uitvoeringen die zonder fouten zijn voltooid |
| **Slagingspercentage** | Percentage succesvolle uitvoeringen vs. totaal aantal uitvoeringen |
| **Faalpercentage** | Percentage mislukte uitvoeringen vs. totaal aantal uitvoeringen |

{% hint style="warning" %}
Een hoog faalpercentage (weergegeven als **CRITICAL** in rood) geeft aan dat workflows fouten tegenkomen. Onderzoek de falende workflows met behulp van de uitvoeringslogboeken in de [Geavanceerde Workflow Builder](advanced-workflow-builder/).
{% endhint %}

### Grafiek Workflowuitvoeringen

De grafiek toont een maandelijkse uitsplitsing van **succesvolle** (groen) en **mislukte** (rood/roze) workflowuitvoeringen, waarmee u trends en pieken in fouten kunt identificeren.

### Recente Activiteit

- **Laatste Workflowtests** — Toont recente testuitvoeringen met slaag-/faalstatus
- **Laatste Workflows** — Toont recent aangemaakte of gewijzigde workflows

## Tabblad Workflowlijst

Het tabblad Workflowlijst toont alle workflows met zoek-, sorteer- en beheermogelijkheden.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Kolommen

| Kolom | Beschrijving |
|---|---|
| **Status** | Schakelpictogram — klik om een workflow in/uit te schakelen |
| **Naam** | Workflownaam (klik om te openen in de Workflow Builder) |
| **Type** | Badge met `Advanced` voor visuele workflows |
| **Wanneer...** | Samenvatting van de triggervoorwaarde |
| **Bijgewerkt door** | Gebruiker die de workflow het laatst heeft gewijzigd |
| **Aangemaakt op** | Aanmaakdatum en -tijd |
| **Bijgewerkt** | Laatste wijzigingsdatum en -tijd |
| **Acties** | Contextmenu (verwijderen, dupliceren, exporteren) |

### Acties

- **Zoeken** — Filter workflows op naam met de zoekbalk
- **+ WORKFLOW TOEVOEGEN** — Maak een nieuwe workflow aan (opent de [Geavanceerde Workflow Builder](advanced-workflow-builder/))
- **SJABLONEN** — Blader door en laad opgeslagen workflowsjablonen
- **WORKFLOW IMPORTEREN** — Importeer een workflow vanuit een JSON-bestand

## Tabblad Testmanagerlijst

Het tabblad Testmanagerlijst toont alle testconfiguraties en resultaten van workflows. Gebruik dit om geautomatiseerde testscenario's voor uw workflows op te zetten.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Workflow Testmanagerlijst met testscenario's en Alle Tests Uitvoeren"><figcaption><p>De Testmanagerlijst — elk scenario toont een slaag-/faalresultaat; gebruik <strong>Run All Tests</strong> om ze allemaal opnieuw uit te voeren.</p></figcaption></figure>

## Tabblad Licentie

Het tabblad Licentie toont uw huidige DocFlow-licentiestatus en beschikbare functies.

## Tabblad Card SDK

Het tabblad Card SDK stelt u in staat om aangepaste workflowkaarten (partnerkaarten) te bouwen en beheren die de ingebouwde mogelijkheden van DocFlow uitbreiden.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### ZIP Uploaden

Upload een partner-app als een ZIP-bestand dat het volgende bevat:
- `app.json` — Kaartmetadata en configuratie
- `.docflowcompose/flow/` — Kaartdefinitiebestanden

Maximale bestandsgrootte: **10 MB**. Klik op **Upload & Validate** om de kaart ter beoordeling in te dienen.

### GitHub Import

Importeer partnerkaarten rechtstreeks vanuit een GitHub-repository in plaats van een ZIP-bestand te uploaden.

### Inzendingen

Bekijk en beheer alle ingediende partnerkaarten:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Kolom | Beschrijving |
|---|---|
| **Kaartnaam** | Naam van de partner-app en kaart |
| **card_type_label** | Kaarttype (`Action_card` of `Condition_card`) |
| **Versie** | Kaartversienummer |
| **Ingediend** | Inzenddatum |
| **Status** | Huidige beoordelingsstatus |
| **Acties** | Beschikbare acties op basis van status |

#### Kaartstatussen

| Status | Betekenis | Beschikbare acties |
|---|---|---|
| **Validated** | Kaart heeft validatie doorstaan | Downloaden, Goedkeuren, Afwijzen |
| **Approved** | Kaart is actief en beschikbaar in workflows | Downloaden, Uitschakelen, Intrekken |
| **Rejected** | Kaart is niet door de beoordeling gekomen | Verwijderen |
| **Disabled** | Kaart is gedeactiveerd | Verwijderen |

### SDK-sjabloon Downloaden

Klik op **Download SDK Template** om een startersjabloon te krijgen voor het bouwen van uw eigen aangepaste kaarten. Het sjabloon bevat de vereiste bestandsstructuur en voorbeeldconfiguraties.

{% hint style="info" %}
Partnerkaarten kunnen ook programmatisch worden beheerd via de [DocFlow MCP-tools](../../../advanced-functions-and-tools/docflow-mcp/). Gebruik de Card SDK MCP-tools om kaarten te maken, valideren, goedkeuren en testen vanuit uw IDE of automatiseringsscripts.
{% endhint %}
