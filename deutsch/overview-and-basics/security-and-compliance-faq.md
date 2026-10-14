# DocBits (FELLOWPRO AG) — Sicherheits- und Compliance-Fragebogen

**Anbieter:** DocBits von FELLOWPRO AG | **Hosting:** Frankfurt, Deutschland | **ISO 27001 zertifiziert** | **Datum:** 2026-03-04

---

## Legendenzeichen Status

| Symbol | Bedeutung |
|--------|---------|
| ✅ Bestätigt | Antwort verifiziert aus offizieller DocBits-Dokumentation oder öffentlichen Quellen |
| ✅ Teilweise | Teilweise beantwortet; zusätzliche Details vom DocBits-Team erforderlich |
| ❓ Zu bestätigen | Keine öffentlichen Informationen verfügbar — muss direkt mit DocBits/FELLOWPRO geklärt werden |
| ⚠️ Bedarf Klarstellung | Öffentliche Informationen deuten auf Bedenken oder Mehrdeutigkeiten hin, die eine explizite Vendor-Klärung erfordern |

---

## 🔹 Datenspeicherort & Residenz

### 1. Wo genau wird die Produktionsumgebung gehostet?

**Antwort:** Gehostet auf AWS Cloud-Infrastruktur in Frankfurt, Deutschland. Verwendet S3 für Speicherung und OpenSearch für Log-Indexierung. DocBits ist ISO 27001 zertifiziert. Alle Verbindungen sind durch SSH, HTTPS und branchenübliche Verschlüsselungsprotokolle gesichert.

**Status:** ✅ Bestätigt

**Notizen:** AWS Frankfurt bestätigt (S3 + OpenSearch). Erfragen Sie den spezifischen AWS-Regionscode (eu-central-1) und ob Single oder Multi-AZ.

---

### 2. Wo wird die DR-Umgebung (Disaster Recovery) gehostet?

**Antwort:** DR nutzt einen sekundären Backup-Standort in Amsterdam, Niederlande (EU). Kombiniert mit dem primären Frankfurt-Standort bietet dies geografische Redundanz innerhalb der EU.

**Status:** ✅ Bestätigt

**Notizen:** Frankfurt (primär) + Amsterdam (sekundär). Beide EU-Standorte. Erfragen Sie RTO/RPO-Ziele und Details zum Failover-Prozess.

---

### 3. Wo werden Sicherungen gespeichert?

**Antwort:** Sicherungen sind an zwei EU-Standorten gespeichert:
- **Primär:** Frankfurt, Deutschland
- **Sekundär:** Amsterdam, Niederlande

Backup-Zeitplan: Tägliche, wöchentliche, vierteljährliche und jährliche Sicherungen.

**Status:** ✅ Bestätigt

**Notizen:** Umfassender Backup-Zeitplan (täglich/wöchentlich/vierteljährlich/jährlich) über zwei EU-Standorte. Alle Daten bleiben innerhalb der EU. Bestätigen Sie die Backup-Verschlüsselung und die Häufigkeit von Wiederherstellungstests.

---

### 4. Gibt es Geo-Partitionierungsoptionen (z. B. nur UK)?

**Antwort:** Zwei Datencenter-Regionen sind verfügbar:
- **Frankfurt, Deutschland** — für alle EU-Kunden
- **New York, USA** — nur für US-Kunden

EU-Kundendaten werden ausschließlich in Frankfurt gehostet. Derzeit ist keine Nur-UK-Option verfügbar.

**Status:** ✅ Bestätigt

**Notizen:** EU-Kunden sind auf Frankfurt beschränkt — keine regionenübergreifende Datenvermischung. UK-Only-Hosting nicht verfügbar; UK-Kunden würden von Frankfurt aus bedient. Klären Sie, ob zusätzliche Regionen auf der Roadmap stehen.

---

### 5. Sind Daten im Ruhezustand und während der Übertragung verschlüsselt?

**Antwort:** Alle Verbindungen zwischen Komponenten sind mit branchenüblichen Verschlüsselungsprotokollen (SSH, HTTPS) gesichert. ISO 27001-Zertifizierung schreibt Verschlüsselungskontrollen vor.

