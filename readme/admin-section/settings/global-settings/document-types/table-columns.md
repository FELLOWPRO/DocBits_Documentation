# Tabellenspalten

Tabellenspalten legen fest, welche Spalten die Positionstabelle eines Dokumenttyps hat: was DocBits in jede Spalte extrahiert, was der Benutzer im Validierungsbildschirm sieht und was beim Export an das ERP gesendet wird.

**Wo:** Einstellungen → Globale Einstellungen → Dokumenttypen → Tabellenspalten

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Liste der Tabellenspalten mit den Kennzeichen Erforderlich, Schreibgeschützt, Versteckt und KI nutzen pro Spalte"><figcaption><p>Tabellenspalten: eine Zeile pro Spalte, die Kennzeichen werden direkt in der Liste umgeschaltet</p></figcaption></figure>

## Was Sie sehen

Jede Zeile ist eine Spalte einer Tabelle. Die Liste zeigt:

| Spalte | Bedeutung |
|---|---|
| **Spaltenname** | Technischer Name, der aus dem Titel erzeugt wird (Großbuchstaben, Unterstriche). Wird in Skripten, Export-Mappings und der API verwendet. Kann nachträglich nicht geändert werden. |
| **Titel** | Beschriftung, die im Validierungsbildschirm angezeigt wird. Ändern Sie sie über das Übersetzungssymbol in der Spalte *Aktionen* (*Übersetzungsschlüssel aktualisieren*). |
| **Spaltentyp** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` oder `CURRENCY`. Bestimmt Validierung und Formatierung. |
| **Name der Tabelle** | Die Tabelle, zu der die Spalte gehört, zum Beispiel `INVOICE_TABLE`. |
| **Erforderlich** | Das Dokument kann nicht freigegeben werden, solange diese Spalte in einer Zeile leer ist. |
| **Schreibgeschützt** | Benutzer sehen den Wert, können ihn aber nicht bearbeiten. |
| **Versteckt** | Die Spalte wird weder angezeigt noch exportiert. Damit schalten Sie Standardspalten ab, die Sie nicht benötigen. |
| **KI nutzen** | Die KI-Tabellenextraktion füllt diese Spalte, auch wenn ein Lieferant trainierte Regeln hat. |
| **Aktionen** | Übersetzungssymbol: Titel umbenennen. Info-Symbol: woher die angezeigte Beschriftung stammt (Ihre Übersetzung, der Standard, der Schlüssel). Drei-Punkte-Menü: *Löschen*, nur für Spalten, die Ihre Organisation angelegt hat; Standardspalten können nur versteckt werden. |

Zwei Schaltflächen über der Liste:

* **Neue Tabelle erstellen**: eine zweite Positionstabelle für den Dokumenttyp (zum Beispiel eine Tabelle für Zuschläge neben der Artikeltabelle).
* **Neue Tabellenspalte hinzufügen**: öffnet den Dialog, der im Abschnitt [Neue Spalte anlegen](#neue-spalte-anlegen) beschrieben ist.

## Standardspalten und eigene Spalten

Jeder Dokumenttyp wird mit einem Satz Standardspalten ausgeliefert (für Rechnungen: Artikelnummer, Beschreibung, Menge, Einzelpreis, Gesamtbetrag, Steuer, …). Sie gehören DocBits, nicht Ihrer Organisation, und können daher nicht gelöscht werden; verstecken Sie sie stattdessen. Spalten, die Sie selbst hinzufügen, gehören Ihrer Organisation und können gelöscht werden.

{% hint style="info" %}
**Änderungen gelten nur für neue Dokumente.** Eine Spalte, die Sie hinzufügen, verstecken oder löschen, erscheint auf Dokumenten, die nach der Änderung hochgeladen oder neu gestartet werden. Dokumente, die bereits im Dashboard liegen, behalten ihre Tabelle so, wie sie extrahiert wurde. Starten Sie ein Dokument neu, damit es die neue Konfiguration übernimmt.
{% endhint %}

## Zweck und Verwendung

Eine Tabellenspalte ist ein Feld der Positionstabelle. Alles, was DocBits mit einer Tabelle tut (Extraktion, Validierung, Bestellabgleich, Export), arbeitet mit den hier konfigurierten Spalten.

### Wo eine Spalte auftaucht

| Ort | Was die Spalte dort bewirkt |
|---|---|
| **Validierungsbildschirm** | Eine Spalte in der Positionstabelle. Der *Titel* ist die Überschrift, der *Spaltentyp* bestimmt den Editor (Betrag, Datum, Text, Ja/Nein). Versteckte Spalten werden nicht angezeigt. |
| **Tabellentraining** | Wenn Sie die Tabelle eines Lieferanten trainieren, ordnen Sie jede erkannte Tabellenspalte einer der hier konfigurierten Spalten zu. Nur konfigurierte Spalten können zugeordnet werden. |
| **KI-Tabellenextraktion** | Die KI füllt die konfigurierten Spalten. Eine Spalte mit *KI nutzen* wird von der KI gefüllt, auch bei Lieferanten mit trainierten Regeln. |
| **Validierungsregeln** | Positionsprüfungen wie *Menge × Einzelpreis = Positionssumme* laufen auf den Standardspalten `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Bestellabgleich (PO-Matching)** | Benötigt die Standardspalten Artikelnummer, Einzelpreis, Menge und Gesamtbetrag. Ohne sie zeigt das Dokument *Line Item Table is missing Mandatory column for PO* (In der Positionstabelle fehlt eine obligatorische Spalte für die Bestellung). |
| **Export** | Jede nicht versteckte Spalte ist Teil der Positionsdaten, die an das ERP gesendet werden. Das Export-Mapping referenziert den *Spaltennamen*. |
| **Skripte** | Skripte lesen und schreiben Spalten über den *Spaltennamen*, zum Beispiel `row["TOTAL_AMOUNT"]`. |

