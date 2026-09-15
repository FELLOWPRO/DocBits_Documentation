# Best practices

## Behoud de standaardkolommen voor bedragen en hoeveelheden

De controles op regelniveau (*hoeveelheid × eenheidsprijs = regeltotaal*) en PO-matching zoeken naar de standaardkolommen `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Als u voor deze waarden in plaats daarvan eigen kolommen aanmaakt, draaien de controles niet en meldt PO-matching ontbrekende verplichte kolommen. Hernoem de *titel* als de formulering u niet bevalt; behoud de kolom.

## Verbergen, niet verwijderen

Standaardkolommen die u niet nodig hebt, worden verborgen, niet verwijderd; ze kunnen sowieso niet worden verwijderd. Ook voor uw eigen kolommen is verbergen de veiligere keuze zolang u niet zeker weet of een script of een exportmapping nog naar de kolom verwijst.

## Markeer alleen als verplicht wat de export blokkeert

Elke verplichte kolom moet in elke rij gevuld zijn voordat een gebruiker het document kan goedkeuren. Gebruik dit voor waarden die het ERP afwijst als ze ontbreken (bijvoorbeeld de kostenplaats in een boekhoudexport), niet voor waarden die alleen maar handig zijn.

## Gebruik *Alleen-lezen* voor opgezochte waarden

Waarden die een script of een stamgegevens-lookup in de tabel schrijft (artikelomschrijving uit het artikelbestand, belastingcode van de leverancier) moeten alleen-lezen zijn, zodat gebruikers de bron corrigeren in plaats van de kopie.

## Gebruik AI per kolom, niet per leverancier

Voor een leverancier met getrainde regels komen de meeste kolommen goed uit de regels. Als één kolom onbetrouwbaar is (lange omschrijvingen die afbreken, een korting die soms op een andere plek staat), schakel dan alleen voor die kolom *AI gebruiken* in. De regels blijven de rest vullen.

## Benoem kolommen voor het ERP, niet voor het document

De *Kolomnaam* komt terecht in exportmappings en scripts. `COST_CENTRE` is gemakkelijker te mappen dan `KST` en verandert niet wanneer een leverancier het anders afdrukt.

## Test op een opnieuw gestart document

Start na een wijziging één bestaand document van het documenttype opnieuw en open het: de nieuwe kolom verschijnt, de verborgen kolom is weg, verplichte cellen zijn gemarkeerd. Rol de wijziging pas daarna uit naar gebruikers.

## Eén tabel per regelitemstructuur

Maak alleen een tweede tabel aan wanneer een documenttype echt twee onafhankelijke tabellen heeft (bijvoorbeeld artikelregels en een aparte kostentabel). Extra lege tabellen verschijnen op elk document van het type.
