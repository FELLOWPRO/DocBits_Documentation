# Was er kann und was nicht

Der Wissensassistent ist eine **Recherchehilfe mit Quellen**. Er findet, was in Ihren Dokumenten steht, und zeigt, wo. Er ersetzt weder die Prüfung an der Quelle noch eine fachliche, rechtliche oder qualitätssichernde Entscheidung. Besonders bei Chemie, Life Sciences und Gefahrgut gilt: **Öffnen Sie vor jeder Entscheidung die Quelle und lesen Sie die Stelle selbst.**

Unsere Tests nutzten erfundene, kurze und saubere Demo-Dokumente (30 je Branche, acht Branchen). Die meisten liefen im November 2026 auf einer separaten Testinstallation. Auf der aktuellen Entwicklungsumgebung haben wir zusätzlich die Oberfläche, eine Beispielfrage mit Quellenvorschau, die Branchenvorlagen und die Dokumentliste geprüft. Löschen von Dokumenten, Rollen, die Trennung von Organisationen und die Verarbeitung von Uploads haben wir dort nicht erneut getestet. Wie gut der Assistent mit Ihren Dokumenten arbeitet, zeigt nur ein Pilot mit Ihren eigenen Dokumenten.

Kennzeichnungen in der letzten Spalte:

* **Im Test belegt:** so in unseren Tests beobachtet (November 2026).
* **Bekannte Einschränkung:** gilt heute; wir nennen sie ausdrücklich.

## Antworten

| Aussage | Kennzeichnung |
| --- | --- |
| Antworten stammen aus Ihren hochgeladenen Dokumenten und nennen das Dokument. Ein Klick öffnet die Stelle, an der die Antwort gefunden wurde. In den Tests nannte der Assistent bei beantwortbaren Fragen die Quelle, mit zwei Einzelfällen, die nicht wieder auftraten. | Im Test belegt |
| Von rund 650 Testfragen wurden 654 von 656 über die Programmierschnittstelle und 143 von 144 im Browser richtig beantwortet. Die Fehler waren eine um eins verschobene Seitenzahl, eine Antwort ohne Quellenhinweis und eine fachlich schwache Differenzfrage. Das ist ein Ergebnis mit kurzen Demo-Dokumenten, keine Zusage für Ihre Dokumente. | Im Test belegt |
| Ein Sprachmodell kann sich irren. Bei Zahlen zu Geld, Sicherheit oder Fristen öffnen Sie die Quelle. | Bekannte Einschränkung |
| Fehlt eine Angabe, sagt der Assistent „nicht in den Unterlagen“ (88 von 88 solcher Testfragen ohne erfundenen Wert). Das heißt: nicht in den hochgeladenen Dokumenten, nicht: existiert nicht. Quellenhinweise können dabei erscheinen; es sind geprüfte Dokumente, kein Beleg. | Im Test belegt |
| Bei Widersprüchen zwischen zwei Fassungen nennt der Assistent die neuere und verweist auf die ältere; bei zwei verschiedenen Werten nennt er beide mit ihren Quellen. | Im Test belegt |
| Gültigkeitsfragen: Trägt ein abgelaufenes Dokument selbst den Vermerk „gültig“, fällt die Antwort manchmal vorsichtig aus. Mit dem Zusatz „Antworte mit Ja oder Nein und nenne das Gültig-bis-Datum.“ war sie in den geprüften Fällen eindeutig. | Im Test belegt |
| Rechenfragen über mehrere Dokumente (Differenz zweier Werte) wurden im Test richtig beantwortet. Eine Differenzfrage zu einer Abschnittsnummer, die keine Menge ist, nicht. | Im Test belegt |
| Summen, Listen und Filter über viele Dokumente („alle offenen Rechnungen über 10.000 EUR“) kommen aus dem DocBits-Dashboard und den extrahierten Feldern, nicht aus dem Wissensassistenten. | Bekannte Einschränkung |
| Der Wissensassistent trifft keine Entscheidungen und gibt keine Rechtsberatung. Freigeben, Zahlen und Bewerten bleiben bei Ihren Fachleuten. Er ist kein Archiv; Originale bleiben in Ihrem Archiv oder Dokumentenmanagementsystem. | Bekannte Einschränkung |
| Der Wissensassistent ist kein validiertes System. Für GxP-Anwendungen, zum Beispiel in Life Sciences, nutzen Sie ihn nur als Nachschlagehilfe, nicht als validierte Entscheidungsgrundlage. | Bekannte Einschränkung |

## Dokumente und Formate

