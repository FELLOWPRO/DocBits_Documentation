# Knowledge Assistant für Maschinen- und Anlagenbau

Ihr Serviceteam beantwortet jede Frage zu Wartung, Ersatzteilen und Lieferanten aus dem gültigen Dokument, mit der Quelle im Blick. So fährt kein Techniker mit dem falschen Teil oder einem überholten Plan los.

<!-- VIDEO: rag/mechanical-engineering/v1/de.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
Die Beispiele auf dieser Seite verwenden **erfundene Demo-Daten**: 30 fiktive Dokumente für diese Branche. Firmennamen, Dokumentnummern und Werte sind ausgedacht.
{% endhint %}

## Was die Vorlage bietet

Ein Administrator schaltet die Vorlage dieser Branche unter **Knowledge Assistant** → **Settings** → **Industry templates** ein. Siehe [Aufgaben und wo Sie sie finden](../tasks-and-where-to-find-them.md#eine-branchenvorlage-einschalten-administrator). Die Karte zeigt dann „On · 3 agents · 3 knowledge bases“.

**Wissensdatenbanken** (in sie laden Sie Ihre Dokumente hoch):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->
* Documentation
* Service and spare parts
* Suppliers

**Assistenten** (Sie wählen einen im Chat):

* Conformity assistant for the machinery regulation
* Service assistant for spare parts and faults
* Weekly deadline and certificate overview

Die genauen Namen stehen auf der Vorlagenkarte und im Chat.

## Beispielfragen aus dem Demo-Satz

| Frage | Antwort |
| --- | --- |
| Gibt es widersprüchliche Angaben zur Lieferzeit bei Ersatzteil ET-2607-2048? | 18 Tage in der Original-Teileliste und 3 Tage in der Kopie. Ein Klick auf die Quelle öffnet das Dokument an dieser Stelle. |
| Ist Vereinbarung QS-2603-4841 heute (23.11.2026) noch gültig? | Nein. Sie war bis 25. März 2025 gültig. |
| Welches Wartungsintervall gilt aktuell für Plan WP-2603-6421? (auf Englisch gefragt) | 2.521 Betriebsstunden laut Version 2; Version 1 mit 4.055 wurde ersetzt. Die Antwort kommt auf Englisch. |

Sie können auf Deutsch, Englisch oder Französisch fragen. In unseren Tests folgte die Antwort der Sprache der Frage, gleich in welcher Sprache das Dokument geschrieben war.

## Was bei Ihnen bleibt

* **Prüfung:** Jede Antwort nennt ihre Quelle. Öffnen Sie sie und lesen Sie die Stelle, bevor Sie handeln. Steht etwas nicht in Ihren Dokumenten, sagt der Assistent „nicht in den Unterlagen“.
* **Kontrolle:** Die Vorlage ist aus, bis Ihr Administrator sie einschaltet. Beim Ausschalten verschwinden die Assistenten; Ihre Dokumente bleiben.
* **Trennung:** Dokumente und Antworten sind je Organisation getrennt.
* **Entscheidung:** Der Assistent schlägt nach und vergleicht. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er gibt keine Rechtsberatung.

## Am Demo-Satz nicht getestet

Der Assistent liest nur Text. Zeichnungen und Bildinhalte versteht er nicht. Er gibt keine Konformität frei und ersetzt keine technische oder rechtliche Prüfung.

Wie gut der Assistent mit Ihren Dokumenten arbeitet, etwa mit langen Verträgen, Handschrift, Stempeln oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten. Siehe [Was er kann und was nicht](../what-it-can-and-cannot-do.md).
