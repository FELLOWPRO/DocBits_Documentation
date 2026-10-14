# Batch instance

## Tabel `public.batch_instance`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & beschrijving

## Tabeldocumentatie: `public.batch_instance`

### Inleiding

De tabel `public.batch_instance` is bedoeld om informatie over verschillende batchinstanties binnen een organisatie op te slaan. Ze bevat belangrijke metagegevens over elke instantie, waaronder de unieke identificatie, de organisatie waartoe de instantie behoort en details over aanmaak en wijziging. Deze tabel is essentieel voor het volgen van de levenscyclus en het beheer van batchinstanties, vermoedelijk in een softwaretoepassing voor batchverwerking.

### Kolommen

#### `id`

* **Betekenis**: Deze kolom bevat de unieke identifier van elke batchinstantie.
* **Rol**: Primaire sleutel (`id`).
* **Typische inhoud**: Een UUID-tekenreeks die elke batchinstantie uniek identificeert, bijv. `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Betekenis**: Deze kolom bevat de identifier van de organisatie die bij de batchinstantie hoort.
* **Rol**: Refererende sleutel (`org_id`).
* **Typische inhoud**: Een UUID-tekenreeks die de organisatie vertegenwoordigt, bijv. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Betekenis**: Deze kolom geeft de gebruiker of systeementiteit aan die de batchinstantie heeft aangemaakt.
* **Rol**: Mogelijk een refererende sleutel die naar een gebruikerstabel of vergelijkbaar verwijst.
* **Typische inhoud**: Een geheel getal dat de ID van de maker vertegenwoordigt, bijv. `1`.

#### `created_on`

* **Betekenis**: Deze kolom registreert de tijdstempel van het moment waarop de batchinstantie is aangemaakt.
* **Rol**: Technisch veld voor audit- en trackingdoeleinden.
* **Typische inhoud**: Een timestamp with time zone, bijv. `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Betekenis**: Deze kolom bevat de tijdstempel van de laatste wijziging van de batchinstantie.
* **Rol**: Technisch veld voor het auditen van wijzigingen.
* **Typische inhoud**: Meestal null, of een timestamp with time zone als er wijzigingen zijn doorgevoerd.

#### `is_deleted`

* **Betekenis**: Deze kolom geeft aan of de batchinstantie als verwijderd is gemarkeerd.
* **Rol**: Technisch veld voor zachte verwijdering.
* **Typische inhoud**: Een booleaanse waarde, meestal `False` als de instantie actief is, bijv. `False`.

Deze documentatie geeft een uitgebreid overzicht van de tabel `public.batch_instance` en beschrijft het doel en de structuur van elke kolom, wat van cruciaal belang is voor ontwikkelaars die met dit datamodel werken.
