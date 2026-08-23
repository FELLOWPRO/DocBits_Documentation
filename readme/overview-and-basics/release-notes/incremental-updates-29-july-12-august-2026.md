# DocBits Release-Notizen — 29. Juli – 12. August 2026

_Was sich mit dem DocBits-Produktions-Upgrade geändert hat, das am 10.–12.
August 2026 ausgerollt wurde — alles seit dem Release vom 29. Juli. Jeder
Service unten zeigt die Version, die live gegangen ist, gefolgt von dem, was
neu oder behoben ist, in klarer Sprache. Nicht aufgeführte Services (Auto
Accounting `1.21.1`, Ideas `0.3.1`, OCR `1.10.3`, Operator `1.42.1`, PO Match
`1.59.3`, FTP `1.32.4`) hatten keine für Kunden sichtbaren Änderungen._

---

## Highlights

- **FacturaE-Unterstützung.** Spanische FacturaE-3.1-E-Rechnungen werden ohne
  weitere Einrichtung klassifiziert und extrahiert, mit vollständigen
  Feldzuordnungen. In derselben Welle wurden die ebInterface-Mappings
  (Österreich) versionstreu, die Factur-X- und ZUGFeRD-Standards erhielten den
  Pfad für den Firmennamen, und mehrere falsche Standard-Mappings für Rabatte,
  Umsatzsteuer und Einzelpreise wurden korrigiert.
- **Dashboard-Suche und -Sortierung repariert.** Die Sortierung hängt nicht
  mehr davon ab, welche Spalten gerade sichtbar sind, ein OR-Filter in
  Kombination mit einer Bereichs- oder Gleichheitsbedingung löscht die
  Suchbegriffe nicht mehr, Lieferantennamen erscheinen wieder in der
  Schnellsuche, und ISO-formatierte Daten werden korrekt gelesen.
- **KI-Extraktion korrigiert sich selbst.** Ein nachweisbarer Tausch von
  Netto- und Gesamtbetrag durch die KI wird automatisch rückgängig gemacht,
  per KI gescannte Felder kommen nach einem Dokument-Neustart nicht mehr
  falsch zurück, und die KI-Tabellenextraktion verarbeitet Dokumente in
  Seiten-Batches, sodass lange Tabellen vollständig ankommen.
- **Workflows überstehen einen Auth-Aussetzer.** Ein kurzzeitig nicht
  erreichbarer Auth-Service wird erneut versucht, statt den Lauf fehlschlagen
  zu lassen, und ein Workflow-Trigger, der sich nicht authentifizieren kann,
  meldet den Fehler, statt das Dokument hängen zu lassen.
- **Schwer lesbare PDFs werden wieder extrahiert.** Wenn der
  Standard-PDF-Textdecoder eine Seite nicht lesen kann (häufig bei mit
  Ghostscript erzeugten Dateien), fällt die Extraktion auf eine zweite Engine
  zurück, statt nichts zu liefern.
- **MFA funktioniert über Regionen hinweg.** Die Registrierungsdaten der
  Zwei-Faktor-Authentifizierung werden zwischen der EU- und der US-Region
  repliziert, sodass ein in einer Region eingerichteter zweiter Faktor auch
  in der anderen anerkannt wird.

---

## Web App — `10.49.4`

### Anmeldung und Konten

- Wer sich in einem Browser-Tab abmeldet, wird auch in den anderen Tabs
  abgemeldet — ohne die Fehlermeldungen, die bisher erschienen, wenn die Tabs
  sich über die Sitzung uneinig waren.
- Das Ändern des eigenen Passworts im Profil läuft über den dedizierten
  Self-Service-Endpunkt und funktioniert damit ohne Admin-Berechtigungen.
- Die Passkey-Anmeldung aus der Nicht-Heimatregion zeigt übersetzte
  Fehlermeldungen, und ihre Absenden-Schaltfläche ist sichtbar.

### Validierungsbildschirm

