# DocBits Release-Notizen — 14.–29. Juli 2026

_Was sich mit dem DocBits-Produktions-Upgrade am 29. Juli 2026 (dem Update des
Nova-Kanals) geändert hat — alles seit dem Release vom 14. Juli. Jeder Service
unten zeigt die jetzt aktive Version, gefolgt von dem, was neu oder behoben
ist, in klarer Sprache. Nicht aufgeführte Services hatten keine für Kunden
sichtbaren Änderungen._

---

## Highlights

- **Zwei-Faktor-Authentifizierung.** DocBits-Konten lassen sich jetzt mit einem
  zweiten Faktor schützen: einer Authenticator-App (TOTP), einem Einmalcode per
  E-Mail oder einem Passkey über Touch ID, Windows Hello, YubiKey und
  Ähnliches. Backup-Codes decken den Fall eines verlorenen Geräts ab, und ein
  vertrauenswürdiges Gerät kann den zweiten Faktor eine Zeit lang überspringen.
  Jeder Benutzer kann die Funktion für sich selbst einschalten; Administratoren
  können sie für die gesamte Organisation verpflichtend machen. Siehe den
  [Leitfaden zur Zwei-Faktor-Authentifizierung](../two-factor-authentication.md).
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
- **Turbo-KI-Stufe eingestellt.** Das Turbo-Modell hat sein Lebensende
  erreicht. Wer es ausgewählt hatte, wurde automatisch auf Fast umgestellt; es
  ist nichts zu tun.

---

## Web App — live: `10.46.2`

### Anmeldung

- **Zwei-Faktor-Authentifizierung:** Richten Sie in Ihrem Profil eine
  Authenticator-App, E-Mail-Codes oder einen Passkey ein, drucken Sie
  Backup-Codes aus und markieren Sie ein Gerät als vertrauenswürdig, damit
  nicht jedes Mal nachgefragt wird. Wer einen Passkey nutzt, kann sich ganz
  ohne Passwort anmelden. Administratoren einer Organisation erhalten einen
  Schalter, um die Funktion verpflichtend zu machen, sowie eine Übersicht,
  wer sie bereits eingerichtet hat.
- **Gelöschte Konten:** Die Anmeldung mit einem gelöschten Konto sagt das
  jetzt auch, statt mit einem generischen Fehler fehlzuschlagen.
- **SSO:** Fehler behoben, der beim Anmelden auftrat, während eine andere
  Region ausgewählt war. SSO-Sitzungen laufen jetzt dann ab, wenn der
  Identitätsanbieter es vorgibt, und nicht nach einem festen lokalen Timer.

### Arbeiten mit Dokumenten

- **Gelöschte Dokumente:** Das Öffnen eines zwischenzeitlich gelöschten
  Dokuments zeigt eine verständliche Meldung statt Skriptfehlern.
- **Field Validation:** Das Eingabefeld für die Seitenzahl ist breiter und
  springt mit Enter zur gewählten Seite. Ein per Skript schreibgeschütztes
  Feld zeigt weiterhin seine Feldverbindung. Ein Warnhinweis, der bisher rohen
  JavaScript-Code ausgab, zeigt jetzt die eigentliche Meldung, und der
  Bildschirm friert bei Dokumenten mit langen E-Dokument-Positionstabellen
  nicht mehr ein.
- **Tabellenextraktion:** Das Löschen einer Spalte gibt ihren Namen zur
  Wiederverwendung frei, und gelöschte Überschriften tauchen nicht mehr in
  der gespeicherten Tabelle auf.
- **Freigaben:** Beim Öffnen eines gerade zur Freigabe anstehenden Dokuments
  landen Sie auf dem richtigen Freigabebildschirm. Benutzer können keinen
  Sales-Tax-Schritt mehr freigeben, für den ihre Gruppe keine Berechtigung
  hat, und die Freigabehistorie zeigt wieder alle Einträge. Die Historie nennt
  außerdem die Person, die tatsächlich freigegeben hat, einschließlich
  Freigaben, die ein Admin stellvertretend für den Bearbeiter erteilt hat.
