---
description: "Lernweg vom Einstieg zum Experten"
---

# Lernweg vom Einstieg zum Experten

Sieben Stufen führen vom ersten Blick in den Workflow-Designer bis zur eigenen Änderung an einem laufenden Workflow. Jede Stufe nennt ein Ziel, die Schritte in Ihrer eigenen Testorganisation und ein Ergebnis, das Sie prüfen können. Arbeiten Sie sie der Reihe nach durch und bauen Sie jede Übung selbst nach: Jede Stufe setzt auf der Konfiguration der vorherigen auf.

1. [Orientierung und Ausführungsmodell](./#level-1)
2. [Erste eigene Regel](./#level-2)
3. [Felder, Datentypen und Grenzen](./#level-3)
4. [Geschäftsregeln und Freigaben](./#level-4)
5. [Advanced-Kontrollfluss und Unterworkflows](./#level-5)
6. [Berechnung, Schnittstelle und Export](./#level-6)
7. [Änderungen und Expertenbetrieb](./#level-7)

## Bevor Sie beginnen

* Eine eigene Testorganisation mit einem synthetischen Beleg darin. Üben Sie nie an Kundenbelegen.
* Ihre Rolle, die Workflow-Lizenz und die Advanced-Freigabe, geprüft vor Stufe 1.
* Importierte Übungen bleiben inaktiv, bis Sie sie getestet haben.
* Vollständige JSON-Daten gehören in **Advanced Test → Custom Data**.
* Echte Freigaben und Integrationen brauchen eigene Testbenutzer und Testziele; ein Test im Designer ersetzt das nicht.

## 1. Orientierung und Ausführungsmodell <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/de.html).

**Ziel:** Sie wissen, was einen Workflow startet, und was Ihnen ein Testergebnis sagen kann und was nicht.

1. Prüfen Sie Organisation, Ihren Zugriff, das Workflow-Modul und die Advanced-Freigabe.
2. Sagen Sie When–And–Then in eigenen Worten und erklären Sie dann, wo eine lineare Regel endet und wie ein Advanced-Graph stattdessen seinen verbundenen Ausgängen folgt.
3. Halten Sie vier Dinge auseinander, die im Designer ähnlich aussehen: den Dokumenttypfilter, den Ausführungsanlass, das Speichern und das Aktivieren.

**Abschlusskriterium:** Sie können sagen, wann eine Regel überhaupt betrachtet wird, und welcher Nachweis eine Simulation von einem Lauf auf einem echten Beleg trennt.

**Vertiefung:** [Wann läuft mein Workflow?](workflow-execution-model.md) · [Status ändern, ohne den Workflow neu zu starten](masterclass/status-and-reentry.md)

## 2. Erste eigene Regel <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/de.html).

**Ziel:** Eine Regel vom Designer bis zu einem geprüften Ergebnis bringen, ohne einen Beleg anzufassen.

1. Bauen Sie sie im Advanced Builder: When Rechnung → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Eine lineare Regel dieser Größe braucht keinen Kontrollknoten.
2. Speichern Sie sie und prüfen Sie in der Regelliste, ob sie noch inaktiv ist, denn das Speichern einer neuen Regel kann sie bereits aktivieren. Advanced Test ist eine eigene Ausführungsebene: Es wertet den Graphen im Builder aus, nicht die aktivierte Regel.
3. Führen Sie Advanced Test mit vollständigen Daten für 999, 1000 und 1000.01 aus. Notieren Sie je Fall Feldtyp, Operator und gewählten Ausgang und ergänzen Sie einen Fall, in dem der Betrag ganz fehlt.

**Abschlusskriterium:** REVIEW wird nur bei 1000.01 erreicht, ein fehlender Betrag erscheint als Fehler und nicht als gewöhnliches Ergebnis unterhalb der Grenze, und die Regel ist am Ende wieder abgeschaltet.

**Vertiefung:** [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md) · [Workflow-Übungspaket](workflow-training-kit.md)

## 3. Felder, Datentypen und Grenzen <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/de.html).

**Ziel:** Sie wissen, was eine Bedingung tatsächlich vergleicht, bevor Sie ihrem Ergebnis trauen.

1. Prüfen Sie die Leer-Prüfung gegen ein fehlendes Feld, `null`, leeren Text, Leerzeichen, `false`, `0`, `"0"` und `"false"` und notieren Sie, welche davon als leer zählen.
2. Rechnen Sie dieselbe Toleranz von 2 Prozent zweimal: einmal mit der Bestellung als Referenz (Bestellung 100, Beleg 102.02) und einmal mit dem Beleg als Referenz.
3. Wechseln Sie auf der Bestellkarte zwischen Any und All und zählen Sie, wie viele Positionen tatsächlich verglichen wurden.

**Abschlusskriterium:** Sie erklären wahr, falsch und Fehler aus Wert, Typ, Referenz und vorhandenen Daten. In Version 5 der Bestellkarte ist ein Beleg ohne vergleichbare Position ein Datenfehler und keine erfolgreiche Freigabe.

**Vertiefung:** [P1: Field is, Docfield is und zwei Felder vergleichen](masterclass/field-conditions.md) · [P1: Toleranzen und Bestellreferenz eindeutig machen](masterclass/tolerances-and-po.md)

## 4. Geschäftsregeln und Freigaben <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/de.html).

**Ziel:** Eine Rechnung über eine Entscheidungstabelle an die richtige Person schicken und anschließend eine Freigabekette laufen lassen, die auf die erste prüfende Person wartet.

**Übung 1: Entscheidungstabelle mit direkter Zuweisung**

1. Legen Sie eine Entscheidungstabelle mit zwei Regeln an, die nicht beide zutreffen können: Prüfer A bis 1000, Prüfer B über 1000, mit `cost_center=4711` und `total_amount`.
2. Setzen Sie in **Decision Table has Returns** Version 3 `store_data=wf_store_data`. Weisen Sie den Beleg mit **Assign document based on decision table** und `assignee_type=user` zu und verwenden Sie echte Benutzer aus Ihrer Testorganisation.
3. Testen Sie einen Treffer, keinen Treffer, mehrere Treffer und eine ungültige Benutzer-ID und leiten Sie Nichttreffer und Zuweisungsfehler in einen ausdrücklichen Rückfall. Nehmen Sie die Zuweisung am Beleg selbst an.

**Übung 2: Sequenzielle Freigabe ohne direkte Zuweisung**

1. Legen Sie eine zweite, getrennte Regel mit den sequenziellen Karten an: die sequenzielle Zuweisungskarte an Position 10 für Prüfer A, dann die sequenzielle Aufgabenkarte an Position 20 für Prüfer B. Lassen Sie die direkte Zuweisung in diesem Lauf weg, denn die geprüfte Finalisierung kann den ersten sequenziellen Empfänger überspringen, wenn der Beleg im selben Lauf bereits direkt zugewiesen wurde.
2. Geben Sie als A frei und prüfen Sie, dass B den Beleg erst nach der verarbeiteten Entscheidung von A erhält; geben Sie dann als B frei.
3. Lehnen Sie in einem frischen Lauf als A ab und bestätigen Sie, dass der Export nicht stattfindet. Testen Sie anschließend, was passiert, wenn sich kein Empfänger ermitteln lässt.

**Abschlusskriterium:** Sie unterscheiden Zuständigkeit, Aufgabe, Benachrichtigung und tatsächliche Freigabe; A → Freigabe → B → Freigabe ist in dieser Reihenfolge passiert; eine Ablehnung von A hat den Export verhindert; und ein fehlender Empfänger galt nicht als abgeschlossene Freigabe.

**Vertiefung:** [P1: Entscheidungstabelle bis zur Zuweisung nachvollziehen](masterclass/decision-table-routing.md) · [P1: Zuweisung, Aufgabe und sequenzielle Freigabe unterscheiden](masterclass/assignment-task-sequential.md)

## 5. Advanced-Kontrollfluss und Unterworkflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/de.html).

**Ziel:** Parallele Pfade richtig zusammenführen und Arbeit an einen anderen Workflow übergeben.

1. Vergleichen Sie ALL, ANY und OR an zwei Prüfungen, die tatsächlich erreicht werden: ALL braucht einen passenden Ausgang von jeder Quelle, ANY und OR brauchen einen, und grün plus orange aus einer Quelle zählen weiterhin als eine Quelle.
2. Sehen Sie sich einen Zweig an, den der Lauf nicht genommen hat, wie im Fall MERGE-04: Advanced Test wertet die wartende Zusammenführung weiter aus, während der normale Lauf sie überspringt, sobald ein Vorgänger nie ankommt.
3. Führen Sie die sieben Fälle der v2-Fallstudie aus (darüber, darunter, Grenze, knapp darüber, fehlend, ungültige Zahl, anderer Beleg). Rufen Sie danach mit Run Workflow einen eigenen inaktiven Workflow auf und öffnen Sie den Pfad im Ziel selbst.

**Abschlusskriterium:** Sie erklären den Unterschied aus MERGE-04 zwischen Test und Lauf aus Schritt 2, wie Quellen gezählt werden und wohin ein Fehler wandert. Ein grüner Run-Workflow-Aufruf braucht trotzdem eine Prüfung im Ziel. V2 meint hier die zweite Version des Fallstudien-Graphen: Die Statuskarte jeder Route führt direkt zur gemeinsamen Abschlusskarte, ohne wartenden OR-Knoten.

**Vertiefung:** [P0: Wait ALL, Wait ANY und OR richtig verbinden](masterclass/control-nodes.md) · [P0: Run Workflow, Zielbedingungen und Fehler verstehen](masterclass/run-workflow.md) · [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md)

## 6. Berechnung, Schnittstelle und Export <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/de.html).

**Ziel:** Werte berechnen, ein Ergebnis aus einem externen System zurückholen und erst nach einer echten Freigabe exportieren.

1. Berechnen Sie eine Spalte und vergleichen Sie die ganze Tabelle vorher und nachher, einschließlich einer Zeile, in der der reguläre Ausdruck nicht greift, und einer Division durch null.
2. Schreiben Sie den Rückschreibevertrag mit dem externen System auf: Welches Belegfeld nimmt das Ergebnis auf, welche Karte oder Erweiterung schreibt es dorthin, und wie prüfen Sie den gespeicherten Wert anschließend? HTTP 200 allein ist kein Ergebnis.
3. Planen Sie den Export nach der Freigabe mit Ihrer eigenen Exportkonfiguration und notieren Sie, was Sie beim Empfänger prüfen werden.

**Abschlusskriterium:** Folgewerte im Feld, Eingang beim Empfänger und Verarbeitung im ERP haben jeweils einen eigenen Nachweis. Eine Simulation oder ein eingereihter Export ist keine Zustellung.

**Vertiefung:** [P1: Tabellen berechnen und Regex-Abhängigkeit prüfen](masterclass/table-calculations.md) · [P1: API-Aufruf und Weiterverwendung der Antwort prüfen](masterclass/api-response-contract.md) · [P1: Exportvarianten, offene Aufgaben und Abschlussstatus](masterclass/export-lifecycle.md)

## 7. Änderungen und Expertenbetrieb <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln und Sprechertext öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/de.html).

**Ziel:** Einen Workflow ändern, den Sie nicht gebaut haben, und die Änderung wieder zurücknehmen können.

1. Exportieren Sie den Workflow und notieren Sie die Kartenversionen, bevor Sie etwas anfassen.
2. Wiederholen Sie nach der Änderung die Positiv-, Negativ-, Fehler- und Grenzfälle und zusätzlich einen zweiten Lauf desselben Falls.
3. Führen Sie den ersten Fehler auf eine Eingabe und eine Konfiguration zurück und halten Sie den gesicherten Export als Rückweg bereit.

**Abschlusskriterium:** Sie können die Änderung abnehmen, die gesicherte Konfiguration wiederherstellen und einen neuen Beleglauf mit Nachweisen vergleichen. Notieren Sie Ursache, Korrektur und die Grenzen, die bleiben.

**Vertiefung:** [Workflow-Fehler systematisch diagnostizieren](workflow-troubleshooting.md) · [Karten verstehen und zuverlässig konfigurieren](card-reference-standard.md)

## Wissen selbst prüfen

| Frage | Antwort |
| --- | --- |
| Ist `false` bei Field is v2 leer? | Ja. Die Zahl 0 und der Text "false" sind nicht leer. |
| Garantiert ein grüner OR-Test den Beleglauf? | Nein. Im geprüften Fall MERGE-04 wertet ein Test die Zusammenführung aus, die ein Beleglauf überspringt, wenn ein Vorgänger nie ankommt. |
| Kann Run Workflow ein inaktives Ziel aufrufen? | Ja, beim geprüften ausdrücklichen Aufruf. Prüfen Sie trotzdem Zielbedingungen und Ergebnis. |
| Macht HTTP 200 automatisch api.response.cost\_center verfügbar? | Nein. Die geprüften Aktionen bieten diesen automatischen JSON-Ausgabevertrag nicht. |
| Beweist ein grüner Test den Exportempfang? | Nein. Beleglauf, Eingang beim Empfänger und ERP-Verarbeitung brauchen getrennte Nachweise. |

## Festhalten, was Sie abgenommen haben

Laden Sie `workflow-training-kit-v2.zip` aus dem [Workflow-Übungspaket](workflow-training-kit.md) herunter, entpacken Sie es und öffnen Sie `acceptance-record-template.json`. Das ist ein leeres Protokoll und nichts, was Sie importieren; dieselbe ZIP enthält auch die Daten, die Erwartungen und die gespeicherten Testantworten, auf die sich die Stufen beziehen.

Tragen Sie ein, was Sie getestet haben und woran Sie das erkennen: das Szenario, die Konfiguration (Hash des Workflow-Exports, Kartenversionen), Ihre Erwartung, Ihre Beobachtung und welche Art von Nachweis Sie haben. Halten Sie einen Test in Advanced Test, eine isolierte Quellprüfung, einen echten Beleglauf, einen Eingang beim Empfänger und die ERP-Verarbeitung auseinander, und lassen Sie Schritte, die Sie nicht getestet haben, als offen stehen.
