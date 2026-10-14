# DocBits Release-Notizen — 12.–25. August 2026

_Was sich mit dem DocBits-Produktions-Upgrade am 25. August 2026 ändert —
alles seit dem Release vom 12. August. Jeder Service unten zeigt die Version,
die ausgerollt wird, gefolgt von dem, was neu oder behoben ist, in klarer
Sprache. Nicht aufgeführte Services hatten keine für Kunden sichtbaren
Änderungen._

---

## Highlights

- **Strengere Organisations-Isolation.** Eine Sicherheitsüberprüfung hat
  mehrere Stellen geschlossen, an denen Daten einer Organisation aus einer
  anderen gelesen oder verändert werden konnten: Dokumentskripte,
  Benutzerlisten von Unterorganisationen, Gruppenmitgliedschaften und das
  Verarbeitungs-Token, das ein Dokument durch die Pipeline trägt, werden jetzt
  alle gegen die Organisation des Aufrufers geprüft. Auch Freigaben setzen das
  Vier-Augen-Prinzip jetzt korrekt durch: Die zweite Freigabe muss von einer
  anderen Person kommen als die erste.
- **Dokumente bleiben nicht mehr hängen.** Vier separate Ursachen, aus denen
  Dokumente dauerhaft festhingen, wurden behoben: Exporte, die nach einer
  Ablehnung im Status „Exporting“ verharrten, Neustarts, die einfroren, wenn
  ein Verarbeitungsschritt abstürzte, Barcode-Splits, die sich nie
  zurückmeldeten, und der Accounting-Bildschirm, der bei „Preparing…“ hängen
  blieb. In jedem Fall wird das Dokument jetzt entweder fertig verarbeitet
  oder zeigt einen echten Fehler, auf den Sie reagieren können.
- **Gutschriften werden als Gutschriften erkannt.** XRechnung-3.0-, 3.0.1-
  und 3.0.2-Gutschriften in CII-Syntax, reine CII-Gutschriften sowie
  Dokumente nach ZUGFeRD 2.4 / Factur-X 1.08 werden jetzt korrekt
  klassifiziert, mit dem Gesamtbetrag aus dem richtigen Feld. Bei gescannten
  Dokumenten, die sowohl „Rechnung“ als auch „Gutschrift“ erwähnen,
  entscheidet, welches Schlüsselwort näher an der Dokumenttyp-Angabe steht,
  und Beträge werden wieder positiv, wenn Sie eine Gutschrift zurück in eine
  Rechnung umklassifizieren.
- **PO-Matching rechnet verlässlich.** Toleranzen werden als exakte
  Dezimalwerte statt als Gleitkommazahlen verglichen, beziehen sich auf den
  Bestellwert, und Rechnungen, die sich auf mehrere Bestellungen beziehen,
  werden gegen alle abgeglichen. Spalten, die Sie nie zugeordnet haben,
  verfälschen die Prüfung der Positionsbeträge nicht mehr, und wenn
  Pflichtspalten fehlen, nennt der Fehler sie beim Namen.
- **Workflow-Läufe behalten ihre Arbeit.** Ein Workflow, der einen Feldwert
  schreibt, schreibt ihn jetzt so auf das Dokument, dass ein späterer Export
  ihn nicht stillschweigend zurücksetzen kann. Wiederholte Trigger verwerfen
  nicht mehr, was der Lauf bereits erledigt hat, und zwei Trigger auf
  dasselbe Dokument stellen sich in eine Warteschlange, statt sich
  gegenseitig die Sperre zu stehlen.
- **Passwort-Zurücksetzen-E-Mails werden wieder versendet.** Sie verließen
  den Server stillschweigend nie. Das Formular zum Zurücksetzen zeigt nach
  dem Absenden außerdem eine echte Rückmeldung, und die Antwort verrät nicht
  mehr, ob ein Konto existiert.

---

## Web App — `10.55.0`

### Anmeldung und Konten