- **Lieferanten:** Die Accounting-Seite zeigt keine falsche Warnung
  „Supplier is missing“ mehr an, und das Löschen eines Lieferanten, der nur
  aus der Extraktion stammt, lässt den Dialog nicht mehr hängen.
- **Stammdaten:** Tabellen auf der Stammdatenseite lassen sich wieder
  scrollen.
- **Aufgaben und Benachrichtigungen:** Das Löschen einer Aufgabe ist nicht
  mehr Administratoren vorbehalten. Ob Benutzer ohne Admin-Rechte ihre eigenen
  Aufgaben löschen dürfen, ist jetzt eine Einstellung der Organisation, und
  Benutzer mit einer Aufgabe an einem Dokument, das sie nicht öffnen dürfen,
  erhalten eine reine Aufgabenansicht statt einer Fehlermeldung.

### Dashboard und Suche

- **Export:** Exporte verwenden das tatsächlich ausgewählte Dashboard, und
  die App warnt, bevor Sie ein Dashboard mit ungespeicherten Änderungen
  exportieren.
- **Suche:** Der Rechnungstyp (Invoice Type) steht als Suchfeld mit seiner
  Werteliste zur Verfügung. Ist eine Ergebnismenge größer als das Fenster,
  das das Dashboard anzeigen kann, weist die Trefferanzeige jetzt darauf hin,
  statt die Liste stillschweigend abzuschneiden.
- **Importprotokoll:** Aufgeteilte Dokumente lassen sich über ihr
  übergeordnetes Dokument finden, und die Spalte „Failed Filenames“ listet
  nur noch Dateien, die tatsächlich fehlgeschlagen sind oder übersprungen
  wurden.

### Einstellungen und Administration

- **Support-Tickets:** Erstellen Sie ein Ticket direkt aus einem
  Fehlereintrag. Tickets enthalten Umgebung und Release-Kanal, und die
  Screenshot-Aufnahme bleibt nicht mehr hängen.
- **Gruppen und Berechtigungen:** Nicht klassifizierte Dokumente lassen sich
  wie jeder andere Dokumenttyp als Berechtigung vergeben.
- **Workflow Builder:** Neu erstellte oder umbenannte Karten, E-Mail-Vorlagen
  und andere Dropdown-Einträge erscheinen sofort — ohne die Seite neu zu
  laden.
- **Entscheidungsbäume:** Die Bezeichnungen der Dokumentfelder im Designer
  folgen der Sprache der Oberfläche, statt immer den englischen Namen
  anzuzeigen.
- **Dokumenttypen:** Neue Einstellung „Structured Extraction“ im
  Extraktionsbereich.
- **E-Doc-Steuercodes:** Neue Einstellungsseite zur Zuordnung Ihrer
  ERP-Steuercodes für elektronische Dokumente (siehe Highlights).
- **Auto Accounting:** Dimensionen werden zuverlässig angezeigt statt nur
  gelegentlich.
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

## API Service — live: `12.68.1`

- **Zwei-Faktor-Authentifizierung:** Alle passwortbasierten Anmeldewege laufen
  über die Prüfung des zweiten Faktors — keine Integrationsroute umgeht sie.
- **E-Doc-Steuercodes:** ERP-Steuercode-Zuordnung für elektronische
  Dokumente, mit einer zentralen Prüfung vor dem Export, damit fehlende
  Codes früh auffallen.
- **Zugriffssteuerung:** Admins können Benutzern ohne Admin-Rechte Einsicht
  in nicht klassifizierte Dokumente gewähren.
- **Nachweis von Löschungen:** Dokumente halten fest, wer sie wann gelöscht
  hat.
- **Persönliche Dashboards:** Freigabe-Einstellungen, die sich nicht
  speichern ließen, sind behoben.
- **Dashboard-Suche:** Der Rechnungstyp gehört jetzt zu den erweiterten
  Suchfeldern, und Dokumente aus einer Barcode- oder QR-Aufteilung werden
  über ihr übergeordnetes Dokument gefunden.
