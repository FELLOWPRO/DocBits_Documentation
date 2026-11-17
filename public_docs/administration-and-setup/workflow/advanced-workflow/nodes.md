# Knoten

## Aktueller Konfigurations- und Ergebnisvertrag

ALL verlangt einen passenden verbundenen Ausgang von **jeder unterschiedlichen Quelle**. ANY und OR benötigen mindestens eine passende Quelle. Verbinden Sie eine Quelle über Grün und Orange, zählt sie weiterhin einmal. OR erzeugt keine exklusive Verzweigung und beendet andere Aktionen nicht. Auch ANY ist keine Zusage „der schnellste Zweig gewinnt“.

Im geprüften Scheduler warten diese Knoten zunächst auf alle eingehenden Vorgänger. Bleibt eine Quelle wegen eines nicht gewählten Zweigs unerreichbar, überspringt der echte Ablauf die wartende Zusammenführung. Der Testmodus kann sie mit den vorhandenen Ergebnissen trotzdem auswerten. **Ein grüner Teiltest beweist deshalb nicht, dass derselbe Graph im Dokumentlauf weiterläuft.**

Für zwei verpflichtende Prüfungen führen Sie beide Prüfungen tatsächlich aus und verbinden passende Ergebnisse mit ALL. Für alternative Routen in dieser Version verwenden Sie die direkte gemeinsame Then-Abschlusskarte aus dem v2-Geschäftsfall. Diese Zusammenführung ist für gegenseitig ausschließende Routen gedacht; sie ersetzt keine Schranke für mehrere gleichzeitig ausgeführte Aktionen.

Prüfen Sie Quelle, verbundenen Ausgang, gewählten Ausgang und tatsächliche Erreichbarkeit getrennt. Eine Quelle mit Error bleibt ein Fehler im Gesamtlauf, auch wenn ANY/OR anschließend erfolgreich sind. Ein nicht erfülltes ALL besitzt im geprüften Code zusätzlich einen Fehlerhinweis; nur auf seine orange Farbe zu schauen genügt nicht.

[P0: Wait ALL, Wait ANY und OR richtig verbinden](../masterclass/control-nodes.md)


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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4" %}

**Video:** Die Version einer Karte ändern · 0:39 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Das Label zeigt die Version der Karte** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4#t=0.25)

Karten können mehrere Versionen haben. Das kleine Label auf einer Karte, zum Beispiel v1, zeigt, welche Version sie nutzt. Eine neuere Version kann mehr.

**Klicken, um die Versionen zu sehen** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4#t=11.583)

Klicken Sie auf das Versionslabel, um die Versionen dieser Karte zu sehen.

**Version 3: Status nach dem Export** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4#t=16.916)

Wählen Sie die neuere Version. Diese kann nach dem Export auch den Status des Dokuments setzen.

**Die Werte neu setzen** · [0:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4#t=23.683)

Die Werte werden nicht übernommen. Setzen Sie sie neu, hier die Exportkonfiguration und den Status.

**Validieren und testen** · [0:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/de.mp4#t=31.65)

Validieren und testen Sie dann den Workflow, wie nach jeder Änderung. Speichern Sie, wenn er tut, was Sie erwarten.

</details>

* **Start** — manueller Einstieg; in der geprüften Oberfläche benötigt der gespeicherte Graph zusätzlich einen When-Einstieg.
- **When** — eine Trigger-Karte, identisch mit der im Standard-Builder.
- **And** — eine Bedingungskarte. Sie wird zu wahr oder falsch ausgewertet und kann den Ablauf verzweigen.
- **Then** — eine Aktionskarte, die Arbeit ausführt (Felder setzen, Aufgaben erstellen, APIs aufrufen, …).
* **Wait ALL** — jede unterschiedliche Quelle muss einen verbundenen Ausgang gewählt haben. Der Scheduler wartet auf alle Vorgänger.
* **Wait ANY** — mindestens eine Quelle muss einen verbundenen Ausgang gewählt haben. Der Scheduler wartet trotzdem auf alle Vorgänger; kein Wettlauf.
* **OR** — mindestens eine passende Quelle; keine exklusive Auswahl. Weniger als zwei Quellen erzeugen im Backend eine Warnung.
- **Note** — eine Freitext-Anmerkung auf der Arbeitsfläche; sie hat keinen Einfluss auf die Ausführung.

Die Knoten **When / And / Then** verwenden exakt dieselben Karten, die im Abschnitt [Karten](../cards-overview.md) beschrieben sind.

## Knoten verbinden

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4" %}

**Video:** Erfolg, fehlgeschlagene Bedingung und Fehler in einem Workflow-Lauf · 1:24 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Wenn, Und, Dann zur Laufzeit** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=0.25)

Wenn ein Workflow läuft, startet ihn die Wenn-Karte. Und-Karten prüfen Bedingungen, und Dann-Karten handeln. Was als Nächstes passiert, hängt vom Ergebnis jeder Karte ab.

**Erfolg, gescheiterte Bedingung oder Fehler** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=12.216)