- Das Zurücksetzen des Passworts funktioniert wieder von Anfang bis Ende: Die
  E-Mail kommt an, das Formular bestätigt das Absenden, und die Antwort ist
  dieselbe — unabhängig davon, ob zur Adresse ein Konto existiert.
- Wenn Ihre Organisation die Einrichtung eines zweiten Faktors verlangt, sagt
  der Anmeldebildschirm das jetzt, statt ohne Meldung fehlzuschlagen.
- Administratoren können die organisationsweite MFA-Pflicht nicht mehr
  einschalten, bevor die Einrichtung bei der Anmeldung verfügbar ist — das
  konnte Benutzer bisher aussperren.

### Validierungsbildschirm

- Der Zoom-Regler reicht jetzt bis 150 % (bisher war bei 80 % Schluss), und
  das Zoomen in eine Tabelle funktioniert über die Containerbreite hinaus,
  statt nichts zu tun.
- Leere Betragsfelder zählen als 0, statt eine Fehlermeldung auszulösen, und
  ein Doppelklick auf das Dokumentbild wird ignoriert, wenn kein Feld
  ausgewählt ist.
- Das Banner, das erscheint, wenn eine andere Sitzung die Dokumentsperre
  hält, hatte keinen Text; jetzt erklärt es sich selbst. Das Taggen einer
  Tabelle löst keine falsche Warnung „Dokument wurde extern geändert“ über
  die eigene Änderung mehr aus.
- In der KI-Tabelle fragt eine Spalten-Neuzuordnung, die eine andere Spalte
  aufheben würde, zuerst nach Bestätigung, und Werte, die keine Zahlen sind,
  werden in AMOUNT- und NUMBER-Spalten markiert.
- Der Tab „Extracted table“ verlinkt wieder auf das manuelle
  Tabellentraining, wenn er leer ist.
- Artikelnummern in der Positionstabelle des Compare-Bildschirms werden als
  Kennungen angezeigt, nicht wie Beträge gerundet.
- Freigeberfelder lösen Benutzer- und Gruppen-IDs zu Namen auf, sodass sie
  nie eine rohe ID zeigen oder leer bleiben. Aufgabenfristen werden über
  einen einzigen UTC-bewussten Pfad umgerechnet, sodass alle Betrachter
  dasselbe Datum sehen.
- Dokumente, die zurück in die Validierung geschickt wurden, zeigen während
  der Vorbereitung einen Ladeindikator statt eines toten Bildschirms.

### Accounting

- Gesplittete Positionen behalten nach Drücken von Enter ihr %-Zeichen, und
  0 % wird als Wert akzeptiert.
- Im Kontenfilter übernimmt Enter das erste passende Konto, statt nichts zu
  tun.
- Flexdimension-Zeichen werden über die Dimensions-ID zugeordnet, sodass
  Dimensionen auch dann in der richtigen Spalte landen, wenn die Reihenfolge
  abweicht.
- Eine fehlgeschlagene Accounting-Vorbereitung fängt sich mit einer
  Fehlermeldung, statt endlos bei „Preparing…“ zu hängen, und das erneute
  Öffnen eines Dokuments liefert keine veralteten Daten des vorherigen mehr.

### PO-Matching

- PO Matching lässt sich wieder öffnen, auch wenn nicht jede Pflichtspalte
  zugeordnet ist; fehlt etwas Benötigtes, nennt die Meldung die genauen
  Spalten.
- Spalten ohne Zuordnung werden beim Öffnen des Bildschirms ausgeblendet —
  nach einmaliger Rückfrage — und fließen nicht mehr in die Berechnung der
  Positionsbeträge ein.
- Die abgeglichene Menge aktualisiert sich nach dem Speichern, und das Popup
  zu fehlenden Spalten führt Sie zur Feldvalidierung, wo Sie das Problem
  beheben können.

### Dashboard und Suche

