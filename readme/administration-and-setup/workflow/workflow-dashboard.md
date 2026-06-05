---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Workflow-Dashboard

Das Workflow-Dashboard ist Ihre zentrale Anlaufstelle zur Verwaltung und Uberwachung aller Workflows in DocBits. Greifen Sie darauf zu, indem Sie auf das **Workflows**-Symbol in der linken Seitenleiste klicken.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard with run totals, success and fail rates, the runs chart and recent activity"><figcaption><p>Das Workflow-Dashboard — Ausführungssummen, Erfolgs-/Fehlerraten und letzte Aktivitäten für jeden Workflow.</p></figcaption></figure>

## Dashboard-Reiter

Der Dashboard-Reiter bietet einen schnellen Uberblick uber die Workflow-Leistung fur einen ausgewahlten Zeitraum.

### Filter

- **Startdatum / Enddatum** — Wahlen Sie den Zeitraum fur die Statistiken
- **Workflow-Name** — Filtern Sie nach einem bestimmten Workflow oder zeigen Sie alle an
- **Vergleichen** — Vergleichen Sie zwei Zeitraume nebeneinander
- **Zurucksetzen** — Alle Filter zurucksetzen

### Statistik-Karten

| Metrik | Beschreibung |
|---|---|
| **Heute ausgefuhrte Workflows** | Gesamtzahl der Workflow-Ausfuhrungen heute |
| **Erstellte Workflows (Zeitraum)** | Neue Workflows, die im ausgewahlten Zeitraum erstellt wurden |
| **Gesamtausfuhrungen** | Kumulative Workflow-Ausfuhrungen uber den Zeitraum |
| **Erfolgreiche Ausfuhrungen** | Anzahl der Ausfuhrungen, die ohne Fehler abgeschlossen wurden |
| **Erfolgsrate** | Prozentsatz erfolgreicher Ausfuhrungen im Verhaltnis zu den Gesamtausfuhrungen |
| **Fehlerrate** | Prozentsatz fehlgeschlagener Ausfuhrungen im Verhaltnis zu den Gesamtausfuhrungen |

{% hint style="warning" %}
Eine hohe Fehlerrate (angezeigt als **CRITICAL** in Rot) weist darauf hin, dass Workflows auf Fehler stossen. Untersuchen Sie die fehlgeschlagenen Workflows mithilfe der Ausfuhrungsprotokolle im [Erweiterten Workflow-Builder](advanced-workflow-builder/).
{% endhint %}

### Diagramm der Workflow-Ausfuhrungen

Das Diagramm zeigt eine monatliche Aufschlusselung von **erfolgreichen** (grun) und **fehlgeschlagenen** (rot/rosa) Workflow-Ausfuhrungen und hilft Ihnen, Trends und Fehler-Spitzen zu erkennen.

### Letzte Aktivitaten

- **Letzte Workflow-Tests** — Zeigt die letzten Testausfuhrungen mit Bestanden-/Fehlgeschlagen-Status
- **Letzte Workflows** — Zeigt kurzlich erstellte oder geanderte Workflows

## Reiter Workflow-Liste

Der Reiter Workflow-Liste zeigt alle Workflows mit Such-, Sortier- und Verwaltungsfunktionen.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Spalten

| Spalte | Beschreibung |
|---|---|
| **Status** | Umschaltsymbol — klicken Sie, um einen Workflow zu aktivieren/deaktivieren |
| **Name** | Workflow-Name (klicken Sie, um ihn im Workflow-Builder zu offnen) |
| **Typ** | Badge mit `Advanced` fur visuelle Workflows |
| **Wenn...** | Zusammenfassung der Auslosebedingung |
| **Aktualisiert von** | Benutzer, der den Workflow zuletzt geandert hat |
| **Erstellt am** | Erstellungsdatum und -uhrzeit |
| **Aktualisiert** | Datum und Uhrzeit der letzten Anderung |
| **Aktionen** | Kontextmenu (Loschen, Duplizieren, Exportieren) |

### Aktionen

- **Suche** — Workflows nach Name uber die Suchleiste filtern
- **+ WORKFLOW HINZUFUGEN** — Einen neuen Workflow erstellen (offnet den [Erweiterten Workflow-Builder](advanced-workflow-builder/))
- **VORLAGEN** — Gespeicherte Workflow-Vorlagen durchsuchen und laden
- **WORKFLOW IMPORTIEREN** — Einen Workflow aus einer JSON-Datei importieren

## Reiter Test-Manager-Liste

Die Test-Manager-Liste zeigt alle Workflow-Testkonfigurationen und -ergebnisse. Nutzen Sie diese, um automatisierte Testszenarien fur Ihre Workflows einzurichten.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Workflow Test Manager List with test scenarios and Run All Tests"><figcaption><p>Die Test-Manager-Liste — jedes Szenario zeigt ein Bestanden-/Fehlgeschlagen-Ergebnis; verwenden Sie <strong>Run All Tests</strong>, um alle erneut auszuführen.</p></figcaption></figure>

## Reiter Lizenz

Der Reiter Lizenz zeigt Ihren aktuellen DocFlow-Lizenzstatus und die verfugbaren Funktionen.

## Reiter Card SDK

Der Reiter Card SDK ermoglicht es Ihnen, benutzerdefinierte Workflow-Karten (Partner-Karten) zu erstellen und zu verwalten, die die integrierten Funktionen von DocFlow erweitern.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### ZIP hochladen

Laden Sie eine Partner-App als ZIP-Datei hoch, die Folgendes enthalt:
- `app.json` — Karten-Metadaten und Konfiguration
- `.docflowcompose/flow/` — Karten-Definitionsdateien

Maximale Dateigrösse: **10 MB**. Klicken Sie auf **Upload & Validate**, um die Karte zur Uberprufung einzureichen.

### GitHub-Import

Importieren Sie Partner-Karten direkt aus einem GitHub-Repository, anstatt eine ZIP-Datei hochzuladen.

### Einreichungen

Alle eingereichten Partner-Karten anzeigen und verwalten:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Spalte | Beschreibung |
|---|---|
| **Card Name** | Name der Partner-App und Karte |
| **card_type_label** | Kartentyp (`Action_card` oder `Condition_card`) |
| **Version** | Kartenversionsnummer |
| **Eingereicht** | Einreichungsdatum |
| **Status** | Aktueller Uberprufungsstatus |
| **Aktionen** | Verfugbare Aktionen basierend auf dem Status |

#### Karten-Status

| Status | Bedeutung | Verfugbare Aktionen |
|---|---|---|
| **Validated** | Karte hat die Validierung bestanden | Herunterladen, Genehmigen, Ablehnen |
| **Approved** | Karte ist aktiv und in Workflows verfugbar | Herunterladen, Deaktivieren, Widerrufen |
| **Rejected** | Karte hat die Uberprufung nicht bestanden | Loschen |
| **Disabled** | Karte wurde deaktiviert | Loschen |

### SDK-Vorlage herunterladen

Klicken Sie auf **Download SDK Template**, um eine Startvorlage zum Erstellen Ihrer eigenen benutzerdefinierten Karten zu erhalten. Die Vorlage enthalt die erforderliche Dateistruktur und Beispielkonfigurationen.

{% hint style="info" %}
Partner-Karten konnen auch programmgesteuert uber die [DocFlow MCP-Tools](../../../advanced-functions-and-tools/docflow-mcp/) verwaltet werden. Verwenden Sie die Card SDK MCP-Tools, um Karten aus Ihrer IDE oder Ihren Automatisierungsskripten zu erstellen, zu validieren, zu genehmigen und zu testen.
{% endhint %}
