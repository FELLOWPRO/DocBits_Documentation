# Export mit alternativem Export

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## Wann sollte diese Karte verwendet werden?

Verwenden Sie diese Dann-Aktion für den alternativen Export, der für den aktuellen Dokumenttyp konfiguriert ist. Konfigurieren und validieren Sie diese Route, bevor Sie die Aktion hinzufügen.

## Die Konfiguration ergibt sich aus dem Dokumenttyp

Die Karte verfügt über keinen Exportkonfigurationsselektor. Es liest, ob der alternative Export aktiviert ist, die alternative Exportkonfiguration und den Status nach dem Export aus den Dokumenttypeinstellungen. Intern sind dies `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` und `DOC_ALTERNATE_EXPORT_STATUS`.

Ein explizit deaktivierter alternativer Export führt zu einer fehlgeschlagenen Bedingung. Fehlende Aktivierungsdaten, Konfigurationen oder Ergebnisstatus werden gemeldet, anstatt stillschweigend die Standardroute zu ersetzen. Der Exportauftrag prüft anstehende Aufgaben.

## Überprüfen Sie das Ergebnis

Überprüfen Sie das Kartenprotokoll, den Exportverlauf, den Dokumentenstatus und das autorisierte Testziel. Eine Anfrage, ein Timeout oder eine Statusänderung allein beweist nicht, dass die Daten das Ziel erreicht haben. Überprüfen Sie den Exportverlauf, bevor Sie einen Vorgang wiederholen, der zu Duplikaten führen könnte.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Alternatives Exportbeispiel

**Konfiguration:** Bereiten Sie den synthetischen Dokumenttyp `DEMO_INVOICE` mit aktiviertem alternativen Export, einer autorisierten Testexportkonfiguration und dem gewünschten Ergebnisstatus in seinen Dokumenttypeinstellungen vor. Fügen Sie diese Dann-Aktion nach den erforderlichen Prüfungen hinzu. Diese Karte liest diese Einstellungen; Es bietet keinen Exportkonfigurationsselektor.

**Erwartetes Ergebnis und Gegenbeispiel:** Die Aktion fordert den Export über diese alternative Konfiguration an und prüft ausstehende Aufgaben. Überprüfen Sie das Exportergebnis und das Testziel separat. Das Deaktivieren des alternativen Exports führt zu einer fehlgeschlagenen Bedingung. Eine fehlende Aktivierungseinstellung oder -konfiguration ist kein erfolgreicher Export. Führen Sie dieses Beispiel nicht für ein Buchhaltungsziel aus.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.
