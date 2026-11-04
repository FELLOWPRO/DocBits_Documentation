# Touchless Intelligence: Dokumentverlauf

<!-- touchless-admin-video-v2-20261104:start -->
**Video-Kapitel (Prüffassung):** [Läufe vergleichen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/de.html#chapter=08).
<!-- touchless-admin-video-v2-20261104:end -->

Geben Sie eine Dokument-ID in **Dokument-ID** ein oder öffnen Sie ein Beispieldokument aus einem Cluster, um zu sehen, **was mit genau diesem Dokument passiert ist**.

Die Kopfzeile zeigt die Datei, ihren Status (zum Beispiel **In Bearbeitung**), den Lauf, den Sie gerade ansehen, und dessen ersten Blocker sowie eine Schaltfläche **Dokument** mit der Dokument-ID.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-de.png" alt="Dev NOVA: Verarbeitungspfad und echte aufgezeichnete Werte des ersten Testlaufs"><figcaption><p>Neu aufgenommen auf Dev NOVA 11.0.3 am 4. November 2026: Der fiktive Testbeleg stoppt bei der Feldvalidierung. Klassifizierung, Lieferantensuche, Kopfdaten- und Tabellenextraktion enthalten tatsächlich aufgezeichnete Werte. Die Karten rechts zeigen Dokument und Laufhistorie. Dies ist eine laufende Produktoberfläche.</p></figcaption></figure>

Der **Verarbeitungspfad** zeigt 14 Schritte: Eingang, Klassifizierung, E-Dokument-Prüfung, Lieferantenerkennung, Texterkennung, Kopfdatenextraktion, Tabellenextraktion, Feldvalidierung, Bestellsuche, Bestellzeilenabgleich, Freigabe, Workflow-Steuerung, Export, ERP-Bestätigung. Jeder Schritt trägt genau einen Zustand:

| Zustand | Bedeutung |
| --- | --- |
| **Bestanden** (grün) | Der Schritt ist fehlerfrei gelaufen |
| **Hier angehalten** (orange) | Der Schritt hat das Dokument blockiert |
| **Als Nächstes** | Im Verarbeitungspfad als nachfolgender Schritt dargestellt; zusätzliche Einträge im Schrittprotokoll prüfen |
| **Nichts erfasst** (gestrichelt) | Für diesen Schritt wurden keine Daten aufgezeichnet |
| **Nicht zutreffend** | Der Schritt gilt für dieses Dokument nicht |

### Schrittprotokoll

Das **Schrittprotokoll** unter dem Pfad listet dieselben Schritte mit dem auf, was jeder von ihnen aufgezeichnet hat. Ein Statuspunkt und das Statuswort stehen links und rechts in jeder Zeile.

* Jeder Wert ist ein **Wert-Chip**: eine Zahl mit ihrer Einheit, zum Beispiel **Konfidenz 100 %**, **Schwellenwert 60 %**, **Fehlgeschlagene Regeln 0**, **8 fehlende Felder** oder **0 Zuordnungslücken**. Prozentwerte erscheinen als `97 %`, nie als `0.97`.
* **Details** öffnet die vollständige Liste der Werte, die ein Schritt aufgezeichnet hat, einschließlich der geprüften Alternativen.
* Der Schritt, der das Dokument blockiert hat, nennt den Grund, zum Beispiel **Feldvalidierung fehlgeschlagen**.
* Ein Wert, den kein Schritt aufgezeichnet hat, erscheint als **Nicht erfasst**, nie als erfundener Wert. Werte sind Zahlen und feste Begriffe, nie Dokumenttext.
* **Rohdiagnose anzeigen** blendet die Rohdaten ein, wenn der Support danach fragt.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-de.png" alt="Dev NOVA: Schrittprotokoll mit Konfidenz, Extraktionswerten und blockierter Feldvalidierung"><figcaption><p>Echter erster Lauf: 100 % Klassifizierungskonfidenz, 0 Lieferantenkandidaten, 1 Tabellenzeile und 7 Zuordnungslücken. Bestanden bedeutet, dass ein Schritt ausgeführt wurde; es bestätigt weder eine Lieferantenzuordnung noch die Richtigkeit aller Rechnungswerte. Die Feldvalidierung meldet ein fehlendes Pflichtfeld.</p></figcaption></figure>

### Läufe und Änderungen

Die Laufauswahl oben im Schrittprotokoll (**Lauf 1 · Aktuell**) wechselt zwischen den Läufen des Dokuments. Die **Laufhistorie** rechts listet jeden Lauf mit seinem Ergebnis und der Stelle auf, an der er stehen geblieben ist. Wenn ein Dokument mehrfach gelaufen ist, wählen Sie den gewünschten Lauf. Vorhandene Änderungen beziehen sich auf seinen vorherigen Lauf: Die geänderten Werte tragen dann ein Abzeichen mit der Differenz und ihrer Einheit, zum Beispiel **−2 Felder** oder **+3 %**.

Die Karte **Dokument** neben dem Schrittprotokoll nennt Dokumenttyp, Lieferant, Rechnungsnummer, Bestellung, Seitenzahl und die aufgezeichnete Analysemethode. Im Beispiel steht dort **Manuell**, weil der Dokumenttyp beim Testimport vorgegeben wurde; die 100 % sind daher kein unabhängiger Nachweis einer automatischen Klassifizierung.

### Lieferanten- und Tabellendetails lesen

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-de.png" alt="Dev NOVA: Lieferantendetails unterscheiden gefundene Kennungen, Stammdatensuche und Zuordnung"><figcaption><p>Der echte Testlauf findet den Namen auf der Rechnung und sucht ihn in den Stammdaten, ordnet aber keinen Lieferanten zu. USt-ID, IBAN, E-Mail und GLN stehen nicht auf diesem Testbeleg. Ein fehlender Stammdatentreffer ist eine andere Diagnose als ein nicht gefundener Rechnungswert.</p></figcaption></figure>

Prüfen Sie die drei Fragen getrennt: Ist die Kennung auf dem Dokument vorhanden? Wurde sie gesucht? Gab es eine Zuordnung? Ein grüner Schritt allein beantwortet diese Fragen nicht.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-de.png" alt="Dev NOVA: Tabellendetails des ersten Laufs mit sieben gemeldeten Zuordnungslücken"><figcaption><p>Die Tabellendetails melden 7 Zuordnungslücken bei 1 Tabelle und 1 Zeile. Prüfen Sie die Spaltenzuordnung, bevor Sie einen Auslesefehler annehmen. Die Oberfläche zeigt im ersten Lauf noch „Keine Änderung seit Lauf 0“; für den ersten Lauf gibt es keinen früheren Lauf als Vergleichsbasis.</p></figcaption></figure>

### Einen echten Neustart erkennen

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-de.png" alt="Dev NOVA: Vergleichstabelle der beiden tatsächlichen Testläufe ohne geänderte Schrittwerte"><figcaption><p>Derselbe Testbeleg nach einem tatsächlich ausgelösten manuellen Neustart. Es wurden keine Rechnungsfelder korrigiert. Die neue Laufnummer belegt einen weiteren Versuch, keine erfolgreiche Verbesserung. Unveränderte Werte erzeugen keine erfundenen Differenz-Abzeichen.</p></figcaption></figure>

Der Neustart ist ein menschlicher Eingriff. Erst ein später erfolgreich abgeschlossener Beleg würde in diesem Fall als **AP mit Eingriff** zählen; solange er noch in Bearbeitung ist, gehört er nicht in den Nenner der Abschlussquote.

**Grenzen dieses Nachweises.** Dieser Testfall zeigt keine fachliche Freigabe, keinen erfolgreichen Export und keine ERP-Bestätigung. Der PO-Bereich enthält keinen aufgezeichneten Entscheidungsweg des Legacy-Matchers. Er beweist keinen Infor-Abgleich. In NOVA 11.0.3 sind zudem nicht alle Anzeigen konsistent: Das Schrittprotokoll kann nach der blockierten Feldvalidierung noch einen bestandenen Bestellsuchschritt enthalten, während der Pfad ihn als „Als Nächstes“ zeigt. Prüfen Sie beide Ansichten. Die Dokumentkarte zeigt die Rechnungsnummer hier als „Nicht erfasst“, obwohl sie im Extraktionsergebnis vorhanden ist; sie ersetzt deshalb nicht den Original- und Feldvergleich.

## Original und ursprüngliche Auslesung nachweisen

<figure><img src="../.gitbook/assets/touchless-original-field-comparison-de.png" alt="Deutsche Validierungsansicht mit Rechnungsnummer DB20261042 links und derselben Nummer im Originalbeleg rechts"><figcaption><p>Original und aktuelles Feld nebeneinander: Die Nummer DB20261042 ist rechts im synthetischen Beleg markiert und links dem Rechnungsnummernfeld zugeordnet. Die Aufnahme erklärt den Wertevergleich, belegt aber weder den ursprünglichen Extraktionswert vor einer Bearbeitung noch einen Infor-Abgleich oder den erfolgreichen Abschluss des Dokuments. Der rote Feldhinweis muss zusätzlich geprüft werden.</p></figcaption></figure>

1. Öffnen Sie den Verlauf desselben Dokuments und notieren Sie den betrachteten Lauf. Über **Dokument** öffnen Sie die zugehörige Rechnung; vergleichen Sie die Dokument-ID, bevor Sie Werte übernehmen.
2. Prüfen Sie im Original mindestens Bestellnummer, Währung, Menge, Einheit, Preiseinheit, Stückpreis und Positionsbetrag sowie die relevanten Kopfsummen. Vergleichen Sie dazu die Felder und Positionen der Validierungsansicht.
3. Unterscheiden Sie den **aktuell angezeigten Wert** von der **ursprünglichen Auslesung vor einer Korrektur**. Bei bereits bearbeiteten Rechnungen benötigen Sie einen passenden historischen Nachweis, etwa eine vorhandene Feldhistorie oder einen vom Support bereitgestellten Extraktionsnachweis dieses Laufs.
4. Der Wechsel zwischen Läufen zeigt aufgezeichnete Schritte und Kennzahlen. Er ist keine Zusicherung, dass jedes alte Feld und jede Tabellenzelle als vollständiger Wertestand wiederhergestellt wird. Fehlt der ursprüngliche Wert, notieren Sie „Auslesequalität für diesen Wert nicht nachgewiesen“.
5. Halten Sie für die Quellseite zusätzlich die tatsächlich importierten Bestellwerte, den Importzeitpunkt und den aktuellen Infor-Stand fest. Nur so lässt sich eine falsche Quelle von einer veralteten Kopie unterscheiden.

| Prüfpunkt des Schulungsfalls | Original | Auslesung vor Korrektur | Importierte Bestellung | Befund |
| --- | --- | --- | --- | --- |
| Menge | 10 Stück | 10 Stück | 10 Stück | Übereinstimmung |
| Stückpreis | 10,00 € | 10,00 € | 9,00 € | Auslesung korrekt; Abweichung zu den Bestelldaten |
| Positionsbetrag | 100,00 € | 100,00 € | 90,00 € | Gleiche Abweichung, kein zusätzlicher Beweis für ihre Ursache |

Die Tabelle ist ein Lesebeispiel. Die Verlaufsscreenshots zeigen native Bedienelemente und aufgezeichnete Schritte; sie belegen diese Preiswerte nicht. Eine Konfidenz von 100 % oder ein grüner Extraktionsschritt ersetzt den Vergleich nicht. Siehe auch die [Validierungsansicht](../end-user-and-partner-section/end-user-section/validation-screen/README.md).

### Auslesequalität einer Stichprobe festhalten

Legen Sie vor der Prüfung fest, welche Felder und Positionen beurteilt werden. Eine Rechnung gilt in einer Prüfung nur dann als vollständig korrekt, wenn alle vorgesehenen, nachweisbaren Werte stimmen. Fehlende historische Nachweise separat als nicht beurteilbar ausweisen; sie sind kein bestätigter Erfolg. Dokumentieren Sie Stichprobengröße, Auswahl, betrachteten Lauf und Prüfumfang. Das Ergebnis dieser Prüfung bleibt getrennt von der Touchless-Quote.

## Auslesung und Quelldaten unterscheiden

1. Öffnen Sie die **Originalrechnung** und vergleichen Sie Kopffelder und Positionen mit der DocBits-Auslesung. Verwenden Sie für einen früheren Lauf die Werte vor einer manuellen Korrektur. Ein heute korrigierter Wert beweist nicht, was ursprünglich ausgelesen wurde.
2. Lesen Sie den ersten Blocker im Dokumentverlauf. Ein bestandener Extraktionsschritt bedeutet, dass der Schritt abgeschlossen wurde; er bestätigt nicht die Richtigkeit jedes Rechnungswertes.
3. Vergleichen Sie bei einer Bestellabweichung die Rechnungswerte mit den **tatsächlich in DocBits verfügbaren Bestelldaten** und dem zugehörigen Infor-Datensatz. Berücksichtigen Sie Einheiten, Preiseinheiten, Mengen und den Importzeitpunkt.
4. Halten Sie den bestätigten Unterschied fest: **Rechnung gegen Auslesung**, **korrekte Auslesung gegen importierte Quelldaten** oder **Infor gegen importierte Kopie**. Fehlen die nötigen Nachweise, bleibt die Ursache offen.
5. Prüfen Sie Laufhistorie und Endergebnis auf manuelle Korrektur, Freigabe oder Neustart. Ergebnis und Ursache beantworten unterschiedliche Fragen.

**Beispiel.** Originalrechnung und ausgelesener Wert enthalten beide 10,00 €, die importierte Bestellung enthält 9,00 €. Damit ist eine Abweichung zu den Bestelldaten nachgewiesen, kein Auslesefehler. Klären Sie den vereinbarten Preis und ob Infor selbst oder die importierte Kopie korrigiert werden muss. Startet AP die Rechnung manuell neu und wird sie anschließend erfolgreich abgeschlossen, zählt sie trotz korrekter Auslesung als „AP mit Eingriff“. Siehe [Beispiele und Berechnung](touchless-intelligence.md).

**Wiederholt fehlende Felder.** Mehrere Stopps bei der Feldvalidierung belegen einen wiederkehrenden Blocker. Mögliche Ursachen sind Extraktion, ein tatsächlich fehlender Rechnungswert, eine Validierungsregel oder ein fehlender konfigurierter Standardwert. Vergleichen Sie die Nachweise vor einer Änderung; die Wiederholung allein beweist keine dieser Ursachen.

## Mehrere Blocker bei derselben Rechnung

Das folgende Beispiel beschreibt einen möglichen Verlauf, nicht die einzelnen Läufe der Screenshots:

| Zeitpunkt / Lauf | Was sichtbar wird | Was daraus folgt |
| --- | --- | --- |
| Lauf 1 | Bestellnummer richtig ausgelesen, Bestellung noch nicht importiert | Erster Blocker dieses Laufs: Bestellsuche. Noch kein Beweis für einen Auslesefehler |
| Nach dem Import, Lauf 2 | Die Bestellung ist vorhanden; jetzt fällt die Preisabweichung 10,00 € gegen 9,00 € auf | Der spätere Blocker wird erst nach Behebung des früheren sichtbar. Er beweist nicht, dass Lauf 1 dieselbe Prüfung erreicht hat |
| AP klärt und startet nach korrigiertem Import manuell neu | Der nächste Lauf kann Abgleich und Export erfolgreich beenden | Bei erfolgreichem Endergebnis: AP mit Eingriff. Der manuelle Neustart bleibt dokumentiert |
| Alternative: ERP weist den Export endgültig zurück | Die Übermittlung allein war noch kein bestätigter Erfolg | Prozessausnahme, auch wenn AP vorher eingegriffen hat |

Wählen Sie die Läufe nacheinander und vergleichen Sie **ersten Blocker**, aufgezeichnete Details und Laufresultat. Prüfen Sie danach das **Dokumentergebnis**. Ein später bestandener Schritt löscht weder den früheren Blocker noch die menschliche Bearbeitung. **Nicht erfasst** bedeutet fehlender Nachweis, nicht bestanden.

Die zugehörigen MCP-Aufrufe und die Einordnung menschlicher Aktionen sind unter [Touchless mit MCP](touchless-mcp.md) beschrieben.

## Weiterführende Seiten

* [Touchless Intelligence](touchless-intelligence.md)
* [Lieferantendiagnose und Fehlermuster](touchless-supplier-diagnosis.md)
* [Bestellabgleich-Diagnose](touchless-po-matching-diagnosis.md)

Die fünf neuen Verlaufsscreenshots zeigen die deutsche Oberfläche von Dev NOVA 11.0.3 und denselben eigens angelegten Testbeleg. Die separate Validierungsaufnahme dient weiterhin nur dem Vergleich von Original und angezeigtem Feld.

<!-- Doku-Prüfung 04.11.2026: Auslesequalität getrennt von Prozessergebnissen; Kennzahlen und Endergebnisse gegen DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py und bucket.py, geprüft. Bestehende deutsche Originalaufnahmen getrennt von den Schulungsbeispielen geprüft. -->

<!-- Completion review 2026-11-04: AP actions, original-value evidence, overlapping KPI labels, sequential blockers and screenshot proof limits checked. -->
