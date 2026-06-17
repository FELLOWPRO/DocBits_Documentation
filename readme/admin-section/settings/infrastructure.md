# Infrastruktur

Die Seite **Infrastruktur** bietet Administratoren einen aktuellen Überblick darüber, wo jeder Teil von DocBits läuft (EU oder US), wie ein Dokument das System durchläuft und ob die Hintergrundverarbeitung fehlerfrei arbeitet. Die Seite ist rein lesend — hier wird nichts konfiguriert; sie beantwortet die Frage: *„Läuft alles, und bleiben meine Daten in meiner Region?"*

> **Zugriff:** Infrastruktur ist eine reine Administrator-Seite. Öffnen Sie **Einstellungen → Organisation & Zugriff → Infrastruktur**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Infrastruktur-Seite mit geöffnetem Topologie-Tab"><figcaption><p>Die Infrastruktur-Seite, Tab Topologie</p></figcaption></figure>

Die Seite ist in drei Tabs unterteilt:

| Tab | Beantwortet |
|-----|-------------|
| **Topologie** | Wo läuft jede Komponente, und liegt alles in meiner Region? |
| **Verarbeitung** | Laufen die Verarbeitungsschritte (OCR, Extraktion, PO-Abgleich …) und sind sie aktuell? |
| **Geplante Aufgaben** | Laufen die wiederkehrenden Hintergrundaufgaben planmäßig? |

## Topologie

Der Topologie-Tab stellt die gesamte DocBits-Plattform als Diagramm dar, gegliedert in Schichten — **Edge / Web**, **Core API**, **Import**, **Hintergrunddienste**, **Datenspeicher** und **Authentifizierung**. Jedes Feld ist eine Komponente (Web-App/CDN, API-Gateway, OCR-Worker, Datenbank usw.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Topologie-Diagramm mit Regions-Badges"><figcaption><p>Jede Komponente ist mit der Region gekennzeichnet, in der sie läuft</p></figcaption></figure>

### Regions-Transparenz

Jede Komponente trägt ein Regions-Badge, sodass Sie Ihren Datenstandort auf einen Blick bestätigen können:

| Badge | Bedeutung |
|-------|-----------|
| **EU ✓** / **US ✓** | Die Komponente läuft in der Region Ihrer Organisation. |
| **SHARED** | Eine globale Komponente (z. B. das CDN) ohne feste Region — das ist erwartet und kein Problem. |
| **Regions-Abweichung** | Die Komponente läuft in einer *anderen* Region als Ihre Organisation. Sie wird hervorgehoben, damit Sie dies mit dem Support klären können. |

Das Banner oben fasst das Ergebnis zusammen: **„Alle Komponenten laufen in Ihrer Region (EU)"**, wenn alles übereinstimmt, oder eine Warnung, falls eine kritische Komponente regionsübergreifend läuft.

### Architektur vs. Prozess abspielen

Mit dem Umschalter über dem Diagramm wechseln Sie die Ansicht:

- **Architektur** — die statische Karte aller Komponenten und ihrer Verbindungen.
- **Prozess abspielen** — animiert den Weg eines Dokuments durch das System Schritt für Schritt, sodass Sie die Reihenfolge der beteiligten Komponenten sehen.

Die Anzeige **● live** signalisiert, dass die Gesundheitsinformationen im Diagramm den aktuellen Systemzustand widerspiegeln.

### Optionale Module

Komponenten, die zu einem optionalen Modul gehören (Volltextsuche, DocFlow, Auto-Accounting, DocNet, PO-Abgleich), zeigen ein Badge **aktiviert** oder **deaktiviert**. Ein Klick auf ein deaktiviertes Modul führt Sie direkt zu der Seite, auf der Sie es einschalten können — **Einstellungen → Modul** für die meisten Module bzw. **Dokumenttypen** für den PO-Abgleich (der je Dokumenttyp aktiviert wird).

## Verarbeitung

Der Verarbeitungs-Tab zeigt die Dokumentenverarbeitungs-Pipeline für **Ihre Organisation** — wann jeder Schritt zuletzt lief und ob Arbeit fließt oder sich staut.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Verarbeitungstabelle mit Status-Badges"><figcaption><p>Verarbeitungsstatus je Schritt für Ihre Organisation</p></figcaption></figure>

| Spalte | Beschreibung |
|--------|--------------|
| **Prozess** | Der Verarbeitungsschritt — Dokumentenverarbeitung, OCR, TR-OCR, Barcode-Split, Barcode-Extraktion, Extraktion, PO-Abgleich. |
| **Letzter Lauf** | Wie lange der Schritt zuletzt lief. Für den genauen Zeitstempel mit der Maus darüberfahren. *„Nie gelaufen"* bedeutet, dass noch kein Dokument diesen Schritt erreicht hat. |
| **Status** | Ein Ampel-Badge (siehe unten). |

Status-Badges:

| Badge | Bedeutung |
|-------|-----------|
| **OK** (grün) | Keine aktuellen Fehler und nichts in Wartestellung — der Schritt ist gesund. |
| **In Bearbeitung (N)** (gelb) | `N` Dokumente werden derzeit von diesem Schritt verarbeitet. |
| **Fehler (N)** (rot) | `N` Dokumente sind kürzlich an diesem Schritt fehlgeschlagen. |

Fehler und *In Bearbeitung* sind unabhängige Signale, daher kann ein Schritt beide Badges gleichzeitig zeigen — so sehen Sie einen Fehler auch dann, wenn andere Arbeit noch läuft. Über **Aktualisieren** (oben rechts) holen Sie die neuesten Werte.

## Geplante Aufgaben

Der Tab Geplante Aufgaben listet die wiederkehrenden Hintergrundaufgaben auf, die DocBits am Laufen halten (Cache-Aktualisierungen, Status-Benachrichtigungen, Dokument-Timeouts, ausgehende Synchronisationen u. v. m.), und bestätigt, dass jede pünktlich ausgeführt wird.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabelle der geplanten Aufgaben"><figcaption><p>Wiederkehrende Hintergrundaufgaben und ihr Zeitplanstatus</p></figcaption></figure>

| Spalte | Beschreibung |
|--------|--------------|
| **Aufgabe** | Der Name der geplanten Aufgabe. |
| **Letzter Lauf** | Wie lange sie zuletzt lief. Für den genauen Zeitstempel mit der Maus darüberfahren; *„Nie gelaufen"* bedeutet, dass sie noch nicht ausgeführt wurde. |
| **Status** | Zeitplan-Status (siehe unten). |

Status-Werte:

| Badge | Bedeutung |
|-------|-----------|
| **Im Zeitplan** (grün) | Die Aufgabe läuft im erwarteten Intervall. |
| **Verzögert** (rot) | Die Aufgabe wurde nicht wie erwartet ausgeführt — sollte geprüft oder mit dem Support geklärt werden. |
| **Unbekannt** (grau) | Der Zeitplan-Status konnte nicht ermittelt werden. |

Mit **Aktualisieren** prüfen Sie den Zeitplan-Status bei Bedarf erneut.
