# Benutzer dem Lieferanten zuweisen

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_user_to_supplier_v2-de-de.png" alt="Benutzer dem Lieferanten zuweisen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Zweck:

Diese Workflow-Karte legt den zugewiesenen Benutzer eines registrierten Lieferanten fest. Der zugewiesene Benutzer ist der interne Ansprechpartner, der für den Lieferanten zuständig ist. Die Karte arbeitet nicht mit einem Dokument: Sie ist für Workflows gedacht, die durch eine Statusänderung eines Lieferanten gestartet werden, zum Beispiel mit der When-Karte **Supplier status changed**. Der Lieferant, dessen Status sich geändert hat, ist der Lieferant, dem der Benutzer zugewiesen wird.

## Bestandteile der Karte:

1. **Benutzer**
   * **Beschreibung:** Der Benutzer, der zum zugewiesenen Benutzer des Lieferanten wird.
   * **Detail:** Es kann ein Benutzer der Organisation ausgewählt werden. Hat der Lieferant bereits einen zugewiesenen Benutzer, wird dieser ersetzt.

## Funktionalität:

* **Ausführung der Aktion:** Die Karte übernimmt den Lieferanten aus dem Workflow-Lauf und speichert den ausgewählten Benutzer als zugewiesenen Benutzer des Lieferanten. Das Ergebnis wird im Workflow-Protokoll festgehalten.
* **Verwendung mit E-Mails:** Sobald ein Benutzer zugewiesen ist, können E-Mails mit der Option **Dem Lieferanten zugewiesener Benutzer** an diesen Benutzer adressiert werden, zum Beispiel in der Karte **Send Email**.
* **Fehlende Daten:** Ist auf der Karte kein Benutzer ausgewählt, wird die Karte nicht ausgeführt und meldet die fehlenden Daten im Workflow-Protokoll.
* **Fehler:** Lehnt der Lieferantendienst die Anfrage ab oder antwortet er nicht rechtzeitig, endet die Karte mit einem Fehler.

## Einrichtung und Konfiguration:

* Die Karte kann in einem Workflow verwendet werden, der durch eine Statusänderung eines Lieferanten gestartet wird.
* Die Karte kann aus der Kategorie **Zugewiesener Benutzer** hinzugefügt werden. Danach wird im Feld **Benutzer** der Benutzer ausgewählt, der für den Lieferanten zuständig sein soll.

## Fazit:

Die Workflow-Karte „Assign User to Supplier“ gibt jedem Lieferanten automatisch einen zuständigen Ansprechpartner, wenn sich sein Status ändert, zum Beispiel nach der Registrierung. Spätere Schritte, etwa E-Mails an den zugewiesenen Benutzer, können auf dieser Zuweisung aufbauen.
