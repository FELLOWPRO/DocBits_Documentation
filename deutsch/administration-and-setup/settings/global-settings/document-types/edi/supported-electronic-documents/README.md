---
description: "Ermitteln Sie die konfigurierte eDocs-Familie, Syntax, Version und das Profil, bevor Sie die Dokumentverarbeitung testen."
---

# eDocs-Formate, Versionen und Länderanleitungen

Beginnen Sie mit dem Quelldokument und der passenden Länderanleitung. Ein Ländername allein bezeichnet kein Dateiformat. Eine Versionsbezeichnung, die XML-Syntax und ein Geschäftsprofil beschreiben unterschiedliche Eigenschaften.

{% hint style="info" %}
Die Tabellen dokumentieren eine Prüfung des Entwicklungskatalogs vom 17. Oktober 2026 und des zugehörigen Verarbeitungscodes. Sie beschreiben verfügbare Regeln und Konfigurationskomponenten, bestätigen jedoch nicht jede Datei, jede gesetzliche Anforderung oder die Einführung in Produktion. Ihre Organisation kann die Standardregeln überschreiben.
{% endhint %}

## Die Unterstützungsmatrix richtig lesen

- Familie: das elektronische Dokumentformat, zum Beispiel XRechnung, Factur-X, KSeF oder CFDI.
- Syntax: der tatsächliche Dateninhalt, zum Beispiel UBL-XML, CII-XML oder ein PDF mit eingebettetem XML. Ein PDF-Scan, JSON-Export oder QR-Bild ist kein gleichwertiger XML-Dateninhalt.
- Version: die angegebene Veröffentlichung oder Schemaversion. Eine generische Familienbezeichnung belegt nicht die Unterstützung jeder Version.
- Profil: eine geschäftliche oder datenbezogene Teilmenge, zum Beispiel BASIC, EN16931, EXTENDED oder Selbstfakturierung. Ein Profil ist keine Veröffentlichungsversion.
- Regel und Komponenten: Klassifizierung, Transformation, Preview und Extraction Paths sind voneinander getrennt. Ein konfiguriertes Profil hat nicht zwangsläufig eine eigene Klassifizierungsregel.
- Validierung und Übertragung: Die Darstellung oder Extraktion einer Datei bestätigt für sich allein nicht alle gesetzlichen Regeln, Signaturen, steuerlichen Freigaben oder die Netzwerkzustellung.

## Länderanleitungen

