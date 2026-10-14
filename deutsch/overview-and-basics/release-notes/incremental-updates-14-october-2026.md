# DocBits Release-Notizen — 14. Oktober 2026

_Was sich mit dem DocBits-Produktions-Hotfix am 14. Oktober 2026 (Release
R1.0.15) ändert — alles seit dem [Hotfix vom 15. September](incremental-updates-15-september-2026.md).
Jeder Service unten zeigt die Version, die ausgerollt wird, gefolgt von dem,
was neu oder behoben ist, in klarer Sprache. Nicht aufgeführte Services hatten
keine für Kunden sichtbaren Änderungen._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/de.mp4" %}

---

## Highlights

- **Der Settings Assistant.** Eine Chatleiste auf jeder Einstellungsseite
  beantwortet Fragen zur Konfiguration Ihrer Organisation, in Ihrer Sprache und
  auf Basis der DocBits-Dokumentation. Er liest den aktuellen Stand Ihrer
  Einstellungen und erklärt sie (Gruppenberechtigungen, Importkanäle,
  Bestellschalter, Buchhaltung). Wenn Sie ihn bitten, etwas ein- oder
  auszuschalten, zeigt er zuerst eine Vorschau, wartet auf Ihre Bestätigung und
  bietet ein Rückgängigmachen an. „Open setting“ springt direkt zur
  Einstellung, auch innerhalb eines eingeklappten Abschnitts, und hebt sie
  hervor. Organisationsadministratoren schalten den Assistenten unter
  Firmeninformationen ein oder aus. Er beantwortet nur DocBits-Fragen und
  ändert nie etwas ohne Bestätigung.
- **Neue KI-Stufen.** Die Stufen Fast und Full laufen auf neuen Modellen. Eine
  neue Stufe Auto wählt pro Dokument zwischen Fast und Full, und Nexus Flash
  ergänzt Nexus. Ein Vision-Modus (hybrid oder auto) entscheidet, wann das
  Seitenbild mitgesendet wird. Gespeicherte KI-Modell-Einstellungen wechseln
  von selbst auf die neuen Stufen, und die Oberflächen zeigen nur Stufennamen.
  „Use AI“ ist ein Dropdown (Standard, Ja, Nein) mit einer Vorschau dessen, was
  die strukturierte Extraktion anfordern wird.
- **Prüfung der Kopffelder.** Der Validierungsbildschirm hat neben „Speichern“
  die Schaltfläche „Header field check“. Ihr Bericht listet jedes Kopffeld
  mit der Herkunft des Werts (KI, Regel, Skript oder Stammdaten), in einer
  kompakten Tabelle mit Quellenfilter, Suche und Sortierung und mit denselben
  Feldbezeichnungen wie der Validierungsbildschirm. Das Herkunfts-Popup zeigt
  die Quelle jedes Werts in einem Streifen.
- **Anmeldung und Sicherheit der Organisation.** Eine MFA-Abfrage kann auf
  jedem Anmeldeweg nur einmal verwendet werden, und das Einrichten eines
  Authenticators erfordert den E-Mail-Code. Organisationen verwalten eine Liste
  verifizierter E-Mail-Domains; ein Social Login (zum Beispiel Microsoft)
  tritt der Organisation bei, die die Domain führt, und legt nie von sich aus
  eine Organisation, einen Benutzer oder ein Abonnement an. Nur
  Organisationsadministratoren ändern Organisationseinstellungen und schreiben
  oder genehmigen Regeln für den Bestellabgleich. Zwischengespeicherte
  Antworten können nicht mehr über Organisationen hinweg abfließen.
- **Bestellabgleich und Nebenkosten.** Nebenkosten, die die Bestellung mit null
  erwartet, erhalten eine absolute Untergrenze, die Nebenkosten-Toleranz gilt
  auch für Nebenkosten, die die Bestellung nicht einplant, und ein Feld kann
  mehrere Kostenelemente auflisten, deren Beträge proportional zur Bestellung
  aufgeteilt werden. Eine Abgleichspalte kann ein Kennzeichen „Abweichung
  erlauben“ tragen. Workflow-Karten vergleichen Nebenkosten pro Liste, und das
  Ausführungslimit für Workflows steigt von 30 auf 50.
