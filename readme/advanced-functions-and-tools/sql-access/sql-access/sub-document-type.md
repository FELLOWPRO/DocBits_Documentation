# Dokumentuntertyp

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_type_key`: intern
* `sub_doc_type_key`: intern
* `name`: intern
* `title`: intern
* `translation_key`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Tabelle `public.sub_document_type`

## Einführung

Die Tabelle `sub_document_type` speichert detaillierte Informationen zu verschiedenen Dokumentuntertypen innerhalb einer Organisation. Dazu gehören eindeutige Kennungen, Organisationszuordnungen, beschreibende Namen und Metadaten zur Erstellung und Änderung dieser Dokumentuntertypen. Die Tabelle pflegt außerdem den Status des logischen Löschens (Soft Delete) für Datensätze.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Diese Spalte speichert die eindeutige Kennung für jeden Dokumentuntertyp.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die einen Dokumentuntertyp-Datensatz eindeutig identifiziert (z. B. `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Bedeutung**: Diese Spalte gibt die Organisation an, zu der der Dokumentuntertyp gehört.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Organisation verweist (z. B. `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Bedeutung**: Stellt den Dokumenttyp-Schlüssel dar, der dem Dokumentuntertyp zugeordnet ist.
- **Rolle**: Fremdschlüssel (durch die Namenskonvention impliziert).
- **Typischer Inhalt**: Ein Zeichenfolgen-Schlüssel, der auf einen übergeordneten Dokumenttyp verweist (z. B. `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Bedeutung**: Bezeichnet einen spezifischen Schlüssel für den Dokumentuntertyp innerhalb einer Dokumentkategorie.
- **Rolle**: Eindeutige Kennung für den Dokumentuntertyp im Geltungsbereich eines Dokumenttyps.
- **Typischer Inhalt**: Ein Zeichenfolgen-Schlüssel, der einen Dokumentuntertyp eindeutig identifiziert (z. B. `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Bedeutung**: Speichert einen Kurznamen oder Code für den Dokumentuntertyp.
- **Rolle**: Beschreibend.
- **Typischer Inhalt**: Eine prägnante Kennung oder ein Code (z. B. `'TEST_SUB_TEST'`).

### title
- **Bedeutung**: Enthält einen gut lesbaren Titel für den Dokumentuntertyp.
- **Rolle**: Beschreibend.
- **Typischer Inhalt**: Ein beschreibender Titel für Benutzeroberflächen oder Berichte (z. B. `'Test Sub Test'`).

### translation_key
- **Bedeutung**: Schlüssel für Internationalisierung und Lokalisierung, mit dem der Name des Dokumentuntertyps übersetzt wird.
- **Rolle**: Technisch.
- **Typischer Inhalt**: Eine Zeichenfolge, die in Übersetzungsdateien verwendet wird (z. B. `'test_sub_test'`).

### created_by
- **Bedeutung**: Identifiziert den Benutzer, der den Dokumentuntertyp-Eintrag erstellt hat.
- **Rolle**: Technisch.
- **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt (z. B. `8`).

### created_on
- **Bedeutung**: Zeitstempel, der angibt, wann der Dokumentuntertyp erstellt wurde.
- **Rolle**: Technisch.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone (z. B. `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Bedeutung**: Zeitstempel, der angibt, wann der Dokumentuntertyp zuletzt geändert wurde.
- **Rolle**: Technisch.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, möglicherweise `None`, wenn nach der Erstellung nie geändert.

### is_deleted
- **Bedeutung**: Boolesches Kennzeichen, das angibt, ob der Dokumentuntertyp logisch gelöscht wurde.
- **Rolle**: Technisch.
- **Typischer Inhalt**: `True` oder `False`, das den Löschstatus angibt (z. B. `False`).
```
