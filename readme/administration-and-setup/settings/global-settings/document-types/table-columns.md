# Tabelkolommen

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_overview.png" alt="Docbits Table Columns Overview"><figcaption></figcaption></figure>

#### Overzicht

De interface voor tabelkolommen in Docbits wordt gebruikt om de kolommen te specificeren die in de gegevenstabellen voor elk documenttype verschijnen. Elke kolom kan worden geconfigureerd om specifieke gegevenstypen te bevatten, zoals tekenreeksen of numerieke waarden, en kan essentieel zijn voor de functies voor sorteren, filteren en rapporteren binnen Docbits.

#### Belangrijkste functies en opties

1. **Kolomconfiguratie**:
* **Kolomnaam**: De identificatie van de kolom in de database.
* **Titel**: De voor mensen leesbare titel van de kolom die in de interface verschijnt.
* **Kolomtype**: Definieert het gegevenstype van de kolom (bijvoorbeeld STRING, AMOUNT), wat bepaalt welk soort gegevens in de kolom kan worden opgeslagen.
* **Tabelnaam**: Geeft aan tot welke tabel de kolom behoort, waardoor deze wordt gekoppeld aan een specifiek documenttype zoals INVOICE\_TABLE.
2. **Acties**:
* **Bewerken**: Wijzig de configuratie van een bestaande kolom.
* **Verwijderen**: Verwijder de kolom uit de tabel, wat nuttig is als de gegevens niet langer nodig zijn of als de gegevensstructuur van het documenttype verandert.
3. **Nieuwe kolommen en tabellen toevoegen**:
* **Nieuwe tabelkolom toevoegen**: Opent een dialoogvenster waar je een nieuwe kolom kunt definiëren, inclusief de naam, of deze vereist is, het gegevenstype en de tabel waartoe deze behoort.
* **Nieuwe tabel aanmaken**: Maakt de creatie van een nieuwe tabel mogelijk, waarbij een unieke naam wordt gedefinieerd die wordt gebruikt om gegevens op te slaan die verband houden met een specifieke set documenttypen.

<figure><img src="../../../../.gitbook/assets/docbits_create_new_table.png" alt="Docbits Create New Table"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_integrity.png" alt="Docbits Table Columns Integrity"><figcaption></figcaption></figure>

Deze sectie is essentieel voor het behoud van de structurele integriteit en de bruikbaarheid van de gegevens binnen het Docbits-systeem, waardoor wordt gegarandeerd dat de uit documenten geëxtraheerde gegevens op een georganiseerde en toegankelijke manier worden opgeslagen.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