- Der Tab „Extracted table“ dreht sich nicht mehr endlos, wenn bereits eine
  KI-Tabelle existiert.
- Dokumente, deren Barcode-Daten fehlen, bringen die Ansicht für die
  Barcode-Zuordnung nicht mehr zum Absturz.
- M3-Mehrfachsteuer-Zeilen bieten den Steuercode als Dropdown aus der
  Werteliste an statt als Freitextfeld.
- Große Lieferantenrechnungen öffnen sich spürbar schneller.

### Aufgaben

- Kanban-Spalten laden beim Scrollen seitenweise nach, sodass Boards mit
  vielen Aufgaben schnell aufbauen.
- Der Zähler offener Aufgaben in der Seitenleiste zählt Aufgaben im Kontext
  Ihrer Unterorganisation — nicht im Kontext des Dokuments, das gerade
  geöffnet ist.

### Workflow Builder

- Die Workflow-Liste behält Ihre Suche, Sortierung, Seite und Seitengröße,
  wenn Sie einen Workflow öffnen und zurückkehren — auch über die Breadcrumb.
  Die Seite öffnet standardmäßig auf dem Tab „List“.

### Einstellungen und Administration

- Die Stammdaten-Seite bleibt nicht mehr wegen einer Sortier-Wettlaufbedingung
  leer, und das Sortieren nach Badges bringt die Seite nicht mehr zum
  Absturz.
- Ein Abonnement im Status „cancelling“ lässt sich fortsetzen.
- Die XSLT-Detailseite meldet Ladefehler, statt nichts anzuzeigen, und die
  Einstellungen für E-Mail-Benachrichtigungen nutzen die volle Seitenbreite
  mit einem funktionierenden Log-Bereich.
- Die Organisationsauswahl für Benutzer mit mehreren Organisationen hat
  korrektes Zeilenlayout, passende Größen und Theme-Farben, scrollt richtig
  und bietet einen Filter für Konten mit vielen Organisationen.
- Analytics: Eine fehlgeschlagene Metrik-Abfrage zeigt einen Fehlerzustand,
  statt Nullen zu rendern, und die Nutzungs-Widgets melden ehrlich, wenn
  keine Messdaten vorliegen.
- Veraltete Cache-Optionen wurden von der Cache-Verwaltungsseite entfernt,
  und die Seiten „Benutzer“ und „Gruppen“ haben ihre verschachtelten
  doppelten Scrollleisten verloren.
- „Use Default Template“ im Layout-Manager stürzt nicht mehr ab und bleibt
  nicht mehr ohne Reaktion; die Funktion behauptet auch nicht mehr, es gebe
  kein Standard-Layout.
- Auswahlregeln behalten ihre Operatoren für Textabgleich, Vorhandensein und
  Regex, wenn eine Regel erneut geöffnet wird.
- Dokumenttypen unterstützen Transformationsregeln pro Typ, und die
  Regelliste erhielt eine Aktion zum Setzen eines festen Werts.
- Bestellstatus-Badges werden auch für Statuswerte in ERP-Schreibweise
  korrekt zugeordnet.
- Die DocNet-Bildschirme (AI Workforce) einschließlich des Agent Wizard sind
  übersetzt, und der Dialog zum Anlegen und Bearbeiten von Ideen scrollt
  horizontal.
- Lieferantenportal-Angebote: Verwaltete Mengeneinheiten erscheinen in der
  Positionstabelle, das Freigabe-Styling gilt nur für Vertragsangebote, und
  die Vergleichszeile erscheint nicht mehr, wenn beide Werte identisch sind.
- Der JSON-Fallback der Fehlerseite ist im Dark Mode lesbar, und Berichte
  verwenden eine richtige Beschriftung „letzte 7 Tage“ statt einer
  verlorenen „7“.

## API Service — `12.74.0`

### Dashboard und Suche

- Die Sortierung funktioniert unabhängig davon, welche Spalten sichtbar sind,
  und ein Suchbegriff, den die Suche an die Volltextsuche delegiert,
  hinterlässt kein kaputtes SQL-Fragment mehr.