| Aussage | Kennzeichnung |
| --- | --- |
| PDF, gescanntes PDF, Word, Excel, Markdown, Text und Fotos (als Text) wurden gelesen und mit Quelle beantwortet. Die Quellenvorschau funktioniert für diese Formate; bei Excel wird die Zeile nicht markiert, bei Bildern ist der Text nicht bestätigt. | Im Test belegt |
| E-Mail-Dateien (.eml) und XML-Dateien werden beim Upload abgewiesen. Der Import über Web-Adresse ist abgeschaltet. | Bekannte Einschränkung |
| Die Verarbeitungszeit lag bei 8 bis 23 Sekunden je Dokument für kleine Dateien (2 bis 137 KB). Zeiten für große Dateien haben wir nicht gemessen. | Im Test belegt |
| Die Oberfläche nennt höchstens 50 MB je Datei. Dateien dieser Größe und viele große Dateien auf einmal haben wir nicht getestet. | Bekannte Einschränkung |
| Menge: Wir haben mit 30 Dokumenten je Wissensdatenbank-Satz getestet. Wissensdatenbanken mit Hunderten oder Tausenden Dokumenten haben wir nicht getestet. | Bekannte Einschränkung |
| Lange, klauselreiche Verträge, Schriftverkehr, Handschrift, Stempel und schlechte Kopien sind nicht getestet; prüfen Sie hier gegen die Quelle. | Bekannte Einschränkung |
| Die automatische Kurzbeschreibung von Excel- und CSV-Dokumenten schlägt manchmal fehl. Der Inhalt wird trotzdem gelesen und beantwortet Fragen. | Bekannte Einschränkung |

## PDF-Tabellen

| Aussage | Kennzeichnung |
| --- | --- |
| Tabellen in PDF werden **zeilenweise** gelesen. In unseren Tests waren Fragen zu einem einzelnen Eintrag, zum höchsten und niedrigsten Wert und zur Zeilenzahl einer Übersichtstabelle richtig. Verbundene Zellen, mehrere Tabellen auf einer Seite und Tabellen über mehrere Seiten sind nicht getestet; prüfen Sie dort die Werte in der Vorschau. | Bekannte Einschränkung |

## Scans

| Aussage | Kennzeichnung |
| --- | --- |
| Gescannte PDFs werden per Texterkennung gelesen und sind danach durchsuchbar. Das gilt für gedruckte, saubere, ganzseitige Scans. | Im Test belegt |
| Ohne erreichbare Texterkennung bleibt ein Scan ohne Text; das Dokument endet dann mit einer Fehlermeldung, statt zu hängen. Ein Bild, das nur einen Teil der Seite abdeckt, wird nicht als Scan behandelt. | Im Test belegt |
| Bitte prüfen Sie Handschrift, Stempel und schlechte Kopien gegen die Quelle. | Bekannte Einschränkung |

## Seitenzahlen

| Aussage | Kennzeichnung |
| --- | --- |
| Bei langen Dokumenten (etwa 30 Seiten) stimmte die Seitenzahl im Wiederholungslauf bei allen zehn Fragen; im ersten Lauf war eine um eine Seite verschoben. Eine Seitenzahl ist nicht garantiert: Bestätigen Sie die Seite in der Vorschau. | Bekannte Einschränkung |

## Bilder und Gallery

| Aussage | Kennzeichnung |
| --- | --- |
| Die Gallery zeigt nur **in Dokumente eingebettete** Bilder (zum Beispiel in PDF oder Word), und nur wenn die Bildverarbeitung eingeschaltet ist. Einzeln hochgeladene Fotos und Scans erscheinen dort nicht. | Bekannte Einschränkung |
| Beschreibungen von Gallery-Bildern sind derzeit leer („No caption“); die Suche nach Beschreibungstext in der Gallery liefert nichts. | Bekannte Einschränkung |
| Einzeln hochgeladene Fotos werden per Texterkennung gelesen. Fragen zum geschriebenen Text im Foto waren in 24 von 24 Läufen richtig. Der Assistent beurteilt keinen Bildinhalt (zum Beispiel „Ist die Palette beschädigt?“). | Im Test belegt |
| In früheren Testständen war das Hochladen eines Fotos in der Oberfläche gesperrt, bis die Bildverarbeitung eingeschaltet war. Für die aktuelle Version haben wir das nicht erneut geprüft. Fotos können als Text gelesen werden. | Bekannte Einschränkung |

## Organisationen, Berechtigungen und Daten

| Aussage | Kennzeichnung |
| --- | --- |
| Jede Organisation hat einen eigenen Bereich. Eine zweite Organisation erhielt keinen Zugriff auf Wissensdatenbank, Dokumente, Download und Assistenten der ersten. | Im Test belegt |
| Rollen: Wer nur lesen darf (Viewer), kann nicht hochladen, ändern, löschen oder herunterladen. Mitglieder haben standardmäßig Contributor-Rechte. | Im Test belegt |
| Gelöschte Dokumente erscheinen nicht mehr in Antworten; der Speicher wird freigegeben. | Im Test belegt |
| **Unterorganisationen werden nicht getrennt.** Der Wissensassistent trennt nach Organisation. Alle Nutzer einer Organisation sehen dieselben Wissensdatenbanken, auch wenn sie in DocBits unterschiedlichen Unterorganisationen zugeordnet sind. Planen Sie vertrauliche Dokumente entsprechend. Das stammt aus der Analyse des Programms, nicht aus einem Live-Test. | Bekannte Einschränkung |
| Es gibt ein Speicherkontingent je Organisation; bei Überschreitung wird der Upload abgewiesen. | Im Test belegt |

