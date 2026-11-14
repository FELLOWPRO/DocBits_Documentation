# Layout-Editor

Mit dem Layout-Editor ordnen Sie die Felder und Steuerelemente an, die Personen beim Validieren oder Freigeben eines Dokuments sehen. Ein Layout gehört zu einem Dokumenttyp, einer Herkunft und einem Layouttyp. Prüfen Sie diese drei Angaben oben auf der Seite, bevor Sie speichern.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## Layout öffnen

1. Öffnen Sie **Settings → Document Types**.
2. Wählen Sie den Dokumenttyp, den Sie bearbeiten möchten, und öffnen Sie **Layout Builder**. Öffnen Sie bei einem Dokumentuntertyp die Layout Builder-Aktion dieses Untertyps.
3. Prüfen Sie die Aktionsleiste. Die linke Auswahl ist die **origin** (zum Beispiel **Default**), danach folgen **Document Type** (zum Beispiel **Invoice**) und **Layout type** (zum Beispiel **Field Validation**). Jede Auswahl öffnet eine Liste; die Wahl eines anderen Eintrags lädt das entsprechende Layout. Ist der Layout Builder nicht verfügbar, muss ein Administrator das Modul möglicherweise für Ihre Organisation freischalten.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="Der Layout Builder für eine Rechnung in DocBits mit den Auswahlen für origin, Document Type und Layout type, den Reitern Structure, Fields und Elements, der Layoutfläche und dem Bereich Properties rechts"><figcaption><p>Der Layout Builder: die Auswahlen in der Aktionsleiste, die Elementlisten links, die Layoutfläche in der Mitte und der Bereich Properties rechts.</p></figcaption></figure>

## Mit der Aktionsleiste arbeiten

* **Document Type** und **Layout type** wechseln zwischen Layouts. Die Seite lädt das gewählte Layout neu.
* Neben **Save** zeigt DocBits an, ob das Layout **unsaved changes** enthält. Nach dem Speichern zeigt es, wann das Layout zuletzt gespeichert wurde.
* **Save** speichert das Layout für den gewählten Dokumenttyp, die gewählte Herkunft und den gewählten Layouttyp.
* Das Menü **More** (drei Punkte) enthält **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** und **Layout settings**. **Auto Generate template** und **Use default template** ersetzen ein individuell angeordnetes Layout; prüfen Sie deshalb zuerst den gewählten Dokumenttyp und das Layout. **Edit JSON** ist für die erweiterte Konfiguration gedacht und sollte nur verwendet werden, wenn Sie das Vorlagenformat kennen.
* Wenn Sie die Seite mit ungespeicherten Änderungen verlassen, fragt DocBits, ob sie gespeichert oder verworfen werden sollen.

## Elemente finden: Structure, Fields, Elements

Die linke Seite hat drei Reiter:

| Reiter | Verwendung |
| --- | --- |
| **Structure** | Das Layout als Baum anzeigen. Gruppen und ihre Felder erscheinen in der Reihenfolge der Layoutfläche, mit der Anzahl der platzierten und der verfügbaren Felder. |
| **Fields** | Alle für den Dokumenttyp konfigurierten Felder, nach Feldgruppe gruppiert und standardmäßig eingeklappt. Der Filter wechselt zwischen **All**, **Unused** und **Hidden**; der technische Feldname steht unter der Feldbezeichnung. |
| **Elements** | Darstellungs- und Interaktionselemente wie Text, Label, Check Box, Trennlinien, Tabellen, Schaltflächen und Untergruppen. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="Der Reiter Structure des Layout Builders mit den aufgeklappten Gruppen Invoice details, Payment details, Purchase Order und Delivery Details und ihren Feldern"><figcaption><p>Der Reiter Structure zeigt das erstellte Layout als Baum aus Gruppen und Feldern.</p></figcaption></figure>

Wählen Sie einen Eintrag, um ihn hinzuzufügen, oder ziehen Sie ihn auf die Layoutfläche. Ein Gruppentitel sagt der Person, die das Dokument validiert, was in diesen Abschnitt gehört. Wiederverwendbare Dokumentfelder erstellen oder benennen Sie zuerst unter [Document Types](README.md) um.

