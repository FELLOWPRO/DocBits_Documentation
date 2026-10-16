---
description: Passwort-Hashing, Speicherung von API-Schlüsseln, TLS, Einsicht in Zugangsdaten und Kontowiederherstellung in DocBits.
---

# Sichere Speicherung von Zugangsdaten

DocBits behandelt Anmeldepasswörter, DocBits-API-Schlüssel, Kontoinformationen und Zugangsdaten für angebundene Systeme entsprechend ihrem jeweiligen Zweck. Diese Seite beschreibt, wie die einzelnen Kategorien geschützt werden und wie der Zugang wiederhergestellt werden kann.

## Anmeldepasswörter

DocBits speichert Anmeldepasswörter als **gesalzene Einweg-Hashes**. Bei der Anmeldung wird das eingegebene Passwort mit dem gespeicherten Hash geprüft. Das ursprüngliche Passwort wird nicht in einer Form gespeichert, die entschlüsselt und ausgelesen werden kann.

Administratoren und der DocBits-Support können das bestehende Klartextpasswort daher nicht aus dem gespeicherten Passwort-Hash abrufen. Wenn ein Passwort vergessen wurde, muss es zurückgesetzt werden, um sich wieder mit einem Passwort anzumelden.

### Passwort zurücksetzen

1. Wählen Sie auf der Anmeldeseite **Passwort vergessen?**.
2. Geben Sie die E-Mail-Adresse des Kontos ein.
3. Öffnen Sie den Link zum Zurücksetzen, der an diese Adresse gesendet wurde.
4. Legen Sie ein neues Passwort fest und melden Sie sich damit an.

