---
description: "Leerpad van beginner tot expert"
---

# Leerpad van beginner tot expert

Zeven niveaus brengen u van de eerste blik in de workflow-ontwerper tot het zelf verantwoorden van een wijziging in een workflow die in productie draait. Elk niveau noemt een doel, de stappen die u in uw eigen testorganisatie uitvoert en een resultaat dat u kunt controleren. Werk ze op volgorde door en bouw elke oefening zelf: elk niveau bouwt voort op de configuratie van het vorige.

1. [Oriëntatie en uitvoeringsmodel](./#level-1)
2. [Uw eerste eigen regel](./#level-2)
3. [Velden, types en grenzen](./#level-3)
4. [Bedrijfsregels en goedkeuringen](./#level-4)
5. [Advanced-besturing en onderliggende workflows](./#level-5)
6. [Berekening, integratie en export](./#level-6)
7. [Wijzigingen en deskundig beheer](./#level-7)

## Voordat u begint

* Een eigen testorganisatie met een synthetische factuur erin. Oefen nooit op documenten van klanten.
* Uw rol, de workflow-licentie en de Advanced-rechten, gecontroleerd vóór niveau 1.
* Geïmporteerde oefeningen blijven inactief tot u ze hebt getest.
* Volledige JSON-gegevens horen in **Advanced Test → Custom Data**.
* Echte goedkeuringen en integraties hebben eigen testgebruikers en testdoelen nodig; een test in de ontwerper vervangt die niet.

## 1. Oriëntatie en uitvoeringsmodel <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/nl.html).

**Doel:** Weten wat een workflow start en wat een testresultaat wel en niet zegt over een echte uitvoering.

1. Controleer de organisatie, uw toegang, de workflowmodule en de Advanced-rechten.
2. Zeg When–And–Then in eigen woorden en leg daarna uit waar een lineaire regel ophoudt en hoe een Advanced-graaf in plaats daarvan zijn verbonden uitgangen volgt.
3. Houd vier dingen uit elkaar die er in de ontwerper op elkaar lijken: het documenttypefilter, de uitvoeringsgebeurtenis, het opslaan en het activeren.

**Afrondingscriterium:** U kunt zeggen wanneer een regel eigenlijk wordt bekeken en welk bewijs een simulatie van een uitvoering op een echt document scheidt.

**Verdieping:** [Wanneer wordt mijn workflow uitgevoerd?](workflow-execution-model.md) · [Status wijzigen zonder de workflow opnieuw te starten](masterclass/status-and-reentry.md)

## 2. Uw eerste eigen regel <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/nl.html).

**Doel:** Een regel van de ontwerper naar een gecontroleerd resultaat brengen zonder een document aan te raken.

1. Bouw hem in de Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Een lineaire regel van deze omvang heeft geen controleknooppunt nodig.
2. Sla hem op en controleer in de regellijst of hij nog inactief is, want het opslaan van een nieuwe regel kan hem al activeren. Advanced Test is een aparte uitvoeringsoppervlakte: het evalueert de graaf in de builder, niet de geactiveerde regel.
3. Voer Advanced Test uit met volledige gegevens voor 999, 1000 en 1000.01. Noteer per geval veldtype, operator en gekozen uitgang en voeg een geval toe waarin het bedrag helemaal ontbreekt.

**Afrondingscriterium:** REVIEW wordt alleen bij 1000.01 bereikt, een ontbrekend bedrag verschijnt als fout en niet als gewoon resultaat onder de grens, en de regel staat aan het eind weer uit.

**Verdieping:** [Advanced-bedrijfscasus: factuurroutering](advanced-workflow-case-study.md) · [Workflow-oefenpakket](workflow-training-kit.md)

## 3. Velden, types en grenzen <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/nl.html).

**Doel:** Weten wat een voorwaarde werkelijk vergelijkt voordat u op het resultaat vertrouwt.

1. Test de leegcontrole tegen een ontbrekend veld, `null`, lege tekst, spaties, `false`, `0`, `"0"` en `"false"` en noteer welke daarvan als leeg tellen.
2. Reken dezelfde tolerantie van 2 procent twee keer uit: één keer met de bestelling als referentie (bestelling 100, document 102.02) en één keer met het document als referentie.
3. Wissel op de bestelkaart tussen Any en All en tel hoeveel regels werkelijk zijn vergeleken.

**Afrondingscriterium:** U verklaart waar, onwaar en fout vanuit waarde, type, referentie en aanwezige gegevens. In versie 5 van de bestelkaart is een document zonder vergelijkbare regel een gegevensfout en geen geslaagde goedkeuring.

**Verdieping:** [P1: Field is, Docfield is en twee velden vergelijken](masterclass/field-conditions.md) · [P1: Toleranties en bestelreferentie ondubbelzinnig maken](masterclass/tolerances-and-po.md)

## 4. Bedrijfsregels en goedkeuringen <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/nl.html).

**Doel:** Een factuur via een beslissingstabel naar de juiste persoon sturen en daarna een goedkeuringsketen laten lopen die op de eerste controleur wacht.

**Oefening 1: beslissingstabel met directe toewijzing**

1. Maak een beslissingstabel met twee regels die niet samen kunnen gelden: controleur A tot 1000, controleur B boven 1000, met `cost_center=4711` en `total_amount`.
2. Stel in **Decision Table has Returns** versie 3 `store_data=wf_store_data` in. Wijs het document toe met **Assign document based on decision table** en `assignee_type=user` en gebruik echte gebruikers uit uw testorganisatie.
3. Test één overeenkomst, geen overeenkomst, meerdere overeenkomsten en een ongeldige gebruikers-ID, en leid geen-overeenkomst en toewijzingsfouten naar een expliciete terugval. Accepteer de toewijzing op het document zelf.

**Oefening 2: sequentiële goedkeuring zonder directe toewijzing**

1. Maak een tweede, aparte regel met de sequentiële kaarten: de sequentiële toewijzingskaart op positie 10 voor controleur A, daarna de sequentiële taakkaart op positie 20 voor controleur B. Laat de directe toewijzing in deze uitvoering weg, want de gecontroleerde afronding kan de eerste sequentiële ontvanger overslaan wanneer het document in dezelfde uitvoering al direct is toegewezen.
2. Keur goed als A en controleer dat B het document pas krijgt na de verwerkte beslissing van A; keur daarna goed als B.
3. Wijs af als A in een nieuwe uitvoering en bevestig dat de export niet plaatsvindt. Test daarna wat er gebeurt als er geen ontvanger kan worden bepaald.

**Afrondingscriterium:** U onderscheidt verantwoordelijkheid, taak, melding en werkelijke goedkeuring; A → goedkeuring → B → goedkeuring is in die volgorde gebeurd; een afwijzing van A heeft de export verhinderd; en een ontbrekende ontvanger gold niet als afgeronde goedkeuring.

**Verdieping:** [P1: De beslissingstabel tot en met de toewijzing volgen](masterclass/decision-table-routing.md) · [P1: Toewijzing, taak en sequentiële goedkeuring onderscheiden](masterclass/assignment-task-sequential.md)

## 5. Advanced-besturing en onderliggende workflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/nl.html).

**Doel:** Parallelle paden correct samenbrengen en werk aan een andere workflow overdragen.

1. Vergelijk ALL, ANY en OR op twee controles die werkelijk worden bereikt: ALL heeft een passende uitgang van elke bron nodig, ANY en OR hebben er één nodig, en groen plus oranje uit één bron tellen nog steeds als één bron.
2. Bekijk een tak die de uitvoering niet nam, zoals in geval MERGE-04: Advanced Test evalueert de wachtende samenvoeging nog, terwijl de normale uitvoering die overslaat zodra een voorganger nooit aankomt.
3. Voer de zeven gevallen van de v2-casus uit (erboven, eronder, grens, net erboven, ontbrekend, ongeldig getal, andere factuur). Roep daarna met Run Workflow een eigen inactieve workflow aan en open het pad in het doel zelf.

**Afrondingscriterium:** U legt het verschil uit geval MERGE-04 tussen test en uitvoering uit stap 2 uit, hoe bronnen worden geteld en waar een fout naartoe gaat. Een groene Run Workflow-aanroep vraagt nog steeds om een controle in het doel. V2 betekent hier de tweede versie van de casusgraaf: de statuskaart van elk pad leidt direct naar de gezamenlijke afrondingskaart, zonder wachtend OR-knooppunt.

**Verdieping:** [P0: Wait ALL, Wait ANY en OR correct verbinden](masterclass/control-nodes.md) · [P0: Run Workflow, doelvoorwaarden en fouten begrijpen](masterclass/run-workflow.md) · [Advanced-bedrijfscasus: factuurroutering](advanced-workflow-case-study.md)

## 6. Berekening, integratie en export <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/nl.html).

**Doel:** Waarden berekenen, een resultaat uit een extern systeem terughalen en pas na een echte goedkeuring exporteren.

1. Bereken een kolom en vergelijk de hele tabel voor en na, inclusief een rij waarin de reguliere expressie niet past en een deling door nul.
2. Schrijf het terugschrijfcontract met het externe systeem op: welk documentveld neemt het resultaat op, welke kaart of extensie schrijft het daar en hoe controleert u de opgeslagen waarde daarna. HTTP 200 alleen is geen resultaat.
3. Plan de export na goedkeuring met uw eigen exportconfiguratie en noteer wat u bij de ontvanger gaat controleren.

**Afrondingscriterium:** Vervolgwaarden in het veld, ontvangst bij de ontvanger en verwerking in het ERP hebben elk hun eigen bewijs. Een simulatie of een in de rij gezette export is geen aflevering.

**Verdieping:** [P1: Tabellen berekenen en regex-afhankelijkheid controleren](masterclass/table-calculations.md) · [P1: API-aanroep en hergebruik van het antwoord controleren](masterclass/api-response-contract.md) · [P1: Exportvarianten, open taken en afrondingsstatus](masterclass/export-lifecycle.md)

## 7. Wijzigingen en deskundig beheer <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/nl.mp4" %}

[Video openen met Nederlandse ondertitels en transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/nl.html).

**Doel:** Een workflow wijzigen die u niet hebt gebouwd en de wijziging weer kunnen terugdraaien.

1. Exporteer de workflow en noteer de kaartversies voordat u iets aanraakt.
2. Herhaal na de wijziging de positieve, negatieve, fout- en grensgevallen en daarnaast een tweede uitvoering van hetzelfde geval.
3. Leid de eerste fout terug naar één invoer en één configuratie en houd de bewaarde export als weg terug.

**Afrondingscriterium:** U kunt de wijziging accepteren, de bewaarde configuratie herstellen en een nieuwe documentuitvoering met bewijs vergelijken. Noteer oorzaak, correctie en de grenzen die blijven.

**Verdieping:** [Workflowfouten systematisch diagnosticeren](workflow-troubleshooting.md) · [Kaarten begrijpen en betrouwbaar configureren](card-reference-standard.md)

## Toets uw kennis

| Vraag | Antwoord |
| --- | --- |
| Is `false` bij Field is v2 leeg? | Ja. Het getal 0 en de tekst "false" zijn niet leeg. |
| Garandeert een groene OR-test de documentuitvoering? | Nee. In het gecontroleerde geval MERGE-04 evalueert een test de samenvoeging die een documentuitvoering overslaat wanneer een voorganger nooit aankomt. |
| Kan Run Workflow een inactief doel aanroepen? | Ja, bij de gecontroleerde expliciete aanroep. Controleer toch de doelvoorwaarden en het resultaat. |
| Maakt HTTP 200 automatisch api.response.cost\_center beschikbaar? | Nee. De gecontroleerde acties bieden dat automatische JSON-uitvoercontract niet. |
| Bewijst een groene test de ontvangst van de export? | Nee. Documentuitvoering, ontvangst bij de ontvanger en ERP-verwerking vragen apart bewijs. |

## Vastleggen wat u hebt geaccepteerd

Download `workflow-training-kit-v2.zip` uit het [workflow-oefenpakket](workflow-training-kit.md), pak het uit en open `acceptance-record-template.json`. Dat is een leeg verslag en niets dat u importeert; dezelfde ZIP bevat ook de gegevens, de verwachtingen en de bewaarde testantwoorden waar de niveaus naar verwijzen.

Noteer wat u hebt getest en waaraan u dat ziet: het scenario, de configuratie (hash van de workflow-export, kaartversies), uw verwachting, uw waarneming en welk soort bewijs u hebt. Houd een test in Advanced Test, een geïsoleerde broncontrole, een echte documentuitvoering, ontvangst bij de ontvanger en ERP-verwerking uit elkaar, en laat stappen die u niet hebt getest open staan.
