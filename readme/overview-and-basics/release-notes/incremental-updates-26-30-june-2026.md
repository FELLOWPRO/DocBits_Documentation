# DocBits Release-Notizen — 26.–30. Juni 2026

_Was dieses Produktions-Upgrade gebracht hat, in verständlicher Sprache. Bei jedem
Service ist die Version angegeben, die jetzt in der Produktion live ist. Nicht
aufgeführte Services hatten in diesem Zeitraum keine für Kunden sichtbaren
Änderungen._

---

## Highlights

- **Eine Verbindung für KI-Assistenten ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Ein einziges, einheitliches
  Gateway bedient jetzt alle DocBits-Tools — einschließlich DocFlow — über die
  Haupt-API, sodass KI-Assistenten (Claude, Gemini CLI, Codex) über einen
  zuverlässigen Endpunkt statt über mehrere verbunden sind.
- **Intelligentere mehrsprachige Dashboard-Suche.** Suchoperatoren (**AND / OR**)
  erscheinen jetzt in Ihrer Sprache mit Farbhervorhebung, Rechnungs-Untertypen
  bieten ein Wert-Dropdown, und Meldungen zur Suchsyntax sind lokalisiert — mit
  durchgehend reibungsloserer Tastaturbedienung.
- **Reibungslosere Genehmigungen & Berechtigungen.** Eine Genehmigung wird nicht
  mehr ausgelöst, wenn die Packeinheit aus einer Auftragsbestätigung leer ist,
  normale Benutzer können nach der Migration der Zugriffssteuerung wieder
  Kalkulationselemente genehmigen, und Berechtigungen auf Dokumentebene werden
  korrekt angewendet, selbst wenn eine Tabellenspalte bereits existiert.
- **Die App aktualisiert sich selbst.** Wenn eine neue Version veröffentlicht wird,
  aktualisiert sich DocBits jetzt automatisch, statt Sie mit einem
  „Jetzt aktualisieren“-Popup zu unterbrechen.
- **Robusterer Bestellabgleich.** Werttransformationen für Spalten,
  Absturzsicherungen für Positionen ohne Preis oder Menge und automatische
  Wiederholungen bei abgebrochenen Datenbankverbindungen machen den Abgleich
  stabiler.
- **Weniger Fehler auf ganzer Linie.** Viele seltene Serverfehler bei Dashboards,
  Lieferantenrechnungen, PO-Datensätzen und OCR-Jobs wurden aufgespürt und behoben.

---

## Web App — live: `10.34.4`

- **Dashboard-Schnellsuche:** lokalisierte **AND / OR**-Operatoren (de/fr) mit
  farbiger Syntaxhervorhebung; Wert-Dropdown für Rechnungs-Untertypen; lokalisierte
  Fehlermeldungen zur Suchsyntax; reibungslosere Tastaturbedienung; die Warnung
  „Volltext erforderlich“ wird jetzt inline dargestellt, sodass das Layout nicht
  mehr springt.
- **Genehmigungen & Berechtigungen:** behoben, dass eine Genehmigung fälschlich
  ausgelöst wurde, wenn die Packeinheit aus einer Auftragsbestätigung leer ist;
  normale Benutzer können nach der Migration der Zugriffssteuerung wieder
  Kalkulationselemente genehmigen; Berechtigungen auf Dokumentebene werden jetzt
  angewendet, wenn eine Tabellenspalte bereits existiert.
- **Automatische Aktualisierung:** Die App aktualisiert sich bei einer neuen Version
  automatisch, statt ein „Jetzt aktualisieren“-Popup anzuzeigen; der alte
  Versionsinfo-Dialog wurde entfernt.
- **Einstellungen für eingehende E-Mails:** neuer Schalter und neues Feld für
  Empfänger von Fehlerbenachrichtigungen; das Importprotokoll zeigt jetzt ausgehende
  Aktivität und den Fehlergrund; die Eingangsadresse lässt sich zuverlässig
  kopieren.
- **Dokumentenaufteilung:** Der Bildschirm zur Dokumentenaufteilung lässt sich jetzt
  scrollen.
- **Dark Mode:** Korrekturen für die Tabellenextraktion, den Aufgabenzähler und die
  Markierungen für geschlossene Dokumente auf dem Dashboard.
- **Bedienbarkeit & Stabilität:** Korrekturen an der Export-UI des Dashboards;
  fixierte Tabellenüberschriften scheinen nicht mehr durch Dialoge hindurch; das
  DocNet-Dashboard stürzt bei einer fehlgeschlagenen Statistikanfrage nicht mehr ab;
  Feldskripte setzen geleerte Felder nicht mehr auf ihre alten Werte zurück;
  Korrekturen an den Kontrollkästchen und am Layout der PO-Einstellungen; Korrekturen
  der Anzeige der Klassifizierungsliste.
