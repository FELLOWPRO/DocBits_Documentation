# Qualitätsstandard und Abnahme

**Stand:** 27.10.2026 · **Academy-Version:** 1.0

Ein Tutorial ist erst fertig, wenn ein fachlicher Anwender den beschriebenen Vorgang in einer DocBits-Testumgebung mit den bereitgestellten Unterlagen selbständig erfolgreich durchführen kann. Ein vorbereiteter Text, eine richtige Beispielsummenberechnung oder ein vorhandenes Video ersetzt diese Abnahme nicht.

## Checkliste je Tutorial

- [ ] Geschäftsproblem, Zielgruppe, Voraussetzungen und Lernziel verständlich
- [ ] Herunterladbares synthetisches oder anonymisiertes Beispieldokument vorhanden
- [ ] Schritte und UI-Bezeichnungen gegen die tatsächlich getestete Version geprüft
- [ ] Screenshots zeigen die tatsächliche Oberfläche und den jeweiligen neuen Übungsfall
- [ ] Kurzes Video des Falls mit geprüften Untertiteln vorhanden
- [ ] Sollwerte und nachvollziehbare Ergebnisprüfungen vorhanden
- [ ] Mindestens ein realistischer Fehlerfall tatsächlich ausgeführt
- [ ] Bestehende Funktionsanleitung verlinkt
- [ ] Produktversion, Aktualisierungsdatum und Medienversion dokumentiert
- [ ] DocBits Key User hat den Fall selbständig erfolgreich ausgeführt
- [ ] Bei ERP-Fällen: fachliche Antwort, genau ein Zielbeleg und relevante Zielpositionen geprüft

## Veröffentlichung in Etappen

| Phase | Umfang | Voraussetzung für Veröffentlichung |
| --- | --- | --- |
| 1 – Grundlagen | Tutorials 1, 2 und 6 samt Testrechnungen | Import, Korrektur, PO-Fälle und Tabellen vollständig abgenommen; erforderliche ERP-Schritte bestätigt |
| 2 – Automatisierung | Tutorials 3 und 4 mit Beispielkonfigurationen | Automatik getrennt von manueller Kontierung bestätigt; beide Freigaben, Grenzfälle und Sperren geprüft |
| 3 – Betrieb | Tutorial 5 | Eigener reproduzierter Testfehler, geprüfte Korrektur, Retry und Dublettenprüfung belegt |
| 4 – Erweiterung | Weitere Tabellenfälle, XRechnung, ZUGFeRD, Lieferantenportal, E-Mail-Import und Advanced Workflows | Je eigener Fall, Medien und fachliche Abnahme |

## Abnahmeprotokoll

| Nachweis | Einzutragen |
| --- | --- |
| Tutorial und Paketversion | Titel, 1.0, Dateiprüfsummen |
| Umgebung und Version | Tatsächliche URL, Organisation, Releasekanal und angezeigte Version |
| Rolle | Fachliche Testrolle und erforderliche Berechtigungen |
| Testdokument | Dokument-ID und eindeutige Rechnungsnummer |
| Durchführung | Schritte, Soll-/Ist-Werte, Fehlerfall und erneute Prüfung |
| Medien | Passende Screenshot-/Videoversion und geprüfte Untertitel |
| ERP-Ergebnis | Ziel, fachliche Antwort, eindeutiger Zielbeleg und Positionsvergleich |
| Fachliche Abnahme | Datum, Key-User-Rolle, bestanden oder konkrete offene Abweichung |

Veröffentlichen Sie keine Zugangsdaten oder internen Protokolle. Ein Produktfehler und ein Fehler der Anleitung müssen getrennt beschrieben werden. Nach einer verifizierten Korrektur gehören Ursache und die wichtigste Verbesserung in die kurze Retrospektive.

[Academy](README.md)
