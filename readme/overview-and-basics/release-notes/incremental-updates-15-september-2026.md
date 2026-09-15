# DocBits Release-Notizen — 15. September 2026

_Was sich mit dem DocBits-Produktions-Hotfix am 15. September 2026 (Release
R1.0.13) ändert — alles seit dem Release vom 1. September. Jeder Service unten
zeigt die Version, die ausgerollt wird, gefolgt von dem, was neu oder behoben
ist, in klarer Sprache. Nicht aufgeführte Services hatten keine für Kunden
sichtbaren Änderungen._

---

## Highlights

- **Ein Regelwerk für die Dashboard-Suche.** `field=value` bedeutet jetzt auf
  jeder Suchmaschine genau diesen Wert, `field:value` bedeutet „enthält“ (mit
  `value*` und `*value` für „beginnt mit“ und „endet mit“), und `field!=value`
  liefert auch Dokumente, die gar keinen Wert haben. Eine Suche ohne Chip ist
  eine Teilstring-Suche über alle Felder, Geschäftskennungen eingeschlossen.
  Trefferzahl und Trefferliste beschreiben dieselbe Dokumentmenge, und eine
  Suche, die an das Ergebnisfenster gestoßen ist oder ohne den Volltextindex
  lief, sagt das, statt „vollständig“ zu melden. Die eigene Suchverbindung des
  Dashboards (WebSocket) hat den Volltextindex bisher nie erreicht; jetzt tut
  sie es.
- **Lieferanten werden häufiger erkannt.** Wenn ein Nachschlagefeld
  (Steuernummer, IBAN, Lieferantennummer) genau einen Lieferanten trifft, wird
  dieser Lieferant verwendet — auch wenn ein breites Feld wie der Name mehrere
  trifft. XRechnung-CII- und Facturae-Dokumente führen ihre Lieferantenfelder
  wieder mit. Wo Stammdaten einen extrahierten Wert ersetzt haben, sagt der
  Validierungsbildschirm das und lässt Sie das Original wiederherstellen.
- **Der Bestellabgleich erklärt sich selbst.** Der Bildschirm sagt, warum kein
  Abgleich vorliegt und warum ein Abgleich nicht beibehalten wurde, die
  Abgleichhistorie listet die ausgeführten Transformationsregeln auf, und
  Bestell-Einheitspreise werden aus dem Nettobetrag abgeleitet. Manuelle
  Abgleiche funktionieren wieder für Organisationen ohne Fallback-Regel, und
  eine abgebrochene Abgleichaufgabe markiert das Dokument als fehlgeschlagen,
  statt es für immer in „Queue“ zu parken.
- **Hängende Dokumente und falsche Fehler.** Bei Organisationen, die
  kontinuierlich hochladen, wurden Dokumente auf eine Warteschlangenpriorität
  herabgestuft, die während der Geschäftszeiten nie bedient wurde (866
  Dokumente hingen bei einem Kunden in „new“ fest). Ein Retry-Sweeper konnte
  ein erfolgreich exportiertes Dokument Stunden später mit „error“
  überschreiben und dafür die Exportfehler-Mail auslösen. Dieser Pfad ist
  geschlossen.
- **Touchless Intelligence.** Der Analytics-Tab, der misst, wie viele
  Dokumente DocBits ohne menschliches Zutun durchlaufen, erhält sein
  vollständiges erstes Release: Problem-Cluster mit KI-Empfehlungen,
  Massenanalyse, Änderungsvorschläge mit Vorschau, Anwenden und Rückgängig,
  eine KI-Diagnose pro Lieferant und ein Pipeline-Flussdiagramm pro Dokument.
- **Schneller bei großen Datenmengen.** Das Accounting-Dropdown funktioniert
  für Organisationen mit mehr als 2.000 Konten, die Regelseite unter
  E-Dokumente blättert ihre 1.600 Regeln auf dem Server, statt den Browser
  einzufrieren, und „Refresh“ auf dem Bestell-Dashboard liefert frische Daten
  statt einer zwischengespeicherten Liste.
- **Sicherheit.** Frontend-Source-Maps werden nicht mehr mit jedem Deploy
  ausgeliefert, Filter im Stammdaten-Lookup werden als SQL-Parameter gebunden
  statt in die Abfrage eingefügt, ein abgelaufenes Token wird auch bei einem
  Cache-Treffer abgewiesen, und die Organisationsprüfung des
  Verarbeitungs-Tokens wird unabhängig von der davor liegenden Schicht
  durchgesetzt.