- **Aktualität des Dashboards:** Das Aktualisieren einer Tabelle oder das
  erneute Verarbeiten eines Dokuments leert den Dashboard-Cache — die Liste
  zeigt damit nicht mehr die Werte von vor der Änderung.
- **Uploads:** Wiederholte Uploads derselben Datei während eines
  Netzwerk-Retrys erzeugen keine doppelten Dokumente mehr.
- **Lieferanten-Lookup:** Ergebnisse kommen, sobald die Daten bereitstehen,
  statt nach einer festen Wartezeit.
- **Infor-Export:** Stückpreise behalten vier Nachkommastellen. M3-Exporte
  können Positionszuschläge mit Betrag null enthalten, und negative
  LN-Kostenzeilen werden als positive Gutschriften gesendet. Der Export
  wartet außerdem auf einen laufenden Workflow, statt mitten im Workflow zu
  starten.
- **Freigaben:** Eine Freigabe wird nur dann mit einer Freigabeanforderung
  verknüpft, wenn der Freigebende auch ihr Bearbeiter ist. Änderungen, die ein
  Workflow von sich aus vorgenommen hat, werden dem Systembenutzer
  zugeschrieben und nicht der Person, die das Dokument zuletzt bearbeitet hat.
- **Anmeldestabilität:** Ein vorübergehender Fehler in der Token-Prüfung
  meldet Benutzer nicht mehr ab; die App versucht es stattdessen erneut. Für
  Dokumente gilt dasselbe — sie scheitern bei einem kurzen Aussetzer der
  Authentifizierung nicht mehr vollständig.
- **Klassifizierung:** Quellregeln prüfen jetzt gegen jedes
  Dokumentquellen-Feld, nicht gegen feste Positionen.
- **Validierungsstabilität:** Ein Feld ohne Namen bringt die
  Dokumentvalidierung nicht mehr zum Absturz.
- **KI-Modelle:** Die eingestellte Turbo-Stufe wird überall auf Fast
  umgestellt, inklusive feinabgestimmter Varianten — mit einer Absicherung,
  dass ein eingestelltes Modell nie ausgeführt werden kann.
- **Hintergrundjobs:** Ein blockierter Scheduler wird erkannt und neu
  gestartet — wiederkehrende Jobs können damit nicht mehr unbemerkt
  aussetzen.

## Auth Service — live: `1.75.3`

- **Zwei-Faktor-Authentifizierung:** Das Backend hinter dem
  Highlights-Eintrag. Authenticator-Apps, Einmalcodes per E-Mail, Passkeys und
  vertrauenswürdige Geräte, dazu Backup-Codes, verpflichtende Aktivierung je
  Organisation und passwortlose Anmeldung per Passkey. Die Einrichtung meldet
  Ihre übrigen Sitzungen ab, eine Passwortänderung entzieht
  vertrauenswürdigen Geräten ihren Status, und die Verifizierungs-Endpunkte
  sind mit Ratenbegrenzung, Sperre und einem Schutz gegen die
  Wiederverwendung von Codes abgesichert.
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
  Die vom Anbieter zurückgegebene Token-Laufzeit wird an die App
  weitergereicht.
- **Sitzungstokens:** Behoben, dass kurzlebige Sitzungstokens als ungültig
  abgelehnt wurden, obwohl sie nicht abgelaufen waren.
- **Verwaltungswerkzeuge:** Die Region einer Organisation ist in der
  Verwaltungs-API sichtbar, der Systembenutzer einer Organisation kann neu
  zugewiesen werden, und die Plan- und Nutzungsverwaltung hat eigene
  Endpunkte erhalten. Diese Änderungen betreffen interne DocBits-Werkzeuge,
  nicht die Kunden-App.

## Email Service — live: `1.40.2`

- **Import in der richtigen Region:** Eingangs-E-Mail-Domains existieren pro
  Region, und Mails, die in der falschen Region ankommen, werden in die
  richtige weitergeleitet. US-Organisationen hängen nicht mehr am
  EU-Eingangspfad.
