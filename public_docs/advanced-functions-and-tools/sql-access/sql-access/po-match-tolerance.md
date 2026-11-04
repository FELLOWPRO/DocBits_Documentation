# Tolerantie voor inkoopordermatching

## Tabel `public.po_match_tolerance`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `item_number`: intern
* `supplier_item_number`: intern
* `description`: intern
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: intern
* `quantity_tolerance_type`: intern

### Analyse & Beschrijving

## Technische documentatie voor de tabel `public.po_match_tolerance`

### Inleiding

De tabel `public.po_match_tolerance` is bedoeld voor het beheren en opslaan van tolerantieniveaus die horen bij het matchingproces van inkooporders (PO). Het gaat hierbij doorgaans om de toegestane afwijkingen in eenheidsprijzen en hoeveelheden tussen bestelde en ontvangen goederen. Elk item in de tabel vertegenwoordigt de toleranties voor specifieke artikelen, waarmee organisaties consistentie en nauwkeurigheid in hun inkoopprocessen kunnen waarborgen.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elk item in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-reeks die elk tolerantierecord uniek identificeert.

#### org\_id

* **Betekenis**: Identificatie van de organisatie waaraan de toleranties zijn gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-reeks die verwijst naar de organisatie binnen het systeem.

#### item\_number

* **Betekenis**: Het specifieke artikelnummer waarvoor toleranties zijn gedefinieerd.
* **Rol**: Zakelijke identificator.
* **Typische inhoud**: Een tekenreeks met de code of het nummer van het artikel in de voorraad van de organisatie.

#### supplier\_item\_number

* **Betekenis**: Het artikelnummer zoals dat door de leverancier wordt opgegeven.
* **Rol**: Zakelijke identificator.
* **Typische inhoud**: Een tekenreeks die `None` kan zijn als er niets is opgegeven en die de code of het nummer van de leverancier voor het artikel weergeeft.

#### description

* **Betekenis**: Een tekstuele beschrijving van het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks met details over het artikel, die `None` kan zijn.

#### unit\_price\_tolerance

* **Betekenis**: De toegestane afwijking in eenheidsprijs voor het artikel.
* **Rol**: Bedrijfsregel.
* **Typische inhoud**: Een numerieke waarde die de tolerantie in de eenheidsprijs aangeeft, als percentage of als absolute waarde.

#### quantity\_tolerance

* **Betekenis**: De toegestane afwijking in hoeveelheid voor het artikel.
* **Rol**: Bedrijfsregel.
* **Typische inhoud**: Een numerieke waarde die de tolerantie in de hoeveelheid aangeeft, als percentage of als absolute waarde.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het item heeft aangemaakt.
* **Rol**: Audit-/logveld.
* **Typische inhoud**: Een integer die doorgaans verwijst naar een gebruikers-ID in het systeem.

#### created\_on

* **Betekenis**: De tijdstempel van het moment waarop het item is aangemaakt.
* **Rol**: Audit-/logveld.
* **Typische inhoud**: Een datum-tijdwaarde met tijdzone die de aanmaakdatum en -tijd aangeeft.

#### last\_modified\_on

* **Betekenis**: De tijdstempel van de laatste wijziging van het item.
* **Rol**: Audit-/logveld.
* **Typische inhoud**: Een datum-tijdwaarde met tijdzone die aangeeft wanneer het record voor het laatst is bijgewerkt, en die `None` kan zijn als het niet is gewijzigd.

#### is\_deleted

* **Betekenis**: Geeft aan of het item logisch is verwijderd.
* **Rol**: Technische indicator voor soft delete.
* **Typische inhoud**: Een boolean waarbij `False` actief betekent en `True` logisch verwijderd.

#### unit\_price\_tolerance\_type

* **Betekenis**: Bepaalt het type eenheidsprijstolerantie (bijv. percentage of absolute waarde).
* **Rol**: Bedrijfsregel.
* **Typische inhoud**: Een tekenreeks, vaak 'value', die het type tolerantiemaat aangeeft.

#### quantity\_tolerance\_type

* **Betekenis**: Bepaalt het type hoeveelheidstolerantie (bijv. percentage of absolute waarde).
* **Rol**: Bedrijfsregel.
* **Typische inhoud**: Een tekenreeks, vaak 'value', die het type tolerantiemaat aangeeft.

Deze documentatie geeft een gedetailleerd overzicht van elk veld in de tabel `public.po_match_tolerance` en biedt inzicht in de mogelijke inhoud en de rol van deze velden in het beheer van inkooporders.
