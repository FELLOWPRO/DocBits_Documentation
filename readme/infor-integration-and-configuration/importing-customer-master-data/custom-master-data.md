---
description: Stamgegevens rechtstreeks in DocBits importeren.
---

# Aangepaste stamgegevens

#### Aangepaste stamgegevens activeren <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Ga vanaf het dashboard naar Settings → Document Processing → Module.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_activate_slider.png" alt="Schuifregelaar voor aangepaste stamgegevens activeren in DocBits" width="375"><figcaption></figcaption></figure></div>

Activeer Custom Master Data in Module met de schuifregelaar zoals hieronder weergegeven.

<div align="left"></div>

#### Functieoverzicht <a href="#feature-overview" id="feature-overview"></a>

Ga naar Master Data Lookup in Settings om eigen stamgegevens aan DocBits toe te voegen.

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-nl.png" alt="Stamgegevens opzoeken: gegevensbronnen en leverancierstabel met afgeschermde waarden."><figcaption><p>Stamgegevens opzoeken: gegevensbronnen en leverancierstabel met afgeschermde waarden.</p></figcaption></figure></div>

Klik op “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

U kunt vervolgens een sjabloon of een eindpunt aanmaken.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Een sjabloon maken <a href="#create-a-template" id="create-a-template"></a>

Kies eerst of u het ION API-bestand van uw organisatie of OAuth2 gebruikt en voer de vereiste gegevens in.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Stel vervolgens de voorinstellingen in. Voer de naam van de stamgegevenstabel en de URL van de API-aanroep in.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Voer daarna het JSON-pad in met puntnotatie. Lees [hier](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/) meer over puntnotatie.

Koppel tot slot de gegevens aan de kolommen die u wilt aanmaken, zoals in het onderstaande voorbeeld.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Klik daarna op Done om de nieuwe stamgegevens aan te maken en te vullen.

#### Een eindpunt maken <a href="#create-an-endpoint" id="create-an-endpoint"></a>

Kies eerst of u het ION API-bestand van uw organisatie, OAuth2 of geen van beide gebruikt en voer de vereiste gegevens in.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Stel vervolgens de voorinstellingen in. Voer de naam van de stamgegevenstabel en de URL van de API-aanroep in.

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_presets_config.png" alt="Voorinstellingen voor aangepaste stamgegevens in DocBits" width="375"><figcaption></figcaption></figure></div>

Voer daarna het JSON-pad in met puntnotatie. Lees [hier](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/) meer over puntnotatie.

Koppel tot slot de gegevens aan de kolommen die u wilt aanmaken, zoals in het onderstaande voorbeeld.

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_map_columns.png" alt="Kolommen koppelen voor aangepaste stamgegevens in DocBits" width="375"><figcaption></figcaption></figure></div>

Klik daarna op Done om de nieuwe stamgegevens aan te maken en te vullen.
