---
description: >-
  Waar de waarde van een koptekstveld vandaan komt en hoe die ontstaat — de
  uitleg achter de Koptekstveldcontrole op het validatiescherm.
---

# Koptekstveldcontrole: waar de gegevens vandaan komen

De knop **Koptekstveldcontrole** staat naast **Opslaan** op het validatiescherm. Hij opent het rapport *Waar komt elke waarde vandaan?*: voor elk koptekstveld laat het zien wat er op het document stond, wat de waarde onderweg heeft veranderd, wat DocBits nu toont en waarom.

Deze pagina legt uit hoe een waarde ontstaat en wat elke bron betekent. Er is geen expertkennis nodig.

{% hint style="info" %}
De Koptekstveldcontrole maakt deel uit van de module **Analytics**. Als de knop grijs is, kan een beheerder hem aan uw rol toekennen onder **Instellingen › Rollen**.
{% endhint %}

## Een waarde ontstaat altijd in deze volgorde

| Stap | Wat er gebeurt |
| --- | --- |
| **1. Lezen** | De waarde wordt uit het document gelezen — door een getrainde regel, door de AI of rechtstreeks uit een e-factuur. |
| **2. Omvormen** | De scripts en transformatieregels van de klant wijzigen de gelezen waarde: inkorten, aanvullen, het formaat aanpassen. |
| **3. Opzoeken** | De waarde wordt in de stamgegevens gezocht. Wordt er iets gevonden, dan vervangt het stamgegevensrecord de gelezen waarde. |
| **4. Weergeven** | De gebruiker ziet alleen het resultaat. Wat er onderweg is gebeurd, toont de Koptekstveldcontrole. |

Stap 2 en 3 worden niet altijd uitgevoerd — maar als ze dat wel worden, veranderen ze de waarde. Precies daar komen de meeste gemelde gevallen vandaan.

## De bronnen — wat elke bron betekent

De pictogrammen zijn dezelfde als die het rapport toont in de kolom **Actie** en in de filterbalk bovenaan.

### Getrainde regel

DocBits onthoudt waar een veld op dit documenttype staat, omdat iemand het daar ooit heeft gemarkeerd.

* **Voorbeeld:** leverancier “Bornemann” — altijd op dezelfde plek linksboven.
* **Als het fout is:** markeer de juiste plek op het document en sla op — de regel leert ervan.

### AI

Geen vast patroon. De AI leest het document als een mens en beslist zelf welke tekst bij welk veld hoort.

* **Voorbeeld:** factuurdatum, bedragen, betalingsvoorwaarden.
* **Als het fout is:** corrigeer het. In- en uitschakelen kan onder **Instellingen › OCR-koptekstvelden**.

### E-factuur

Bij XRechnung of ZUGFeRD wordt niets herkend: de waarde is in het document al een gegevensveld en wordt rechtstreeks overgenomen.

* **Voorbeeld:** factuurnummer uit het XML-veld van de afzender.
* **Als het fout is:** de fout ligt bij de afzender. DocBits toont precies uit welk XML-veld de waarde komt.

### Script / transformatieregel

Na het lezen grijpt de logica van de klant in en vormt de waarde om. Het document blijft gelijk — de waarde niet.

* **Voorbeeld:** `1001 / LS 206776` wordt `1001`.
* **Als het fout is:** zoek niet op het document. Controleer **Instellingen › Scripts** of **Transformatieregels**.

### Stamgegevens

De gelezen waarde wordt gezocht in uw eigen gegevens — bestellingen, leveranciers. Een treffer vervangt de waarde en trekt andere velden mee.

* **Voorbeeld:** `1001` vindt bestelling `06O051001` — en leverancier en koper komen dan ook van daar.
* **Als het fout is:** controleer **Instellingen › Lookup-configuratie**. Daar staat of het zoeken exact is of ook gedeeltelijke treffers accepteert.

### Berekend

Niet gelezen, maar berekend uit andere velden.

* **Voorbeeld:** vervaldatum uit factuurdatum plus betalingsvoorwaarden.
* **Als het fout is:** meestal is een van de velden waaruit wordt berekend fout.

### Barcode

Gelezen uit een barcode of QR-code op het document.

* **Voorbeeld:** het factuurnummer zit in de QR-code.
* **Als het fout is:** controleer de barcode-instellingen van het documenttype.

## Wat het vaakst verkeerd wordt begrepen

{% hint style="warning" %}
Als een veld plotseling een waarde bevat die zo niet op het document staat, was het bijna nooit de AI — maar stap 2 of stap 3. Meestal de stamgegevenstreffer, die ook gedeeltelijke treffers accepteert: `1001` komt overeen met `06O051001`, en met de gevonden bestelling verandert ook de leverancier.
{% endhint %}

In het rapport is zo'n veld rood gemarkeerd. De kolom **Actie** toont het stamgegevensrecord samen met een rode chip *alleen gedeeltelijke treffer*, en het overeenkomende deel van de waarde is gemarkeerd.

## Het rapport lezen

* **Statuschips** bovenaan tellen de velden die ongewijzigd uit het document kwamen, onderweg zijn veranderd of zo niet op het document staan. Klik op een chip om alleen die velden te tonen; klik opnieuw om alles te tonen.
* **Bronfilter:** de rij pictogrammen toont elke extractiemethode. Klik op een pictogram om alleen de velden te tonen die erdoor zijn gegaan.
* **Actie:** elke stap die de waarde heeft doorlopen, met het pictogram van de bron. De stap waar de huidige waarde vandaan komt, is gemarkeerd. Houd de muisaanwijzer erboven om te zien wat elke stap deed, van welke waarde naar welke.
* **Reden:** de status van het veld. Het (i)-pictogram legt uit waarom de waarde is wat ze is. Staat er *Veld bestond niet*, dan was het veld niet aanwezig op het document.
* Lange waarden worden met … ingekort — houd de muisaanwijzer erboven voor de volledige waarde.