- **Weniger falsche Zahlen.** Beträge erscheinen im persönlichen Format jedes
  Benutzers (Schweiz und Slowenien eingeschlossen), reine Datumswerte behalten
  in jeder Zeitzone ihren Kalendertag, die US-Gesamtbetragsgleichung
  berücksichtigt Zusatzbeträge und Rechnungen mit mehreren Steuern, und
  Dokumente mit Kopfbeträgen von 0,00 fallen nicht mehr in den falschen
  Kandidatendurchlauf.

---

## Außerdem in diesem Release behoben

- Das Dashboard bleibt nicht mehr leer, wenn ein Wettlauf den Filter der
  Unterorganisation auf die Organisations-ID setzt und damit jedes Dokument
  ausschließt.
- Dimensionswerte lassen sich für jeden Benutzer wieder auswählen.
- Ein von einem Kunden gemeldeter Upload-Fehler ist behoben.
- „Match on total“ funktioniert für Lieferanten, deren Rechnung nur eine
  Position hat, und für die Lieferanten-Setups, die es gemeldet haben.
- SPS-E-Dokumente: Die Nebenkosten der 810 werden angepasst, das Layout der
  Nebenkosten der 855 wird aktualisiert, und das Kundenlogo in der
  E-Dokument-Vorschau ist korrigiert.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Eine Chat-Seitenleiste mit Umschalter steht auf allen Einstellungsseiten
  bereit. Die Unterhaltung bleibt über Seitenwechsel erhalten, ist auf 20
  Nachrichten begrenzt und zeigt die angewendeten Änderungen mit einer Option
  zum Rückgängigmachen.
- Er begrüßt Sie mit Fragen, die zur aktuellen Einstellungsseite passen, und
  zeigt Einstellungskarten mit einem Ein/Aus-Schalter. Esc schließt zuerst
  Menüs, „Stop“ bricht eine laufende Antwort ab, und Screenshots in Antworten
  öffnen sich in einer Lightbox.
- Das Anwenden einer Änderung öffnet einen Dialog mit Vorschau, Bestätigung und
  Rückgängigmachen.
- Jede Einstellung ist über die Seitenleiste durchsuchbar, und die gefundene
  Einstellung wird in einer anderen Farbe hervorgehoben. „Open setting“
  scrollt innerhalb eines eingeklappten Akkordeons zum Ziel.
- Ein Schalter für Organisationsadministratoren zum Ein- und Ausschalten des
  Assistenten steht unter Firmeninformationen.
- KI-Hinweise werden Nova zugeschrieben, und es erscheinen nur Stufennamen,
  nie Modell-IDs.

**Validierungsbildschirm und Dokumentverarbeitung**
- Neue Schaltfläche „Header field check“ mit Bericht, Herkunft pro Feld und
  Hilfeseite (siehe Highlights). Quellenbezeichnungen und Status-Chips bleiben
  innerhalb ihrer Zellen.
- Die Text-Badges „from master data“ neben den Feldbezeichnungen entfallen; das
  Herkunfts-Popup trägt diese Information.
- Überall läuft dieselbe gemeinsame Feldvalidierung, wodurch der allgemeine
  Fehler „One or more fields need validation“ nach Auto Accounting entfällt.
- Tooltips an den Schaltflächen des Feld-Popups (Löschen, Leeren, Bestätigen)
  sagen, was jede tut, bevor Sie klicken.
- Eine optimistische Zeile zeigt jetzt, was gespeichert wurde, nicht was
  eingegeben wurde. Eine Neuzuordnung von Spalten fragt nur dann nach einer
  Bestätigung, wenn eine sichtbare Spalte ihre Zuordnung verliert.
- Seiten jenseits des OCR-Seitenlimits sind schreibgeschützt und markiert, auch
  im Auto-Accounting-Viewer. Das alte Panel zur Seitenbeschränkung beim Import
  ist entfernt.
