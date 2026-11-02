---
description: "Lernweg vom Einstieg zum Experten"
---

# Lernweg vom Einstieg zum Experten

Arbeiten Sie die Stufen nacheinander durch. Lesen allein genügt nicht: Jede Stufe endet mit einer eigenen Konfiguration, einer überprüfbaren Erwartung und einem Nachweis. P0 schützt den Ablauf vor grundlegenden Fehlannahmen; P1 vertieft Daten, Geschäftsentscheidungen und Integrationen.

1. [Orientierung und Ausführungsmodell](#level-1)
2. [Erste eigene Regel](#level-2)
3. [Felder, Datentypen und Grenzen](#level-3)
4. [Geschäftsregeln und Freigaben](#level-4)
5. [Advanced-Kontrollfluss und Unterworkflows](#level-5)
6. [Berechnung, Schnittstelle und Export](#level-6)
7. [Änderungen und Expertenbetrieb](#level-7)

## Voraussetzungen

Verwenden Sie eine eigene Testorganisation und einen synthetischen Beleg. Prüfen Sie Organisation, Rolle, Workflow-Lizenz und Advanced-Freigabe. Lassen Sie importierte Übungen inaktiv. Die beigefügten vollständigen JSON-Daten sind für Advanced Test → Custom Data bestimmt. Für echte Freigaben und Integrationen benötigen Sie gesonderte Testbenutzer und Testziele.

## 1. Orientierung und Ausführungsmodell <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/de.html).

**Übung:** Erklären Sie Organisation, Zugriff, When–And–Then und den Unterschied zwischen linearer Regel und Advanced-Graph. Unterscheiden Sie Dokumenttypfilter, Ausführungsanlass, Speichern und Aktivieren.

**Abschlusskriterium:** Sie können vor dem Aufbau sagen, wann die Regel berücksichtigt wird und welcher Nachweis eine Simulation von einem Dokumentlauf unterscheidet.

Lesen und nachbauen: [Wann läuft mein Workflow?](workflow-execution-model.md) · [P0: Status wechseln und erneute Ausführung begrenzen](masterclass/status-and-reentry.md).

## 2. Erste eigene Regel <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/de.html).

**Übung:** Bauen Sie When Rechnung → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Lassen Sie die Regel inaktiv. Testen Sie mit den vollständigen Daten für 999, 1000 und 1000.01; diese lineare Regel benötigt noch keinen Kontrollknoten.

**Abschlusskriterium:** REVIEW wird nur über 1000 erreicht. Sie notieren Feldtyp, Operator und gewählten Ausgang. Fehlende Eingabe wird gesondert behandelt.

Lesen und nachbauen: [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md) · [Workflow-Übungspaket](workflow-training-kit.md).

## 3. Felder, Datentypen und Grenzen <a id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/de.html).

**Übung:** Prüfen Sie fehlend, null, leeren Text, Leerzeichen, false, 0 und Zahlen als Text. Rechnen Sie eine Toleranz einmal mit Bestell- und einmal mit Dokumentreferenz. Vergleichen Sie eine und alle tatsächlich zugeordneten Positionen.

**Abschlusskriterium:** Sie begründen wahr, falsch und Fehler anhand von Wert, Typ, Referenz und vorhandenen Daten; keine vergleichbare Position wird nicht als erfolgreiche Freigabe gewertet.

Lesen und nachbauen: [P1: Field is, Docfield is und zwei Felder vergleichen](masterclass/field-conditions.md) · [P1: Toleranzen und PO-Vergleich mit eindeutiger Referenz](masterclass/tolerances-and-po.md).

## 4. Geschäftsregeln und Freigaben <a id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/de.html).

**Übung:** Konfigurieren Sie eine Entscheidungstabelle mit zwei überschneidungsfreien Betragsregeln. Verfolgen Sie die gespeicherte Benutzer-Rückgabe bis zur Zuweisung. Planen Sie A mit Reihenfolge 10 und B mit 20 einschließlich Ablehnung und Rückfallroute.

**Abschlusskriterium:** Sie unterscheiden Zuständigkeit, Aufgabe, Nachricht und tatsächliche Genehmigung. Ein realer Übergang zu B wird nur mit einer verarbeiteten Entscheidung von A abgenommen.

Lesen und nachbauen: [P1: Entscheidungstabelle bis zur Zuweisung nachvollziehen](masterclass/decision-table-routing.md) · [P1: Zuweisung, Aufgabe und sequenzielle Freigabe unterscheiden](masterclass/assignment-task-sequential.md).

## 5. Advanced-Kontrollfluss und Unterworkflows <a id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/de.html).

**Übung:** Vergleichen Sie ALL, ANY und OR mit zwei tatsächlich erreichten Prüfungen. Untersuchen Sie zusätzlich einen nicht gewählten Zweig. Führen Sie die sieben v2-Routingfälle aus und prüfen Sie Run Workflow mit einem eigenen inaktiven Ziel.

**Abschlusskriterium:** Sie erklären Test-/Scheduler-Unterschied, Quellenzählung und Fehlerweitergabe. Der gemeinsame Abschluss wird in v2 ohne wartenden OR erreicht; ein grüner Unteraufruf wird am Ziel überprüft.

Lesen und nachbauen: [P0: Wait ALL, Wait ANY und OR richtig verbinden](masterclass/control-nodes.md) · [P0: Run Workflow, Zielbedingungen und Fehler verstehen](masterclass/run-workflow.md) · [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md).

## 6. Berechnung, Schnittstelle und Export <a id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/de.html).

**Übung:** Vergleichen Sie eine Tabelle vor und nach Berechnung einschließlich Regex-Nichttreffer und Division durch null. Definieren Sie für eine Schnittstelle den tatsächlichen Rückschreibweg. Planen Sie Export erst nach Freigabe mit eigener Testkonfiguration.

**Abschlusskriterium:** Sie weisen gelesene Folgewerte, Empfängereingang und ERP-Verarbeitung getrennt nach. Simulation oder Exportanforderung wird nicht als Zustellung protokolliert.

Lesen und nachbauen: [P1: Tabellen berechnen und Regex-Abhängigkeit prüfen](masterclass/table-calculations.md) · [P1: API-Aufruf und Weiterverwendung der Antwort prüfen](masterclass/api-response-contract.md) · [P1: Exportvarianten, offene Aufgaben und Abschlussstatus](masterclass/export-lifecycle.md).

## 7. Änderungen und Expertenbetrieb <a id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/de.html).

**Übung:** Sichern Sie den Workflow-Export und notieren Sie Kartenversionen vor einer Änderung. Wiederholen Sie Positiv-, Negativ-, Fehler- und Grenzfälle sowie eine zweite Ausführung. Ordnen Sie den ersten Fehler einer konkreten Eingabe und Konfiguration zu.

**Abschlusskriterium:** Sie können eine Änderung abnehmen, auf den gesicherten Stand zurückgehen und einen neuen Dokumentlauf mit Wirkungsnachweisen vergleichen. Ursache, Korrektur und offene Grenzen stehen im Protokoll.

Lesen und nachbauen: [Workflow-Fehler systematisch diagnostizieren](workflow-troubleshooting.md) · [Karten verstehen und zuverlässig konfigurieren](card-reference-standard.md).

## Wissen selbst prüfen

| Frage | Antwort |
| --- | --- |
| Ist false bei Field is v2 leer? | Ja. 0 und der Text "false" sind dagegen nicht leer. |
| Garantiert ein grüner OR-Test den Dokumentlauf? | Nein. Nicht erreichte Vorgänger werden im Test anders behandelt als im geprüften Scheduler. |
| Kann Run Workflow ein inaktives Ziel aufrufen? | Ja, beim geprüften ausdrücklichen Aufruf. Zielbedingungen und Ergebnis weiterhin prüfen. |
| Stellt HTTP 200 automatisch api.response.cost_center bereit? | Nein. Die geprüften Aktionen haben dafür keinen automatischen JSON-Ausgabevertrag. |
| Beweist ein grüner Test den Exportempfang? | Nein. Dokumentlauf, Empfängereingang und ERP-Verarbeitung benötigen eigene Nachweise. |

## Die fünf Begleitkapitel

Diese Kapitel begleiten die Übungen durchgehend: Ausführungsmodell → nachgebauter Geschäftsfall → Übungspaket → Diagnose → Kartenreferenz. Sie sind Arbeitsunterlagen zu den Stufen, keine fünf zusätzlichen ungeprüften Aufgaben.

1. [Wann läuft mein Workflow?](workflow-execution-model.md)
2. [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md)
3. [Workflow-Übungspaket](workflow-training-kit.md)
4. [Workflow-Fehler systematisch diagnostizieren](workflow-troubleshooting.md)
5. [Karten verstehen und zuverlässig konfigurieren](card-reference-standard.md)

## Abschlussprotokoll

Verwenden Sie acceptance-record-template.json aus dem Übungspaket. Halten Sie Szenario, Konfigurationsstand, Erwartung, Beobachtung und Nachweisart fest. Unterscheiden Sie Dev-Test, isolierten Quelltest, echten Dokumentlauf, Empfang und ERP-Verarbeitung. Markieren Sie nicht geprüfte Schritte ausdrücklich als offen.

## Vom Lernfall in den Betrieb

Nach den Übungen helfen [kontrollierte Aktivierung](workflow-go-live.md), [Änderung und Wiederherstellung](workflow-change-and-recovery.md) sowie der [Meldungskatalog](workflow-error-catalog.md). Belegen Sie den vorgesehenen Ausführungsanlass, die tatsächliche Wirkung und eine Wiederholung getrennt.
