# DocBits Roadmap

_Planungsstand 18. September 2026. Jedes Release nennt den geplanten
Sandbox-Termin (ab dem Kunden es testen können) und den geplanten
Produktionstermin. Die Themen beschreiben, was für das Release geplant ist,
nicht, was bereits ausgeliefert wurde; Umfang und Termine können sich
verschieben. Hotfixes zwischen den Releases sind in den
[Release-Notizen](release-notes/README.md) dokumentiert._

| Release | Sandbox | Produktion |
|---|---|---|
| R1.1 | 5. Oktober 2026 | 14. Oktober 2026 |
| R1.2 | 23. November 2026 | 2. Dezember 2026 |
| R1.3 | 8. Februar 2027 | 17. Februar 2027 |
| R1.4 | 7. April 2027 | 15. April 2027 |
| R1.5 | 18. Mai 2027 | 27. Mai 2027 |
| R1.6 | 6. Juli 2027 | 15. Juli 2027 |
| R1.7 | 21. September 2027 | 30. September 2027 |
| R2.0 | wird noch bekannt gegeben | wird noch bekannt gegeben |

---

## R1.1 — Sandbox 5. Oktober 2026 · Produktion 14. Oktober 2026

**Transformationsregeln und Layouts**

- Eine Regel-Engine für extrahierte Feld- und Spaltenwerte: Werte setzen,
  ersetzen oder ableiten mit verschachtelten Bedingungsgruppen, dazu eine
  Einstellungsseite zur Verwaltung der Regeln. Regeln für die Layoutauswahl
  erhalten dieselben verschachtelten Bedingungen.
- Die Layoutauswahl funktioniert unabhängig davon, woher ein Dokument stammt.
- Klare Vorrangregeln für Feldbezeichnungen bei Kopffeldern und
  Tabellenspalten.
- Eine Tabellenspalte lässt sich nach dem Löschen erneut zuweisen, und die
  Lieferanten-Artikelpreistabelle zeigt alle ihre Spalten.

**Genehmigungs- und Validierungsbildschirm**

- Die drei Positionstabellen auf dem Genehmigungsbildschirm
  (Rechnungspositionen, Vergleichspositionen, Bestellabgleich) teilen sich
  einen Stil, und die Vergleichsansicht zeigt die Artikelnummer, die zur
  Position gehört.
- Das zuletzt geöffnete Seitenpanel (Aktivitätsstream oder
  Genehmigungshistorie) wird pro Benutzer gemerkt.
- Dokumente lassen sich vom Genehmigungsbildschirm aus mit dem
  Dokument-Uploader zusammenführen.
- Benutzerdefinierte Validierungsregeln behandeln Versandkosten generisch, und
  Regeln, die fälschlicherweise nicht angeschlagen haben, sind korrigiert.
- Ein Ladebalken ersetzt das einfache Ladesymbol; lesbarere Seiten-URLs.

**Duplikaterkennung**

- Benutzerdefinierte Felder erscheinen im Ergebnis der Duplikaterkennung, und
  die Duplikat-Einstellungen lassen sich durchsuchen.

**Workflows und Aufgaben**

- Eine Schaltfläche „Neuer Workflow“, Logs für erweiterte Workflows, ein
  übersichtlicherer Watchdog-Log-Bildschirm, und Workflow-Schritte, die ein
  Feld oder eine Checkbox ändern, greifen zuverlässig.
- Das Hinzufügen einer Zeile in einem Entscheidungsbaum behält die
  Benutzernamen bei, statt IDs anzuzeigen.
- Jede Statusänderung eines Dokuments wird protokolliert.
- Das Anlegen einer neuen E-Mail-Vorlage funktioniert wieder.

**Import**

- Der E-Mail-Import verschiebt eine Mail erst aus dem Posteingang, wenn der
  Upload bestätigt ist, behandelt eine erneut zugestellte Weiterleitung als
  eine Zustellung, hält fest, wer zuletzt gespeichert hat, und akzeptiert
  S/MIME-signierte Mails.
