# DocBits Release-Notizen — 21.–25. Juni 2026

_Was dieses Produktions-Upgrade gebracht hat, in verständlicher Sprache. Bei jedem
Service ist die Version angegeben, die jetzt in der Produktion live ist. Nicht
aufgeführte Services hatten in diesem Zeitraum keine für Kunden sichtbaren
Änderungen._

---

## Highlights

- **Intelligentere Dashboard-Suche.** Suchen Sie Dokumente zuverlässig nach Beträgen
  und Zahlen — finden Sie Rechnungen über einem bestimmten Wert oder suchen Sie nach
  der **Anforderungsnummer** — mit Betragsbereichen, die echte Zahlen vergleichen,
  nicht Text. Rechnungs-Untertypen sind über ihre übersetzten Namen durchsuchbar.
- **Zuverlässige E-Mail-Benachrichtigungen.** Benachrichtigungen zu Statusänderungen
  werden jetzt für jeden Status verschickt (keine still verworfenen E-Mails mehr),
  und Eingangsbestätigungen sowie Fehlermeldungen für eingehende Importe sind nun
  korrekt im DocBits-Branding gestaltet, mit empfängerspezifischen Steuerungen.
- **Reibungslosere Anmeldung über Regionen hinweg (EU/US).** Der Regionswechsel ist
  jetzt ein kleines Banner statt einer bildschirmfüllenden Unterbrechung, SSO landet
  in der richtigen Region, und das Angemeldetbleiben über mehrere Browser-Tabs
  hinweg ist zuverlässiger.
- **Berechtigungskorrekturen.** Benutzer erhalten den Zugriff, den ihre Gruppe ihnen
  gewährt — das Öffnen, Bearbeiten, Genehmigen und Neustarten von Dokumenten
  funktioniert jetzt auch dann korrekt, wenn Gruppen und Berechtigungen auf weniger
  gängige Weise konfiguriert sind.
- **Stabilere Dokumentenverarbeitung.** Dokumente, die zuvor nach dem Hochladen
  hängen blieben, werden automatisch wieder aufgenommen, und ein Ansturm von einem
  Kunden bremst die anderen nicht mehr aus.

---

## Web App — live: `10.32.4`

- **Schnellsuche-Sprung (Cmd/Ctrl + K)** direkt zur Einstellung
  **E-Rechnungs-Validierung**.
- **Region & Anmeldung:** Der Regionswechsel wird als dauerhaftes Banner statt als
  blockierender Bildschirm angezeigt; SSO leitet jetzt in die richtige Region weiter
  (EU/US); das Angemeldetbleiben über mehrere Tabs hinweg ist zuverlässiger.
- **Berechtigungen:** Fälle behoben, in denen Benutzer Dokumente nicht
  **genehmigen**, **bearbeiten**, **öffnen** oder **neu starten** konnten, obwohl
  sie die richtigen Gruppenberechtigungen hatten.
- **Einstellungen für eingehende E-Mails:** neue Schalter „Absender benachrichtigen“
  und „Bei Eingang an Absender antworten“.
- **Bedienbarkeit:** Die Warnung vor Duplikat-Dokumenten muss jetzt geschlossen
  werden, bevor man fortfahren kann; das Banner „Backend nicht verfügbar“ erscheint
  nur noch bei tatsächlichen Ausfällen; Aufgabenzähler aktualisieren sich sofort,
  wenn Aufgaben abgeschlossen werden; Korrektur im Dark Mode auf dem Validierungs-
  bildschirm für KI-Tabellen.
- **Performance:** Ein Einfrieren auf dem E-Dokument-Bildschirm während der
  Feldvalidierung und des PO-Abgleichs wurde behoben.
- **Suche nach Rechnungs-Untertypen über ihre übersetzten Namen.**

## API Service — live: `12.41.9`

- **Überarbeitung der Dashboard-Suche:** Anforderungsnummer und Anforderer sind
  jetzt durchsuchbar; Suchen nach Beträgen und Zahlen liefern korrekte Ergebnisse
  (echter numerischer Vergleich); Gesamt-Nettobetrag und berechnete Spalten werden
  korrekt angezeigt.
- **Zuverlässige Status-Benachrichtigungs-E-Mails** für jeden Dokumentstatus, wobei
  Sendefehler nicht mehr verborgen werden.
- **Berechtigungen:** Benutzer ohne Gruppe können ihre eigenen Dokumente öffnen und
  genehmigen; die Dokumentsichtbarkeit für Benutzer ohne Gruppe wurde
  wiederhergestellt.
- **Zuverlässigkeit der Dokumentenverarbeitung:** Dokumente, die im Status „neu“
  feststecken, werden automatisch erneut eingereiht; faire Verarbeitung, damit ein
  großer Ansturm einer Organisation andere nicht aushungert; Selbstheilung bei
  seltenen Problemen mit Datenbanksequenzen.
- **Gescannte PDFs mit defekter Textebene werden an OCR weitergeleitet**, statt
  unzuverlässigen Text zu erzeugen.
- **Genauigkeit von Extraktion & PO:** Lieferantenname wird aus der verknüpften
  Bestellung gefüllt; doppelte Artikelnummer-Spalten entfernt; bessere Behandlung
  von geschützten (nicht umbrechenden) Leerzeichen.
- **Infor ERP / SAP-Export:** Authentifizierung des SFTP-Exports behoben.
- **E-Rechnung:** Verfeinerungen am ZUGFeRD-/E-Dokument-Extraktionspfad.

## Auth Service — live: `1.66.0`

- **Fehlende Organisationszuordnung behoben** für einige Benutzer (leere Org-ID).

## Docflow Service — live: `2.3.4`

- **Die Abkühlzeit für Workflow-Auslöser** ist jetzt pro Umgebung konfigurierbar.

## Email Service — live: `1.35.9`

- **Gebrandete E-Mails:** Eingangsbestätigungen und Fehlermeldungen für eingehende
  Importe verwenden jetzt das echte DocBits-Logo und die echten Farben.
- **Steuerungen pro Organisation:** Bestätigungs-E-Mail bei Eingang, „Absender
  benachrichtigen“ bei Fehlern und Antwort-an-Absender-Optionen.
- **Zuverlässigerer eingehender Import:** Importergebnisse werden korrekt erfasst,
  Teilfehler werden als Fehler gemeldet (nicht als stille Erfolge), und problema-
  tische Zeichen in E-Mail-Texten unterbrechen den Import nicht mehr.
- **EU/US-Routing:** Routing pro Organisation an die richtige regionale API.

## Fulltext Service — live: `1.34.5`

- **Die Suche nach Beträgen und Zahlen** funktioniert jetzt zuverlässig, einschließ-
  lich Tausendertrennzeichen und Betragsbereichen (die Engine hinter der
  überarbeiteten Dashboard-Suche).
- **Stabilere Suchinfrastruktur:** verwaiste Hintergrund-Warteschlangen werden
  bereinigt, sodass sie keine gemeinsam genutzten Ressourcen mehr blockieren.

## PO Match Service — live: `1.54.7`

- **Robusterer Bestellabgleich:** textbasierte Verpackungs-/Packeinheit-Codes
  blockieren einen Abgleich nicht mehr, und der manuelle Positionsabgleich behandelt
  leere Ergebnisse sicher.

---

## Keine für Kunden sichtbaren Änderungen in diesem Zeitraum

Stabil, keine nennenswerten Produktänderungen zwischen dem 21. und 25. Juni: Auto
Accounting (`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`),
FTP (`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
