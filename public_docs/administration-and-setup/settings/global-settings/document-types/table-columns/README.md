# Tabellenspalten

Tabellenspalten legen fest, welche Spalten die Positionstabelle eines Dokumenttyps hat: was DocBits in jede Spalte extrahiert, was der Benutzer in der Validierungsmaske sieht und was beim Export an das ERP gesendet wird.

**Wo:** Settings → Document Processing → Document Types → Table Columns

<figure><img src="../../../../../.gitbook/assets/structured-output-column-choice-de-20261104.png" alt="Aktuelle Use-AI-Auswahl mit Standard, Ja und Nein. Es wurde keine Option geändert. Titelzellen sind aus Datenschutzgründen ausgeblendet."><figcaption><p>Aktuelle Use-AI-Auswahl mit Standard, Ja und Nein. Es wurde keine Option geändert. Titelzellen sind aus Datenschutzgründen ausgeblendet.</p></figcaption></figure>

## Was Sie sehen

Jede Zeile ist eine Spalte einer Tabelle. Die Liste zeigt:

| Spalte | Bedeutung |
|---|---|
| **Column name** | Technischer Name, aus dem Titel erzeugt (Großbuchstaben, Unterstriche). Wird in Skripten, Export-Mappings und der API verwendet. Kann später nicht geändert werden. |
| **Title** | Bezeichnung, die in der Validierungsmaske angezeigt wird. Ändern Sie sie mit dem Übersetzungs-Symbol in der Spalte *Actions* (*Update translation key*). |
| **Column Type** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` oder `CURRENCY`. Bestimmt Validierung und Formatierung. |
| **Table name** | Die Tabelle, zu der die Spalte gehört, zum Beispiel `INVOICE_TABLE`. |
| **Is Required** | Das Dokument kann nicht freigegeben werden, solange diese Spalte in einer beliebigen Zeile leer ist. |
| **Read Only** | Benutzer sehen den Wert, können ihn aber nicht bearbeiten. |
| **Hidden** | Die Spalte wird weder angezeigt noch exportiert. Damit schalten Sie Standardspalten ab, die Sie nicht benötigen. |
| **Use AI** | Dreistufige KI-Auswahl: Standard übernimmt die KI-Vorgabe des Dokumenttyps, Ja fordert die Spalte ausdrücklich an, Nein schließt sie aus dem Basisschema aus. Dies ist von Pflichtfeld, Schreibgeschützt und Ausgeblendet getrennt. |
| **Actions** | Übersetzungs-Symbol: Titel umbenennen. Info-Symbol: woher die angezeigte Bezeichnung stammt (Ihre Übersetzung, der Standard, der Schlüssel). Drei-Punkte-Menü: *Delete*, nur für Spalten, die Ihre Organisation angelegt hat; Standardspalten können nur ausgeblendet werden. |

Zwei Schaltflächen über der Liste:

* **Create new table**: eine zweite Positionstabelle für den Dokumenttyp (zum Beispiel eine Tabelle für Nebenkosten neben der Artikeltabelle).
* **Add new table column**: öffnet den Dialog, der unter [Neue Spalte hinzufügen](adding-a-new-column.md) beschrieben ist.

## Standardspalten und eigene Spalten

Jeder Dokumenttyp wird mit einer Reihe von Standardspalten ausgeliefert (für Rechnungen: Artikelnummer, Beschreibung, Menge, Einzelpreis, Gesamtbetrag, Steuer, …). Sie gehören zu DocBits und nicht zu Ihrer Organisation, daher können sie nicht gelöscht werden; blenden Sie sie stattdessen aus. Spalten, die Sie selbst hinzufügen, gehören zu Ihrer Organisation und können gelöscht werden.

{% hint style="info" %}
**Änderungen gelten nur für neue Dokumente.** Eine Spalte, die Sie hinzufügen, ausblenden oder löschen, erscheint bei Dokumenten, die nach der Änderung hochgeladen oder neu gestartet werden. Dokumente, die sich bereits im Dashboard befinden, behalten ihre Tabelle so, wie sie extrahiert wurde. Starten Sie ein Dokument neu, um die neue Konfiguration zu übernehmen.
{% endhint %}

## Verwandte Seiten

* [Zweck und Verwendung](purpose-and-use.md): wo Tabellenspalten erscheinen
* [Neue Spalte hinzufügen](adding-a-new-column.md)
* [Spalten bearbeiten und löschen](editing-and-deleting-columns.md)
* [Bewährte Vorgehensweisen](best-practices-2.md)
* [Fehlerbehebung](troubleshooting-1.md)
* [Positionsfelder und Tabellen trainieren](../../../../setup/document-training/training-line-fields-table-training/README.md): DocBits beibringen, wo sich die Tabelle eines Lieferanten befindet
* [KI-Tabelle](../../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): was der Benutzer in der Validierungsmaske sieht

## Use AI: Standard, Ja oder Nein

Öffnen Sie die [Tabellenspalten](README.md) des richtigen Dokumenttyps und der richtigen Tabelle. **Use AI** ist eine dreistufige Auswahl, keine Checkbox. Die Auswahl wird unmittelbar gespeichert.

| Auswahl im aktuellen Menü | Bedeutung für das Basisschema |
| --- | --- |
| **Default · requested** oder **Default · not requested** | Übernimmt die DocBits-Vorgabe für diesen Dokumenttyp und Spaltennamen. Standard bedeutet weder immer an noch immer aus. |
| **Yes · requested** | Fordert diese konfigurierte Spalte ausdrücklich von der KI an. |
| **No · not requested** | Fordert sie im Basisschema nicht an, auch wenn sie zur KI-Standardauswahl gehört. |

Zurück auf **Default** entfernt die ausdrückliche Ja-/Nein-Auswahl. Eine neu angelegte eigene Spalte gehört normalerweise nicht zur KI-Standardauswahl; setzen Sie sie auf **Yes**, wenn die KI sie liefern soll. Die Liste der KI-Standardspalten ist nicht identisch mit allen mitgelieferten Spalten. Die angezeigte Wirkung und die Vorschau sind maßgeblich.

**Required**, **Read Only** und **Hidden** haben andere Aufgaben: Vollständigkeitsprüfung, Bearbeitbarkeit und Sichtbarkeit. Keines dieser Merkmale ersetzt die KI-Auswahl. **No** löscht weder die Spalte noch vorhandene Werte und verhindert nicht, dass Regeln, Skripte oder andere Quellen Werte liefern. Lieferantentraining und zusätzliche KI-Tags können den Laufauftrag erweitern; lösen Sie Widersprüche dort ebenfalls auf. Ein rein regelbasiertes Ergebnis wird durch den Structured-Output-Schalter nicht automatisch ersetzt.

[Structured Output für Tabellen](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