- Der FTP-Import erhält neben Verschieben und Archivieren eine echte Option
  „Nach dem Import löschen“.
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

**Dashboard**

- Das Dashboard fasst bis zu 10.000 Dokumente pro Suche.
- Skontofälligkeitsdatum und Rechnungsfälligkeitsdatum stehen als Layoutfelder
  zur Verfügung und werden beim Import gefüllt.
- Freigegebene Dashboard-Benutzer bleiben beim Speichern eines Dashboards
  erhalten, und „Updated by“ zeigt die richtige Person.
- Archivierte Dokumente lassen sich aus dem Status „Archived“ wieder
  zurückholen.

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

**Sicherheit**

- Die Organisationsprüfung für API-Schlüssel wird in jeder Umgebung
  durchgesetzt.

---

## R1.2 — Sandbox 23. November 2026 · Produktion 2. Dezember 2026

**Genehmigung und Bestellabgleich**

- Ein Status „Eingabe ausstehend“ pausiert ein Dokument, bis jemand
  antwortet, ohne den Workflow oder die Audit-Historie zu unterbrechen, und
  Genehmiger können Fragen stellen, ohne den Genehmigungsablauf zu
  unterbrechen.
- Vorauszahlungsrechnungen lassen sich vor dem Wareneingang abgleichen,
  während „Match on received quantity“ aktiv bleibt.
- Ein Kennzeichen zur Wareneingangsverfügbarkeit vergleicht in Rechnung
  gestellte und erhaltene Mengen.
- Auftragsbestätigungen: Kostenelemente werden angezeigt, während die
  Genehmigung aussteht, farblich markierte Zuschlagspositionen im
  Bestellabgleich, und die Artikelnummer-Spalte in den Rechnungspositionen.
- Spalten, die nicht gemappt sind, fließen nicht mehr in die Berechnung des
  Tabellenbetrags ein.
- Lieferanten-RMA-Positionen werden verarbeitet.

**Import und Klassifizierung**

- Die Absenderadresse steht aus dem E-Mail-Import zur Verfügung.
- Der Lieferantentyp wird aus den Positionen abgeleitet.

**Einstellungen und Automatisierung**

- Das Skript „Set sub-organisation“ wird zu einer Transformationsregel.
- Standardspalten lassen sich aus einem Dokumenttyp entfernen.

**Export**

- Die Exporthistorie listet exportierte Dokumente wieder auf.
- Frachtrechnungen werden nach Infor LN exportiert.

---

## R1.3 — Sandbox 8. Februar 2027 · Produktion 17. Februar 2027

**Auto Accounting Rule Manager**

- Regeln weisen Konten und Dimensionen automatisch zu, eingegrenzt pro
  Unterorganisation und Dokumenttyp, mit einem Audit-Bildschirm, der zeigt,
  welche Regel gegriffen hat.
- Eine Regel kann einen Wert aus einer Spalte der Tabellenpositionen befüllen.
- Felder und Dimensionen lassen sich einzeln leeren, Positionen lassen sich
  löschen (auch Positionen ohne Betrag), und Regeln funktionieren weiter bei
  Feldern, die von Text auf Dropdown umgestellt wurden.

**Bestellabgleich**

- Das Abgleichsymbol navigiert, scrollt und hebt tabübergreifend hervor, auch
  bei 1:n-Abgleichen.
- Einheitenumrechnung mit Aliassen (zum Beispiel KG und TO), eine
  konfigurierbare Rundungsabweichung mit Rundungskonto, und Berechnungen mit
  vier Dezimalstellen, angezeigt als drei.

**Export**

- Konfigurierbare Exportdateinamen.
- Ein unvollständiges Dokument in Infor LN wird nach einem fehlgeschlagenen
  Export gelöscht.
- Der Datenbank-Connector umfasst alle relevanten Tabellen.

---

## R1.4 — Sandbox 7. April 2027 · Produktion 15. April 2027

**Import**

- Ein Wiederholungsmechanismus für FTP-, E-Mail- und Inbound-E-Mail-Import
  mit automatischer und manueller Neuverarbeitung.

**DocNet Agents**

