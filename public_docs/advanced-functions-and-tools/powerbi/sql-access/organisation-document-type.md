# Organisatie Documenttype

## Tabel `public.organisation_document_type`

### Kolommen

* `id`: intern
* `document_type_id`: intern
* `organisation_id`: intern
* `created_on`: tijdstempel met tijdzone
* `created_by`: intern
* `is_active`: booleaans

### Analyse & Beschrijving

## Technische documentatie voor `public.organisation_document_type` tabel

### Inleiding

De `public.organisation_document_type` tabel wordt gebruikt om de associatie tussen organisaties en documenttypen te beheren. Het definieert welke documenttypen beschikbaar en actief zijn voor specifieke organisaties binnen het systeem. Deze tabel is essentieel voor het configureren van documentspecificaties per organisatie.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de koppeling tussen organisatie en documenttype.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden, bijv. `'b2c3d4e5-f6a7-8901-2345-67890abcdef1'`.

#### document\_type\_id

* **Betekenis**: De identificatie van het documenttype.
* **Rol**: Vreemde sleutel, verwijzend naar de documenttypen-tabel.
* **Typische inhoud**: UUID-waarden die specifieke documenttypen vertegenwoordigen, zoals Factuur, Bestelling, enz.

#### organisation\_id

* **Betekenis**: De identificatie van de organisatie.
* **Rol**: Vreemde sleutel, verwijzend naar de organisatietabel.
* **Typische inhoud**: UUID-waarden die de organisatie identificeren.

#### created\_on

* **Betekenis**: De datum en tijd waarop de koppeling is gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels met tijdzone, bijv. `2024-03-15 09:30:00 UTC`.

#### created\_by

* **Betekenis**: De gebruiker die de koppeling heeft gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID of systeemidentificatie.

#### is\_active

* **Betekenis**: Geeft aan of de koppeling tussen het documenttype en de organisatie momenteel actief is.
* **Rol**: Statusvlag.
* **Typische inhoud**: Booleaanse waarden (`True` of `False`).