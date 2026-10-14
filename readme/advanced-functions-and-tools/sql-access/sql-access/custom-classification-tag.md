# Custom classification tag

## Tabel `public.custom_classification_tag`

### Kolommen

* `id`: integer
* `org_id`: ID naar organisatie
* `name`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & beschrijving

## Technische documentatie voor de tabel `public.custom_classification_tag`

### Inleiding

De tabel `public.custom_classification_tag` is bedoeld om aangepaste classificatietags binnen een organisatie te beheren. Ze legt essentiële informatie over elke tag vast, waaronder de koppeling aan een organisatie, details over aanmaak en wijziging en de levenscyclusstatus.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identifier voor elke classificatietag.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een geheel getal dat elk record in de tabel uniek identificeert.

#### org\_id

* **Betekenis**: De identifier van de organisatie waartoe de classificatietag behoort.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een tekenreeks, waarschijnlijk een UUID, die de unieke ID van de organisatie vertegenwoordigt.

#### name

* **Betekenis**: De naam of het label van de classificatietag.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de naam of beschrijving van de tag aangeeft. Kan een lege tekenreeks zijn als er geen naam is opgegeven.

#### created\_by

* **Betekenis**: De identifier van de gebruiker die de classificatietag heeft aangemaakt.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een geheel getal dat het gebruikers-ID van de maker vertegenwoordigt.

#### created\_on

* **Betekenis**: De tijdstempel die aangeeft wanneer de classificatietag is aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een timestamp with time zone die de exacte datum en tijd van aanmaak vastlegt.

#### last\_modified\_on

* **Betekenis**: De tijdstempel van de laatste wijziging van de classificatietag.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een timestamp with time zone, die `None` kan zijn als er sinds het aanmaken geen wijzigingen hebben plaatsgevonden.

#### is\_deleted

* **Betekenis**: Een vlag die aangeeft of de classificatietag als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een booleaanse waarde (`True` of `False`), waarbij `False` betekent dat de tag actief is en `True` aangeeft dat deze is verwijderd of gedeactiveerd.