- Dropdown-basierte Spalten (Rechnungstyp, Status und ähnliche) zeigen ihre
  Bezeichnung in Ihrer Oberflächensprache statt des rohen gespeicherten
  Werts.
- Die Freitextsuche akzeptiert Klammern als normalen Text; bisher wies sie
  die Abfrage zurück. Der Filteroperator „ungleich“ bleibt ausgewählt, und
  das manuelle Bearbeiten eines Filters beschädigt den Feldnamen nicht mehr.
- Die Auswahl einer Unterorganisation in der Schnellsuche fügt deren Namen
  ein, nicht ihre UUID, und die Autovervollständigung für Unterorganisationen
  listet keine Duplikate mehr.
- Das Dashboard kann jetzt bis zu 10.000 Dokumente pro Suchfenster abrufen,
  sodass große Ergebnismengen korrekt blättern.
- Das Duplikat-Panel zeigt dieselben aufgelösten Spalten wie die Hauptliste,
  und mehrteilige Lieferanten-Filterwerte überstehen das Drücken von Enter.

### Aufgaben

- Die Zuweisungs-E-Mail geht raus, wenn eine Aufgabe zugewiesen wird — genau
  einmal. Das Bearbeiten oder Erledigen einer Aufgabe versendet sie nicht
  erneut, und das Datum „zugewiesen am“ bleibt das Datum der Zuweisung.
  Aufgaben-E-Mails werden außerdem in Outlook korrekt dargestellt.

### Workflow Builder

- Suche, Sortierung und Seitennavigation der Workflow-Liste bleiben beim
  Filtern konsistent.
- Der Schalter „run workflow on change“ im Layout-Builder steuert den Lauf
  jetzt tatsächlich, und beim Aktivieren muss ein Workflow ausgewählt werden.

### Einstellungen und Administration

- Der WatchDog-Download-Link und der Einrichtungsbefehl zeigen auf die
  Umgebung, in der Sie sich befinden, nicht immer auf die Produktion.
- Entscheidungsbäume: Das ausgewählte Dokumentfeld bleibt hervorgehoben, wenn
  sich die Auswahl erneut öffnet, abgeschnittene Bezeichnungen erhalten einen
  Tooltip, und beim Hinzufügen einer Zeile werden Benutzernamen (statt roher
  IDs) angezeigt.
- Die Checkbox „System Admin“ ist beim Bearbeiten eines Benutzers editierbar.
- Analytics: Core Web Vitals werden aus den echten Messdaten dargestellt, und
  die Ansicht des Log-Service funktioniert.
- „Use Default Template“ im Layout-Manager kopiert das Standard-Layout wie
  vorgesehen.
- Benutzerdefinierte Feldbezeichnungen überschreiben nicht mehr die
  mitgelieferten Übersetzungen der Standardfelder.
- Lieferantenportal-Angebote: Das Einreichen eines Angebots mit einem
  REF1-Wert außerhalb der zulässigen Liste wird blockiert.
- MediOrder erhält eine Duplikaterkennung auf seinem Validierungsbildschirm.

## API Service — `12.82.3`

### Sicherheit und Organisations-Isolation

- Der Wechsel der aktiven Organisation wird gegen Ihre tatsächliche
  Mitgliedschaft geprüft und schlägt im Zweifel sicher fehl; ein interner
  Test-Endpunkt, der sich zum Organisationswechsel missbrauchen ließ, wurde
  geschlossen.
- Dokumentskripte können nicht mehr organisationsübergreifend gelesen oder
  überschrieben werden — weder über den Aufruf zum Anwenden auf ein Dokument
  noch über eine fremde Versions-ID beim Speichern.
- Benutzerlisten von Unterorganisationen und Gruppenmitgliederlisten geben
  nur noch Personen aus der Organisation des Aufrufers zurück, und das
  gleichzeitige Hinzufügen mehrerer Benutzer zu einer Gruppe verwirft nicht
  mehr alle bis auf den ersten.