- Für jede Bestellnummer in einem Kopffeld mit mehreren Bestellungen erscheint
  eine Bestelltabelle, und der Layout Builder beschriftet Bestell-Tabs anhand
  des Schlüssels der Bestelltabelle und meldet das Modul nicht mehr als
  deaktiviert, wenn die Bestelltabelle aktiv ist.
- Die Vorschlagskarte gibt die Toleranz aus statt `[object Object]`, und der
  Vergleichsbildschirm der Genehmigung rundet konfigurierte Vergleichsspalten
  (Artikelnummern) nicht mehr.

**Konten, Einstellungen und Fehler**
- Jede Fehlermeldung und jeder Anmeldefehler zeigt die Trace-ID der
  fehlgeschlagenen Anfrage, damit der Support sie finden kann.
  WebSocket-Fehler des Dashboards weisen genau die Anfrage ab, die sie nennen.
- Firmeninformationen listet die E-Mail-Domains der Organisation auf.
- Administratoren können die E-Mail „Passwort festlegen“ von der Benutzerseite
  aus erneut senden.
- Globale Administratoren legen den Vertragsbeginn in der Abonnementtabelle
  fest.
- Organisationsadministratoren sehen den Tab „Executive Dashboard“ und die
  Schaltflächen zum Hinzufügen und Löschen von XSLT. Mitglieder speichern
  Layouts als ihre eigene Einstellung.
- Eine Sitzung ohne Organisation erhält eine klare Fehlermeldung und die
  Organisationsauswahl statt eines leeren Dashboards.
- Beträge folgen dem persönlichen Zahlenformat des Benutzers, und reine
  Datumswerte behalten ihren Tag in jeder Zeitzone.
- Stammdaten senden Unterorganisations-IDs nur, wenn sie sich von der
  Organisations-ID unterscheiden, und benutzerdefinierte Stammdaten-Header
  werden als Header gesendet.
- Die Tabellenmaske schneidet das Dropdown „Use AI“ nicht mehr ab, der
  KI-Hinweistext verdeckt nicht mehr die Trainingszeile, und die KI-Tabelle
  behält ihre direkte Schaltfläche „Anwenden“, mit einer reinen Icon-Kopfprüfung
  und einer Lizenzmeldung.
- Icons der Tabellenextraktion werden wieder dargestellt, nachdem die alte
  Icon-Schrift entfernt wurde.

**Aufgabenboard**
- Das Board lädt seine erste Seite mit weniger doppelten Anfragen, Enter startet
  die Suche sofort, verspätete Antworten werden der richtigen Suche zugeordnet,
  die Fußzeile zeigt die tatsächliche Trefferzahl statt der Seitenkapazität,
  und ein in einer Organisation gestartetes Löschen wird beim Wechsel der
  Organisation abgebrochen, bevor es gesendet wird.

---

## API Service — `12.83.293`

**Settings Assistant und MCP**
- Chat-Endpunkt mit Leitplanken: nur DocBits-Fragen, keine Änderung ohne
  Bestätigung, unklare oder Meta-Fragen erhalten Hilfe statt einer Ablehnung,
  und Antworten streamen zuerst Karten, dann Text.
- Schreibgeschützte Bausteine für jeden Einstellungsbereich
  (Gruppenberechtigungen, Importkanäle, Bestellabgleich, Buchhaltung,
  E-Mail-Domains), ein Katalog von Deep Links mit einem Werkzeug zum Finden von
  Einstellungen und eine Dokumentationssuche mit Bildern aus den DocBits-Docs.
- Anwendungsablauf der Welle 1: Vorschau, Bestätigung und Rückgängigmachen für
  unterstützte Einstellungen, eine Geltungsbereichsregel für alle drei,
  abgesichert gegen doppelte Bestätigung und Ablauf.
- MCP-Werkzeuge lesen im Remote-Modus nie Dateien vom Server, und Fixture- und
  Lab-Werkzeuge laufen nur auf Dev.

