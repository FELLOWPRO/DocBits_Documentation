# DocBits Release-Notizen — 3.–4. Juli 2026

_Ein Überblick darüber, was sich für Sie mit diesem DocBits-Release ändert. Jeder
Service unten zeigt die Version, die jetzt in der Produktion läuft, gefolgt von dem,
was neu oder behoben ist — in klarer Sprache, ohne Ticket-Nummern und ohne
Entwickler-Jargon. Nicht aufgeführte Services hatten in diesem Zeitraum keine für
Kunden sichtbaren Änderungen._

---

## Highlights

- **Zero-Downtime-Deployments, flottenweit.** API, Auto Accounting, Docflow,
  Extraction, OCR und PO Match fahren jetzt bei einem neuen Release sauber
  herunter. Bisher konnte eine Anfrage, die während eines Deployments gerade
  in Bearbeitung war, abgebrochen werden; jetzt wird jede laufende Anfrage
  abgeschlossen, bevor die alte Version stoppt — Releases verursachen dadurch
  keine kurzen Aussetzer mehr für Nutzer.
- **Verbesserungen beim E-Rechnungs-Export.** Der Export eines Dokuments in
  mehrere Exportkonfigurationen gleichzeitig ist jetzt zuverlässiger — die
  Duplikatsprüfung beim Export läuft nur noch einmal pro Batch statt einmal pro
  Position, und ein neuer Export-Endpunkt verhindert, dass der Exportstatus
  flackert, wenn mehrere Exporte gemeinsam ausgelöst werden. XRechnung-/
  ZUGFeRD-Dokumente erhalten außerdem ein konsistenteres Feld-Mapping.
- **Stabilere Dokumentenverarbeitung.** Ein Absturz behoben, der ein komplettes
  OCR-Dokument lahmlegen konnte, wenn eine einzelne Seite fehlschlug; die
  Synchronisierung der Bestellungs-Lieferdaten (Purchase-Order) behoben, die
  bisher nur die ersten 100 Datensätze abrief; und mehrere Services gegen kurze
  Datenbankverbindungsabbrüche gehärtet.
- **E-Mail-Anhänge wiederhergestellt.** Ein Fall behoben, in dem E-Mail-Anhänge
  beim eingehenden Import beschädigt oder mit fehlenden Bytes ankommen konnten.
- **Workflow-Zuverlässigkeit.** Behoben, dass Workflows durch eine Sperre
  hängen blieben, die nicht korrekt aufgehoben wurde, und die
  Neuplanungslogik korrigiert, sodass übersprungene Workflow-Schritte korrekt
  behandelt und protokolliert werden.
- **Neu: Ideas Service.** Ein neuer Backend-Service (Ideas, v0.3.0) ist der
  Produktionsflotte beigetreten.

---

## API Service — live: `12.52.4`

- **OCR-Zuverlässigkeit:** Ein Absturz bei einer einzelnen Seite lässt das
  gesamte Dokument nicht mehr fehlschlagen.
- **Export:** Die Duplikatsprüfung beim Export läuft jetzt nur noch einmal pro
  Batch statt einmal pro Position; ein neuer Export-Endpunkt verhindert, dass
  der Exportstatus flackert, wenn mehrere Exporte gleichzeitig laufen;
  XRechnung-/ZUGFeRD-Dokumente erhalten ein konsistenteres kanonisches
  Feld-Mapping.
- **Bestellungen (Purchase Orders):** Behoben, dass die Lieferungs-Synchronisierung
  pro Bestellung nur die ersten 100 Datensätze abrief.
- **Aktivitätsprotokolle:** Behoben, dass die Schaltfläche „Weiter“ zu einem
  falschen Zeitraum sprang.
- **Stammdatensuche (Master Data Lookup):** Ein Serverfehler (HTTP 500) behoben.
- **Suchindexierung:** Eine Zustellbestätigungsmarkierung und Wiederholungslogik
  hinzugefügt, damit Dokumente zuverlässig für die Volltextsuche eingereiht
  werden.
- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.
- Allgemeine Stabilitätskorrekturen zur Behebung mehrerer wiederkehrender
  Hintergrundfehler.

## Auth Service — live: `1.68.7`

- Nur interne Zuverlässigkeits- und Wartungsarbeiten in diesem Zeitraum.

## Auto Accounting — live: `1.18.8`

- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.

## Barcode Service — live: `1.15.8`

- Nur eine interne Bereitstellungskonfigurations-Korrektur in diesem Zeitraum.

## Docflow Service — live: `2.5.3`

- **Neue Exportoption** zum gleichzeitigen Senden eines Dokuments an mehrere
  Exportkonfigurationen.
- **Behoben, dass Workflows hängen blieben** durch eine Sperre, die
  unabhängig vom Status nicht korrekt aufgehoben wurde.
- **Workflow-Neuplanung behoben**, sodass übersprungene Schritte korrekt
  behandelt und protokolliert werden, statt stillschweigend verworfen zu
  werden.
- **Schnellerer Start:** Datenbanken werden jetzt im Hintergrund vorab
  aufgewärmt.
- Widerstandsfähiger gegenüber kurzen Datenbankverbindungsabbrüchen.
- Verbessertes Parsing von Datumsfeldern bei Workflow-Karten.
- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.

## Email Service — live: `1.37.9`

- **Eingehende Anhänge behoben**, die beschädigt oder mit fehlenden Bytes
  ankommen konnten.
- **Klarere Fehlermeldungen**, wenn ein E-Mail-Postfachordner nicht abgerufen
  werden kann, statt eines generischen Fehlers.

## Extraction Service — live: `1.49.6`

- **Abstürze behoben** bei Dokumenten mit nicht erkanntem Dokumenttyp und bei
  Tabellen mit ungewöhnlicher/fehlerhafter Struktur.
- Widerstandsfähiger gegenüber kurzen Datenbankverbindungsabbrüchen
  mitten in einer Abfrage.
- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.

## FTP Service — live: `1.30.3`

- Nur ein internes Framework-Upgrade in diesem Zeitraum.

## Fulltext Service — live: `1.36.3`

- **Suchindexierung:** Ein periodischer Durchlauf repariert jetzt alle
  Dokumente, die für eine Organisation nicht in den Suchindex gelangt sind.
- **ERP-Synchronisierung:** Eine hängende Sperre behoben, die die
  ERP-Synchronisierung nach einem fehlgeschlagenen Wiederholungsversuch
  blockieren konnte.

## OCR Service — live: `1.7.8`

- **OCR-Authentifizierung behoben**, sodass Organisations-API-Schlüssel
  wieder korrekt funktionieren.
- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.

## Operator Service — live: `1.39.7`

- Nur interne Zuverlässigkeitskorrekturen für Deployments in diesem Zeitraum.

## PO Match Service — live: `1.56.0`

- **Einen Absturz behoben** beim Sortieren von PO-Match-Mengen, die leere
  Werte enthielten.
- **Zero-Downtime-Deployments:** Laufende Anfragen werden jetzt abgeschlossen,
  bevor ein Release den Service neu startet.

## Web App — live: `10.36.9`

- **Einen Fehler behoben** bei der Rückkehr zur Feldvalidierung von einem
  anderen Bildschirm aus.
- **Die Schaltfläche „Scripts“ behoben**, die auf eine 404-Seite führte.
- **Aktivitätsprotokolle:** Eine falsche Anzeige „Seite 2 von 1“ behoben und
  behoben, dass der WARN-Schweregradfilter keine Treffer fand.

---

## Keine für Kunden sichtbaren Änderungen in diesem Zeitraum

Auth Service, Barcode Service, FTP Service, Operator Service und Docnet
Service (`1.54.6`, unverändert) erhielten nur interne oder
Bereitstellungskonfigurations-Wartung.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
