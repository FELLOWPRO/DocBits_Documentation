---
description: "Ereignisse, Bedingungen, Reihenfolge, Tests und Aktivierung von Workflows richtig unterscheiden."
---

# Wann läuft mein Workflow?

Ein Workflow benötigt einen Ausführungsanlass und passende Bedingungen. **Dokumenttyp ist Rechnung** beschreibt eine Auswahl. Daraus folgt nicht, dass jede beliebige Änderung an einer Rechnung automatisch einen neuen Lauf startet.

## Vom Ereignis zur Aktion

1. Prüfen Sie Organisation, Berechtigungen, Workflow-Modul und bei Advanced zusätzlich die Advanced-Freigabe.
2. Bestimmen Sie den Anlass: dokumentbezogene Verarbeitung, expliziter manueller Aufruf oder ein unterstützter Ereignis-Trigger. Verwenden Sie nur Trigger, die der Kartenkatalog Ihrer Version tatsächlich anbietet.
3. Im Standard Workflow müssen When und alle And-Bedingungen zutreffen. Eine falsche Bedingung beendet diese Kartenfolge.
4. Im Advanced Workflow bestimmen Einstieg und verbundene Ergebnisausgänge den Weg. Eine falsche And-Bedingung kann über Orange weiterlaufen; Rot behandelt einen Auswertungsfehler.
5. Prüfen Sie das Ergebnis am richtigen Ort: Testantwort, gespeicherter Lauf, Dokument oder angeschlossenes Zielsystem.

**Start** dient als manueller Einstieg. Das Übungspaket verwendet einen When-Einstieg für Rechnung und eine zusätzliche Begrenzung auf die Trainingsnummer, damit es auch die Anforderungen der aktuellen Oberfläche erfüllt. Es wird inaktiv importiert und manuell getestet; ein erfolgreicher manueller Test belegt keinen automatischen Dokumentereignis-Trigger.

## Speichern, Testen und Aktivieren

| Zustand | Bedeutung |
| --- | --- |
| Lokaler Entwurf | Eine Browserkopie ersetzt kein Speichern auf dem Server. |
| Gespeichert | Die Konfiguration ist vorhanden. Prüfen Sie den Aktivzustand separat; Speichern kann eine neue Regel bereits aktivieren. |
| Advanced-Test | Prüft den aktuellen Graphen, auch mit ungespeicherten Änderungen. Dokumentaktionen werden im Testmodus simuliert. |
| Aktiviert | Die Regel kann bei ihrem passenden Ausführungsanlass berücksichtigt werden. Das ersetzt keinen Test dieses Anlasses. |

Der Test Manager und der Advanced-Testdialog sind verschiedene Ausführungsoberflächen. Ein Statusvergleich allein bestätigt keine Zuweisung, Nachricht oder Exportzustellung. Prüfen Sie mögliche Nebenwirkungen der verwendeten Testoberfläche vor einem Lauf an echten Dokumenten.

## Mehrere Workflows und erneute Ausführung

Kleinere Werte der **Ausführungsreihenfolge** laufen zuerst. Beispiel: Workflow 100 bereitet ein Feld vor; Workflow 200 prüft dessen Wert. Verwenden Sie unterschiedliche Werte und bestätigen Sie die tatsächlich gelesenen Daten in einem neuen Lauf. Die Position einer Advanced-Karte auf der Arbeitsfläche bestimmt keine Reihenfolge.

**Change Status to → Trigger Workflows** kann eine weitere Workflow-Ausführung anstoßen. **Run Workflow** ruft einen ausgewählten Workflow auf. Beide Mechanismen benötigen bewusst gesetzte Bedingungen; sie sind keine Zusicherung einer einmaligen Ausführung. Begrenzen Sie Aufgaben und Exporte über einen fachlichen Bearbeitungszustand und prüfen Sie den zweiten Lauf ausdrücklich. Ein Erledigt-Merkmal allein ist bei gleichzeitigen Aufrufen kein allgemeiner Schutz vor Doppelverarbeitung.

Weiter mit dem [Advanced-Geschäftsfall](advanced-workflow-case-study.md), dem [Übungspaket](workflow-training-kit.md) und der [Fehlerdiagnose](workflow-troubleshooting.md).

## WF-01: Übung und Abnahme

Notieren Sie für Ihre Regel Anlass, Filter, Aktivzustand und Kartenversion. Prüfen Sie zwei aufeinanderfolgende Ausführungen und die Reihenfolge 100/200 mit einem tatsächlich gelesenen Folgefeld. Trennen Sie erwartete Folgeausführung und beobachteten Lauf.

[Lernweg](workflow-learning-path.md)
