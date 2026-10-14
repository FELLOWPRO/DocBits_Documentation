# DocBits Roadmap

_Planungsstand 7. Oktober 2026. Jedes Release nennt den geplanten
Sandbox-Termin (ab dem Kunden es testen können) und den geplanten
Produktionstermin. Die Themen beschreiben, was für das Release geplant ist,
nicht, was bereits ausgeliefert wurde; Umfang und Termine können sich
verschieben. Hotfixes zwischen den Releases sind in den
[Release-Notizen](release-notes/README.md) dokumentiert._

| Release | Sandbox | Produktion |
|---|---|---|
| R1.1 | 16. Oktober 2026 | 4. November 2026 |
| R1.2 | 16. Februar 2027 | 3. März 2027 |
| R1.3 | 1. Juni 2027 | 16. Juni 2027 |
| R1.4 | 5. Oktober 2027 | 20. Oktober 2027 |

---

## R1.1 — Sandbox 16. Oktober 2026 · Produktion 4. November 2026

**Transformationsregeln und Layouts**

- Eine Regel-Engine für extrahierte Feld- und Spaltenwerte: Werte setzen,
  ersetzen oder ableiten mit verschachtelten Bedingungsgruppen, dazu eine
  Einstellungsseite zur Verwaltung der Regeln. Die Bedingung „ist eines von“
  nimmt mehrere Werte entgegen, die Regelliste lässt sich nach Regel-ID
  durchsuchen, und Regeln laufen auch nach dem Stammdaten-Lookup.
- Regeln für die Layoutauswahl erhalten dieselben verschachtelten Bedingungen
  und ein optionales Ausführungslog. Die Layoutauswahl funktioniert unabhängig
  davon, woher ein Dokument stammt.
- Manage Layouts, Custom Validation Rules und Transformation Rules benötigen den
  Beta-Schalter nicht mehr.
- Klare Vorrangregeln für Feldbezeichnungen bei Kopffeldern und
  Tabellenspalten. Benutzer können eigene Übersetzungsschlüssel für
  Feldeinstellungen und Tabellenspalten anlegen.
- Eine Tabellenspalte lässt sich nach dem Löschen erneut zuweisen, und die
  Lieferanten-Artikelpreistabelle zeigt alle ihre Spalten.

**Genehmigungs- und Validierungsbildschirm**

- Die drei Positionstabellen auf dem Genehmigungsbildschirm
  (Rechnungspositionen, Vergleichspositionen, Bestellabgleich) teilen sich
  einen Stil.
- Das zuletzt geöffnete Seitenpanel (Aktivitätsstream oder
  Genehmigungshistorie) wird pro Benutzer gemerkt.
- Dokumente lassen sich vom Genehmigungsbildschirm aus mit dem
  Dokument-Uploader zusammenführen.
- Benutzerdefinierte Validierungsregeln behandeln Versandkosten generisch,
  zeigen eine Feldmeldung statt eines allgemeinen Fehlers, wenn ein Pflichtfeld
  leer ist, und Regeln, die fälschlicherweise nicht angeschlagen haben, sind
  korrigiert. Standardregeln des Systems lassen sich duplizieren.
- Eine Abweichung zwischen Menge und Nettobetrag bei einer KI-extrahierten
  Tabelle wird gemeldet, eine Rechnung mit abgeglichener Bestellung wird nicht
  mehr als Kostenrechnung klassifiziert, und ein von einer Regel umformatiertes
  Datum wird akzeptiert.
- Ein Genehmigungsbildschirm, der nach dem Genehmigen oder Ablehnen im
  Lade-Overlay hing, ist behoben. Ein Ladebalken ersetzt das einfache
  Ladesymbol; Seiten-URLs sind lesbarer.
- Das Öffnen eines Dokumentlinks nach Ablauf der Sitzung führt zur Anmeldeseite
  statt zu einem 404.

**Duplikaterkennung**