- **Microsoft 365:** Nationale Cloud-Tenants werden über eine
  Cloud-Instance-Auswahl konfiguriert — das repariert O365-Importe für
  US-Kunden. Ein ungültiger Tenant erzeugt jetzt einen klaren Anmeldefehler
  statt eines Serverfehlers, und unvollständige Tenant-Zugangsdaten schlagen
  sofort mit einer Meldung fehl, statt still zu scheitern.
- **Verbindungstest:** Der Test eines IMAP-Postfachs, das nicht antwortet,
  schlägt nach wenigen Sekunden mit einer Timeout-Meldung fehl, statt in
  einen Gateway-Timeout zu laufen.
- **Posteingangs-Hygiene:** E-Mails ohne Anhang werden aus dem Posteingang
  verschoben, statt sich dort zu stapeln.
- **Keine Duplikate bei Wiederholungen:** Uploads zur Dokument-API tragen
  einen Idempotenz-Schlüssel — eine wiederholte Zustellung kann dasselbe
  Dokument nicht zweimal anlegen.
- **Quellenbenennung:** O365-Quellen mit konfiguriertem Ordner enthalten die
  Konto-E-Mail im Namen, damit ähnliche Quellen unterscheidbar sind. Die
  Postfachadresse wird aus dem authentifizierten Konto gelesen statt aus
  einem manuell befüllten Feld.
- **Importprotokoll-Aufräumung:** Einträge im Importprotokoll werden 90 Tage
  aufbewahrt und danach automatisch bereinigt.

## PO Match Service — live: `1.59.3`

- **Status „Tabelle unvollständig“:** Rechnungen, deren Positionstabelle
  nicht zugeordnet werden konnte, erhalten einen eigenen Status statt des
  irreführenden „Bestellung nicht gefunden“ (siehe Highlights). Das Dashboard
  zeigt ihn mit dem Nicht-zugeordnet-Symbol.
- **Bessere Fehlerdetails:** Fehler bei der Tabellenzuordnung benennen die
  konkrete Spalte, die nicht zugeordnet werden konnte.
- **Schneller bei großen Rechnungen:** Der regelbasierte Abgleich gruppiert
  die Kandidaten nach Artikelnummer und liest die Toleranzeinstellungen
  einmal pro Organisation statt einmal pro Position.
- **Sauberes API-Verhalten:** Anfragen nach nicht vorhandenen PO-Regeln
  liefern eine korrekte Nicht-gefunden-Antwort, und beschädigte
  Cache-Einträge werden verworfen, statt wiederholte Fehler zu verursachen.
- **Abgleich über die Gesamtsumme:** Fehler beim Abgleich gegen die
  Bestellsumme behoben.

## Fulltext Service — live: `1.39.1`

- **Europäische Zahlenformate:** Beträge mit Dezimalkomma (`1.234,56`) werden
  vor der Indexierung normalisiert — Betragssuchen und -filter funktionieren
  damit unabhängig vom Zahlenformat.
- **Ehrliche Trefferanzahl:** Findet eine Suche mehr Dokumente, als das
  Dashboard-Fenster zurückgibt, weist die Antwort darauf hin, statt eine
  gekürzte Liste als vollständig auszugeben.
- **ERP-Zähler:** Token-Fehler behoben, der den Live-Zählerstrom auf dem
  Dashboard unterbrechen konnte.
- **Robuste Indexierung:** Die Indexierung übersteht jetzt vorübergehende
  Aussetzer von Datenbank und Auth Service (automatischer Retry, Fallback auf
  die primäre Datenbank) und verwirft fehlerhafte Queue-Nachrichten, statt
  sie endlos zu wiederholen.

## OCR Service — live: `1.10.3`

- **Stabile Lesereihenfolge:** Der Text wird in einer festgelegten
  Reihenfolge gelesen — dasselbe Dokument wird damit jedes Mal gleich
  extrahiert.
