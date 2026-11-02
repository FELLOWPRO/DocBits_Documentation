# Workflow-Protokolle

## **Übersicht**

Die **Workflow-Protokolle** ermöglichen es Benutzern, zu analysieren, welche Workflows für ein Dokument ausgeführt wurden, die Ausführungsergebnisse zu verstehen und in die Detailinformationen auf Bedingungsebene einzutauchen, um Fehlerbehebung oder Validierung durchzuführen.

## **Zugriff auf Workflow-Protokolle**

Um auf die Workflow-Protokolle zuzugreifen:

1. Navigieren Sie zum **Dashboard**.
2. Klicken Sie auf das **Aktionen-Menü** (Drei-Punkte-Symbol) neben dem gewünschten Dokument.
3. Wählen Sie **Workflow-Protokolle** aus dem Menü aus.
   * <mark style="color:red;">**Hinweis**</mark>**:** Die Workflow-Funktion muss aktiviert sein, um diese Option nutzen zu können.
4.  Ein **Seitenbereich** wird geöffnet, der eine Zusammenfassung der ausgeführten Workflows zeigt.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Komponenten des Workflow-Protokoll-Panels**

#### **1. Workflow-Zusammenfassungszähler**

Oben im Protokollbereich befinden sich:

* **Blau**: Gesamtanzahl der ausgeführten Workflows.
* **Rot**: Workflows, die mit **Fehlern** endeten.
* **Gelb**: Workflows, die aufgrund von Bedingungsfehlern **nicht abgeschlossen** wurden.
* **Grün**: Erfolgreich **ausgeführte** Workflows.

#### **2. Workflow-Ausführungstabelle**

Jede Zeile in der Tabelle repräsentiert eine Workflow-Ausführung und enthält:

* **Workflow-Name**
* **Zeitstempel** (Erstellt am)
* **Laufzeit** (in Sekunden)
* **Ergebnis-Symbol**:
  * Grüner Haken: Workflow wurde erfolgreich ausgeführt.
  * Rotes Kreuz: Workflow wurde mit einem Fehler ausgeführt.
  * Oranger Strich: Ausführung wurde aufgrund einer nicht erfüllten Bedingung gestoppt.

Durch Klicken auf den **Pfeil** links von jeder Zeile wird die **Detailansicht des Workflows** erweitert.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Detailansicht des Workflows**

Durch Klicken auf eine bestimmte Workflow-Zeile wird das **ausführliche Ausführungsprotokoll** geöffnet, das Folgendes zeigt:

#### **Bedingungsauswertung**

* **Wenn...**-Block: Anfangsbedingung.
* **Und...**-Block(s): Zusätzliche Bedingungen.
* **Dann...**-Block(s): Aktionen, die ausgeführt werden, wenn alle Bedingungen erfüllt sind.

Jede Bedingungszeile zeigt:

* **Grüner Haken**: Bedingung wurde erfüllt.
* **Oranger Strich**: Bedingung wurde nicht erfüllt.
* **Rotes Kreuz**: Bedingung ist **aufgrund eines Fehlers** fehlgeschlagen.

### **Wichtiger Verhaltenshinweis**

In einer Standard-Kartenfolge beendet eine nicht erfüllte Bedingung die nachfolgende Folge. Im Advanced Workflow bestimmt dagegen die verbundene Ausgangsroute, welche Knoten als Nächstes erreichbar sind. Graue Karten können übersprungen worden sein; sie belegen keinen technischen Fehler. Wählen Sie den betreffenden Knoten aus und lesen Sie dessen konkreten Status.

Auch ein grüner Laufkopf allein belegt keinen fachlichen Abschluss. Im [geprüften ALL-Beispiel](masterclass/control-nodes.md) enthält der gespeicherte echte Dokumentlauf vier erfolgreiche Knoten, während ALL und die Abschlussaktion übersprungen werden. Prüfen Sie deshalb die erwartete Abschlussaktion und die Wirkung am Dokument.

## Einen konkreten Fehler bis zum Nachtest verfolgen

Wählen Sie einen konkreten Lauf und notieren Sie Zeitpunkt, Workflow-Stand und Dokumentbezug. Öffnen Sie den ersten relevanten Knoten und vergleichen Sie dessen tatsächliche Eingabe, Kartenversion, Operator und angeschlossenen Ausgang. Unterscheiden Sie einen regulären Nichttreffer von einem technischen Fehler und von einer nicht erreichten Karte. Im Advanced Workflow kann ein regulär falscher Vergleich eine ausdrücklich verbundene Alternativroute erreichen; übertragen Sie das Stoppen einer Standard-Kartenfolge nicht pauschal auf den gesamten Graphen.

Nach einer gezielten Korrektur vergleichen Sie einen neuen Lauf mit dem alten. Prüfen Sie die fachliche Wirkung am Dokument oder am eigenen Testziel. Ein alter grüner Protokolleintrag belegt den neuen Stand nicht. Konkrete Beispiele stehen unter [Workflow-Meldungen](workflow-error-catalog.md) und [systematischer Fehlerdiagnose](workflow-troubleshooting.md).
