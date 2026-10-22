---
description: "Workflow-Probleme anhand von Ausführungsanlass, Eingabedaten, gewähltem Weg und tatsächlichem Ergebnis eingrenzen."
---

# Workflow-Fehler systematisch diagnostizieren

Beginnen Sie mit genau einem betroffenen Lauf. Notieren Sie Organisation und Umgebung, Workflow-Name und gespeicherten Stand, Dokumentreferenz, Zeitpunkt und Zeitzone sowie die genaue Knotenmeldung. In Testantworten hilft zusätzlich die `execution_id`. Zugangsschlüssel und ungeschützte Kundendaten gehören nicht in geteilte Nachweise.

## Vom Symptom zur Prüfung

| Symptom | Beleg suchen | Korrektur und Nachtest |
| --- | --- | --- |
| Kein Lauf vorhanden | Lizenz, Modul, Aktivzustand, Zeitraumfilter und passender Ausführungsanlass | Einstieg und Filter korrigieren; den tatsächlichen Anlass erneut auslösen. Ein manueller Start beweist diesen nicht. |
| Aktion bleibt grau | Ergebnis des Vorgängers und verbundener Ausgang | Den tatsächlich genommenen Weg verfolgen. Ein übersprungener Knoten ist nicht selbst fehlgeschlagen. |
| Bedingung orange | Gelesener Feldschlüssel, Datentyp, Wert und Vergleichsoperator | Negativfall von Auswertungsfehler unterscheiden. Unter, an und über der Grenze erneut testen. |
| Bedingung oder Aktion rot | Erste Fehlermeldung und notwendige Eingabedaten | Daten oder Konfiguration korrigieren; ursprünglichen Fehlerfall und Erfolgsfall wiederholen. |
| Wait ALL erreicht keine Folgeaktion | Jede Quelle und genau der angeschlossene Ergebnisausgang | Gegenseitig ausschließende Routen nicht als gemeinsame Pflicht behandeln. Für jede erforderliche Quelle einen erfüllbaren Weg nachweisen. |
| Doppelte Aufgaben oder Exporte | Mehrere Läufe, Ereignisse, Statusänderungen und Run-Workflow-Aufrufe | Auslösebedingungen und Zustandsübergänge begrenzen; denselben Fall zweimal testen. Bei gleichzeitigen Aufrufen einen geeigneten Schutz im Zielprozess prüfen. |
| Ein Variablenwert beeinflusst andere Workflows | Gemeinsam verwendete Organisationsvariable | Abhängigkeiten prüfen. Änderungen werden unabhängig vom Canvas gespeichert; betroffene Workflows erneut testen. |
| Test bestanden, Wirkung fehlt | Was wurde tatsächlich verglichen oder simuliert? | Zuweisung am Dokument, Aufgabe im Aufgabenbereich und Empfang beim Ziel prüfen. Ein erwarteter Status allein reicht nicht. |
| Export gestartet, Empfänger hat nichts | Exportverlauf, Antwort und Empfängerdaten | Fehler vor erneutem Versand eingrenzen; prüfen, ob der Empfänger die erste Anfrage bereits verarbeitet hat. |

## Eine Meldung richtig lesen

Im [Advanced-Beispiel](advanced-workflow-case-study.md) führt ein fehlender Betrag über Rot zur Datenkorrektur. Der Fehlerhandler und die OR-Zusammenführung können anschließend erfolgreich sein. Der Gesamtlauf bleibt fehlerhaft, weil die Betragsauswertung einen Fehler hatte. Eine gewöhnlich falsche Betragsbedingung nimmt dagegen Orange und kann mit der Standardroute erfolgreich enden.

Zwei Linien von derselben Quelle sind keine zwei unabhängigen Freigaben. Bei Zusammenführungen zählen die verbundenen Ergebnisse der Quellen. Prüfen Sie den ganzen Ablauf; ein Teiltest ab einem mittleren Knoten kann die erforderlichen Vorgänger auslassen.

## Korrektur belegen

1. Sichern Sie den ursprünglichen Befund und die fachliche Erwartung.
2. Ändern Sie gezielt Daten oder Konfiguration. Passen Sie die Erwartung nur an, wenn sich die Anforderung geändert hat.
3. Wiederholen Sie Fehlerfall, Positivfall und betroffene Grenzfälle mit dem [Übungspaket](workflow-training-kit.md).
4. Speichern Sie die korrigierte Regel und prüfen Sie den Aktivzustand separat.
5. Vergleichen Sie einen neuen echten Lauf mit dem alten. Alte Protokolle bleiben Nachweise ihres damaligen Stands.

Notieren Sie abschließend Ursache, Korrektur, nachgewiesenes Ergebnis und verbleibende Einschränkungen. Trennen Sie Wartezeit und Ausführungszeit; eine lange Gesamtdauer allein belegt keinen langsamen Einzelknoten.

## WF-04: Übung und Abnahme

Starten Sie mit invalid-number. Sichern Sie die erste Fehlermeldung von amount und den Gesamtausgang error. Wiederholen Sie mit above und vergleichen Sie die neuen Ergebnisse. Das alte Fehlerprotokoll bleibt erhalten; eine erfolgreiche Fehlerbehandlung allein genügt nicht.

[Lernweg](workflow-learning-path.md)

## Einzelkartentests gezielt wiederholen

Im geprüften Dev-Designer wechselte „Erneuter Test“ nach „Test von diesem Knoten“ zum gesamten Graphen. Öffnen Sie den Kontextmenütest der gewünschten Karte erneut und prüfen Sie die tatsächlich besuchten Knoten. Ein Ergebnis mit sechs Knoten belegt nicht den Test einer einzelnen Leerprüfkarte. Ein Zähler für gescheiterte Aktionen kann auch eine nicht erfüllte Bedingung enthalten: Lesen Sie zusätzlich Kartenausgang, Logmeldung und Gesamtergebnis.

## Beobachtete Meldungen gezielt einordnen

Der [Meldungskatalog](workflow-error-catalog.md) verbindet tatsächliche Meldungen mit Eingabe, Konfiguration und Nachtest. Vergleichen Sie Knotenpfad und Gesamtergebnis getrennt. Für einen neuen Dokumentlauf verwenden Sie den [Leitfaden zur kontrollierten Aktivierung](workflow-go-live.md); für Änderungen den [gesicherten Wiederherstellungsablauf](workflow-change-and-recovery.md).