- **Große Dokumente:** Das OCR-Zeitbudget skaliert mit der Dokumentgröße —
  sehr große Dateien scheitern nicht mehr an einem Timeout.
- **Ungewöhnliche Zeichen:** Ein Bereinigungsschritt entfernt Zeichen, die
  die OCR-Engine nicht darstellen kann, und behebt damit Fehler bei
  Dokumenten mit exotischen Symbolen.
- **Weniger vorübergehende Fehler:** Temporäre Verbindungsfehler zum Speicher
  werden automatisch wiederholt, und ein hängender Worker wird daran erkannt,
  ob er tatsächlich Arbeit abarbeitet.

## Extraction Service — live: `1.53.3`

- **US-Rechnungen ohne Steuer:** Fall behoben, in dem das korrekte
  Netto/Steuer-Paar verworfen wurde, wenn der Steuerbetrag null ist.
- **Tabellenextraktion:** Tabellen bleiben bearbeitbar, wenn die
  konfigurierte Zuordnung mehr Spalten erwartet, als das Dokument liefert,
  und ein Absturz bei ungewöhnlichen Zeilendaten ist behoben.
- **Stabile Lesereihenfolge:** Entspricht der OCR-Änderung oben — die
  Extraktion sieht dieselbe Token-Reihenfolge, die die OCR erzeugt hat.
- **KI-Modelle:** Einstellung der Turbo-Stufe, übernommen vom API Service.

## Docflow Service — live: `2.7.3`

- **PO-Matching in Workflows:** Fehlende Vergleichswerte werden als fehlende
  Daten behandelt, nicht als Abweichung.
- **Auftragsbestätigungs-Karten:** Einkäufer und verantwortliche Person
  werden zuverlässig aufgelöst.
- **Angebots-Karten:** Das Protokoll hält jetzt fest, wenn ein Angebotspreis
  zwar vorliegt, aber außerhalb des zulässigen Zeitraums liegt — das sah
  bisher nach fehlenden Daten aus.
- **Frachtkosten:** Wenn keine der beiden Seiten Kosten ausweist, wird der
  Fall über die Operator-Karte gelöst, statt hängen zu bleiben.
- **Sicherheit:** Workflow-API-Tokens werden gegen die Organisation geprüft,
  zu der sie gehören.
- **Schnelleres Auslösen:** Die Prüfung auf aktive Workflows wird
  zwischengespeichert, und die Hintergrund-Worker starten sauber neu, statt
  hängende Prozesse zu hinterlassen.

## Barcode Service — live: `1.18.1`

- **Lang laufende Aufteilungen:** Die Verbindung zur Task-Queue wird bei
  langen Barcode-Jobs offen gehalten — das Aufteilen großer Stapel bleibt
  damit nicht mehr kurz vor dem Ende stehen.

## FTP Service — live: `1.31.2`

- **Importprotokoll-Aufräumung:** Dieselbe 90-Tage-Aufbewahrung und
  automatische Bereinigung wie beim Email Service.

## Auth Bridge Service — live: `0.4.1`

- **Verlässliche Replikations-Warnungen:** Die Replikationsbrücke für Konten
  zwischen EU und US misst einen Stillstand ab dem letzten echten Fortschritt
  statt ab dem ersten Fehler und wertet nur tatsächliche
  Replikationsbewegung als Fortschritt. Die nächtlichen Fehlalarme „bridge
  stalled“ entfallen damit. In der App ändert sich nichts.

## Operator Service — live: `1.42.1`

- **Worker-Stabilität:** Ein hängender Worker wird daran erkannt, ob er
  Arbeit abarbeitet, und der überflüssige Nachrichtenaustausch zwischen den
  Workern im Leerlauf ist abgeschaltet.

---

## Unverändert in diesem Release

**Auto Accounting** (`1.21.1`) wurde ohne für Kunden sichtbare Änderungen neu
gebaut. **Docnet** (`1.55.1`) und **Ideas** (`0.3.1`) enthalten in diesem
Zeitraum keine Änderungen.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