- Zugangsdaten aus der falschen Organisation werden abgewiesen, bevor sie zum
  Verarbeitungs-Token eines Dokuments werden können, und
  Volltextsuchabfragen laufen als der aufrufende Benutzer statt als
  Service-Identität.
- Das Vier-Augen-Prinzip bei Freigaben wird durchgesetzt: Der zweite
  Freigeber muss eine andere Person sein als die, die zuerst freigegeben hat.
- Die Live-Liste des PO Dashboards ist auf die Unterorganisationen des
  Benutzers eingeschränkt.

### Dokumenten-Pipeline

- Dokumente, deren Export abgelehnt wurde, bleiben nicht mehr dauerhaft in
  „Exporting“ stehen, und Exportfehler tragen immer eine Meldung statt einer
  leeren.
- Stürzt ein Verarbeitungsschritt ab, geht das Dokument in einen
  Fehlerzustand, statt ausweglos in „restart in progress“ festzuhängen.
- Ein Barcode-Split, der fehlschlägt oder in einen Timeout läuft, markiert
  das Dokument als Error, statt stillschweigend „Running“ anzuzeigen, und
  ein Split ohne erzeugte Kind-Dokumente behält das übergeordnete Dokument
  und markiert es, statt alles zu löschen.
- Ein fehlgeschlagener Wiederholungsversuch kann kein Dokument mehr
  überschreiben, das inzwischen fertig verarbeitet wurde.
- Ohne Benutzerinteraktion neu gestartete Dokumente und Split-Kinder laufen
  jetzt unter einem langlebigen Organisations-Token, sodass lang laufende
  Verarbeitung nicht mehr an einer abgelaufenen Sitzung scheitert.
- Eine leere Layout-Template-Antwort wird nicht mehr sechs Stunden lang
  zwischengespeichert — das ließ Layouts bisher verschwinden, bis der Cache
  ablief.

### Extraktion und E-Dokumente

- Beträge mit nachgestelltem Minus („100,00-“) werden als negativ erkannt,
  statt verworfen zu werden.
- Schweizer Dokumente werden als Schweizer Dokumente erkannt (CHF,
  CHE-USt-Nummern, CH-IBANs), statt auf deutsche Konventionen zurückzufallen,
  und Daten mit typografischen Gedankenstrichen werden korrekt geparst.
- XRechnung-3.0-, 3.0.1- und 3.0.2-Gutschriften in CII-Syntax werden als
  Gutschriften klassifiziert, mit dem Gesamtbetrag aus dem Feld für die
  Gesamtsumme; dasselbe gilt für reine CII-Gutschriften. Eine deklarierte
  ZUGFeRD-2.4- / Factur-X-1.08-Version gewinnt gegen den generischen
  Profil-Identifier, und bloße XRechnung-Typen werden zu ihrem UBL- oder
  CII-Pendant aufgelöst, statt fehlzuschlagen.
- Dropdown-Felder (Wertelisten) wie Tax Country und Tax Code behalten ihren
  Wert durch die Feldtransformation; bisher wurden sie geleert.
- Tabellenextraktion: Ein Fehler in einer reinen Zahlenspalte bleibt auf
  diese Spalte beschränkt, statt die ganze Tabelle zu verwerfen, die
  KI-Tabellenextraktion erhält einen Timeout, der Multi-Batch-Läufe
  übersteht, und zwei Abstürze bei ungewöhnlichen Tabellenformen (Zeilen
  ohne Seitenpositionen, unregelmäßige Spaltenzahlen) sind behoben.
- Source-Rule-Muster matchen unabhängig von Groß- und Kleinschreibung.

### Export

- Eine Steuerprüfung, die während der Export-Vorschau fehlschlägt, liefert
  einen lesbaren Fehler statt eines Serverfehlers — auf beiden
  Vorschau-Endpunkten.
- Der SFTP-Export kann das Originaldokument zusätzlich zum konvertierten
  mitsenden.
