# Additional charge costing element

## Tabel `public.additional_charge_costing_element`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `costing_element`: intern
* `description`: intern
* `charge_type`: intern
* `distribution_method`: intern
* `distribution_type`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: intern
* `charge_count`: integer
* `charge_icon`: intern
* `charge_category`: intern
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & beschrijving

## Tabeldocumentatie: `public.additional_charge_costing_element`

### Inleiding

De tabel `public.additional_charge_costing_element` is bedoeld om informatie over verschillende extra kostenelementen binnen een organisatie te beheren en op te slaan. Dit omvat gegevens over het type kosten, de wijze waarop ze worden verdeeld en administratieve metagegevens zoals details over aanmaak en wijziging. Deze tabel wordt waarschijnlijk gebruikt voor financieel en operationeel beheer binnen een organisatie, met de nadruk op extra kosten die moeten worden bijgehouden en geanalyseerd.

### Kolombeschrijvingen

#### id

* **Betekenis**: Deze kolom bevat een unieke identifier voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een unieke alfanumerieke tekenreeks die elk kostenelementrecord identificeert.

#### org\_id

* **Betekenis**: De identifier van de organisatie waartoe dit kostenelement behoort.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID die de organisatie vertegenwoordigt.

#### costing\_element

* **Betekenis**: Een identifier of code voor het kostenelement.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een alfanumerieke tekenreeks die het specifieke kostenelement vertegenwoordigt.

#### description

* **Betekenis**: Een tekstuele beschrijving van het kostenelement.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een korte tekstuele toelichting op het kostenelement.

#### charge\_type

* **Betekenis**: Het type kosten dat aan dit kostenelement is gekoppeld.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een code of korte tekst die het kostentype aangeeft.

#### distribution\_method

* **Betekenis**: De methode waarmee de kosten worden verdeeld.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een code of korte tekst die de verdelingsmethode aangeeft.

#### distribution\_type

* **Betekenis**: Het type verdeling voor de kosten.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een code of korte tekst die het verdelingstype aangeeft.

#### created\_by

* **Betekenis**: Identifier van de gebruiker die het record heeft aangemaakt.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een geheel getal dat de gebruikers-ID vertegenwoordigt.

#### created\_on

* **Betekenis**: Tijdstempel dat aangeeft wanneer het record is aangemaakt.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van het record.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Booleaanse waarde (`True` of `False`).

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop het record als verwijderd is gemarkeerd.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie of `None` als het record niet is verwijderd.

#### sub\_org\_id

* **Betekenis**: Identifier van een suborganisatie die bij het kostenelement hoort.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID die de suborganisatie vertegenwoordigt.

#### charge\_count

* **Betekenis**: Het aantal kosten dat aan het kostenelement is gekoppeld.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een geheel getal dat het aantal kosten weergeeft.

#### charge\_icon

* **Betekenis**: Pictogram of symbool dat aan de kosten is gekoppeld.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die het pictogram vertegenwoordigt, waarschijnlijk een pad of identifier.

#### charge\_category

* **Betekenis**: De categorie waaronder de kosten vallen.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de kostencategorie vertegenwoordigt.

#### charge\_sequence\_number

* **Betekenis**: Volgnummer voor het ordenen van kosten.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een geheel getal waarmee kosten in volgorde worden gezet.

#### charge\_operator

* **Betekenis**: Identifier van de operator die verantwoordelijk is voor de kosten.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een geheel getal dat de operator-ID vertegenwoordigt.

#### last\_modified\_by

* **Betekenis**: Identifier van de gebruiker die het record het laatst heeft gewijzigd.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een tekenreeks die de gebruikers-ID vertegenwoordigt, mogelijk `None` als het record nooit is gewijzigd.

#### deleted\_by

* **Betekenis**: Identifier van de gebruiker die het record als verwijderd heeft gemarkeerd.
* **Rol**: Administratief veld.
* **Typische inhoud**: Een tekenreeks die de gebruikers-ID vertegenwoordigt, mogelijk `None` als het record niet is verwijderd.
