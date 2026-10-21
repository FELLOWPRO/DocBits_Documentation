# Workflow-Exportkarten und Dokumentstatus

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-11f244132c25-de.png" alt="Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus."><figcaption><p>Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus.</p></figcaption></figure>

Wählen Sie, ob der Export sofort erfolgen soll oder ob eine Konfiguration am Ende des Laufs für den endgültigen Export in die Warteschlange gestellt werden soll. Diese Auswahlmöglichkeiten sind unabhängig vom Status, den das Dokument nach einem erfolgreichen Export haben sollte.

| Karte | Wenn der Export ausgeführt wird | Wichtige Einstellungen |
| --- | --- | --- |
| Export mit Validierung starten (`EXPORT`) | Startet den Export mit den konfigurierten Exporteinstellungen des Dokuments. | Validierung und ab v4 Status nach dem Export. |
| Export mit Exportkonfiguration (`ACTION_EXPORT_WITH`) | Exportiert unter Verwendung der ausgewählten Konfiguration während der Kartenausführung. | Konfiguration exportieren, ausstehende Aufgaben ignorieren und ab v3 Status nach dem Export. |
| Verzögerter Export mit Konfiguration (`ACTION_EXPORT_WITH_CONFIG_DEFERRED`) | Sammelt die Konfiguration für den endgültigen Export am Ende des Laufs. Das Hinzufügen einer Exportanforderung zur Warteschlange beweist nicht, dass der endgültige Export erfolgreich war. | Konfiguration exportieren, ausstehende Aufgaben ignorieren und ab v3 Status nach dem Export. |
| Alternativer Export (`ACTION_ALTERNATE_EXPORT`) | Verwendet die auf seiner Karte dokumentierte alternative Exportroute. | Gehen Sie nicht davon aus, dass es dieselben Versions- oder Statusoptionen wie die drei oben genannten Karten hat. |

## Status nach dem Export

| Wert | Bedeutung nach erfolgreichem Export | Typische Verwendung |
| --- | --- | --- |
| `finished` | Exportiert und geschlossen. | Die Bearbeitung ist abgeschlossen. |
| `exported` | Exportiert, bleibt aber zur weiteren Verarbeitung geöffnet. | Die Genehmigung oder ein anderer Workflow muss noch folgen. |

Export starten v4, Export mit Exportkonfiguration v3 und in die Warteschlange gestellter Export v3 bieten diese Auswahl. Frühere Versionen behalten `finished` bei. Eine fehlende Auswahl fällt auf `finished` zurück und wird protokolliert; Ein ungültiger Wert wird vor dem Export abgelehnt. Eine gespeicherte alte Karte übernimmt nicht das neue Verhalten, nur weil eine neue Vorlagenversion vorhanden ist. Überprüfen Sie die Kartenversion und testen Sie alle expliziten Upgrades erneut.

Die Dokumentstatusbedingungen und die Karte „Status ändern“ bieten auch `exported` in Releases an, die die entsprechende Statusaktualisierung enthalten. Eine Statusänderung allein führt noch nicht zu einem Export. Verwenden Sie das Exportergebnis und die Protokolle, um festzustellen, ob die Daten tatsächlich ihr Ziel erreicht haben.

## Sofortiger Export mit Konfiguration

1. Fügen Sie die Karte unter Dann hinzu und wählen Sie eine gültige Exportkonfiguration aus.
2. Wählen Sie aus, ob ausstehende Aufgaben ignoriert werden sollen. Lassen Sie diese Option deaktiviert, wenn Aufgaben den Export blockieren müssen.
3. Wählen Sie in Version 3 bewusst `finished` oder `exported` aus.
4. Testen Sie mit einem Dokument in einem zulässigen Verarbeitungsstatus und überprüfen Sie dann das Kartenergebnis und das Ziel.

Wenn ausstehende Aufgaben den Export verhindern, wird auf der Karte ein abgelehnter Export vermerkt. Lösen Sie die Aufgaben und veranlassen Sie den vorgesehenen Workflow-Auslöser oder versuchen Sie es erneut. Diese Karte verspricht nicht, automatisch zu warten und fortzufahren. Ein Timeout beweist auch nicht, dass das Remote-System nichts unternommen hat; Überprüfen Sie den Exportverlauf, bevor Sie einen Vorgang wiederholen, der zu Duplikaten führen könnte.

## Verzögerter Export mit Konfiguration

Fügen Sie diese Karte hinzu, wenn der Export für den letzten Schritt des Laufs erfasst werden soll. Wählen Sie die Konfiguration, die Einstellung für offene Aufgaben und den Ergebnisstatus aus. Die Karte speichert die angeforderte Konfiguration; Überprüfen Sie das endgültige Exportergebnis separat. Die Nachricht zur Bestätigung der in die Warteschlange gestellten Anfrage ist keine Bestätigung einer Buchung im ERP-System.

Wählen Sie beispielsweise `exported` aus, wenn bei einem erfolgreichen Export das Dokument für eine spätere Genehmigung verfügbar bleiben muss. Wählen Sie `finished`, wenn keine weitere Verarbeitung erforderlich ist. Überprüfen Sie den Endzustand sowie das Exportziel erneut.

## Erforderliche Kontrollen

Testen Sie eine gültige Konfiguration, eine fehlende Konfiguration, ausstehende Aufgaben mit beiden Einstellungen und beiden Ergebnisstatus. Testen Sie die bereits in einem bestehenden Workflow verwendete Version, bevor Sie sie ändern. Überprüfen Sie bei einem Export in der Warteschlange die endgültige Ausführung. Für einen sofortigen Export überprüfen Sie das eigene Ergebnis. Überprüfen Sie [Workflow-Protokolle](../workflow-logs.md) und verwechseln Sie eine übersprungene Karte nicht mit Erfolg.