- Lieferantennamen erscheinen wieder in der Schnellsuche — auch für
  Organisationen ohne Volltext-Indexierung.
- ISO-formatierte Daten (2026-08-12) werden vom Tag-zuerst-Datumsnormalisierer
  nicht mehr falsch gelesen.
- Dashboard-Exporte leiten reine Textwerte wie Rechnungsnummern in die
  richtige Spalte.

### E-Rechnungen

- FacturaE 3.1 (Spanien): Klassifizierungsregel und vollständige
  Feldzuordnungen.
- XRechnung-Klassifizierungsregeln sind an ihre Syntaxfamilie gebunden,
  sodass ein UBL-Dokument nicht mehr von CII-Regeln erfasst wird und
  umgekehrt.
- Die akzeptierte Version „3.0“ deckt ihre gesamte Patch-Familie ab (3.0.1,
  3.0.2).
- CII-Rechnungen übernehmen den rechtlichen Namen des Lieferanten; der
  Handelsname dient nur noch als Fallback.
- Die ebInterface-Mappings (Österreich) sind versionstreu, mit korrigierter
  Catch-all-Zuordnung und neu aufgebauten Fixtures.
- Die Factur-X- und ZUGFeRD-Standards erhielten den Extraktionspfad für den
  Firmennamen, und die Standard-Header-Transformationen für Steuersatz,
  Rechnungstyp und Tier-3-Felder wurden korrigiert — ebenso die familienweite
  Semantik für Rabatte, Umsatzsteuer und Einzelpreise.
- Steuerkategorie-Codes aus dem Quelldokument werden nicht mehr blind auf
  Ihre ERP-Codes abgebildet.
- Dokumente, die sowohl „Rechnung“ als auch „Gutschrift“ erwähnen, bevorzugen
  die Gutschrift-Klassifizierung.

### Dokumente und Extraktion

- Wenn der Standard-PDF-Decoder den eingebetteten Text einer Seite nicht
  lesen kann, fällt die Extraktion auf eine zweite Engine zurück — betroffene
  PDFs werden also extrahiert, statt leer zurückzukommen.
- Der Hauptschalter für Barcodes heißt jetzt `BARCODE_EXTRACTION`; die alte
  QR-Code-Einstellung funktioniert als Alias weiter.
- Ein Speicherleck im Hintergrund-Scheduler wurde gestopft; es verlangsamte
  die Verarbeitung über Tage der Laufzeit hinweg schleichend.
- Lieferanten, die ohne Land importiert werden, bleiben leer, statt
  standardmäßig auf Deutschland gesetzt zu werden.

### Export und Stammdaten

- „Save Rules“ meldet einen Fehler, wenn nichts geschrieben wurde, statt
  Erfolg zu behaupten.
- Positionen mit Betrag null werden nicht mehr aus Auto-Accounting-Exporten
  entfernt, und ein Filter, der auf jeden Bucket passte, wurde korrigiert.
- M3-Exporte unterstützen Additional-Info-Post-Hooks.
- Eine einzelne fehlschlagende Datensatz-Prüfung leert nicht mehr den
  gesamten Stammdaten-Bildschirm.
- PO-Caches werden invalidiert, wenn das ERP den Status einer Bestellung
  aktualisiert — das Dashboard zeigt also nicht mehr den veralteten Stand.

### Administration

- Jede Einstellung zeigt, welcher Benutzer sie zuletzt geändert hat.
- Extraktionsregeln können pro Lieferant gelöscht und über neue Endpunkte
  geklont werden.
- Empfänger von Status-Alarm-E-Mails werden NULL-sicher verglichen — das
  behebt einen Absturz beim Versand von Benachrichtigungen.

## Auth Service — `1.75.9`

- Ein Organisations-API-Schlüssel, der gegen eine fremde Organisation
  verwendet wird, wird abgewiesen.
