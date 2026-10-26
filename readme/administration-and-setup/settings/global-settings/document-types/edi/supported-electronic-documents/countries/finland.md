---
description: "Für Finvoice 1.3, 2.0, 2.01 und 3.0 gibt es separate Einträge. TEAPPSXML ist eine weitere Familie."
---

# Finnland

Verwenden Sie diese Anleitung, um die konfigurierte Familie und den Versionsumfang zu ermitteln, bevor Sie eine Quelldatei testen.

[Alle Länder und Umfang der Unterstützung](../README.md)

## Erklärvideo zum Land

Ein Sprechertext und WebVTT-Untertitel in der jeweiligen Sprache erklären Formatauswahl, Konfiguration und Abnahmeprüfungen.

Dieser lesende Rundgang zeigt die in DocBits vorhandene Konfiguration für das Land. Prüfen Sie die verwendete Quelle und aktive Version und testen Sie repräsentative Rechnungen, Gutschriften und Exporte in Ihrer eigenen Organisation.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_finland/v2/de.mp4" %}

[Finnland — Erklärvideo zum Land](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_finland/v2/de.mp4)

[WebVTT](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_finland/v2/de.vtt)

## Varianten und Versionsgrenzen

Für Finvoice 1.3, 2.0, 2.01 und 3.0 gibt es separate Einträge. TEAPPSXML ist eine weitere Familie.

**Syntax:** XML

Prüfen Sie die Version der Quelldatei, bevor Sie eine Zuordnung auswählen. Die Bezeichnung TEAPPSXML nennt keine Veröffentlichungsversion.

Die Tabellen dokumentieren eine Prüfung des Entwicklungskatalogs vom 17. Oktober 2026 und des zugehörigen Verarbeitungscodes. Sie beschreiben verfügbare Regeln und Konfigurationskomponenten, bestätigen jedoch nicht jede Datei, jede gesetzliche Anforderung oder die Einführung in Produktion. Ihre Organisation kann die Standardregeln überschreiben.

## Geprüfte Regel- und Komponentenmatrix

| Genaue Formatbezeichnung | Dokumentschlüssel der Regel | Verfügbare Komponenten |
| --- | --- | --- |
| `FINVOICE 1.3` | `INVOICE` | C / T / P / E |
| `FINVOICE 2.0` | `INVOICE` | C / T / P / E |
| `FINVOICE 2.01` | `INVOICE` | C / T / P / E |
| `FINVOICE 3.0` | `INVOICE` | C / T / P / E |
| `TEAPPSXML` | `INVOICE` | C / T / P / E |

C = Klassifizierung, T = Transformation, P = Preview, E = Extraction Paths. Der Dokumentschlüssel dient zur Suche nach Regeln und Konfigurationen; er garantiert nicht den endgültig gespeicherten Wert von invoice_type. Eine Transformation kann eine Gutschrift über eine INVOICE-Zuordnung klassifizieren.

Ein Strich bedeutet, dass die Statusprüfung für genau diese Kombination aus Format und Dokumentschlüssel keine eigene Komponente gemeldet hat. Eine gemeinsam genutzte Zuordnung oder eine Ausweichzuordnung ist damit nicht ausgeschlossen. Prüfen Sie die tatsächlich verwendete Auflösungslogik und eine repräsentative Datei, bevor Sie sich auf diesen Pfad verlassen.

## Die Zuordnung in DocBits finden

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-finland-de.png" alt="Finnland: FINVOICE 3.0"><figcaption><p>Echte Entwicklungsoberfläche: das repräsentative Format und seine verfügbaren Konfigurationskomponenten. Weitere Versionen sind in der Matrix aufgeführt.</p></figcaption></figure>

## Abnahmeprüfungen

Eine Komponentenprüfung bestätigt das Vorhandensein einer Konfiguration. Sie ist kein vollständiger Verarbeitungstest für jede Version. Testen Sie den genauen Dateninhalt und den von Ihrer Integration benötigten Verarbeitungsweg für Rechnungen oder Gutschriften.

## Ein Format in Ihrer Organisation prüfen

1. Bewahren Sie das ursprüngliche XML oder das PDF mit seinem eingebetteten XML auf. Lesen Sie den Namespace, die Schema- oder Anpassungskennung sowie die angegebene Version und das Profil.

2. Öffnen Sie Einstellungen → Dokumenttypen → E-Doc für den entsprechenden Geschäftsdokumenttyp. Suchen Sie nach dem genauen elektronischen Dokumentformat aus der Anleitung.

3. Prüfen Sie die tatsächlich verwendete Quelle Default oder Custom und ihre aktive Konfigurationsversion. Prüfen Sie Transformation, Preview und Extraction Paths. Das Speichern eines Entwurfs aktiviert ihn nicht.

4. Testen Sie repräsentative Quelldateien für jede benötigte Syntax, Version und jeden Geschäftsdokumenttyp. Prüfen Sie wichtige Felder, Beträge, Steuern, die Klassifizierung als Rechnung oder Gutschrift und den ERP-Export.

5. Bestätigen Sie die Validierungsrichtlinie und den Übertragungsweg separat. Erhalten Sie angepasste Zuordnungen und prüfen Sie Freigaben und Exporthistorie, bevor Sie vorhandene Dokumente neu starten.

## Weiterführende Formatreferenz

- [🇫🇮 FINVOICE 1.3](../finvoice-1-3.md)
- [🇫🇮 FINVOICE 2.0](../finvoice-2-0.md)
- [🇫🇮 FINVOICE 2.01](../finvoice-2-01.md)
- [🇫🇮 FINVOICE 3.0](../finvoice-3-0.md)
- [🇫🇮 TEAPPSXML](../teappsxml.md)
