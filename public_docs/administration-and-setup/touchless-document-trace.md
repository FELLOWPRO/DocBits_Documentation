# Touchless Intelligence: Dokumentverlauf

Geben Sie eine Dokument-ID in **Dokument-ID** ein oder öffnen Sie ein Beispieldokument aus einem Cluster, um zu sehen, **was mit genau diesem Dokument passiert ist**.

Die Kopfzeile zeigt die Datei, ihren Status (zum Beispiel **In Bearbeitung**), den Lauf, den Sie gerade ansehen, und dessen ersten Blocker sowie eine Schaltfläche **Dokument** mit der Dokument-ID.

<figure><img src="../.gitbook/assets/touchless-document-trace-pipeline-de.png" alt="Die Seite Dokumentverlauf mit Dateikopfzeile, dem bei der Feldvalidierung gestoppten Verarbeitungspfad und dem Anfang des Schrittprotokolls"><figcaption><p>Der Dokumentverlauf: der Verarbeitungspfad mit allen Schritten und das Schrittprotokoll mit den Angaben, die jeder Schritt aufgezeichnet hat.</p></figcaption></figure>

Der **Verarbeitungspfad** zeigt 14 Schritte: Eingang, Klassifizierung, E-Dokument-Prüfung, Lieferantenerkennung, Texterkennung, Kopfdatenextraktion, Tabellenextraktion, Feldvalidierung, Bestellsuche, Bestellzeilenabgleich, Freigabe, Workflow-Steuerung, Export, ERP-Bestätigung. Jeder Schritt trägt genau einen Zustand:

| Zustand | Bedeutung |
| --- | --- |
| **Bestanden** (grün) | Der Schritt ist fehlerfrei gelaufen |
| **Hier angehalten** (orange) | Der Schritt hat das Dokument blockiert |
| **Als Nächstes** | Das Dokument ist nie so weit gekommen |
| **Nichts erfasst** (gestrichelt) | Für diesen Schritt wurden keine Daten aufgezeichnet |
| **Nicht zutreffend** | Der Schritt gilt für dieses Dokument nicht |

### Schrittprotokoll

Das **Schrittprotokoll** unter dem Pfad listet dieselben Schritte mit dem auf, was jeder von ihnen aufgezeichnet hat. Ein Statuspunkt und das Statuswort stehen links und rechts in jeder Zeile.

* Jeder Wert ist ein **Wert-Chip**: eine Zahl mit ihrer Einheit, zum Beispiel **Konfidenz 100 %**, **Schwellenwert 60 %**, **Fehlgeschlagene Regeln 0**, **8 fehlende Felder** oder **0 Zuordnungslücken**. Prozentwerte erscheinen als `97 %`, nie als `0.97`.
* **Details** öffnet die vollständige Liste der Werte, die ein Schritt aufgezeichnet hat, einschließlich der geprüften Alternativen.
* Der Schritt, der das Dokument blockiert hat, nennt den Grund, zum Beispiel **Feldvalidierung fehlgeschlagen**.
* Ein Wert, den kein Schritt aufgezeichnet hat, erscheint als **Nicht erfasst**, nie als erfundener Wert. Werte sind Zahlen und feste Begriffe, nie Dokumenttext.
* **Rohdiagnose anzeigen** blendet die Rohdaten ein, wenn der Support danach fragt.

<figure><img src="../.gitbook/assets/touchless-document-trace-stage-log-de.png" alt="Das Schrittprotokoll mit bestandenen Schritten, blockierter Feldvalidierung und Einträgen Nicht erfasst"><figcaption><p>Dieses Beispiel stoppt bei der Feldvalidierung. Die Einträge zeigen <strong>Nicht erfasst</strong>: Der Screenshot benennt einen Blocker, beweist aber weder einen Auslesefehler noch falsche Quelldaten.</p></figcaption></figure>

### Läufe und Änderungen

