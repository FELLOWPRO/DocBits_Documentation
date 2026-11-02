# Custom\_classification\_document\_label

## Tabel `public.custom_classification_document_label`

### Kolommen

* `id`: integer
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `label_id`: integer
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

### Analyse & Beschrijving

## Technische Documentatie voor de Tabel `public.custom_classification_document_label`

### Inleiding

De tabel `public.custom_classification_document_label` is ontworpen om associaties tussen documenten en hun respectievelijke labels binnen een organisatie te beheren en op te slaan. Deze tabel vergemakkelijkt het categoriseren en ophalen van documenten op basis van aangepaste labels, en biedt een gestructureerde manier om documentclassificatie te beheren voor diverse organisatorische behoeften.

### Kolombeschrijvingen

#### id

* **Betekenis**: Deze kolom dient als de unieke identificatie voor elk record in de tabel.
* **Rol**: Primaire Sleutel (Primary Key)
* **Typische Inhoud**: Een integerwaarde die elke rij uniek identificeert.
* **Opmerking**: Elk item in de tabel heeft een unieke `id` om de gegevensintegriteit te waarborgen en efficiënte verwijzingen te ondersteunen.

#### org\_id

* **Betekenis**: Vertegenwoordigt de organisatie waartoe de document-label associatie behoort.
* **Rol**: Vreemde Sleutel (Foreign Key)
* **Typische Inhoud**: Een karakterreeks, waarschijnlijk een UUID, die een organisatie uniek identificeert.
* **Opmerking**: Zorgt ervoor dat de associatie van documenten en labels beperkt blijft tot de juiste organisatorische context.

#### doc\_id

* **Betekenis**: Identificeert het document dat wordt gelabeld.
* **Rol**: Vreemde Sleutel (Foreign Key)
* **Typische Inhoud**: Een karakterreeks, waarschijnlijk een UUID, die een document uniek identificeert.
* **Opmerking**: Maakt de koppeling van specifieke documenten aan labels mogelijk, wat documentcategorisatie faciliteert.

#### label\_id

* **Betekenis**: Verwijst naar het label dat op het document is toegepast.
* **Rol**: Vreemde Sleutel (Foreign Key)
* **Typische Inhoud**: Een integer die verwijst naar een label uit een afzonderlijke labelstabel.
* **Opmerking**: Faciliteert de associatie tussen documenten en hun respectievelijke labels.

#### created\_by

* **Betekenis**: Identificeert de gebruiker die het record heeft aangemaakt.
* **Rol**: Vreemde Sleutel (mogelijk naar een gebruikerstabel)
* **Typische Inhoud**: Een integer die de gebruikers-ID vertegenwoordigt.
* **Opmerking**: Houdt de oorsprong van elke document-label associatie bij voor auditing en verantwoording.

#### created\_on

* **Betekenis**: Geeft aan wanneer het record is aangemaakt.
* **Rol**: Technisch Veld
* **Typische Inhoud**: Een tijdstempel met tijdzone-informatie.
* **Opmerking**: Biedt een temporele context voor wanneer de document-label relatie tot stand is gekomen.

#### last\_modified\_on

* **Betekenis**: Registreert de tijdstempel van de laatste wijziging van het record.
* **Rol**: Technisch Veld
* **Typische Inhoud**: Een tijdstempel met tijdzone-informatie, kan `None` zijn indien nooit gewijzigd.
* **Opmerking**: Nuttig voor het bijhouden van de geschiedenis van wijzigingen aan de document-label associaties.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch Veld
* **Typische Inhoud**: Een boolean waarde (`True` of `False`).
* **Opmerking**: Ondersteunt soft-deletion praktijken, waardoor logische verwijdering van gegevens mogelijk is zonder fysieke verwijdering uit de database.