| Land / Region | Familien und Versionsumfang | Katalogergebnis |
| --- | --- | --- |
| [Österreich](countries/austria.md) | Für ebInterface 4.3, 5.0, 6.0 und 6.1 gibt es separate Einträge. | Einträge gefunden |
| [Dänemark](countries/denmark.md) | OIOUBL 2.1 ist der namentlich aufgeführte dänische Eintrag. | Einträge gefunden |
| [Finnland](countries/finland.md) | Für Finvoice 1.3, 2.0, 2.01 und 3.0 gibt es separate Einträge. TEAPPSXML ist eine weitere Familie. | Einträge gefunden |
| [Frankreich](countries/france.md) | Für Factur-X gibt es generische und veröffentlichungsspezifische Einträge, darunter 1.0.05, 1.08 und 1.09. VRBL FR CIUS 1.0 ist separat. | Einträge gefunden |
| [Deutschland](countries/germany.md) | XRechnung hat dreizehn Versionsbezeichnungen von 1.0 bis 3.0.2, jeweils in CII und UBL. ZUGFeRD umfasst ältere Profile sowie Einträge für 2.5 in CII und UBL. | Einträge gefunden |
| [Italien](countries/italy.md) | FatturaPA ist die konfigurierte italienische Familie. | Einträge gefunden |
| [Niederlande](countries/netherlands.md) | Für SI-UBL 2.0 gibt es einen eigenen Eintrag. | Einträge gefunden |
| [Norwegen](countries/norway.md) | EHF Invoice 3.0 ist neben EHF Order, Order Response und Despatch Advice aufgeführt. | Einträge gefunden |
| [Polen](countries/poland.md) | Für KSeF gibt es generische Einträge sowie Einträge für FA2 und FA3. | Einträge gefunden |
| [Slowenien](countries/slovenia.md) | Für e-SLOG 1.6 und 2.0 gibt es separate Einträge. | Einträge gefunden |
| [Spanien](countries/spain.md) | Für Facturae gibt es generische Einträge sowie Einträge für 3.2, 3.2.1 und 3.2.2. | Einträge gefunden |
| [Schweden](countries/sweden.md) | Svefaktura 1.0 ist der namentlich aufgeführte schwedische Eintrag. | Einträge gefunden |
| [Australien](countries/australia.md) | PINT A-NZ hat Regeleinträge für Rechnungen und Gutschriften, die gemeinsam mit Neuseeland verwendet werden. | Einträge gefunden |
| [Neuseeland](countries/new-zealand.md) | PINT A-NZ hat Regeleinträge für Rechnungen und Gutschriften, die gemeinsam mit Australien verwendet werden. | Einträge gefunden |
| [Indien](countries/india.md) | Für India GST E-Invoice und GST CreditNote gibt es separate Einträge. | Einträge gefunden |
| [Indonesien](countries/indonesia.md) | Indonesia E-Faktur ist die konfigurierte Familie. | Einträge gefunden |
| [China](countries/china.md) | Der Katalog enthält Fapiao, E-Fapiao, General VAT Invoice und Special VAT Invoice. | Einträge gefunden |
| [Japan](countries/japan.md) | JP PINT und JP PINT Self-Billing sind separate Einträge. | Einträge gefunden |
| [Südkorea](countries/korea.md) | Korea E-Tax Invoice und Korea NTS sind konfigurierte Familien. | Einträge gefunden |
| [Malaysia](countries/malaysia.md) | Für MyInvois gibt es Regeleinträge für Rechnungen und Gutschriften. | Einträge gefunden |
| [Philippinen](countries/philippines.md) | Philippines EIS ist die konfigurierte Familie. | Einträge gefunden |
| [Singapur](countries/singapore.md) | Für InvoiceNow gibt es Rechnungs- und Gutschrifteinträge. InvoiceNow SG ist eine weitere konfigurierte Bezeichnung. | Einträge gefunden |
| [Taiwan](countries/taiwan.md) | Taiwan eGUI ist die konfigurierte Familie. | Einträge gefunden |
| [Thailand](countries/thailand.md) | Thailand E-Tax Invoice ist die konfigurierte Familie. | Einträge gefunden |
| [Vietnam](countries/vietnam.md) | Vietnam E-Invoice ist die konfigurierte Familie. | Einträge gefunden |
| [Argentinien](countries/argentina.md) | Argentina AFIP und Factura Electronica sind konfigurierte Bezeichnungen. | Einträge gefunden |
| [Brasilien](countries/brazil.md) | Für Brasilien gibt es Einträge für NF-e, NFC-e, CT-e, NFS-e und SPED NFS-e. NFS-e umfasst die Versionen 1.00 und 2.00 bis 2.04, SPED die Versionen 1.00.02 und 1.01. | Einträge gefunden |
| [Chile](countries/chile.md) | Für Chile DTE gibt es Einträge für Rechnungen, Gutschriften und Versandbegleitdokumente. | Einträge gefunden |
| [Kolumbien](countries/colombia.md) | Für Colombia Factura Electronica und Documento Soporte gibt es separate Einträge. | Einträge gefunden |
| [Costa Rica](countries/costa-rica.md) | Die ältere Dokumentation nennt Costa Rica. Im geprüften Entwicklungskatalog wurde jedoch kein passender Klassifizierungs- oder Konfigurationseintrag gefunden. | Nicht bestätigt |
| [Ecuador](countries/ecuador.md) | Für Ecuador SRI gibt es generische Einträge sowie Einträge für 1.0.0, 1.1.0, 2.0.0 und 2.1.0. Quellensteuer ist ein separater Dokumenttyp. | Einträge gefunden |
| [Mexiko](countries/mexico.md) | Für Mexico CFDI 3.3 und 4.0 gibt es separate Einträge. | Einträge gefunden |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN und SIFEN 150 sind konfigurierte Bezeichnungen. | Einträge gefunden |
| [Peru](countries/peru.md) | Für Peru CPE gibt es generische Einträge sowie Einträge für UBL 2.0 und UBL 2.1. Factura Electronica ist eine weitere Bezeichnung. | Einträge gefunden |
| [Uruguay](countries/uruguay.md) | Für Uruguay CFE gibt es generische Einträge sowie Einträge für 24 und 25. E-Factura und E-Nota Credito sind ebenfalls aufgeführt. | Einträge gefunden |
| [Kasachstan](countries/kazakhstan.md) | Kazakhstan ESF ist die konfigurierte Familie. | Einträge gefunden |
| [Saudi-Arabien](countries/saudi-arabia.md) | Für ZATCA Fatoorah, Reporting, Simplified und Tax Invoice gibt es separate Einträge. | Einträge gefunden |
| [Türkei](countries/turkey.md) | Turkey E-Fatura und E-Arsiv sind separate konfigurierte Familien. | Einträge gefunden |
| [Vereinigte Arabische Emirate](countries/united-arab-emirates.md) | UAE VAT Invoice ist die konfigurierte Bezeichnung. | Einträge gefunden |
| [International](countries/international.md) | Internationale Einträge umfassen Peppol BIS 3.0, UBL 2.1, reines CII, EDI, INVOIC02, cXML, OCI, BOD und SPS Commerce RSX 7.7.4. | Einträge gefunden |