**KI**
- Neue Modelle hinter den Stufen Fast und Full, die Stufe Auto, Nexus Flash und
  die Einstellung für den Vision-Modus. Gespeicherte `AI_MODEL`-Einstellungen
  werden auf die neuen Stufen umgestellt.
- „Use AI“ dokumentiert, was die strukturierte Extraktion anfordert.

**Sicherheit und Isolation**
- Nur Organisationsadministratoren ändern Organisationseinstellungen.
- Der Aufruf `/accounting/rebuild` trainiert nur die Organisation des Aufrufers,
  schlägt bei einer fehlgeschlagenen Organisationsabfrage geschlossen fehl und
  antwortet bei einer ungültigen ID mit 400.
- XSLT-, XML- und PDF-Rendering verweigern Datei- und Netzwerkzugriff, lösen
  keine externen Includes auf, und Rechnungsbytes werden bereinigt, bevor sie
  den Transformer erreichen. Gerenderte PDF-Vorschauen erlauben nur
  vertrauenswürdige Bild-Hosts.
- Cache-Schlüssel tragen die Organisation, und dieselbe Kennung ergibt immer
  denselben Schlüssel, sodass eine fremde Organisations-ID keine
  zwischengespeicherten Daten mehr lesen kann. Das organisationsweite Leeren des
  Dashboard-Caches bei jeder Dokumentänderung entfällt.
- Die E-Mail-Domain-Liste der Organisation wird an Auth weitergereicht.

**Bestellabgleich und Export**
- Ein Feld kann mehrere Kostenelemente auflisten, deren Beträge proportional zur
  Bestellung aufgeteilt werden.
- Genehmigungsvertretungen verweisen auf die aktive Genehmigungsanfrage,
  Speichervorgänge geheilter Genehmigungen blockieren nicht mehr, und ein
  Dokument mit ausstehender Genehmigung wird für den Export abgelehnt.
- Die PDF/A-Annotation behält Katalog und eingebettetes XML, sodass E-Rechnungen
  ihr XML nach der Annotation behalten. UBL-Rechnungen mit der bloßen
  EN-16931-CustomizationID werden klassifiziert (E-Rechnungsnetzwerk).
- GRPR rundet auf die 6 Dezimalstellen, die M3 akzeptiert.
  Umrechnungsfaktoren der Basismengeneinheit werden der eingefrorenen Position
  hinzugefügt.
- Soft-gelöschte Trainings und Formatierungsregeln werden respektiert, und MCP
  `update_document_fields` bestätigt keinen Schreibvorgang mehr, den es
  verloren hat. `get_table_rules` antwortet mit einem typisierten Fehltreffer,
  und eine leere Übersetzungs-Payload verwendet ihren Fallback.
- Slowenische Beträge verwenden `sl_SI`, und gespeicherte Einstellungen werden
  migriert. Benutzerdefinierte Klassifizierungsbezeichnungen, die als UUID-IDs
  gesendet werden, werden aufgelöst. Freigegebene Dashboards behalten beim
  Aktualisieren `created_by` und die Freigabeliste.
- Fehlerframes des Dashboards tragen die `request_id` der Anfrage, und jede
  fehlgeschlagene JSON-Antwort trägt eine Trace-ID.
- Das System startet nur fehlerhafte Worker neu statt der gesamten API-Flotte
  und prüft die registrierte Aufgabenliste korrekt. Die Queue des
  Hang-Monitors wird wieder abgearbeitet.

---

## Auth Service — `1.78.49`

- Eine Multi-Faktor-Abfrage ist auf jedem Anmeldeweg nur einmal verwendbar, nicht
  nur im MCP-Ablauf. Das Einrichten erfordert den E-Mail-Code, nach einer
  Anmeldung mit gemeinsamem Passwort wird kein Einrichtungs-Token ausgestellt,
  und Benutzer werden benachrichtigt, wenn ein Faktor eingerichtet wird.
