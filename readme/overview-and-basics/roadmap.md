# DocBits Roadmap

_Planungsstand 15. September 2026. Jedes Release nennt den geplanten
Sandbox-Termin (ab dem Kunden es testen können) und den geplanten
Produktionstermin. Die Themen beschreiben, was für das Release geplant ist,
nicht, was bereits ausgeliefert wurde; Umfang und Termine können sich
verschieben. Hotfixes zwischen den Releases sind in den
[Release-Notizen](release-notes/README.md) dokumentiert._

| Release | Sandbox | Produktion |
|---|---|---|
| R1.1 | 16. September 2026 | 23. September 2026 |
| R1.2 | 21. Oktober 2026 | 28. Oktober 2026 |
| R1.3 | 25. November 2026 | 2. Dezember 2026 |
| R1.4 | 27. Januar 2027 | 3. Februar 2027 |
| R1.5 | 10. März 2027 | 17. März 2027 |

---

## R1.1 — Sandbox 16. September 2026 · Produktion 23. September 2026

**Transformationsregeln und Layouts**

- Eine Regel-Engine für extrahierte Feld- und Spaltenwerte: Werte setzen,
  ersetzen oder ableiten mit verschachtelten Bedingungsgruppen, dazu eine
  Einstellungsseite zur Verwaltung der Regeln. Regeln für die Layoutauswahl
  erhalten dieselben verschachtelten Bedingungen.
- Die Layoutauswahl funktioniert unabhängig davon, woher ein Dokument stammt.
- Klare Vorrangregeln für Feldbezeichnungen bei Kopffeldern und
  Tabellenspalten.

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

- Eine Schaltfläche „Neuer Workflow“, Logs für erweiterte Workflows, und
  Workflow-Schritte, die ein Feld oder eine Checkbox ändern, greifen
  zuverlässig.
- Genehmigungs-E-Mails erreichen die zugewiesenen Genehmiger in
  Eingangsrechnungs-Workflows.
- Jede Statusänderung eines Dokuments wird protokolliert.

**Import**

- Der E-Mail-Import verschiebt eine Mail erst aus dem Posteingang, wenn der
  Upload bestätigt ist, behandelt eine erneut zugestellte Weiterleitung als
  eine Zustellung, hält fest, wer zuletzt gespeichert hat, und akzeptiert
  S/MIME-signierte Mails.
- Der FTP-Import erhält neben Verschieben und Archivieren eine echte Option
  „Nach dem Import löschen“.
- Der Upload aus der Scanner-App funktioniert wieder.

**Dokumentenverarbeitung und Extraktion**

- Wenn der Barcode-Service hängt, zeigt das Dokument den Fehler an, statt
  unbegrenzt in „Processing“ zu bleiben.
- „Restrict to pages“ begrenzt nur noch OCR und Seitenzählung; es schneidet
  keine Seiten mehr vom Dokument ab.
- Das Speichern eines Dokuments lässt nicht betroffene Daten unangetastet.
- Eine neue, günstigere KI-Modellstufe („Eco“) für die Extraktion, und das
  Anwenden von Tabellen-Tags auf die KI-Tabelle funktioniert wieder.
- Das Zusammenführen einer ZUGFeRD-PDF mit einer anderen PDF behält die
  E-Rechnungsdaten; UBL-E-Dokument-Vorlagen werden angepasst;
  Extraktionskorrekturen für Beträge, Steuersätze und Bestellnummern bei
  bestimmten Lieferantenlayouts.
- Zusätzliche Datumsformate werden erkannt.

**Bestellabgleich**

- Der Abgleich setzt eine Mengenspalte voraus, verwendet den Preis pro
  Basismengeneinheit, und der Fallback auf die letzte Position lässt sich pro
  Kunde umschalten.
- Der E-Dokument-Bildschirm friert bei Rechnungen mit mehr als 250 Positionen
  nicht mehr ein.
- Die Diagnose misst die Menge auch dann, wenn eine Bestellposition keinen
  Preis hat.

**Touchless Intelligence**

- Mehr Details im Touchless-Bericht, und ein Bestell-Blocker wird als solcher
  gemeldet statt als fehlgeschlagene Feldvalidierung.

**Dashboard**

- Das Dashboard fasst bis zu 10.000 Dokumente pro Suche.
- Skontofälligkeitsdatum und Rechnungsfälligkeitsdatum stehen als Layoutfelder
  zur Verfügung und werden beim Import gefüllt.
- Freigegebene Dashboard-Benutzer bleiben beim Speichern eines Dashboards
  erhalten; „Assigned to“ und „Updated by“ zeigen die richtige Person.
- Dokumentberechtigungen gelten auch für den Volltextindex.

**Export und EDI**

- Der BOD-Export behält Tabellenspaltenwerte mit mehr als 30 Zeichen.
- Ein zusätzlicher Exportschritt nach Infor M3 für weitere
  Rechnungsinformationen, und Einheitspreise in Exporten des Positionstyps 5.
- Der erneute Import einer Receive Delivery scheitert nicht mehr an einem
  doppelten Schlüssel.
- Die EDI-X12-Mappings für Rechnung (810), Bestellung (850),
  Auftragsbestätigung (855), Lieferavis (856, einschließlich WMS-Export) und
  Bestelländerung (860) werden aktualisiert.

**Sicherheit**

- Lieferanten-Kontenplan-Mappings werden mit gebundenen SQL-Parametern
  gespeichert, und die Organisationsprüfung für API-Schlüssel wird in jeder
  Umgebung durchgesetzt.

---

## R1.2 — Sandbox 21. Oktober 2026 · Produktion 28. Oktober 2026

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
- Ein Ablauf für Bestelländerungsanfragen und der Dokumenteigentümer im
  Infor-Export-Mapping.

**Export**

- Die Exporthistorie listet exportierte Dokumente wieder auf.
- Frachtrechnungen werden nach Infor LN exportiert.

---

## R1.3 — Sandbox 25. November 2026 · Produktion 2. Dezember 2026

**Auto Accounting Rule Manager**

- Regeln weisen Konten und Dimensionen automatisch zu, eingegrenzt pro
  Unterorganisation und Dokumenttyp, mit einem Audit-Bildschirm, der zeigt,
  welche Regel gegriffen hat.
- Eine Regel kann einen Wert aus einer Spalte der Tabellenpositionen befüllen.
- Felder und Dimensionen lassen sich einzeln leeren, Positionen ohne Betrag
  lassen sich löschen, und Regeln funktionieren weiter bei Feldern, die von
  Text auf Dropdown umgestellt wurden.

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

## R1.4 — Sandbox 27. Januar 2027 · Produktion 3. Februar 2027

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
- Mehrere Wareneingänge können auf eine Rechnungsposition passen, und
  Maßeinheiten werden beim Rechnungsabgleich umgerechnet.

**Sonstiges**

- Feedbackrunde zum Rule Manager.
- Das Support-Ticket-Formular akzeptiert Anhänge und verknüpft die
  Organisation automatisch.
- Erweiterte Vertex-Steuerintegration.

---

## R1.5 — Sandbox 10. März 2027 · Produktion 17. März 2027

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

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
