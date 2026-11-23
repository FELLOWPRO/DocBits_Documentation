# Knowledge Assistant für Life Sciences

Finden Sie abgelaufene Lieferantendokumente, überholte Fassungen und widersprüchliche Angaben selbst, bevor es ein Auditor tut. Jede Antwort zeigt Dokument, Fassung, Status und die Stelle.

<!-- VIDEO: rag/life-sciences/v1/de.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
Die Beispiele auf dieser Seite verwenden **erfundene Demo-Daten**: 30 fiktive Dokumente für diese Branche. Firmennamen, Dokumentnummern und Werte sind ausgedacht.
{% endhint %}

## Was die Vorlage bietet

Ein Administrator schaltet die Vorlage dieser Branche unter **Knowledge Assistant** → **Settings** → **Industry templates** ein. Siehe [Aufgaben und wo Sie sie finden](../tasks-and-where-to-find-them.md#eine-branchenvorlage-einschalten-administrator). Die Karte zeigt dann „On · 3 agents · 3 knowledge bases“.

**Wissensdatenbanken** (in sie laden Sie Ihre Dokumente hoch):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->
* Controlled documents (SOP library)
* Regulations and guidelines
* Suppliers, quality agreements and certificates

**Assistenten** (Sie wählen einen im Chat):

* SOP lookup
* Regulatory researcher
* Weekly certificate and deadline report

Die genauen Namen stehen auf der Vorlagenkarte und im Chat.

## Beispielfragen aus dem Demo-Satz

| Frage | Antwort |
| --- | --- |
| Ist Auditbericht AB-2606-5182 heute (23.11.2026) noch gültig? | Nein. Er war bis 3. Juli 2025 gültig, obwohl das Dokument selbst „Status: gültig“ nennt. |
| Welches Auditintervall gilt aktuell in Qualitätsvereinbarung QV-2606-2101? | 33 Monate laut Version 2. Version 1 nannte 25 Monate und ist überholt. Beide Dateien stehen als Quellen. |
| Gibt es widersprüchliche Angaben zum Partikelgrenzwert 0,5 µm im Leitlinienauszug LL-2609-9744? | Ja: 342.228 je m³ im Original und 290.560 je m³ in der Kopie, mit beiden Quellen. |

Sie können auf Deutsch, Englisch oder Französisch fragen. In unseren Tests folgte die Antwort der Sprache der Frage, gleich in welcher Sprache das Dokument geschrieben war.

## Was bei Ihnen bleibt

* **Prüfung:** Jede Antwort nennt ihre Quelle. Öffnen Sie sie und lesen Sie die Stelle, bevor Sie handeln. Steht etwas nicht in Ihren Dokumenten, sagt der Assistent „nicht in den Unterlagen“.
* **Kontrolle:** Die Vorlage ist aus, bis Ihr Administrator sie einschaltet. Beim Ausschalten verschwinden die Assistenten; Ihre Dokumente bleiben.
* **Trennung:** Dokumente und Antworten sind je Organisation getrennt.
* **Entscheidung:** Der Assistent schlägt nach und vergleicht. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er gibt keine Rechtsberatung.

## Am Demo-Satz nicht getestet

Der Knowledge Assistant ist eine Nachschlagehilfe. Er ist **kein validiertes GxP-System** und ersetzt weder Ihr Qualitätsmanagementsystem noch Ihr Fristenregister. Jede Antwort ist ein Hinweis, den Sie am Original prüfen. Patientendaten und Roh-Studiendaten gehören nicht in die Wissensdatenbanken. Der Demo-Satz enthält keine CAPA- oder Abweichungsberichte, Chargenprotokolle oder Schulungsnachweise; dazu machen wir keine Aussage.

Wie gut der Assistent mit Ihren Dokumenten arbeitet, etwa mit langen Verträgen, Handschrift, Stempeln oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten. Siehe [Was er kann und was nicht](../what-it-can-and-cannot-do.md).
