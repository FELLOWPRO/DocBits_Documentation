# Knoten

Ein Advanced Workflow ist ein Graph aus **Knoten**, die durch Kanten verbunden sind. Sie fügen Knoten über das Menü **+ Add** hinzu (oder per Rechtsklick auf die Arbeitsfläche) und verbinden sie, um den Ausführungsablauf festzulegen.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menü zum Hinzufügen von Knoten mit den verfügbaren Knotentypen"><figcaption><p>Das Menü <strong>+ Add</strong> für Knoten — die verfügbaren Knotentypen.</p></figcaption></figure>

## Knotentypen

- **Start** — der Einstiegspunkt des Workflows. Wird automatisch hinzugefügt; jeder Ablauf beginnt hier.
- **When** — eine Trigger-Karte, identisch mit der im Standard-Builder.
- **And** — eine Bedingungskarte. Sie wird zu wahr oder falsch ausgewertet und kann den Ablauf verzweigen.
- **Then** — eine Aktionskarte, die Arbeit ausführt (Felder setzen, Aufgaben erstellen, APIs aufrufen, …).
- **Wait ALL** — wartet, bis *alle* eingehenden Zweige abgeschlossen sind, bevor fortgefahren wird.
- **Wait ANY** — fährt fort, sobald *ein beliebiger* eingehender Zweig abgeschlossen ist.
- **OR** — verzweigt den Ablauf auf alternative Pfade.
- **Note** — eine Freitext-Anmerkung auf der Arbeitsfläche; sie hat keinen Einfluss auf die Ausführung.

Die Knoten **When / And / Then** verwenden exakt dieselben Karten, die im Abschnitt [Karten](../cards-overview.md) beschrieben sind.

## Knoten verbinden

Knoten werden durch **farbige Kanten** verbunden. Ziehen Sie von einem Anschlusspunkt auf der **rechten** Seite eines Knotens zum Eingangsanschluss auf der **linken** Seite eines anderen Knotens, um eine Verbindung zu erstellen. Jede Farbe steht für ein anderes Ausführungsergebnis:

- **Success** (blau) — der Standardpfad, der genommen wird, wenn ein Knoten erfolgreich abgeschlossen wird. Bei allen Knotentypen verfügbar.
- **Failed Condition** (orange) — wird genommen, wenn eine Bedingung zu falsch ausgewertet wird. Bei **And**-Knoten (Bedingung) verfügbar.
- **Error** (rot) — wird genommen, wenn bei einem Knoten während der Ausführung ein Fehler auftritt. Bei **And**- und **Then**-Knoten (Aktion) verfügbar.

## Hervorhebung des Ausführungspfads

Klicken Sie auf einen beliebigen Knoten, um seinen Ausführungspfad anzuzeigen. Alle Knoten, die zu ihm führen, und alle Knoten, die ihm folgen, werden hervorgehoben — alles andere wird abgedunkelt. Bei **Wait ALL**-Knoten wird jeder eingehende Zweig angezeigt, sodass Sie genau sehen, worauf das Gate wartet, bevor es fortfährt.

## Nächste Schritte

- Geben Sie Daten zwischen Knoten weiter mit [Variablen](variables.md).
- Prüfen und starten Sie Ihren Ablauf mit [Validierung & Test](validation-and-testing.md).
