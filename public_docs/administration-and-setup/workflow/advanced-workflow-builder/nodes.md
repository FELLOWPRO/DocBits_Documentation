# Nodes

## Aktueller Konfigurations- und Ergebnisvertrag

ALL verlangt einen passenden verbundenen Ausgang von **jeder unterschiedlichen Quelle**. ANY und OR benötigen mindestens eine passende Quelle. Verbinden Sie eine Quelle über Grün und Orange, zählt sie weiterhin einmal. OR erzeugt keine exklusive Verzweigung und beendet andere Aktionen nicht. Auch ANY ist keine Zusage „der schnellste Zweig gewinnt“.

Im geprüften Scheduler warten diese Knoten zunächst auf alle eingehenden Vorgänger. Bleibt eine Quelle wegen eines nicht gewählten Zweigs unerreichbar, überspringt der echte Ablauf die wartende Zusammenführung. Der Testmodus kann sie mit den vorhandenen Ergebnissen trotzdem auswerten. **Ein grüner Teiltest beweist deshalb nicht, dass derselbe Graph im Dokumentlauf weiterläuft.**

Für zwei verpflichtende Prüfungen führen Sie beide Prüfungen tatsächlich aus und verbinden passende Ergebnisse mit ALL. Für alternative Routen in dieser Version verwenden Sie die direkte gemeinsame Then-Abschlusskarte aus dem v2-Geschäftsfall. Diese Zusammenführung ist für gegenseitig ausschließende Routen gedacht; sie ersetzt keine Schranke für mehrere gleichzeitig ausgeführte Aktionen.

Prüfen Sie Quelle, verbundenen Ausgang, gewählten Ausgang und tatsächliche Erreichbarkeit getrennt. Eine Quelle mit Error bleibt ein Fehler im Gesamtlauf, auch wenn ANY/OR anschließend erfolgreich sind. Ein nicht erfülltes ALL besitzt im geprüften Code zusätzlich einen Fehlerhinweis; nur auf seine orange Farbe zu schauen genügt nicht.

[P0: Wait ALL, Wait ANY und OR richtig verbinden](../masterclass/control-nodes.md)


Ein Advanced Workflow ist ein Graph aus **Knoten**, die durch Kanten verbunden sind. Sie fügen Knoten über das Menü **+ Add** hinzu (oder per Rechtsklick auf die Arbeitsfläche) und verbinden sie, um den Ausführungsablauf festzulegen.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menü zum Hinzufügen von Knoten mit den verfügbaren Knotentypen"><figcaption><p>Das Menü <strong>+ Add</strong> für Knoten — die verfügbaren Knotentypen.</p></figcaption></figure>

## Knotentypen

* **Start** — manueller Einstieg; in der geprüften Oberfläche benötigt der gespeicherte Graph zusätzlich einen When-Einstieg.
* **When** — eine Trigger-Karte, identisch mit der im Standard-Builder.
* **And** — eine Bedingungskarte. Sie wird zu wahr oder falsch ausgewertet und kann den Ablauf verzweigen.
* **Then** — eine Aktionskarte, die Arbeit ausführt (Felder setzen, Aufgaben erstellen, APIs aufrufen, …).
* **Wait ALL** — jede unterschiedliche Quelle muss einen verbundenen Ausgang gewählt haben. Der Scheduler wartet auf alle Vorgänger.
* **Wait ANY** — mindestens eine Quelle muss einen verbundenen Ausgang gewählt haben. Der Scheduler wartet trotzdem auf alle Vorgänger; kein Wettlauf.
* **OR** — mindestens eine passende Quelle; keine exklusive Auswahl. Weniger als zwei Quellen erzeugen im Backend eine Warnung.
* **Note** — eine Freitext-Anmerkung auf der Arbeitsfläche; sie hat keinen Einfluss auf die Ausführung.

Die Knoten **When / And / Then** verwenden exakt dieselben Karten, die im Abschnitt [Karten](../cards-overview/) beschrieben sind.

## Knoten verbinden

Knoten werden durch **farbige Kanten** verbunden. Ziehen Sie von einem Anschlusspunkt auf der **rechten** Seite eines Knotens zum Eingangsanschluss auf der **linken** Seite eines anderen Knotens, um eine Verbindung zu erstellen. Jede Farbe steht für ein anderes Ausführungsergebnis:

* **Success** (blau) — der Standardpfad, der genommen wird, wenn ein Knoten erfolgreich abgeschlossen wird. Bei allen Knotentypen verfügbar.
* **Failed Condition** (orange) — wird genommen, wenn eine Bedingung zu falsch ausgewertet wird. Bei **And**-Knoten (Bedingung) verfügbar.
* **Error** (rot) — wird genommen, wenn bei einem Knoten während der Ausführung ein Fehler auftritt. Bei **And**- und **Then**-Knoten (Aktion) verfügbar.

## Hervorhebung des Ausführungspfads

Klicken Sie auf einen beliebigen Knoten, um seinen Ausführungspfad anzuzeigen. Alle Knoten, die zu ihm führen, und alle Knoten, die ihm folgen, werden hervorgehoben — alles andere wird abgedunkelt. Bei **Wait ALL**-Knoten wird jeder eingehende Zweig angezeigt, sodass Sie genau sehen, worauf das Gate wartet, bevor es fortfährt.

## Nächste Schritte

* Geben Sie Daten zwischen Knoten weiter mit [Variablen](variables.md).
* Prüfen und starten Sie Ihren Ablauf mit [Validierung & Test](validation-and-testing.md).
