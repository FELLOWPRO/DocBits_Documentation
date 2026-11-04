# PO-matchtolerantie

## Tabel `public.po_match_tolerance`

### Kolommen

* `id`: intern
* `po_match_rule_id`: intern
* `tolerance`: numeriek
* `created_on`: tijdstempel met tijdzone
* `created_by`: intern
* `last_modified_on`: tijdstempel met tijdzone
* `last_modified_by`: intern

### Analyse & Beschrijving

## Technische documentatie voor `public.po_match_tolerance` tabel

### Inleiding

De `public.po_match_tolerance` tabel slaat tolerantie-instellingen op voor regels voor het matchen van inkooporders (Purchase Order, PO). Het definieert de toegestane afwijking (tolerantie) voor specifieke matchregels, waardoor flexibiliteit in het matchingsproces mogelijk is.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de tolerantie-instelling.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden.

#### po\_match\_rule\_id

* **Betekenis**: De identificatie van de PO-matchregel waaraan deze tolerantie is gekoppeld.
* **Rol**: Vreemde sleutel, verwijzend naar de PO-matchregels-tabel.
* **Typische inhoud**: UUID-waarden.

#### tolerance

* **Betekenis**: De numerieke waarde van de toegestane tolerantie.
* **Rol**: Configuratieveld.
* **Typische inhoud**: Numerieke waarden die percentages of absolute bedragen vertegenwoordigen, bijv. `0.05` (5%) of `10.00`.

#### created\_on

* **Betekenis**: De datum en tijd waarop de tolerantie-instelling is gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels met tijdzone.

#### created\_by

* **Betekenis**: De gebruiker die de tolerantie-instelling heeft gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID.

#### last\_modified\_on

* **Betekenis**: De datum en tijd van de laatste wijziging.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels met tijdzone of `None`.

#### last\_modified\_by

* **Betekenis**: De gebruiker die de tolerantie-instelling voor het laatst heeft gewijzigd.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID of `None`.