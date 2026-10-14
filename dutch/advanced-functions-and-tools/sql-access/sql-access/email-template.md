# Email template

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `name`: intern
* `email_type`: intern
* `value`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `subject`: intern
* `last_modified_by`: intern
* `deleted_by`: intern
* `doc_type`: DOC-type

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.email_template`

## Inleiding

De tabel `public.email_template` is ontworpen om e-mailtemplates op te slaan die binnen het systeem worden gebruikt. Deze templates zijn gekoppeld aan verschillende organisaties en worden waarschijnlijk gebruikt om gestandaardiseerde e-mailcommunicatie te verzenden. De tabel bevat metadata over de templates, inclusief details over aanmaak en wijziging, en houdt ook bij of een template is verwijderd.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identificatie voor elke e-mailtemplate.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een UUID-reeks zoals `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Opmerking**: Dit dient als de belangrijkste identificatie voor het templaterecord.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan de e-mailtemplate is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks.
- **Opmerking**: Koppelt de template aan een specifieke organisatie.

### name
- **Betekenis**: De naam van de e-mailtemplate.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Beschrijvende tekst zoals `Supplier Magic Link Email`.
- **Opmerking**: Wordt gebruikt om het doel van de template te identificeren.

### email_type
- **Betekenis**: Type of categorie van de e-mailtemplate.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeksen zoals `supplier_invite`.
- **Opmerking**: Geeft de context of het gebruik van de template aan.

### value
- **Betekenis**: De inhoud van de e-mailtemplate, meestal in HTML-formaat.
- **Rol**: Inhoudsveld.
- **Typische Inhoud**: HTML-reeks met de lay-out en inhoud van de e-mail.
- **Opmerking**: Dit is de feitelijke template die in e-mails wordt gebruikt.

### created_by
- **Betekenis**: Identificatie voor de gebruiker die de template heeft aangemaakt.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een integer die een gebruikers-ID vertegenwoordigt.
- **Opmerking**: Houdt bij wie de template heeft gemaakt.

### created_on
- **Betekenis**: Tijdstempel van wanneer de template is aangemaakt.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een tijdstempel zoals `2024-07-18 13:29:59 UTC`.
- **Opmerking**: Registreert de datum en tijd van aanmaak.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging van de template.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een tijdstempel.
- **Opmerking**: Volgt de meest recente update van de template.

### is_deleted
- **Betekenis**: Geeft aan of de template als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde, `True` of `False`.
- **Opmerking**: Wordt gebruikt voor soft-deletion van de template.

### deleted_on
- **Betekenis**: Tijdstempel van wanneer de template als verwijderd is gemarkeerd.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een tijdstempel of `None` indien niet verwijderd.
- **Opmerking**: Registreert wanneer de template is verwijderd.

### subject
- **Betekenis**: De onderwerpregel van de e-mailtemplate.
- **Rol**: Inhoudsveld.
- **Typische Inhoud**: Tekst zoals `Welkom bij het Testing Ruiz Foods Supplier Portal. We helpen u graag bij het instellen`.
- **Opmerking**: Wordt gebruikt als e-mailonderwerp wanneer de template wordt verzonden.

### last_modified_by
- **Betekenis**: Identificatie voor de gebruiker die de template voor het laatst heeft gewijzigd.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een gebruikersidentificatie.
- **Opmerking**: Houdt bij wie de template voor het laatst heeft gewijzigd.

### deleted_by
- **Betekenis**: Identificatie voor de gebruiker die de template als verwijderd heeft gemarkeerd.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een gebruikersidentificatie.
- **Opmerking**: Registreert wie de template heeft verwijderd.

### doc_type
- **Betekenis**: Type of formaat van het document gerelateerd aan de template.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeksen die het documenttype aangeven.
- **Opmerking**: Zou gerelateerd kunnen zijn aan het formaat of de categorie van de e-mailinhoud.
```
