# Bereken PO eenheidsprijs

## **Overzicht**

Je kunt ervoor kiezen om de **eenheidsprijs** van elke inkooporderregel automatisch te berekenen op basis van het **bedrag** en de **hoeveelheid** van de regel, in plaats van de eenheidsprijs te gebruiken die bij de inkooporder hoort. Dit is vooral handig wanneer de eenheidsprijs in de inkooporder (in Infor ERP / SAP) afwijkt van de prijs op het document. Dergelijke verschillen kunnen ontstaan als er een korting wordt toegepast op de eenheidsprijs in de inkooporder, terwijl het document de korting alleen op het nettobedrag toepast.

## **Activeringsstappen**

1.  Navigeer naar **Instellingen** -> **Globale Instellingen** -> **Documenttypen**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecteer het gewenste documenttype en klik op **Meer Instellingen**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Schakel in de sectie **Inkooporder** de optie **Bereken PO Eenheidsprijs** in.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Hoe de prijs wordt berekend

Zodra de instelling is geactiveerd, wordt de eenheidsprijs van een inkooporderregel als volgt berekend:

**`Eenheidsprijs = Regelbedrag ÷ Hoeveelheid × Eenheidsprijs Per`**

waarbij het **regelbedrag** als volgt wordt gekozen:

| Inkooporderregel bevat                                                                   | Gebruikt regelbedrag                  |
| ---------------------------------------------------------------------------------------- | ------------------------------------ |
| een **netto bedrag** (`extended_amount`) dat groter is dan 0 en niet boven het regel totaal uitkomt | het netto bedrag                     |
| geen netto bedrag, of een netto bedrag boven het regel totaal                            | het regel **totaal** (`total_amount`) |
| geen positief bedrag, of geen positieve hoeveelheid                                      | er wordt niets berekend, de PO-prijs blijft |

Waarom het netto bedrag eerst komt: ERP-feeds (Infor BODs) sturen het netto regelbedrag als `extended_amount` en bevatten **belasting en toeslagen erbovenop** in `total_amount`. Het delen van een belast totaal door de hoeveelheid geeft een bruto eenheidsprijs, en elke factuur die netto wordt geprijsd, toont dan als _eenheidsprijs te laag_ hoewel deze correct is. Voorbeeld van een echte inkooporderregel: hoeveelheid 9, netto bedrag 879,84, totaal 954,63 (8,5% belasting) — de netto-gebaseerde prijs is 97,76 en komt overeen met de factuur; de totaal-gebaseerde prijs zou 106,07 zijn.

Een netto bedrag dat **groter** is dan het regel totaal kan geen netto bedrag zijn, dus wordt in dat geval het totaal gebruikt. Een `Eenheidsprijs Per` van 0 of leeg telt als 1.

{% hint style="info" %}
De berekende prijs wordt weggeschreven naar de inkoopordersnapshot die op het document wordt opgeslagen, en deze wordt **elke keer dat het document wordt gematcht opnieuw berekend** (Auto PO Match, handmatige match, matchen bij opslaan). Een document dat vóór het wijzigen van de instelling al was gematcht, neemt de nieuwe prijs op bij de volgende match — herladen van de inkooporder is niet nodig.
{% endhint %}

## Voorbeeld:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

In dit geval wordt de eenheidsprijs (zonder de korting) uit het document gehaald, terwijl de inkooporder in het ERP de eenheidsprijs met de korting opslaat. Dit resulteert in een mismatch in de eenheidsprijs. Met de instelling geactiveerd wordt de eenheidsprijs in plaats daarvan genomen uit het regelbedrag en de hoeveelheid, zodat beide kanten overeenkomen.

## Gerelateerde instellingen

* [Regels voor het matchen van inkooporders](purchase-order-matching-rules.md) — de regels vergelijken de **effectieve** eenheidsprijs, wat deze berekende prijs is wanneer de instelling aan staat.
* [Instellingen voor inkoopordertolerantie](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — hoeveel de factuurprijs mag afwijken van de berekende prijs.