**Status:** ✅ Bestätigt

**Notizen:** Bestätigen Sie spezifische Verschlüsselungsstandards (z. B. AES-256 im Ruhezustand, TLS 1.2+ während der Übertragung).

---

## 🔹 KI/ML-Modell-Handhabung

### 6. Werden Rechnungsinhalte an externe Modell-Hosts (z. B. OpenAI, Azure AI) gesendet?

**Antwort:** KI-Modelle werden NICHT an externe Hosts gesendet. DocBits nutzt Mistral AI-Modelle, die in Frankfurt, Deutschland laufen — am gleichen Standort wie die Produktionsumgebung. Es verlassen keine Daten die Frankfurt-Region für KI-Verarbeitung.

**Status:** ✅ Bestätigt

**Notizen:** Mistral-Modelle in Frankfurt gehostet. Keine API-Aufrufe von Drittanbietern zur Dokumentenverarbeitung. Vollständig in sich geschlossen.

---

### 7. Werden extrahierte Dokumente zum Training breiterer Modelle über alle Kunden hinweg verwendet?

**Antwort:** Ja — DocBits nutzt „KI-Schwarmintelligation", die Klassifizierungs- und Extraktionsmodelle über alle Kunden hinweg trainiert. Die Technologie funktioniert jedoch wie eine Karte durch die Daten — sie erlernt die Koordinaten/strukturellen Positionen von Datenfeldern in Dokumenten, NICHT den tatsächlichen Dokumentinhalt. Rohe Dokumentdaten werden nicht über Mandanten hinweg gemeinsam genutzt.

**Status:** ✅ Bestätigt

**Notizen:** Schwarmintelligung erlernt strukturelle Layout-Muster (Feldkoordinaten/Positionen), nicht Dokumentinhalt. Dies bedeutet, dass keine Kundendaten (Rechnungsbeträge, Lieferantennamen usw.) über Mandanten hinweg gemeinsam genutzt werden — nur Wissen über Dokumentstruktur.

---

### 8. Können Sie das Modell-Training auf Ihren Mandanten beschränken?

**Antwort:** Keine Option zur Isolation von Modellen pro Mandant. Die gemeinsam genutzten KI-Modelle erlernen jedoch nur Dokumentlayout-Koordinaten und strukturelle Muster — keine tatsächlichen Dokumentinhalte oder Geschäftsdaten. Kunden können zusätzlich benutzerdefinierte Dokumenttypen trainieren, die auf ihren eigenen Mandanten beschränkt sind.

**Status:** ✅ Bestätigt

**Notizen:** Geringes Risiko: Gemeinsame Modelle erlernen nur Positions-/Strukturdaten (Koordinaten), nicht Geschäftsinhalte. Training für benutzerdefinierte Dokumenttypen bleibt auf den Mandanten begrenzt.

---

### 9. Wo werden KI/ML-Modelle gehostet und ausgeführt?

**Antwort:** KI/ML-Modelle (Mistral) sind in Frankfurt, Deutschland gehostet und werden ausgeführt — in derselben Region wie die Produktionsumgebung.

**Status:** ✅ Bestätigt

**Notizen:** Positiv: KI-Verarbeitung bleibt innerhalb von Frankfurt. Keine Datenübertragung zu externer KI-Infrastruktur.

---

### 10. Welche KI/ML-Technologien werden verwendet (OCR-Engine, LLM, NLP)?

**Antwort:** DocBits verwendet KI, OCR und maschinelles Lernen zur Extraktion. Unterstützt 120+ Sprachen. Behauptet 96%+ Genauigkeit. Nutzt auch Gen AI für die Funktion „KI-Tags".

**Status:** ✅ Teilweise

**Notizen:** Erfragen Sie nach spezifischen Modelldetails: proprietär vs. OCR von Drittanbietern, welches LLM die Gen AI-Funktionen unterstützt.

---

### 11. Gibt es eine Option für lokale KI-Modell-Bereitstellung?

