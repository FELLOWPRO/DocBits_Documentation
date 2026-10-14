# Voorkeuren

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `pref_key`: intern
* `pref_value`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `deleted_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: intern

## Analyse & Beschrijving

```markdown
# Technische documentatie voor de tabel `public.preferences`

## Inleiding
De tabel `public.preferences` is bedoeld voor het opslaan van configuratie-instellingen en voorkeuren voor diverse organisatorische entiteiten binnen een systeem. Elk item in de tabel vertegenwoordigt een specifieke voorkeurssleutel en de bijbehorende waarde, gekoppeld aan een organisatie of suborganisatie. Deze configuratiegegevens kunnen instellingen omvatten voor btw-nummers, extractie-instellingen, module-activering en meer.

## Kolombeschrijvingen

### id
- **Betekenis**: Deze kolom bevat de unieke identificatie van elk voorkeursitem.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: Een UUID-reeks die elke rij uniek identificeert, zoals `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Betekenis**: Deze kolom bevat de identificatie van de organisatie waaraan de voorkeur is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks die overeenkomt met een organisatie, vergelijkbaar met `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Betekenis**: Deze kolom bevat de sleutel of naam van de voorkeursinstelling.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Tekenreeksen die configuratiesleutels vertegenwoordigen, zoals `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Betekenis**: Deze kolom bevat de waarde van de voorkeur die bij de `pref_key` hoort.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Verschilt per `pref_key`; voorbeelden zijn door komma's gescheiden btw-nummers of boolean-waarden zoals `true` of `false`.

### created_by
- **Betekenis**: Deze kolom geeft het gebruikers-ID aan van de persoon die het voorkeursitem heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een integer die een gebruikers-ID vertegenwoordigt, bijv. `1`.

### created_on
- **Betekenis**: Deze kolom registreert de tijdstempel van het moment waarop de voorkeur is aangemaakt.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tijdstempel met tijdzone, bijv. `2021-11-09 11:04:18+00`.

### last_modified_on
- **Betekenis**: Deze kolom legt de tijdstempel van de laatste wijziging van de voorkeur vast.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tijdstempel met tijdzone die het tijdstip van de laatste update aangeeft, zoals `2023-12-04 10:10:26+00`.

### deleted_on
- **Betekenis**: Deze kolom noteert de tijdstempel van het moment waarop de voorkeur als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Doorgaans `null`, tenzij de rij voor verwijdering is gemarkeerd.

### is_deleted
- **Betekenis**: Deze kolom geeft aan of de voorkeur als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een boolean-waarde, doorgaans `false`.

### user_id
- **Betekenis**: Deze kolom bevat het gebruikers-ID dat aan de voorkeur is gekoppeld.
- **Rol**: Beschrijvend veld, mogelijk een vreemde sleutel.
- **Typische inhoud**: Een integer of `null` indien niet van toepassing.

### sub_org_id
- **Betekenis**: Deze kolom identificeert de suborganisatie die aan de voorkeur is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks of `null` indien niet van toepassing.

De tabel `public.preferences` biedt een flexibele en uitgebreide manier om configuratie-instellingen voor verschillende organisatorische entiteiten te beheren, zodat voorkeuren dynamisch kunnen worden aangepast en in de tijd kunnen worden gevolgd.
```
