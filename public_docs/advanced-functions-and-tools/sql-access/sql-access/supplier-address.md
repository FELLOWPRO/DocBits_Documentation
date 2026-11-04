# Leveranciersadres

## Kolommen

* `org_id`: ID naar organisatie
* `customer_number`: intern
* `supplier_number`: intern
* `address_id`: intern
* `supplier_name`: Supplier Name
* `address_1`: intern
* `address_2`: intern
* `address_3`: intern
* `address_4`: intern
* `zip_code`: intern
* `town_city`: intern
* `country_code`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `sub_org_id`: intern
* `id`: intern

## Analyse & Beschrijving

```markdown
# Technische documentatie voor de tabel `public.supplier_address`

## Inleiding

De tabel `public.supplier_address` is bedoeld voor het opslaan van informatie over de adressen van leveranciers. Ze bevat diverse velden die details vastleggen, zoals organisatie-ID's, klant- en leveranciersnummers, meerdere adresregels, contactgegevens, metadata over aanmaak en wijziging en de verwijderstatus. Deze tabel wordt waarschijnlijk in een systeem gebruikt om leveranciersinformatie en de bijbehorende adressen te beheren, wat van belang kan zijn voor logistiek, facturering en contactdoeleinden.

## Kolombeschrijvingen

### org_id
- **Betekenis**: Deze kolom bevat de unieke identificatie van de organisatie.
- **Rol**: Vreemde sleutel, mogelijk gekoppeld aan een organisatietabel.
- **Typische inhoud**: UUID die een organisatie vertegenwoordigt.

### customer_number
- **Betekenis**: Deze kolom kan een uniek nummer bevatten dat aan klanten is toegekend.
- **Rol**: Identificator voor klanten.
- **Typische inhoud**: Alfanumerieke tekenreeks die klantnummers weergeeft.

### supplier_number
- **Betekenis**: Deze kolom bevat een uniek nummer dat aan leveranciers is toegekend.
- **Rol**: Identificator voor leveranciers.
- **Typische inhoud**: Numerieke tekenreeks die leveranciersnummers weergeeft.

### address_id
- **Betekenis**: Deze kolom bevat waarschijnlijk het type adres, zoals 'Discrete' of 'Text'.
- **Rol**: Beschrijvend veld voor de categorisering van adressen.
- **Typische inhoud**: Waarden zoals 'Discrete', 'Text'.

### supplier_name
- **Betekenis**: Deze kolom bevat de naam van de leverancier.
- **Rol**: Beschrijvend veld voor de identificatie van de leverancier.
- **Typische inhoud**: Naam van de leverancier, bijv. "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Betekenis**: Deze kolom bevat de eerste regel van het adres van de leverancier.
- **Rol**: Beschrijvend veld voor adresinformatie.
- **Typische inhoud**: Straatadres, bijv. "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Betekenis**: Deze kolom bevat de tweede regel van het adres van de leverancier, indien van toepassing.
- **Rol**: Aanvullend veld voor adresinformatie.
- **Typische inhoud**: Extra adresgegevens, vaak leeg gelaten.

### address_3
- **Betekenis**: Deze kolom bevat de derde regel van het adres van de leverancier, indien van toepassing.
- **Rol**: Aanvullend veld voor adresinformatie.
- **Typische inhoud**: Extra adresgegevens, vaak leeg gelaten.

### address_4
- **Betekenis**: Deze kolom bevat de vierde regel van het adres van de leverancier, indien van toepassing.
- **Rol**: Aanvullend veld voor adresinformatie.
- **Typische inhoud**: Extra adresgegevens, vaak leeg gelaten.

### zip_code
- **Betekenis**: Deze kolom bevat de postcode van het adres van de leverancier.
- **Rol**: Beschrijvend veld voor geografische identificatie.
- **Typische inhoud**: Numerieke postcode, bijv. "06449".

### town_city
- **Betekenis**: Deze kolom bevat de plaatsnaam van het adres van de leverancier.
- **Rol**: Beschrijvend veld voor geografische identificatie.
- **Typische inhoud**: Naam van de plaats of stad, bijv. "Aschersleben".

### country_code
- **Betekenis**: Deze kolom bevat de ISO-landcode van het adres van de leverancier.
- **Rol**: Beschrijvend veld voor de identificatie van het land.
- **Typische inhoud**: Landcode van twee letters, bijv. "DE".

### created_by
- **Betekenis**: Deze kolom bevat de identificatie van de gebruiker of het systeem dat het record heeft aangemaakt.
- **Rol**: Technisch veld voor het bijhouden van de aanmaak van het record.
- **Typische inhoud**: Integer die een gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: Deze kolom bevat de tijdstempel van het moment waarop het record is aangemaakt.
- **Rol**: Technisch veld voor het bijhouden van het aanmaaktijdstip van het record.
- **Typische inhoud**: Tijdstempel met tijdzone, bijv. "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Betekenis**: Deze kolom bevat de tijdstempel van de laatste wijziging van het record.
- **Rol**: Technisch veld voor het bijhouden van het tijdstip van de laatste update.
- **Typische inhoud**: Tijdstempel met tijdzone, vaak leeg gelaten als `None`.

### is_deleted
- **Betekenis**: Deze kolom geeft aan of het record als verwijderd is gemarkeerd.
- **Rol**: Technisch veld voor soft-delete-functionaliteit.
- **Typische inhoud**: Boolean-waarde, bijv. `False`.

### sub_org_id
- **Betekenis**: Deze kolom bevat een identificatie van een suborganisatie, indien van toepassing.
- **Rol**: Vreemde sleutel of identificator voor suborganisaties.
- **Typische inhoud**: UUID, vaak leeg gelaten.

### id
- **Betekenis**: Deze kolom bevat de unieke identificatie van het record.
- **Rol**: Primaire sleutel van de tabel.
- **Typische inhoud**: UUID die het record vertegenwoordigt.

```
