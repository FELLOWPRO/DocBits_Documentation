# Lookup-tabel

## Tabel `public.lookup_table`

### Kolommen

* `id`: intern
* `name`: Naam van de lookup-tabel
* `created_on`: tijdstempel met tijdzone
* `org_id`: ID naar organisatie

### Analyse & Beschrijving

## Technische documentatie voor `public.lookup_table` tabel

### Inleiding

De `public.lookup_table` tabel fungeert als een register voor lookup-tabellen die binnen de organisatie worden gebruikt. Het slaat essentiële metagegevens over elke lookup-tabel op, waaronder de unieke identificatie, naam, aanmaaktijdstempel en de bijbehorende organisatie. Deze tabel is van fundamenteel belang voor het beheer en de verwijzing naar verschillende datasets die voor lookup-doeleinden in het systeem worden gebruikt.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elke lookup-tabel-invoer.
* **Rol**: Primaire sleutel die elke rij in de tabel uniek identificeert.
* **Typische inhoud**: UUID-waarden, bijv. `'a1b2c3d4-e5f6-7890-1234-567890abcdef'`.

#### name

* **Betekenis**: De naam van de lookup-tabel.
* **Rol**: Beschrijvend veld dat wordt gebruikt om de specifieke lookup-tabel te identificeren.
* **Typische inhoud**: Tekenreeksen die de dataset vertegenwoordigen, zoals `'Countries'`, `'Currencies'`, `'Departments'`.

#### created\_on

* **Betekenis**: De datum en tijd waarop de lookup-tabel-invoer is gemaakt.
* **Rol**: Auditveld voor het volgen van de aanmaaktijd van het record.
* **Typische inhoud**: Tijdstempels met tijdzone-informatie, bijv. `2024-01-01 12:00:00 UTC`.

#### org\_id

* **Betekenis**: De identificatie van de organisatie waartoe de lookup-tabel behoort.
* **Rol**: Vreemde sleutel, gekoppeld aan de organisatietabel.
* **Typische inhoud**: UUID-waarden die de organisatie-ID aangeven, bijv. `'f9e8d7c6-b5a4-3210-9876-543210fedcba'`.