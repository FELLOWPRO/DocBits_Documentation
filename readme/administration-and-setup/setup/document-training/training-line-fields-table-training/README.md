# Positionsfelder und Tabellen trainieren

## Tabellentraining: Einsatz und Vorgehensweise

DocBits verwendet standardmäßig eine KI-basierte Tabellenextraktion, die lieferantenübergreifend funktioniert. Wenn Sie die Extraktion von Positionen für einen bestimmten Lieferanten genauer steuern möchten, können Sie die Struktur mit dem **Tabellentraining** manuell festlegen.

#### &#x20;**Wichtig: lieferantenspezifisches Training**

Das Tabellentraining ist **lieferantenspezifisch**. Die Regeln eines trainierten Tabellenlayouts gelten nur für die Dokumente des jeweiligen Lieferanten.\
Für andere Lieferanten wird weiterhin die KI-basierte Tabellenextraktion verwendet, sofern Sie deren Layouts nicht separat trainieren.

#### Wann ist Tabellentraining sinnvoll?

Verwenden Sie Tabellentraining **nur bei einem gleichbleibenden Dokumentlayout**, um eine einheitliche, hochwertige Extraktion zu erreichen. Es eignet sich besonders für Lieferanten, die:

* dauerhaft ein **festes Rechnungsformat** verwenden;
* eine **präzise Zuordnung** von Positionen zu bestimmten Feldern erfordern;
* **viele Dokumente** liefern, sodass sich eine einheitliche Automatisierung lohnt.

#### Wann sollten Sie auf Tabellentraining verzichten?

Verzichten Sie auf Tabellentraining, wenn:

* der Lieferant **sein Rechnungslayout häufig ändert**, beispielsweise alle paar Monate;
* Sie nur selten Dokumente dieses Lieferanten erhalten;
* die standardmäßige KI-Extraktion ohne manuelles Training bereits **ausreichend gute Ergebnisse** liefert.

In diesen Fällen wäre ein wiederholtes Neutraining der Tabelle aufwendig und ineffizient.



## Vorgehensweise

Im **Trainingsmodus (Training Mode)** legen Sie fest, wie DocBits die Positionen aus dem Dokumentlayout eines bestimmten Lieferanten extrahiert.

Im Trainingsmodus definieren Sie:

* **wo sich die Tabelle** im Dokument befindet;
* **welche Bereiche den einzelnen Spalten entsprechen**, beispielsweise Menge, Beschreibung und Stückpreis.

Dabei entsteht eine **wiederverwendbare Extraktionsvorlage** für den Lieferanten. Künftige Dokumente mit demselben Layout werden damit automatisch verarbeitet, ohne das Layout erneut trainieren zu müssen.

**Wichtige Merkmale:**

* **Zugeordnete Spalten sind schreibgeschützt**; ihr Text lässt sich nicht manuell ändern.
* Sie können **keine Zeilen hinzufügen oder löschen**.
* Der Modus dient der **Zuordnung von Positionen** im Dokument. Werte korrigieren Sie im Korrekturmodus.
* Klicken Sie nach dem Zuordnen der Tabelle und ihrer Spalten auf **„Save Rules“**, damit DocBits die Regeln auf ähnliche Dokumente desselben Lieferanten anwenden kann.



Im **Korrekturmodus (Correction Mode)** beheben Sie **Extraktionsfehler** in den Tabellendaten des aktuellen Dokuments. Verwenden Sie ihn, wenn DocBits die Tabelle bereits extrahiert hat und das Ergebnis kleinere Korrekturen benötigt.

Verwenden Sie den Korrekturmodus, wenn:

* **Werte fehlen oder falsch zugeordnet sind**;
* eine **leere oder doppelte Zeile** extrahiert wurde, die entfernt werden muss.

**Möglichkeiten im Korrekturmodus:**

* **Werte in zugeordneten Spalten manuell anpassen**, beispielsweise falsche Zuordnungen korrigieren.
* **Zeilen löschen**, die nicht zur Tabelle gehören.
* **Zeilen hinzufügen**, die bei der Extraktion vollständig übersehen wurden.
