# DocBits Release-Notizen — 14.–23. Juli 2026

_Was sich mit dem DocBits-Produktions-Upgrade am 23. Juli 2026 (dem Update des
Nova-Kanals) geändert hat — alles seit dem Release vom 14. Juli. Jeder Service
unten zeigt die jetzt aktive Version, gefolgt von dem, was neu oder behoben
ist, in klarer Sprache. Nicht aufgeführte Services hatten keine für Kunden
sichtbaren Änderungen._

---

## Highlights

- **Support-Tickets direkt aus dem Fehlerbildschirm.** Wenn etwas schiefgeht,
  können Sie jetzt direkt aus dem Fehlereintrag ein Support-Ticket eröffnen.
  Das Ticket enthält den technischen Kontext bereits — Sie müssen ihn nicht
  mehr beschreiben.
- **E-Mail-Eingang in der richtigen Region.** US-Organisationen erhalten
  Import-Adressen für eingehende E-Mails in ihrer eigenen Region, und
  Microsoft-365-Postfächer auf nationalen Cloud-Tenants (GCC, 21Vianet und
  ähnliche) lassen sich jetzt über eine Cloud-Instance-Auswahl konfigurieren.
- **Klarerer PO-Matching-Status.** Rechnungen, deren Positionstabelle nicht
  zugeordnet werden konnte, trugen bisher den Status „Bestellung nicht
  gefunden“ — und schickten Anwender auf die Suche nach dem falschen Problem.
  Sie erhalten jetzt einen eigenen Status „Tabelle unvollständig“ mit Details
  auf Spaltenebene, was nicht zugeordnet werden konnte.
- **Steuercode-Zuordnung für E-Dokumente.** Eine neue Einstellungsseite ordnet
  Ihre ERP-Steuercodes für elektronische Dokumente zu, und Exporte prüfen die
  Zuordnung vorab, statt erst im ERP zu scheitern.
- **Skriptänderungen sind passwortgeschützt.** Eigene Skripte können die
  Dokumentverarbeitung verändern, deshalb erfordert jede Skriptänderung jetzt
  ein Passwort, das stündlich wechselt. Das aktuelle Passwort erhalten Sie von
  Ihrem Administrator.
- **Turbo-KI-Stufe eingestellt.** Das Turbo-Modell hat sein Lebensende
  erreicht. Wer es ausgewählt hatte, wurde automatisch auf Fast umgestellt; es
  ist nichts zu tun.

---

## Web App — live: `10.45.1`

### Arbeiten mit Dokumenten

- **Gelöschte Dokumente:** Das Öffnen eines zwischenzeitlich gelöschten
  Dokuments zeigt eine verständliche Meldung statt Skriptfehlern.
- **Feldvalidierung:** Das Eingabefeld für die Seitenzahl ist breiter und
  springt mit Enter zur gewählten Seite. Ein per Skript schreibgeschütztes
  Feld zeigt weiterhin seine Feldverbindung.
- **Tabellenextraktion:** Das Löschen einer Spalte gibt ihren Namen zur
  Wiederverwendung frei, und gelöschte Überschriften tauchen nicht mehr in
  der gespeicherten Tabelle auf.
- **Freigaben:** Benutzer können keinen Sales-Tax-Schritt mehr freigeben, für
  den ihre Gruppe keine Berechtigung hat, und die Freigabehistorie zeigt
  wieder alle Einträge. Die Historie nennt außerdem die Person, die
  tatsächlich freigegeben hat, einschließlich Freigaben, die ein Admin
  stellvertretend für den Bearbeiter erteilt hat.
- **Lieferanten:** Die Accounting-Seite zeigt keine falsche Warnung
  „Supplier is missing“ mehr an, und das Löschen eines Lieferanten, der nur
  aus der Extraktion stammt, lässt den Dialog nicht mehr hängen.
- **Aufgaben und Benachrichtigungen:** Die Löschoption wird für Benutzer ohne
  Admin-Rechte ausgeblendet.

### Dashboard und Suche

- **Export:** Exporte verwenden das tatsächlich ausgewählte Dashboard, und
  die App warnt, bevor Sie ein Dashboard mit ungespeicherten Änderungen
  exportieren.
