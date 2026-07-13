# DocBits Release-Notizen — 9.–13. Juli 2026

_Ein Überblick darüber, was sich für Sie mit diesem DocBits-Release ändert. Jeder
Service unten zeigt die Version, die jetzt ausgerollt wird, gefolgt von dem, was
neu oder behoben ist — in klarer Sprache, ohne Ticket-Nummern und ohne
Entwickler-Jargon. Nicht aufgeführte Services hatten in diesem Zeitraum keine für
Kunden sichtbaren Änderungen._

---

## Highlights

- **Anmeldung mit mehreren Organisationen.** Nutzer, die mehreren Organisationen
  angehören, erhalten jetzt eine richtige Organisationsauswahl bei der Anmeldung,
  einen Organisationsumschalter in der Kopfzeile und eine Einstellung für die
  Standardorganisation. Sitzungen sind sicher an jeweils eine Organisation
  gebunden, und die App folgt automatisch der Region der aktiven Organisation.
  Eine Anmeldung gegen die falsche Region versucht jetzt automatisch die
  richtige Region, statt fehlzuschlagen.
- **Release-Kanäle (frozen / latest).** Organisationen können jetzt auf ein
  stabiles („frozen“) Release festgelegt werden, während andere die neuesten
  Updates erhalten — das ermöglicht kontrollierte Rollouts. Der Dialog
  „Service-Versionen“ zeigt eine neue Spalte *Release*, und Administratoren
  verwalten den Kanal über die Unternehmensinformationen. Mehrere Services
  zeigen in diesem Zeitraum größere Versionssprünge, die ausschließlich auf die
  neue Kanal-Versionsnummerierung zurückgehen — diese Sprünge enthalten keine
  funktionalen Änderungen.
- **Konfigurierbare Regelwerke.** Drei neue Regelsysteme kommen in die API
  (jeweils standardmäßig deaktiviert, aktivierbar pro Organisation):
  **Validierungsregeln**, die extrahierte Werte prüfen und Verstöße direkt am
  Dokument markieren, **Transformationsregeln**, die extrahierte Feld- und
  Tabellenwerte automatisch bereinigen oder umschreiben, und **regelbasierte
  Layout-Auswahl**, die das passende Dokumentlayout per Regeln auswählt statt
  danach, woher das Dokument kam.
- **Transparenz beim E-Mail-Import.** Das E-Mail-Importprotokoll zeigt jetzt
  eine aufklappbare Zeile pro Anhang, listet auf, welche Dokumente erstellt
  wurden (mit Schaltflächen, die direkt zum Dashboard springen), kennzeichnet
  übersprungene und aufgeteilte Elemente und erlaubt den Download der
  Original-E-Mail als `.eml`-Datei.
- **KI-Tabellenextraktion.** Ein neuer strukturierter KI-Extraktionsmodus für
  Tabellen, mit einer „Use AI“-Checkbox pro Tabelle und pro Spalte in den
  Dokumenttyp-Einstellungen.
- **Web App-Stabilität.** Eine Endlos-Neuladeschleife nach einer abgelaufenen
  Sitzung behoben, den defekten Layout Builder repariert, und
  Extraktionstabellen haben jetzt einen ziehbaren Höhenregler.
- **Neu: Auth Bridge Service.** Ein neuer Service hält Anmeldedaten
  kontinuierlich zwischen der EU- und der US-Region synchron — mit
  eingebauter Selbstheilung und Überwachung.

---

## API Service — live: `12.57.8`

- **Validierungsregeln (neu, pro Organisation):** Ein von Administratoren
  konfigurierbares Regelwerk prüft extrahierte Werte (Summen, Pflichtfelder und
  mehr) und markiert Verstöße direkt am Dokument, inklusive der ausgelösten
  Regel. Regeln können vor der Aktivierung in einem Testlauf geprüft werden,
  lassen sich pro Dokumenttyp einschalten und werden mit einem Startkatalog an
  Standardregeln ausgeliefert (alle deaktiviert, bis Sie sie aktivieren).
- **Transformationsregeln (neu, pro Organisation):** Extrahierte Feld- und
  Tabellenwerte werden während der Verarbeitung automatisch bereinigt oder
  umgeschrieben — konfigurierbar pro Dokumenttyp oder für die gesamte
  Organisation.
