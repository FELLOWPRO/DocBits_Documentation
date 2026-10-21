# Dokument der Unterorganisation zuordnen

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-a05599461b30-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **„Dokument einer Unterorganisation zuordnen“** weist ein Dokument einer bestimmten Unterorganisation innerhalb des Systems zu und stellt so sicher, dass es zur Verarbeitung an die passende Organisationseinheit weitergeleitet wird.

## **Bestandteile der Karte:**

1. **Unterorganisation**
   * **Beschreibung:** Gibt die Unterorganisation an, der das Dokument zugewiesen wird.
   * **Detail:** Zur Auswahl der Ziel-Unterorganisation wird eine Dropdown-Liste der verfügbaren Unterorganisationen bereitgestellt.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **„Wenn“**- als auch der **„Und“**-Abschnitt als erfüllt ausgewertet werden.
* **Dokumentzuweisung:**\
  Die Karte weist das Dokument der aus der Dropdown-Liste ausgewählten Unterorganisation zu.

## **Einrichtung und Konfiguration:**

* **Unterorganisation auswählen:**\
  Wählen Sie aus der Dropdown-Liste die passende Unterorganisation, der das Dokument zugewiesen werden soll.

## **Fazit:**

Die Workflow-Karte **„Dokument einer Unterorganisation zuordnen“** stellt sicher, dass Dokumente an die richtige Unterorganisation weitergeleitet werden, und optimiert so den Dokumentenmanagementprozess, indem die Verantwortung auf Basis der Organisationsstruktur zugewiesen wird.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Leiten Sie ein Dokument an eine bekannte Geschäftseinheit weiter.

**Konfiguration:** Wählen Sie die konfigurierte Unterorganisation `Demo North`.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Dokument gehört nach der Aktion zur ausgewählten Unterorganisation. Bestätigen Sie das Ziel, bevor Sie den Workflow aktivieren, da die Zugriffsregeln für Unterorganisationen unterschiedlich sein können.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
