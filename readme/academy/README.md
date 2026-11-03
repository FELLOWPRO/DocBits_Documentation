---
description: "Von Ihrem Geschäftsproblem zur fertigen Lösung: DocBits anhand von Rechnungen, Tabellen und kontrollierten Ergebnissen lernen."
---

# DocBits Academy – Learn by Example

**Von Ihrem Geschäftsproblem zur fertigen Lösung.**

Lernen Sie DocBits anhand realistischer Geschäftsvorfälle kennen. Jedes Tutorial führt Sie von einem Beispieldokument über Konfiguration, Verarbeitung und Prüfung bis zum kontrollierten Ergebnis. Wählen Sie zuerst Ihr Geschäftsproblem.

## Mit diesen sechs Tutorials beginnen

| Ihr Vorhaben | Tutorial | Dauer |
| --- | --- | --- |
| Dienstleistungsrechnung ohne PO verarbeiten | [1. Rechnung ohne Bestellung](rechnung-ohne-bestellung.md) | 10–15 Min. |
| Eine Preisabweichung zur Bestellung entscheiden | [2. Rechnung mit Bestellung](rechnung-mit-bestellung.md) | 15–20 Min. |
| Eine Kostenrechnung auf drei Kostenstellen verteilen | [3. Kontierung und Kostenstellen](kostenstellen-aufteilen.md) | 15 Min. |
| Zwei erforderliche Freigaben nachvollziehen | [4. Mehrstufige Freigabe](mehrstufige-freigabe.md) | 15–20 Min. |
| Einen fehlgeschlagenen Export sicher wiederholen | [5. ERP-Exportfehler](erp-export-fehler.md) | 20 Min. |
| Alle Positionen über drei Seiten vollständig prüfen | [6. Mehrseitige KI-Tabelle](mehrseitige-ki-tabellen.md) | 15–20 Min. |

[Übungspaket herunterladen und Testumgebung vorbereiten](vorbereitung.md). Alle Beispieldaten sind synthetisch. Die Dauer ist eine Orientierung und setzt die vorbereitete Testorganisation voraus.

## 1. Einstieg

- [Erste Rechnung verarbeiten](rechnung-ohne-bestellung.md)
- [Dokumente importieren](../end-user-and-partner-section/end-user-section/how-to-import-documents/manual-import.md) und [klassifizieren](../administration-and-setup/settings/document-processing/classification-and-extraction/README.md)
- [Extrahierte Daten prüfen und korrigieren](../end-user-and-partner-section/end-user-section/validation-screen/README.md)
- [Dokumentstatus verstehen](../end-user-and-partner-section/end-user-section/dashboard/document-status.md)

## 2. Rechnungsverarbeitung

- [Rechnung ohne Bestellung verarbeiten](rechnung-ohne-bestellung.md)
- [Rechnung mit Bestellung abgleichen](rechnung-mit-bestellung.md)
- [Teilrechnungen, Teillieferungen und Multi Match](../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md)
- [Rechnungen mit zusätzlichen Kosten und Rabatten](ki-rabatte-zuschlaege.md)
- [Gutschriften: Dokumentart und Extraktion prüfen](../administration-and-setup/settings/document-processing/classification-and-extraction/README.md)

## 3. KI-Tabellen

- [Positionen aus mehrseitigen Rechnungen extrahieren](mehrseitige-ki-tabellen.md)
- [Tabellen ohne Rahmenlinien bearbeiten](ki-ohne-rahmenlinien.md)
- [Unterschiedliche Spaltenbezeichnungen zuordnen](ki-spalten-zuordnen.md)
- [Nicht benötigte Spalten entfernen](ki-spalten-entfernen.md)
- [Tabellenfehler erkennen und korrigieren](ki-tabellen-korrigieren.md)
- [Berechnungen und Summen kontrollieren](ki-tabellenregeln.md)
- [Extrahierte Positionen für ERP-Export vorbereiten](ki-positionen-exportieren.md)

[Alle zehn priorisierten Tabellenfälle](ki-tabellen.md) · [Kompletter Geschäftsfall: 30 Positionen, drei Abweichungen](dreissig-positionen-abgleichen.md)

## 4. Automatisierung und Freigaben

- [Automatische Kontierung und Kostenstellen aufteilen](kostenstellen-aufteilen.md)
- [Mehrstufige Rechnungsfreigabe](mehrstufige-freigabe.md)
- [Toleranzen und Konfliktregeln](rechnung-mit-bestellung.md)
- [Ausnahmen über Betragsrouting weiterleiten](../administration-and-setup/workflow/advanced-workflow-case-study.md)

## 5. ERP und Fehlerbehebung

- [Rechnung nach Infor LN](../infor-integration-and-configuration/exporting-to-infor/ln/ln-configuration.md) oder [M3 exportieren](../infor-integration-and-configuration/exporting-to-infor/m3/m3-configuration.md)
- [Dokument in Infor IDM archivieren](../infor-integration-and-configuration/exporting-to-infor/exporting-to-idm.md)
- [Fehlgeschlagenen Export untersuchen](erp-export-fehler.md)
- [Falsche Dokumentklassifizierung: Einstellungen prüfen](../administration-and-setup/settings/document-processing/classification-and-extraction/README.md)
- [Verarbeitungsfehler anhand des Dokument-Flows eingrenzen](../end-user-and-partner-section/end-user-section/dashboard/document-flow.md)

## Weitere Geschäftsprobleme

| Frage | Einstieg |
| --- | --- |
| Wie richte ich ein Rechnungspostfach ein? | [E-Mail-Import](../end-user-and-partner-section/end-user-section/how-to-import-documents/email/README.md) und [IMAP-Einrichtung](../end-user-and-partner-section/end-user-section/how-to-import-documents/email/imap.md) |
| Was tun bei unbekanntem Lieferanten? | [Lieferantenprüfung im ersten Tutorial](rechnung-ohne-bestellung.md#fehlerbehebung) |
| Wie prüfe ich eine XRechnung? | [E-Rechnungsprüfung und Validierungsbericht](../administration-and-setup/settings/document-processing/e-documents/validation-rules.md) |
| Welche Rechnungen warten auf Freigabe? | [Nach Status und Zuständigkeit filtern](../end-user-and-partner-section/end-user-section/dashboard/filtering-documents.md) |

Beim Suchen nach „seit mehr als drei Tagen auf Freigabe“ benötigen Sie den Beginn des Freigabestatus. Ein Importdatum allein misst diese Wartezeit nicht. Prüfen Sie den Freigabeverlauf der gefilterten Belege beziehungsweise ein dafür eingerichtetes Statuszeitfeld.

Die verlinkten Funktionsanleitungen ergänzen die neuen Übungsfälle. Für Gutschriften, IDM, XRechnung/ZUGFeRD, Lieferantenportal und E-Mail-Import gelten die vorhandenen Anleitungen; eigenständige neue Academy-End-to-End-Fälle folgen der [Erweiterungsphase](qualitaet-und-abnahme.md#veröffentlichung-in-etappen).

## So ist jede Übung aufgebaut

**Problem → Beispieldokument → Konfiguration → Ausführung → Ergebnis → Fehlerbehebung.** Vergleichen Sie zuerst Original und Sollwerte, danach die gespeicherten Daten und schließlich das tatsächliche Ergebnis im Zielsystem.

[Qualitätsstandard, fachliche Abnahme und Veröffentlichungsphasen](qualitaet-und-abnahme.md)

**Stand:** 27.10.2026 · **Academy-Version:** 1.0
