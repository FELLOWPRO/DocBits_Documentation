# Probleemoplossing

## De nieuwe kolom verschijnt niet op het validatiescherm

* Het document is verwerkt voordat de kolom werd toegevoegd. Wijzigingen gelden voor documenten die daarna worden geüpload of opnieuw gestart: **start het document opnieuw** (Dashboard → documentmenu → Opnieuw starten).
* De kolom is **Verborgen**. Controleer de vlag in de lijst met tabelkolommen.
* De kolom is toegevoegd aan een **andere tabel** dan de getoonde. Het validatiescherm toont de tabellen van het documenttype; vergelijk de kolom *Tabelnaam*.
* Het document heeft niet het documenttype dat u hebt geconfigureerd.

## De kolom is er, maar altijd leeg

* De leverancier heeft **getrainde regels** en de nieuwe kolom is daarin niet gekoppeld. Open een van de documenten van de leverancier in de tabeltraining en koppel de kolom, of schakel *AI gebruiken* voor de kolom in.
* Bij AI-extractie is de waarde op het document niet herkenbaar (geen kolomkop, afgekort, in een andere taal). Voeg een [AI-tabeltag](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) toe die de kolom benoemt, of koppel de kolom in de training.

## "Column name already exists"

Een kolom met dezelfde technische naam staat al in de tabel. Als die niet in de lijst staat, is het een verborgen standaardkolom: de melding zegt dan *Please activate it in Table Column settings*. Schakel *Verborgen* voor die kolom uit in plaats van een nieuwe kolom aan te maken.

## Goedkeuring wordt geblokkeerd door een verplichte kolom

De melding op de tabel noemt de kolom. Vul de cel in elke rij, of (als de waarde op dit document niet bestaat) schakel *Verplicht* voor de kolom uit, start het document opnieuw en probeer het nogmaals. Overweeg of de kolom überhaupt verplicht moet zijn (zie [Best practices](best-practices-2.md)).

## De AI vult een kolom met de verkeerde waarde

Typisch geval: `CHARGES` krijgt het regeltotaal, waardoor elke rij de regeltotaalcontrole niet haalt met *Line total does not match quantity x unit price (expected …, got …)*, omdat kosten deel uitmaken van de formule `hoeveelheid × eenheidsprijs + kosten`.

* Schakel *AI gebruiken* voor de kolom uit als de getrainde regels de kolom correct vastleggen.
* Als de leverancier geen regels heeft, train de tabel dan eenmalig (Tabeltraining) zodat de kolom aan de juiste positie is gebonden, of verberg de kolom als de leverancier die waarde nooit afdrukt.
* Als laatste redmiddel schakelt *Tabelvalidatie overslaan* in de Meer instellingen van het documenttype alle tabelcontroles voor het hele documenttype uit; de afwijking wordt dan niet meer gesignaleerd, en lege verplichte kolommen ook niet.

## PO-matching: "Line Item Table is missing Mandatory column"

PO-matching heeft de standaardkolommen artikelnummer, eenheidsprijs, hoeveelheid en totaalbedrag nodig. Een daarvan is verborgen of vervangen door een eigen kolom. Maak de standaardkolom weer zichtbaar, of koppel de waarde eraan in de tabeltraining.

## Een script of export mislukt na het verwijderen van een kolom

Het script of de exportmapping verwijst nog naar de verwijderde *Kolomnaam*. Verwijder de verwijzing, of voeg de kolom opnieuw toe met dezelfde titel; de technische naam wordt van de titel afgeleid en klopt dan weer.

## Waar verder te kijken

* [Tabel Extractie Probleemoplossing](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): extractiekwaliteit, OCR, E-Text
* [Training Line Fields / Tabeltraining](../../../../setup/document-training/training-line-fields-table-training/README.md)
