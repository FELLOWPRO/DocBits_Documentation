# Metrieken en berekening

<!-- touchless-admin-video-v2-20261104:start -->
**Videohoofdstuk (controleversie):** [De percentages berekenen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=03).
<!-- touchless-admin-video-v2-20261104:end -->

### Correct uitlezen en een touchless proces zijn twee verschillende dingen

**DocBits kan elke factuurwaarde correct uitlezen en toch kan de factuur AP-aandacht nodig hebben, omdat de gegevens uit het bronsysteem afwijken.** AP staat voor Accounts Payable, het team dat leveranciersfacturen verwerkt. Controleer deze twee vragen afzonderlijk:

| Vraag | Vergelijk met | Wat het resultaat je vertelt |
| --- | --- | --- |
| **Heeft DocBits het document correct uitgelezen?** | De originele factuur tegen de uitgelezen kopvelden en tabelregels, vóór elke handmatige correctie | Extractiekwaliteit: komt de uitgelezen waarde overeen met wat er werkelijk op de factuur staat? |
| **Kon het proces zonder ingreep worden afgerond?** | De correct uitgelezen factuur tegen de inkooporder en de stamgegevens uit Infor ERP, samen met de vastgelegde verwerkingsgeschiedenis | Procesautomatisering: konden de geconfigureerde controles, de matching en de export zonder correctie of herstart worden afgerond? |

Een afwijkende waarde in Infor zegt op zichzelf niet welke kant ongelijk heeft. Controleer de factuur, de afgesproken order en de gegevens die werkelijk in DocBits zijn geïmporteerd. De bron kan onjuist zijn, de import kan verouderd zijn, of de leverancier kan een andere waarde hebben gefactureerd.

{% hint style="info" %}
**Het touchless-percentage meet het proces, niet de extractienauwkeurigheid.** Een AP-assisted document bewijst geen fout in de extractie van DocBits. Omgekeerd bewijst een geslaagde extractiestap of een hoge betrouwbaarheidsscore niet dat elke waarde correct is. Vergelijk daarvoor het originele document met de uitgelezen waarden.
{% endhint %}

Elk document eindigt in precies **één** uitkomst:

| Uitkomst              | Betekenis                                                                                           | Telt mee in het percentage                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Pure touchless**    | Van import tot export verwerkt **zonder enige menselijke betrokkenheid**                            | Ja, als succes                                                                             |
| **AP touchless**      | Liep automatisch en een persoon gaf alleen de **inhoudelijke goedkeuring**. Er was geen correctie nodig | Ja, als succes                                                                             |
| **AP assisted**       | Succesvol afgerond, maar een persoon moest **een veld corrigeren, het document herstarten** of op een andere manier ingrijpen; dat kan ook nodig zijn wanneer de extractie correct was | Ja, buiten de touchless-teller; het benoemt op zichzelf niet de oorzaak                    |
| **Process exception** | Eindigde in een **fout**, werd **afgewezen**, werd **door het ERP geweigerd** of **liep vast** in de pipeline | Ja, als gemist                                                                             |
| **In progress**       | Nog niet afgerond                                                                                   | **Nee**. Er is nog geen uitkomst                                                           |
| **Not eligible**      | Verwijderd, gearchiveerd, een testdocument of een uitgesloten documenttype                          | **Nee**                                                                                    |

Het **AP touchless-percentage**, inclusief documenten met alleen goedkeuring, is:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Hier is **AP touchless** in de teller de documentuitkomst "alleen goedkeuring". Het **AP touchless percentage** van het dashboard is het gecombineerde percentage: pure plus documenten met alleen goedkeuring. **Tel de twee getoonde percentages niet op.** Het pure percentage gebruikt alleen pure documenten in de teller, met dezelfde noemer.

Documenten die nog **in verwerking** zijn of **niet meetellen**, zitten nooit in de berekening. Dat beschermt het percentage: een document dat vijf minuten geleden binnenkwam, kan het niet naar beneden trekken.

{% hint style="info" %}
**Eén aanraking telt blijvend.** Zodra een persoon een document heeft aangeraakt, blijft het als aangeraakt meetellen, ook als een latere automatische run niemand nodig had. **Een document herstarten maakt het niet opnieuw touchless.** Het percentage weerspiegelt het werk dat is gebeurd.
{% endhint %}

### Rekenvoorbeeld (illustratieve getallen)

In 30 dagen kwamen 200 documenten binnen:

| Uitkomst                      | Documenten |
| ----------------------------- | ---------- |
| Pure touchless                | 120        |
| AP touchless                  | 30         |
| AP assisted                   | 30         |
| Process exception             | 10         |
| In progress                   | 8          |
| Not eligible (testdocumenten) | 2          |

