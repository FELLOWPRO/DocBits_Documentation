# DocBits Release-Notizen — 3.–4. Juli 2026

_Was dieses Produktions-Upgrade gebracht hat, in verständlicher Sprache. Bei jedem
Service ist die Version angegeben, die jetzt in der Produktion live ist. Nicht
aufgeführte Services hatten in diesem Zeitraum keine für Kunden sichtbaren
Änderungen._

---

## Highlights

- **Sauberere Deploys, fleet-weit.** Mehrere Kern-Services (API, Auto Accounting,
  Docflow, Extraction, OCR, PO Match) fahren jetzt bei einem Release korrekt
  herunter, sodass ein rollierendes Deployment keine bereits laufende Anfrage
  mehr abbricht.
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
- Allgemeine Stabilitätskorrekturen zur Behebung mehrerer wiederkehrender
  Hintergrundfehler.

## Auth Service — live: `1.68.7`

- Nur interne Zuverlässigkeits- und Wartungsarbeiten in diesem Zeitraum.

## Auto Accounting — live: `1.18.8`

- **Sauberere Shutdowns** bei Deployments, wodurch unterbrochene laufende
  Anfragen vermieden werden.

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
- Sauberere Shutdowns bei Deployments.

## Operator Service — live: `1.39.7`

- Nur interne Zuverlässigkeitskorrekturen für Deployments in diesem Zeitraum.

## PO Match Service — live: `1.56.0`

- **Einen Absturz behoben** beim Sortieren von PO-Match-Mengen, die leere
  Werte enthielten.
- Sauberere Shutdowns bei Deployments.

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
