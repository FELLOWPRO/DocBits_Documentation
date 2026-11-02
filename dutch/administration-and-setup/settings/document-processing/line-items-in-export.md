# Regelitems in de export

Wat er met de regelitemtabel gebeurt wanneer een document wordt goedgekeurd en geëxporteerd, hangt af van de exportmethode. Deze pagina legt uit welke kolommen DocBits verlaten, welke verplicht zijn en waarom een export minder regels kan tonen dan het validatiescherm.

## Twee soorten export

| Exportmethode | Wat er voor de tabel wordt verzonden |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | De tabel zoals die op het validatiescherm staat: elke niet-verborgen [tabelkolom](../global-settings/document-types/table-columns/README.md) van elke rij, met waarde, opgemaakte waarde en betrouwbaarheid. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (Infor ERP / SAP BODs) | Niet de ruwe tabel. DocBits bouwt hieruit **ontvangstregels** (receipt lines) en **kostenregels** (cost lines) (zie hieronder) en beeldt ze af op de BOD-velden met de mapping die is geconfigureerd onder [Exporteren naar Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Ontvangstregels en kostenregels (Infor-exports)

Een ERP-factuurregel is ofwel een **ontvangstregel** (receipt line), die een inkooporderontvangst afwikkelt, ofwel een **kostenregel** (cost line), die een bedrag op een grootboekrekening met dimensies boekt. DocBits beslist dit per factuurregel:

* **Ontvangstregels** komen uit de **PO-matching**. Elke factuurregel die aan een inkooporderregel is gematcht (Dashboard → PO Match, of automatisch met *PO auto match*) wordt een ontvangstregel met het inkoopordernummer, de inkooporderregel, de ontvangstregel en de gematchte hoeveelheid en het gematchte bedrag. Een factuur zonder PO-match heeft **geen ontvangstregels**; het exportvoorbeeld toont dan `receipt_lines: []`, wat correct is en geen bug.
* **Kostenregels** komen uit het **boekingsrecord** dat de kostenboekingsstap (of Auto Accounting) aanmaakt: grootboekrekening, dimensies, bedrag, hoeveelheid per regel. Een factuur zonder boekingsrecord heeft geen kostenregels.
* **Belastingregels** worden opgebouwd uit de belastingbedragen in de koptekst, niet uit de tabel.

Voor Infor-exports is de regelitemtabel dus de *invoer* voor PO-matching en boekhouding; wat het ERP ontvangt, is het resultaat van die twee stappen. Een regel die noch PO-gematcht noch geboekt is, bereikt het ERP niet.

{% hint style="warning" %}
Om PO-matching te laten werken, moet de tabel de standaardkolommen **artikelnummer, eenheidsprijs, hoeveelheid en totaalbedrag** hebben. Als een daarvan verborgen is, toont het validatiescherm *Line Item Table is missing Mandatory column for PO* en kunnen er geen ontvangstregels worden opgebouwd.
{% endhint %}

## Verplichte kolommen en het goedkeuringsdialoogvenster

Voordat een document kan worden goedgekeurd, controleert DocBits de tabel:

1. Elke kolom met de markering **Verplicht** (Instellingen → Documenttypen → Tabelkolommen) moet in elke rij een waarde hebben.
2. Elke rij moet de **regeltotaalcontrole** doorstaan: `totaal = hoeveelheid × eenheidsprijs + kosten − korting` binnen 0,02. Rijen die niet slagen, worden gemarkeerd; de melding noemt de verwachte en de werkelijke waarde.
3. De **som van de regeltotalen** wordt vergeleken met het nettobedrag in de koptekst. Een verschil is een waarschuwing en blokkeert de goedkeuring niet.

Het goedkeuringsdialoogvenster toont wat er nog ontbreekt. Een beheerder kan alle tabelcontroles per documenttype uitschakelen met **Tabelvalidatie overslaan** (Documenttypen → Meer instellingen); regeltotalen en verplichte kolommen worden dan niet meer gecontroleerd, de koptekstcontroles blijven.

Details van de meldingen: [Tabel Extractie Probleemoplossing](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#meldingen-op-de-tabel).

## Lege tabel

* **JSON / XML-exports** verzenden het document met `tables: []` (of de tabel met nul rijen). Het ontvangende systeem moet een lege tabel kunnen verwerken.
* **Infor-exports** zonder ontvangstregels en zonder kostenregels verzenden alleen de koptekst en de belastingregels. De meeste ERP's weigeren een factuur zonder regels; configureer Auto Accounting of een standaardkostenregel voor zulke documenttypen, of stuur ze naar een andere export.
* Een documenttype **zonder tabel** (geen tabel geconfigureerd) verzendt nooit regelgegevens; dat is normaal voor documenttypen zoals orderbevestigingen die op koptekstniveau worden gematcht.

## Controleren voordat u goedkeurt

Partners en support met API- of MCP-toegang kunnen de exportpayload voor een document opvragen voordat deze wordt verzonden: de MCP-tool `get_export_preview(doc_id)` geeft precies terug wat de export zal verzenden, `receipt_lines`, `cost_lines` en `tax_lines` voor Infor-exports, `tables` voor JSON-exports. Gebruik dit wanneer het ERP ontbrekende regels meldt: als `receipt_lines` leeg is, is de factuur niet PO-gematcht; als `cost_lines` leeg is, bestaat er geen boekingsrecord.

## Gerelateerde pagina's

* [Exporteren](export.md): exportconfiguraties en -methoden
* [Tabelkolommen](../global-settings/document-types/table-columns/README.md)
* [Exporteren naar Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md): BOD-veldmappings voor ontvangst-, kosten- en belastingregels