---

## Web App — `10.66.3`

### Anmeldung und Konten

- Das Overlay „Updating DocBits v10.59.3.1 → v10.59.3.1“, das auf Sandbox
  endlos neu lud, ist behoben. Ein Neuladen bei gleicher Version zeigt das
  Overlay nicht mehr, die Schleife ist pro Tab begrenzt, und ein Banner bietet
  eine manuelle Wiederherstellung an, falls es erneut passiert.
- Die Checkbox „System Admin“ kann bei einem bestehenden Benutzer gesetzt
  werden. Das Anlegen eines Systemadministrators über das Frontend hat jetzt
  eine Wirkung; ein Sync-Job setzte das Flag bisher bei jedem Lauf zurück.

### Dashboard und Suche

- Neue Operatorregeln, auch im Hilfe-Popup der Suche beschrieben: `=` ist
  genau dieser Wert (ohne Unterscheidung von Groß- und Kleinschreibung), `:`
  ist „enthält“, `: value*` „beginnt mit“, `: *value` „endet mit“, `!=` ist
  alles, was nicht genau dieser Wert ist, einschließlich Dokumente ohne Wert.
  Anführungszeichen gruppieren nur einen Wert mit Leerzeichen.
- Eine Phrase in Anführungszeichen wie `"Johnson and Johnson"` wird als eine
  Phrase gesucht. „and“ und „or“ innerhalb von Anführungszeichen werden nicht
  mehr als Verknüpfungen gelesen.