- Benutzerdefinierte Felder erscheinen im Ergebnis der Duplikaterkennung, und
  die Duplikat-Einstellungen lassen sich durchsuchen.
- „Block Duplicate Document Export“ blockiert den Export eines erkannten
  Duplikats.

**Workflows und Aufgaben**

- Eine Schaltfläche „Neuer Workflow“, Logs für erweiterte Workflows, ein
  übersichtlicherer Watchdog-Log-Bildschirm, und Workflow-Schritte, die ein
  Feld oder eine Checkbox ändern, greifen zuverlässig.
- Das Hinzufügen einer Zeile in einem Entscheidungsbaum behält die
  Benutzernamen bei, statt IDs anzuzeigen.
- Jede Statusänderung eines Dokuments wird protokolliert.
- Das Anlegen einer neuen E-Mail-Vorlage funktioniert wieder.
- Die Aufgabenliste zeigt ihre Aufgaben beim ersten Laden.

**Import**

- Der E-Mail-Import verschiebt eine Mail erst aus dem Posteingang, wenn der
  Upload bestätigt ist, behandelt eine erneut zugestellte Weiterleitung als
  eine Zustellung, hält fest, wer zuletzt gespeichert hat, und führt einen
  Anhang bei einem Fehler einmal mit dem Grund auf.
- Der FTP- und SFTP-Import erhält neben Verschieben und Archivieren eine echte
  Option „Nach dem Import löschen“. Passwörter werden beim Bearbeiten einer
  Konfiguration nicht mehr beschädigt, der Verbindungstest funktioniert für neue
  SFTP-Verbindungen, und eine fehlgeschlagene SFTP-Verbindung oder eine falsche
  Anmeldung zeigt eine konkrete Meldung statt eines allgemeinen Fehlers.
- Administratoren werden im Settings Assistant informiert, wenn ein
  konfigurierter FTP- oder E-Mail-Import nicht mehr funktioniert.
- Der Upload aus der Scanner-App funktioniert wieder.
- Bestell-BOD-Dateien, die in der US-Region hochgeladen werden, bleiben in der
  US-Region.

**Dokumentenverarbeitung und Extraktion**

- Wenn der Barcode-Service hängt, zeigt das Dokument den Fehler an, statt
  unbegrenzt in „Processing“ zu bleiben.
- Eine neue, günstigere KI-Modellstufe („Eco“) für die Extraktion.
- Bei der strukturierten KI-Extraktion bleiben trainierte
  Lieferanten-Artikelnummern trainiert, und Artikelnummer und
  Lieferanten-Artikelnummer werden nicht mehr vertauscht.
- UBL-E-Dokument-Vorlagen werden angepasst; Extraktionskorrekturen für
  Beträge, Steuersätze, Einheitspreise und Bestellnummern bei bestimmten
  Lieferantenlayouts.
- Zusätzliche Datumsformate werden erkannt.
- Eine Kostenrechnung mit zwei Mehrwertsteuersätzen behält beide
  Buchungszeilen.

**Bestellabgleich**

- Der Abgleich setzt eine Mengenspalte voraus, verwendet den Preis pro
  Basismengeneinheit, und der Fallback auf die letzte Position lässt sich pro
  Kunde umschalten.
- Lieferscheinpositionen lassen sich einzeln auswählen.
- Der E-Dokument-Bildschirm friert bei Rechnungen mit mehr als 250 Positionen
  nicht mehr ein.

**Touchless Intelligence**

- Mehr Details im Touchless-Bericht, und die Touchless-Checkbox spiegelt die
  gespeicherte Einstellung wider.

**Dashboard, Konten und Abonnement**

- Das Dashboard fasst bis zu 10.000 Dokumente pro Suche, und ein
  benutzerdefinierter Datumsfilter wird korrekt angewendet.
- Skontofälligkeitsdatum und Rechnungsfälligkeitsdatum stehen als Layoutfelder
  zur Verfügung und werden beim Import gefüllt.