- Organisationen verwalten eine Liste von E-Mail-Domains, die jeweils nur einmal
  zuweisbar sind. Ein Social Login tritt der Organisation bei, die die
  verifizierte Domain führt, erfindet nie eine Organisation, einen Benutzer oder
  ein Abonnement und lehnt ab, ohne jemanden zu nennen, während stattdessen die
  Administratoren informiert werden. Die von Microsoft zurückgegebenen Domains
  werden behandelt.
- Jede abgelehnte Anmeldung trägt eine Trace-ID. Administratoren können die
  E-Mail „Passwort festlegen“ erneut senden. Das Vertragsguthaben ist
  vorzeichenbehaftet, und der Vertragsbeginn wird auditiert.

## Auth Bridge — `0.5.7`

- Die Replikation der EU- und US-Konten hält ihre Verbindung während des
  Abgleichs gefüllt, bindet einen abgerissenen Replikations-Slot selbstständig
  wieder an, nutzt begrenzten Speicher und behandelt eine vorhandene
  Replikationsherkunft als Erfolg. Die regionsübergreifende Anmeldung ist
  zuverlässiger.

## Docflow Service — `2.10.22`

- Die separate Einheitspreis-Karte liest die Standard-Felddefinitionen der
  Organisation für Nebenkosten und vergleicht jedes Kostenelement, das ein Feld
  auflistet.
- Das Ausführungslimit für Workflows steigt von 30 auf 50, und
  Workflow-Log-Suchen weisen eine ID zurück, die keine UUID ist.

## Docnet Service — `1.56.15`

- `list_document_fields` meldet jede konfigurierte Tabellenspalte, auch die
  leeren.

## Extraction Service — `1.56.0.1`

- Stufen: neue Modelle hinter Fast und Full, Auto, Nexus Flash und ein
  Vision-Modus. Vision-Anfragen an den Inferenz-Host bleiben unter dessen
  Größenlimit.
- Die Tabellenextraktion mit Nexus bündelt Seiten (zwei pro Stapel), führt
  Stapel parallel mit einem gemessenen Timeout aus, wiederholt bei vorübergehenden
  Fehlern und teilt einen Stapel, der ins Timeout lief. Kopffelder werden aus
  allen Stapeln gelesen.
- US-Gesamtbeträge: Zusatzbeträge sind Teil der Gesamtbetragsgleichung, Paar 1
  zählt in der Absicherung von Paar 2, Kandidaten mit niedriger Bewertung
  werden übersprungen, wenn die Steuern nicht null sind, und „above“ und
  „below“ erkennen mehrwortige Bezeichnungen.
- Kennungsfelder reparieren Zeichen, die tatsächlich vorkommen, und unsichtbare
  Zeichen werden nach ihrer Bedeutung behandelt, sodass aus einem „O“ kein
  merkwürdiges Zeichen mehr wird.

## Fulltext Service — `1.42.41`

- Neuer Index für die DocBits-Dokumentation mit Ingest- und Such-Endpunkten,
  Bildern in Antworten und einer Frist für die gesamte Suche. Er speist den
  Settings Assistant.

## PO Match Service — `1.59.48`

- Absolute Untergrenze für Nebenkosten, die die Bestellung mit null erwartet,
  und Nebenkosten-Toleranz für Nebenkosten, die die Bestellung nicht einplant.
- Eine Spalte kann ein Kennzeichen „Abweichung erlauben“ tragen. Mehrere
  Kostenelemente pro Feld werden proportional aufgeteilt.
- Nur Organisationsadministratoren schreiben oder genehmigen Abgleichsregeln,
  und Regelbedingungen akzeptieren nur eine Whitelist-Ausdrucksgrammatik.
- Regeländerungen lassen sich gegen einen Override-Regelsatz simulieren, ohne zu
  schreiben, für Touchless-Änderungsvorschläge. Zusätzliche Bestellspalten für
  den Abgleich werden aus dem Attribut des Dokumenttyps gelesen, mit einer
  Migration der alten Einstellung.

---

_Nicht betroffen in diesem Release: Auto Accounting, Barcode, E-Mail, FTP,
Ideas, OCR, Operator. FTP und Operator enthalten nur interne Wartung._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