- Existieren Exportkonfigurationen auf mehreren Ebenen, gewinnt konsistent
  die spezifischste.
- BOD-Exporte können über das Mapping Spaltentyp-Attribute mitführen.

### Import und Stammdaten

- Das E-Mail-Importprotokoll ist vollständig: Abgewiesene und fehlgeschlagene
  eingehende E-Mails erhalten immer eine Protokollzeile mit dem tatsächlichen
  Grund. Keine stillen Verluste mehr.
- Bestell-BOD-Importe halten Unterpositionen an der richtigen Position; ein
  verschlepptes Flag hängte sie bisher an die falsche.
- Der Import einer CSV mit mehreren neuen Lieferanten funktioniert (ihre
  generierten IDs kollidieren nicht mehr), Aliasnamen für Skontobedingungen
  werden importiert und respektieren die „on conflict“-Einstellung, und die
  On-Conflict-Auswahl IGNORE gilt über Lieferanten hinaus.
- Der Lieferantenvorschlag (TF-IDF) behält seine Lieferanten-ID, wenn eine
  Einstellung aktualisiert wird — Vorschläge zeigen also nicht mehr ins
  Leere.

### Weitere Korrekturen

- Dashboard-Zeilen lösen Dropdown-Bezeichnungen in der Sprache des Benutzers
  auf, ohne die Anfrage zu blockieren.
- Nach dem Bearbeiten von Feldern aktualisiert sich der PO-Match-Status,
  statt den Stand vor der Bearbeitung anzuzeigen.
- Purchase-Order-Change-Dokumente erhalten fünf Felder in Parität zur
  Bestellung sowie ein Standard-Layout für die Feldvalidierung.
- Fehlerantworten über 152 Endpunkte hinweg liefern lesbare Meldungen statt
  roher Exception-Objekte, und die Log-Analytics-Seite antwortet für
  Organisationen ohne Log-Index nicht mehr mit 502.

## Auth Service — `1.77.9`

- Passwort-Zurücksetzen-E-Mails wurden stillschweigend nie versendet;
  behoben — zusammen mit dem darunterliegenden Thread-Safety-Problem.
- Ein wiederverwendetes Refresh-Token wird abgewiesen: Die maßgebliche
  Datenbankprüfung läuft jetzt jedes Mal, statt bei einem Cache-Treffer
  übersprungen zu werden.
- Zwei-Faktor-Authentifizierung: Eine Authenticator-App kann zusätzlich zu
  E-Mail-Codes eingerichtet werden, und das Entfernen des letzten Passkeys
  oder das Neugenerieren von Backup-Codes erfordert zuerst einen frischen
  zweiten Faktor.
- Eine gültige Unterorganisations-ID wird nicht mehr mit „Organization not
  found“ abgewiesen, und ein in einer Unterorganisation erstellter
  API-Schlüssel löst seinen technischen Benutzer aus dieser Unterorganisation
  auf.
- Das Bearbeiten einer Organisation validiert die Partner-ID und setzt den
  Organisationstyp nicht mehr als Nebeneffekt zurück.
- „Remaining tokens“ in der Abonnement-Ansicht bezieht sich auf das
  Vertragsjahr, nicht auf das Kalenderjahr.

## Auth Bridge Service — `0.5.7`

- Die Kontenreplikation zwischen der EU- und der US-Region erholt sich jetzt
  selbstständig. Ein abgerissener Replikationsstream verbindet sich an Ort
  und Stelle neu, die Replikation läuft weiter, während ein Abgleich
  ausgeführt wird, und der Speicherverbrauch des Abgleichs ist begrenzt,
  sodass der Service bei großen Tabellen nicht mehr in eine Absturzschleife
  gerät.

## Barcode Service — `1.18.7`

- Das Lesen von Barcodes läuft unter einem Zeitlimit und meldet einen
  Timeout, statt zu hängen — was das Dokument bisher in der Verarbeitung
  feststecken ließ.

## Docflow Service — `2.9.8`

