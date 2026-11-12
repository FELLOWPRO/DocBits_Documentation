# Inkooporder

## Overzicht

Deze instelling schakelt de sectie [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) in, die na de documentvalidatie bereikbaar wordt.

<mark style="color:red;">**Opmerking**</mark>: Voor het documenttype **Invoice** moeten daarnaast de volgende voorwaarden gelden:

* De instelling **Purchase Order** moet zijn ingeschakeld (zoals op deze pagina beschreven)
* De factuur moet van het type **Purchase Invoice** zijn
* Een **Extracted Table** moet aanwezig zijn

## Activatiestappen <a href="#activation-steps" id="activation-steps"></a>

1. Ga naar **Settings → Document Types**.
2. Zoek de kaart van het documenttype en klik op het tandwiel (**More Settings**).
3. Open de sectie **Purchase Order** en schakel **Purchase Order** in.

<figure><img src="../../../../../../.gitbook/assets/po-settings-purchase-order-nl-20261031.png" alt="More Settings van het documenttype Invoice met de sectie Purchase Order open"><figcaption><p>De sectie <strong>Purchase Order</strong> in <strong>More Settings</strong>. De eerste schakelaar schakelt de inkooporderafstemming voor het documenttype in, de schakelaars eronder verfijnen die.</p></figcaption></figure>

## **Functionaliteit**

Zodra de instelling is ingeschakeld, is de sectie [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) na de documentvalidatie beschikbaar.

### Welke hoeveelheid wordt vergeleken

Welke hoeveelheid van de inkooporder de afstemming gebruikt, hangt af van **PO match server side**:

* **PO match server side off** – naast de schakelaar **Purchase Order** staat een keuzelijst **Match quantity**. Kies **Quantity**, **Received Quantity** of **Received Delivery Open Quantity**. DocBits stemt af met de ingebouwde matcher en vergelijkt de gekozen hoeveelheid.
* **PO match server side on** – de afstemming gebruikt de regelset van het documenttype, en **Match quantity** hoort bij die regels. De kopregel van de sectie toont dan de link **Configure PO matching rules**, die de regels opent. Zie [Purchase Order Matching Rules](purchase-order-matching-rules.md).

{% hint style="info" %}
De opname hierboven is gemaakt met **PO match server side** aan; de keuzelijst **Match quantity** staat daarom niet op dat scherm - die wordt in de afstemmingsregels ingesteld.
{% endhint %}

### Vooruitbetaling vóór goederenontvangst

Sommige facturen komen eerder dan de goederen. Om zo'n factuur af te stemmen op de bestelde in plaats van de ontvangen hoeveelheid, schakelt u **Allow pre-payment before goods receipt** in dezelfde sectie in.

De schakelaar verschijnt alleen als alle drie gelden:

* het documenttype is **Invoice**,
* **Purchase Order** is ingeschakeld,
* en de afgestemde hoeveelheid is **Received Quantity**.

Wijzigt u de afgestemde hoeveelheid in een andere waarde, dan verdwijnt de schakelaar uit de instellingen. Op het [PO matching screen](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) verschijnt dan **Match as pre-payment** onder **Use Lines Net Amount for Matched Total**, met de hint *Match on ordered quantity instead of received quantity*. De schakelaar is uitgegrijsd en voorzien van een notitie wanneer de leverancier in het ERP niet vóór de goederenontvangst mag worden gefactureerd.

Zolang de schakelaar aan staat, leest het scherm voor handmatige koppelingen en voor het afgestemde totaal de bestelde hoeveelheid, niet de ontvangen. De keuze wordt op het document opgeslagen en **Auto Match** loopt opnieuw; mislukt die afstemming, dan keert de keuze terug naar de vorige waarde.