**Antwort:** DocBits-Architekturdokumentation verweist auf beide Bereitstellungsoptionen: „DocBits Cloud-Kunde" und „DocBits vor Ort".

**Status:** ✅ Teilweise

**Notizen:** Bestätigen Sie den Umfang der lokalen Option: Enthält sie die vollständige KI-Verarbeitung oder nur Dokumentenspeicherung?

---

## 🔹 Datenzugriff & Protokollierung

### 12. Wer (Vendor-Support/Ingenieure) kann auf Rohdokumente und Infor LN-Daten zugreifen?

**Antwort:** FELLOWPRO AG hat einen designierten Datenschutzbeauftragten (Daniel Jordan). DPAs mit Subunternehmen sind gemäß GDPR vorhanden. ISO 27001 schreibt Zugriffskontrolle vor.

**Status:** ✅ Teilweise

**Notizen:** Erfragen Sie bei DocBits: Exakte Liste von Personalrollen mit Zugriff auf Rohdokumente. Ist der Zugriff nur bei Bedarf / auf Anfrage?

---

### 13. Welche Zugriffskontrolle und Protokollierung existiert für Vendor-Personal?

**Antwort:** ISO 27001-Zertifizierung erfordert dokumentierte Zugriffskontrolle, Audit Trails und Sicherheitsmaßnahmen. DocBits führt Audit Trails zur Einhaltung und Überprüfung.

**Status:** ✅ Teilweise

**Notizen:** Erfragen Sie: RBAC-Details, MFA-Anforderungen, privilegiertes Zugriffsverwaltung (PAM) und ob der Zugriff mit unveränderlichen Audit Trails protokolliert wird.

---

### 14. Wie lange werden Zugriffsprotokolle beibehalten?

**Antwort:** Protokolle werden auf AWS S3 in Frankfurt und OpenSearch gespeichert. Kundenzugängliche Protokolle werden 30 Tage lang beibehalten. Interne Protokolle werden 3 Monate lang beibehalten.

**Status:** ✅ Bestätigt

**Notizen:** S3 + OpenSearch in Frankfurt. 30-Tage Kundenzugriff / 3-Monate interne Aufbewahrung. Bestätigen Sie, ob Protokolle unveränderbar/manipulationssicher sind.

---

### 15. Wie lange werden hochgeladene Dokumente / extrahierte Daten in DocBits beibehalten?

**Antwort:** Kunden können die Datenspeicherung in den Einstellungen konfigurieren. Optionen: 30 Tage oder 3 Monate. Nach dem konfigurierten Zeitraum werden Dokumente und extrahierte Daten automatisch von DocBits-Servern gelöscht.

**Status:** ✅ Bestätigt

**Notizen:** Kundenkonfigurierbare Aufbewahrung (30 Tage / 3 Monate). Bestätigen Sie: Umfasst die Löschung alle Kopien (S3, OpenSearch, KI-Trainingsdaten)?

---

### 16. Können Kunden die Datenlöschung auf Anfrage anfordern?

**Antwort:** FELLOWPRO AG erfüllt GDPR-Betroffenenrechte einschließlich Löschanfragen. Der DPO verarbeitet diese Anfragen gemäß GDPR Art. 17.

**Status:** ✅ Bestätigt

**Notizen:** Bestätigen Sie: Umfasst die Löschung alle Kopien einschließlich Backups und KI-Trainingsdaten, die vom Mandanten abgeleitet sind?

---

### 17. Welche Subunternehmen haben Zugriff auf Kundendaten?

**Antwort:** Cloudflare wird für Bot-Schutz/DDoS verwendet. DPAs sind gemäß GDPR-Anforderungen mit allen Subunternehmern vorhanden.

**Status:** ✅ Teilweise

**Notizen:** Erfragen Sie die vollständige Subunternehmer-Liste. Cloudflare bestätigt; erfragen Sie nach Cloud-Hosting-Anbieter, KI-Service-Anbietern usw.

---

### 18. Welche Zertifizierungen und Compliance-Frameworks hat DocBits?

