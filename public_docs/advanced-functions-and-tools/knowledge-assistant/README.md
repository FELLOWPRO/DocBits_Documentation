# Wissensassistent

Der Wissensassistent beantwortet Fragen aus **Ihren eigenen Dokumenten**, direkt im DocBits-Client. Jede Antwort nennt das Dokument, aus dem sie stammt. Ein Klick öffnet dieses Dokument neben der Antwort an der Stelle, an der die Information gefunden wurde. Sie müssen der Antwort nicht blind vertrauen: Sie öffnen die Quelle und prüfen sie.

<!-- VIDEO: rag/overview/v1/de.mp4 noch nicht veröffentlicht -->

<figure><img src="../../.gitbook/assets/ka-source-preview-de.png" alt="Chat-Antwort zu einem Nachtrag mit der Quellenvorschau rechts, die das gescannte Dokument und den Hinweis Auf Seite 1 gefunden zeigt"><figcaption><p>Eine Antwort mit ihrer Quelle: Das Dokument öffnet sich neben dem Chat.</p></figcaption></figure>

{% hint style="info" %}
Alle Beispiele in diesem Bereich verwenden **erfundene Demo-Daten**: fiktive Firmen, Dokumentnummern, Beträge und Werte. Sie zeigen nur, wie der Assistent arbeitet. Es sind keine Kundendaten und keine Zusage für Ergebnisse mit Ihren Dokumenten.
{% endhint %}

## Was Sie damit tun können

* **In ganzen Sätzen fragen.** Zum Beispiel: „Welches Zahlungsziel und welche Kündigungsfrist gelten für Liefervertrag LV-2607-9239?“ Sie erhalten den Wert und das Dokument, aus dem er gelesen wurde.
* **Mit der gültigen Fassung arbeiten.** Gibt es ein Dokument in zwei Fassungen, nennt der Assistent den Wert der neueren und sagt, welche Fassung sie ersetzt hat. Widersprechen sich zwei Dokumente, nennt er beide Werte mit ihren Quellen, statt einen auszuwählen.
* **„Nicht in den Unterlagen“ statt einer erfundenen Zahl bekommen.** Steht eine Information nicht in Ihren hochgeladenen Dokumenten, sagt der Assistent das. Damit können Sie arbeiten: Das Dokument fehlt.
* **Scans und Fotos von Dokumenten lesen.** Gescannte PDFs werden per Texterkennung gelesen und sind dann durchsuchbar und abfragbar.
* **In Ihrer Sprache fragen.** In unseren Tests folgte die Antwort der Sprache der Frage (getestet: Deutsch, Englisch und Französisch), auch wenn das Dokument in einer anderen Sprache geschrieben war.
* **Mit einer Branchenvorlage starten.** Ein Administrator schaltet eine Vorlage für acht Branchen ein und erhält fertige Wissensdatenbanken und Assistenten. Siehe [Branchenvorlagen](industry-templates/README.md).

## So funktioniert es in vier Schritten

1. **Ein Administrator schaltet den Wissensassistent** für Ihre Organisation ein und, falls gewünscht, eine Branchenvorlage. Siehe [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md#den-wissensassistenten-einschalten-administrator).
2. **Sie laden Dokumente** in eine Wissensdatenbank hoch (PDF, gescanntes PDF, Word, Excel, Markdown, Text, Fotos).
3. **Sie stellen im Chat eine Frage** und wählen einen Assistenten.
4. **Sie öffnen die Quelle** unter der Antwort und bestätigen den Wert im Dokument.

## Was er nicht ist

Der Wissensassistent ist eine **Recherchehilfe mit Quellen**. Er ersetzt nicht die Prüfung des Originals und entscheidet nicht für Sie.

* Er gibt **keine Rechtsberatung** und trifft keine Freigabe-, Zahlungs- oder Compliance-Entscheidung.
* Er ist **kein Archiv**. Ihr Archiv oder Dokumentenmanagementsystem bleibt der Ort für Originale.
* Er **ersetzt keine Auswertungen und Dashboards in DocBits**. Summen, Listen und Filter über viele Dokumente („alle offenen Rechnungen über 10.000 EUR“) kommen aus dem DocBits-Dashboard und den extrahierten Feldern.
* Er ist **kein validiertes System**. In regulierten Bereichen wie Life Sciences nutzen Sie ihn nur als Nachschlagehilfe.

Lesen Sie [Was er kann und was nicht](what-it-can-and-cannot-do.md), bevor Sie sich bei wichtigen Entscheidungen darauf verlassen.

## In diesem Bereich

| Seite | Wofür |
| --- | --- |
| [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md) | Klickweg für jede Aufgabe: einrichten, hochladen, fragen, Quellen prüfen, Wissensdatenbanken verwalten |
| [Fehlerbehebung](troubleshooting.md) | Ein Symptom nachschlagen und die passende Maßnahme finden |
| [Was er kann und was nicht](what-it-can-and-cannot-do.md) | Grenzen verstehen und wissen, was getestet wurde |
| [Branchenvorlagen](industry-templates/README.md) | Sehen, was die Vorlage Ihrer Branche bietet, mit Beispielfragen |

{% hint style="warning" %}
Die Demo-Dokumente, mit denen wir getestet haben, sind kurz und sauber. Wie gut der Assistent mit Ihren Dokumenten arbeitet, zum Beispiel mit langen Verträgen, Handschrift oder schlechten Kopien, zeigt nur ein Pilot mit Ihren eigenen Dokumenten.
{% endhint %}
