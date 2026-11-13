# Dashboard

Het **Workflow-dashboard** is het startpunt van het workflowgedeelte. Het laat zien hoe uw workflows presteren (uitvoeringstotalen, slaag- en faalpercentages, een grafiek van uitvoeringen in de tijd en recente activiteit) en geeft toegang tot de workflowlijst, de testmanager en de Card SDK.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard met uitvoeringstotalen, slaag- en faalpercentages, de uitvoeringsgrafiek en recente activiteit"><figcaption><p>Het Workflow Dashboard: uitvoeringstotalen, slaag-/faalpercentages en recente activiteit voor elke workflow.</p></figcaption></figure>

## Tabbladen

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.mp4" %}

**Video:** Zoeken en filteren op het Workflow-dashboard · 0:53 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Zoeken op naam** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.mp4#t=0.25)

In de Workflowlijst vindt het zoekveld Workflows op naam. Typ een deel van een naam, en alleen de passende Workflows blijven in de lijst.

**Zoekopdracht wissen** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.mp4#t=10.616)

Wis de zoekopdracht om weer alle Workflows te zien. De zoekopdracht staat ook in het paginaadres, dus terug in de lijst blijft hij behouden.

**Datums en Workflow** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.mp4#t=20.983)

Op het tabblad Dashboard bepalen de filters bovenaan wat de cijfers en de grafiek tellen: een start- en een einddatum, standaard de laatste maand, en alle Workflows of één enkele.

**Twee periodes vergelijken** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/nl.mp4#t=33.983)

Vergelijken voegt een tweede periode toe: vul de start- en einddatum in. Elk cijfer toont dan ook de waarde van die periode en het verschil. Deze browser onthoudt de filters voor uw volgende bezoek.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4" %}

**Video:** Een Workflow als JSON downloaden en uploaden · 0:55 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Downloaden als JSON** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4#t=0.25)

Om een kopie van een Workflow te bewaren, opent u de acties in de lijst en kiest u Download. U krijgt één JSON-bestand met de naam, het type en alle kaarten en verbindingen.

**Back-up of verplaatsen** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4#t=13.183)

Gebruik het als back-up, of om een Workflow te verplaatsen die u in een testomgeving hebt gebouwd en getest.

**Workflow importeren** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4#t=21.15)

Om hem terug te halen, klikt u op Workflow importeren en kiest u de JSON-bestanden, tot tien tegelijk.

**Komt uitgeschakeld binnen** · [0:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4#t=30.483)

Een geüploade Workflow komt uitgeschakeld binnen, zodat er niets draait voordat u hem hebt bekeken.

**Gebruikers, groepen en tabellen controleren** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/nl.mp4#t=38.616)

Kaarten die gebruikers, groepen, suborganisaties of beslistabellen noemen, verwijzen ernaar met een interne id. Open na een upload uit een andere omgeving de kaarten en controleer of ze nog zo zijn ingesteld als u wilt. Test hem daarna en schakel hem in.

</details>

- **Dashboard** — uitvoeringsstatistieken en recente activiteit (hierboven weergegeven).
- **Workflowlijst** — elke workflow met zijn type, uitvoeringsvolgorde en trigger. Maak een nieuwe aan met **Nieuwe workflow**.
- **Test Manager-lijst** — testscenario's die uw workflows valideren; voer ze uit met **Alle tests uitvoeren**.
- **Licentie** — informatie over workflowlicenties.
- **Card SDK** — bouw en upload aangepaste workflowkaarten (zie [Card SDK](card-sdk.md)).

De werkbalk biedt ook **Sjablonen**, waarmee de bibliotheek [Workflow Templates](standard-workflow-builder.md#workflow-templates) wordt geopend, en **Workflow importeren**, waarmee u een workflow uit een JSON-bestand importeert.

Met de **Testbeheer** kunt u per workflow testscenario's opslaan en gezamenlijk uitvoeren, zodat u kunt bevestigen dat uw workflows na wijzigingen nog steeds correct werken:

<figure><img src="../../.gitbook/assets/prior-u032-nl.png" alt="Lijst met workflowtestscenario&#x27;s."><figcaption><p>Lijst met workflowtestscenario&#x27;s.</p></figcaption></figure>

## Volgende stappen

- Bouw een lineaire automatisering met de **Standaardworkflow**-builder.
- Bouw een vertakkende flow met de **Geavanceerde workflow**-builder.
