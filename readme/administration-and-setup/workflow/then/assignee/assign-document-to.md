# Dokument zuordnen

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_based_on_decision_table_v2-de-de.png" alt="Dokument zuordnen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Zweck:

Die Workflow-Karte **„Dokument basierend auf Entscheidungstabelle \[Benutzer/Gruppe] zuweisen“** weist Dokumente dynamisch Benutzern oder Gruppen auf Basis des Ergebnisses einer **Entscheidungstabelle** zu. Diese Funktion stellt sicher, dass die Dokumentzuweisung effizient und konsistent auf Grundlage vordefinierter Bedingungen erfolgt.

## Bestandteile der Karte:

1. **Benutzer/Gruppe**
   * **Beschreibung:** Gibt den **Benutzer** oder die **Gruppe** an, dem bzw. der das Dokument zugewiesen wird.
   * **Detail:** Wird auf Basis des Ergebnisses der **Entscheidungstabelle** ausgewählt.
2. **Entscheidungstabelle**
   * **Beschreibung:** Eine **Entscheidungstabelle** wird verwendet, um den passenden **Benutzer** oder die passende **Gruppe** für die Dokumentzuweisung zu bestimmen.
   * **Detail:** Verwendet die im **„und“**-Abschnitt definierte Entscheidungstabelle.

## Funktionalität:

* **Bedingungsauswertung:** Die Karte führt ihre Aktion nur aus, wenn sowohl der **„Wenn“**- als auch der **„Und“**-Abschnitt als erfüllt ausgewertet werden.
* **Dynamische Dokumentzuweisung:** Das Dokument wird dem **Benutzer** oder der **Gruppe** zugewiesen, der bzw. die durch die **Entscheidungstabelle** bestimmt wird.

## Einrichtung und Konfiguration:

* **Entscheidungstabelle definieren:** Richten Sie die **Entscheidungstabelle** so ein, dass sie die Bedingungen zur Bestimmung des Ziel-**Benutzers** oder der Ziel-**Gruppe** enthält.
* **Dokument Benutzer/Gruppe zuweisen:** Das Dokument wird dynamisch auf Basis des Ergebnisses der Entscheidungstabelle zugewiesen.

## Fazit:

Die Workflow-Karte **„Dokument basierend auf Entscheidungstabelle \[Benutzer/Gruppe] zuweisen“** bietet dynamische Möglichkeiten zur Dokumentzuweisung auf Basis von Entscheidungslogik. Dies sorgt für eine präzise und effiziente Verarbeitung, indem Dokumente automatisch an den passenden **Benutzer** oder die passende **Gruppe** geleitet werden, und steigert so die Workflow-Automatisierung.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Wählen Sie einen Dokumentverantwortlichen aus einer Entscheidungstabelle.

**Konfiguration:** Wählen Sie eine Demo-Entscheidungstabelle aus, deren Übereinstimmungsregel den konfigurierten Prüfer zurückgibt, und wählen Sie den von dieser Kartenversion angebotenen Beauftragtentyp aus.

**Erwartetes Ergebnis und Gegenbeispiel:** Der zurückgegebene Benutzer oder die zurückgegebene Gruppe wird zum Dokumentverantwortlichen. Ein leeres Entscheidungstabellenergebnis muss separat diagnostiziert werden.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
