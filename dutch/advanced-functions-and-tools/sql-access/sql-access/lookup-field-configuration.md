# Lookup field configuration

## Tabel `public.lookup_field_configuration`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `lookup_rec_id`: intern
* `field_id`: intern
* `lookup_field`: intern
* `is_searchable`: boolean
* `parent_field_id`: intern
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `search_operator`: intern
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & beschrijving

## Tabeldocumentatie: `public.lookup_field_configuration`

### Inleiding

De tabel `public.lookup_field_configuration` lijkt een configuratietabel te zijn die wordt gebruikt om opzoekvelden binnen een toepassing te definiëren en te beheren. De tabel bevat metagegevens over elk veld, zoals de identifier, de gekoppelde organisatie, doorzoekbaarheid en auditinformatie. Deze tabel maakt waarschijnlijk deel uit van een groter systeem voor het beheren van dynamische of door de gebruiker gedefinieerde velden, met mogelijkheden voor complexe query's en configuratie.

### Kolombeschrijvingen

#### `id`

* **Betekenis**: De unieke identifier van elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die elke configuratievermelding uniek identificeert.

#### `org_id`

* **Betekenis**: De organisatie-identifier waaraan deze configuratie is gekoppeld.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die de organisatie vertegenwoordigt.

#### `lookup_rec_id`

* **Betekenis**: Een identifier voor het specifieke opzoekrecord waarop deze configuratie van toepassing is.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die naar een specifiek opzoekrecord verwijst.

#### `field_id`

* **Betekenis**: De identifier van het veld dat wordt geconfigureerd.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die naar een bepaald veld verwijst.

#### `lookup_field`

* **Betekenis**: De naam of het label van het veld dat wordt geconfigureerd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de veldnaam weergeeft, zoals "address\_1" of "taxratefree".

#### `is_searchable`

* **Betekenis**: Geeft aan of het veld in zoekbewerkingen kan worden opgenomen.
* **Rol**: Configuratievlag.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `parent_field_id`

* **Betekenis**: Identifier van het bovenliggende veld, indien van toepassing.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID-tekenreeks of `None` als er geen bovenliggend veld bestaat.

#### `auto_trigger`

* **Betekenis**: Geeft aan of de veldconfiguratie automatisch bepaalde acties moet activeren.
* **Rol**: Configuratievlag.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `created_by`

* **Betekenis**: De identifier van de gebruiker die de configuratievermelding heeft aangemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Een geheel getal dat het gebruikers-ID vertegenwoordigt.

#### `created_on`

* **Betekenis**: De tijdstempel van het moment waarop de configuratievermelding is aangemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### `last_modified_on`

* **Betekenis**: De tijdstempel van de meest recente wijziging van de configuratievermelding.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, of `None` als nooit gewijzigd.

#### `is_deleted`

* **Betekenis**: Geeft aan of de configuratievermelding als verwijderd is gemarkeerd.
* **Rol**: Vlag voor zachte verwijdering.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`).

#### `deleted_on`

* **Betekenis**: De tijdstempel van het moment waarop de configuratievermelding als verwijderd is gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, of `None` als niet verwijderd.

#### `search_operator`

* **Betekenis**: Definieert de zoekoperator die voor het veld wordt gebruikt.
* **Rol**: Configuratieveld.
* **Typische inhoud**: Een tekenreeks zoals "contains" die het type zoekbewerking aangeeft.

#### `last_modified_by`

* **Betekenis**: Identifier van de gebruiker die de configuratievermelding het laatst heeft gewijzigd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een UUID-tekenreeks of `None` als nooit gewijzigd.

#### `deleted_by`

* **Betekenis**: Identifier van de gebruiker die de vermelding als verwijderd heeft gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Een UUID-tekenreeks of `None` als niet verwijderd.

Deze documentatie geeft een gedetailleerd inzicht in de structuur en het doel van elke kolom in de tabel `public.lookup_field_configuration` en biedt ontwikkelaars een volledig beeld van hoe opzoekvelden in het systeem worden geconfigureerd en beheerd.