- **Suche:** Der Rechnungstyp (Invoice Type) steht als Suchfeld mit seiner
  Werteliste zur Verfügung.
- **Importprotokoll:** Aufgeteilte Dokumente lassen sich über ihr
  übergeordnetes Dokument finden, und die Spalte „Failed Filenames“ listet
  nur noch Dateien, die tatsächlich fehlgeschlagen sind oder übersprungen
  wurden.

### Anmeldung

- **Gelöschte Konten:** Die Anmeldung mit einem gelöschten Konto sagt das
  jetzt auch, statt mit einem generischen Fehler fehlzuschlagen.
- **SSO:** Fehler behoben, der beim Anmelden auftrat, während eine andere
  Region ausgewählt war.

### Einstellungen und Administration

- **Support-Tickets:** Erstellen Sie ein Ticket direkt aus einem
  Fehlereintrag. Tickets enthalten Umgebung und Release-Kanal, und die
  Screenshot-Aufnahme bleibt nicht mehr hängen.
- **Workflow Builder:** Neu erstellte oder umbenannte Karten, E-Mail-Vorlagen
  und andere Dropdown-Einträge erscheinen sofort — ohne die Seite neu zu
  laden.
- **Dokumenttypen:** Neue Einstellung „Structured Extraction“ im
  Extraktionsbereich.
- **E-Doc-Steuercodes:** Neue Einstellungsseite zur Zuordnung Ihrer
  ERP-Steuercodes für elektronische Dokumente (siehe Highlights).
- **KI-Modellauswahl:** Die eingestellte Turbo-Stufe ist aus dem Dropdown
  verschwunden; bestehende Auswahlen zeigen Fast.
- **Dialog „Service-Versionen“:** Jetzt scrollbar, enthält den Auth Bridge
  Service und zeigt die Release-Kanal-Namen Vesta und Nova.
- **Import-Seite:** Stürzt bei Organisationen mit leerem Abonnement-Eintrag
  nicht mehr ab.

### Kleinere Korrekturen

Leere Toast-Benachrichtigungen werden unterdrückt, der Dialog zum Erstellen
und Bearbeiten von Ideen scrollt, verrutschte Checkboxen in den
Feldeinstellungen sind wieder ausgerichtet, blockierte Dokumentlöschungen
erklären den Grund, und die E-Dokument-Einstellungen verarbeiten den Wechsel
von Default zu Custom sauber.

## API Service — live: `12.64.3`

- **Skript-Sicherheit:** Skriptänderungen erfordern ein zeitbasiertes
  Passwort (siehe Highlights).
- **E-Doc-Steuercodes:** ERP-Steuercode-Zuordnung für elektronische
  Dokumente, mit einer zentralen Prüfung vor dem Export, damit fehlende
  Codes früh auffallen.
- **Zugriffssteuerung:** Admins können Benutzern ohne Admin-Rechte Einsicht
  in nicht klassifizierte Dokumente gewähren.
- **Persönliche Dashboards:** Freigabe-Einstellungen, die sich nicht
  speichern ließen, sind behoben.
- **Dashboard-Suche:** Der Rechnungstyp gehört jetzt zu den erweiterten
  Suchfeldern, und Dokumente aus einer Barcode- oder QR-Aufteilung werden
  über ihr übergeordnetes Dokument gefunden.
- **Uploads:** Wiederholte Uploads derselben Datei während eines
  Netzwerk-Retrys erzeugen keine doppelten Dokumente mehr.
- **Lieferanten-Lookup:** Ergebnisse kommen, sobald die Daten bereitstehen,
  statt nach einer festen Wartezeit.
- **Infor-Export:** Stückpreise behalten vier Nachkommastellen. M3-Exporte
  können Positionszuschläge mit Betrag null enthalten, und negative
  LN-Kostenzeilen werden als positive Gutschriften gesendet.
- **Freigaben:** Eine Freigabe wird nur dann mit einer Freigabeanforderung
  verknüpft, wenn der Freigebende auch ihr Bearbeiter ist.
- **Anmeldestabilität:** Ein vorübergehender Fehler in der Token-Prüfung
  meldet Benutzer nicht mehr ab; die App versucht es stattdessen erneut.
- **Klassifizierung:** Quellregeln prüfen jetzt gegen jedes
  Dokumentquellen-Feld, nicht gegen feste Positionen.
