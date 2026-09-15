---
description: Hoe u een Receive Delivery BOD handmatig in DocBits importeert via de API
---

# Goederenontvangsten importeren (Receive Delivery BOD)

Goederenontvangsten bereiken DocBits normaal gesproken automatisch via uw ION-datastroom. Deze pagina beschrijft hoe u een **Receive Delivery BOD** handmatig verstuurt — handig wanneer u een ontvangst opnieuw wilt importeren, een batch wilt laden die nooit is aangekomen, of een veldtoewijzing wilt testen voordat u de automatische stroom inschakelt.

## Twee manieren om dezelfde BOD te versturen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-endpoints.png)

| Endpoint | Wanneer u het gebruikt |
| --- | --- |
| `/import/receive_delivery_bod` | U hebt de BOD als **XML-bestand** en wilt het uploaden. |
| `/import/receive_delivery_bod_xml` | U wilt de **XML-inhoud** in het verzoek meesturen in plaats van een bestand. De BOD moet in JSON worden verpakt, dus dit past bij korte XML of bij een ander systeem dat de API aanroept — voor een volledige BOD met de hand kunt u beter het bestand uploaden. |

Beide worden hieronder beschreven. Stap 1 en 2 zijn in beide gevallen hetzelfde.

## Voordat u begint

U hebt nodig:

* **Een API key.** Zie [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) als u er nog geen hebt.
* **De BOD** — een `SyncReceiveDelivery`-XML-bestand, of de inhoud daarvan.
* **Uw Org ID**, uit **Settings → Integration & SSO**, in de sectie **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** toont de suborganisatie die in de koptekst is geselecteerd. Met **CROSS** geselecteerd — de weergave over alle suborganisaties heen — toont het dezelfde waarde als **Org ID**. Schakel eerst naar een specifieke suborganisatie als u het ID daarvan nodig hebt.

Als u niet in een specifieke suborganisatie importeert, laat u het veld `sub_org_id` leeg.
{% endhint %}

## Stapsgewijze instructies

### 1. De API-link openen

Open de testinterface van de API voor de omgeving en regio waarmee u werkt:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Sandbox API (Verenigde Staten)](https://us.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Verenigde Staten)](https://us.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)

Klap het gewenste endpoint uit door erop te klikken.

{% hint style="info" %}
Gebruik de regio waarin uw organisatie wordt gehost — dezelfde regio waarmee u bij DocBits inlogt. De Europese en Amerikaanse omgevingen staan los van elkaar, dus een import die naar de verkeerde regio wordt gestuurd, verschijnt niet in uw organisatie.

De adressen zonder regiovoorvoegsel — `api.docbits.com` en `sandbox.api.docbits.com` — wijzen naar Europa. U komt ze tegen in oudere documentatie en in bestaande configuraties; het is dezelfde omgeving als de `eu.`-adressen hierboven.
{% endhint %}

### 2. Autoriseren

Alles onder **import** is vergrendeld totdat u autoriseert. Er zijn twee dingen in te vullen: uw organisatie en uw API key.

* Klik op het **slotpictogram** rechts van het endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-lock.png)

