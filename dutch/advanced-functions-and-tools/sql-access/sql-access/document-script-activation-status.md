# Document Script activation status

## Tabel `public.document_script_activation_status`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `script_id`: intern

### Analyse & Beschrijving

## Tabeldocumentatie: `public.document_script_activation_status`

### Inleiding

De tabel `public.document_script_activation_status` is ontworpen om de activatiestatus van scripts geassocieerd met documenten binnen een organisatie te beheren. Elk item in de tabel komt overeen met een specifiek script en de huidige activatiestatus ervan, waardoor organisaties mogelijk de uitvoering van scripts in relatie tot hun documenten kunnen controleren en organiseren.

### Kolombeschrijvingen

#### id

* **Betekenis**: Deze kolom slaat een unieke identificatie op voor elk item in de tabel.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Universally unique identifier (UUID) zoals `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Opmerking**: Zorgt ervoor dat elk record uniek identificeerbaar is.

#### org\_id

* **Betekenis**: Vertegenwoordigt de identificatie voor een organisatie.
* **Rol**: Vreemde sleutel, waarschijnlijk verwijzend naar een organisatietabel.
* **Typische Inhoud**: UUID die de organisatie identificeert, bijv. `23f3d697-7411-4c95-981d-faf089d266be`.
* **Opmerking**: Koppelt de scriptactivatiestatus aan een specifieke organisatie.

#### sort\_order

* **Betekenis**: Geeft de volgorde aan waarin scripts moeten worden uitgevoerd of weergegeven.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Integerwaarden die de volgorde vertegenwoordigen, zoals `0`.
* **Opmerking**: Kan worden gebruikt om scripts te prioriteren of te organiseren.

#### is\_active

* **Betekenis**: Geeft aan of een script momenteel actief is.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Boolean waarden, `True` of `False`.
* **Opmerking**: Bepaalt of het bijbehorende script moet worden uitgevoerd.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het record heeft aangemaakt.
* **Rol**: Vreemde sleutel, waarschijnlijk verwijzend naar een gebruikerstabel.
* **Typische Inhoud**: Integerwaarde die een gebruikers-ID vertegenwoordigt, zoals `1`.
* **Opmerking**: Houdt de maker van het record bij voor auditingdoeleinden.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het record is aangemaakt.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd met tijdzone, bijv. `2023-11-20 10:44:14.685170+00:00`.
* **Opmerking**: Biedt een aanmaaktijdstempel voor de verslaglegging.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging aan het record.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd met tijdzone, of `None` indien nooit gewijzigd.
* **Opmerking**: Nuttig voor het volgen van wijzigingen in de loop van de tijd.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Boolean waarden, `True` of `False`.
* **Opmerking**: Maakt soft-deletion van records mogelijk zonder fysieke verwijdering uit de database.

#### script\_id

* **Betekenis**: Identificatie voor het script dat aan het record is gekoppeld.
* **Rol**: Vreemde sleutel, waarschijnlijk verwijzend naar een scripttabel.
* **Typische Inhoud**: UUID die het script identificeert, bijv. `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Opmerking**: Koppelt de activatiestatus aan een specifiek script.
