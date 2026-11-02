# TF-IDF-voorkeuren

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `tfidf_id`: intern
* `pref_key`: intern
* `pref_value`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_by`: intern
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_by`: intern
* `deleted_on`: tijdstempel met tijdzone
* `supplier_id`: intern

## Analyse & Beschrijving

```markdown
# Technische documentatie voor de tabel `public.tfidf_preferences`

## Inleiding

De tabel `public.tfidf_preferences` is kennelijk bedoeld voor het opslaan van voorkeuren met betrekking tot TF-IDF-configuraties of -modellen (Term Frequency-Inverse Document Frequency). Deze tabel bevat informatie over specifieke voorkeuren die door organisaties zijn ingesteld, inclusief voorkeurssleutels en de bijbehorende waarden, samen met metadata over aanmaak-, wijzigings- en verwijderacties.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk record in de tabel.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: Een UUID-reeks die de unieke ID van een voorkeursitem vertegenwoordigt.

### org_id
- **Betekenis**: Identificatie van de organisatie die aan de voorkeur is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks die de voorkeur aan een specifieke organisatie koppelt.

### tfidf_id
- **Betekenis**: Identificatie van de specifieke TF-IDF-configuratie of het specifieke TF-IDF-model.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks die de gekoppelde TF-IDF-configuratie vertegenwoordigt.

### pref_key
- **Betekenis**: De sleutel of naam van de voorkeursinstelling.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een tekenreeks die de naam van de voorkeur weergeeft, zoals 'USE_ETEXT_IF_AVAILABLE' of 'AI_MODEL'.

### pref_value
- **Betekenis**: De waarde die bij de voorkeurssleutel hoort.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een tekenreeks of tekstwaarde die overeenkomt met de voorkeurssleutel, bijv. 'true', 'false' of 'Full'.

### created_by
- **Betekenis**: Identificatie van de gebruiker die het voorkeursitem heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een integer die het gebruikers-ID van de maker vertegenwoordigt.

### created_on
- **Betekenis**: Tijdstempel van het moment waarop het voorkeursitem is aangemaakt.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tijdstempel met tijdzone die de aanmaakdatum en -tijd aangeeft.

### last_modified_by
- **Betekenis**: Identificatie van de gebruiker die het voorkeursitem het laatst heeft gewijzigd.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een UUID die het gebruikers-ID vertegenwoordigt van de persoon die het item het laatst heeft gewijzigd, indien van toepassing.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging van het voorkeursitem.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tijdstempel met tijdzone die de datum en tijd van de laatste wijziging toont.

### is_deleted
- **Betekenis**: Vlag die aangeeft of het voorkeursitem als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een boolean-waarde; `True` als het item is verwijderd, anders `False`.

### deleted_by
- **Betekenis**: Identificatie van de gebruiker die het voorkeursitem als verwijderd heeft gemarkeerd.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een UUID die het gebruikers-ID vertegenwoordigt van degene die het item heeft verwijderd, indien van toepassing.

### deleted_on
- **Betekenis**: Tijdstempel van het moment waarop het voorkeursitem als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tijdstempel met tijdzone die aangeeft wanneer het item is verwijderd.

### supplier_id
- **Betekenis**: Identificatie van de leverancier die aan de voorkeur is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks die de aan de voorkeur gekoppelde leverancier vertegenwoordigt.

Deze documentatie geeft een gedetailleerd overzicht van het doel en de structuur van de tabel `public.tfidf_preferences` en helpt ontwikkelaars te begrijpen hoe zij deze gegevens effectief kunnen gebruiken.
```
