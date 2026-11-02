# FTP-Importkonfigurationen

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `sub_org_id`: intern
* `server_url`: intern
* `username`: intern
* `password`: intern
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `port`: integer
* `default_directory`: intern
* `ftp_type`: intern
* `token`: intern
* `file_name_matching_patterns`: intern
* `last_mtime`: intern
* `auth_failed_count`: integer
* `auth_message`: text
* `ignore_certificate`: boolean
* `move_after_import`: boolean
* `destination_directory`: intern
* `import_directory`: intern
* `include_subfolder_content`: boolean

## Analyse & Beschreibung

```markdown
# Dokumentation der Tabelle FTP Import Configurations

## Einführung

Die Tabelle `public.ftp_import_configurations` speichert Konfigurationsdetails für FTP-Importprozesse. Sie enthält die Informationen, die für die Verbindung zu FTP-Servern, die Verwaltung der Authentifizierung und die Verarbeitung von Dateiimporten erforderlich sind. Sie unterstützt sowohl das FTP- als auch das SFTP-Protokoll und umfasst Felder für FTP-Server-Details, Anmeldedaten und Betriebseinstellungen, etwa ob Dateien nach dem Import verschoben werden und ob der Inhalt von Unterordnern einbezogen wird.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jeden Datensatz einer FTP-Importkonfiguration.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: UUID-Format, z. B. `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Bedeutung**: Kennung der Organisation, der diese Konfiguration zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: UUID-Format.

### sub_org_id
- **Bedeutung**: Kennung einer Unterorganisation, falls zutreffend.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: UUID-Format oder `null`, falls nicht zutreffend.

### server_url
- **Bedeutung**: Die URL oder IP-Adresse des FTP-Servers.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Domainname oder IP-Adresse, z. B. `sftp.it.doxee.com`.

### username
- **Bedeutung**: Benutzername für die Authentifizierung am FTP-Server.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Benutzername im Klartext.

### password
- **Bedeutung**: Passwort für die Authentifizierung am FTP-Server.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Verschlüsselte Passwort-Zeichenfolge.

### is_active
- **Bedeutung**: Gibt an, ob die Konfiguration derzeit aktiv ist.
- **Rolle**: Statuskennzeichen.
- **Typischer Inhalt**: `True` oder `False`.

### created_by
- **Bedeutung**: Kennung des Benutzers, der die Konfiguration erstellt hat.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung der Konfiguration.
- **Rolle**: Audit-Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung der Konfiguration.
- **Rolle**: Audit-Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.

### is_deleted
- **Bedeutung**: Gibt an, ob die Konfiguration als gelöscht markiert wurde.
- **Rolle**: Statuskennzeichen.
- **Typischer Inhalt**: `True` oder `False`.

### deleted_on
- **Bedeutung**: Zeitstempel, wann die Konfiguration als gelöscht markiert wurde.
- **Rolle**: Audit-Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation oder ein Standarddatum für nicht gelöschte Datensätze.

### port
- **Bedeutung**: Portnummer für die Verbindung zum FTP-Server.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, z. B. `22` für SFTP.

### default_directory
- **Bedeutung**: Der Standardverzeichnispfad auf dem FTP-Server.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge mit dem Verzeichnispfad.

### ftp_type
- **Bedeutung**: Typ des verwendeten FTP-Protokolls (z. B. FTP, SFTP).
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: `FTP` oder `SFTP`.

### token
- **Bedeutung**: Sicherheits-Token für zusätzliche Authentifizierung oder Identifizierung.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Verschlüsselte oder codierte Zeichenfolge.

### file_name_matching_patterns
- **Bedeutung**: Muster, mit denen Dateinamen für den Import abgeglichen werden.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Musterzeichenfolgen oder `null`.

### last_mtime
- **Bedeutung**: Zeitpunkt der letzten Änderung von Dateien, der zum Filtern von Importen verwendet wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge, die einen Zeitstempel darstellt, oder `null`.

### auth_failed_count
- **Bedeutung**: Zähler für fehlgeschlagene Authentifizierungsversuche.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, z. B. `0` oder `5`.

### auth_message
- **Bedeutung**: Meldung, die das Ergebnis des letzten Authentifizierungsversuchs beschreibt.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Textmeldung oder `null`.

### ignore_certificate
- **Bedeutung**: Gibt an, ob die Validierung des SSL-Zertifikats ignoriert werden soll.
- **Rolle**: Statuskennzeichen.
- **Typischer Inhalt**: `True` oder `False`.

### move_after_import
- **Bedeutung**: Gibt an, ob Dateien nach Abschluss des Imports verschoben werden sollen.
- **Rolle**: Statuskennzeichen.
- **Typischer Inhalt**: `True` oder `False`.

### destination_directory
- **Bedeutung**: Verzeichnispfad, in das Dateien nach dem Import verschoben werden sollen.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge mit dem Verzeichnispfad oder `null`.

### import_directory
- **Bedeutung**: Verzeichnispfad, aus dem Dateien importiert werden.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge mit dem Verzeichnispfad oder `null`.

### include_subfolder_content
- **Bedeutung**: Gibt an, ob der Inhalt von Unterordnern in den Import einbezogen werden soll.
- **Rolle**: Statuskennzeichen.
- **Typischer Inhalt**: `True` oder `False`.
```

Diese Dokumentation vermittelt ein umfassendes Verständnis jeder Spalte der Tabelle `public.ftp_import_configurations` und erläutert auf Grundlage der vorliegenden Daten und Spaltennamen deren Zweck, Rolle und typischen Inhalt.
