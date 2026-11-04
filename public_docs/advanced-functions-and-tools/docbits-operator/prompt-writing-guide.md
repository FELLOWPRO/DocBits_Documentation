# Prompt Schrijfgids

Deze gids legt uit hoe je effectieve prompts schrijft voor de DocBits Operator. Prompts zijn stapsgewijze instructies die de operator begeleiden bij het uitvoeren van specifieke taken, zoals het navigeren op webpagina's, het interacteren met UI-elementen en het invoeren van gegevens.

## Wat is een Prompt?

Een prompt is een reeks instructies geschreven in tekst die de operator begeleidt bij het uitvoeren van een workflow. Prompts kunnen commando's bevatten zoals het klikken op knoppen, het invullen van formulieren, wachten op het laden van pagina's of elementen, en meer.

## Prompt Syntax en Structuur

* Elke instructie moet worden geschreven als een genummerde stap.
* Gebruik duidelijke, beknopte taal om elke actie te beschrijven.
* Specificeer UI-elementen op naam, label of indexnummer om precisie te garanderen.
* Gebruik consistente opmaak om de leesbaarheid te verbeteren.

## Gebruik van Variabelen in Prompts

Variabelen stellen je in staat om prompts dynamisch te maken door verschillende waarden in te voegen tijdens runtime. In plaats van waarden zoals datums of documentnummers hard te coderen, gebruik je placeholders binnen accolades—bijvoorbeeld: `{invoice_number}`, `{url}`, of `{purchase_order}`.

Dit maakt prompts herbruikbaar en aanpasbaar voor verschillende workflows of datasets.

### Hoe Variabelen te Gebruiken

* Schrijf variabelen binnen accolades in je prompttekst:
  * Voer het factuurnummer in: {invoice\_number} in het veld 'Factuurnummer HP'.
* Elke variabele moet een unieke naam hebben (bijv. `invoice_number`, `url`, `document_type`).
* Variabelenamen mogen geen spaties of speciale tekens bevatten (underscores zijn toegestaan).
* Voor workflows moeten variabelenamen exact overeenkomen met de veld-ID's van het document om automatische gegevenskoppeling mogelijk te maken.

## Prompt Variabelen Pop-up

Om de Prompt Variabelen pop-up te openen, klik je op het **tandwielicoon** naast het invoerveld voor de prompt.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Pop-up Lay-out en Bedieningselementen

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Sleutel Invoerveld:** Voer hier de variabelenaam in (zonder accolades).
* **Waarde Invoerveld:** Voer de waarde in die moet worden gebruikt voor deze variabele wanneer de prompt wordt uitgevoerd.
* **Opslaan als Gevoelig (Checkbox):** Wanneer aangevinkt, markeert dit de variabele waarde als gevoelig. Gevoelige waarden worden versleuteld en verborgen in workflows om vertrouwelijke informatie te beschermen tegen onbevoegde gebruikers.
* **Toevoegen Knop (+):** Klik om een andere invoerrij voor sleutel-waarde toe te voegen.
* **Verwijder Pictogram (Prullenbak):** Wanneer er meerdere sleutel-waardeparen bestaan, tonen alle paren behalve de eerste een klein prullenbakpictogram om dat specifieke paar te verwijderen.
* **Wissen Knop:** Reset de pop-up door alle sleutel-waardeparen en ingevoerde waarden te wissen.
* **Opslaan Knop :** Slaat alle gedefinieerde variabelen en hun waarden op voor de huidige prompt.
