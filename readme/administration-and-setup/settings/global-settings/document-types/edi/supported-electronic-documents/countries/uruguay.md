---
description: "Für Uruguay CFE gibt es generische Einträge sowie Einträge für 24 und 25. E-Factura und E-Nota Credito sind ebenfalls aufgeführt."
---

# Uruguay

Verwenden Sie diese Anleitung, um die konfigurierte Familie und den Versionsumfang zu ermitteln, bevor Sie eine Quelldatei testen.

[Alle Länder und Umfang der Unterstützung](../README.md)

## Varianten und Versionsgrenzen

Für Uruguay CFE gibt es generische Einträge sowie Einträge für 24 und 25. E-Factura und E-Nota Credito sind ebenfalls aufgeführt.

**Syntax:** XML

Für Gutschrifteinträge sind im geprüften Status keine eigenen Extraktionspakete ausgewiesen. Bestätigen Sie die CFE-Version und die tatsächlich verwendete Rechnungs- oder Gutschriftzuordnung.

Die Tabellen dokumentieren eine Prüfung des Entwicklungskatalogs vom 17. Oktober 2026 und des zugehörigen Verarbeitungscodes. Sie beschreiben verfügbare Regeln und Konfigurationskomponenten, bestätigen jedoch nicht jede Datei, jede gesetzliche Anforderung oder die Einführung in Produktion. Ihre Organisation kann die Standardregeln überschreiben.

## Geprüfte Regel- und Komponentenmatrix

| Genaue Formatbezeichnung | Dokumentschlüssel der Regel | Verfügbare Komponenten |
| --- | --- | --- |
| `URUGUAY E-FACTURA` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY E-NOTA CREDITO` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY CFE` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 24` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 25` | `INVOICE` | C / T / P / E |
| `URUGUAY E-FACTURA` | `INVOICE` | C / T / P / E |

C = Klassifizierung, T = Transformation, P = Preview, E = Extraction Paths. Der Dokumentschlüssel dient zur Suche nach Regeln und Konfigurationen; er garantiert nicht den endgültig gespeicherten Wert von invoice_type. Eine Transformation kann eine Gutschrift über eine INVOICE-Zuordnung klassifizieren.

Ein Strich bedeutet, dass die Statusprüfung für genau diese Kombination aus Format und Dokumentschlüssel keine eigene Komponente gemeldet hat. Eine gemeinsam genutzte Zuordnung oder eine Ausweichzuordnung ist damit nicht ausgeschlossen. Prüfen Sie die tatsächlich verwendete Auflösungslogik und eine repräsentative Datei, bevor Sie sich auf diesen Pfad verlassen.

## Die Zuordnung in DocBits finden

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-uruguay-de.png" alt="Uruguay: URUGUAY CFE 25"><figcaption><p>Echte Entwicklungsoberfläche: das repräsentative Format und seine verfügbaren Konfigurationskomponenten. Weitere Versionen sind in der Matrix aufgeführt.</p></figcaption></figure>

## Erklärvideo zum Land

Ein Sprechertext und WebVTT-Untertitel in der jeweiligen Sprache erklären Formatauswahl, Konfiguration und Abnahmeprüfungen.

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-de.mp4" %}
Uruguay — Erklärvideo zum Land
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-de.vtt" %}
WebVTT
{% endfile %}

## Abnahmeprüfungen

Eine Komponentenprüfung bestätigt das Vorhandensein einer Konfiguration. Sie ist kein vollständiger Verarbeitungstest für jede Version. Testen Sie den genauen Dateninhalt und den von Ihrer Integration benötigten Verarbeitungsweg für Rechnungen oder Gutschriften.

## Ein Format in Ihrer Organisation prüfen

1. Bewahren Sie das ursprüngliche XML oder das PDF mit seinem eingebetteten XML auf. Lesen Sie den Namespace, die Schema- oder Anpassungskennung sowie die angegebene Version und das Profil.

2. Öffnen Sie Einstellungen → Dokumenttypen → E-Doc für den entsprechenden Geschäftsdokumenttyp. Suchen Sie nach dem genauen elektronischen Dokumentformat aus der Anleitung.

3. Prüfen Sie die tatsächlich verwendete Quelle Default oder Custom und ihre aktive Konfigurationsversion. Prüfen Sie Transformation, Preview und Extraction Paths. Das Speichern eines Entwurfs aktiviert ihn nicht.

4. Testen Sie repräsentative Quelldateien für jede benötigte Syntax, Version und jeden Geschäftsdokumenttyp. Prüfen Sie wichtige Felder, Beträge, Steuern, die Klassifizierung als Rechnung oder Gutschrift und den ERP-Export.

5. Bestätigen Sie die Validierungsrichtlinie und den Übertragungsweg separat. Erhalten Sie angepasste Zuordnungen und prüfen Sie Freigaben und Exporthistorie, bevor Sie vorhandene Dokumente neu starten.

## Weiterführende Formatreferenz

- [🇺🇾 URUGUAY CFE](../uruguay-cfe.md)
- [🇺🇾 URUGUAY CFE 24](../uruguay-cfe-24.md)
- [🇺🇾 URUGUAY CFE 25](../uruguay-cfe-25.md)
- [🇺🇾 URUGUAY E-FACTURA](../uruguay-e-factura.md)
- [🇺🇾 URUGUAY E-NOTA CREDITO](../uruguay-e-nota-credito.md)
