---
description: "Gespeicherte Workflow-Tests anlegen, eine Grenzwert-Regression erkennen und die Korrektur mit vier echten Testläufen bestätigen."
---

# Workflow-Änderungen mit Regressionstests prüfen

Prüfen Sie Änderungen an einem Standard Workflow mit vier gespeicherten Szenarien: einem positiven Fall, dem exakten Grenzwert, einem kleineren Betrag und einer anderen Rechnungsnummer. Thomas zeigt in der deutschen DocBits-Oberfläche, wie eine Änderung von **Größer als** zu **Größer oder gleich** einen vorhandenen Test fehlschlagen lässt und wie nach der Korrektur wieder alle vier Fälle bestehen.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.html) · [Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.vtt) · [Transkript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.txt) · 4:15

## Die vier Testfälle

Die Ausgangsregel prüft den Dokumenttyp **Rechnung**, eine festgelegte Trainings-Rechnungsnummer und einen Gesamtbetrag **größer als 1000 Euro**. Bei einem Treffer setzt sie den Status auf **Genehmigung ausstehend**.

| Fall | Gesamtbetrag | Rechnungsnummer | Erwarteter Status |
| --- | --- | --- | --- |
| Positivfall | 1785 Euro | Trainingsnummer | Genehmigung ausstehend |
| Exakter Grenzwert | 1000 Euro | Trainingsnummer | Bereit zur Validierung |
| Unterhalb der Grenze | 999 Euro | Trainingsnummer | Bereit zur Validierung |
| Andere Rechnung | 1785 Euro | Abweichende Nummer | Bereit zur Validierung |

## Vorgehen im Test Manager

1. Legen Sie für jeden Fall ein eigenes Szenario mit dem gespeicherten Workflow, einer JSON-Eingabe und einer JSON-Erwartung an.
2. Starten Sie die vier Szenarien über das jeweilige Zeilenmenü und laden Sie die gespeicherten Ergebnisse erneut. Im Ausgangszustand bestehen alle vier.
3. Ändern Sie nur den Operator zu **Größer oder gleich** und speichern Sie den Workflow. Lassen Sie die Erwartungen unverändert.
4. Führen Sie dieselben Fälle erneut aus. Der Test mit genau 1000 Euro schlägt fehl; die anderen drei bestehen.
5. Stellen Sie **Größer als** wieder her, speichern Sie und wiederholen Sie alle vier Tests. Prüfen Sie anschließend die erneut geladenen Ergebnisse.

Die Trainingsregel bleibt während dieser Übung ausgeschaltet. Das verhindert eine automatische Ausführung dieser Regel, während die gespeicherten Szenarien manuell getestet werden.

{% hint style="info" %}
**Was „Bestanden“ hier bestätigt:** Der Test Manager vergleicht in diesem Beispiel den erwarteten Dokumentstatus. Weitere Wirkungen wie Benutzerzuweisung, E-Mail oder Export müssen zusätzlich am Dokument beziehungsweise am Zielsystem geprüft werden. Manuelle Tests können tatsächliche Dokumentänderungen auslösen; verwenden Sie eigene Trainingsdokumente.
{% endhint %}

## Eine Regression richtig einordnen

Ein fehlgeschlagener Test bedeutet nicht zwingend, dass eine Aktion technisch abgebrochen ist. Im Video läuft die Statusänderung durch, verletzt aber die unveränderte Erwartung für genau 1000 Euro. Korrigieren Sie die Regel, wenn die fachliche Anforderung gleich geblieben ist. Passen Sie eine Erwartung erst an, wenn die Anforderung tatsächlich geändert wurde.

<details>
<summary>Kapitel und Transkript</summary>