Jede Und-Karte endet mit einem von drei Ergebnissen. Erfolg folgt dem blauen Erfolgspfad, eine gescheiterte Bedingung dem orangen Pfad und ein Fehler dem roten Fehlerpfad.

**Fehlende Daten sind ein Fehler** · [0:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=24.016)

Fehlende Daten sind keine gescheiterte Bedingung. Fehlt ein Feld, das die Karte braucht, fehlt eine Variable oder gibt es kein Dokument, meldet die Karte einen Fehler und nimmt den roten Fehlerpfad.

**Kein oranger Pfad: Der Lauf stoppt** · [0:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=36.316)

Schlägt eine Bedingung fehl und ihr oranger Pfad ist nicht verbunden, stoppt der Workflow an dieser Karte. Der Lauf endet als gescheiterte Bedingung.

**Verbunden: nur ein weiterer Zweig** · [0:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=47.083)

Ist der orange Pfad verbunden, ist eine gescheiterte Bedingung einfach ein weiterer Zweig. Der Workflow läuft dort weiter und kann trotzdem mit Erfolg enden.

**Roter Fehlerpfad: Fehler auffangen** · [0:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=57.383)

Verbinden Sie den roten Fehlerpfad mit einem Ausweg, zum Beispiel einer Aufgabe für eine Person, damit Fehler nicht unbemerkt bleiben. Der Ausweg läuft, aber der Lauf gilt trotzdem als Fehler.

**Wie ein Lauf endet** · [1:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/de.mp4#t=70.783)

Kurz gesagt: Jeder Fehler macht den Lauf zum Fehler. Eine gescheiterte Bedingung ohne verbundenen orangen Pfad macht ihn zur gescheiterten Bedingung. Alles andere endet mit Erfolg.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4" %}

**Video:** UND und ODER: Bedingungen verbinden · 4:19 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.vtt)

<details>

<summary>Transkript</summary>

**UND und ODER** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=0.25)

Bedingungen lassen sich auf zwei Arten verbinden. Karten hintereinander wirken wie UND: alle müssen wahr sein. Karten nebeneinander, mit derselben nächsten Karte verbunden, wirken wie ODER: eine wahre Karte genügt. Verbindungsknoten zeigen das auf der Arbeitsfläche.

**UND: Karten hintereinander** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=18.55)

Eine Karte nach der anderen ist UND: Jede Karte auf dem Pfad muss wahr sein, bevor die nächste läuft. Diese Rechnung ist bereit zur Validierung und nicht in Genehmigung, also sind beide Karten wahr und die Aktion läuft.

**ODER: Karten nebeneinander** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=34.85)

ODER heißt Karten nebeneinander. Verbinden Sie den grünen Ausgang beider Und-Karten direkt mit dem Eingang der nächsten Karte. Testen Sie es: Die erste Karte ist falsch, die zweite wahr, und ein wahrer Pfad reicht, damit die Aktion läuft. Das Testbanner meldet trotzdem eine nicht erfüllte Bedingung, weil der orange Ausgang der falschen Karte nicht verbunden ist, aber die Aktion läuft.

**Dasselbe mit einer ODER-Karte** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=58.416)

Sie können die Pfade auch mit einer ODER-Karte zusammenführen. Sie bewirkt dasselbe, macht das ODER aber auf der Arbeitsfläche sichtbar. Rechtsklick auf die Arbeitsfläche, Hinzufügen, dann ODER. Verbinden Sie beide Und-Karten damit und die ODER-Karte mit der Aktion.

**Ein wahrer Fall genügt für ODER** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=76.316)

Der Test liefert dasselbe Ergebnis: Ein wahrer Fall genügt der ODER-Karte, also läuft die Aktion. Auch hier meldet das Banner die nicht erfüllte Bedingung der falschen Karte.

**Auf EINEN warten: dasselbe wie ODER** · [1:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=90.283)

Auf EINEN warten funktioniert genau wie ODER: Die Karte wartet auf jede Karte davor und macht weiter, wenn mindestens ein Pfad genommen wurde. Beide sind austauschbar, nehmen Sie den Namen, der in Ihrem Workflow besser passt.

