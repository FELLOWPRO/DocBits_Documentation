# Datenspeicherung, Aufbewahrung und Löschung

Ihre Daten sind bei DocBits gut aufgehoben. Wir betreiben DocBits in zwei Regionen, **Frankfurt am Main (EU)** und **San Francisco (USA)**, und Sie legen über Ihre Einstellungen selbst fest, wie lange Dokumente bei uns bleiben. Auf dieser Seite finden Sie alles Wichtige zu Speicherorten, Aufbewahrungsfristen und Löschung.

**Dokumentationsstand: 28. Oktober 2026.**

## Das Wichtigste in Kürze

- **Sie wählen die Region:** Frankfurt für EU-Kunden, San Francisco für US-Kunden.
- **Ihre Daten bleiben in Ihrer Region.** EU-Daten werden in Frankfurt gehostet, US-Daten in San Francisco. Es gibt keine regionsübergreifende Vermischung.
- **Sie steuern die Aufbewahrung Ihrer Dokumente** unter **Dokumentenverarbeitung → Dokumentenablauf** ([zur Einstellung](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Temporäre OCR-Dateien** werden nach 90 Minuten automatisch gelöscht.
- **Wir helfen persönlich weiter:** Fragen und Löschanfragen beantwortet Ihnen unser Team unter **compliance@fellowpro.com**.

## Wo werden Ihre Daten gespeichert?

| Region | Für wen | Standort | Eingesetzte Dienste |
| --- | --- | --- | --- |
| **EU** | Alle EU-Kunden | **Frankfurt am Main, Deutschland** | DigitalOcean Kubernetes (Region `fra1`) mit verwalteten PostgreSQL-, OpenSearch- und Valkey-Datenbanken (`fra1`) sowie DigitalOcean Spaces als Dateispeicher |
| **USA** | US-Kunden | **San Francisco, USA** | DigitalOcean Kubernetes (Region `sfo2`) mit verwalteten PostgreSQL-, OpenSearch- und Valkey-Datenbanken (`sfo2`) |

**Sicherungen in der EU:** Frankfurt ist der primäre Sicherungsstandort, Amsterdam (Niederlande) der sekundäre. So bleiben auch Ihre Sicherungskopien innerhalb der EU.

**Sicherungen in den USA:** Den Sicherungsstandort Ihrer US-Umgebung nennen wir Ihnen gern auf Anfrage über compliance@fellowpro.com.

**Angebundene Systeme:** Exportieren Sie Dokumente in Ihr ERP, nach Infor IDM oder in ein anderes Zielsystem, liegen die Kopien dort nach den Regeln und am Standort dieses Systems. Das behalten Sie in Ihrer eigenen Hand.

## Wie lange bleiben Daten erhalten?

| Datenart | Aufbewahrung |
| --- | --- |
| **Hochgeladene Dokumente und extrahierte Daten** | Von Ihnen steuerbar über den [Dokumentenablauf](../administration-and-setup/settings/document-processing/documents-expiry.md) (siehe unten). |
| **Temporäre OCR-Dateien** | Automatische Bereinigung nach **90 Minuten**. Das betrifft nur den temporären OCR-Speicher, nicht Ihr Dokument in DocBits. |
| **Für Kunden zugängliche Protokolle** (einsehbar unter [Aktivitätsprotokollierung](../administration-and-setup/settings/log-settings/README.md)) | **30 Tage** |
| **Interne Protokolle** | **3 Monate** |
| **Tägliche Datenbank-Backups (verwaltet)** | **7 Tage**, ältere Sicherungen werden automatisch entfernt. |
| **Zusätzliche tägliche Backups (SnapShooter)** | Für Produktions- und Sandbox-Datenbanken, Aufbewahrung je Umgebung festgelegt. |
| **Cookies und Browserspeicher** | Je nach Zweck unterschiedlich, siehe [Cookies und Browserspeicher](cookies-and-browser-storage.md). |

Zusätzlich sichern wir täglich, wöchentlich, vierteljährlich und jährlich. Die genauen Aufbewahrungsfristen dieser Sicherungsarten nennen wir Ihnen auf Anfrage für Ihre Umgebung.

## So legen Sie die Aufbewahrung Ihrer Dokumente fest

Öffnen Sie in den Einstellungen **Dokumentenverarbeitung → Dokumentenablauf**. Dort finden Sie zwei Einstellungen:

- **Delete document after:** Wie lange Dokumente aufbewahrt werden.
- **Delete finished document after:** Wie lange abgeschlossene, vollständig verarbeitete und exportierte Dokumente aufbewahrt werden.

Zur Auswahl stehen **Default**, **48 Hours**, **1 Week**, **2 Weeks** und **4 Weeks**. **Default** übernimmt den Systemstandard. Möchten Sie eine feste Frist, wählen Sie einfach einen der Zeiträume aus. Alle Details finden Sie in der [Anleitung zum Dokumentenablauf](../administration-and-setup/settings/document-processing/documents-expiry.md).

## Was passiert bei der Löschung?

Der Dokumentenablauf löscht Ihre Dokumente automatisch nach der gewählten Frist. Das ist unabhängig von der Bereinigung temporärer OCR-Dateien, vom Ablauf der Protokolle und von der Aufbewahrung der Sicherungen.

Gut zu wissen:

- **Sicherungen laufen nach ihrem eigenen Zeitplan aus.** Eine Löschung im Live-System entfernt Sicherungskopien also nicht sofort, sondern mit Ablauf der jeweiligen Backup-Frist.
- **Exportierte Kopien liegen bei Ihnen.** Löscht DocBits ein Dokument, bleibt die Kopie im ERP oder Archiv bestehen. Planen Sie die Aufbewahrung dort passend zu Ihren eigenen Vorgaben.

## Fragen oder Löschanfragen? Wir sind für Sie da

Für Auskünfte zu Ihrer Bereitstellung oder eine Löschanfrage schreiben Sie uns an **compliance@fellowpro.com**. Nennen Sie uns Ihre Organisation, die betroffene Umgebung, die Datenart und den gewünschten Umfang. Bitte senden Sie dabei keine Passwörter oder API-Schlüssel.

Gern bestätigen wir Ihnen auch:

- Ihre aktive Region und die wirksamen Aufbewahrungseinstellungen einschließlich des Systemstandards.
- Beginn der Löschfrist und Rhythmus der Bereinigung.
- Löschumfang für Dokumente, extrahierte Daten, Suchindizes und abgeleitete Daten.
- Standorte und Fristen aller Sicherungsarten, auch nach Vertragsende.

## Weitere Sicherheitsinformationen

- [Sicherheit und Compliance: Standorte, Protokolle und Aufbewahrung](security-and-compliance-faq.md)
- [Verschlüsselung gespeicherter Daten und Backup-Umfang](encryption-at-rest.md)
- [Sichere Speicherung von Zugangsdaten](secure-storage-of-credentials.md)
- [Cookies und Browserspeicher](cookies-and-browser-storage.md)