### Geltungsbereich

* Tabellenspalten werden **pro Tabelle** konfiguriert, und eine Tabelle gehört zu einem **Dokumenttyp**. Rechnungsspalten wirken sich nicht auf Lieferscheine aus.
* Die Konfiguration gilt **pro Organisation**. Unterorganisationen erben sie.
* Welche Spalten für einen bestimmten Lieferanten *gefüllt* werden, entscheidet das Training dieses Lieferanten oder die KI; die Spaltenkonfiguration legt nur fest, welche Spalten es gibt.

### Typische Gründe, die Konfiguration zu ändern

* Ein kundenspezifischer Wert muss pro Position erfasst werden (Kostenstelle, Projektnummer, interne Artikelnummer) → Spalte hinzufügen.
* Eine Standardspalte wird nie verwendet und macht den Validierungsbildschirm unübersichtlich → Spalte verstecken.
* Eine Spalte muss vor dem Export immer gefüllt sein → als *Erforderlich* markieren.
* Ein Wert kommt aus dem ERP-Lookup und darf von Benutzern nicht bearbeitet werden → als *Schreibgeschützt* markieren.
* Die KI erfasst eine Spalte besser als die trainierten Regeln (zum Beispiel Freitextbeschreibungen) → *KI nutzen* setzen.

## Neue Spalte anlegen

Legen Sie eine Spalte an, wenn pro Position ein Wert erfasst werden muss, den die Standardspalten nicht abdecken: eine Kostenstelle, eine Projektnummer, eine interne Artikelnummer.

### Bevor Sie beginnen

* Entscheiden Sie, zu welcher **Tabelle** die Spalte gehört. Die meisten Dokumenttypen haben eine Tabelle (zum Beispiel `INVOICE_TABLE`). Ist die Liste leer, klicken Sie zuerst auf **Neue Tabelle erstellen**; der Dialog fragt nur nach einem Tabellennamen.
* Entscheiden Sie den **Typ**: `AMOUNT` für Geldbeträge, `NUMBER` für Mengen, `DATE`, `BOOLEAN` für Ja/Nein, `CURRENCY` für einen ISO-Währungscode, `STRING` für alles andere. Der Typ kann nach dem Speichern nicht geändert werden.
* Prüfen Sie, ob bereits eine **Standardspalte** mit derselben Bedeutung existiert, aber versteckt ist. Versteckte Spalten stehen mit gesetztem Kennzeichen *Versteckt* in der Liste; heben Sie das Verstecken auf, statt ein Duplikat anzulegen.

### Schritte

1. Öffnen Sie **Einstellungen → Globale Einstellungen → Dokumenttypen → Tabellenspalten**.
2. Klicken Sie auf **Neue Tabellenspalte hinzufügen**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Dialog Neue Tabellenspalte hinzufügen mit Titel, Ist eine Spalte erforderlich, Spaltentyp auswählen und Tabelle auswählen"><figcaption><p>Neue Tabellenspalte hinzufügen</p></figcaption></figure>

3. Füllen Sie den Dialog aus:

