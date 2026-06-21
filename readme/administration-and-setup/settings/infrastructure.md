# Infrastruktur

Die Seite **Infrastruktur** bietet Administratoren eine aktuelle Übersicht auf einen Blick darüber, wo jeder Teil von DocBits läuft (EU oder US), wie ein Dokument das System durchläuft und ob die Hintergrundverarbeitung fehlerfrei funktioniert. Sie ist schreibgeschützt – hier wird nichts konfiguriert; sie beantwortet die Frage *„Läuft alles, und bleiben meine Daten in meiner Region?"*

> **Zugriff:** Die Infrastruktur ist eine reine Administratorenseite. Öffnen Sie **Einstellungen → Organisation & Zugriff → Infrastruktur**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Infrastructure page with the Topology tab open"><figcaption><p>Die Seite „Infrastruktur", Registerkarte „Topologie"</p></figcaption></figure>

Die Seite ist in drei Registerkarten unterteilt:

| Registerkarte | Beantwortet |
|-----|---------|
| **Topologie** | Wo läuft jede Komponente, und befindet sich alles in meiner Region? |
| **Verarbeitung** | Laufen die Schritte der Dokumentenverarbeitung (OCR, Extraktion, PO-Matching …) und sind sie auf dem aktuellen Stand? |
| **Geplante Aufgaben** | Laufen die wiederkehrenden Hintergrundaufgaben planmäßig? |

## Topologie

Die Registerkarte „Topologie" stellt die gesamte DocBits-Plattform als Diagramm dar, gruppiert in Ebenen – **Edge / Web**, **Core API**, **Import**, **Hintergrunddienste**, **Datenspeicher** und **Authentifizierung**. Jedes Kästchen ist eine Komponente (die Web-App/CDN, das API-Gateway, der OCR-Worker, die Datenbank usw.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Topology diagram with region badges"><figcaption><p>Jede Komponente ist mit der Region gekennzeichnet, in der sie läuft</p></figcaption></figure>

### Regionserkennung

Jede Komponente trägt eine Regionsmarkierung, sodass Sie Ihren Datenspeicherort auf einen Blick bestätigen können:

| Markierung | Bedeutung |
|-------|---------|
| **EU ✓** / **US ✓** | Die Komponente läuft in der Region Ihrer Organisation. |
| **SHARED** | Eine globale Komponente (z. B. das CDN) ohne einzelne Region – das ist normal und kein Problem. |
| **Region mismatch** | Die Komponente läuft in einer *anderen* Region als Ihre Organisation. Sie wird hervorgehoben, damit Sie sie beim Support melden können. |

Das Banner oben fasst das Ergebnis zusammen: **„Alle Komponenten laufen in Ihrer Region (EU)"**, wenn alles übereinstimmt, oder eine Warnung, falls eine kritische Komponente regionsübergreifend läuft.

### Architektur vs. Prozessablauf

Verwenden Sie den Umschalter oberhalb des Diagramms, um die Ansicht zu wechseln:

- **Architektur** – die statische Karte aller Komponenten und ihrer Verbindungen.
- **Prozessablauf** – animiert den Weg eines Dokuments durch das System Schritt für Schritt, sodass Sie die Reihenfolge sehen, in der die Komponenten beteiligt sind.

Die Anzeige **● live** zeigt, dass die Zustandsinformationen im Diagramm den aktuellen Zustand des Systems widerspiegeln.

### Optionale Module

Komponenten, die zu einem optionalen Modul gehören (Volltextsuche, DocFlow, Auto-Accounting, DocNet, PO-Matching), zeigen eine Markierung **aktiviert** oder **deaktiviert** an. Wenn Sie auf ein deaktiviertes Modul klicken, gelangen Sie direkt zu der Seite, auf der Sie es einschalten können – **Einstellungen → Modul** für die meisten Module, oder **Dokumenttypen** für das PO-Matching (das pro Dokumenttyp aktiviert wird).

## Verarbeitung

Die Registerkarte „Verarbeitung" zeigt die Pipeline der Dokumentenverarbeitung für **Ihre Organisation** – wann jeder Schritt zuletzt ausgeführt wurde und ob die Arbeit fließt oder sich staut.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Processing tasks table with status badges"><figcaption><p>Verarbeitungsstatus je Schritt für Ihre Organisation</p></figcaption></figure>

| Spalte | Beschreibung |
|--------|-------------|
| **Prozess** | Der Verarbeitungsschritt – Dokumentenverarbeitung, OCR, TR-OCR, Barcode-Split, Barcode-Extraktion, Extraktion, PO-Matching. |
| **Letzte Ausführung** | Wie lange es her ist, dass der Schritt zuletzt ausgeführt wurde. Bewegen Sie den Mauszeiger darüber, um den genauen Zeitstempel zu sehen. *„Nie ausgeführt"* bedeutet, dass noch kein Dokument diesen Schritt erreicht hat. |
| **Status** | Eine Ampelmarkierung (siehe unten). |

Statusmarkierungen:

| Markierung | Bedeutung |
|-------|---------|
| **OK** (grün) | Keine aktuellen Fehler und nichts in Wartestellung – der Schritt funktioniert fehlerfrei. |
| **In Bearbeitung (N)** (gelb) | `N` Dokumente werden derzeit von diesem Schritt verarbeitet. |
| **Fehler (N)** (rot) | `N` Dokumente sind bei diesem Schritt kürzlich fehlgeschlagen. |

Fehler und *In Bearbeitung* sind unabhängige Signale, sodass ein Schritt beide Markierungen gleichzeitig anzeigen kann – Sie sehen einen Fehler also auch dann, während andere Arbeit läuft. Verwenden Sie **Aktualisieren** (oben rechts), um die neuesten Zahlen abzurufen.

## Geplante Aufgaben

Die Registerkarte „Geplante Aufgaben" listet die wiederkehrenden Hintergrundaufgaben auf, die DocBits am Laufen halten (Cache-Aktualisierungen, Statuswarnungen, Dokument-Timeouts, ausgehende Synchronisierungen und mehr), und bestätigt, dass jede davon pünktlich ausgelöst wird.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Scheduled tasks table"><figcaption><p>Wiederkehrende Hintergrundaufgaben und ihr Zeitplanstatus</p></figcaption></figure>

| Spalte | Beschreibung |
|--------|-------------|
| **Aufgabe** | Der Name der geplanten Aufgabe. |
| **Letzte Ausführung** | Wie lange es her ist, dass sie zuletzt ausgeführt wurde. Bewegen Sie den Mauszeiger darüber, um den genauen Zeitstempel zu sehen; *„Nie ausgeführt"* bedeutet, dass sie noch nicht ausgelöst wurde. |
| **Status** | Zeitplanzustand (siehe unten). |

Statuswerte:

| Markierung | Bedeutung |
|-------|---------|
| **Planmäßig** (grün) | Die Aufgabe läuft in ihrem erwarteten Intervall. |
| **Verzögert** (rot) | Die Aufgabe ist nicht zum erwarteten Zeitpunkt ausgeführt worden – sollte untersucht oder beim Support gemeldet werden. |
| **Unbekannt** (grau) | Der Zeitplanstatus konnte nicht ermittelt werden. |

Verwenden Sie **Aktualisieren**, um den Zeitplanstatus bei Bedarf erneut zu überprüfen.
