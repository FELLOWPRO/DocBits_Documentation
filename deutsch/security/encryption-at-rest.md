---
description: Verschlüsselung gespeicherter DocBits-Daten bei DigitalOcean, einschließlich Datenbanken, Spaces und Backups.
---

# Verschlüsselung gespeicherter Daten

DocBits nutzt DigitalOcean Managed Databases und DigitalOcean Spaces. Die Prüfung am **16. Oktober 2026** bestätigte verwaltete PostgreSQL-, OpenSearch- und Valkey-Dienste für die EU-Produktion in Frankfurt. Die [Sicherheits- und Compliance-FAQ](../overview-and-basics/security-and-compliance-faq.md) dokumentiert die Nutzung von Spaces als Speicher.

Diese Seite beschreibt die von DigitalOcean veröffentlichten Verschlüsselungsmaßnahmen für diese Dienste. On-Premises-Installationen und Kopien in anderen Systemen erfordern eine eigene Bewertung.

## Verschlüsselungsverfahren und Geltungsbereich

| Speicherdienst | Verschlüsselung gespeicherter Daten | Geltungsbereich |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | LUKS-Verschlüsselung der gesamten Volumes; `aes-xts-plain64:sha256` mit 512 Bit XTS-Schlüsselmaterial | Die zugrunde liegenden Volumes des Datenbankdienstes einschließlich der darauf gespeicherten Daten. Dies schützt auf Speicherebene und bedeutet keine separate Verschlüsselung jedes Datenbankfeldes. |
| Backups von Managed Databases | AES-256 im CTR-Modus mit HMAC-SHA256 für die Integrität; Schlüssel pro Datei durch RSA-3072 geschützt | Vom verwalteten Datenbankdienst erstellte Backups. Zusätzliche Exporte und Sicherungskopien erfordern eine gesonderte Prüfung. |
| DigitalOcean Spaces | Vollständige Datenträgerverschlüsselung mit 256-Bit-AES-XTS | Daten auf den physischen Speichermedien. Dies ist von optionaler Verschlüsselung auf Objekt- oder Client-Ebene zu unterscheiden. |
| DigitalOcean Volumes, sofern eingesetzt | LUKS-Verschlüsselung des Speicherclusters | Daten auf diesen Blockspeichervolumes; Volume-Snapshots übernehmen die Verschlüsselung. |

XTS verwendet zwei AES-Schlüssel. Die zusammen 512 Bit XTS-Schlüsselmaterial des verwalteten Datenbankdienstes entsprechen zwei AES-Schlüsseln mit je 256 Bit (AES-256-XTS), keinem AES-Verfahren mit einem 512-Bit-Schlüssel.

Die Angaben zu Datenbanken und Backups stammen aus dem [Sicherheitsmodell für Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). Das [Sicherheitsmodell für Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) bestätigt die Verschlüsselung gespeicherter Daten; das [Sicherheitsmodell für App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) nennt 256-Bit-AES-XTS für die physischen Spaces-Datenträger. Die [Volume-Funktionen](https://docs.digitalocean.com/products/volumes/details/features/) beschreiben den Schutz von Volumes und Snapshots.

## Schlüsselverwaltung und berechtigte Zugriffe

DigitalOcean verwaltet die beschriebene Infrastrukturverschlüsselung. Für Managed Databases dokumentiert der Anbieter einen zufällig erzeugten Schlüssel je Instanz und Volume, der beim Löschen der Instanz verworfen wird. Backups verwalteter Datenbanken verwenden einen zufälligen Schlüssel pro Datei, geschützt durch ein dienstspezifisches RSA-Schlüsselpaar.

Speicherverschlüsselung schützt Daten auf Speichermedien. Berechtigte Anwendungen und Datenbankbenutzer können Daten weiterhin über den Dienst lesen. Daraus folgt weder, dass Mitarbeiter des Anbieters keine Kontoinformationen einsehen können, noch, dass jedes Feld auf Anwendungsebene verschlüsselt ist. Das Hashing von Anmeldepasswörtern und API-Schlüsseln ist eine gesonderte Maßnahme; siehe [Sichere Speicherung von Zugangsdaten](../overview-and-basics/secure-storage-of-credentials.md).

Spaces unterstützt außerdem [SSE-C mit kundenseitig bereitgestellten Schlüsseln](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Diese optionale Funktion belegt nicht, dass DocBits SSE-C oder kundenseitig verwaltete Verschlüsselungsschlüssel verwendet.

## Verschlüsselung von Backups

Backups der DigitalOcean Managed Databases werden mit AES-256-CTR verschlüsselt und durch HMAC-SHA256 gegen unbemerkte Änderungen geschützt. Die dateispezifischen Verschlüsselungsschlüssel sind durch RSA-3072 abgesichert. Volume-Snapshots übernehmen die Verschlüsselung des zugrunde liegenden DigitalOcean-Volumes. Diese Angaben beschreiben die Sicherungsfunktionen der genannten verwalteten Dienste.

## Arten der Verschlüsselung gespeicherter Daten

Die wichtigsten Verschlüsselungsverfahren der genannten Dienste im Überblick:

> DocBits nutzt DigitalOcean Managed Databases und Spaces. Gespeicherte Daten verwalteter Datenbanken werden auf Ebene der gesamten Volumes mit LUKS und AES-256-XTS verschlüsselt (zusammen 512 Bit XTS-Schlüsselmaterial). Backups verwalteter Datenbanken verwenden AES-256-CTR mit HMAC-SHA256 zur Integritätssicherung und RSA-3072 zum Schutz der dateispezifischen Verschlüsselungsschlüssel. Spaces verwendet vollständige Datenträgerverschlüsselung mit 256-Bit-AES-XTS auf den physischen Speichermedien.
>
> Diese Maßnahmen auf Speicherebene schützen die Daten auf den betreffenden Volumes und Datenträgern; sie bedeuten keine separate Verschlüsselung jedes Datenbankfeldes. DigitalOcean verwaltet die Infrastruktur-Verschlüsselungsschlüssel. Diese Aussage umfasst die genannten verwalteten Dienste.