**UND mit Auf ALLE warten** · [1:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=111.983)

Für UND mit Karten nebeneinander nehmen Sie Auf ALLE warten. Rechtsklick auf die Arbeitsfläche, Hinzufügen, dann Auf ALLE warten. Verbinden Sie beide Und-Karten damit und Auf ALLE warten mit der Aktion. Testen Sie es: Die Karte wartet auf beide, beide sind wahr, also läuft die Aktion.

**Die Reihenfolge: wie die Verbindungen gezogen wurden** · [2:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=139.816)

In welcher Reihenfolge läuft das? Der Workflow arbeitet eine Liste ab. Die Karten hinter einer Karte kommen in der Reihenfolge dazu, in der ihre Verbindungen gezogen wurden, also läuft die obere Bedingung zuerst, dann die untere. Die ODER-Karte wartet, bis beide gelaufen sind, und die Aktion läuft einmal, egal wie viele Bedingungen wahr waren.

**Direkt in eine Aktion: kein Warten** · [2:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=170.783)

Karten, die direkt mit einer Aktion verbunden sind, warten nicht. Die Aktion wird über den kurzen Pfad erreicht und läuft, bevor die letzte Karte des langen Pfads geprüft ist, also ändert diese Karte nichts mehr. Soll die Aktion auf jede Prüfung warten, setzen Sie eine ODER-, Auf EINEN warten- oder Auf ALLE warten-Karte davor.

**Jeder Ausgang kann woanders hinführen** · [3:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=192.783)

Jede Karte hat bis zu drei Ausgänge: Erfolg, nicht erfüllte Bedingung und Fehler. Jeder Ausgang kann zu einer eigenen nächsten Karte führen.

**Mehrere Ausgänge, ein Eingang: einer genügt** · [3:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=204.816)

Sie können auch mehrere Ausgänge einer Karte mit demselben Eingang verbinden. Nur einer davon kann genommen werden, weil eine Karte mit genau einem Ergebnis endet, also wartet die nächste Karte nur auf diesen einen. Das gilt für jeden Eingang, nicht nur für diese Verbindungsknoten. Testen Sie es: Die Bedingung ist nicht erfüllt, und Auf ALLE warten läuft trotzdem weiter.

**Verbindungsknoten: welche Pfade genommen wurden** · [3:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/de.mp4#t=233.85)

Die Verbindungsknoten machen einen Workflow vor allem leichter lesbar. ODER und Auf EINEN warten laufen weiter, sobald mindestens ein verbundener Pfad genommen wurde. Auf ALLE warten wartet, bis alle vorherigen Karten fertig sind, und läuft nur weiter, wenn alle verbundenen Pfade genommen wurden. Jeder Ausgang einer Karte kann verbunden werden, nicht nur der grüne: Endet eine Karte mit nicht erfüllter Bedingung, zählt ihr orange Ausgang als genommen.

</details>

Knoten werden durch **farbige Kanten** verbunden. Ziehen Sie von einem Anschlusspunkt auf der **rechten** Seite eines Knotens zum Eingangsanschluss auf der **linken** Seite eines anderen Knotens, um eine Verbindung zu erstellen. Jede Farbe steht für ein anderes Ausführungsergebnis:

- **Success** (blau) — der Standardpfad, der genommen wird, wenn ein Knoten erfolgreich abgeschlossen wird. Bei allen Knotentypen verfügbar.
- **Failed Condition** (orange) — wird genommen, wenn eine Bedingung zu falsch ausgewertet wird. Bei **And**-Knoten (Bedingung) verfügbar.
- **Error** (rot) — wird genommen, wenn bei einem Knoten während der Ausführung ein Fehler auftritt. Bei **And**- und **Then**-Knoten (Aktion) verfügbar.

## Hervorhebung des Ausführungspfads

Klicken Sie auf einen beliebigen Knoten, um seinen Ausführungspfad anzuzeigen. Alle Knoten, die zu ihm führen, und alle Knoten, die ihm folgen, werden hervorgehoben — alles andere wird abgedunkelt. Bei **Wait ALL**-Knoten wird jeder eingehende Zweig angezeigt, sodass Sie genau sehen, worauf das Gate wartet, bevor es fortfährt.

## Nächste Schritte

- Geben Sie Daten zwischen Knoten weiter mit [Variablen](variables.md).
- Prüfen und starten Sie Ihren Ablauf mit [Validierung & Test](validation-and-testing.md).