* Noemer: 120 + 30 + 30 + 10 = **190**. De 8 documenten in verwerking en de 2 niet-meetellende documenten blijven buiten beschouwing.
* **Pure touchless**: 120 ÷ 190 = **63,2 %**
* Aandeel met **alleen goedkeuring**: 30 ÷ 190 = **15,8 %**. Dat is het aandeel van die uitkomst, niet het gecombineerde AP touchless-percentage.
* **AP touchless-percentage**: (120 + 30) ÷ 190 = **78,9 %**

Het tabblad toont een **doel** (70 % tenzij je organisatie een ander doel gebruikt). In dit voorbeeld ligt het gecombineerde AP-percentage boven 70%, terwijl het pure percentage van 63,2% eronder ligt. Vergelijk het doel met het percentage dat de betreffende kaart of grafiek aangeeft.

Klik rechtsboven op **How touchless is calculated** om deze uitleg binnen DocBits te openen, met de getallen van je eigen periode (documenten in periode, nog in verwerking, uitgesloten, gemeten).

<figure><img src="../../../.gitbook/assets/touchless-report-methodology-nl-20261104.png" alt="Huidige trainingspopulatie: 201 meetellende afgeronde facturen, waarvan geen enkele nog in verwerking is of uitgesloten. De 107 volledig automatische facturen geven 53,2%; met 11 facturen met alleen goedkeuring erbij zijn dat 118 en 58,7%. Deze procespercentages meten geen extractienauwkeurigheid."><figcaption><p>Huidige trainingspopulatie: 201 meetellende afgeronde facturen, waarvan geen enkele nog in verwerking is of uitgesloten. De 107 volledig automatische facturen geven 53,2%; met 11 facturen met alleen goedkeuring erbij zijn dat 118 en 58,7%. Deze procespercentages meten geen extractienauwkeurigheid.</p></figcaption></figure>

### Voorbeeld: 100% correcte extractie, 80% AP touchless

Stel dat een controle van de originele facturen en hun uitgelezen waarden bevestigt dat **alle 100 afgeronde, meetellende facturen correct zijn uitgelezen**. Hun verwerkingsuitkomsten zijn:

| Wat er gebeurde | Documenten | Uitkomst |
| --- | --- | --- |
| Factuur en brongegevens kwamen overeen; het hele proces is automatisch afgerond | 70 | Pure touchless |
| Factuur en brongegevens kwamen overeen; alleen inhoudelijke goedkeuring was nodig | 10 | AP touchless (uitkomst alleen goedkeuring) |
| De factuurgegevens waren correct uitgelezen, maar de geïmporteerde Infor-gegevens weken af. AP verduidelijkte het verschil en herstartte de documenten handmatig in DocBits nadat de brongegevens waren gecorrigeerd; daarna zijn ze succesvol afgerond | 20 | AP assisted |

* **Correct uitgelezen documenten in deze gecontroleerde steekproef:** 100 ÷ 100 = **100%**.
* **Pure touchless-percentage:** 70 ÷ 100 = **70%**.
* **AP touchless-percentage:** (70 + 10) ÷ 100 = **80%**.

Dat is geen tegenspraak: de extractie was op alle facturen correct, terwijl bij 20 een ingreep in de verwerking nodig was door de brongegevens. Het **extractiecijfer van 100% is een illustratief resultaat van een aparte documentcontrole**, geen extra KPI die dit dashboard toont. Bereken het niet alleen uit de touchless-uitkomsten.

### Voorbeelden: wat moest AP werkelijk doen?

De volgende gevallen zijn illustratief en niet de afzonderlijke documenten achter de schermafbeeldingen. De succesvolle uitkomsten veronderstellen dat de verwerking is afgerond, inclusief ERP-bevestiging waar die vereist is.

| Geval | Originele factuur / DocBits-extractie / brongegevens | AP-actie en uitkomst | Waar te onderzoeken |
| --- | --- | --- | --- |
| **Extractiefout** | PO-nummer `45001234` / onjuist uitgelezen als `45001284` / de correcte order `45001234` bestaat in Infor | AP corrigeert het uitgelezen nummer; de factuur eindigt als **AP assisted** | Extractie voor deze leverancier |
| **Afwijking in het bronsysteem** | Eenheidsprijs €10.00 / correct uitgelezen €10.00 / de geïmporteerde Infor-order zegt €9.00, buiten de ingestelde tolerantie | AP bevestigt dat €10.00 de afgesproken prijs is, laat de order corrigeren en herstart de factuur handmatig in DocBits; die eindigt als **AP assisted** | Infor-ordergegevens en de import daarvan |
| **Vertraging in de import** | Het PO-nummer is correct op de factuur en in DocBits / de order bestaat in Infor maar heeft DocBits nog niet bereikt | Als een latere import en nieuwe poging automatisch afronden zonder vastgelegde menselijke ingreep of goedkeuring, kan de uitkomst **Pure touchless** blijven. Een handmatige herstart gevolgd door succes geeft **AP assisted** | Importtijdstip en de werkelijke uitvoeringsgeschiedenis |
| **ERP-afwijzing** | De extractie is correct, maar het ERP weigert het geëxporteerde document | **Process exception** zolang het als een definitieve ERP-afwijzing is ingedeeld, ook als iemand eerder heeft ingegrepen | ERP-afwijzing en bewijs van de export |

