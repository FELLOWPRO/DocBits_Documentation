---
description: Hoe u stamgegevens uit een XML-bestand in een lookup-dataset importeert
---

# Stamgegevens importeren uit XML

Naast de BOD-imports kan DocBits stamgegevens uit **elk willekeurig XML-bestand** inlezen in een lookup-dataset van uw keuze. U geeft aan in welke dataset moet worden geschreven en uit welk XPath elke kolom moet worden gelezen, dus de XML hoeft helemaal geen BOD-formaat te volgen.

Gebruik dit voor stamgegevens die niet als BOD binnenkomen — prijslijsten, kostenplaatsen, artikelkenmerken, alles wat uw ERP als XML kan exporteren.

## Twee manieren om de XML te versturen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Wanneer u het gebruikt |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | U hebt de gegevens als **XML-bestand** en wilt het uploaden. |
| `/master_data_lookup/xml/import_xml_data` | U wilt de **XML in het verzoek plakken**. Anders dan de BOD-endpoints accepteert dit endpoint de XML als platte tekst — zonder JSON-verpakking. |

Beide worden hieronder beschreven. Stap 1 en 2 zijn in beide gevallen hetzelfde.

## Voordat u begint

U hebt nodig:

* **Een API key.** Zie [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) als u er nog geen hebt.
* **De XML** — als bestand of als inhoud die u kunt plakken.
* **Een gegevenstype** — de naam van de lookup-dataset waarin moet worden geschreven.
* **Veldtoewijzingen** — welk XPath welke kolom vult.
* **Uw Org ID**, uit **Settings → Integration & SSO**, in de sectie **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Stapsgewijze instructies

### 1. De API-link openen

Open de testinterface van de API voor de omgeving en regio waarmee u werkt:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Verenigde Staten)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Verenigde Staten)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Deze endpoints staan onder **master data lookup** in plaats van onder **import**, verderop op de pagina.

{% hint style="info" %}
Gebruik de regio waarin uw organisatie wordt gehost — dezelfde regio waarmee u bij DocBits inlogt. De Europese en Amerikaanse omgevingen staan los van elkaar, dus een import die naar de verkeerde regio wordt gestuurd, verschijnt niet in uw organisatie.
{% endhint %}

### 2. Autoriseren

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

Autoriseren werkt precies zoals bij de BOD-imports: klik op het **slotpictogram**, plak uw **Org ID** in **X-ORG-ID**, plak uw API key in **X-API-KEY** en klik bij elk op **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. De velden invullen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Klik op **Try it out** en vul vervolgens het formulier in.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Veld | |
| --- | --- |
| **data\_type** | Verplicht. De lookup-dataset waarin moet worden geschreven. Die wordt automatisch omgezet naar kleine letters, dus `PriceList` en `pricelist` zijn dezelfde dataset. |
| **field\_mappings** | Verplicht. Een JSON-object dat elke kolom koppelt aan het XPath waaruit die wordt gelezen. Zie hieronder. |
| **file** | Verplicht bij `import_xml_file`. Klik op **Choose file** en selecteer uw XML. |
| **xml** | Verplicht bij `import_xml_data` in plaats van het bestand — plak de XML als platte tekst. |
| **org\_id** | Uw Org ID — dezelfde waarde die u in stap 2 in **X-ORG-ID** hebt gezet. |
| **sub\_org\_id** | Alleen nodig als u in een specifieke suborganisatie importeert. |

#### Veldtoewijzingen

`field_mappings` is een JSON-object met één item per kolom. Anders dan bij de BOD-imports, waar de namen vastliggen op `custom_field_1` … `custom_field_5`, kiest u ze hier zelf:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

De namen links worden de kolommen in de dataset en zijn aan u. De waarden rechts moeten overeenkomen met de structuur van de XML die u uploadt — in het voorbeeld hierboven pakt `//Item/ID` het `<ID>`-element binnen elk `<Item>`. De twee kanten staan los van elkaar: de toewijzing hierboven leest `<UnitPrice>` in een kolom die `Price` heet.

{% hint style="warning" %}
Alleen **onjuist opgebouwde** XPaths worden geweigerd, met een `400` die het veld noemt. Een XPath die geldig is maar niets aantreft in uw XML, gaat er stilzwijgend doorheen en laat die kolom simpelweg leeg — een typefout in een pad ziet er dus uit als een import die is gelukt maar een kolom is kwijtgeraakt. Als juist het `ID`-pad niets aantreft, mislukt de import wél en wordt gemeld dat de kolom `ID` ontbreekt voor dat record.
{% endhint %}

{% hint style="warning" %}
**Een van de kolommen moet `ID` heten.** Die identificeert een record: dezelfde gegevens opnieuw importeren werkt de rij met dat ID bij in plaats van een duplicaat toe te voegen. De naam is niet hoofdlettergevoelig, dus `ID`, `Id` en `id` werken allemaal, maar een naam als `ItemID` telt niet — het verzoek wordt geweigerd met `ID_FIELD_IS_MISSING` en er wordt niets geschreven.
{% endhint %}

{% hint style="warning" %}
**Eén verzoek importeert één record.** Elk XPath wordt één keer gelezen, dus als uw XML meerdere elementen bevat, wordt alleen de eerste overeenkomst van elk gebruikt. Stuur voor een lijst één verzoek per record, of gebruik in plaats daarvan een CSV-import.
{% endhint %}

#### Een gegevenstype kiezen

`data_type` is de sleutel van de dataset waarin u schrijft. Die wordt omgezet naar kleine letters en van spaties ontdaan, dus `Items` en `items` zijn dezelfde dataset. Elke naam die nog niet bezet is, maakt een eigen dataset aan — `items_example`, `cost_centres`, `price_list` — en er opnieuw in importeren werkt die bij.

{% hint style="danger" %}
Sommige namen zijn niet vrij: het zijn DocBits' eigen stamgegevenstabellen, en importeren in zo'n tabel schrijft er rechtstreeks in.

| Naam | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Geweigerd met `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Geaccepteerd, en ze overschrijven echte stamgegevens.** Gebruik deze alleen als dat werkelijk uw bedoeling is. |

Kies voor al het andere een eigen naam.
{% endhint %}

{% hint style="warning" %}
Controleer naar welke omgeving en welke organisatie u wijst voordat u uitvoert. Een import schrijft rechtstreeks in de stamgegevens van die organisatie.
{% endhint %}

### 4. Uitvoeren

Controleer voordat u uitvoert de keuzelijst **Servers** onderaan het formulier.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Klik op **Execute**. Een geslaagde import geeft terug:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

Anders dan de BOD-imports melden deze endpoints problemen met een echte foutstatus in plaats van een `200` met `"success": false` — een **400** betekent dat het verzoek is geweigerd en dat er niets is geschreven.

### 5. Controleren of de gegevens zijn aangekomen

* Ga in DocBits naar **Settings → Document Processing → Lookup Master Data**.
* Selecteer links **Imported** en open vervolgens het tabblad van uw gegevenstype.
* De kolommen zijn de namen die u aan de linkerkant van `field_mappings` hebt gebruikt.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