- Auftragserfassung: Aus einer Kundenbestellung wird ein Verkaufsauftrag in
  Infor M3 oder Infor LN (erste Version, Textdokumente).

**Genehmigung**

- Ein verbesserter Genehmigungsablauf, Delegation an einen anderen Benutzer
  während der Genehmigung, und eine Schaltfläche „Export & Next“.

**Bestellabgleich**

- Auf dem Abgleichbildschirm werden nur noch in Frage kommende
  Bestellpositionen angeboten.
- Rechnungen mit Mehrmenge, bei denen die in Rechnung gestellte Menge die
  erhaltene Menge übersteigt, werden auf dem Abgleichbildschirm erkannt, und
  Maßeinheiten werden beim Rechnungsabgleich umgerechnet.

**Sonstiges**

- Feedbackrunde zum Rule Manager.
- Das Support-Ticket-Formular akzeptiert Anhänge und verknüpft die
  Organisation automatisch.
- Erweiterte Vertex-Steuerintegration.

---

## R1.5 — Sandbox 18. Mai 2027 · Produktion 27. Mai 2027

**Auto Accounting**

- Lookup-Aktion im Rule Manager: Stammdaten abgleichen und mehrere Felder auf
  einmal zuweisen.
- Vorhersagen unterstützen mehrere Steuercodes und Dimensionen, Belege und
  Buchungsreferenzen.
- Auto-Accounting-Bildschirme in mehreren Sprachen.

**Genehmigung und Bestellabgleich**

- Ein Dokument einem anderen Benutzer neu zuweisen.
- Die Spaltenreihenfolge auf dem Bestellabgleich-Bildschirm wird pro Benutzer
  gespeichert.
- Zuschlagscodes (Maut, Transport, Energie) werden erkannt und ihre Kosten
  verteilt.

**Exportsperren**

- Der Export wird mit einer Warnung blockiert, wenn die abgeglichene Menge die
  erhaltene Menge übersteigt oder zu stark von ihr abweicht, oder wenn das
  Buchungsdatum vor dem Wareneingangsdatum liegt.

**Benutzerfreundlichkeit**

- Die Ausführungsreihenfolge der Dokumentskripte ist im Frontend sichtbar.
- Enter und Tab springen per Tastatur von Feld zu Feld.

---

## R1.6 — Sandbox 6. Juli 2027 · Produktion 15. Juli 2027

**Einstellungen**

- Die Einstellungen lassen sich über alle Schalter und Unterseiten hinweg
  durchsuchen.
- In der E-Mail-Server-Einrichtung können Sie ein abgelaufenes OAuth- oder
  Client-Secret ersetzen, ohne das Postfach neu einzurichten.
- Die Lieferanten-Artikelnummern-Zuordnung (Umschlüsselungstabelle für
  Artikelnummern) lässt sich per CSV-Import befüllen.

**Auto Accounting**

- Dimensionen werden in einer neuen Struktur gespeichert, damit große
  Dimensionssätze schneller laden.

---

## R1.7 — Sandbox 21. September 2027 · Produktion 30. September 2027

**Auto Accounting auf dem Genehmigungsbildschirm**

- Genehmiger können Auto Accounting direkt auf dem Genehmigungsbildschirm
  nutzen.
- Die Genehmigung lässt sich an Buchhaltungsfelder wie Sachkonto oder Land
  knüpfen, mit einer Kreditorenkorrektur, wenn ein Dokument zurückgegeben
  wird.
- Ein Steuercode-Dropdown in Auto Accounting, ohne mehrere Steuerzeilen
  einrichten zu müssen.

---

## R2.0 — Sandbox wird noch bekannt gegeben · Produktion wird noch bekannt gegeben

**Auto Accounting**

- Felder, die auf einer Liste basieren, akzeptieren auch Freitext.
- Pflichtfelder werden validiert.
- Modellvorhersagen füllen Buchhaltungsfelder automatisch (Hybridmodus mit dem
  trainierten Vorhersagemodell), mit einem Audit-Trail dessen, was das Modell
  befüllt hat.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