- **Regelbasierte Layout-Auswahl (neu):** Dokumentlayouts können jetzt über
  konfigurierbare Regeln ausgewählt werden, statt an die Herkunft des Dokuments
  gebunden zu sein. Bestehendes herkunftsbasiertes Verhalten wird automatisch
  migriert, Layout-Vorlagen können umbenannt werden, und doppelte Layout-Titel
  werden verhindert.
- **Schnellere Dashboard-Exporte:** Vom Dashboard ausgelöste Exporte werden
  jetzt an einen dedizierten Worker übergeben, statt auf einen Abfragezyklus zu
  warten — sie starten dadurch umgehend.
- **Exportblock der Duplikaterkennung behoben:** Der Exportblock für
  vermutete Duplikate funktioniert wieder.
- **Einstellungen, die nicht gespeichert blieben:** Behoben, dass gespeicherte
  Einstellungen gelegentlich nicht erhalten blieben, wenn eine ältere gelöschte
  Kopie derselben Einstellung existierte.
- **Dokumente mit ungewöhnlichen Zeichen:** Speicherfehler behoben, die durch
  unsichtbare NUL-Zeichen in extrahierten Daten verursacht wurden.
- **Korrektes „Aktualisiert von“:** Automatisch als E-Dokumente hochgeladene
  Dokumente zeigen nicht mehr einen Systembenutzer als letzten Bearbeiter — das
  Feld bleibt leer, bis tatsächlich eine Person bearbeitet.
- **Gescannte PDFs mit gutem Textlayer:** Eine neue Option lässt DocBits dem
  bereits in einer gescannten Seite eingebetteten Text vertrauen, statt OCR
  erneut auszuführen — schneller und oft genauer.
- **E-Rechnungen:** Robustere Erkennung von eingebettetem XML, wenn die
  Originaldatei erneut geprüft werden muss.
- **Aufgaben:** Neuer Organisationsschalter, mit dem Nicht-Administratoren den
  Filter „Alle“ in der Aufgabenliste nutzen können.
- **Positionsabgleich:** Das Fuzzy-Matching-Verhalten ist jetzt pro Position
  konfigurierbar.
- **Stabilität:** WebSocket-Verbindungen werden bei Fehlern sauber geschlossen,
  statt Serverausnahmen auszulösen; die Synchronisierung des
  Berechtigungs-Caches überprüft und repariert sich selbst; die Service-Version
  ist jetzt am Health-Endpunkt sichtbar.

## Auth Service — live: `1.71.1`

- **Anmeldung mit mehreren Organisationen:** Die Anmeldung fragt jetzt, welche
  Organisation betreten werden soll, wenn ein Nutzer mehreren angehört;
  Sitzungen sind an diese Organisation gebunden, und neue Endpunkte
  unterstützen das Auswählen, Wechseln und Festlegen einer
  Standardorganisation. Doppelte oder widersprüchliche
  Organisationsmitgliedschaften wurden bereinigt und werden jetzt auf
  Datenbankebene verhindert — mit schnelleren Mitgliedschaftsabfragen.
- **Korrekturen bei der Standardorganisation:** Die Anmeldung wählt automatisch
  Ihre Standardorganisation aus (nicht eine beliebige), und eine Änderung der
  Standardorganisation greift sofort, statt veraltete Profildaten anzuzeigen.
- **Abmeldung behoben:** Ein Serverfehler (HTTP 500) bei der Abmeldung wurde
  behoben und der Endpunkt zum Widerrufen von Tokens wiederhergestellt.
- **Token-Sicherheit:** Token-Prüfung und -Caching berücksichtigen jetzt die
  Organisation, für die ein Token ausgestellt wurde, und der Token-Widerruf ist
  zentralisiert.
- **Release-Kanäle:** Der Release-Kanal der Organisation wird hier gespeichert,
  ist durch Organisations-Administratoren verwaltbar und wird der App sowie der
  Routing-Schicht bereitgestellt.

## Auth Bridge Service — live: `0.2.4.2` _(neuer Service)_