## Auf der Layoutfläche arbeiten

* **Main layout** zeigt das Layout des Dokuments selbst. **Table** zeigt das Tabellenlayout für Positionen.
* **Document** öffnet oder schließt das Beispieldokument neben der Layoutfläche, sodass Sie das Layout mit einem echten Dokument vergleichen können.
* Gruppen werden als Karten dargestellt; die Felder innerhalb einer Gruppe lassen sich in Zeilen anordnen und mit unterschiedlichen Breiten versehen.

## Eigenschaften eines Elements ändern

Wählen Sie ein Element oder eine Gruppe auf der Layoutfläche. **Properties** rechts ist immer sichtbar und in Abschnitte gegliedert:

* **Display** – Bezeichnung, Feldname, Position der Bezeichnung und Elementbreite.
* **Behaviour** – schreibgeschützt, ausgeblendet und Tab-Reihenfolge.
* **Values & lists** – die für das Element angebotenen Werte.
* **Automation** – Regeln, die das Element befüllen oder ändern.
* **Borders & spacing** – das Erscheinungsbild des Elements.

Wählen Sie für die Breite eine der Vorgaben (25, 33, 50, 66, 75 oder 100 Prozent), statt einen Wert einzutippen; prüfen Sie das Ergebnis auf der Layoutfläche. Welche Abschnitte und Optionen erscheinen, hängt vom gewählten Element ab. Weitere Details finden Sie unter [Feldeigenschaften konfigurieren](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Schaltflächenbeschriftungen übersetzen

Schaltflächen wie **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** und **Reject** beziehen ihre Beschriftung aus einem Übersetzungsschlüssel. Die Ansicht zeigt die Beschriftung in der Sprache der Person, die das Layout öffnet. Hat der Schlüssel keinen Text für diese Sprache, zeigt DocBits die im Layout gespeicherte Beschriftung.

* Eine eigenständige Schaltfläche hat ein Feld **Translation Key** unter **Properties**.
* **Invoice Buttons** fasst mehrere Schaltflächen zusammen. Legen Sie den Schlüssel für eine einzelne untergeordnete Schaltfläche fest oder je untergeordneter Schaltfläche einen Schlüssel in der Liste im Bereich der Gruppe.

Layouts, die vor dieser Änderung erstellt wurden, behalten ihre Beschriftungen: DocBits trägt für sie den Standardschlüssel des jeweiligen Schaltflächentyps ein. Layouts, die mit einem Schlüssel gespeichert werden, behalten diesen Schlüssel, auch nach dem Neuladen.

## Save and go back to Dashboard

Eine Schaltfläche vom Typ **Save and go back to Dashboard** speichert die Dokumentwerte wie **Save** und öffnet anschließend das Dashboard. Der Typ eignet sich für Layouts, in denen eine prüfende Person eine Warteschlange von Dokumenten nacheinander abarbeitet.

* Fügen Sie auf der Layoutfläche ein Schaltflächenelement hinzu und wählen Sie den Typ in seinen **Properties**.
* Schlägt das Speichern fehl, bleibt die Schaltfläche auf dem Validierungsbildschirm und öffnet das Dashboard nicht, sodass das Problem zuerst behoben werden kann.
* Die Beschriftung wird wie die Beschriftung jeder anderen Schaltfläche aufgelöst; siehe *Schaltflächenbeschriftungen übersetzen* oben.

## Prüfen und speichern

Ordnen Sie die Gruppen und Felder an, prüfen Sie das Layout auf der Layoutfläche und verwenden Sie **Save** in der Aktionsleiste, sobald das Ergebnis passt. Zu herkunftsspezifischen Layouts siehe [Herkunfts-Layouts](origin-layouts.md).

{% hint style="info" %}
Die Screenshots zeigen synthetische Einstellungen in der DocBits-Testorganisation, in der in der Anwendung Englisch ausgewählt ist. Beim Aufnehmen wurde kein Layout gespeichert oder ersetzt.
{% endhint %}