**Zelfs een kleine vastgelegde correctie of handmatige herstart telt als ingreep.** AP assisted betekent "een persoon heeft geholpen het document te verwerken"; het is niet de naam van een aparte AI-assistent. Een probleem in de brongegevens en een extractieprobleem kunnen dus dezelfde uitkomst hebben, maar vragen een andere oplossing.

De indeling gebruikt de gebeurtenissen die DocBits vastlegt. Ga er niet van uit dat werk dat alleen in Infor is gedaan, zonder bijbehorende vastgelegde DocBits-gebeurtenis, automatisch als AP-ingreep telt. Neem dat werk ook mee in de diagnose.

### Welke AP-acties tellen als ingreep?

Het volgende veronderstelt een succesvolle afronding, inclusief de vereiste ERP-bevestiging. De vastgelegde actie en wie die uitvoerde tellen, niet hoe lang het werk duurde.

| Actie | Gevolg voor de documentuitkomst |
| --- | --- |
| Openen, lezen, filteren, vergelijken of een voorbeeld bekijken | Vormt op zichzelf geen ingreep in de verwerking; Pure Touchless blijft mogelijk |
| Inhoudelijke goedkeuring geven, ook een tweede goedkeuring | AP Touchless, als er geen ingreep in de verwerking was |
| Een kopveld of tabelcel wijzigen en opslaan | AP Assisted; zelfs één opgeslagen correctie telt |
| Een document handmatig valideren en verder laten gaan, ook zonder een waarde te corrigeren | AP Assisted; handmatige validatie is iets anders dan alleen goedkeuring |
| De verwerking of de export handmatig opnieuw starten | AP Assisted; een latere automatische run maakt de ingreep niet ongedaan |
| Automatische nieuwe poging van het systeem of automatische workflow-schrijfactie | Vormt op zichzelf geen menselijke ingreep; eerdere menselijke aanrakingen blijven bestaan |
| Alleen gegevens in Infor corrigeren | Extern werk is niet automatisch een vastgelegde DocBits-gebeurtenis; leg het apart vast en controleer de daaropvolgende DocBits-actie |
| Definitieve ERP-afwijzing na een correctie | Process exception heeft voorrang; de ingreep blijft in de geschiedenis staan |

Een klik op Save zonder bewijs van een gewijzigde waarde bewijst geen correctie. Controleer of daarmee ook handmatige validatie of een herstart is gestart.

### Het AP-label heeft twee betekenissen

| Locatie | Betekenis |
| --- | --- |
| AP-koppercentage | Gecombineerd Pure + alleen goedkeuring: (120 + 30) / 190 = 78.9% |
| Documentaantal onder dat percentage in het huidige rapport | Gecombineerd Pure + alleen goedkeuring: 150 = 120 + 30 |
| Uitkomstcategorie AP Touchless, zoals de MCP-bucket `AP_TOUCHLESS` | Afzonderlijke categorie alleen goedkeuring: 30 / 190 = 15.8% |
| Blauwe AP-lijn in de huidige [screenshot van de dashboardtrend](touchless-dashboard.md) | Gecombineerd percentage Pure + alleen goedkeuring op elk punt, met de populatie van dat punt |

De definitieve uitkomstcategorieën tellen op tot 100% van de gemeten populatie. Het Pure- en het gecombineerde AP-koppercentage overlappen elkaar en mogen niet worden opgeteld.

### Hoe actueel zijn de cijfers

Uitkomsten worden **elke 15 minuten opnieuw berekend**. De uitkomst van een document kan nog veranderen nadat die voor het eerst verschijnt: het ERP kan een export uren later bevestigen. De regel **Data as of …** onderaan het tabblad toont wanneer de cijfers voor het laatst zijn berekend.





## Gerelateerde pagina's

* [Touchless Intelligence](./)
* [Het dashboard gebruiken](touchless-dashboard.md)
* [Uitgewerkte voorbeelden: prijs en aantal](touchless-examples.md)
* [Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [PO-matchingdiagnose](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals en rapporten](touchless-change-proposals.md)
* [Touchless uitleggen en verbeteren met MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
