# DocBits Release-Notizen — 30. Juni – 3. Juli 2026

_Was dieses Produktions-Upgrade gebracht hat, in verständlicher Sprache. Bei jedem
Service ist die Version angegeben, die jetzt in der Produktion live ist. Nicht
aufgeführte Services hatten in diesem Zeitraum keine für Kunden sichtbaren
Änderungen._

---

## Highlights

- **KI-Chat auf den Aktivitätsprotokollen.** Ein neues KI-Chat-Panel auf der Seite
  Aktivitätsprotokolle lässt Sie direkt Fragen zur Protokollaktivität stellen, ohne
  sich durch Rohdaten wühlen zu müssen.
- **Nachverfolgung ausgehender E-Mail-Importe.** Das Importprotokoll erfasst jetzt
  ausgehende neben eingehender Post, mit Schnellfilter-Chips für Fehler / Eingehend /
  Ausgehend — fehlschlagende Postfächer werden nach wiederholten Fehlschlägen
  automatisch deaktiviert, Admins können per E-Mail über einen Importfehler
  benachrichtigt werden, und Wiederholungsversuche laufen jetzt bis zu 15-mal über
  etwa 5 Stunden, bevor aufgegeben wird.
- **Klarere Fehlermeldungen beim E-Mail-Import.** Anmeldefehler zeigen jetzt den
  tatsächlichen zugrunde liegenden Grund, mit eigenen Meldungen für ein ungültiges
  Zertifikat oder ein falsches Gmail-App-Passwort.
- **Anmelde-Schleife behoben.** Manche Benutzer konnten während der
  Token-Aktualisierung in einer wiederholten Anmelde-Schleife hängen bleiben — dies
  ist behoben.
- **Stabilere Dokumentenverarbeitung.** Ein Absturz bei der Datenextraktion durch
  nicht gerundete Koordinatenwerte wurde behoben, das Lesen von Barcodes wiederholt
  jetzt behebbare Fehlschläge, statt stillschweigend aufzugeben, und ein seltener
  Fall, in dem ein Dokument gleichzeitig doppelt exportiert werden konnte, ist
  behoben.
- **Verbesserungen am Validierungsbildschirm.** Sie können jetzt weiter in Dokumente
  hineinzoomen, Felder werden nicht mehr von Skripten geleert, wenn sich ihr Wert
  tatsächlich nicht geändert hat, und das Dashboard merkt sich Ihre Seitenposition,
  wenn Sie zurücknavigieren.

---

## Web App — live: `10.35.7`

