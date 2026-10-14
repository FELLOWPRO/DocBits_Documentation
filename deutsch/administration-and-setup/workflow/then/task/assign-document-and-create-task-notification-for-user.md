# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Die Workflow-Karte "**Assign Document and Create Task/Notification for User**" weist ein Dokument einem angegebenen Benutzer zu, erstellt eine Aufgabe oder Benachrichtigung mit konfigurierbaren Details und sendet optional eine E-Mail-Benachrichtigung an den Benutzer. Diese Karte ermöglicht außerdem das Festlegen eines numerischen Prioritätswerts, um die Reihenfolge der Ausführung zu bestimmen.

## **Bestandteile der Karte**

1. **Benutzer**
   * **Beschreibung:** Gibt den Benutzer an, der die Aufgabe oder Benachrichtigung erhält.
   * **Detail:** Ein Dropdown-Menü zur Auswahl des Benutzers, dem das Dokument und die Aufgabe/Benachrichtigung zugewiesen werden.
2. **Task/Notification**
   * **Beschreibung:** Gibt die Art der für den Benutzer zu erstellenden Aktion an.
   * **Detail:** Ein Dropdown zur Auswahl von entweder "Task" oder "Notification" je nach beabsichtigter Aktion.
3. **Titel**
   * **Beschreibung:** Der Titel der Aufgabe oder Benachrichtigung.
   * **Detail:** Ein Feld, um einen prägnanten, beschreibenden Titel für die Aufgabe oder Benachrichtigung anzugeben.
4. **Beschreibung**
   * **Beschreibung:** Zusätzliche Details zur Aufgabe oder Benachrichtigung.
   * **Detail:** Ein Feld, um den Zweck der Aufgabe zu beschreiben oder Kontext für die Benachrichtigung zu liefern.
5. **Priorität**
   * **Beschreibung:** Legt die Dringlichkeitsstufe der Aufgabe oder Benachrichtigung fest.
   * **Optionen:**
     * **Hoch:** Erfordert sofortige Aufmerksamkeit.
     * **Mittel:** Wichtig, aber nicht dringend.
     * **Niedrig:** Kann später bearbeitet werden.
6. **Mail senden**
   * **Beschreibung:** Konfiguriert, ob eine E-Mail-Benachrichtigung an den Benutzer gesendet wird.
   * **Optionen:**
     * **True:** Sendet eine E-Mail-Benachrichtigung an den Benutzer.
     * **False:** Es wird keine E-Mail-Benachrichtigung gesendet.
7. **Wert**
   * **Beschreibung:** Legt die numerische Priorität für die Dokumentzuweisung fest.
   * **Detail:** Ein Feld zur Eingabe eines numerischen Werts, wobei niedrigere Zahlen eine höhere Priorität anzeigen.

## **Funktionalität**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktionen nur aus, wenn die konfigurierten Workflow-Bedingungen erfüllt sind.
* **Dokumentzuweisung und Erstellung von Aufgabe/Benachrichtigung:**\
  Das Dokument wird dem im Feld "Benutzer" angegebenen Benutzer zugewiesen. Es wird eine Aufgabe oder Benachrichtigung mit dem angegebenen Titel, der Beschreibung und der Prioritätsstufe erstellt.
* **E-Mail-Benachrichtigung:**\
  Ist "Mail senden" auf True gesetzt, wird eine E-Mail an den Benutzer gesendet, um ihn über die Aufgabe oder Benachrichtigung zu informieren.

## **Einrichtung und Konfiguration**

1. **Benutzer auswählen:**
   * Wählen Sie den Benutzer aus dem Dropdown-Menü Benutzer.
2. **Details der Aufgabe/Benachrichtigung konfigurieren:**
   * Wählen Sie "Task" oder "Notification" aus dem Dropdown Task/Notification.
   * Geben Sie den Titel und die Beschreibung für die Aufgabe oder Benachrichtigung ein.
   * Legen Sie die Priorität fest, indem Sie Hoch, Mittel oder Niedrig aus dem Dropdown auswählen.
3. **E-Mail-Benachrichtigung aktivieren:**
   * Konfigurieren Sie die Option Mail senden auf True oder False, je nachdem, ob eine E-Mail-Benachrichtigung gesendet werden soll.
4. **Numerische Priorität festlegen:**
   * Geben Sie im Feld Wert einen numerischen Wert ein, um die Priorität der Zuweisung zu bestimmen, wobei niedrigere Werte zuerst verarbeitet werden.
5. Speichern Sie die Kartenkonfiguration und aktivieren Sie den Workflow.

## **Fazit**

Die Workflow-Karte "Assign Document and Create Task/Notification for User" stellt sicher, dass Dokumente dem passenden Benutzer zugewiesen werden, und erstellt gleichzeitig Aufgaben oder Benachrichtigungen mit definierten Prioritäten und optionalen E-Mail-Benachrichtigungen. Diese Karte hilft, die Aufgabendelegation zu optimieren, und steigert die Workflow-Effizienz.