| Feld | Was einzutragen ist |
|---|---|
| **Titel** | Beschriftung, die der Benutzer im Validierungsbildschirm sieht, zum Beispiel `Cost Centre`. Nur Buchstaben und Ziffern. DocBits leitet daraus den technischen *Spaltennamen* ab (`COST_CENTRE`). |
| **Ist eine Spalte erforderlich?** | Anhaken, wenn das Dokument nicht freigegeben werden darf, solange die Spalte in einer Zeile leer ist. |
| **Spaltentyp auswählen** | Siehe die Typenliste oben. |
| **Tabelle auswählen** | Die Tabelle, die die Spalte erhält. |

4. Klicken Sie auf **Weiter**. Die Spalte erscheint in der Liste; *Schreibgeschützt*, *Versteckt* und *KI nutzen* sind nicht gesetzt. Schalten Sie diese Kennzeichen bei Bedarf in der Liste um, siehe Abschnitt *Spalten bearbeiten und löschen* weiter unten.

### Nach dem Anlegen

* Die Spalte ist **auf bestehenden Dokumenten leer**. Sie wird auf Dokumenten gefüllt, die nach der Änderung hochgeladen oder neu gestartet werden.
* Bei Lieferanten mit **trainierten Regeln** öffnen Sie eines ihrer Dokumente im Tabellentraining und ordnen die neue Spalte zu, sonst bleibt die Spalte für diesen Lieferanten leer. Siehe [Definieren von Tabellen und Spalten](../../../../administration-and-setup/setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Mit **KI-Tabellenextraktion** füllt die KI die Spalte, wenn der Wert auf dem Dokument erkennbar ist. Setzen Sie *KI nutzen*, wenn der Lieferant trainierte Regeln hat, diese Spalte aber trotzdem von der KI kommen soll.
* Nehmen Sie die Spalte in das **Export-Mapping** auf, wenn das ERP sie erhalten soll, siehe [Export](../../../../administration-and-setup/settings/document-processing/export.md).

### Meldungen

| Meldung | Bedeutung |
|---|---|
| *Column name already exists* (Spaltenname existiert bereits) | Eine Spalte mit diesem technischen Namen ist bereits in der Tabelle. Wählen Sie einen anderen Titel. |
| *Column name already exists – Please activate it in Table Column settings* (Spaltenname existiert bereits - Bitte aktivieren Sie ihn in den Einstellungen der Tabellenspalten) | Eine versteckte Standardspalte trägt diesen Namen. Entfernen Sie deren Kennzeichen *Versteckt*, statt eine neue Spalte anzulegen. |
| *No table exists. Please create table before creating columns.* (Es existiert keine Tabelle. Bitte erstellen Sie eine Tabelle, bevor Sie Spalten erstellen.) | Der Dokumenttyp hat noch keine Tabelle: Klicken Sie zuerst auf **Neue Tabelle erstellen**. |

## Spalten bearbeiten und löschen

Alles außer dem Titel wird direkt in der Liste geändert; es gibt keinen Bearbeitungsdialog.

**Wo:** Einstellungen → Globale Einstellungen → Dokumenttypen → Tabellenspalten

### Ein Kennzeichen umschalten

Setzen oder entfernen Sie den Haken im Kontrollkästchen der Zeile. Die Änderung wird sofort gespeichert (*Successfully saved*).

| Kennzeichen | Ein | Aus |
|---|---|---|
| **Erforderlich** | Die Freigabe ist blockiert, solange die Spalte in einer Zeile leer ist; der Validierungsbildschirm markiert die Zelle. | Leere Zellen sind erlaubt. |
| **Schreibgeschützt** | Der Wert wird angezeigt, kann aber nicht überschrieben werden. Verwenden Sie es für Werte, die aus einem Lookup oder einem Skript stammen. | Benutzer können die Zelle bearbeiten. |
| **Versteckt** | Die Spalte verschwindet aus dem Validierungsbildschirm und aus dem Export. Ihre Daten bleiben erhalten. | Die Spalte wird angezeigt und exportiert. |
| **KI nutzen** | Die KI-Tabellenextraktion füllt diese Spalte, auch bei Lieferanten mit trainierten Regeln. | Die Spalte wird von den trainierten Regeln gefüllt, oder von der KI, wenn keine Regeln existieren. |

{% hint style="info" %}
Kennzeichen wirken auf Dokumente, die **nach** der Änderung hochgeladen oder neu gestartet werden. Offene Dokumente behalten ihre aktuelle Tabelle, bis sie neu gestartet werden.
{% endhint %}

### Den Titel umbenennen

Klicken Sie auf das Übersetzungssymbol in der Spalte *Aktionen* (*Übersetzungsschlüssel aktualisieren*), geben Sie die neue Beschriftung ein und bestätigen Sie. Das Info-Symbol daneben zeigt, welche Beschriftung gerade wirksam ist und woher sie stammt. Nur die Beschriftung ändert sich; der technische *Spaltenname* bleibt gleich, sodass Skripte, Export-Mappings und trainierte Regeln weiterhin funktionieren.

### Den Typ oder die Tabelle ändern

Nicht möglich. Verstecken Sie die Spalte (oder löschen Sie sie, wenn es Ihre eigene ist) und legen Sie eine neue mit dem richtigen Typ an.

### Eine Spalte löschen

Die Aktion Löschen wird nur für Spalten angeboten, die Ihre Organisation angelegt hat. Standardspalten können nicht gelöscht werden; verstecken Sie sie.

1. Öffnen Sie das Drei-Punkte-Menü in der Spalte *Aktionen* und wählen Sie **Löschen**. Bei Standardspalten fehlt der Eintrag.
2. Bestätigen Sie.

Was passiert:

* Die Spalte wird aus der Konfiguration entfernt. Dokumente, die **ab jetzt** verarbeitet werden, haben sie nicht mehr.
* Bereits extrahierte Dokumente behalten die Spalte und ihre Werte, bis sie neu gestartet werden.
* Trainierte Regeln, die diese Spalte zugeordnet hatten, funktionieren für die übrigen Spalten weiter; die Zuordnung der gelöschten Spalte wird ignoriert.
* Wird die Spalte in einem Export-Mapping oder einem Skript referenziert, entfernen Sie diese Referenz; andernfalls schlägt der Export oder das Skript mit einem Fehler wegen fehlender Spalte fehl.

### Eine Löschung rückgängig machen

Eine gelöschte Spalte kann nicht aus der Liste wiederhergestellt werden. Legen Sie sie mit demselben Titel erneut an: Der technische Name wird aus dem Titel abgeleitet, daher erhält eine Spalte mit demselben Titel denselben *Spaltennamen*, und bestehende Mappings passen wieder.

## Best Practices

### Behalten Sie die Standardspalten für Beträge und Mengen

Die Positionsprüfungen (*Menge × Einzelpreis = Positionssumme*) und der Bestellabgleich suchen nach den Standardspalten `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Legen Sie stattdessen eigene Spalten für diese Werte an, laufen die Prüfungen nicht, und der Bestellabgleich meldet fehlende Pflichtspalten. Benennen Sie den *Titel* um, wenn Ihnen die Formulierung nicht passt; behalten Sie die Spalte.

### Verstecken statt löschen

Standardspalten, die Sie nicht benötigen, werden versteckt, nicht gelöscht; löschen lassen sie sich ohnehin nicht. Auch bei eigenen Spalten ist Verstecken die sicherere Wahl, solange Sie nicht sicher sind, ob ein Skript oder ein Export-Mapping die Spalte noch referenziert.

### Nur als erforderlich markieren, was den Export blockiert

Jede erforderliche Spalte muss in jeder Zeile gefüllt sein, bevor ein Benutzer das Dokument freigeben kann. Verwenden Sie das Kennzeichen für Werte, die das ERP bei Fehlen ablehnt (zum Beispiel die Kostenstelle in einem Buchhaltungsexport), nicht für Werte, die lediglich nützlich sind.

### *Schreibgeschützt* für nachgeschlagene Werte verwenden

Werte, die ein Skript oder ein Stammdaten-Lookup in die Tabelle schreibt (Artikelbeschreibung aus dem Artikelstamm, Steuercode vom Lieferanten), sollten schreibgeschützt sein, damit Benutzer die Quelle korrigieren und nicht die Kopie.

### KI pro Spalte, nicht pro Lieferant

Bei einem Lieferanten mit trainierten Regeln kommen die meisten Spalten aus den Regeln korrekt heraus. Ist eine Spalte unzuverlässig (lange Beschreibungen, die umbrechen; ein Rabatt, der manchmal an anderer Stelle steht), setzen Sie *KI nutzen* nur für diese Spalte. Die Regeln behalten den Rest.

### Spalten für das ERP benennen, nicht für das Dokument

Der *Spaltenname* landet in Export-Mappings und Skripten. `COST_CENTRE` lässt sich leichter mappen als `KST` und ändert sich nicht, wenn ein Lieferant den Wert anders druckt.

### Auf einem neu gestarteten Dokument testen

Starten Sie nach einer Änderung ein bestehendes Dokument des Dokumenttyps neu und öffnen Sie es: Die neue Spalte erscheint, die versteckte ist weg, erforderliche Zellen sind markiert. Erst dann geben Sie die Änderung für die Benutzer frei.

### Eine Tabelle pro Positionsstruktur

Erstellen Sie eine zweite Tabelle nur, wenn ein Dokumenttyp wirklich zwei unabhängige Tabellen hat (zum Beispiel Artikelpositionen und eine separate Tabelle für Zuschläge). Zusätzliche leere Tabellen erscheinen auf jedem Dokument des Typs.

## Fehlerbehebung

### Die neue Spalte erscheint nicht im Validierungsbildschirm

* Das Dokument wurde verarbeitet, bevor die Spalte hinzugefügt wurde. Änderungen gelten für Dokumente, die danach hochgeladen oder neu gestartet werden: **Starten Sie das Dokument neu** (Dashboard → Dokumentmenü → Neustart).
* Die Spalte ist **versteckt**. Prüfen Sie das Kennzeichen in der Liste der Tabellenspalten.
* Die Spalte wurde einer **anderen Tabelle** hinzugefügt als der angezeigten. Der Validierungsbildschirm zeigt die Tabellen des Dokumenttyps; vergleichen Sie die Spalte *Name der Tabelle*.
* Das Dokument gehört nicht zu dem Dokumenttyp, den Sie konfiguriert haben.

### Die Spalte ist da, aber immer leer

* Der Lieferant hat **trainierte Regeln**, und die neue Spalte ist darin nicht zugeordnet. Öffnen Sie eines der Dokumente des Lieferanten im Tabellentraining und ordnen Sie die Spalte zu, oder setzen Sie *KI nutzen* für die Spalte.
* Bei KI-Extraktion ist der Wert auf dem Dokument nicht erkennbar (keine Überschrift, abgekürzt, in einer anderen Sprache). Fügen Sie ein [KI-Tabellen-Tag](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) hinzu, das die Spalte benennt, oder ordnen Sie sie im Training zu.

### „Column name already exists“

Eine Spalte mit demselben technischen Namen ist bereits in der Tabelle. Steht sie nicht in der Liste, ist es eine versteckte Standardspalte: Die Meldung lautet dann *Please activate it in Table Column settings*. Entfernen Sie *Versteckt* bei dieser Spalte, statt eine neue anzulegen.

### Die Freigabe wird durch eine erforderliche Spalte blockiert

Die Meldung an der Tabelle nennt die Spalte. Füllen Sie entweder die Zelle in jeder Zeile, oder (wenn der Wert auf diesem Dokument nicht existiert) entfernen Sie *Erforderlich* bei der Spalte, starten das Dokument neu und versuchen es erneut. Überlegen Sie, ob die Spalte überhaupt erforderlich sein sollte (siehe [Best Practices](#best-practices)).

### Die KI füllt eine Spalte mit dem falschen Wert

Typischer Fall: `CHARGES` erhält die Positionssumme, und jede Zeile fällt dann bei der Positionssummenprüfung mit *Line total does not match quantity x unit price (expected …, got …)* durch, weil Zuschläge Teil der Formel `Menge × Einzelpreis + Zuschläge` sind.

* Entfernen Sie *KI nutzen* bei der Spalte, wenn die trainierten Regeln sie korrekt erfassen.
* Hat der Lieferant keine Regeln, trainieren Sie die Tabelle einmal (Tabellentraining), damit die Spalte an die richtige Position gebunden ist, oder verstecken Sie die Spalte, wenn der Lieferant diesen Wert nie druckt.
* Als letztes Mittel schaltet *Tabellenvalidierung überspringen* in den Weiteren Einstellungen des Dokumenttyps alle Tabellenprüfungen für den gesamten Dokumenttyp ab; die Abweichung wird dann nicht mehr erkannt, leere erforderliche Spalten ebenfalls nicht.

### Bestellabgleich: „Line Item Table is missing Mandatory column“

Der Bestellabgleich benötigt die Standardspalten Artikelnummer, Einzelpreis, Menge und Gesamtbetrag. Eine davon ist versteckt oder wurde durch eine eigene Spalte ersetzt. Heben Sie das Verstecken der Standardspalte auf, oder ordnen Sie ihr den Wert im Tabellentraining zu.

### Ein Skript oder Export schlägt nach dem Löschen einer Spalte fehl

Das Skript oder das Export-Mapping referenziert noch den gelöschten *Spaltennamen*. Entfernen Sie die Referenz, oder legen Sie die Spalte mit demselben Titel erneut an; der technische Name wird aus dem Titel abgeleitet und passt wieder.

## Weitere Seiten

* [Tabellenauszug Fehlerbehebung](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): Extraktionsqualität, OCR, E-Text
* [Schulung Linienfelder/Tabelle Schulung](../../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md): DocBits beibringen, wo die Tabelle eines Lieferanten liegt
* [KI-Tabelle](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): was der Benutzer im Validierungsbildschirm sieht
