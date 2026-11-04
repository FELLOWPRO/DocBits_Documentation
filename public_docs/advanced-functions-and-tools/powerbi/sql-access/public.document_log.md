# Documentlogboek

## Tabel `public.document_log`

### Kolommen

* `id`: intern
* `document_id`: intern
* `message`: intern
* `created_on`: tijdstempel met tijdzone
* `created_by`: intern
* `log_level`: intern

### Analyse & Beschrijving

## Technische documentatie voor `public.document_log` tabel

### Inleiding

De `public.document_log` tabel dient als een auditlogboek voor activiteiten en gebeurtenissen met betrekking tot documenten. Het legt berichten, tijdstempels en gebruikersacties vast, wat essentieel is voor het volgen van de documentgeschiedenis en het oplossen van problemen.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de logboekvermelding.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden.

#### document\_id

* **Betekenis**: De identificatie van het document waarop de logboekvermelding betrekking heeft.
* **Rol**: Vreemde sleutel, verwijzend naar de documententabel.
* **Typische inhoud**: UUID-waarden.

#### message

* **Betekenis**: De inhoud van het logboekbericht of de beschrijving van de gebeurtenis.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekstuele beschrijvingen van acties, fouten of statuswijzigingen (bijv. "Document geüpload", "Validatie mislukt").

#### created\_on

* **Betekenis**: De datum en tijd waarop de logboekvermelding is gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels met tijdzone.

#### created\_by

* **Betekenis**: De gebruiker of het systeemproces dat de logboekvermelding heeft gegenereerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID of systeemidentificatie.

#### log\_level

* **Betekenis**: Het ernstniveau of de categorie van het logboekbericht.
* **Rol**: Classificatieveld.
* **Typische inhoud**: Waarden zoals `'INFO'`, `'WARNING'`, `'ERROR'`.