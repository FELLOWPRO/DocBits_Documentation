# Wissensassistent für Chemie

Bevor jemand nach einer alten Fassung, einem widersprüchlichen Zertifikat oder einer abgelaufenen Spezifikation handelt, zeigt eine Frage, welcher Wert gilt und wo er steht.

<!-- VIDEO: rag/chemicals/v1/de.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
Die Beispiele auf dieser Seite verwenden **erfundene Demo-Daten**: 30 fiktive Dokumente für diese Branche. Firmennamen, Dokumentnummern und Werte sind ausgedacht.
{% endhint %}

## Was die Vorlage bietet

Ein Administrator schaltet die Vorlage dieser Branche unter **Wissensassistent** → **Einstellungen** → **Branchenvorlagen** ein. Siehe [Aufgaben und wo Sie sie finden](../tasks-and-where-to-find-them.md#eine-branchenvorlage-einschalten-administrator). Die Karte zeigt dann „An“ und „3 Agenten · 3 Wissensbasen“.

**Wissensdatenbanken** (in sie laden Sie Ihre Dokumente hoch):

* Sicherheitsdatenblätter und Stoffdaten
* Chargen und Zertifikate
* Compliance und Fristen

**Assistenten** (Sie wählen einen unter **Eigene Agenten** im Chat):

* SDB-Prüfer
* Rechnungsabgleich Chemie
* Wochenbericht Fristen und Zertifikate

Die Namen und Beschreibungen kommen mit der Vorlage. Dieselben Namen erscheinen unter **Wissensdatenbank** und in der Agentenauswahl im Chat.

## Beispielfragen aus dem Demo-Satz

| Frage | Antwort |
| --- | --- |
| Welcher Wert gilt aktuell für Mengenschwelle bei Prüfbericht PB-2601-4654? | 161 t laut Version 2. Version 1 nannte 285 t und gilt nicht mehr. Beide Dateien sind verlinkt. |
| Gibt es widersprüchliche Angaben zum Wassergehalt bei Charge CH-2601-6586? | Ja: 0,93 % im Original und 1,36 % in der Kopie, jeweils mit Dateinamen. |
| Ist Spezifikation SP-2601-6995 heute (23.11.2026) noch gültig? | Nein. Das Dokument nennt „gültig bis 27.05.2025“. |

Sie können auf Deutsch, Englisch oder Französisch fragen. In unseren Tests folgte die Antwort der Sprache der Frage, gleich in welcher Sprache das Dokument geschrieben war.

## Was bei Ihnen bleibt

* **Prüfung:** Jede Antwort nennt ihre Quelle. Öffnen Sie sie und lesen Sie die Stelle, bevor Sie handeln. Steht etwas nicht in Ihren Dokumenten, sagt der Assistent „nicht in den Unterlagen“.
* **Kontrolle:** Die Vorlage ist aus, bis Ihr Administrator sie einschaltet. Beim Ausschalten verschwinden die Assistenten; Ihre Dokumente bleiben.
* **Trennung:** Dokumente und Antworten sind je Organisation getrennt.
* **Entscheidung:** Der Assistent schlägt nach und vergleicht. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er gibt keine Rechtsberatung.

## Am Demo-Satz nicht getestet

Der Rechnungsabgleich und das abschnittsweise Lesen von Sicherheitsdatenblättern (Abschnitte 1 bis 16) wurden am Demo-Satz nicht getestet. Der Assistent ist eine Nachschlagehilfe: Er ersetzt weder das Sicherheitsdatenblatt noch eine Gefährdungsbeurteilung und gibt keine Rechtsberatung.

Wie gut der Assistent mit Ihren Dokumenten arbeitet, etwa mit langen Verträgen, Handschrift, Stempeln oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten. Siehe [Was er kann und was nicht](../what-it-can-and-cannot-do.md).
