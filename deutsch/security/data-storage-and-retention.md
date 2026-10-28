# Datenspeicherung, Aufbewahrung und Löschung

Wo DocBits Daten speichert und wann sie gelöscht werden, hängt von der Datenart, der gebuchten Region und den Einstellungen Ihrer Organisation ab. Dokumente, temporäre OCR-Dateien, Protokolle und Backups haben unterschiedliche Aufbewahrungsregeln.

**Dokumentationsstand: 27. Oktober 2026.** Diese Übersicht führt die vorhandenen Sicherheits- und Betriebsangaben zusammen. Sie bestätigt keine individuelle Mandantenkonfiguration. Maßgeblich für Ihre Bereitstellung sind die vereinbarten Leistungen und Aufbewahrungsregeln.

## Wo werden die Daten gespeichert?

| Bereich | Speicherort und Dienste |
| --- | --- |
| EU-Produktionsumgebung | DigitalOcean in **Frankfurt am Main, Deutschland**. DocBits nutzt DigitalOcean Spaces als Dateispeicher sowie verwaltete PostgreSQL-, OpenSearch- und Valkey-Dienste. |
| Sicherungen und Wiederherstellung der EU-Umgebung | Die [Sicherheits- und Compliance-FAQ](security-and-compliance-faq.md) nennt **Frankfurt** als primären und **Amsterdam, Niederlande**, als sekundären Sicherungsstandort. |
| US-Bereitstellung | Die FAQ nennt **New York, USA**, für US-Kunden. Diese Region ist von der EU-Bereitstellung zu unterscheiden. |
| Angebundene Systeme | Nach einem Export liegen weitere Kopien gegebenenfalls im ERP, in Infor IDM oder in einem anderen Zielsystem. Dessen Speicherort und Löschregeln werden durch die jeweilige Bereitstellung bestimmt. |

Frankfurt bezeichnet den produktiven Speicherort der EU-Umgebung; Sicherungskopien können am dokumentierten zweiten EU-Standort Amsterdam liegen. Daraus folgt keine pauschale Standortzusage für jedes zusätzlich angebundene System oder jeden optionalen Dienst.

## Wann werden Daten gespeichert und wie lange bleiben sie erhalten?

| Datenart | Wann sie entsteht oder gespeichert wird | Aufbewahrung und Löschung |
| --- | --- | --- |
| Hochgeladene Dokumente und extrahierte Daten | Beim Import und während der Verarbeitung, zum Beispiel bei OCR, Extraktion, Prüfung und Export. | Die Aufbewahrung wird über die Organisationseinstellungen gesteuert. Unter **Dokumentenablauf** gibt es getrennte Einstellungen für Dokumente und abgeschlossene Dokumente. Prüfen Sie die tatsächlich gewählten Werte; eine allgemeine Frist von 30 Tagen oder 3 Monaten beschreibt nicht alle dokumentierten Optionen. |
| Temporäre Dateien des OCR-Dienstes | Während der OCR-Verarbeitung wird eine verarbeitete Datei vorübergehend zum Abruf bereitgestellt. | Die Betriebsdokumentation beschreibt eine automatische Bereinigung **nach 90 Minuten**. Diese Frist betrifft den temporären OCR-Speicher, nicht die Aufbewahrung des importierten Dokuments in DocBits. |
| Für Kunden zugängliche Protokolle | Bei protokollierten Verarbeitungs- und Zugriffsereignissen. | Laut Sicherheits- und Compliance-FAQ **30 Tage**. |
| Interne Protokolle | Bei internen Betriebs- und Diagnoseereignissen. | Laut Sicherheits- und Compliance-FAQ **3 Monate**. Diese Angabe ist keine Frist für sämtliche optionalen Analyse- oder Überwachungsdienste. |
| Verwaltete Datenbank-Backups | Die Betriebsdokumentation beschreibt tägliche automatische Sicherungen. | Für diese Sicherungsart sind **7 Tage** dokumentiert; ältere Sicherungen werden automatisch entfernt. Die Frist gilt nicht automatisch für zusätzliche Sicherungsarten. |
| Zusätzliche Datenbank-Sicherungen | Für Produktions- und Sandbox-Datenbanken sind zusätzliche tägliche Sicherungen über SnapShooter dokumentiert. | Die Aufbewahrung wird **je Umgebung** festgelegt. Eine einheitliche Tageszahl ist dafür nicht dokumentiert. |
| Cookies und Browserspeicher | Bei Website-Besuch, Anmeldung und Nutzung der Anwendung. | Je nach Zweck unterschiedlich. Siehe die gesonderte Übersicht [Cookies und Browserspeicher](cookies-and-browser-storage.md). |