- Freigegebene Dashboard-Benutzer bleiben beim Speichern eines Dashboards
  erhalten, und „Updated by“ zeigt die richtige Person.
- Archivierte Dokumente lassen sich aus dem Status „Archived“ wieder
  zurückholen.
- Benutzer können sich nach dem Zurücksetzen des Passworts wieder anmelden.
- Die Seite des Abonnementplans zeigt die Nutzung für den Plan und seine
  Funktionen.

**Export und EDI**

- Ein zusätzlicher Exportschritt nach Infor M3 für weitere
  Rechnungsinformationen.
- Eine Packliste mit mehreren Containernummern wird als ein Datensatz pro
  Container exportiert.
- Der erneute Import einer Receive Delivery scheitert nicht mehr an einem
  doppelten Schlüssel, und Receive-Delivery-BODs werden in der richtigen
  Reihenfolge angewendet.
- Die EDI-Mappings für Rechnung, Bestellung und Auftragsbestätigung werden
  aktualisiert.
- Der Verbindungstest einer neuen Infor-IDM- oder Infor-LN-Exportkonfiguration
  funktioniert.

**Sicherheit**

- Die Organisationsprüfung für API-Schlüssel wird in jeder Umgebung
  durchgesetzt.

---

## R1.2 — Sandbox 16. Februar 2027 · Produktion 3. März 2027

**Genehmigung und Bestellabgleich**

- Ein Status „Eingabe ausstehend“ pausiert ein Dokument, bis jemand
  antwortet, ohne den Workflow oder die Audit-Historie zu unterbrechen, und
  Genehmiger können Fragen stellen, ohne den Genehmigungsablauf zu
  unterbrechen.
- Ein Dokument lässt sich einem anderen Benutzer neu zuweisen (erste Phase).
- Vorauszahlungsrechnungen lassen sich vor dem Wareneingang abgleichen,
  während „Match on received quantity“ aktiv bleibt.
- Der Abgleichbildschirm bietet nur noch in Frage kommende Bestellpositionen
  an, und Abgleiche über mehrere Positionen, die den Preisvergleich
  überspringen, zeigen auf dem Genehmigungsbildschirm weiterhin den
  Einheitspreis.
- Ein Kennzeichen zur Wareneingangsverfügbarkeit vergleicht in Rechnung
  gestellte und erhaltene Mengen.
- Auftragsbestätigungen: Kostenelemente werden angezeigt, während die
  Genehmigung aussteht, farblich markierte Zuschlagspositionen im
  Bestellabgleich, und die Artikelnummer-Spalte in den Rechnungspositionen.
- Lieferanten-RMA-Positionen werden verarbeitet.

**Import und Klassifizierung**

- Der Lieferantentyp wird aus den Positionen abgeleitet.
- Das Support-Ticket-Formular akzeptiert Anhänge und verknüpft die
  Organisation automatisch.

**Einstellungen und Automatisierung**

- Das Skript „Set sub-organisation“ wird zu einer Transformationsregel.
- Standardspalten lassen sich aus einem Dokumenttyp entfernen.

**Export**

- Die Exporthistorie listet exportierte Dokumente wieder auf.
- Frachtrechnungen werden nach Infor LN exportiert.
- Konfigurierbare Exportdateinamen.
- Erweiterte Vertex-Steuerintegration.

---

## R1.3 — Sandbox 1. Juni 2027 · Produktion 16. Juni 2027

**Auto Accounting Rule Manager**

- Regeln weisen Konten und Dimensionen automatisch zu, eingegrenzt pro
  Unterorganisation und Dokumenttyp, mit einem Audit-Bildschirm, der zeigt,
  welche Regel gegriffen hat.
- Eine Regel kann Stammdaten nachschlagen und mehrere Felder auf einmal
  zuweisen oder einen Wert aus einer Spalte der Tabellenpositionen befüllen.
