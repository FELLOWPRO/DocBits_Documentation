# Knoten

## Video: Knoten und Routen

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/de.vtt)

<details>
<summary>Transkript</summary>

Start ist der manuelle Einstieg. When reagiert auf Ereignisse. Beide haben keinen Eingang. And prüft Bedingungen, Then führt Aktionen aus. Beide Editoren verwenden denselben Kartenkatalog.

Ziehen Sie einen Ausgang zum nächsten Eingang. Blau ist im Editor der Erfolgsweg. Orange bedeutet Bedingung falsch, Rot einen Ausführungsfehler. And hat drei Ergebnisse. Then hat Erfolg und Fehler. In Ergebnisansichten ist Erfolg grün.

Prüfen Sie, ob ein Rechnungsbetrag einen Grenzwert überschreitet. Verbinden Sie Blau mit einer Freigabeaufgabe, Orange mit normaler Verarbeitung und Rot mit einer Fehlerbehandlung. Eine falsche Bedingung folgt ihrem verbundenen Weg. Sie stoppt nicht alle Zweige.

Wait ALL führt Zweige zusammen. Jede Quelle muss einen zum Kontrollknoten verbundenen Weg genommen haben. Verbinden Sie beide Prüfungen und die nächste Aktion. Ein nicht gewählter Weg kann kein erforderliches Ergebnis liefern.

Wait ANY und OR führen Zweige zusammen. Mindestens eine Quelle muss einen verbundenen Weg genommen haben. OR benötigt zwei verschiedene Quellknoten. Diese Knoten erzeugen keine exklusive Auswahl und brechen andere Aktionen nicht ab.

Verarbeitungsknoten müssen von einem Einstieg erreichbar sein. Vermeiden Sie Schleifen und eingehende Verbindungen an Einstiegsknoten. Fügen Sie eine Then Aktion hinzu und validieren Sie. Importierte Delay Knoten brauchen eine positive Dauer. Das aktuelle Hinzufügen Menü bietet Delay nicht an.

</details>

[Alle fünf Kapitel ansehen](../advanced-workflow-videos.md)

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