- **Validierungsstabilität:** Ein Feld ohne Namen bringt die
  Dokumentvalidierung nicht mehr zum Absturz.
- **KI-Modelle:** Die eingestellte Turbo-Stufe wird überall auf Fast
  umgestellt, inklusive feinabgestimmter Varianten — mit einer Absicherung,
  dass ein eingestelltes Modell nie ausgeführt werden kann.

## Auth Service — live: `1.72.8`

- **Anmeldehistorie:** Anmeldungen über SSO/SAML erscheinen jetzt in der
  Anmeldehistorie, und der Zeitstempel der letzten Anmeldung wird bei jedem
  Anmeldetyp zuverlässig gesetzt. Die Anmeldehistorie eines anderen
  Benutzers einzusehen erfordert die passende Admin-Stufe.
- **Legacy-Konten:** Das Löschen eines Legacy-Benutzerkontos funktioniert
  wieder, statt stillschweigend nichts zu bewirken.
- **Benutzerverwaltung im Stapel:** Bestehende Benutzer lassen sich per CSV
  gesammelt zu Unterorganisationen und Gruppen hinzufügen, zugeordnet über
  die E-Mail-Adresse. Außerdem behoben: ein Absturz bei ungleichmäßig
  gefüllten CSV-Zeilen und ein Serverfehler beim gleichzeitigen Hinzufügen
  von zwei oder mehr neuen Benutzern.
- **Mitgliederlisten:** Gelöschte Benutzer erscheinen nicht mehr in den
  Mitgliederlisten von Unterorganisationen.
- **Single Sign-on:** Eine Reihe von Härtungskorrekturen. Abgelaufene Tokens
  liefern jetzt eine saubere „abgelaufen“-Antwort, Organisationen ohne
  SAML-Konfiguration erhalten eine korrekte Nicht-gefunden-Antwort statt
  eines falschen Anmeldeflusses, die Abmeldung wird immer abgeschlossen —
  auch wenn die Abmeldeanfrage nicht verifiziert werden kann — und mehrere
  Abstürze rund um fehlende Identity-Provider-Konfiguration sind beseitigt.
- **Sitzungstokens:** Behoben, dass kurzlebige Sitzungstokens als ungültig
  abgelehnt wurden, obwohl sie nicht abgelaufen waren.
- **Verwaltungswerkzeuge:** Die Region einer Organisation ist in der
  Verwaltungs-API sichtbar, der Systembenutzer einer Organisation kann neu
  zugewiesen werden, und die Plan- und Nutzungsverwaltung hat eigene
  Endpunkte erhalten. Diese Änderungen betreffen interne DocBits-Werkzeuge,
  nicht die Kunden-App.

## Email Service — live: `1.39.9`

- **Import in der richtigen Region:** Eingangs-E-Mail-Domains existieren pro
  Region, und Mails, die in der falschen Region ankommen, werden in die
  richtige weitergeleitet. US-Organisationen hängen nicht mehr am
  EU-Eingangspfad.
- **Microsoft 365:** Nationale Cloud-Tenants werden über eine
  Cloud-Instance-Auswahl konfiguriert — das repariert O365-Importe für
  US-Kunden. Ein ungültiger Tenant erzeugt jetzt einen klaren Anmeldefehler
  statt eines Serverfehlers, und unvollständige Tenant-Zugangsdaten schlagen
  sofort mit einer Meldung fehl, statt still zu scheitern.
- **Posteingangs-Hygiene:** E-Mails ohne Anhang werden aus dem Posteingang
  verschoben, statt sich dort zu stapeln.
- **Keine Duplikate bei Wiederholungen:** Uploads zur Dokument-API tragen
  einen Idempotenz-Schlüssel — eine wiederholte Zustellung kann dasselbe
  Dokument nicht zweimal anlegen.
- **Quellenbenennung:** O365-Quellen mit konfiguriertem Ordner enthalten die
  Konto-E-Mail im Namen, damit ähnliche Quellen unterscheidbar sind.
- **Importprotokoll-Aufräumung:** Einträge im Importprotokoll werden 90 Tage
  aufbewahrt und danach automatisch bereinigt.

## PO Match Service — live: `1.59.1`

