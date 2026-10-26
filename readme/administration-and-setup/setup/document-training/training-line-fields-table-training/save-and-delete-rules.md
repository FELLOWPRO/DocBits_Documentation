# Regeln speichern und löschen

Nachdem Sie das Training oder die Korrektur einer Tabelle abgeschlossen haben, ist es wichtig, **Ihre Regeln zu speichern**, damit DocBits sie automatisch auf zukünftige Dokumente desselben Lieferanten anwenden kann.

### Regeln speichern

Nachdem alle Spalten und Korrekturen definiert wurden:

1. Klicken Sie oben auf die Schaltfläche **Regeln speichern**.
2. Ein Regelzähler bestätigt, wie viele Extraktionsregeln gespeichert wurden.

Dies stellt sicher, dass DocBits Ihr trainiertes Layout automatisch beim nächsten Mal verwendet, wenn es ein ähnliches Dokument sieht.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-save-and-delete-rules-save-rules-de-20261009.png" alt="Ansicht der Tabellenauswertung im Trainingsmodus mit den Schaltflächen Speichern, Regeln speichern und Regeln löschen sowie einem Regelzähler von 3."><figcaption><p>Regeln speichern legt die Regeln ab; der Zähler zeigt, wie viele Regeln vorhanden sind.</p></figcaption></figure>

Wie Sie Spalten im Vorfeld anlegen und zuordnen, ist unter [Definieren von Tabellen und Spalten](defining-tables-and-columns.md) beschrieben; wie Sie die Extraktion verbessern, unter [Strukturierung und Verbesserung der Tabellenauswertung in DocBits](improving-table-extraction-with-regex.md).

### Regeln löschen

Sie können gespeicherte Regeln mithilfe der Schaltfläche **Regeln löschen** entfernen, wenn sie falsch konfiguriert wurden oder wenn sich das Layout des Dokuments erheblich geändert hat.

<mark style="color:red;">**Warnung**</mark>: Das Löschen von Regeln wirkt sich auf alle Dokumente desselben Lieferanten mit demselben Layout aus. Sie müssen die **Extraktion der Tabelle von Grund auf neu trainieren**.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-save-and-delete-rules-delete-rules-de-20261009.png" alt="Bestätigungsdialog, der nach dem Klick auf Regeln löschen erscheint."><figcaption><p>Das Löschen von Regeln muss bestätigt werden.</p></figcaption></figure>

Wie Sie den Trainingsmodus starten und die Tabellenauswertung erneut trainieren, lesen Sie unter [Schulung Linienfelder/Tabelle Schulung](README.md).
