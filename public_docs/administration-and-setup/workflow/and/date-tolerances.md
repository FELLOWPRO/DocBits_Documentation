# Datumtoleranties

Verschillende workflowkaarten vergelijken een datum met een referentiedatum en accepteren een tolerantie van een aantal dagen. Ze berekenen de tolerantie allemaal op dezelfde manier. Deze pagina legt die berekening uit, wat elke operator betekent, hoe de **Toegestane tolerantiedagen** werken en hoe twee kaarten kunnen worden gecombineerd voor bereiken zoals "vandaag of morgen".

De kaarten die deze berekening gebruiken:

* [Table Date to Current Date](table/table-date-to-current-date.md) – een datum in een documenttabel vergeleken met de huidige datum.
* [Promised delivery date for line items in table with promised delivery date](compare-with-purchase-order/promised-delivery-date-for-line-items-in-table-with-promised-delivery-date/README.md) – beloofde leverdata van regelitems vergeleken met de huidige datum.
* [Promised Delivery Date on Purchase Order](compare-with-purchase-order/promised-delivery-date-on-purchase-order.md) – leverdata van regelitems vergeleken met de leverdatum op de inkooporder.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4" %}

**Video:** Datumtoleranties en bereikcontroles · 2:11 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Datums met een tolerantie** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=0.25)

Diverse Workflow-kaarten vergelijken een datum met een referentiedatum, met een tolerantie in dagen. Ze tellen die tolerantie allemaal hetzelfde.

**Het tolerantievenster** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=11.016)

Vanaf de referentiedatum wordt de tolerantie terug en vooruit geteld. Het resultaat is een venster, en beide uiteinden horen erbij.

**Twee dagen: dinsdag tot zaterdag** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=20.816)

Met twee dagen rond donderdag de tweeëntwintigste loopt het venster van dinsdag de twintigste tot zaterdag de vierentwintigste. Vandaag is de datum op de DocBits-servers, in U T C.

**Zes operatoren, één venster** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=33.583)

Is gelijk aan accepteert datums binnen het venster, Niet gelijk datums erbuiten. Groter of gelijk aan begint bij het begin van het venster, Groter dan na het einde. Kleiner of gelijk aan en Kleiner dan werken andersom.

**Operator, dagen en weekdagen** · [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=49.216)

Kies in de kaart de operator, de tolerantie in dagen en de weekdagen die meetellen.

**Alleen geselecteerde weekdagen tellen** · [1:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=62.716)

Toegestane tolerantiedagen tellen alleen de geselecteerde weekdagen. Met maandag tot en met vrijdag is één dag na vrijdag maandag, dus het venster loopt van donderdag tot maandag.

**Bereiken vragen twee kaarten** · [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=74.916)

Eén kaart kan niet precies vandaag of morgen accepteren, want haar venster reikt in beide richtingen even ver. Twee kaarten na elkaar kunnen dat wel.

**Is gelijk aan 1 dag, dan Groter of gelijk aan 0 dagen** · [1:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=88.383)

De eerste kaart, Is gelijk aan met één dag, accepteert gisteren, vandaag en morgen. De tweede, Groter of gelijk aan met nul dagen, accepteert vandaag en elke latere dag. Alleen vandaag en morgen halen beide.

**Een dag uitsluiten met Niet gelijk** · [1:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=104.983)

Om één dag uit te sluiten, voegt u een kaart Niet gelijk met nul dagen toe. Hier geven Is gelijk aan met drie dagen en Groter of gelijk aan met nul dagen vandaag tot drie dagen vooruit; Niet gelijk haalt vandaag weg.

