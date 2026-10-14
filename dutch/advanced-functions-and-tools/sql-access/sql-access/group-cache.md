# Group cache

## Tabel `public.group_cache`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `name`: intern
* `description`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `only_assigned_documents`: boolean

### Analyse & Beschrijving

## Technische Documentatie voor de Tabel `public.group_cache`

### Inleiding

De tabel `public.group_cache` beheert gecachte informatie met betrekking tot organisatorische groepen. Op basis van de kolomnamen en voorbeeldgegevens slaat het waarschijnlijk metadata op over diverse groepen, inclusief identificatoren, beschrijvende informatie, aanmaakdetails en statusvlaggen. Deze tabel vergemakkelijkt het efficiënt ophalen van groepsgerelateerde gegevens, mogelijk voor toegangscontrole, categorisering of rapportagedoeleinden binnen een organisatie.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elk groepsitem in de cache.
* **Rol**: Primaire Sleutel (Primary Key)
* **Typische Inhoud**: UUID-reeksen die een groepsitem uniek identificeren.
* **Opmerking**: Essentieel om elke rij in de tabel te onderscheiden.

#### org\_id

* **Betekenis**: Identificatie voor de organisatie waartoe de groep behoort.
* **Rol**: Vreemde Sleutel (Foreign Key)
* **Typische Inhoud**: UUID-reeksen die de groep relateren aan een specifieke organisatie.
* **Opmerking**: Koppel deze tabel aan de primaire organisatiegegevens, zodat groepen aan de juiste entiteit worden gekoppeld.

#### name

* **Betekenis**: De naam van de groep.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Korte reeksen of acroniemen die de groepsnaam vertegenwoordigen.
* **Opmerking**: Gebruikt voor weergavedoeleinden en kan worden gebruikt in zoekfuncties.

#### description

* **Betekenis**: Een gedetailleerdere beschrijving van de groep.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Tekst die extra context of informatie over de groep biedt.
* **Opmerking**: Helpt gebruikers het doel of de aard van de groep te begrijpen.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het groepsitem heeft aangemaakt.
* **Rol**: Vreemde Sleutel (Foreign Key)
* **Typische Inhoud**: Integerwaarden die verwijzen naar gebruikersidentificatoren.
* **Opmerking**: Nuttig voor auditing en het bijhouden van wijzigingen, geeft aan welke gebruiker de groep heeft toegevoegd.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het groepsitem is aangemaakt.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Tijdstempels met tijdzone-informatie, die de aanmaakdatum en -tijd aangeven.
* **Opmerking**: Belangrijk voor historische tracking en het begrijpen van de versheid van de gegevens.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging aan het groepsitem.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Tijdstempels met tijdzone-informatie, of `None` indien niet gewijzigd.
* **Opmerking**: Houdt bij wanneer de gegevens voor het laatst zijn bijgewerkt, wat helpt bij het handhaven van de gegevensintegriteit.

#### is\_deleted

* **Betekenis**: Vlag die aangeeft of het groepsitem als verwijderd is gemarkeerd.
* **Rol**: Statusveld.
* **Typische Inhoud**: Boolean waarden (`True` of `False`).
* **Opmerking**: Maakt soft-deletion van gegevens mogelijk, waarbij items in de database blijven maar als inactief worden gemarkeerd.

#### only\_assigned\_documents

* **Betekenis**: Vlag die aangeeft of de groep beperkt is tot alleen toegewezen documenten.
* **Rol**: Statusveld.
* **Typische Inhoud**: Boolean waarden (`True` of `False`).
* **Opmerking**: Bepaalt toegangs- of zichtbaarheidsbeperkingen op groepsgerelateerde documenten, mogelijk gebruikt voor beveiliging of handhaving van organisatorisch beleid.

Deze documentatie biedt een uitgebreid overzicht van de tabel `public.group_cache`, met gedetailleerd inzicht in de functie van elke kolom en de rol ervan in het databaseschema.