- **KI-Chat-Panel** zur Seite Aktivitätsprotokolle hinzugefügt (#15512).
- **Importprotokoll:** neue Schnellfilter-Chips für Fehler / Eingehend / Ausgehend;
  Schalter und Feld für Empfänger von Fehlerbenachrichtigungen bei den Einstellungen
  für eingehende E-Mails.
- **Validierungsbildschirm:** Der Dokumentenzoom geht jetzt über die bisherige
  Standardgröße hinaus; von Validierungsskripten geleerte Felder behalten jetzt
  korrekt ihren Wert, wenn das Skript denselben Wert zurückgibt.
- **Dashboard:** Die Seitenposition bleibt beim Zurücknavigieren zur Tabelle
  erhalten; der Anfasser zur Spaltenbreitenänderung ragt nicht mehr über den
  Tabellenkopf hinaus.
- **Bildschirm Automatische Buchhaltung:** ein Validierungsfehler behoben.
- **DocBits-Aufgaben:** ein Berechtigungsproblem behoben.
- **Watchdog-Protokolle:** einen Zeitraumfilter und eine anpassbare Auswahl für
  Zeilen pro Seite hinzugefügt.
- **Korrekturen:** ein Diagrammfehler („Element nicht gefunden“) auf der
  Boards-Seite; ein defekter Link zum Exportlöschen auf den Aktivitätsprotokollen;
  Layout-Korrekturen auf dem Layout-Builder-Bildschirm; eine fehlende Übersetzung
  beim Zeitraumfilter der Aktivitätsprotokolle.
- **Automatische Aktualisierung:** weitere Härtung des automatischen
  App-Update-Mechanismus (schnellere Startbereinigung, zuverlässigere
  Versionserkennung, Cache-Bereinigung vor einem Wiederherstellungs-Reload).

## API Service — live: `12.48.1`

- **Schnelleres Laden von Dokumentskripten:** Validierungsskripte werden jetzt
  serverseitig zwischengespeichert (6-Stunden-Cache), statt jedes Mal neu abgerufen
  zu werden.
- **Präzisere Betrags-Konfidenz:** Die Konfidenzbewertung berücksichtigt jetzt
  Dokumente, die unterschiedliche Konventionen für das Dezimaltrennzeichen
  verwenden.
- **Zuverlässigkeit:** Die Dokumentenvalidierung führt immer die einzige aktive
  Skriptversion aus, und welche Version gelaufen ist, wird jetzt protokolliert; ein
  seltener Fall, in dem ein Dokument gleichzeitig doppelt exportiert werden konnte,
  ist behoben; lieferantenspezifische Extraktionsregeln greifen nach einer
  erzwungenen erneuten OCR wieder korrekt.
- **E-Mail-Import:** Backend-Unterstützung für die Protokollierung ausgehender
  E-Mails und für Fehlerbenachrichtigungs-E-Mails hinzugefügt (siehe Email Service
  unten).

## Auth Service — live: `1.68.5`

- **Anmelde-Schleife behoben**, in der manche Benutzer während der Aktualisierung
  ihres Sitzungstokens hängen bleiben konnten.
- **Schnellere Bildschirme für Organisationsadministratoren:** Benutzer- und
  Abonnementdaten werden jetzt gebündelt statt einzeln geladen.
- **Seltenen Datenbankkonflikt behoben**, der beim Verknüpfen eines Benutzers mit
  einer Organisation auftreten konnte.

## Email Service — live: `1.37.4`

- **Das Importprotokoll erfasst jetzt auch ausgehende Post** neben eingehender, mit
  einem Filter, der nur eingehende, ausgehende oder fehlgeschlagene Importe
  anzeigt.
- **Fehlschlagende Postfächer werden jetzt nach wiederholten Fehlschlägen
  automatisch deaktiviert**, und Admins können per E-Mail benachrichtigt werden,
  wenn ein Import fehlschlägt; Wiederholungsversuche laufen jetzt bis zu 15-mal über
  etwa 5 Stunden, bevor aufgegeben wird.
- **Klarere Meldungen bei Anmeldefehlern:** zeigt den tatsächlichen zugrunde
  liegenden Grund, eine eigene Meldung für ein ungültiges Zertifikat und eine
  spezifische Meldung für ein falsches Gmail-App-Passwort.
- **Fehlerhafte Weiterleitung bei eingehender Post behoben**, die Serveradressen
  für Konten in der EU-Region fälschlich umschrieb.
- Widerstandsfähiger gegenüber kurzen Redis-Verbindungsabbrüchen.

## Extraction Service — live: `1.49.0`

- **Absturz bei der Extraktion behoben**, verursacht durch nicht gerundete
  Koordinatenwerte.
- **Präzisere Betrags-Konfidenz** für Dokumente mit gemischten
  Dezimaltrennzeichen-Formaten; kleine Rundungsdifferenzen bei Steuersummen
  blockieren einen Abgleich nicht mehr.

## Docflow Service — live: `2.4.2`

- **Authentifizierung für erweiterte (Celery-basierte) Workflows überarbeitet**,
  mit Absicherungen, sodass eine fehlgeschlagene Authentifizierungsprüfung einen
  Workflow-Lauf nicht mehr zum Absturz bringen kann.
- **Klarere Antwort**, wenn ein Workflow-Schritt gegen einen nicht mehr
  existierenden Workflow ausgeführt werden soll.

## Barcode Service — live: `1.15.7`

- **Das Lesen von Barcodes wiederholt jetzt automatisch** behebbare Fehlschläge,
  statt stillschweigend aufzugeben.

## OCR Service — live: `1.7.3`

- **OCR-Fehlschlag behoben**, verursacht durch ein Problem bei der
  Redis-Hostnamensauflösung.
- Health-Check-bedingte Redis-Verbindungsabbrüche werden nicht mehr als Fehler
  protokolliert, was falsche Alarme reduziert.

## PO Match Service — live: `1.55.8`

- **Behoben, dass Notizen nicht bei PO-Match-Datensätzen angezeigt wurden.**

---

## Keine für Kunden sichtbaren Änderungen in diesem Zeitraum

Stabil, keine nennenswerten Produktänderungen zwischen dem 30. Juni und 3. Juli:
Auto Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`),
Operator (`1.39.5`). Auto Accounting erhielt nur interne
Bereitstellungskonfigurations-Wartung. Der Ideas Service konnte in diesem Zeitraum
für eine Versionsprüfung nicht erreicht werden.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
