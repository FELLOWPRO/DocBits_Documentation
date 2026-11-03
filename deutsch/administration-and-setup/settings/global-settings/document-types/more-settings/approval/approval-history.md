# Genehmigungsverlauf

Der **Genehmigungsverlauf** hilft dabei, Entscheidungen im Genehmigungsworkflow eines Dokuments nachzuvollziehen. Die frühere Version dieser Seite verwies auf einen alten Pfad über **Allgemeine Einstellungen** und zeigte drei Bilder einer älteren Oberfläche, ohne die Bedienelemente zu erklären. Aktivieren Sie die Option in den aktuellen Dokumenttyp-Einstellungen und prüfen Sie das Ergebnis anschließend mit einer Testgenehmigung in Ihrer eigenen Organisation.

## Option für einen Dokumenttyp aktivieren

1. Öffnen Sie mit einem Administratorkonto **Einstellungen** → **Dokumenttypen**. Suchen Sie den Dokumenttyp, zum Beispiel **Rechnung**, und wählen Sie das **Zahnrad-Symbol**, um **Weitere Einstellungen** zu öffnen. Die Links **Layouts** und **Felder** auf der Karte führen zu anderen Editoren.

   <figure><img src="../../../../../../.gitbook/assets/dbdc567-invoice-card-native-de-20261103.png" alt="Vollständige deutsche Karte Rechnung, Standard, mit Zahnrad-Symbol rechts für Weitere Einstellungen"><figcaption><p>Öffnen Sie „Weitere Einstellungen“ bei dem Dokumenttyp, dessen Genehmigungsworkflow Sie prüfen möchten.</p></figcaption></figure>

2. Klappen Sie **Genehmigung & Ablehnung** auf und suchen Sie **Genehmigungsverlauf**. Dieser Schalter ist unabhängig von **Erste Genehmigung**, **Zweite Genehmigung** und **Genehmigungsstempel**. Die native deutsche Aufnahme zeigt den Dokumenttyp **Rechnung**. **Erste Genehmigung** und **Genehmigungsverlauf** waren bereits **ein**; **Vor dem Export genehmigen V2**, **Zweite Genehmigung** und **Genehmigungsstempel** waren **aus**. Diese vorgefundenen Zustände wurden für die Anleitung nicht geändert und sind keine Konfigurationsempfehlung.

   <figure><img src="../../../../../../.gitbook/assets/dbdc560-567-approval-panel-native-de-20261103.png" alt="Vollständiger deutscher Bereich Genehmigung und Ablehnung für Rechnung mit eingeschaltetem Genehmigungsverlauf und unveränderten übrigen Schaltern"><figcaption><p>Prüfen Sie den Schalter „Genehmigungsverlauf“ für den ausgewählten Dokumenttyp.</p></figcaption></figure>

3. Aktivieren Sie den Genehmigungsverlauf erst, nachdem Sie den vorgesehenen Genehmigungsworkflow und die Personen, die die Entscheidungen sehen dürfen, geklärt haben. Notieren Sie die vorherige Einstellung, damit ein Test damit verglichen werden kann.

## Mit einem Testdokument prüfen

Verwenden Sie ein Testdokument des eingerichteten Typs, das tatsächlich in den Genehmigungsworkflow gelangt. Lassen Sie es von einem berechtigten Testbenutzer genehmigen oder ablehnen, öffnen Sie dann die Genehmigungsansicht dieses Dokuments und prüfen Sie den verfügbaren Verlauf. Vergleichen Sie Entscheidung, Benutzer, Zeitpunkt und einen eventuell eingegebenen Kommentar mit der von Ihnen ausgeführten Aktion. Bei einem Workflow mit mehr als einer genehmigenden Person prüfen Sie die Reihenfolge nach jeder Entscheidung. Ist kein Verlauf sichtbar, prüfen Sie Dokumenttyp, Workflow-Status, Schalter und Ansichtsberechtigungen, bevor Sie es als Dokumentations- oder Produktfehler behandeln.

Die beiden nativen Dev-Aufnahmen belegen den aktuellen Einstellungsweg und die sichtbaren Schalter. Für diese Aufnahmen wurde kein Dokument genehmigt oder abgelehnt und kein Export ausgeführt. Die Verlaufsansicht benötigt weiterhin ein Testdokument mit Genehmigungsaktivität; ein eingeschalteter Schalter allein belegt noch keinen vorhandenen Verlauf.
