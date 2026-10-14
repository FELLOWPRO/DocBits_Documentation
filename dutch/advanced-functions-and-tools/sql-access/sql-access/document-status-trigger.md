# Document status trigger

## Tabel `public.document_status_trigger`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `trigger_doc_type`: intern
* `trigger_doc_status`: intern
* `trigger_url`: intern
* `is_active`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

### Analyse & Beschrijving

## Technische Documentatie voor de Tabel `public.document_status_trigger`

### Inleiding

De tabel `public.document_status_trigger` is ontworpen om de status van documenten binnen een organisatie te beheren en te volgen. Deze tabel lijkt triggers te verwerken die verband houden met documentverwerking, waarschijnlijk in een workflow-systeem. Het legt informatie vast over documenttypen en hun statuswijzigingen, waarbij acties of workflows mogelijk worden getriggerd via gespecificeerde URL's.

### Kolombeschrijvingen

#### id

* **Betekenis**: Deze kolom slaat een unieke identificatie op voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Een UUID-reeks, bijv. `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Betekenis**: Vertegenwoordigt de unieke identificatie voor een organisatie.
* **Rol**: Vreemde sleutel, die linkt naar een organisatie-entiteit.
* **Typische Inhoud**: Een UUID-reeks, bijv. `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Betekenis**: Specificeert het type document dat aan de trigger is gekoppeld.
* **Rol**: Beschrijvend veld dat het documenttype aangeeft.
* **Typische Inhoud**: Namen van documenttypen, zoals `INVOICE`.

#### trigger\_doc\_status

* **Betekenis**: Geeft de specifieke status van het document aan die de trigger activeert.
* **Rol**: Beschrijvend veld dat de documentstatus specificeert.
* **Typische Inhoud**: Statusbeschrijvingen, zoals `approved_pending_second_approval`.

#### trigger\_url

* **Betekenis**: URL die wordt geactiveerd (getriggerd) wanneer de documentstatus aan bepaalde voorwaarden voldoet.
* **Rol**: Technisch veld voor workflowautomatisering.
* **Typische Inhoud**: URL's, bijv. `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Betekenis**: Geeft aan of de trigger momenteel actief is.
* **Rol**: Technisch veld voor het beheren van trigger-statussen.
* **Typische Inhoud**: Boolean waarden, `True` of `False`.

#### created\_by

* **Betekenis**: Identificeert de gebruiker die het record heeft aangemaakt.
* **Rol**: Vreemde sleutel naar een gebruikersentiteit.
* **Typische Inhoud**: Integer gebruikers-ID's, bijv. `1`.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het record is aangemaakt.
* **Rol**: Technisch veld voor auditing en het bijhouden van wijzigingen.
* **Typische Inhoud**: Tijdstempels met tijdzone, bijv. `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging aan het record.
* **Rol**: Technisch veld voor auditing en het bijhouden van wijzigingen.
* **Typische Inhoud**: Tijdstempels met tijdzone, kan `None` zijn indien niet gewijzigd.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd of inactief wordt beschouwd.
* **Rol**: Technisch veld voor soft-deletion.
* **Typische Inhoud**: Boolean waarden, `True` of `False`.

Deze tabel biedt een gestructureerde aanpak voor het beheren van documentstatussen en bijbehorende triggers binnen het workflow-systeem van een organisatie, waardoor acties automatisch kunnen worden ondernomen naarmate documenten door verschillende statussen vorderen.
