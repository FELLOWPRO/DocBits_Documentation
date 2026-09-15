# KI-Tabelle

Die KI-extrahierte Tabelle ist die Positionstabelle, die DocBits mit KI liest, wenn ein Lieferant keine trainierten Tabellenregeln hat. Sie erscheint im Validierungsbildschirm unterhalb der Kopffelder. Diese Seite beschreibt, wann Sie sie erhalten, wie Sie sie erneut ausführen und wie Sie beeinflussen, was sie extrahiert.

## Wann Sie die KI-Tabelle erhalten

* Ein Administrator hat **AI-Tabellen-Extraktion** eingeschaltet (Einstellungen → Dokumentenverarbeitung → Klassifizierung und Extraktion). Ist sie ausgeschaltet, zeigt der Tabellenbereich *AI Table will display here. Enable in …* (Hier wird die KI-Tabelle angezeigt. Aktivieren in …).
* Der Lieferant hat **keine gespeicherten Regeln**. Sobald jemand die Tabelle des Lieferanten trainiert und auf *Regeln speichern* klickt, ersetzen die gespeicherten Regeln die KI-Tabelle für diesen Lieferanten; die Zeilen erscheinen dann im Tab *Extrahierte Tabelle* statt im Tab *KI Extrahierte Tabelle*.
* Ausnahme: Spalten, die in den Tabellenspalten-Einstellungen mit **KI nutzen** markiert sind, werden auch bei Lieferanten mit gespeicherten Regeln von der KI gefüllt, siehe [KI pro Spalte nutzen](#ki-pro-spalte-nutzen).

Welche KI-Stufe die Tabelle liest (Fast, Full, Nexus), wird pro Organisation festgelegt und kann pro Lieferant unter *Weitere Einstellungen* im Validierungsbildschirm überschrieben werden, siehe [Lieferantenspezifisches KI-Modell](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Die KI-Tabelle erneut extrahieren

Verwenden Sie dies, wenn Zeilen fehlen oder eine Spalte verschoben ist und die KI es erneut versuchen soll, zum Beispiel nach dem Hinzufügen eines [Tags](ai-table-tags.md):

1. Fügen Sie im Feld unter der Tabelle [Tags](ai-table-tags.md) hinzu oder ändern Sie sie und klicken Sie auf **Anwenden**. Die KI baut die Tabelle für dieses Dokument mit Ihren Tags und Spaltenänderungen neu auf; für den Lieferanten wird noch nichts gespeichert. Hat das Dokument mit Bestellungen abgeglichene Positionen, warnt DocBits, dass die Zuordnungen durch den Neuaufbau entfernt werden.
2. Zufrieden mit dem Ergebnis? Klicken Sie auf **Speichern** (*Regeln speichern*), damit das nächste Dokument dieses Lieferanten auf dieselbe Weise extrahiert wird.
3. Um von vorn zu beginnen, klicken Sie auf **Löschen** (*Regeln löschen*): DocBits bestätigt *Rules has been deleted successfully* (Regeln wurden erfolgreich gelöscht) und führt die KI-Extraktion ohne gespeicherte Tags oder Formatierungen erneut aus.

*Regeln löschen* entfernt die für diesen Lieferanten gespeicherten Tags und Formatierungsregeln, nicht die Konfiguration der Tabellenspalten. Um das gesamte Dokument (Kopf und Tabelle) erneut zu extrahieren, nachdem ein Administrator Einstellungen oder Spalten geändert hat, verwenden Sie stattdessen *Neustart* im Dokumentmenü des Dashboards.

## KI pro Spalte nutzen

Jede Tabellenspalte hat ein Kennzeichen **KI nutzen** (Einstellungen → Globale Einstellungen → Dokumenttypen → [Tabellenspalten](../../../admin-section/settings/global-settings/document-types/table-columns.md)). Ist es gesetzt, füllt die KI diese Spalte auch dann, wenn der Lieferant gespeicherte Regeln hat; die übrigen Spalten kommen weiterhin aus den Regeln. Typische Anwendung: eine Freitext-Beschreibungsspalte, die trainierte Regeln schlecht erfassen, oder ein Wert, der auf der Seite die Position wechselt.

Beachten Sie, dass die KI diese Spalte dann aus der gesamten Zeile errät. Setzt sie dort durchgehend den falschen Wert ein (zum Beispiel die Positionssumme in *Charges*), schlägt die Positionssummenprüfung in jeder Zeile fehl. Schalten Sie in diesem Fall *KI nutzen* für diese Spalte aus, oder fügen Sie ein Tag hinzu, das der KI sagt, was die Spalte ist.

## Strukturierte Extraktion

Ist **Strukturierte Extraktion nutzen (KI)** in den Organisationseinstellungen aktiviert, liefert die KI die Tabelle in einer festen Struktur, die direkt auf die konfigurierten Tabellenspalten abgebildet wird, statt die Spaltenüberschriften des Lieferanten zu übernehmen. Die Spaltennamen entsprechen dann immer Ihrer Konfiguration; eine Spalte, die der Lieferant druckt, die Sie aber nicht konfiguriert haben, wird nicht extrahiert. Bitten Sie Ihren Administrator, die Option einzuschalten, wenn die Überschriften der Lieferanten stark variieren und Sie viel Zeit mit dem Neuzuordnen verbringen.

## Arbeiten mit der extrahierten Tabelle

Hier finden Sie die wichtigsten Funktionen und Anwendungshinweise:

* **Spalten löschen**: Wenn bestimmte Spalten in der extrahierten Tabelle nicht benötigt werden, können Benutzer sie ganz einfach entfernen, indem sie auf das Symbol "Spalte löschen" (dargestellt durch drei vertikale Punkte) neben der Spaltenüberschrift klicken. Dies hilft, die Tabelle übersichtlicher zu gestalten und sich nur auf die relevanten Informationen zu konzentrieren.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Währungsformat ändern**: Das Währungsformat kann geändert werden, indem das gewünschte Format aus dem Dropdown-Menü neben dem Feld "Währung" ausgewählt wird. So wird sichergestellt, dass die Währungswerte im bevorzugten Format angezeigt werden, was die Interpretation und Analyse der Finanzdaten erleichtert.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Nicht zugeordnete Spalten ein-/ausblenden**: Standardmäßig sind nur die zugeordneten Spalten (Spalten mit extrahierten Daten) in der Tabelle sichtbar. Benutzer können jedoch wählen, ob sie die nicht zugeordneten Spalten ein- oder ausblenden möchten, indem sie auf die Schaltfläche "Nicht zugeordnete Spalten ausblenden" oder "Nicht zugeordnete Spalten anzeigen" am unteren Rand der Tabelle klicken. Diese Funktion ist nützlich, wenn Benutzer alle verfügbaren Spalten überprüfen möchten, auch wenn diese aktuell keine Daten enthalten.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Tabellenüberschriften ändern**: Die Tabellenüberschriften (Spaltennamen) können geändert werden, indem Sie auf die Überschrift klicken und den gewünschten Namen eingeben. Mit dieser Funktion können Benutzer die Spaltennamen anpassen, um sie besser an ihre Terminologie oder Vorlieben anzupassen, wodurch die Daten lesbarer und verständlicher werden.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Änderungen speichern**: **Speichern** neben den Tags (Tooltip *Regeln speichern*) speichert die aktuelle Spaltenzuordnung, die ausgeblendeten Spalten und die Tags für diesen Lieferanten. Das nächste Dokument des Lieferanten wird damit extrahiert.

Diese Funktionen geben Ihnen Kontrolle über die extrahierten Daten. Benötigt derselbe Lieferant jedes Mal dieselben Korrekturen, trainieren Sie stattdessen die Tabelle einmal, siehe [Schulung Linienfelder/Tabelle Schulung](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md); die KI-Tabelle wird dann für diesen Lieferanten nicht mehr verwendet.