Die Laufauswahl oben im Schrittprotokoll (**Lauf 1 · Aktuell**) wechselt zwischen den Läufen des Dokuments. Die **Laufhistorie** rechts listet jeden Lauf mit seinem Ergebnis und der Stelle auf, an der er stehen geblieben ist. Wenn ein Dokument mehrfach gelaufen ist, wählen Sie in der Auswahl einen Lauf, um ihn mit dem aktuellen zu vergleichen: Die geänderten Werte tragen dann ein Abzeichen mit der Differenz und ihrer Einheit, zum Beispiel **−2 Felder** oder **+3 %**.

Die Karte **Dokument** neben dem Schrittprotokoll nennt Dokumenttyp, Lieferant, Rechnungsnummer, Bestellung, Seitenzahl und ob die Analyse **regelbasiert** ist oder von einer KI geschrieben wurde.

## Auslesung und Quelldaten unterscheiden

1. Öffnen Sie die **Originalrechnung** und vergleichen Sie Kopffelder und Positionen mit der DocBits-Auslesung. Verwenden Sie für einen früheren Lauf die Werte vor einer manuellen Korrektur. Ein heute korrigierter Wert beweist nicht, was ursprünglich ausgelesen wurde.
2. Lesen Sie den ersten Blocker im Dokumentverlauf. Ein bestandener Extraktionsschritt bedeutet, dass der Schritt abgeschlossen wurde; er bestätigt nicht die Richtigkeit jedes Rechnungswertes.
3. Vergleichen Sie bei einer Bestellabweichung die Rechnungswerte mit den **tatsächlich in DocBits verfügbaren Bestelldaten** und dem zugehörigen Infor-Datensatz. Berücksichtigen Sie Einheiten, Preiseinheiten, Mengen und den Importzeitpunkt.
4. Halten Sie den bestätigten Unterschied fest: **Rechnung gegen Auslesung**, **korrekte Auslesung gegen importierte Quelldaten** oder **Infor gegen importierte Kopie**. Fehlen die nötigen Nachweise, bleibt die Ursache offen.
5. Prüfen Sie Laufhistorie und Endergebnis auf manuelle Korrektur, Freigabe oder Neustart. Ergebnis und Ursache beantworten unterschiedliche Fragen.

**Beispiel.** Originalrechnung und ausgelesener Wert enthalten beide 10,00 €, die importierte Bestellung enthält 9,00 €. Damit ist eine Abweichung zu den Bestelldaten nachgewiesen, kein Auslesefehler. Klären Sie den vereinbarten Preis und ob Infor selbst oder die importierte Kopie korrigiert werden muss. Startet AP die Rechnung manuell neu und wird sie anschließend erfolgreich abgeschlossen, zählt sie trotz korrekter Auslesung als „AP mit Eingriff“. Siehe [Beispiele und Berechnung](touchless-intelligence.md).

**Wiederholt fehlende Felder.** Mehrere Stopps bei der Feldvalidierung belegen einen wiederkehrenden Blocker. Mögliche Ursachen sind Extraktion, ein tatsächlich fehlender Rechnungswert, eine Validierungsregel oder ein fehlender konfigurierter Standardwert. Vergleichen Sie die Nachweise vor einer Änderung; die Wiederholung allein beweist keine dieser Ursachen.

## Weiterführende Seiten

* [Touchless Intelligence](touchless-intelligence.md)
* [Lieferantendiagnose und Fehlermuster](touchless-supplier-diagnosis.md)
* [Bestellabgleich-Diagnose](touchless-po-matching-diagnosis.md)

Die Screenshots auf dieser Seite zeigen die deutsche Benutzeroberfläche.

<!-- Doku-Prüfung 04.11.2026: Auslesequalität getrennt von Prozessergebnissen; Kennzahlen und Endergebnisse gegen DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py und bucket.py, geprüft. Bestehende deutsche Originalaufnahmen getrennt von den Schulungsbeispielen geprüft. -->
