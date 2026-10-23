# Layout-Editor

Mit dem Layout-Editor ordnen Sie die Felder und Steuerelemente an, die Personen beim Validieren oder Freigeben eines Dokuments sehen. Ein Layout gehört zu genau einem Dokumenttyp, einer Herkunft und einem Layouttyp – prüfen Sie diese drei Angaben oben auf der Seite, bevor Sie speichern.

## Layout öffnen

1. Öffnen Sie **Einstellungen → Dokumenttypen**.
2. Wählen Sie den Dokumenttyp aus, den Sie bearbeiten möchten, und öffnen Sie den **Layout-Editor**. Bei einem Untertyp eines Dokuments öffnen Sie die Aktion Layout-Editor dieses Untertyps.
3. Prüfen Sie die Kopfzeile. Der linke Selektor ist die **Herkunft** (zum Beispiel **Standard**), gefolgt vom **Dokumenttyp** (zum Beispiel **Rechnung**) und dem **Layouttyp** (zum Beispiel **Feldvalidierung**). Jeder Selektor öffnet eine Liste; mit einer anderen Auswahl wird das jeweilige Layout geladen. Ist der Layout-Editor nicht verfügbar, muss ein Administrator das Modul möglicherweise für Ihre Organisation freischalten.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-de.png" alt="Der Layout-Editor für eine Rechnung in DocBits, mit den Selektoren für Herkunft, Dokumenttyp und Layouttyp, den Tabs Struktur, Felder und Elemente, der Layoutfläche und dem Bereich Eigenschaften rechts"><figcaption><p>Der Layout-Editor: die Selektoren in der Kopfzeile, die Elementlisten links, die Fläche in der Mitte und der Bereich Eigenschaften rechts.</p></figcaption></figure>

## Mit der Kopfzeile arbeiten

* Über **Dokumenttyp** und **Layouttyp** wechseln Sie zwischen Layouts. Die Seite lädt das gewählte Layout neu.
* Neben **Speichern** zeigt DocBits an, ob das Layout **Nicht gespeicherte Änderungen** enthält. Nach dem Speichern sehen Sie, wann das Layout zuletzt gespeichert wurde.
* **Speichern** sichert das Layout für den ausgewählten Dokumenttyp, die Herkunft und den Layouttyp.
* Das Menü **Mehr** (drei Punkte) enthält **Vorlage automatisch generieren**, **Standardlayout auf die Herkunft anwenden**, **Standardvorlage verwenden**, **JSON bearbeiten**, **JSON kopieren** und **Layout-Einstellungen**. **Vorlage automatisch generieren** und **Standardvorlage verwenden** ersetzen ein individuelles Layout – prüfen Sie daher zuerst den ausgewählten Dokumenttyp und das Layout. **JSON bearbeiten** ist für die erweiterte Konfiguration gedacht und sollte nur verwendet werden, wenn Sie das Vorlagenformat kennen.
* Verlassen Sie die Seite mit nicht gespeicherten Änderungen, fragt DocBits, ob diese gespeichert oder verworfen werden sollen.

## Elemente finden: Struktur, Felder, Elemente

Die linke Seite hat drei Tabs:

| Tab | Wofür |
| --- | --- |
| **Struktur** | Zeigt das Layout als Baum. Gruppen und ihre Felder werden in der Reihenfolge aufgeführt, in der sie auf der Fläche erscheinen, mit der Anzahl der platzierten und der verfügbaren Felder. |
| **Felder** | Alle für den Dokumenttyp konfigurierten Felder, nach Feldgruppe gruppiert und standardmäßig eingeklappt. Der Filter wechselt zwischen **Alle**, **Nicht verwendet** und **Versteckt**; der technische Feldname steht unter der Bezeichnung des Feldes. |
| **Elemente** | Steuerelemente für Darstellung und Interaktion wie Text, Bezeichnung, Kontrollkästchen, Trennlinien, Tabellen, Schaltflächen und Untergruppen. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-de.png" alt="Der Tab Struktur des Layout-Editors mit den aufgeklappten Gruppen Rechnungsdetails, Zahlungsdetails, Bestellung und Lieferdetails samt ihren Feldern"><figcaption><p>Der Tab Struktur zeigt das erstellte Layout als Baum aus Gruppen und Feldern.</p></figcaption></figure>

Wählen Sie ein Element aus, um es hinzuzufügen, oder ziehen Sie es auf die Fläche. Der Titel einer Gruppe sagt der Person, die das Dokument validiert, was in diesen Abschnitt gehört. Wiederverwendbare Dokumentfelder erstellen oder benennen Sie zuerst unter [Dokumenttypen](README.md) um.

## Auf der Fläche arbeiten

* **Hauptlayout** zeigt das Layout des Dokuments selbst. **Tabelle** zeigt das Tabellenlayout für Positionen.
* **Dokument** öffnet oder schließt das Beispieldokument neben der Fläche, sodass Sie das Layout mit einem echten Dokument vergleichen können.
* Gruppen werden als Karten dargestellt; die Felder innerhalb einer Gruppe lassen sich in Zeilen anordnen und unterschiedlich breit machen.

## Eigenschaften eines Elements ändern

Wählen Sie ein Element oder eine Gruppe auf der Fläche aus. **Eigenschaften** rechts ist immer sichtbar und in Abschnitte gegliedert:

* **Darstellung** – Bezeichnung, Feldname, Position der Bezeichnung und Breite des Elements.
* **Verhalten** – schreibgeschützt, versteckt und Tab-Index.
* **Werte & Listen** – die für das Element angebotenen Werte.
* **Automatisierung** – Regeln, die das Element befüllen oder verändern.
* **Rahmen & Abstände** – das Erscheinungsbild des Elements.

Wählen Sie für die Breite eine der Vorgaben (25, 33, 50, 66, 75 oder 100 Prozent), statt einen Wert einzugeben, und prüfen Sie das Ergebnis auf der Fläche. Welche Abschnitte und Optionen erscheinen, hängt vom ausgewählten Element ab. Weitere Details finden Sie unter [Feldeigenschaften konfigurieren](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Prüfen und speichern

Ordnen Sie die Gruppen und Felder an, prüfen Sie das Layout auf der Fläche und verwenden Sie **Speichern** in der Kopfzeile, sobald das Ergebnis passt. Zu herkunftsspezifischen Layouts siehe [Herkunfts-Layouts](origin-layouts.md).

{% hint style="info" %}
Die Screenshots zeigen synthetische Einstellungen in der DocBits-Testorganisation mit deutscher Spracheinstellung in der Anwendung. Beim Erstellen der Aufnahmen wurde kein Layout gespeichert oder ersetzt.
{% endhint %}