Die FAQ nennt darüber hinaus tägliche, wöchentliche, vierteljährliche und jährliche Sicherungen. Ein Sicherungsintervall beschreibt, **wie oft** gesichert wird; es sagt nicht, **wie lange** jede Kopie erhalten bleibt. Für den vollständigen Sicherungsumfang Ihrer Umgebung müssen die jeweiligen Aufbewahrungsfristen gesondert bestätigt werden.

## Wie prüfe ich die Aufbewahrung meiner Dokumente?

Öffnen Sie in den Einstellungen **Dokumentenverarbeitung → Dokumentenablauf**. Je nach Oberflächensprache heißen die Einstellungen:

- **Delete document after:** Aufbewahrung von Dokumenten.
- **Delete finished document after:** Aufbewahrung abgeschlossener, vollständig verarbeiteter und exportierter Dokumente.

Die [Anleitung zum Dokumentenablauf](../administration-and-setup/settings/document-processing/documents-expiry.md) beschreibt die Optionen **Default**, **48 Hours**, **1 Week**, **2 Weeks** und **4 Weeks**. **Default** übernimmt den Systemstandard; die Bezeichnung allein nennt keine konkrete Dauer. Lassen Sie den wirksamen Standard für Ihre Organisation bestätigen, wenn kein ausdrücklicher Zeitraum ausgewählt ist.

Für eine verbindliche Löschplanung müssen außerdem der Beginn der Frist und der Ausführungsrhythmus der automatischen Bereinigung geklärt sein. Aus der gewählten Dauer allein lässt sich kein sekundengenauer Löschzeitpunkt ableiten.

## Was bedeutet die Löschung in DocBits?

Die automatische Dokumentenlöschung wird durch den konfigurierten Dokumentenablauf gesteuert. Sie ist von der Bereinigung temporärer OCR-Dateien, dem Ablauf von Protokollen und der Aufbewahrung von Sicherungskopien zu unterscheiden.

**Eine Löschung im produktiven System belegt nicht, dass im selben Moment jede Sicherungskopie entfernt wurde.** Der genaue Löschumfang für Dateispeicher, Suchindizes, abgeleitete Daten und Backups muss für die jeweilige Bereitstellung bestätigt werden. Die verfügbaren Angaben belegen auch keine einheitliche Löschfrist für Benutzerkonten, Stammdaten, Konfigurationen oder Trainingsdaten.

Ein Export in ein ERP oder Archiv ist ebenfalls kein Nachweis, dass die DocBits-Kopie bereits gelöscht wurde. Umgekehrt entfernt eine Löschung in DocBits keine separat gespeicherten Kopien in angebundenen Systemen. Planen Sie die Aufbewahrung im Zielarchiv unabhängig vom Dokumentenablauf in DocBits.

## Individuelle Auskunft und Löschanfragen

Für eine Auskunft zur konkreten Bereitstellung oder eine Löschanfrage wenden Sie sich an **compliance@fellowpro.com**. Nennen Sie Ihre Organisation, die betroffene Umgebung und Datenart sowie den gewünschten Umfang. Übermitteln Sie dabei keine Passwörter oder API-Schlüssel.

Lassen Sie insbesondere diese Punkte bestätigen:

- Aktive Region und tatsächliche Aufbewahrungseinstellungen einschließlich des Systemstandards.
- Beginn der Löschfrist und Rhythmus der Bereinigung.
- Löschumfang für Dokumente, extrahierte Daten, Suchindizes und abgeleitete Daten.
- Speicherorte, Aufbewahrungsfristen und Behandlung gelöschter Daten in allen Sicherungsarten, auch nach Vertragsende.

## Weitere Sicherheitsinformationen

- [Sicherheit und Compliance: Standorte, Protokolle und Aufbewahrung](security-and-compliance-faq.md)
- [Verschlüsselung gespeicherter Daten und Backup-Umfang](encryption-at-rest.md)
- [Sichere Speicherung von Zugangsdaten](secure-storage-of-credentials.md)
- [Cookies und Browserspeicher](cookies-and-browser-storage.md)