- **Was es ist:** Ein neuer Service, der Authentifizierungsdaten kontinuierlich
  zwischen der EU- und der US-Region repliziert, damit Konten und Anmeldungen
  über die Regionen hinweg konsistent bleiben.
- **Selbstheilung:** Er erkennt und repariert Datenabweichungen zwischen den
  Regionen — inklusive der Sicherstellung, dass Löschungen weitergegeben
  werden — und erholt sich automatisch von Verbindungsabbrüchen, statt Daten zu
  verlieren.
- **Sicherheit und Überwachung:** Eine frühere bidirektionale
  Replikationsschleife wurde gestoppt und wird jetzt aktiv erkannt und
  abgesichert; Fehlerverfolgung und Alarmierung sind angebunden; und der
  Service meldet seine Version im Dialog „Service-Versionen“.

## Docflow Service — live: `2.6.1`

- **Workflow-Karten akzeptieren leere Werte:** Checkbox- und Partner-Karten
  schlagen nicht mehr fehl, wenn ein Feld berechtigterweise leer ist; die
  Kartentyp-Prüfungen sind strenger und vorhersehbarer.
- **Workflows laufen bei echten Änderungen erneut:** Die Workflow-Sperre
  berücksichtigt wieder den Dokumentstatus aus dem Auslöser und verfolgt jetzt
  zusätzlich die Dokumentversion — ein Dokument, dessen Daten sich tatsächlich
  geändert haben, kann den Workflow damit auch bei gleichem Status erneut
  durchlaufen, während echte Duplikate weiterhin blockiert bleiben.
- **Größere erweiterte Workflows:** Das Limit für Workflow-Knoten wurde erhöht
  und ist jetzt pro Umgebung konfigurierbar.
- **Alternativer Export:** Durch Workflows ausgelöste alternative Exporte
  werden jetzt als solche gekennzeichnet, damit nachgelagerte Systeme sie
  unterscheiden können.
- **Widerstandsfähigkeit:** Der Service verbindet sich automatisch neu, wenn
  eine Datenbankverbindung mitten in der Nutzung abbricht, toleriert einen
  langsameren Message-Broker, statt fehlzuschlagen, und fehlgeschlagene
  API-Anfragen werden jetzt mit vollem Kontext und nachverfolgbaren
  Ausführungs-IDs protokolliert.

## Email Service — live: `1.38.4`

- **Importprotokoll, neu aufgebaut für Nachvollziehbarkeit:** Jede importierte
  E-Mail hält jetzt fest, welche Dokumente daraus erstellt wurden — mit
  Detailzeilen pro Anhang.
- **Download der Original-E-Mail:** Die ursprüngliche Nachricht kann direkt aus
  dem Importprotokoll als `.eml`-Datei heruntergeladen werden.
- **Anhang-Wiederherstellung:** Der Wiederherstellungspfad für beschädigte
  Anhänge verarbeitet jetzt auch reine Textnachrichten, sodass mehr beschädigte
  eingehende E-Mails wiederhergestellt statt übersprungen werden.

## Extraction Service — live: `1.51.6`

- **Steuer/Netto nicht mehr vertauscht:** Ein Fall bei US-Dokumenten behoben,
  in dem der Steuerbetrag größer als der Nettobetrag zugeordnet werden konnte,
  wenn mehrere Kandidatenpaare gefunden wurden.
- **Mehrere Steuersätze pro Lieferant:** Die Extraktion verarbeitet jetzt
  Lieferanten, deren Rechnungen unterschiedliche Steuersätze auf einem Dokument
  ausweisen.
- **KI-Tabellenextraktion (neu, opt-in):** Strukturierte
  KI-Extraktionsendpunkte für Tabellen, aktivierbar pro Organisation über ein
  Feature-Flag.
- **Schnellere KI-Aufrufe:** Die während der Extraktion verwendete
  KI-Modellkonfiguration wurde optimiert, um unnötige Verarbeitungszeit zu
  vermeiden.
- **Absturz behoben:** Ein Fehler bei Dokumenten behoben, die während der
  Extraktion eine leere Kandidatenliste erzeugten.

## Fulltext Service — live: `1.37.2`

- **Suchindex-Migrationen repariert:** Migrationsdefinitionen
  wiederhergestellt, die auseinandergelaufen waren — Suchindex-Upgrades bleiben
  damit zuverlässig.