- Feldwerte, die eine Workflow-Karte schreibt, landen in beiden
  gespeicherten Repräsentationen auf dem Dokument, sodass ein späterer
  Export sie nicht mehr zurücksetzt.
- Ein wiederholter Trigger behält die bereits erledigte Arbeit des Laufs,
  konkurrierende Trigger auf demselben Dokument stellen sich in eine
  Warteschlange, statt sich die Sperre zu stehlen, und ein eskalierter
  Wiederholungsversuch wird in der Warteschlange vorgezogen.
- Bestellvergleichs-Karten: Toleranzen werden als exakte Dezimalwerte
  verglichen und beziehen sich auf den Bestellwert, umgekehrte
  Vergleichsrichtungen stehen als Optionen zur Verfügung, eine zugewiesene
  Gruppe wird als Gruppe gemeldet, statt an einem Benutzer-ID-Vergleich zu
  scheitern, Zuweisungs-IDs werden korrekt als UUIDs verglichen, Zeilen mit
  leeren numerischen Werten werden übersprungen, und ein
  „received“-Vergleich ohne Wareneingangsdaten meldet fehlende Daten, statt
  eine Übereinstimmung vorzutäuschen.
- Die Karte „Apply Decision Table“ wurde eingestellt.

## Email Service — `1.41.0`

- Gmail-Importe holen jeden Anhang genau einmal ab; Duplikate durch
  überlappende Abrufe gehören der Vergangenheit an.
- Der Lesezeiger des Imports rückt erst vor, nachdem ein Import bestätigt
  wurde — ein Absturz mitten im Import kann also keine E-Mails mehr
  überspringen.
- Wird eine Importkonfiguration deaktiviert, weil eine ähnliche existiert,
  ist diese Deaktivierung jetzt sichtbar und wird gemeldet, statt still zu
  geschehen.

## Extraction Service — `1.54.5`

- Ob ein Dokument eine Gutschrift oder eine Rechnung ist, entscheidet jetzt,
  welches Schlüsselwort näher an der Dokumenttyp-Erwähnung steht — statt
  „erster Treffer gewinnt“.
- Liegen mehrere Steuerinterpretationen innerhalb der Toleranz, wird die
  exakte Abstimmung einem knappen Beinahe-Treffer vorgezogen.
- Nach einem erzwungenen erneuten OCR-Lauf werden Dokumenttyp und
  Spracheinstellung wiederhergestellt, sodass Tabellenextraktion und
  Training auf erneut per OCR verarbeiteten Dokumenten wieder funktionieren.
- Dokumente ohne Dokumenttyp bringen die Suche nach Tabellenregeln nicht
  mehr zum Absturz.

## FTP Service — `1.32.8`

- Das Scannen von Ordnern braucht nur noch einen Listendurchlauf pro Ordner
  mit begrenzter Tiefe — Importe aus großen FTP-Verzeichnissen sind dadurch
  deutlich schneller und laufen nicht mehr in Timeouts.

## Fulltext Service — `1.42.3`

- Dokumente, deren gespeicherte Suchdaten keine extrahierten Felder
  enthielten, werden aus der Datenbank neu indexiert und tauchen damit
  wieder in der Dashboard-Suche auf.
- Das Suchfenster des Dashboards unterstützt bis zu 10.000 Dokumente.
- Facettensuchen schlagen nicht mehr fehl, wenn die semantische Suche aktiv
  ist.

## OCR Service — `1.10.7`

- Das OCR-Zeitbudget bemisst sich an den realen Kosten pro Seite, sodass
  lange Dokumente fertig werden, statt am Pipeline-Limit zu scheitern.

## PO Match Service — `1.59.8`

- Tabellenzeilen mit Menge null werden bei Abweichungsprüfungen übersprungen,
  statt falsche Abweichungen zu erzeugen.
- Fehlen erforderliche PO-Match-Spalten, nennt das Ergebnis sie beim Namen.
