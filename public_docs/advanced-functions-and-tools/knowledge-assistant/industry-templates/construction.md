# Knowledge Assistant für Bau, Gebäude und Energie

Finden Sie den Vertragswert, den Nachtrag oder das Zertifikat in der gültigen Fassung, mit der genauen Stelle im Dokument. Das hilft, wenn ein Nachtrag, eine Vertragsstrafe oder ein Einbehalt strittig ist.

<!-- VIDEO: rag/construction/v1/de.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
Die Beispiele auf dieser Seite verwenden **erfundene Demo-Daten**: 30 fiktive Dokumente für diese Branche. Firmennamen, Dokumentnummern und Werte sind ausgedacht.
{% endhint %}

## Was die Vorlage bietet

Ein Administrator schaltet die Vorlage dieser Branche unter **Knowledge Assistant** → **Settings** → **Industry templates** ein. Siehe [Aufgaben und wo Sie sie finden](../tasks-and-where-to-find-them.md#eine-branchenvorlage-einschalten-administrator). Die Karte zeigt dann „On · 3 agents · 3 knowledge bases“.

**Wissensdatenbanken** (in sie laden Sie Ihre Dokumente hoch):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->
* Contracts and change orders
* Site and site diary
* Building and energy certificates

**Assistenten** (Sie wählen einen im Chat):

* Change order and contract checker
* Deadline watch for construction
* Incoming invoice check for construction

Die genauen Namen stehen auf der Vorlagenkarte und im Chat.

## Beispielfragen aus dem Demo-Satz

| Frage | Antwort |
| --- | --- |
| Nenne Mehrmenge und Einheitspreis von Nachtrag NT-2605-7869. | 849,3 m² und 76,03 EUR je m². Quelle: ein gescanntes Nachtragsangebot; ein Klick zeigt die gescannte Seite. |
| Gibt es widersprüchliche Angaben zur Vertragsstrafe je Werktag bei Bauvertrag BV-2611-1818? | Ja: 5,5 ‰ im Original und 7,3 ‰ in der Kopie. Beide Dateien werden genannt und lassen sich öffnen. |
| Ist Energieausweis EA-2604-2072 heute (23.11.2026) noch gültig? | Nein. Der Ausweis war bis 17. März 2025 gültig. |

Sie können auf Deutsch, Englisch oder Französisch fragen. In unseren Tests folgte die Antwort der Sprache der Frage, gleich in welcher Sprache das Dokument geschrieben war.

## Was bei Ihnen bleibt

* **Prüfung:** Jede Antwort nennt ihre Quelle. Öffnen Sie sie und lesen Sie die Stelle, bevor Sie handeln. Steht etwas nicht in Ihren Dokumenten, sagt der Assistent „nicht in den Unterlagen“.
* **Kontrolle:** Die Vorlage ist aus, bis Ihr Administrator sie einschaltet. Beim Ausschalten verschwinden die Assistenten; Ihre Dokumente bleiben.
* **Trennung:** Dokumente und Antworten sind je Organisation getrennt.
* **Entscheidung:** Der Assistent schlägt nach und vergleicht. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er gibt keine Rechtsberatung.

## Am Demo-Satz nicht getestet

Der Abgleich einer Eingangsrechnung mit dem Vertrag wurde am Demo-Satz nicht getestet: Er enthält keine Rechnungen. Die Assistenten beantworten Fragen im Chat; sie prüfen nicht jede eingehende Rechnung automatisch.

Wie gut der Assistent mit Ihren Dokumenten arbeitet, etwa mit langen Verträgen, Handschrift, Stempeln oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten. Siehe [Was er kann und was nicht](../what-it-can-and-cannot-do.md).
