# Standard Workflow

Der **Standard Workflow**-Builder ist der lineare, kartenbasierte Editor zur Automatisierung der Dokumentenverarbeitung. Ein Workflow besteht aus drei Kartengruppen — **When** (der Auslöser), **And** (zusätzliche Bedingungen) und **Then** (die auszuführenden Aktionen). Wenn ein Dokument die When-/And-Bedingungen erfüllt, laufen die Then-Aktionen automatisch.

## Zugang

Öffnen Sie **Workflow Dashboard → Workflow List** und klicken Sie auf **Add Workflow**, um einen neuen Standard-Workflow zu erstellen, oder klicken Sie einen bestehenden Workflow zum Bearbeiten an.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List mit Typ, Ausführungsreihenfolge und Auslöser"><figcaption><p>Die Workflow List — jede Zeile ist ein Workflow, den Sie öffnen, ein-/ausschalten oder bearbeiten können.</p></figcaption></figure>

## Das When- / And- / Then-Modell

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Standard-Workflow-Canvas mit When-, And- und Then-Karten"><figcaption><p>Die Standard-Workflow-Canvas. Dieses Beispiel wird bei Rechnungen einer Unterorganisation ausgelöst und weist sie einem Benutzer zu.</p></figcaption></figure>

- **When** — der Auslöser, der den Workflow startet (z. B. *Document type is Invoice*).
- **And** — zusätzliche Bedingungen, die ebenfalls erfüllt sein müssen (z. B. *Document is part of sub-organization*). Leer lassen, um bei jedem Treffer der When-Karte zu laufen.
- **Then** — die auszuführenden Aktionen (z. B. *Assign the document to the user*, eine Aufgabe erstellen, eine API aufrufen, eine E-Mail senden).

## Karten hinzufügen

Klicken Sie in einer beliebigen Gruppe auf **Add Card**, um die Kartenbibliothek zu öffnen. Die Karten sind nach Kategorie geordnet, sodass Sie den benötigten Baustein finden:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-Bibliothek nach Kategorie gruppiert"><figcaption><p>Die <strong>Add Card</strong>-Bibliothek — Bedingungskarten, Vergleichskarten, Aktionskarten und mehr, nach Kategorie gruppiert.</p></figcaption></figure>

Speichern Sie über **Save Workflow** oder sichern Sie das Layout als wiederverwendbare Vorlage über **Save Template**.

## Nächste Schritte

- Was die einzelnen Karten tun, sehen Sie im Abschnitt **Karten**.
- Bewährte Karten-Kombinationen finden Sie in den **Workflow-Pattern-Leitfäden**.
- Für verzweigte Abläufe mit parallelen Pfaden (Wait ALL / Wait ANY / OR) verwenden Sie den **Advanced Workflow**-Builder.
