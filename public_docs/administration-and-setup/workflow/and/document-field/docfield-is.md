# Documentveld vergelijken met een referentiewaarde

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v1-nl-nl.png" alt="Documentveld vergelijken met een referentiewaarde, Versie 1" width="634"><figcaption><p>Versie 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v2-nl-nl.png" alt="Documentveld vergelijken met een referentiewaarde, Versie 2" width="634"><figcaption><p>Versie 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4" %}

**Video:** Kaart: Documentveld vergeleken met een waarde · 0:46 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Documentveld vergeleken met een waarde** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=0.25)

De kaart Documentveld vergelijkt één veld van het document met een waarde die u invoert. Kies het veld, bijvoorbeeld Totaalbedrag, dan de operator, hier Groter dan, en de waarde, tienduizend.

**Tekst, getallen, datums** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=19.05)

Tekstvelden kunnen alleen gelijk of niet gelijk zijn, en hoofdletters maken niet uit. Getallen en datums kunnen ook groter of kleiner dan de waarde zijn. Staat het veld niet op het document, dan neemt de kaart het foutpad.

**Voorbeeld: grote facturen hebben een tweede goedkeuring nodig** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=33.183)

Bijvoorbeeld een tweede goedkeuring voor grote facturen: Totaalbedrag groter dan tienduizend, dan de toewijzingskaart voor financiën. Kleinere facturen bereiken deze stap niet.

</details>

## **Doel:**

Deze kaart vergelijkt één veld van het document met een waarde die u op de kaart invoert. Gebruik haar om documenten afhankelijk van een veldwaarde langs verschillende paden te sturen, bijvoorbeeld een tweede goedkeuring voor grote facturen of een aparte route voor enkele leveranciers.

Op de kaart staat: **Docveld** [Veldnaam] [Operator] [Field Value].

## **Onderdelen van de kaart:**

1. **Veldnaam**
   * Het documentveld dat wordt gecontroleerd, gekozen uit de velden van het documenttype.
2. **Operator**
   * Hoe de veldwaarde met de **Field Value** wordt vergeleken. Welke operatoren zinvol zijn, hangt af van het type van het veld, zie **Operatoren** hieronder.
3. **Field Value**
   * De waarde waarmee wordt vergeleken. Afhankelijk van de operator is dit één waarde, een door komma's gescheiden lijst of een reguliere expressie.

## **Operatoren:**

| Operator | Voldaan als | Veldtypen |
| --- | --- | --- |
| **is gelijk aan** (=) | de veldwaarde gelijk is aan de Field Value | tekst, getal, bedrag, datum |
| **Niet gelijk** (≠) | de veldwaarde verschilt van de Field Value | tekst, getal, bedrag, datum |
| **Groter dan** (>) | de veldwaarde groter is dan de Field Value | getal, bedrag, datum |
| **Groter of gelijk aan** (≥) | de veldwaarde groter dan of gelijk aan de Field Value is | getal, bedrag, datum |
| **Minder dan** (<) | de veldwaarde kleiner is dan de Field Value | getal, bedrag, datum |
| **Kleiner of gelijk aan** (≤) | de veldwaarde kleiner dan of gelijk aan de Field Value is | getal, bedrag, datum |
| **Is een van** | de veldwaarde gelijk is aan één item van een door komma's gescheiden lijst | tekst |
| **Is geen van** | de veldwaarde aan geen van de items van de lijst gelijk is | tekst |
| **Komt overeen met regex** | de reguliere expressie in de veldwaarde wordt gevonden | tekst, getal, bedrag, datum |
| **Komt niet overeen met regex** | de reguliere expressie niet in de veldwaarde wordt gevonden | tekst, getal, bedrag, datum |

Booleaanse velden (selectievakjes) worden door deze kaart niet ondersteund. Gebruik daarvoor **Selectievakje is aangevinkt**.

### is gelijk aan en Niet gelijk bij tekstvelden

Tekst wordt vergeleken zonder rekening te houden met hoofdletters, en een spatie telt hetzelfde als een underscore: `Acme Freight` is gelijk aan `acme_freight`. Spaties aan het begin en einde worden genegeerd.

### Is een van en Is geen van

Gebruik deze operatoren om een tekstveld in één keer met meerdere waarden te vergelijken, bijvoorbeeld met een lijst leveranciers-ID's.