Links zum Zurücksetzen laufen ab. Fordern Sie bei einem abgelaufenen Link einen neuen an. Das Verfahren legt ein neues Passwort fest und zeigt das bisherige nicht an. Die vollständige Anleitung finden Sie unter [Zugang erhalten und anmelden](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

Konten mit eingerichtetem SSO oder Passkey können diese alternative Anmeldemethode verwenden. Bei SSO erfolgt die Passwortwiederherstellung über den Identitätsanbieter. Siehe [Zwei-Faktor-Authentifizierung](two-factor-authentication.md).

## DocBits-API-Schlüssel

API-Schlüssel aus der **API-Schlüsselverwaltung** werden nur einmal vollständig angezeigt: bei ihrer Erstellung. DocBits speichert einen Einweg-Hash des Schlüssels und ein kurzes Präfix zur Identifizierung. Präfix und Metadaten bleiben in der Verwaltungsliste sichtbar; der ursprüngliche vollständige Schlüssel lässt sich nicht aus seinem Hash abrufen.

Weder Administratoren noch der DocBits-Support können den vollständigen Schlüssel nach der Erstellung erneut abrufen. Wenn ein Schlüssel verloren geht, widerrufen Sie ihn und erstellen Sie einen Ersatz. Einzelne Schlüssel können ein Ablaufdatum haben und separat widerrufen werden. Siehe [API-Schlüsselverwaltung](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Kontodaten und Zugangsdaten für angebundene Systeme

Namen, E-Mail-Adressen, Rollen und Kontostatus sind Kontoinformationen, die berechtigte Organisationsadministratoren einsehen und verwalten können. Sie sind vom geheimen Anmeldemittel zu unterscheiden. Siehe [Benutzer](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Zugangsdaten für angebundene Systeme, etwa ein ERP-Dienstkonto, ein Postfach oder einen SFTP-Server, sind ebenfalls von einem DocBits-Anmeldepasswort oder einem von DocBits ausgestellten API-Schlüssel zu unterscheiden. Ein Konnektor kann das nutzbare Geheimnis benötigen, um sich am externen System anzumelden. Speicherung und Zugriffskontrollen müssen deshalb für den jeweiligen Konnektor beurteilt werden.

Dass ein Anmeldepasswort oder ein gehashter DocBits-API-Schlüssel nicht wieder abgerufen werden kann, bedeutet **nicht**, dass sämtliche Kontoinformationen oder Integrationsgeheimnisse für den Anbieter unzugänglich sind. Aussagen zum Zugriff von Mitarbeitern auf Integrationszugangsdaten erfordern eine Bestätigung der jeweiligen betrieblichen Zugriffskontrollen.

## Verschlüsselung bei der Übertragung

Die folgenden öffentlichen DocBits-Endpunkte unterstützen **TLS 1.2 und TLS 1.3** über HTTPS. Prüfungen am **16. Oktober 2026** bestätigten, dass TLS 1.0 und TLS 1.1 abgewiesen wurden.

| Endpunkt | Zweck | Bestätigte TLS-Versionen |
| --- | --- | --- |
| `app.docbits.com` | Webanwendung | TLS 1.2 und TLS 1.3 |
| `auth.docbits.com` | Authentifizierungsdienst | TLS 1.2 und TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 und TLS 1.3 |

### Welche Verschlüsselungsverfahren werden bei der Übertragung unterstützt?

| Frage | Antwort für die oben genannten öffentlichen Endpunkte |
| --- | --- |
| Wird TLS 1.1 unterstützt? | **Nein.** Verbindungen mit TLS 1.1 werden abgewiesen. |
| Wird TLS 1.2 unterstützt? | **Ja.** |
| Wird TLS 1.3 unterstützt? | **Ja.** |

Die folgenden Verschlüsselungsverfahren wurden am 16. Oktober 2026 in Tests mit Zertifikatsprüfung auf **allen drei Endpunkten** erfolgreich ausgehandelt:

| Verschlüsselungsverfahren | Symmetrische Schlüssellänge | Geprüfte TLS-Versionen |
| --- | --- | --- |
| AES-128-GCM | 128 Bit | TLS 1.2 und TLS 1.3 |
| AES-256-GCM | 256 Bit | TLS 1.2 und TLS 1.3 |
| ChaCha20-Poly1305 | 256 Bit | TLS 1.3 |

Diese Verfahren bieten authentifizierte Verschlüsselung und schützen Vertraulichkeit und Integrität der übertragenen Daten. Das ausgehandelte Verfahren hängt von den Fähigkeiten und der Konfiguration von Client und Server ab. Die Bitangaben beziehen sich auf die symmetrischen Schlüssel zur Datenverschlüsselung, unabhängig von den Schlüssellängen der Zertifikate. Die getesteten TLS-1.2-Cipher-Suites verwenden ECDHE für den Austausch temporärer Schlüssel.

Die Prüfung umfasst Verbindungen zu diesen öffentlichen Endpunkten, auch wenn andere Server die Verbindung herstellen. Sie belegt nicht die Protokoll- oder Verschlüsselungseinstellungen jeder internen Dienstverbindung, Datenbankverbindung, jedes regionalen Endpunkts oder jeder externen Integration. Diese Verbindungen müssen für die jeweilige Bereitstellung und Integration gesondert bestätigt werden.

## Verschlüsselung gespeicherter Kontoinformationen

DigitalOcean Managed Databases verwenden LUKS-Verschlüsselung der gesamten Volumes mit AES-256-XTS; ihre verwalteten Backups verwenden AES-256-CTR. Spaces nutzt 256-Bit-AES-XTS auf physischen Datenträgern. [Verschlüsselung gespeicherter Daten](../security/encryption-at-rest.md) beschreibt Verfahren, Schlüsselverwaltung und Backup-Umfang.

Das Hashing von Passwörtern und API-Schlüsseln ist eine andere Schutzmaßnahme als die Verschlüsselung von Datenbanken, Speichervolumes, Objekten und Backups. Die oben beschriebenen Maßnahmen belegen weder, dass jeder Benutzername, jedes Kontofeld oder jedes Integrationsgeheimnis einzeln verschlüsselt wird, noch, dass alle gespeicherten Daten einen bestimmten Verschlüsselungsalgorithmus verwenden.

Wenn eine Anforderung sämtliche Kundenkontoinformationen umfasst, benötigen Sie eine Aussage von FELLOWPRO AG zur konkreten Bereitstellung, die die relevanten Datenspeicher und Backups, Verschlüsselungsverfahren, Schlüsselverwaltung und Mitarbeiterzugriffe abdeckt. Ein Cloud- oder Serverless-Betriebsmodell allein belegt diese Eigenschaften nicht.

## Antwort für einen Sicherheitsfragebogen

Die folgende Formulierung beschreibt den bestätigten Umfang:

> DocBits speichert Anmeldepasswörter als gesalzene Einweg-Hashes. Administratoren und der DocBits-Support können das ursprüngliche Klartextpasswort nicht aus dem gespeicherten Hash abrufen. Wer sein Passwort vergessen hat, muss über das Zurücksetzen per E-Mail ein neues festlegen, um sich wieder mit einem Passwort anzumelden. Eingerichtetes SSO oder Passkeys bieten alternative Anmeldemöglichkeiten.
>
> API-Schlüssel aus der DocBits-API-Schlüsselverwaltung werden nur einmal angezeigt und als Einweg-Hashes gespeichert. Weder Administratoren noch der DocBits-Support können den vollständigen Schlüssel danach erneut abrufen. Verlorene Schlüssel müssen widerrufen und ersetzt werden.
>
> Die oben genannten öffentlichen Endpunkte für Webanwendung, Authentifizierung und API unterstützen HTTPS mit TLS 1.2 und TLS 1.3. TLS 1.0 und TLS 1.1 wurden bei den Prüfungen am 16. Oktober 2026 abgewiesen. Bestätigte Verschlüsselungsverfahren sind AES-128-GCM mit 128 Bit und AES-256-GCM mit 256 Bit unter TLS 1.2 und TLS 1.3 sowie ChaCha20-Poly1305 mit 256 Bit unter TLS 1.3. Diese Aussage gilt für Verbindungen zu diesen Endpunkten. Die Verschlüsselung sämtlicher gespeicherter Kontoinformationen und Backups, der Schutz jeder internen Serververbindung und Mitarbeiterzugriffe auf Zugangsdaten externer Integrationen erfordern eine gesonderte Bestätigung für die jeweilige Bereitstellung.
