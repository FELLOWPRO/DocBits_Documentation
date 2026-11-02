# API-inloggegevens

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `sub_org_id`: intern
* `title`: intern
* `credentials_type`: intern
* `credentials_json`: text
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `last_modified_by`: intern
* `deleted_by`: intern

## Analyse & beschrijving

```markdown
# Tabeldocumentatie: `public.api_credentials`

## Inleiding

De tabel `public.api_credentials` is bedoeld om gegevens over API-credentials op te slaan en te beheren. Deze tabel is van cruciaal belang voor organisaties om hun API-authenticatiegegevens veilig te beheren, zodat verschillende services met de juiste credentials met elkaar kunnen communiceren. Ze bevat informatie over het type credentials, de organisatie waartoe ze behoren en metagegevens over aanmaak en wijziging.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identifier voor elke vermelding in de tabel.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: Een universeel unieke identifier (UUID) die een specifieke set API-credentials vertegenwoordigt.

### org_id
- **Betekenis**: Identifier van de organisatie die eigenaar is van de credentials.
- **Rol**: Refererende sleutel.
- **Typische inhoud**: Een UUID die verwijst naar het record van de organisatie in een andere tabel.

### sub_org_id
- **Betekenis**: Identifier van een suborganisatie binnen de hoofdorganisatie.
- **Rol**: Refererende sleutel (optioneel).
- **Typische inhoud**: Kan een UUID bevatten die naar een suborganisatie verwijst, of `None`.

### title
- **Betekenis**: Een beschrijvende titel voor de API-credentials.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een tekenreeks zoals "supplier_auth" die het doel of gebruik van de credentials aangeeft.

### credentials_type
- **Betekenis**: Geeft het type opgeslagen credentials aan.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Een tekenreeks zoals "ionapi" die het formaat of protocol aangeeft dat de credentials gebruiken.

### credentials_json
- **Betekenis**: Een JSON-object met gedetailleerde credentialinformatie.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een JSON-tekenreeks met diverse sleutel-waardeparen die authenticatieparameters beschrijven.

### created_by
- **Betekenis**: Gebruikers-ID van de persoon die het credentialsrecord heeft aangemaakt.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een geheel getal dat de gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: Tijdstempel dat aangeeft wanneer de credentials zijn aangemaakt.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een datum-tijdwaarde met tijdzone, bijv. `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Betekenis**: Tijdstempel dat het tijdstip van de laatste wijziging van de credentials aangeeft.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een datum-tijdwaarde met tijdzone, of `None` als nooit gewijzigd.

### is_deleted
- **Betekenis**: Vlag die aangeeft of de credentials als verwijderd zijn gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een booleaanse waarde, waarbij `False` aangeeft dat de credentials actief zijn.

### deleted_on
- **Betekenis**: Tijdstempel dat aangeeft wanneer de credentials als verwijderd zijn gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een datum-tijdwaarde met tijdzone, of `None` als niet verwijderd.

### last_modified_by
- **Betekenis**: Identifier van de gebruiker die de credentials het laatst heeft gewijzigd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tekenreeks die de ID van de gebruiker vertegenwoordigt, of `None`.

### deleted_by
- **Betekenis**: Identifier van de gebruiker die de credentials als verwijderd heeft gemarkeerd.
- **Rol**: Technisch veld.
- **Typische inhoud**: Een tekenreeks die de ID van de gebruiker vertegenwoordigt, of `None`.
```