**Antwort:** ISO 27001 zertifiziert. GDPR-konform. Verwaltet DPAs mit allen Subunternehmern. Designierter DPO.

**Status:** ✅ Bestätigt

**Notizen:** Erfragen Sie: SOC 2 Type II? Penetrationstestberichte? ISO 27701 (Datenschutz)? Zeitplan für jährliche Audits?

---

## 🔹 Integrations-Umfang (Infor LN)

### 19. Wie lautet die exakte Liste von Datenfeldern, die von LN Master für die Validierung gepullt werden?

**Antwort:** Master-Daten importiert via Infor BODs:
- **Lieferanten:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Bestellungen:** Sync.PurchaseOrder
- **Kontenpläne:** Sync.CodeDefinition (ChartOfAccounts)
- **Flexible Dimensionen:** Sync.CodeDefinition (FlexDimensions)
- **Steuercodes:** via BOD publish

**Status:** ✅ Bestätigt

**Notizen:** Erfragen Sie die vollständige BOD-Liste und die Feld-Level-Mapping-Dokumentation für Ihre spezifische LN-Konfiguration bei DocBits.

---

### 20. Welche spezifischen Header-Felder werden zurück zu LN exportiert?

**Antwort:** Header-Exportfelder umfassen: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType und mehr.

**Status:** ✅ Bestätigt

**Notizen:** Überprüfen Sie die Feld-Mapping-Datei für Ihre spezifische Umgebung. Bestätigen Sie, dass alle statischen Felder mit Ihrem LN-Unternehmensaufbau übereinstimmen.

---

### 21. Sind Write-Back-Operationen nur auf AP/PO-Interface-Objekte beschränkt?

**Antwort:** Export nutzt Sync.CaptureDocument BOD, das in ION Desk zu Ziel-BODs (z. B. AP-Rechnungs-BODs) transformiert wird. Daten werden auch zu Infor IDM für Dokumentenarchivierung exportiert.

**Status:** ✅ Teilweise

**Notizen:** Bestätigen Sie: Schreibt DocBits NUR zu AP-Rechnungs- und PO-Empfangsobjekten? Werden andere LN-Module berührt? Was ist der IDM-Schreibumfang?

---

### 22. Welche Integrationsmethode wird verwendet (ION API, BODs, Direct DB)?

**Antwort:** Integration via Infor ION API, ION Desk und Infor Standard BODs. Kein direkter Datenbankzugriff. Nutzt ION API-Dateien und Service Accounts für die Authentifizierung.

**Status:** ✅ Bestätigt

**Notizen:** Positiv: Kein direkter DB-Zugriff. Alle Kommunikation über die Infor-Standard-Integrations-Ebene.

---

### 23. Welche Authentifizierung/Autorisierung wird für LN-Konnektivität verwendet?

**Antwort:** Nutzt ION API Files (OAuth2 Client Credentials) mit ION API Client IDs und Service Accounts, die in InforOS erstellt werden.

**Status:** ✅ Bestätigt

**Notizen:** Stellen Sie sicher, dass Service Accounts das Prinzip der geringsten Rechte folgen. Überprüfen Sie die Berechtigungen, die dem DocBits ION API-Benutzer gewährt werden.

---

### 24. Ist die Datenübertragung zwischen DocBits und LN durchgehend verschlüsselt?

**Antwort:** Alle Verbindungen zwischen Komponenten sind mit branchenüblicher Verschlüsselung (SSH, HTTPS) gesichert.

**Status:** ✅ Bestätigt

**Notizen:** ION API-Kommunikation nutzt HTTPS/TLS. Bestätigen Sie die minimale TLS-Version (1.2+).

---

### 25. Welche Dokumenttypen werden über AP-Rechnungen hinaus unterstützt?

**Antwort:** Unterstützt Rechnungen, Lieferscheine/Rechnungen, Angebote, Bestellbestätigungen, Verträge und mehr. Verarbeitet PO und Non-PO-Rechnungen.

**Status:** ✅ Bestätigt

**Notizen:** Klären Sie, welche Dokumenttypen zu LN zurückgeschrieben werden vs. nur in IDM gespeichert sind.