Fragen zu Verarbeitungsort, eingesetztem Sprachmodell und Auftragsverarbeitung beantworten wir für Ihre Umgebung verbindlich im Angebot. Diese Dokumentation macht dazu keine Aussage.

## Sprache

| Aussage | Kennzeichnung |
| --- | --- |
| Getestet wurden Deutsch, Englisch und Französisch. In allen Tests folgte die Antwortsprache der Frage, auch wenn das Dokument in einer anderen Sprache geschrieben war. Das ist **nicht garantiert**; nennen Sie bei Bedarf die gewünschte Sprache in der Frage. Andere Sprachen haben wir nicht getestet. | Im Test belegt |
| Die Oberfläche folgt der Sprache Ihres DocBits-Benutzers. Wir haben Englisch und Deutsch geprüft. In früheren Testständen erschienen einzelne Meldungen auf Chinesisch. | Bekannte Einschränkung |

## Bedienung und Funktionen

| Aussage | Kennzeichnung |
| --- | --- |
| Das Speichern der Abschnittsgröße in den Einstellungen der Wissensdatenbank funktionierte in unseren Tests nicht zuverlässig; für die aktuelle Version haben wir es nicht erneut geprüft. | Bekannte Einschränkung |
| Mermaid-Diagramme in Markdown-Dokumenten werden nicht gezeichnet. | Bekannte Einschränkung |
| In der Oberfläche lassen sich Dokumente nicht zwischen Wissensdatenbanken verschieben; zwischen Ordnern innerhalb einer Wissensdatenbank schon. | Bekannte Einschränkung |
| Die Kopie einer Wissensdatenbank trägt denselben Namen wie das Original. | Bekannte Einschränkung |
| DocBits-Dokumente (Rechnungen, Lieferscheine, Verträge) als Wissensquelle ohne erneutes Hochladen (**Aus DocBits**): Die Übernahme haben wir über die Schnittstelle für Entwickler geprüft, das Auswahlpanel ist vorhanden. Dokumente über das Panel haben wir nicht hinzugefügt. Wer die Wissensdatenbank öffnen darf, kann den hinzugefügten Inhalt lesen. | Bekannte Einschränkung |
| Die Wochenübersicht (Automations) ist standardmäßig aus, liefert ihr Ergebnis in den Verlauf des Assistenten und versendet keine E-Mail. In den Tests lief sie bei manuellem Start in allen acht Branchen. | Im Test belegt |
| Werkzeuge, die eine Anmeldung bei einem externen Dienst verlangen, lassen sich im Wissensassistenten derzeit nicht anmelden. | Bekannte Einschränkung |
| Wiki und Wissensgraph wurden an einer eigenen Demo-Wissensdatenbank getestet, nicht an den Branchenvorlagen. | Bekannte Einschränkung |

## Antwortzeiten

| Aussage | Kennzeichnung |
| --- | --- |
| Die Antwortzeit lag im Mittel bei 6 bis 9 Sekunden, einzelne Antworten bei bis zu 25 Sekunden (mehrere Tests liefen gleichzeitig). Fragen zu Widersprüchen dauerten am längsten (11 bis 15 Sekunden). Keine Antwort dauerte länger als 60 Sekunden. | Im Test belegt |

## Nicht verfügbar

Die Websuche ist optional und standardmäßig aus; ein Administrator schaltet sie ein (siehe [Websuche](web-search.md)). Sie ist als Best Effort gekennzeichnet und ersetzt keine Registerabfrage. Ein eigener Suchanbieter mit eigenem Schlüssel ist geplant und noch nicht verfügbar.

Folgendes gehört heute nicht zum Wissensassistenten und wird nicht angeboten: Ausführen von Code in einer Sandbox, Chat-Kanäle wie E-Mail oder Messenger, eigene Sprachmodelle, getrennte Unterorganisationen und eine Desktop-App. Einen Termin nennen wir für nichts davon.

## Nicht getestet (keine Aussage möglich)

* Chat-Anhänge, das Gedächtnis des Assistenten und die automatische Übernahme aus externen Datenquellen.
* Last aus mehreren Organisationen gleichzeitig, sehr große Importe, parallele Uploads von Dateien über 20 MB.
* Download von mehr als 200 Dokumenten oder sehr großen Mengen.
* Verhalten bei Ausfall des Zusammenfassungs- oder Embedding-Dienstes während einer Textänderung.

Siehe auch: [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md) und [Fehlerbehebung](troubleshooting.md).
