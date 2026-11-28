# Workflow-Protokolle

Für erzählte Erklärungen der erweiterten Protokollansicht sehen Sie [Die relevante Ausführung finden](advanced-workflow-builder/videos.md#find-the-relevant-execution) und [Knoten verfolgen und diagnostizieren](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Beide Kapitel sind auf Englisch und Deutsch verfügbar, mit Untertiteldateien und Transkripten.

## **Übersicht**

Die **Workflow Logs** ermöglichen es Benutzern zu analysieren, welche Workflows für ein Dokument ausgeführt wurden, die Ausführungsergebnisse zu verstehen und bis auf Bedingungsebene in die Details zu gehen, um Fehler zu beheben oder zu validieren.

## **Zugriff auf die Workflow Logs**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Video:** Die Workflow Logs lesen · 1:34 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transkript</summary>

**Workflow Logs öffnen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Jedes Dokument behält die Logs der Workflows, die darauf gelaufen sind. Öffnen Sie im Dashboard die Aktionen eines Dokuments und wählen Sie Workflow Logs.

**Läufe und ihre Ergebnisse** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

Oben sehen Sie, wie viele Läufe es gab und wie viele mit einem Fehler, einer nicht erfüllten Bedingung oder Erfolg endeten. Darunter ist jeder Lauf mit seinem Workflow, Zeit, Dauer und Ergebnis aufgeführt.

**Der Pfad eines Laufs** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Ziehen Sie den Trenner nach links, damit die Logs mehr Platz haben. Klicken Sie dann auf einen Lauf, um den Pfad zu sehen, den er genommen hat. Jede Karte zeigt ihr Ergebnis: grün für Erfolg, orange für eine nicht erfüllte Bedingung, rot für einen Fehler. Hier endete die And-Karte mit einer nicht erfüllten Bedingung, daher lief die Then-Karte danach nicht.

**Warum eine Karte so endete** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Wählen Sie eine Karte, um ihr Log zu lesen. Es sagt, was die Karte verglichen hat und warum sie so endete. Hier ist das Dokument bereit zur Validierung, aber die Karte erwartet eine ausstehende zweite Genehmigung.

**Ein Fehler und sein Grund** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Ein Lauf, der mit einem Fehler endet, zeigt die fehlgeschlagene Karte in Rot. Hier konnte die And-Karte die Lieferadresse nicht aus dem Dokument lesen. Fehlende Daten sind immer ein Fehler, daher lief die Then-Karte danach nicht.

**Läufe finden** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Bei vielen Läufen finden Sie mit der Suche einen Workflow nach Namen und mit dem Filter grenzen Sie die Liste nach Status oder Datum ein.

**Hinweis zum Ausführungslimit** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Oben erscheint ein Hinweis, wenn ein Workflow auf diesem Dokument sein Ausführungslimit erreicht hat. Das Video über Ausführungslimits erklärt ihn.

</details>

So greifen Sie auf die Workflow Logs zu:

1. Navigieren Sie zum **Dashboard**.
2. Klicken Sie auf das **Actions menu** (Drei-Punkte-Symbol) neben dem gewünschten Dokument.
3. Wählen Sie **Workflow Logs** aus dem Menü.
   * <mark style="color:red;">**Note**</mark>: Die Workflow-Funktion muss aktiviert sein, um diese Option zu erreichen.
4.  Ein **side panel** öffnet sich und zeigt eine Zusammenfassung der ausgeführten Workflows.\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Ein Log als eigene Seite öffnen**

Das side panel verdeckt die Dokumentenliste. Für ein Dokument, dessen Workflow Sie eine Weile untersuchen, öffnen Sie dasselbe Log als vollständige Seite: Wählen Sie das Symbol für ein neues Fenster im Kopf des Panels. Die Seite hat die Adresse `/workflows/logs/<document id>`, sodass Sie sie in einem zweiten Browserfenster offen halten oder die Adresse an eine Kollegin oder einen Kollegen senden können, der Zugriff auf das Dokument hat.

Die Seite zeigt dieselben Zusammenfassungszähler, dieselbe Tabelle der ausgeführten Workflows und dieselbe Detailansicht wie das Panel.

## **Zu einem anderen Dokument wechseln**

Auf der vollständigen Seite findet ein Suchfeld über der Liste ein Dokument nach Namen oder nach seiner ID. Die Ergebnisse zeigen das Upload-Datum, den Bearbeiter und den Status jedes Dokuments, sodass Sie Dokumente mit ähnlichen Namen unterscheiden können. Wenn Sie ein Ergebnis auswählen, wird dessen Workflow Log geladen und das Dokument in die Adresse übernommen. Die Suche umfasst die Dokumente Ihrer Organisation, die Sie laut Ihren Berechtigungen sehen dürfen; wenn nichts passt, sagt DocBits das unter dem Feld, statt eine leere Liste zu zeigen.

## **Komponenten des Workflow Logs Panel**

#### **1. Zusammenfassungszähler des Workflows**

Oben im Logs-Panel:

* **Blau**: Gesamtzahl der ausgeführten Workflows.
* **Rot**: Workflows, die mit **Fehlern** endeten.
* **Gelb**: Workflows, die wegen nicht erfüllter Bedingungen **nicht abgeschlossen** wurden.
* **Grün**: Erfolgreich **ausgeführte** Workflows.

#### **2. Tabelle der Workflow-Ausführungen**

Jede Zeile in der Tabelle repräsentiert eine Workflow-Ausführung und enthält:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (in Sekunden)
* **Result Icon**:
  * Grüner Haken: Workflow wurde erfolgreich ausgeführt.
  * Rotes Kreuz: Workflow wurde mit einem Fehler ausgeführt.
  * Oranger Strich: Die Ausführung wurde gestoppt, weil eine Bedingung nicht erfüllt war.

Durch Klicken auf den **Pfeil** links von jeder Zeile wird die **Detailansicht des Workflows** erweitert.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Detailansicht des Workflows**

Durch Klicken auf eine bestimmte Workflow-Zeile wird das **ausführliche Ausführungsprotokoll** geöffnet, das zeigt:

#### **Bedingungsauswertung**

* **When...**-Block: Anfangsbedingung.
* **And...**-Block bzw. -Blöcke: Zusätzliche Bedingungen.
* **Then...**-Block bzw. -Blöcke: Aktionen, die ausgeführt werden, wenn alle Bedingungen erfüllt sind.

Jede Bedingungszeile zeigt:

* **Grüner Haken**: Bedingung wurde erfüllt.
* **Oranger Strich**: Bedingung wurde nicht erfüllt.
* **Rotes Kreuz**: Bedingung ist **aufgrund eines Fehlers** fehlgeschlagen

### **Wichtiger Hinweis zum Verhalten**

Wenn eine Bedingung in einem Workflow **nicht erfüllt** ist, **stoppt das System die Auswertung aller weiteren Workflow-Karten** innerhalb dieses Workflows. Dieses Verhalten verhindert unnötige Verarbeitung\
Als visueller Hinweis wird die Karte, die **ihre Bedingung nicht erfüllt hat**, in **Grau** dargestellt, und alle **nachfolgenden Karten** im selben Workflow erscheinen ebenfalls **Grau**, was anzeigt, dass sie **nicht ausgeführt** wurden.