- Findet eine Suche ohne Chip nichts, erklärt das Dashboard die Regel und
  bietet Ein-Klick-Chips an (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Eine Suche ohne Treffer setzt die Seitennavigation zurück. Bisher behielt
  die Paginierung die Trefferzahl der vorherigen Suche.
- Anforderungsnummern und Anforderer werden über eine einfache Suche gefunden,
  ohne Chip.

### Validierungsbildschirm

- Werte, die Stammdaten ersetzt haben, werden markiert. Ein bernsteinfarbenes
  Badge zeigt den ursprünglichen und den aktuellen Wert, den Datensatz und
  wie er getroffen hat, und eine Schaltfläche stellt den extrahierten Wert
  wieder her. Werte, die Stammdaten bestätigt haben oder die aus der
  Bestellung gefüllt wurden, erhalten eigene Bezeichnungen. Bisher trugen
  alle das Badge „Extracted using saved rules“.
- Der Genehmigungsstempel wird auch dann gespeichert, wenn die Seite bereits
  eine andere Annotation trägt. Heruntergeladene annotierte Dokumente hatten
  in diesem Fall keinen Stempel.
- „Nicht zugeordnete Spalten ausblenden“ behält Spalten, die Sie von Hand
  trainiert haben (zum Beispiel Artikelnummer und Bestellung).
- Das Speichern von Extraktionsregeln funktioniert, nachdem Sie eine
  Seitenzahl eingegeben und dann eine Box für ein Feld gezeichnet haben. Diese
  Reihenfolge ließ das Speichern bisher abstürzen.
- „Modell trainieren“ läuft im Hintergrund. Der Bildschirm zeigt „training
  started“, fragt das Ergebnis ab und meldet Erfolg oder Fehlschlag. Große
  Organisationen erhielten bisher einen Gateway-Fehler, während das Training
  serverseitig weiterlief.
- Dark Mode: Der Scheren-Cursor auf dem Split-Bildschirm und der
  Modus-Umschalter auf dem Auto-Accounting-Bildschirm sind wieder lesbar.

### Bestellabgleich

Die in [Hotfixes 8. September 2026](incremental-updates-8-september-2026.md)
angekündigten Änderungen erreichen mit diesem Release die Produktion: Der
Abgleich bleibt beim Speichern erhalten, der Abgleich wird erneut ausgeführt,
wenn die Bestellnummer korrigiert wird, der Bildschirm sagt, warum kein
Abgleich vorliegt und warum ein Abgleich nicht beibehalten wurde, die
Abgleichhistorie zeigt die Transformationsregeln, und der Bestell-Einheitspreis
wird aus dem Nettobetrag berechnet. Darüber hinaus:

- Die Schaltfläche „Auto Match“ exportiert das Dokument auch, wenn „PO Auto
  Match and Export“ aktiviert ist. Bisher fand der Export nur statt, wenn das
  Dokument über „PO Match“ aus dem Dashboard geöffnet wurde.
- Das Popup für die Mengen-/Einheitspreis-Toleranz bleibt offen, wenn der
  Server das Speichern ablehnt, sodass die eingegebenen Werte nicht verloren
  gehen.
- Die Schaltfläche „Refresh“ auf dem Bestell-Dashboard leert den
  serverseitigen Cache vor dem Neuladen. Eine aus dem ERP importierte
  Bestellung erschien erst nach sieben bis acht Minuten.

### Auto Accounting

- Organisationen mit mehr als 2.000 Konten durchsuchen die Kontenliste auf dem
  Server. Das Dropdown war auf Sandbox für solche Organisationen leer, und das
  Laden der Seite dauerte fünf Sekunden.
- Konten, auf die ein Dokument verweist, werden in Batches aufgelöst: Ein
  Dokument mit 100 Positionen und zwei Splits pro Position braucht 4 Anfragen
  statt 403.
- Die Überschriften der Auto-Accounting- und Bestelltabellen folgen der im
  Layout-Builder festgelegten Bezeichnung statt einem fest hinterlegten Text.

### Einstellungen

- Einstellungen → E-Dokumente → Regeln blättert, durchsucht und sortiert den
  Katalog mit 1.600 Regeln auf dem Server. Der Tab renderte bisher jede Regel
  auf einmal und ließ den Browser einfrieren. „Reset all“ ist ein Aufruf statt
  einer pro Regel.
- Die erweiterten Einstellungen eines Dokumenttyps zeigen den gespeicherten
  Zustand jedes Schalters. Ein gespeichertes `false`, eine Toleranz von `0`
  oder eine leere Auswahl wurden durch den Standardwert ersetzt, und beim
  Wechsel des Dokumenttyps blieben die Werte des vorherigen Typs stehen.
- Transformationsregeln: Eine Aktion „Set value“ lässt sich speichern. Der
  Editor sendete sie unter einem Namen, den der Server ablehnt.
- Der Link zu den Dokumentuntertypen wird bei Standard-Dokumenttypen
  angezeigt.
- Das JPL-Mapping des SMB-Exports wird als `.properties` heruntergeladen,
  sodass die Datei wieder hochgeladen werden kann. Sie hieß `.xml` und wurde
  beim erneuten Hochladen abgelehnt.

### Workflows

- Das Umbenennen eines Workflows behält die in derselben Sitzung
  vorgenommenen Kartenänderungen. Neue Workflows werden in einer einzigen
  Speicheranfrage angelegt, und Umbenennungen von Vorlagen werden gespeichert.
- Eine exportierte Workflow-Datei enthält den gesamten Export-Umschlag
  (Version, Name, Beschreibung). Erweiterte Workflows lassen sich wieder
  importieren; bisher verlor die Datei ihre Version, wurde als
  Standard-Workflow eingelesen und abgelehnt.
- Spaltenfilter in der Workflow-Liste werden mit UND verknüpft. Bei aktivem
  Namens- und Datumsfilter rutschten Zeilen ins Ergebnis, die nur auf den
  Namen passten.
- Aufgabenfristen verwenden das Datumsformat aus Ihren Benutzereinstellungen
  in der Liste, auf dem Board und in der Detailansicht.

### Analytics: Touchless Intelligence

Der Tab „Touchless“ (Analytics → Touchless) misst, wie viele Dokumente DocBits
durchlaufen, ohne dass eine Person sie anfasst, und warum die anderen es nicht
getan haben. Dieses Release vervollständigt ihn:

- **Problem-Cluster mit Belegen.** Dokumente, die einen Eingriff brauchten,
  werden nach Ursache gruppiert. Jede Cluster-Karte nennt die Felder,
  Validierungscodes und Fehlermeldungen, an denen sie scheitert, und ihren
  Lieferanten — oder sagt, dass es keinen gibt. Cluster, die DocBits beheben
  kann (eine Regel, eine Feldeinstellung), werden von denen getrennt, die nur
  der Lieferant beheben kann, und das Budget für die KI-Analyse geht zuerst an
  die behebbaren.
- **KI-Analyse, als solche gekennzeichnet.** Eine Cluster-Karte sagt, ob ein
  Sprachmodell die Empfehlung geschrieben hat oder eine Regel, was die Analyse
  gezählt hat und ab wann sie nicht mehr gilt, und ob ein Klick eine
  zwischengespeicherte Analyse wiederverwendet. Kann der KI-Berater in dieser
  Umgebung nicht laufen, sagt der Tab, warum.
- **Massenanalyse.** Analysieren Sie viele Cluster in einem Lauf, sehen Sie
  Cluster für Cluster, was der Lauf gerade tut, und finden Sie die Ergebnisse
  danach wieder. Die Ergebnisliste übersteht Navigation und Neuladen, und der
  Lauf bleibt in einer Unterorganisationsansicht nicht mehr bei „Running · 0/6
  done“ hängen.
- **Änderungsvorschläge.** Aus einer Empfehlung wird etwas, worauf Sie
  reagieren können: ein Vorschlag, der auf das Feld zielt, das die Dokumente
  blockiert, eine Vorschau, die zeigt, was er bewirken würde (nichts wird
  gespeichert), Anwenden, gemessene Wirkung und Rückgängig. Agenten erreichen
  dieselben Schritte über MCP-Tools. Behebungsschritte verlinken direkt auf
  die genannte Einstellungsseite, vorgefiltert nach Dokumenttyp, Feld oder
  Regel.
- **Lieferantendiagnose.** Die Lieferantenseite erklärt einen leeren Zustand,
  statt Nullen anzuzeigen, und bietet eine KI-Diagnose pro Lieferant an. Bis
  zu fünf Lieferanten lassen sich auswählen und nebeneinander vergleichen.
- **Pipeline-Fluss.** Ein Diagramm pro Dokument und pro Cluster zeigt den Weg
  durch Eingang, Klassifizierung, E-Dokument-Prüfung, Lieferant, OCR,
  Extraktion, Validierung, Bestellabgleich, Freigabe und Export — mit der
  Stufe, die ihn gestoppt hat.
- **Gründe beim Bestellabgleich.** Die Abgleichentscheidung wird pro Dokument
  nachverfolgt (Stufe, Durchlauf, Regel, Spalte) und im Touchless-Ergebnis
  verdichtet. Ursachencodes unterscheiden „Bestellung nicht gefunden“ von
  „Position stimmt nicht überein“ und „Pflichtfeld fehlt“, und die
  Toleranzvorschläge des Beraters zielen auf die Regel-Engine, die
  entscheidet.
- **Korrekte Zahlen.** KPI-Kacheln respektieren den Unterorganisationsfilter
  und zählen nur Dokumente, die der Drill-down auflisten kann.

### DocNet

- Der Aktivitäten-Feed, das Widget „Recent Activity“ und die
  Missions-Zeitleiste sind übersetzt. Audit-Zusammenfassungen waren in allen
  22 Sprachen englisch.
- Agenten sehen Felder, die der Dokumenttyp definiert, die die Extraktion aber
  leer gelassen hat. Bisher schlossen sie daraus, dass solche Felder nicht
  existieren, und übersprangen vorgeschriebene Aktualisierungen, ohne einen
  Schreibversuch zu unternehmen.

### Sicherheit

- Frontend-Source-Maps werden aus jedem Deploy entfernt. Jede Umgebung lieferte
  sie aus, die Produktion eingeschlossen.

---

## API Service — `12.83.156`

### Lieferantenerkennung und Stammdaten

- Ein Lieferant wird identifiziert, wenn ein Nachschlagefeld eindeutig ist. Bei
  mehreren durchsuchbaren Feldern wurden die Ergebnisse als Vereinigung
  zusammengeführt, sodass ein breiter Namenstreffer mit vier Lieferanten eine
  Steuernummer übertönte, die genau einen traf. Felder, die nichts treffen,
  überstimmen die Felder, die getroffen haben, nicht mehr. Wie die Felder
  zusammenspielen, beschreibt
  [Stammdaten-Einstellungen](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md).
- Ersetzungen durch Stammdaten werden mit ihrer Herkunft aufgezeichnet:
  Datensatz, Konfiguration, Quellfeld, Operator und Trefferart. Der
  Validierungsbildschirm zeigt das an und kann den extrahierten Wert
  wiederherstellen.
- Die Skontobedingung (Cash Discount Term) wird aus dem Lieferanten-BOD
  importiert; bei ERP-synchronisierten Lieferanten war sie leer. Ein Discount
  Term Overwrite, der als vollständiger Code eingegeben wird („143“, „012“,
  „X08“), wird angewendet; bisher wurde nur das Prozent-Präfix ausgewertet.
- Stammdaten-Lookups sind auf 1.000 Zeilen pro Seite begrenzt und pivotieren
  in SQL. Ein Lookup über 19.000 Datensätze brauchte fünf Sekunden pro Aufruf
  und blockierte die API.
- Filter-Eigenschaftsnamen und Datentypen im Stammdaten-Lookup werden als
  SQL-Parameter gebunden. Sie wurden in die Abfrage eingefügt.

### Dokumentenverarbeitung

- Dokumente einer Organisation, die kontinuierlich hochlädt, wurden auf
  Priorität 9 herabgestuft, die die Warteschlange nur bedient, wenn jede
  höhere Priorität leer ist. Die Herabstufung ist jetzt auf 3 begrenzt. Der
  Reconciler, der hängende Dokumente neu einreihen soll, hatte in der
  Produktion keine funktionierenden Zugangsdaten; jetzt hat er sie.
- Ein fertiges, exportiertes Dokument wird nie mit „error“ überschrieben. Ein
  Workflow-Flag, das nie zurückgesetzt wurde, ließ den Retry-Sweeper ein
  erfolgreich exportiertes Dokument einmal pro Minute aufgreifen, bis das
  Wiederholungslimit es mit „error“ stempelte und die Exportfehler-Mail des
  Kunden auslöste — 2 h 17 min nach dem Export.
- Zusammenführen und Anhängen akzeptiert `.PDF`- und `.Pdf`-Dateien.
  Scanner-Ausgaben mit dem Namen `SCAN0001.PDF` wurden mit „Only PDF files are
  allowed.“ abgelehnt.
- Die Cache-Invalidierung durchsucht den Schlüsselraum einmal statt zweimal
  und leert nur die Lookup-Datentypen, die ein BOD geändert hat. Jeder BOD
  löschte bisher den gesamten Lookup-Cache der Organisation und blockierte die
  API, während er die Schlüssel aller durchlief.
- Das Modell-Retraining läuft als Hintergrundaufgabe und kehrt sofort mit einem
  Status zurück, den die UI abfragt.
- Ein Verarbeitungs-Token einer anderen Organisation wird unabhängig von der
  davor liegenden Prüfung der Unterorganisations-Mitgliedschaft abgewiesen.
- Der Benutzer-Sync lässt das Systembenutzer-Flag unangetastet, statt es bei
  jedem Lauf zurückzusetzen.

### Export

- M3-Wareneingangspositionen kombinieren den exportierten Einheitspreis mit
  der Preisbasis der Rechnungsposition selbst. Der Preis reiste mit dem
  Divisor der Bestellposition, und das ERP bepreiste die Position mit dem
  1.000-Fachen des Rechnungsbetrags neu.
- Ein Tabellenexport übersteht eine Position, deren Bestellung entfernt wurde;
  die Position wird ohne Preisbasis exportiert.

### E-Dokumente

- XRechnung-CII-Rechnungen, deren fälliger Zahlbetrag 0,00 ist, weil eine
  Vorauszahlung die Summe ausgleicht, zeigen die Gesamtsumme (BT-112) als
  Gesamtbetrag. Der Kunde sah „Gesamtbetrag 0,00“.
- XRechnung-CII- und Facturae-Dokumente liefern ihre Lieferantenfelder wieder.
  Veraltete Überschreibungen auf Organisationsebene verdeckten das korrekte
  Standard-Mapping, sodass die Lieferantenerkennung nie treffen konnte.
- Der Katalog der Validierungsregeln wird auf dem Server geblättert,
  durchsucht und sortiert, mit Facetten für die Filterleiste.

### Klassifizierung

- Schweizer Dokumente werden anhand ihres Inhalts (CHF-Beträge,
  CHE-USt-Nummern, CH-IBAN) als `de_CH`, `fr_CH` oder `it_CH` klassifiziert.
  Die Sprachregion wurde aus dem Organisationsstandard übernommen, und
  Schweizer Dokumente erhielten `de_DE`.

### Dashboard-Suche

- Eine Operatorsemantik auf Postgres und ClickHouse: `=` exakt, `:` enthält
  mit Wildcards am Rand, `!=` Komplement einschließlich leerer Werte. Auf
  Postgres war `=` bisher ein Präfix-Treffer, sodass `invoice_id=911892112`
  auch 911892112333 lieferte.
- Eine Suche ohne Chip ist eine Teilstring-Suche über alle Felder,
  Geschäftskennungen eingeschlossen. Eine Kennung mit Bindestrich wie
  `2026-003` ist ein einziges Literal, und der Klauseltyp ändert sich nach dem
  fünften Zeichen nicht mehr.
- Der Chip für die Rechnungsnummer ist auf Postgres exakt, wie er es auf dem
  Index bereits war. Führende Nullen, Gleitkommaformen und
  Groß-/Kleinschreibung werden im Freitext und in Chips gleich behandelt.
- Die WebSocket-Suche des Dashboards reicht die Zugangsdaten des Aufrufers an
  den Volltext-Service weiter. Bisher wurde jede Delegation abgewiesen, sodass
  das Dashboard stillschweigend nur Postgres durchsuchte und die Antwort als
  vollständig ausgab.
- Trefferzahl und Trefferliste laufen auf einem Satz von Prädikaten. Die
  Trefferzahl war bisher eine Postgres-Näherung, während die Liste aus dem
  Index kam.
- Die Vektorsuche ist auf das tatsächliche Ergebnisfenster begrenzt und meldet
  die Begrenzung, statt „(50)“ als exakte Gesamtzahl auszugeben.
- Eine Suche, die ohne den Volltextindex lief (Index Minuten im Rückstand,
  Capability-Abfrage fehlgeschlagen, eingeschränkte Feldauflösung), meldet
  ihren Fensterstatus statt „vollständig“.
- Dokumentskripte, die die Volltextsuche aufrufen, authentifizieren sich
  korrekt und zeigen Fehler an, statt ein leeres Ergebnis zurückzugeben.

### Bestellabgleich (In-Process-Matcher)

Für Organisationen, die in der API statt im PO Match Service abgleichen: Eine
korrigierte Bestellnummer wird in demselben Speichervorgang abgeglichen, der
sie korrigiert.

### Analytics

- Touchless: alle Backend-Änderungen hinter dem Web-App-Abschnitt oben,
  einschließlich der von jeder Pipeline-Stufe aufgezeichneten Belege, des
  PO-Match-Trace, der Änderungsvorschläge mit Vorschau, Anwenden und
  Zurücksetzen sowie des Massenstatus in einem Aufruf pro Tick.

---

## PO Match Service — `1.59.34`

- Der Einheitspreis einer Bestellposition wird aus ihrem Nettobetrag
  abgeleitet, nicht aus ihrem Bruttobetrag, und der Bestell-Snapshot eines
  Dokuments leitet seine Einheitspreise zum Abgleichzeitpunkt neu ab.
- Der Service protokolliert, woher jeder Bestellnummern-Kandidat stammt und
  welche Nummern ein Lauf nachgeschlagen hat. Die eigene Rechnungsnummer eines
  Dokuments ist nie ein Bestellkandidat. Ein verworfener Abgleich hinterlässt
  seinen Grund am Dokument für den Bildschirm.
- Der manuelle Abgleich funktioniert für Organisationen, deren Regeln kein
  `is_fallback`-Flag tragen. Benutzer wählten Positionen aus, drückten auf
  Abgleichen, und nichts kam zurück.
- Keine verwaisten Dokumente mehr in „Queue“: Datenbank-Statement-Timeouts,
  Keepalives und ein expliziter Soft-Time-Limit-Handler markieren die Aufgabe
  als fehlgeschlagen, statt sich auf einen Abbruch zu verlassen, der keine
  Spur hinterließ.
- Toleranzänderungen werden pro Abgleichanfrage gelesen, sodass eine gerade
  eben gespeicherte Toleranz vom nächsten Abgleich verwendet wird.
- Der fünfstufige Entscheidungs-Trace wird pro Dokument für Touchless
  gespeichert.

---

## Auth Service — `1.78.27`

- Der Token-Ablauf wird bei Cache-Treffern durchgesetzt. Ein
  zwischengespeicherter Eintrag konnte bis zu neun Stunden nach Ablauf des
  Tokens authentifizieren.
- Die Token-Prüfung schreibt eine unveränderte `org_id` nicht mehr bei jeder
  Anfrage in die Benutzerzeile zurück, was ein UPDATE pro Aufruf erzeugte.
- Ein Speicherleck, das den Autoscaler auf die maximale Replikazahl trieb, ist
  behoben, und der Service läuft wieder mit zwei Workern.
- Das Systembenutzer-Flag kann bei einem bestehenden Benutzer geändert werden,
  wenn kein anderes Mitglied es hält.

---

## Auth Bridge Service — `0.5.7`

- Wenn der Replikationsstream zwischen EU und US abreißt, wird der
  Replikations-Slot an Ort und Stelle wieder angebunden, statt die Bridge neu
  aufzubauen und den vollständigen Start-Abgleich erneut auszuführen, während
  dessen der Slot inaktiv war.

---

## Extraction Service — `1.55.33`

- KI-Tabellenextraktion: Betragsspalten werden als Zahlen mit Beschreibung
  typisiert, und erfundene nicht-numerische Werte in Betragsspalten (ein
  „St.“, das aus der Nachbarzelle in den Einheitspreis kopiert wurde) werden
  verworfen statt gespeichert.
- US-Rechnungen: Gleitkomma-Rauschen unterhalb eines Cents entscheidet nicht
  mehr zwischen Kandidatenpaaren für Netto und Steuer (268,28 + 22,13 verlor
  gegen Netto = Gesamt, Steuer = 0).

---

## Fulltext Service — `1.42.35`

- Der Suchergebnis-Cache ist in jeder Umgebung aktiv; Produktion, Sandbox und
  Stage liefen ohne ihn, seit die aktiven Env-Dateien angelegt wurden. Upload
  und Löschung invalidieren ihn, sodass eine Suche nach einem Upload das neue
  Dokument sieht.
- Eine einfache Suche nach einer bloßen Rechnungsnummer liefert die exakt
  passende Rechnung. Ausgeschriebene Währungswerte, ältere Boolean-Mappings,
  Datumsangaben und Steuer-Flags überstehen den Neuaufbau des schlanken
  Index, und Indexeinträge ohne Felder werden erkannt und aus der Extraktion
  wiederhergestellt.
- Exaktes `=` auf einem dynamischen Textfeld vergleicht nur den gesamten Wert.
  Ein Wildcard auf dem analysierten Pfad ließ `note_field=53173` auf „PO 53173
  / 2024“ treffen.
- Eine bloße Kennung mit Bindestrich wie `2026-003` ist ein einziges Literal,
  kein Haufen von Tokens.
- Lesepfade legen den Index, den sie lesen, nicht mehr selbst an, und jede
  Antwort ohne Treffer trägt einen Fensterstatus und einen Grund.
- Das serviceseitige Limit von 50 der Vektorsuche ist weg.

---

## Docflow Service — `2.10.11`

- Importe erweiterter Workflows sind an die Berechtigung der Organisation
  gebunden, und ein Batch wird geprüft, bevor etwas geschrieben wird. Eine
  Organisation ohne das erweiterte Modul konnte einen erweiterten Workflow
  importieren, den sie dann nicht öffnen konnte.
- Eine Workflow-Umbenennung wird mit dem Speichern übernommen, und
  Umbenennungen von Vorlagen werden gespeichert.

---

## Docnet Service — `1.56.12`

- Die Felderkennung liefert jedes Kopffeld, das das Layout definiert, ob
  befüllt oder nicht, und stimmt mit dem überein, was der Schreibschutz prüft.
  Agenten übersprangen vorgeschriebene Feldaktualisierungen, weil leere Felder
  nicht vorhanden aussahen.
- Identitäten werden unter demselben organisationsbezogenen Schlüssel
  zwischengespeichert, den die API verwendet, sodass die
  API-Schlüssel-Grenze der Organisation über beide Services hinweg hält.

---

## Email Service — `1.41.6`

- Freigegebene Office 365-Postfächer mit mehr als zehn Unterordnern lösen
  jeden Ordner auf. Microsoft Graph liefert Ordner in Zehnerseiten; die 11.
  und alle weiteren Konfigurationen scheiterten bei jedem Abruf mit „unable to
  find the selected Folder“.

---

## FTP Service — `1.32.18`

- Der SFTP-Scheduler startet in jedem Worker-Prozess statt vor dem Fork.
  Regelmäßige SFTP-Importe schlugen stillschweigend mit einem beschädigten
  Scheduler-Zustand fehl, während ein frischer Prozess einwandfrei
  funktionierte.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Nur Build- und Deployment-Änderungen (Aktualisierung des Basis-Images,
CI-Zugangsdaten). Keine Verhaltensänderung.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
