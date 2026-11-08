# Infrastruktur

Die Seite **Infrastructure** gibt Administratoren eine aktuelle Übersicht darüber, wo jeder Teil der Plattform läuft (EU oder US) und ob die Verarbeitung fehlerfrei läuft. Sie ist schreibgeschützt, hier wird also nichts konfiguriert.

> **Access:** Infrastructure ist eine reine Administratorenseite. Öffnen Sie **Settings → Organization & Access → Infrastructure**.

Die Seite hat drei Tabs. Jeder lädt seine Daten beim ersten Öffnen, ein Hin- und Herwechseln ruft also nicht alles neu ab.

| Tab | Answers |
|-----|---------|
| **Topology** | Wo läuft jede Komponente, und wie durchläuft ein Dokument DocBits? |
| **Processing** | Laufen die Schritte der Dokumentenverarbeitung, und staut sich die Arbeit? |
| **Scheduled Tasks** | Werden die wiederkehrenden Hintergrundaufgaben planmäßig ausgelöst? |

## Topology

**Topology** öffnet standardmäßig. Die Ansicht zeigt die Plattform in zwei Darstellungen: **Architecture** und **Process**. Über den Umschalter oberhalb des Diagramms wechseln Sie zwischen ihnen; die Anzeige daneben lautet **live**, solange die Ansicht ihren Zustand streamt.

Ein Banner oberhalb des Diagramms fasst die Regionsprüfung zusammen:

* **Green**: alle Komponenten laufen in der Region Ihrer Organisation, und das Banner nennt diese Region (zum Beispiel **EU**).
* **Red**: eine als kritisch gekennzeichnete Komponente läuft außerhalb der Region Ihrer Organisation.
* **Amber**: der Hinweis nennt Komponenten, die in einer anderen Region liegen, obwohl die Gesamtprüfung besteht. Das ist eine Regionsabweichung, kein Fehler.

### Architekturansicht

Die Architekturansicht zeichnet die Plattform als Spuren von Komponentenkarten, zum Beispiel Edge / Web, Core API, Import, Background Services und Modules. Pfeile zeigen die Verbindungen zwischen den Karten.

Jede Karte zeigt den Komponentennamen, eine Regionsmarkierung und bei kritischen Komponenten einen Statuspunkt, der grün wird, wenn die Komponente antwortet, und ihre Latenz in Millisekunden anzeigt, wenn ein Wert gemeldet wird.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | Die Komponente läuft in der Region Ihrer Organisation. |
| **SHARED** | Eine globale Komponente wie das CDN, die keiner einzelnen Region zugeordnet ist. Das ist erwartet. |
| **EU ⓘ** / **US ⓘ** | Die Komponente läuft in einer anderen Region und wird als Hinweis gemeldet. |
| **EU ⚠** / **US ⚠** | Die Komponente läuft in einer anderen Region und wird als Fehler gemeldet. Melden Sie dies dem Support. |
| Graue Markierung, kein Zeichen | Die Region dieser Komponente ist nicht bekannt. |

### Prozessansicht

Die Prozessansicht animiert ein einzelnes Dokument durch die Pipeline: die Eingangsquellen **Email**, **FTP** und **Web** laufen auf **API** zusammen und durchlaufen dann **OCR**, **Extraction**, **PO matching**, **Auto Accounting** und **Export**. Jede Stufe ist mit einem Balken für die Datenspeicher verbunden, mit **Postgres** und Dateispeicher. Eine Bildunterschrift nennt den Schritt, der gerade animiert wird, und die Wiedergabetaste pausiert die Animation oder setzt sie fort.

PO matching und Auto Accounting sind optional. Wenn eines davon für Ihre Organisation abgeschaltet ist, ist die zugehörige Stufe ausgegraut und die Animation überspringt sie.

### Optionale Module

Optionale Module (Full-Text Search, DocFlow, Auto-Accounting, DocNet und PO Matching) tragen auf ihrer Karte eine Markierung **active** oder **inactive**. Ein deaktiviertes Modul bietet eine Schaltfläche **Activate**, die Sie auf die Seite führt, auf der Sie es einschalten: die Module-Einstellungen für die meisten Module oder **Document Types** für PO Matching, das je Dokumenttyp aktiviert wird.

## Processing

Der Tab **Processing** listet die Schritte der Dokumentenverarbeitung für Ihre Organisation auf und sagt Ihnen, ob Arbeit fließt oder sich staut.

| Column | Description |
|--------|-------------|
| **Process** | Der Verarbeitungsschritt: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction und PO Match. |
| **Last run** | Wie lange die letzte Ausführung zurückliegt. Fahren Sie mit der Maus darüber, um den genauen Zeitstempel zu sehen. **Never run** bedeutet, dass noch kein Dokument diesen Schritt erreicht hat. |
| **Status** | Eine oder mehrere Markierungen (siehe unten). |

Die Statusmarkierungen sind unabhängige Signale:

* Rote Markierung **Errors (N)**: `N` Dokumente sind bei diesem Schritt kürzlich fehlgeschlagen.
* Gelbe Markierung mit einer Anzahl: `N` Dokumente werden gerade von diesem Schritt verarbeitet.
* Grüne Markierung **OK**: keine aktuellen Fehler und nichts in der Warteschlange.

Da Fehler und laufende Arbeit getrennt gezählt werden, kann ein Schritt beides gleichzeitig zeigen; ein Fehler bleibt also sichtbar, während andere Dokumente noch laufen.

## Scheduled Tasks

Der Tab **Scheduled Tasks** listet die wiederkehrenden Hintergrundaufgaben auf, die DocBits am Laufen halten, zum Beispiel Cache-Aktualisierungen, Statuswarnungen, Dokument-Timeouts und ausgehende Synchronisierungen. Jede Zeile zeigt, ob die Aufgabe pünktlich ausgelöst wird.

| Column | Description |
|--------|-------------|
| **Task** | Der Name der geplanten Aufgabe, wobei Trennzeichen durch Leerzeichen ersetzt sind. |
| **Last run** | Wie lange die letzte Ausführung zurückliegt. Fahren Sie mit der Maus darüber, um den genauen Zeitstempel zu sehen. **Never run** bedeutet, dass sie noch nicht ausgelöst wurde. |
| **Status** | Zustand des Zeitplans (siehe unten). |

| Status | Meaning |
|--------|---------|
| **On schedule** (grün) | Die Aufgabe läuft in ihrem erwarteten Intervall. |
| **Delayed** (rot) | Die Aufgabe ist nicht zur erwarteten Zeit gelaufen. Untersuchen Sie das oder melden Sie es dem Support. |
| **Unknown** (grau) | Der Zustand des Zeitplans konnte nicht ermittelt werden. |

Beide Tabellen haben eine Schaltfläche **Refresh**, die die aktuellen Zahlen auf Anforderung neu lädt.
