# Lookup table

## Tabel `public.lookup_table`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `data_key`: intern
* `rec_id`: intern
* `prop_name`: intern
* `prop_value`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `prop_value_clean`: intern
* `version`: integer
* `deleted_on`: timestamp with time zone
* `sub_org_id`: intern

### Analyse & beschrijving

## Technische documentatie voor `public.lookup_table`

### Inleiding

De tabel `public.lookup_table` is bedoeld om metagegevens op te slaan over diverse eigenschappen die bij organisatiegegevens horen. Ze fungeert waarschijnlijk als key-valueopslag voor verschillende attributen van klanten of andere entiteiten binnen de organisatie. De tabel legt informatie vast zoals eigenschapsnamen, waarden en de context (bijv. de organisatie en suborganisatie waartoe ze behoren), samen met auditinformatie zoals tijdstempels van aanmaak en wijziging.

### Kolombeschrijvingen

#### `id`

* **Betekenis**: Unieke identifier voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die elke vermelding uniek identificeert.

#### `org_id`

* **Betekenis**: Identifier van de organisatie waartoe de gegevens behoren.
* **Rol**: Refererende sleutel, die waarschijnlijk naar een organisatietabel verwijst.
* **Typische inhoud**: Een UUID-tekenreeks die de organisatie vertegenwoordigt.

#### `data_key`

* **Betekenis**: Een sleutel die een specifieke dataset of context binnen de organisatie vertegenwoordigt.
* **Rol**: Contextuele identifier voor het groeperen van gerelateerde eigenschappen.
* **Typische inhoud**: Alfanumerieke tekenreeks die een categorie aangeeft, zoals `customer_amier`.

#### `rec_id`

* **Betekenis**: Identifier voor een specifiek record binnen de dataset.
* **Rol**: Contextuele identifier, mogelijk een refererende sleutel naar een andere tabel.
* **Typische inhoud**: Alfanumerieke tekenreeks, of null voor records zonder specifieke identifier.

#### `prop_name`

* **Betekenis**: Naam van de eigenschap of het attribuut.
* **Rol**: Beschrijvend veld dat aangeeft wat de eigenschapswaarde vertegenwoordigt.
* **Typische inhoud**: Tekenreeksen zoals 'Kundennummer', 'Versandanschrift', 'Kundenname', enz.

#### `prop_value`

* **Betekenis**: Waarde van de eigenschap die door `prop_name` wordt beschreven.
* **Rol**: Beschrijvend veld met de daadwerkelijke gegevens of waarde.
* **Typische inhoud**: Tekenreeksen of getallen die de waarde van de eigenschap vertegenwoordigen.

#### `created_by`

* **Betekenis**: Identifier van de gebruiker of het systeem dat het record heeft aangemaakt.
* **Rol**: Technisch veld voor auditdoeleinden.
* **Typische inhoud**: Geheel getal dat een gebruikers-ID vertegenwoordigt.

#### `created_on`

* **Betekenis**: Tijdstempel dat aangeeft wanneer het record is aangemaakt.
* **Rol**: Technisch veld voor auditdoeleinden.
* **Typische inhoud**: Datum en tijd met tijdzone-informatie.

#### `last_modified_on`

* **Betekenis**: Tijdstempel dat aangeeft wanneer het record voor het laatst is gewijzigd.
* **Rol**: Technisch veld voor auditdoeleinden.
* **Typische inhoud**: Datum en tijd met tijdzone-informatie, mogelijk null als niet gewijzigd.

#### `is_deleted`

* **Betekenis**: Vlag die aangeeft of het record is verwijderd.
* **Rol**: Technisch veld dat logische verwijdering aangeeft.
* **Typische inhoud**: Booleaanse waarde (`True` of `False`).

#### `prop_value_clean`

* **Betekenis**: Opgeschoonde of verwerkte versie van `prop_value`.
* **Rol**: Beschrijvend veld voor het opslaan van een genormaliseerde of gestandaardiseerde waarde.
* **Typische inhoud**: Vergelijkbaar met `prop_value`, mogelijk null als niet van toepassing.

#### `version`

* **Betekenis**: Versienummer van het record.
* **Rol**: Technisch veld voor versiebeheer.
* **Typische inhoud**: Geheel getal dat de versie van het record vertegenwoordigt.

#### `deleted_on`

* **Betekenis**: Tijdstempel dat aangeeft wanneer het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld voor auditdoeleinden.
* **Typische inhoud**: Datum en tijd met tijdzone-informatie, mogelijk null als niet verwijderd.

#### `sub_org_id`

* **Betekenis**: Identifier voor een suborganisatie binnen de hoofdorganisatie.
* **Rol**: Refererende sleutel, die mogelijk naar een suborganisatietabel verwijst.
* **Typische inhoud**: Een UUID-tekenreeks die de suborganisatie vertegenwoordigt, mogelijk null als niet van toepassing.
