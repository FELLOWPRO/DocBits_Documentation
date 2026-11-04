# Voorkeuren

## Tabel `public.preferences`

### Kolommen

* `id`: intern
* `user_id`: intern
* `type`: intern
* `value`: intern

### Analyse & Beschrijving

## Technische documentatie voor `public.preferences` tabel

### Inleiding

De `public.preferences` tabel wordt gebruikt om gebruikersspecifieke voorkeuren en instellingen op te slaan. Hiermee kunnen gebruikers hun ervaring binnen de applicatie aanpassen door instellingen zoals taal, thema of meldingsvoorkeuren op te slaan.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de voorkeursinstelling.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden.

#### user\_id

* **Betekenis**: De identificatie van de gebruiker aan wie de voorkeur is gekoppeld.
* **Rol**: Vreemde sleutel, verwijzend naar de gebruikerstabel.
* **Typische inhoud**: UUID-waarden of gehele getallen die gebruikers identificeren.

#### type

* **Betekenis**: Het type of de categorie van de voorkeur.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekenreeksen zoals `'theme'`, `'language'`, `'notifications'`.

#### value

* **Betekenis**: De specifieke waarde of instelling voor de voorkeur.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Tekenreeksen, booleaanse waarden of JSON-objecten die de instelling vertegenwoordigen (bijv. `'dark'`, `'nl'`, `true`).