- **Lieferanten:** Lieferantenorganisationen können sich jetzt per Magic Link
  registrieren.

## API Service — live: `12.46.8`

- **DocBits-MCP-Gateway:** ein einheitliches Gateway leitet jetzt DocFlow-Tools über
  die Haupt-API weiter, sodass KI-Assistenten jedes DocBits-Tool über einen Endpunkt
  erreichen; der MCP-Endpunkt wird ohne eine Weiterleitung bereitgestellt, die
  Verbindungen unterbrechen könnte.
- **Buchhaltung:** Kostenstellen-Validierung für die Buchhaltungs-ID hinzugefügt.
- **OCR-Routing:** Dokumente werden für eine vollständige erneute OCR gesendet, wenn
  der Lieferanten-E-Text deaktiviert ist, sodass der Text zuverlässig bleibt.
- **Infor ERP / SAP:** Zusätzliche Gebühren werden korrekt weitergeleitet, wenn das
  ERP-System die Gebühr bereits mit dem Betrag null führt.
- **Zuverlässigkeit (weniger Serverfehler):** abgehärtete Abfragen für Dashboard,
  Lieferantenrechnung, PO-Datensatz und Task-Manager, sodass sie keine seltenen
  500-Fehler mehr zurückgeben; widerstandsfähigere Synchronisierung des
  Organisations-Caches und Bereinigung gespeicherter Dateien.
- **Übersichtlichere Dashboard-Filter:** das überflüssige Filterfeld für die
  Rechnungsnummer entfernt; PO-abgeglichene Menge korrigiert.
- **Entwickler-API-Dokumentation:** Die Swagger-UI bietet jetzt ein Spec-Dropdown
  (OpenAPI 3.0 sowie die Infor-Swagger-2.0-Ansicht) im DocBits-Branding.

## Auth Service — live: `1.68.0`

- **Schnellere Abmeldung / Token-Widerruf:** Der Massen-Token-Widerruf läuft nicht
  mehr minutenlang und bricht die Verbindung nicht mehr ab.
- **E-Mails zum Festlegen des Passworts korrigiert**, sodass sie korrekt dargestellt
  werden.
- **Lieferanten:** Lieferantenorganisationen können sich per Magic Link registrieren.
- **Anmeldungsstabilität:** Ein Mitglied wird bei einem vorübergehenden Fehlschlag
  der Organisationssuche nicht mehr ausgesperrt, und eine ungültige Organisations-ID
  gibt jetzt eine saubere Meldung statt eines Fehlers zurück.

## Docflow Service — live: `2.4.1`

- **Zuverlässiges KI-Gateway:** Hänger und Timeouts am DocFlow-MCP-Endpunkt behoben
  (Handshake, Client-Verbindungsabbrüche, doppelte Antworten) — die DocFlow-Seite
  des einheitlichen DocBits-MCP-Gateways.

## OCR Service — live: `1.7.1`

- **Stabilere OCR-Verarbeitung:** Hintergrund-Antwortwarteschlangen laufen
  automatisch ab, und vorübergehende Verbindungsfehler werden erneut versucht, sodass
  weniger OCR-Jobs hängen bleiben.

## PO Match Service — live: `1.55.7`

- **Werttransformationen** werden jetzt beim Regelabgleich auf die Spalten
  Artikel-ID, Einheitencode und statischer Wert angewendet.
- **Absturzsicherungen:** Eine Position ohne Preis oder Menge, eine ungewöhnliche
  Kombination gewichteter Schlüssel oder eine unmögliche Division führen nicht mehr
  zum Absturz des Abgleichs.
- **Zuverlässigkeit:** Datenbankschreibvorgänge werden bei abgebrochenen oder
  SSL-geschlossenen Verbindungen automatisch wiederholt.
- **Infor ERP / SAP:** Zusätzliche Gebühren werden korrekt weitergeleitet, wenn das
  ERP-System die Gebühr mit dem Betrag null führt.

## Fulltext Service — live: `1.35.6`

- **Schnellere Neuindexierung:** Alle Synchronisierungsphasen werden jetzt
  aufgefächert, sodass Autoscaling greift; das behebt die langsame serielle
  Neuindexierung und ein bei 0 % feststeckendes Fortschritts-Widget.
- **Stabilere Statistiken:** Regionsübergreifende Anfragen für Dokumentstatistiken
  sind begrenzt, sodass sie keine Timeouts mehr verursachen.

---

## Keine für Kunden sichtbaren Änderungen in diesem Zeitraum

Stabil, keine nennenswerten Produktänderungen zwischen dem 26. und 30. Juni: Auto
Accounting (`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`),
Extraction (`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting und FTP
erhielten nur interne Wartung.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
