# Knowledge Assistant für Elektro und Industriegüter

Bevor ein Zeugnis an Ihren Kunden geht oder Sie eine Garantieleistung zusagen, zeigt eine Antwort, welche Fassung gilt, ob das Dokument abgelaufen ist und ob zwei Kopien einander widersprechen.

<!-- VIDEO: rag/electrical/v1/de.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
Die Beispiele auf dieser Seite verwenden **erfundene Demo-Daten**: 30 fiktive Dokumente für diese Branche. Firmennamen, Dokumentnummern und Werte sind ausgedacht.
{% endhint %}

## Was die Vorlage bietet

Ein Administrator schaltet die Vorlage dieser Branche unter **Knowledge Assistant** → **Settings** → **Industry templates** ein. Siehe [Aufgaben und wo Sie sie finden](../tasks-and-where-to-find-them.md#eine-branchenvorlage-einschalten-administrator). Die Karte zeigt dann „On · 3 agents · 3 knowledge bases“.

**Wissensdatenbanken** (in sie laden Sie Ihre Dokumente hoch):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->
* Product documentation
* Suppliers and certificates
* Service

**Assistenten** (Sie wählen einen im Chat):

* Conformity assistant
* Invoice checker for industrial goods
* Weekly report: expiring certificates, declarations and contracts

Die genauen Namen stehen auf der Vorlagenkarte und im Chat.

## Beispielfragen aus dem Demo-Satz

| Frage | Antwort |
| --- | --- |
| Gibt es widersprüchliche Angaben zur Zugfestigkeit bei Schmelze SZ-2609-7050? | Ja: 399 N/mm² im Original des Abnahmeprüfzeugnisses und 625 N/mm² in der Kopie. Beide Dateien werden genannt. |
| Ist Garantie GB-2610-4566 heute (23.11.2026) noch gültig? | Nein. Die Bedingungen nennen „gültig bis 07.02.2025“, obwohl das Dokument den Vermerk „Status: gültig“ trägt. |
| Welche Arbeitszeit gilt aktuell für Servicebericht SB-2611-4115? | 2,6 Stunden aus Version 2. Die 9,1 Stunden aus Version 1 gelten nicht mehr. |

Sie können auf Deutsch, Englisch oder Französisch fragen. In unseren Tests folgte die Antwort der Sprache der Frage, gleich in welcher Sprache das Dokument geschrieben war.

## Was bei Ihnen bleibt

* **Prüfung:** Jede Antwort nennt ihre Quelle. Öffnen Sie sie und lesen Sie die Stelle, bevor Sie handeln. Steht etwas nicht in Ihren Dokumenten, sagt der Assistent „nicht in den Unterlagen“.
* **Kontrolle:** Die Vorlage ist aus, bis Ihr Administrator sie einschaltet. Beim Ausschalten verschwinden die Assistenten; Ihre Dokumente bleiben.
* **Trennung:** Dokumente und Antworten sind je Organisation getrennt.
* **Entscheidung:** Der Assistent schlägt nach und vergleicht. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er gibt keine Rechtsberatung.

## Am Demo-Satz nicht getestet

Der Abgleich einer Rechnung mit einer Bestellung ist am Demo-Satz nicht gezeigt. Der Assistent gibt keine Konformität frei und bewertet keine Normen; Freigabe und Zahlung bleiben bei Ihnen.

Wie gut der Assistent mit Ihren Dokumenten arbeitet, etwa mit langen Verträgen, Handschrift, Stempeln oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten. Siehe [Was er kann und was nicht](../what-it-can-and-cannot-do.md).