- Felder und Dimensionen lassen sich einzeln leeren, Positionen lassen sich
  löschen (auch Positionen ohne Betrag), und Regeln funktionieren weiter bei
  Feldern, die von Text auf Dropdown umgestellt wurden.
- Vorhersagen unterstützen mehrere Steuercodes und Dimensionen, Belege und
  Buchungsreferenzen. Die Auto-Accounting-Bildschirme sind in mehreren Sprachen
  verfügbar.

**Bestellabgleich**

- Das Abgleichsymbol navigiert, scrollt und hebt tabübergreifend hervor, auch
  bei 1:n-Abgleichen.
- Einheitenumrechnung mit Aliassen (zum Beispiel KG und TO), eine
  konfigurierbare Rundungsabweichung mit Rundungskonto, und Berechnungen mit
  vier Dezimalstellen, angezeigt als drei.

**Benutzerfreundlichkeit**

- Die Ausführungsreihenfolge der Dokumentskripte ist im Frontend sichtbar.
- Enter und Tab springen per Tastatur von Feld zu Feld.

**Export**

- Ein unvollständiges Dokument in Infor LN wird nach einem fehlgeschlagenen
  Export gelöscht.
- Der Datenbank-Connector umfasst alle relevanten Tabellen.

---

## R1.4 — Sandbox 5. Oktober 2027 · Produktion 20. Oktober 2027

**Auto Accounting auf dem Genehmigungsbildschirm**

- Genehmiger können Auto Accounting direkt auf dem Genehmigungsbildschirm
  nutzen.
- Die Genehmigung lässt sich an Buchhaltungsfelder wie Sachkonto oder Land
  knüpfen, mit einer Kreditorenkorrektur, wenn ein Dokument zurückgegeben
  wird.
- Ein Steuercode-Dropdown in Auto Accounting, ohne mehrere Steuerzeilen
  einrichten zu müssen.
- Dimensionen werden in einer neuen Struktur gespeichert, damit große
  Dimensionssätze schneller laden, und der Rule Manager erhält eine
  Feedbackrunde.

**Genehmigung**

- Ein verbesserter Genehmigungsablauf, Delegation an einen anderen Benutzer
  während der Genehmigung, und eine Schaltfläche „Export & Next“.

**Bestellabgleich und Exportsperren**

- Rechnungen mit Mehrmenge, bei denen die in Rechnung gestellte Menge die
  erhaltene Menge übersteigt, werden auf dem Abgleichbildschirm erkannt, und
  Maßeinheiten werden beim Rechnungsabgleich umgerechnet.
- Zuschlagscodes (Maut, Transport, Energie) werden erkannt und ihre Kosten
  verteilt.
- Der Export wird mit einer Warnung blockiert, wenn die abgeglichene Menge die
  erhaltene Menge übersteigt oder zu stark von ihr abweicht, oder wenn das
  Buchungsdatum vor dem Wareneingangsdatum liegt.

**Import und Einstellungen**

- Ein Wiederholungsmechanismus für FTP-, E-Mail- und Inbound-E-Mail-Import
  mit automatischer und manueller Neuverarbeitung, und die Absenderadresse
  steht aus dem E-Mail-Import zur Verfügung.
- Die Einstellungen lassen sich über alle Schalter und Unterseiten hinweg
  durchsuchen.
- In der E-Mail-Server-Einrichtung können Sie ein abgelaufenes OAuth- oder
  Client-Secret ersetzen, ohne das Postfach neu einzurichten.
- Die Lieferanten-Artikelnummern-Zuordnung (Umschlüsselungstabelle für
  Artikelnummern) lässt sich per CSV-Import befüllen.
- Die Genehmigungshistorie lässt sich über den SFTP-Export exportieren.

**DocNet Agents**

- Auftragserfassung: Aus einer Kundenbestellung wird ein Verkaufsauftrag in
  Infor M3 oder Infor LN (erste Version, Textdokumente).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