- Interne Routing-Arbeiten für die neue Release-Kanal-Infrastruktur.

## PO Match Service — live: `1.58.2`

- **Toleranteres Matching:** Der PO-Abgleich schlägt bei ungewöhnlichen Daten
  nicht mehr fehl — nicht-textuelle Artikelnummern, fehlende Mengen und
  nicht-textuelle Betragswerte werden jetzt sauber verarbeitet, statt Fehler
  auszulösen.

## Web App — live: `10.41.8`

- **Multi-Organisations-Erlebnis:** Neue Organisationsauswahl-Seite bei der
  Anmeldung, ein eigenes Organisationsumschalter-Symbol in der Kopfzeile,
  Einstellungen für die Standardorganisation, und die App folgt der Region
  Ihrer aktiven Organisation. Eine Anmeldung gegen die falsche Region versucht
  im Hintergrund die richtige Region und leitet Sie bei Bedarf zur
  Organisationsauswahl weiter.
- **Keine endlosen Neuladevorgänge mehr:** Eine Endlos-Neuladeschleife behoben,
  die auftreten konnte, wenn der Server ein gespeichertes Sitzungstoken
  ablehnte — die App erzwingt jetzt eine echte Token-Aktualisierung, statt
  endlos neu zu laden.
- **Layout Builder repariert:** Der Layout Builder funktioniert wieder, und die
  Layout-Auswahl ist von der Herkunft des Dokuments entkoppelt (passend zur
  neuen regelbasierten Auswahl in der API).
- **Extraktionstabellen:** Positionstabellen haben jetzt einen ziehbaren
  Größenregler, damit Sie der Tabelle beim Validieren mehr Platz geben können.
- **E-Mail-Importprotokoll:** Neuer Status „Übersprungen“ und
  Aufteilungs-Badges, aufklappbare Zeilen pro Anhang, Download der
  Original-E-Mail und Dokument-ID-Schaltflächen, die direkt zum auf dieses
  Dokument gefilterten Dashboard springen.
- **Dashboard-Suche:** Das Dropdown für Abfragewerte zeigt jetzt die
  lokalisierte Bezeichnung für Felder mit Wertelisten, und die Beispiele in der
  Suchhilfe wurden überarbeitet.
- **Zuverlässigkeit der Einstellungen:** Benutzereinstellungen werden bei der
  Anmeldung über SSO jetzt zuverlässig geladen, und die Speicherbestätigung
  erscheint nur noch, wenn das Speichern tatsächlich erfolgreich war.
- **Aufgaben:** Der Filter „Alle“ kann für Nicht-Administratoren über einen
  neuen Organisationsschalter wiederhergestellt werden.
- **Watchdog-Protokolle:** Nicht mehr auf 10.000 Einträge begrenzt, plus
  allgemeine Verbesserungen der Bedienbarkeit.
- **Support-Tickets:** Das Support-Formular füllt Ihre E-Mail-Adresse aus Ihrem
  Profil vor.
- **Dokumenttyp-Einstellungen:** Neue „Use AI“-Checkbox an Tabellen und
  Spalten zur Steuerung der KI-gestützten Tabellenextraktion.
- **Dialog „Service-Versionen“:** Neue Spalte *Release*, die den Kanal jedes
  Services zeigt (frozen/latest) — so geroutet, dass er für festgelegte
  Organisationen schnell bleibt.
- **Feldvalidierung:** Ein Fehler bei der Rückkehr zur Feldvalidierung von
  einem anderen Bildschirm aus behoben, und die Schaltfläche „Scripts“ führt
  nicht mehr auf eine 404-Seite.

---

## Nur Versionsneunummerierung (keine funktionalen Änderungen)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) und **Ideas Service** (`0.3.1`) wurden im Zuge der neuen
Release-Kanal-Infrastruktur neu versioniert. Ihre größer wirkenden
Versionssprünge enthalten in diesem Zeitraum keine Funktions- oder
Verhaltensänderungen. Der **Docnet Service** (`1.54.6`) ist seit dem 19. Juni
unverändert.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..13)
     version-bump commits supplied by the user, per service). -->
