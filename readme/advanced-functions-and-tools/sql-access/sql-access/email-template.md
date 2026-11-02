# E-Mail-Vorlage

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `name`: intern
* `email_type`: intern
* `value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `subject`: intern
* `last_modified_by`: intern
* `deleted_by`: intern
* `doc_type`: Dokumenttyp

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.email_template`

## Einführung

Die Tabelle `public.email_template` speichert E-Mail-Vorlagen, die im System verwendet werden. Diese Vorlagen sind verschiedenen Organisationen zugeordnet und dienen vermutlich dem Versand standardisierter E-Mail-Kommunikation. Die Tabelle enthält Metadaten zu den Vorlagen, einschließlich Angaben zu Erstellung und Änderung, und verfolgt außerdem, ob eine Vorlage gelöscht wurde.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jede E-Mail-Vorlage.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge wie `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Hinweis**: Dient als Hauptkennung des Vorlagendatensatzes.

### org_id
- **Bedeutung**: Kennung der Organisation, der die E-Mail-Vorlage zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge.
- **Hinweis**: Verknüpft die Vorlage mit einer bestimmten Organisation.

### name
- **Bedeutung**: Der Name der E-Mail-Vorlage.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Beschreibender Text wie `Supplier Magic Link Email`.
- **Hinweis**: Dient zur Identifizierung des Verwendungszwecks der Vorlage.

### email_type
- **Bedeutung**: Typ oder Kategorie der E-Mail-Vorlage.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen wie `supplier_invite`.
- **Hinweis**: Gibt den Kontext oder die Verwendung der Vorlage an.

### value
- **Bedeutung**: Der Inhalt der E-Mail-Vorlage, üblicherweise im HTML-Format.
- **Rolle**: Inhaltsfeld.
- **Typischer Inhalt**: HTML-Zeichenfolge mit Layout und Inhalt der E-Mail.
- **Hinweis**: Dies ist die eigentliche Vorlage, die in E-Mails verwendet wird.

### created_by
- **Bedeutung**: Kennung des Benutzers, der die Vorlage erstellt hat.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Eine Ganzzahl, die eine Benutzer-ID darstellt.
- **Hinweis**: Verfolgt, wer die Vorlage erstellt hat.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung der Vorlage.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Ein Zeitstempel wie `2024-07-18 13:29:59 UTC`.
- **Hinweis**: Hält Datum und Uhrzeit der Erstellung fest.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung der Vorlage.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Ein Zeitstempel.
- **Hinweis**: Verfolgt die letzte Aktualisierung der Vorlage.

### is_deleted
- **Bedeutung**: Gibt an, ob die Vorlage als gelöscht markiert ist.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert, `True` oder `False`.
- **Hinweis**: Dient zum logischen Löschen (Soft Delete) der Vorlage.

### deleted_on
- **Bedeutung**: Zeitstempel, wann die Vorlage als gelöscht markiert wurde.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Ein Zeitstempel oder `None`, wenn nicht gelöscht.
- **Hinweis**: Hält fest, wann die Vorlage gelöscht wurde.

### subject
- **Bedeutung**: Die Betreffzeile der E-Mail-Vorlage.
- **Rolle**: Inhaltsfeld.
- **Typischer Inhalt**: Text wie `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Hinweis**: Wird als E-Mail-Betreff verwendet, wenn die Vorlage versendet wird.

### last_modified_by
- **Bedeutung**: Kennung des Benutzers, der die Vorlage zuletzt geändert hat.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Eine Benutzerkennung.
- **Hinweis**: Verfolgt, wer die Vorlage zuletzt geändert hat.

### deleted_by
- **Bedeutung**: Kennung des Benutzers, der die Vorlage als gelöscht markiert hat.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Eine Benutzerkennung.
- **Hinweis**: Hält fest, wer die Vorlage gelöscht hat.

### doc_type
- **Bedeutung**: Typ oder Format des Dokuments, das zur Vorlage gehört.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen, die den Dokumenttyp angeben.
- **Hinweis**: Kann sich auf das Format oder die Kategorie des E-Mail-Inhalts beziehen.
```
