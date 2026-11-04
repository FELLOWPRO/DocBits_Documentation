# Lookup-veldconfiguratie

## Tabel `public.lookup_field_configuration`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `lookup_rec_id`: intern
* `field_id`: intern
* `lookup_field`: intern
* `is_searchable`: booleaans
* `parent_field_id`: intern
* `auto_trigger`: booleaans
* `created_by`: geheel getal
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: booleaans
* `deleted_on`: tijdstempel met tijdzone
* `search_operator`: intern
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschrijving

## Tabeldocumentatie: `public.lookup_field_configuration`

### Inleiding

De `public.lookup_field_configuration`-tabel lijkt een configuratietabel te zijn die wordt gebruikt om lookup-velden binnen een applicatie te definiëren en te beheren. De tabel bevat metagegevens over elk veld, zoals de identificatie, gekoppelde organisatie, doorzoekbaarheid en auditinformatie. Deze tabel maakt waarschijnlijk deel uit van een groter systeem voor het beheren van dynamische of door de gebruiker gedefinieerde velden, waardoor complexe zoek- en configuratiemogelijkheden mogelijk zijn.

### Kolombeschrijvingen

#### `id`

* **Betekenis**: De unieke identificatie voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die elke configuratie-invoer uniek identificeert.

#### `org_id`

* **Betekenis**: De organisatie-identificatie waaraan deze configuratie is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die de organisatie vertegenwoordigt.

#### `lookup_rec_id`

* **Betekenis**: Een identificatie voor het specifieke lookup-record waarop deze configuratie van toepassing is.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die verwijst naar een specifiek lookup-record.

#### `field_id`

* **Betekenis**: De identificatie van het veld dat wordt geconfigureerd.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die verwijst naar een bepaald veld.

#### `lookup_field`

* **Betekenis**: De naam of het label van het veld dat wordt geconfigureerd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de veldnaam vertegenwoordigt, zoals "address\_1" of "taxratefree".

#### `is_searchable`

* **Betekenis**: Geeft aan of het veld kan worden opgenomen in zoekopdrachten.
* **Rol**: Configuratievlag.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `parent_field_id`

* **Betekenis**: Identificatie van het bovenliggende veld, indien van toepassing.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-tekenreeks of `None` als er geen bovenliggend veld bestaat.

#### `auto_trigger`

* **Betekenis**: Specificeert of de veldconfiguratie automatisch bepaalde acties moet activeren.
* **Rol**: Configuratievlag.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `created_by`

* **Betekenis**: De identificatie van de gebruiker die de configuratie-invoer heeft gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Een geheel getal dat de gebruikers-ID vertegenwoordigt.

#### `created_on`

* **Betekenis**: De tijdstempel wanneer de configuratie-invoer is gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### `last_modified_on`

* **Betekenis**: De tijdstempel van de meest recente wijziging aan de configuratie-invoer.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, of `None` indien nooit gewijzigd.

#### `is_deleted`

* **Betekenis**: Geeft aan of de configuratie-invoer als verwijderd is gemarkeerd.
* **Rol**: Vlag voor zachte verwijdering (Soft Delete).
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `deleted_on`

* **Betekenis**: De tijdstempel wanneer de configuratie-invoer als verwijderd is gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, of `None` indien niet verwijderd.

#### `search_operator`

* **Betekenis**: Definieert de zoekoperator die voor het veld wordt gebruikt.
* **Rol**: Configuratieveld.
* **Typische inhoud**: Een tekenreeks zoals "contains" die het type zoekbewerking aangeeft.

#### `last_modified_by`

* **Betekenis**: Identificatie van de gebruiker die de configuratie-invoer voor het laatst heeft gewijzigd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een UUID-tekenreeks of `None` indien nooit gewijzigd.

#### `deleted_by`

* **Betekenis**: Identificatie van de gebruiker die de invoer als verwijderd heeft gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een UUID-tekenreeks of `None` indien niet verwijderd.

Deze documentatie biedt een gedetailleerd overzicht van de structuur en het doel van elke kolom in de `public.lookup_field_configuration`-tabel, en biedt ontwikkelaars een uitgebreid inzicht in hoe lookup-velden binnen het systeem worden geconfigureerd en beheerd.