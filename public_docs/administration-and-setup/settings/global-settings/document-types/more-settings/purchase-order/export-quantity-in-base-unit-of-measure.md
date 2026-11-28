# Exporthoeveelheid in basiseenheid

De schakelaar **Export quantity in base unit of measure** staat in het gedeelte **Purchase Order** van de **More Settings** van een documenttype. Hij wijzigt de hoeveelheid en de eenheidsprijs die de Infor LN-export voor gematchte inkooporderregels wegschrijft.

U opent hem onder **Settings → Document Types**, selecteert het tandwielpictogram (**More Settings**) op de kaart van het documenttype en klapt **Purchase Order** open.

## Wat de schakelaar doet

* **Off:** DocBits exporteert de hoeveelheid en de eenheidsprijs in de eenheid van de factuur.
* **On:** DocBits rekent de hoeveelheid en de eenheidsprijs van elke gematchte inkooporderregel met de conversiefactor ervan om naar de basiseenheid van die inkooporderregel en schrijft de code van de basiseenheid in plaats van de code van de gefactureerde eenheid.

Een regel zonder conversiefactor wordt ongewijzigd geëxporteerd; een ontbrekende factor blokkeert de export dus niet.

{% hint style="info" %}
De omrekening geldt alleen voor de Infor LN-export. Andere exportdoelen behouden de gefactureerde eenheid.
{% endhint %}

## Wanneer u hem gebruikt

Zet de schakelaar aan wanneer de Infor LN-instantie orderhoeveelheden in de basiseenheid verwacht. De omrekening gebruikt de factor die op de inkooporderregel is opgeslagen, niet een factor die DocBits uit de artikelstam berekent.

Instellingen kunnen live documenten beïnvloeden. Controleer het resultaat met een testdocument voordat u de wijziging in productie opslaat. De schakelaar wijzigt de geëxporteerde waarden; hij wijzigt niet hoe factuur- en inkooporderregels worden gematcht.

## Gerelateerde pagina's

* [Inkooporder](README.md)
* [Export niet gematchte PO-regels](export-not-matched-po-lines.md)
* [Alternatieve export](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
