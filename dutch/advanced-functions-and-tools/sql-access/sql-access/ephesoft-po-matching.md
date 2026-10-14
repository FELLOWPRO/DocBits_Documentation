# Ephesoft PO matching

## Tabel `public.ephesoft_po_matching`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `doc_type`: DOC-type
* `ephesoft_doc_id`: intern
* `extracted_data`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

### Analyse & Beschrijving

## Technische Documentatie voor de Tabel `public.ephesoft_po_matching`

### Inleiding

De tabel `public.ephesoft_po_matching` is ontworpen voor het opslaan en beheren van gegevens met betrekking tot het matchen van inkooporders (purchase orders) met documenten, zoals facturen, die door het Ephesoft-systeem worden verwerkt. Deze tabel legt diverse details vast over de documenten, hun extractieproces en de matchstatus met inkooporders.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elk record in de tabel, waarschijnlijk een specifiek verwerkt document of transactie vertegenwoordigend.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Universally unique identifier (UUID) in tekstformaat, bijv. `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Betekenis**: Identificatie voor de organisatie die aan het document of de transactie is gekoppeld.
* **Rol**: Vreemde sleutel, mogelijk linkend naar een organisatietabel.
* **Typische Inhoud**: UUID in tekstformaat, bijv. `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Betekenis**: Identificatie voor het document dat door het systeem is verwerkt.
* **Rol**: Vreemde sleutel, linkend naar een documententabel of vergelijkbaar.
* **Typische Inhoud**: UUID in tekstformaat, bijv. `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Betekenis**: Type van het verwerkte document, geeft de aard van het document aan (bijv. INVOICE).
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Reeks die het documenttype aangeeft, bijv. `INVOICE`.

#### ephesoft\_doc\_id

* **Betekenis**: Identificatie gebruikt door het Ephesoft-systeem om het document te volgen.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Korte reeks, mogelijk een identificatie, bijv. `DOC1`.

#### extracted\_data

* **Betekenis**: JSON-gegevens met geëxtraheerde informatie uit het document, inclusief velden, tabellen en metadata.
* **Rol**: Gegevensopslagveld voor geëxtraheerde documentinhoud.
* **Typische Inhoud**: JSON-structuur met details zoals documenttype, velden, tabellen en metadata.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker of het systeem dat het record heeft aangemaakt.
* **Rol**: Vreemde sleutel, mogelijk linkend naar een gebruikerstabel.
* **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt, bijv. `1`.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het record is aangemaakt.
* **Rol**: Technisch veld voor record-tracking.
* **Typische Inhoud**: Tijdstempel met tijdzone, bijv. `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging aan het record.
* **Rol**: Technisch veld voor record-tracking.
* **Typische Inhoud**: Tijdstempel met tijdzone, kan null zijn indien niet gewijzigd sinds aanmaak.

#### is\_deleted

* **Betekenis**: Vlag die aangeeft of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld voor soft-deletion.
* **Typische Inhoud**: Boolean, `true` als het record is verwijderd, anders `false`.
