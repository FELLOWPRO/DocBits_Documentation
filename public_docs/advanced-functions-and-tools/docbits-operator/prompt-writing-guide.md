# Anleitung zur Erstellung von Aufforderungen

Diese Anleitung erläutert, wie Sie effektive Aufforderungen für den DocBits Operator schreiben. Aufforderungen sind schrittweise Anweisungen, die den Operator anweisen, bestimmte Aufgaben auszuführen, wie das Navigieren auf Webseiten, die Interaktion mit UI-Elementen und das Eingeben von Daten.

## Was ist eine Aufforderung?

Eine Aufforderung ist eine Abfolge von Anweisungen in Textform, die den Operator dazu anleiten, einen Workflow auszuführen. Aufforderungen können Befehle wie das Klicken von Schaltflächen, das Ausfüllen von Formularen, das Warten auf das Laden von Seiten oder Elementen und mehr enthalten.

## Aufforderungssyntax und -struktur

* Jede Anweisung sollte als nummerierter Schritt geschrieben werden.
* Verwenden Sie klare, prägnante Sprache, um jede Aktion zu beschreiben.
* Geben Sie UI-Elemente nach Namen, Label oder Indexnummer an, um Präzision sicherzustellen.
* Verwenden Sie eine konsistente Formatierung, um die Lesbarkeit zu verbessern.

## Verwendung von Variablen in Aufforderungen

Variablen ermöglichen es Ihnen, Aufforderungen dynamisch zu gestalten, indem Sie verschiedene Werte zur Laufzeit einfügen. Verwenden Sie Platzhalter innerhalb geschweifter Klammern anstelle von fest codierten Werten wie Daten oder Dokumentennummern, z. B.: `{invoice_number}`, `{url}` oder `{purchase_order}`.

Dadurch werden Aufforderungen wiederverwendbar und anpassbar für verschiedene Workflows oder Datensätze.

### Wie man Variablen verwendet

* Schreiben Sie Variablen innerhalb geschweifter Klammern in Ihrem Aufforderungstext:
  * Geben Sie die Rechnungsnummer ein: {invoice\_number} im Feld 'Rechnungsnummer HP'.
* Jede Variable muss einen eindeutigen Namen haben (z. B. `invoice_number`, `url`, `document_type`).
* Variablennamen dürfen keine Leerzeichen oder Sonderzeichen enthalten (Unterstriche sind erlaubt).
* Für Workflows müssen die Variablennamen genau mit den Feld-IDs des Dokuments übereinstimmen, um eine automatische Datenzuordnung zu ermöglichen.

## Popup für Aufforderungsvariablen

Um das Popup für Aufforderungsvariablen zu öffnen, klicken Sie auf das **Zahnrad-Symbol** neben dem Eingabefeld für die Aufforderung.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Layout und Steuerelemente des Popups

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Eingabefeld für Schlüssel:** Geben Sie den Variablennamen hier ein (ohne geschweifte Klammern).
* **Eingabefeld für Wert:** Geben Sie den Wert ein, der für diese Variable verwendet werden soll, wenn die Aufforderung ausgeführt wird.
* **Als sensibel speichern (Checkbox):** Wenn aktiviert, markiert dies den Variablenwert als sensibel. Sensible Werte werden verschlüsselt und in Workflows ausgeblendet, um vertrauliche Informationen vor unbefugten Benutzern zu schützen.
* **Hinzufügen-Schaltfläche (+):** Klicken Sie hier, um eine weitere Eingabereihe für Schlüssel-Wert-Paare hinzuzufügen.
* **Löschen-Symbol (Mülleimer):** Wenn mehrere Schlüssel-Wert-Paare existieren, zeigt jedes Paar außer dem ersten ein kleines Mülleimersymbol zum Löschen dieses spezifischen Paares an.
* **Löschen-Schaltfläche:** Setzt das Popup zurück, indem alle Schlüssel-Wert-Paare und eingegebenen Werte gelöscht werden.
* **Speichern-Schaltfläche:** Speichert alle definierten Variablen und ihre Werte für die aktuelle Aufforderung.