## Factur-X / ZUGFeRD: keine Veröffentlichungsversion erfinden

Eine harmonisierte CII Guideline ID kann eine Familie und ein Profil identifizieren, obwohl mehrere Veröffentlichungen dieselbe Kennung 1p0 verwenden. Factur-X XMP Version 1.0 ist eine Schemakennung, keine Veröffentlichung wie 1.08 oder 1.09. ZUGFeRD-XMP kann seine Version angeben. Fehlen maßgebliche Metadaten, behalten Sie das generische Familienergebnis bei und klären Sie die ursprüngliche Datei mit dem Absender.

MINIMUM und BASIC WL können Positionsinformationen auslassen, die in nachgelagerten Schritten benötigt werden. BASIC, EN16931/COMFORT und EXTENDED decken unterschiedliche Datenumfänge ab. Ein umfangreicheres Profil kann Felder enthalten, die Ihre Extraktionszuordnung nicht verwendet. Prüfen Sie die erforderlichen Felder anhand tatsächlicher Beispiele.

## Ein Format in Ihrer Organisation prüfen

1. Bewahren Sie das ursprüngliche XML oder das PDF mit seinem eingebetteten XML auf. Lesen Sie den Namespace, die Schema- oder Anpassungskennung sowie die angegebene Version und das Profil.

2. Öffnen Sie Einstellungen → Dokumenttypen → E-Doc für den entsprechenden Geschäftsdokumenttyp. Suchen Sie nach dem genauen elektronischen Dokumentformat aus der Anleitung.

3. Prüfen Sie die tatsächlich verwendete Quelle Default oder Custom und ihre aktive Konfigurationsversion. Prüfen Sie Transformation, Preview und Extraction Paths. Das Speichern eines Entwurfs aktiviert ihn nicht.

4. Testen Sie repräsentative Quelldateien für jede benötigte Syntax, Version und jeden Geschäftsdokumenttyp. Prüfen Sie wichtige Felder, Beträge, Steuern, die Klassifizierung als Rechnung oder Gutschrift und den ERP-Export.

5. Bestätigen Sie die Validierungsrichtlinie und den Übertragungsweg separat. Erhalten Sie angepasste Zuordnungen und prüfen Sie Freigaben und Exporthistorie, bevor Sie vorhandene Dokumente neu starten.

[Abnahmeprüfungen](../credit-note-recognized-as-invoice.md)