* Voer de waarden in als door komma's gescheiden lijst: `40321,40322,40388`.
* De veldwaarde moet exact gelijk zijn aan één item. Een gedeeltelijke waarde is geen overeenkomst: `4032` is geen item van `40321,40322,40388`, en een langere waarde zoals `403210` evenmin.
* Hoofdletters maken niet uit, en een spatie telt hetzelfde als een underscore. Spaties rond de items worden genegeerd, en lege items zoals het item in `a,,b` worden overgeslagen.
* Om een komma binnen een waarde te gebruiken, schrijft u die als `\,`. `Acme Freight\, LLC,Riverside Supply` is een lijst van twee items: `Acme Freight, LLC` en `Riverside Supply`.
* Een lege veldwaarde staat in geen enkele lijst. **Is een van** is dan niet voldaan, en **Is geen van** is voldaan.
* Deze operatoren werken alleen bij tekstvelden. Bij een getal-, bedrag- of datumveld, of bij een lijst zonder items (bijvoorbeeld alleen komma's), eindigt de kaart met een fout.

### Komt overeen met regex en Komt niet overeen met regex

Gebruik deze operatoren wanneer een patroon beslist, bijvoorbeeld "begint met" of "bestaat alleen uit cijfers".

* De **Field Value** is een reguliere expressie in Python-syntaxis. Er wordt overal in de veldwaarde naar gezocht: `Freight` komt overeen met `Acme Freight, LLC`.
* Gebruik `^` en `$` om de hele waarde te controleren: `^33` betekent "begint met 33", en `^(40321|40322|40388)$` betekent "exact een van deze waarden".
* Het patroon is hoofdlettergevoelig. Begin het met `(?i)` om hoofdletters te negeren: `(?i)freight` komt ook overeen met `Acme Freight, LLC`.
* `^` en `$` verwijzen naar de hele veldwaarde. Begin het patroon met `(?m)` om ze op elke regel van een waarde met meerdere regels toe te passen.
* Het patroon wordt exact gebruikt zoals u het typt. Het wordt niet ingekort en hoofdletters blijven behouden, zodat `\D` (elk teken dat geen cijfer is) zijn betekenis houdt, en een patroon dat uit één spatie bestaat naar een spatie zoekt.
* Tekens met een speciale betekenis in reguliere expressies moeten worden geëscaped om letterlijk te worden gevonden: `\(copy\)` komt overeen met de tekst `(copy)`, terwijl `(copy)` een groep is die het woord `copy` vindt.
* Getallen, bedragen en datums worden vergeleken als de tekst waarin ze zijn opgeslagen: een bedrag van 997.60 komt overeen met `^997\.60$`.
* Een lege veldwaarde wordt als lege tekst vergeleken, dus `^$` komt ermee overeen.
* Een ongeldig patroon, bijvoorbeeld `(20` met een ontbrekend haakje, beëindigt de kaart met een fout. Hetzelfde gebeurt wanneer een patroon te lang duurt voor een waarde (meer dan 0,05 seconden), wat alleen voorkomt bij slecht opgebouwde patronen zoals `(a|aa)+$`. In beide gevallen is de kaart voldaan noch niet voldaan, dus **Komt niet overeen met regex** slaagt nooit door een kapot patroon.

## **Hoe de kaart werkt:**

* **Veld niet op het document:** als het document geen veld met de gekozen naam heeft, stopt de kaart en meldt ze dat het veld niet is gevonden, ongeacht de operator.
* **Voorwaarde voldaan:** de Workflow gaat verder met de volgende kaart (in de Advanced Workflow via de succesuitgang).
* **Voorwaarde niet voldaan:** de Workflow stopt bij deze kaart (in de Advanced Workflow neemt ze de uitgang voor een niet-vervulde voorwaarde).
* **Fout:** een operator die niet bij het veldtype past, een ontbrekende Field Value, een lege lijst of een onbruikbaar patroon beëindigen de kaart met een fout. Het kaartlogboek toont de reden.

## **Opzet en configuratie:**

Kies het veld bij **Veldnaam**, de operator bij **Operator** en voer de waarde in bij **Field Value**. Voer bij getallen en bedragen de waarde in zonder valutasymbool en met een decimale punt, bijvoorbeeld `1000.50`.

Om een configuratie te proberen zonder op een document te wachten, opent u het kaartmenu in de **Workflow Builder**, kiest u **Testkaart**, kiest u een document en selecteert u **Test op document**. Het kaartlogboek toont de veldwaarde, de operator en het resultaat.

## **Voorbeelden:**

| Doel | Veldnaam | Operator | Field Value | Veldwaarde op het document | Resultaat |
| --- | --- | --- | --- | --- | --- |
| Tweede goedkeuring voor grote facturen | Totaalbedrag | Groter dan | `10000` | 12500.00 | voldaan |
| Enkele leveranciers routeren | Leveranciers-ID | Is een van | `40321,40322,40388` | 40322 | voldaan |
| | | | | 4032 | niet voldaan |
| Een leverancier met een komma in de naam overslaan | Leveranciersnaam | Is geen van | `Acme Freight\, LLC` | Acme Freight, LLC | niet voldaan |
| Ordernummers die met 33 beginnen | Ordernummer | Komt overeen met regex | `^33` | 33012 | voldaan |
| | | | | 13301 | niet voldaan |
| Referentie met letters | Referentie | Komt overeen met regex | `\D` | AB-1204 | voldaan |
| Kopieën van facturen | Factuurnummer | Komt niet overeen met regex | `\(copy\)` | INV-1204 (copy) | niet voldaan |

## **Conclusie:**

De kaart controleert één documentveld tegen een waarde, een lijst of een patroon. Gebruik **Is een van** voor vaste lijsten van waarden en **Komt overeen met regex** voor patronen zoals voorvoegsels of formaten.

<!-- workflow-card-practical-example-20261021 -->

## Praktisch voorbeeld

**Wanneer gebruiken:** Facturen boven een bepaald bedrag bekijken.

**Configuratie:** Selecteer numeriek veld `total_amount`, operator `>` en referentiewaarde `1000`.

**Verwacht resultaat en tegenvoorbeeld:** Een waarde van `1200` voldoet aan de voorwaarde. `1000` en `900` voldoen niet: de operator `>` vereist een waarde groter dan `1000`.

Dit is een illustratieve configuratie en een verwacht resultaat. Gebruik velden, gebruikers en groepen die in uw testorganisatie zijn geconfigureerd; het is geen bewering dat dit voorbeeld is uitgevoerd.