- **Status „Tabelle unvollständig“:** Rechnungen, deren Positionstabelle
  nicht zugeordnet werden konnte, erhalten einen eigenen Status statt des
  irreführenden „Bestellung nicht gefunden“ (siehe Highlights). Das Dashboard
  zeigt ihn mit dem Nicht-zugeordnet-Symbol.
- **Bessere Fehlerdetails:** Fehler bei der Tabellenzuordnung benennen die
  konkrete Spalte, die nicht zugeordnet werden konnte.
- **Sauberes API-Verhalten:** Anfragen nach nicht vorhandenen PO-Regeln
  liefern eine korrekte Nicht-gefunden-Antwort, und beschädigte
  Cache-Einträge werden verworfen, statt wiederholte Fehler zu verursachen.
- **Abgleich über die Gesamtsumme:** Fehler beim Abgleich gegen die
  Bestellsumme behoben.

## Fulltext Service — live: `1.38.3`

- **Europäische Zahlenformate:** Beträge mit Dezimalkomma (`1.234,56`) werden
  vor der Indexierung normalisiert — Betragssuchen und -filter funktionieren
  damit unabhängig vom Zahlenformat.
- **ERP-Zähler:** Token-Fehler behoben, der den Live-Zählerstrom auf dem
  Dashboard unterbrechen konnte.
- **Robuste Indexierung:** Die Indexierung übersteht jetzt vorübergehende
  Aussetzer von Datenbank und Auth Service (automatischer Retry, Fallback auf
  die primäre Datenbank) und verwirft fehlerhafte Queue-Nachrichten, statt
  sie endlos zu wiederholen.

## OCR Service — live: `1.9.9`

- **Große Dokumente:** Das OCR-Zeitbudget skaliert mit der Dokumentgröße —
  sehr große Dateien scheitern nicht mehr an einem Timeout.
- **Ungewöhnliche Zeichen:** Ein Bereinigungsschritt entfernt Zeichen, die
  die OCR-Engine nicht darstellen kann, und behebt damit Fehler bei
  Dokumenten mit exotischen Symbolen.
- **Weniger vorübergehende Fehler:** Temporäre Verbindungsfehler zum Speicher
  werden automatisch wiederholt.

## Extraction Service — live: `1.52.0`

- **US-Rechnungen ohne Steuer:** Fall behoben, in dem das korrekte
  Netto/Steuer-Paar verworfen wurde, wenn der Steuerbetrag null ist.
- **Tabellenextraktion:** Tabellen bleiben bearbeitbar, wenn die
  konfigurierte Zuordnung mehr Spalten erwartet, als das Dokument liefert,
  und ein Absturz bei ungewöhnlichen Zeilendaten ist behoben.
- **KI-Modelle:** Einstellung der Turbo-Stufe, übernommen vom API Service.

## Docflow Service — live: `2.7.2`

- **PO-Matching in Workflows:** Fehlende Vergleichswerte werden als fehlende
  Daten behandelt, nicht als Abweichung.
- **Auftragsbestätigungs-Karten:** Einkäufer und verantwortliche Person
  werden zuverlässig aufgelöst.
- **Frachtkosten:** Wenn keine der beiden Seiten Kosten ausweist, wird der
  Fall über die Operator-Karte gelöst, statt hängen zu bleiben.
- **Sicherheit:** Workflow-API-Tokens werden gegen die Organisation geprüft,
  zu der sie gehören.
- **Schnelleres Auslösen:** Die Prüfung auf aktive Workflows wird
  zwischengespeichert, und die Hintergrund-Worker starten sauber neu, statt
  hängende Prozesse zu hinterlassen.

## Barcode Service — live: `1.17.4`

- **Lang laufende Aufteilungen:** Die Verbindung zur Task-Queue wird bei
  langen Barcode-Jobs offen gehalten — das Aufteilen großer Stapel bleibt
  damit nicht mehr kurz vor dem Ende stehen.

## FTP Service — live: `1.31.2`

- **Importprotokoll-Aufräumung:** Dieselbe 90-Tage-Aufbewahrung und
  automatische Bereinigung wie beim Email Service.

---

## Unverändert in diesem Release

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) und **Ideas** (`0.3.1`) enthalten in
diesem Zeitraum keine Änderungen.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