* Het dialoogvenster **Available authorizations** opent met twee items.
* Plak uw **Org ID** in **X-ORG-ID** en klik op **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Scroll naar **X-API-KEY**, plak uw API key en klik op **Authorize**. In DocBits vindt u die onder **Settings → Integration & SSO**, in de sectie **API Key**, of u kunt [een nieuwe sleutel aanmaken](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#een-api-sleutel-aanmaken).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Klik op **Close**.

{% hint style="info" %}
Plak de sleutel op zichzelf — zet er geen `Bearer` voor. Beide autorisaties blijven staan totdat u de pagina herlaadt of op **Logout** klikt.
{% endhint %}

### 3. De velden invullen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-rd.png)

Klik op **Try it out** en vul vervolgens het formulier in van het endpoint dat u hebt gekozen.

#### Een bestand uploaden — `/import/receive_delivery_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-form.png)

| Veld | |
| --- | --- |
| **file** | Verplicht. Klik op **Choose file** en selecteer uw `SyncReceiveDelivery`-XML-bestand. |
| **org\_id** | Uw Org ID — dezelfde waarde die u in stap 2 in **X-ORG-ID** hebt gezet. Die hier ook invullen maakt expliciet naar welke organisatie het verzoek schrijft. Het moet een organisatie zijn waartoe uw API key toegang heeft; elke andere wordt geweigerd. |
| **sub\_org\_id** | Alleen nodig als u in een specifieke suborganisatie importeert. |
| **custom\_fields\_mapping** | Optioneel. Extra kopvelden. Zie [Aangepaste veldtoewijzingen](#aangepaste-veldtoewijzingen) hieronder. |
| **custom\_line\_fields\_mapping** | Optioneel. Hetzelfde, voor extra velden op de ontvangstregels. |
| **populate\_additional\_info** | Optioneel, standaard `false`. Zet het op `true` om DocBits na de import aanvullende ontvangstinformatie uit het ERP te laten ophalen. Laat het op `false` tenzij u weet dat u het nodig hebt — het maakt de import trager. |

{% hint style="warning" %}
**`string` is een waarde, geen tijdelijke aanduiding.** Swagger vult de optionele velden met het woord `string`, en het wordt ongewijzigd verstuurd als u het laat staan — een import met `org_id` op `string` mislukt.

Maak elk optioneel veld dat u niet wilt gebruiken leeg. Leegmaken schakelt het selectievakje **Send empty value** eronder in, dat u dan kunt aanvinken.
{% endhint %}

#### Aangepaste veldtoewijzingen

Beide toewijzingsvelden verwachten een JSON-object. De **naam links moet een van DocBits' eigen aangepaste velden zijn** — `custom_field_1` tot en met `custom_field_10` voor goederenontvangsten, twee keer zoveel als inkooporders toestaan. Elke andere naam wordt zonder waarschuwing genegeerd, dus een typefout hier ziet er precies zo uit als een toewijzing die niet heeft gewerkt.

De waarde rechts is het XPath waaruit wordt gelezen. Schrijf het zonder namespace-voorvoegsels — DocBits voegt die zelf toe:

```json
{"custom_field_2": "//ReceiveDelivery/ReceiveDeliveryHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Regeltoewijzingen gebruiken dezelfde namen `custom_field_1` … `custom_field_10`, maar hun XPaths worden **relatief aan elke ontvangstregel** gelezen en beginnen daarom met `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### De XML plakken — `/import/receive_delivery_bod_xml`

<!-- SCREENSHOT: the Try it out form of /import/receive_delivery_bod_xml -->

Dit endpoint accepteert de BOD niet als eenvoudige plakactie. Het veld **xml** is een object, vooringevuld met `{"xml": "string"}`. Vervang `string` door de inhoud van uw BOD en behoud de omringende aanhalingstekens en accolades:

```json
{
  "xml": "<SyncReceiveDelivery ...>...</SyncReceiveDelivery>"
}
```

{% hint style="warning" %}
De BOD staat binnen een JSON-string, dus elk dubbel aanhalingsteken in de XML moet worden ge-escaped als `\"` — en een BOD staat er vol mee. Als het resultaat geen geldige JSON is, mislukt het verzoek met een **422** en wordt er niets geïmporteerd.

Voor een echte BOD is dat lastig met de hand, dus geef de voorkeur aan het **uploaden van het bestand**.
{% endhint %}

Dit endpoint accepteert `org_id`, `sub_org_id` en `populate_additional_info`, maar **helemaal geen veldtoewijzingen** — kop noch regel. Als uw ontvangsten aangepaste velden nodig hebben, upload dan het bestand.

{% hint style="warning" %}
Controleer naar welke omgeving en welke organisatie u wijst voordat u uitvoert. Een import schrijft rechtstreeks in de stamgegevens van die organisatie.
{% endhint %}

### 4. Uitvoeren

Controleer voordat u uitvoert de keuzelijst **Servers** onderaan het formulier. Die bepaalt naar welke omgeving het verzoek daadwerkelijk wordt gestuurd, en kan afwijken van de pagina die u hebt geopend.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-execute.png)

Klik op **Execute**. Een geslaagde import geeft terug:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-response.png)

Receive delivery BOD's worden verwerkt terwijl u wacht, dus tegen de tijd dat u dit bericht ziet, staan de gegevens erin.

Als er iets mis was met het verzoek, krijgt u `"success": false` met een bericht dat het probleem beschrijft.

### 5. Controleren of de gegevens zijn aangekomen

* Ga in DocBits naar **Settings → Document Processing → Lookup Master Data**.
* Selecteer links **BOD Input Data** en open vervolgens het tabblad van de gegevens die u hebt geïmporteerd.
* Zoek naar de ontvangst of de inkooporder waartoe die behoort.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the goods receipt data shown -->

{% hint style="info" %}
DocBits bepaalt wat er met de BOD gebeurt door het type erin te lezen, niet aan de hand van het gebruikte import-endpoint. Als u hier per ongeluk een andere BOD verstuurt, wordt die als dat type geïmporteerd in plaats van geweigerd — controleer dus of het tabblad waarin u de gegevens terugvindt, het tabblad is dat u verwachtte.
{% endhint %}
