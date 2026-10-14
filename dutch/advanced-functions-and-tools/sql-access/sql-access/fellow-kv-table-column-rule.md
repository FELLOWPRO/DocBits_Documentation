# Fellow kv table column rule

## Tabel `public.fellow_kv_table_column_rule`

### Kolommen

* `id`: intern
* `docType`: intern
* `tableName`: intern
* `dlfName`: intern
* `multi_line`: boolean
* `filterID1`: intern
* `filterID2`: intern
* `filterID3`: intern
* `tfidf_doc_id`: intern
* `tfidf_id`: intern
* `valuePattern`: intern
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeriek
* `normalizedY1`: numeriek
* `normalizedX0`: numeriek
* `normalizedX1`: numeriek
* `width`: integer
* `height`: integer
* `patternLeft`: intern
* `patternRight`: intern
* `patternAbove`: intern
* `patternBelow`: intern
* `wordLeft`: intern
* `wordAbove`: intern
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID naar organisatie
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `is_new`: boolean

### Analyse & Beschrijving

## Technische Documentatie voor `public.fellow_kv_table_column_rule`

### Inleiding

De tabel `public.fellow_kv_table_column_rule` lijkt te zijn ontworpen voor het opslaan van regels en patronen voor het verwerken of extraheren van gegevens uit documenten. Dit wordt afgeleid uit de aanwezigheid van velden zoals `docType`, `tableName`, `dlfName` en diverse patroon- en coördinatengerelateerde velden. De tabel vergemakkelijkt de toepassing van regels op verschillende documenttypen, waardoor patroonherkenning en gegevensextractie uit gestructureerde documenten zoals facturen of contracten mogelijk wordt.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elke regel.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: UUID-reeksen.
* **Opmerking**: Essentieel om elke rij uniek te identificeren.

#### docType

* **Betekenis**: Type document waarop de regel van toepassing is.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Documenttypen zoals 'INVOICE', 'CONTRACT'.
* **Opmerking**: Helpt bij het categoriseren van regels per documenttype.

#### tableName

* **Betekenis**: Naam van de tabel waarin de regel wordt toegepast.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Tabelnamen zoals 'INVOICE\_TABLE'.
* **Opmerking**: Geeft de context aan waarbinnen de regel wordt toegepast.

#### dlfName

* **Betekenis**: Specifieke veld- of kolomnaam in het document.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Veldnamen zoals 'COUNTRY\_ORIGIN'.
* **Opmerking**: Specificeert het doelveld voor gegevensextractie.

#### multi\_line

* **Betekenis**: Geeft aan of de regel van toepassing is op tekst van meerdere regels.
* **Rol**: Boolean vlag.
* **Typische Inhoud**: `True` of `False`.
* **Opmerking**: Nuttig voor het afhandelen van tekstvelden met meerdere regels.

#### filterID1, filterID2, filterID3

* **Betekenis**: Filters of voorwaarden voor het toepassen van de regel.
* **Rol**: Beschrijvende of voorwaardelijke velden.
* **Typische Inhoud**: Mogelijk reeksen die filtervoorwaarden vertegenwoordigen.
* **Opmerking**: Gebruikt om de toepassing van regels te verfijnen op basis van bepaalde voorwaarden.

#### tfidf\_doc\_id, tfidf\_id

* **Betekenis**: Identificatoren gerelateerd aan TF-IDF verwerking.
* **Rol**: Vreemde sleutel-achtige rollen of identificatoren.
* **Typische Inhoud**: UUID-reeksen.
* **Opmerking**: Waarschijnlijk gerelateerd aan tekstfnalyse en feature-extractie.

#### valuePattern

* **Betekenis**: Regex-patroon voor waarde-extractie.
* **Rol**: Patroonveld.
* **Typische Inhoud**: Reguliere expressies.
* **Opmerking**: Definieert het patroon dat wordt gebruikt om waarden te identificeren en te extraheren.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Betekenis**: Coördinaten die de bounding box voor extractie definiëren.
* **Rol**: Coördinatenvelden.
* **Typische Inhoud**: Integers die pixelposities vertegenwoordigen.
* **Opmerking**: Definieert het interessegebied in een document voor gegevensextractie.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Betekenis**: Genormaliseerde coördinaten voor extractie.
* **Rol**: Coördinatenvelden.
* **Typische Inhoud**: Numerieke waarden die proportionele posities vertegenwoordigen.
* **Opmerking**: Gebruikt voor resolutie-onafhankelijke gebiedsdefinities.

#### width, height

* **Betekenis**: Afmetingen van het gebied gedefinieerd door de coördinaten.
* **Rol**: Dimensievelden.
* **Typische Inhoud**: Integerwaarden.
* **Opmerking**: Helpt bij het definiëren van de grootte van het extractiegebied.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Betekenis**: Contextuele patronen rondom de doelgegevens.
* **Rol**: Patroonvelden.
* **Typische Inhoud**: Reguliere expressies.
* **Opmerking**: Bieden context voor waar de gegevens zich bevinden ten opzichte van andere tekst.

#### wordLeft, wordAbove

* **Betekenis**: Specifieke woorden die zich in de buurt van de doelgegevens bevinden.
* **Rol**: Contextuele velden.
* **Typische Inhoud**: Specifieke woorden of zinnen.
* **Opmerking**: Helpt bij het verfijnen van de zoekopdracht naar doelgegevens op basis van nabijgelegen woorden.

#### ruleWeight

* **Betekenis**: Significantie of prioriteit van de regel.
* **Rol**: Gewichtings- of prioriteitsveld.
* **Typische Inhoud**: Integerwaarden.
* **Opmerking**: Hogere waarden kunnen wijzen op een hogere prioriteit of belang.

#### user\_id

* **Betekenis**: Identificatie van de gebruiker die de regel heeft aangemaakt of gewijzigd.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: Integerwaarden.
* **Opmerking**: Koppelt de regel aan een specifieke gebruiker.

#### org\_id

* **Betekenis**: Identificatie van de organisatie die aan de regel is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: UUID-reeksen.
* **Opmerking**: Koppel de regel aan een organisatie.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer de regel is aangemaakt.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Tijdstempel met tijdzone.
* **Opmerking**: Nuttig voor het volgen van de aanmaakgeschiedenis van de regel.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van de regel.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Tijdstempel met tijdzone of `None`.
* **Opmerking**: Volgt wijzigingen aan de regel in de loop van de tijd.

#### is\_deleted

* **Betekenis**: Geeft aan of de regel als verwijderd is gemarkeerd.
* **Rol**: Boolean vlag.
* **Typische Inhoud**: `True` of `False`.
* **Opmerking**: Gebruikt voor soft-deletion van regels.

#### is\_new

* **Betekenis**: Geeft aan of de regel nieuw is aangemaakt.
* **Rol**: Boolean vlag.
* **Typische Inhoud**: `True` of `False`.
* **Opmerking**: Helpt bij het identificeren van recent toegevoegde regels.