| Kapitel | Start |
| --- | --- |
| Thomas: Tests für Workflow-Änderungen | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=0.000) |
| Die Ausgangsregel prüfen | [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=5.708) |
| Den positiven Test speichern | [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=33.542) |
| Den exakten Grenzwert speichern | [1:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=60.958) |
| Einen Wert unter der Grenze prüfen | [1:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=77.583) |
| Die Begrenzung auf das Trainingsdokument prüfen | [1:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=87.083) |
| Gespeicherte Eingaben wieder öffnen | [1:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=107.917) |
| Den Ausgangszustand bestätigen | [2:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=125.375) |
| Eine kontrollierte Änderung durchführen | [2:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=151.625) |
| Die tatsächliche Regression erkennen | [2:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=169.792) |
| Die Ursache korrigieren | [3:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=204.833) |
| Alle vier Fälle erneut bestehen lassen | [3:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=215.792) |
| Die getestete Regel übergeben | [3:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/de.mp4#t=236.000) |

**Thomas: Tests für Workflow-Änderungen**

Ich ändere einen Workflow und zeige, wie gespeicherte Tests Fehler dabei sichtbar machen.

**Die Ausgangsregel prüfen**

Unsere gespeicherte Trainingsregel verarbeitet Rechnungen mit genau dieser Rechnungsnummer. Der Gesamtbetrag muss größer als tausend sein. Dann setzt sie den Status auf Genehmigung ausstehend. Workflows auslösen steht auf falsch. Während dieser Übung bleibt die Regel in der Liste ausgeschaltet. Ich prüfe heute die Auswirkungen einer Änderung. Dazu brauche ich einen positiven Fall und Fälle, bei denen die Aktion ausbleiben muss.

**Den positiven Test speichern**

Im Test Manager füge ich ein Testszenario hinzu und wähle unsere gespeicherte Regel. Der Name beschreibt Betrag und erwartetes Ergebnis. Ich lade die Eingabe als JSON und eine zweite JSON-Datei mit der Erwartung hoch. Die Trainingsrechnung hat einen Gesamtbetrag von siebzehnhundertfünfundachtzig Euro. Der Ausgangsstatus ist Bereit zur Validierung. Erwartet wird Genehmigung ausstehend. Mit Senden speichere ich diesen ersten Fall.

**Den exakten Grenzwert speichern**

Als Nächstes lege ich den Grenzwertfall an. Dieselbe Rechnungsnummer, aber genau tausend Euro. Größer als tausend schließt genau tausend aus. Deshalb enthält die Erwartung weiterhin Bereit zur Validierung. Ich speichere auch diesen Fall unter einem eigenen Namen.

**Einen Wert unter der Grenze prüfen**

Der dritte Fall verwendet neunhundertneunundneunzig Euro. Er liegt unter der Grenze und erwartet ebenfalls den unveränderten Ausgangsstatus.

**Die Begrenzung auf das Trainingsdokument prüfen**

Der vierte Fall liegt wieder über tausend, verwendet aber eine andere Rechnungsnummer. Der passende Betrag allein darf die Aktion nicht auslösen. Alle vier Szenarien beziehen sich auf ein eigenes synthetisches Trainingsdokument. Manuelle Tests können tatsächliche Dokumentänderungen auslösen; deshalb verwende ich dafür keine laufende Kundenrechnung.

**Gespeicherte Eingaben wieder öffnen**

Über Bearbeiten kann ich Eingabe und Erwartung eines gespeicherten Szenarios wieder öffnen. Hier kontrolliere ich noch einmal Status, Rechnungsnummer und Betrag. Die Erwartung beschreibt die fachliche Regel. Ich ändere sie später nicht einfach mit, nur damit eine geänderte Regel wieder grün wird.

**Den Ausgangszustand bestätigen**

Jetzt starte ich die vier Fälle jeweils über ihr eigenes Menü. So werden genau unsere neuen Szenarien ausgeführt. Anschließend lade ich die Ergebnisse erneut. Alle vier zeigen ein grünes Symbol. Damit haben wir einen bestätigten Ausgangszustand. In diesem Test Manager bezieht sich Bestanden auf den erwarteten Dokumentstatus. Andere Wirkungen, etwa eine Benutzerzuweisung, müssen zusätzlich am Dokument geprüft werden.

**Eine kontrollierte Änderung durchführen**

Nun ändere ich genau einen Operator: Aus Größer als wird Größer oder gleich. Der Betrag bleibt tausend, alle anderen Bedingungen und Aktionen bleiben gleich. Ich speichere die Änderung und kontrolliere wieder, dass die Trainingsregel ausgeschaltet ist. Die gespeicherten Erwartungen lasse ich unverändert.

**Die tatsächliche Regression erkennen**

Ich führe dieselben vier Fälle erneut aus. Jetzt ist genau der Test mit tausend Euro rot; die anderen drei bleiben grün. Die unveränderte Erwartung macht den Unterschied sichtbar, obwohl die Aktionen technisch erfolgreich durchlaufen. Der Detaildialog zeigt den fehlgeschlagenen Test und seine gespeicherten Daten. Die Änderung hat genau tausend in den zutreffenden Bereich aufgenommen, obwohl dieser Fall seinen Ausgangsstatus behalten soll. Ich korrigiere deshalb die Regel. Einen fehlgeschlagenen Test sollte ich erst dann an eine neue Erwartung anpassen, wenn die fachliche Anforderung tatsächlich geändert wurde.

**Die Ursache korrigieren**

Im Workflow stelle ich den Vergleich zurück auf Größer als und speichere. Die Grenze bleibt tausend. Danach schalte ich die Trainingsregel in der Liste wieder aus.

**Alle vier Fälle erneut bestehen lassen**

Nach der Korrektur starte ich alle vier Fälle erneut. Ich prüfe die vollständige Gruppe, weil eine Reparatur auch einen anderen Fall beeinflussen könnte. Nach dem erneuten Laden sind wieder alle vier Ergebnisse grün. Der Grenzwert wird ausgeschlossen, der positive Betrag bleibt eingeschlossen und die andere Rechnungsnummer bleibt außerhalb der Regel.

**Die getestete Regel übergeben**

Zum Schluss kontrolliere ich den ausgeschalteten Trainingsworkflow und die vier gespeicherten Ergebnisse. Die Fälle stehen für die nächste Änderung wieder bereit. Für eigene Regeln ergänze ich gezielt weitere fachliche Grenzen und fehlende Eingaben. So prüfe ich Änderungen mit denselben nachvollziehbaren Erwartungen.

</details>

## Weiterführende Seiten

- [Einen Standard Workflow erstellen und testen](standard-workflow-builder.md#standard-workflow-tutorial)
- [Workflow Dashboard](workflow-dashboard.md)
