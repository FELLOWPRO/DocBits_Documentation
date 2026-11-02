# Document voor aangepaste classificatie

## Tabel `public.custom_classification_document`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

### Analyse & beschrijving

## Technische documentatie voor de tabel `public.custom_classification_document`

### Inleiding

De tabel `public.custom_classification_document` is bedoeld om gedetailleerde informatie over documentclassificaties binnen een organisatie op te slaan. Dit omvat metagegevens over het document, zoals de inhoud, details over aanmaak en de organisatorische context. De structuur van de tabel wijst op gebruik bij het beheren van documenten die bij organisatieprocessen horen, mogelijk facturen of bestelformulieren, zoals af te leiden is uit de voorbeeldgegevens.

### Kolombeschrijvingen

#### id

* **Betekenis**: Deze kolom bevat waarschijnlijk een unieke identifier voor elke documentvermelding.
* **Rol**: Primaire sleutel
* **Typische inhoud**: Een UUID die een unieke documentidentifier vertegenwoordigt.

#### org\_id

* **Betekenis**: Deze kolom bevat de identifier van de organisatie die bij het document hoort.
* **Rol**: Refererende sleutel
* **Typische inhoud**: Een UUID die het document aan een specifieke organisatie koppelt.

#### first\_page\_content

* **Betekenis**: Deze kolom bevat de tekstinhoud van de eerste pagina van het document.
* **Rol**: Gegevensveld
* **Typische inhoud**: Tekstuele weergave van een document van een organisatie, mogelijk inclusief kopteksten, adressen en eerste details van een factuur of bestelling.

#### content

* **Betekenis**: Deze kolom bevat de volledige tekstinhoud van het document.
* **Rol**: Gegevensveld
* **Typische inhoud**: Volledige tekstinhoud van het document, inclusief alle details van de eerste pagina en van de volgende pagina's.

#### created\_by

* **Betekenis**: Deze kolom geeft de gebruiker aan die de documentvermelding heeft aangemaakt.
* **Rol**: Gegevensveld
* **Typische inhoud**: Een geheel getal dat het gebruikers-ID van de maker vertegenwoordigt.

#### created\_on

* **Betekenis**: Deze kolom registreert de datum en tijd waarop de documentvermelding is aangemaakt.
* **Rol**: Technisch veld
* **Typische inhoud**: Een timestamp with time zone die de datum en tijd van aanmaak aangeeft.

#### last\_modified\_on

* **Betekenis**: Deze kolom bevat de datum en tijd van de laatste wijziging van de documentvermelding.
* **Rol**: Technisch veld
* **Typische inhoud**: Een timestamp with time zone die de datum en tijd van de laatste wijziging aangeeft. Soms `None` als er na het aanmaken geen wijzigingen hebben plaatsgevonden.

#### is\_deleted

* **Betekenis**: Deze kolom geeft aan of de documentvermelding als verwijderd is gemarkeerd.
* **Rol**: Technisch veld
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`) die de verwijderstatus van de documentvermelding toont.

Deze tabel biedt een robuuste structuur voor het beheren van documentgegevens, waarbij elk document uniek kan worden geïdentificeerd, aan een organisatie kan worden gekoppeld en gedurende de levenscyclus van aanmaak en wijziging kan worden gevolgd.