**Drie kaarten, één bereik** · [1:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/nl.mp4#t=119.883)

In de designer volgen de drie kaarten elkaar op het succespad. De Workflow gaat alleen verder als alle drie slagen: van morgen tot drie dagen vooruit.

</details>

## Het tolerantievenster

Vanaf de referentiedatum wordt de tolerantie terug en vooruit geteld. Het resultaat is een **tolerantievenster**: van de begindatum tot en met de einddatum, beide inbegrepen.

* Met een tolerantie van **0 dagen** bestaat het venster alleen uit de referentiedatum zelf.
* Met een tolerantie van **2 dagen** reikt het venster van 2 dagen vóór tot 2 dagen na de referentiedatum.
* De **huidige datum** is de datum op de DocBits-servers, die in **UTC** draaien.

Elke operator vergelijkt de datum met dit venster:

| Operator | Waar wanneer de datum … |
|---|---|
| **is gelijk aan** | binnen het venster ligt |
| **Niet gelijk** | buiten het venster ligt |
| **Groter of gelijk aan** | op of na het **begin** van het venster ligt |
| **Groter dan** | na het **einde** van het venster ligt |
| **Kleiner of gelijk aan** | op of vóór het **einde** van het venster ligt |
| **Minder dan** | vóór het **begin** van het venster ligt |

De tolerantie verruimt ook **Groter of gelijk aan** en **Kleiner of gelijk aan**: met 2 dagen accepteert **Groter of gelijk aan** al een datum die 2 dagen vóór de referentiedatum ligt.

<figure><img src="../../../.gitbook/assets/date-tolerance-operators-nl-nl.png" alt="Tolerantievenster van 2 dagen rond een donderdag en de dagen die elke operator accepteert"><figcaption><p>Referentiedatum donderdag 22, 2 dagen tolerantie: het venster loopt van dinsdag 20 tot en met zaterdag 24.</p></figcaption></figure>

## Toegestane tolerantiedagen

Kaarten met **Toegestane tolerantiedagen** tellen bij de berekening van het venster alleen de geselecteerde weekdagen mee. Weekdagen die niet zijn geselecteerd, worden bij het tellen overgeslagen, maar blijven binnen het venster.

**Voorbeeld:** referentiedatum vrijdag, 1 dag tolerantie, alleen maandag tot en met vrijdag geselecteerd. Terugtellen komt uit op donderdag. Vooruittellen slaat zaterdag en zondag over en komt uit op maandag. Het venster is **donderdag tot en met maandag**.

**Table Date to Current Date** voegt nog een controle toe: de datum in de tabel hoort ook op een van de geselecteerde weekdagen te vallen. Een zaterdag binnen het venster wordt door deze kaart daarom niet geaccepteerd. De twee andere kaarten hebben deze extra controle niet.

<figure><img src="../../../.gitbook/assets/date-tolerance-weekdays-nl-nl.png" alt="Venster van 1 dag rond een vrijdag waarbij alleen maandag tot en met vrijdag worden meegeteld"><figcaption><p>Alleen maandag tot en met vrijdag worden meegeteld, dus 1 dag na vrijdag is maandag.</p></figcaption></figure>

## Voorbeeld: vandaag of morgen

Eén kaart kan niet precies "vandaag of morgen" accepteren, omdat het venster altijd evenveel dagen in beide richtingen reikt. Twee kaarten na elkaar kunnen dat wel:

1. **is gelijk aan** met **1 dag** tolerantie accepteert gisteren, vandaag en morgen.
2. **Groter of gelijk aan** met **0 dagen** tolerantie accepteert vandaag en elke latere dag.

Alleen data die door beide kaarten komen, blijven over: **vandaag en morgen**.

<figure><img src="../../../.gitbook/assets/date-tolerance-today-or-tomorrow-nl-nl.png" alt="is gelijk aan met 1 dag en Groter of gelijk aan met 0 dagen, die samen vandaag en morgen accepteren"><figcaption><p>Vandaag is donderdag 22: samen accepteren de twee kaarten donderdag 22 en vrijdag 23.</p></figcaption></figure>

Op dezelfde manier kunnen andere bereiken worden opgebouwd:

| Bereik | Eerste kaart | Tweede kaart |
|---|---|---|
| Vandaag of morgen | **is gelijk aan**, 1 dag | **Groter of gelijk aan**, 0 dagen |
| Gisteren of vandaag | **is gelijk aan**, 1 dag | **Kleiner of gelijk aan**, 0 dagen |
| Vandaag tot 3 dagen vooruit | **is gelijk aan**, 3 dagen | **Groter of gelijk aan**, 0 dagen |
| Niet vandaag | **Niet gelijk**, 0 dagen | – |
| Vanaf overmorgen | **Groter dan**, 1 dag | – |

Zijn alleen maandag tot en met vrijdag als **Toegestane tolerantiedagen** geselecteerd, dan is "morgen" op een vrijdag de maandag daarna.

## Conclusie

Alle datumkaarten met een tolerantie gebruiken één venster rond de referentiedatum. Wie weet waar het venster begint en eindigt, ziet duidelijk wat elke operator accepteert, en twee kaarten samen kunnen bereiken afdekken die één kaart niet kan afdekken.