- Das Anlegen einer Organisation lieferte einen Fehler zurück, obwohl der
  Datensatz tatsächlich gespeichert wurde; jetzt antwortet es korrekt.
- Die Anmeldung mit einem Passkey, obwohl keiner registriert ist, liefert
  einen eigenen Fehlercode, sodass der Anmeldebildschirm sagen kann, was
  nicht stimmt.

## Auth Bridge Service — `0.4.2`

- Die Tabellen der Zwei-Faktor-Registrierung werden zwischen der EU- und der
  US-Region repliziert, und Zeilen werden über ihren echten Primärschlüssel
  identifiziert.

## Docflow Service — `2.8.7`

- Ein Workflow-Trigger, der sich nicht authentifizieren kann, meldet den
  Fehler, statt das Dokument hängen zu lassen, und ein kurzzeitig nicht
  erreichbarer Auth-Service wird erneut versucht, statt als ungültiges Token
  behandelt zu werden.
- Angebotsvergleichs-Karten: Artikelnummern werden nur für Zeilen verglichen,
  die die Artikelpreis-Matrix beschreibt; Zeilen ohne Mengeneinheit oder ohne
  Preis werden übersprungen, statt den Vergleich fehlschlagen zu lassen.
- Die Karte für den Vertragspreis-Vergleich erhielt eine Any/All-Option für
  den Operator, und Karten-Caches werden nach Migrationen und Code-Updates
  korrekt invalidiert.
- Abgerissene SSL-Verbindungen werden als vorübergehend behandelt und erneut
  versucht, statt den Lauf fehlschlagen zu lassen.

## Docnet Service — `1.56.4`

- Health- und Versions-Endpunkte blockieren nicht mehr auf Live-Prüfungen —
  das ließ den Dialog „Service Versions“ bisher hängen.

## Email Service — `1.40.6`

- Wird eine eingehende E-Mail übersprungen, steht der Grund jetzt in der
  Zeile des Import-Ereignisses, statt verschwiegen zu werden.
- Angehängte `.eml`-Containerdateien werden nicht mehr als Dokumente
  importiert.
- Eine fehlgeschlagene Microsoft-Office-Anmeldung erzeugt eine lesbare
  Fehlermeldung, und ein Transportfehler des KI-Service zählt als „unklar“
  statt als Ablehnung.

## Extraction Service — `1.53.8`

- Ein nachweisbarer Tausch von Netto- und Gesamtbetrag durch die KI wird nach
  der Feldextraktion rückgängig gemacht, und Fehlschläge dieser Prüfung
  werden protokolliert, statt still durchzugehen.
- Per KI gescannte Felder kommen nach einem Dokument-Neustart nicht mehr
  falsch zurück.
- Die KI-Tabellenextraktion arbeitet in Seiten-Batches und sammelt alle
  Batches ein, sodass lange Tabellen vollständig ankommen.
- Dokumente, die sowohl „Rechnung“ als auch „Gutschrift“ erwähnen, bevorzugen
  die Gutschrift-Klassifizierung.
- Die wiederholte Bereinigung von Kopf- und Fußzeilen wird zwischengespeichert,
  was die Extraktion mehrseitiger Dokumente beschleunigt.

## Fulltext Service — `1.41.7`

- Ein OR-Filter in Kombination mit einer Bereichs- oder Gleichheitsbedingung
  löscht die Suchbegriffe nicht mehr.
- Die Sortierung verwendet die korrekten Indexpfade und zeigt den
  tatsächlichen Grund, wenn das Such-Backend eine Abfrage ablehnt; eine
  Sortier-Regression, die die Raw-Query-Suche komplett unbrauchbar machte,
  wurde noch in derselben Woche behoben, in der sie auftrat.
- Dokument-Lookups funktionieren auch auf älteren text-gemappten Indizes.
- Der Token-Cache ist auf das Paar aus Token und Organisation begrenzt,
  sodass ein Organisationswechsel keine Ergebnisse mehr unter dem vorherigen
  Kontext liefern kann.
