# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Die Workflow-Karte "**Assign Document and Create Task/Notification Based on Decision Table**" weist ein Dokument zu und erstellt eine Aufgabe oder Benachrichtigung mit konfigurierbaren Details. Der Zuweisungsempfänger wird durch die Rückgabe einer Entscheidungstabelle bestimmt, und die Karte ermöglicht das Festlegen von Prioritäten und das Senden von E-Mail-Benachrichtigungen.

## **Bestandteile der Karte**

1. **Zuweisungstyp**
   * **Beschreibung:** Gibt an, ob die Rückgabe der Entscheidungstabelle das Dokument und die Aufgabe/Benachrichtigung einem Benutzer oder einer Gruppe zuweist.
   * **Detail:** Ein Feld zur Konfiguration des Zuweisungstyps als entweder "User" oder "Group" auf Basis der Ausgabe der Entscheidungstabelle.
2. **Task/Notification**
   * **Beschreibung:** Gibt die Art der für den Zuweisungsempfänger zu erstellenden Aktion an.
   * **Detail:** Ein Dropdown zur Auswahl von entweder "Task" oder "Notification" je nach Anforderung des Workflows.
3. **Titel**
   * **Beschreibung:** Der Titel der Aufgabe oder Benachrichtigung.
   * **Detail:** Ein Feld, um einen prägnanten Titel anzugeben, der die Aufgabe oder Benachrichtigung kennzeichnet.
4. **Beschreibung**
   * **Beschreibung:** Zusätzliche Details zur Aufgabe oder Benachrichtigung.
   * **Detail:** Ein Feld, um den Zweck und Kontext der Aufgabe oder Benachrichtigung zu beschreiben.
5. **Priorität**
   * **Beschreibung:** Legt die Dringlichkeitsstufe der Aufgabe oder Benachrichtigung fest.
   * **Optionen:**
     * **Hoch:** Erfordert sofortige Aufmerksamkeit.
     * **Mittel:** Wichtig, aber nicht dringend.
     * **Niedrig:** Kann später bearbeitet werden.
6. **Zuweisungstyp**
   * **Beschreibung:** Dieses Feld bestimmt die Art des Zuweisungsempfängers (User oder Group), dem das Dokument und die Aufgabe/Benachrichtigung zugewiesen werden.
   * **Detail:** Ein Dropdown-Menü zur Auswahl, ob die Aufgabe/Benachrichtigung auf Basis der Ausgabe der Entscheidungstabelle einem Benutzer oder einer Gruppe zugewiesen wird.
7. **Mail senden**
   * **Beschreibung:** Konfiguriert, ob eine E-Mail-Benachrichtigung an den Zuweisungsempfänger gesendet wird.
   * **Optionen:**
     * **True:** Sendet eine E-Mail-Benachrichtigung.
     * **False:** Es wird keine E-Mail-Benachrichtigung gesendet.
8. **Wert**
   * **Beschreibung:** Legt die numerische Priorität für die Dokumentzuweisung fest.
   * **Detail:** Ein Feld zur Eingabe eines numerischen Werts, wobei niedrigere Zahlen eine höhere Priorität anzeigen.

## **Funktionalität**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktionen nur aus, wenn die Workflow-Bedingungen erfüllt sind.
* **Auswertung der Entscheidungstabelle:**\
  Die Entscheidungstabelle bestimmt, ob das Dokument und die Aufgabe/Benachrichtigung einem Benutzer oder einer Gruppe zugewiesen werden.
* **Dokumentzuweisung und Erstellung von Aufgabe/Benachrichtigung:**\
  Das Dokument wird dem Ergebnis der Entscheidungstabelle zugewiesen. Es wird eine Aufgabe oder Benachrichtigung mit dem angegebenen Titel, der Beschreibung und der Prioritätsstufe erstellt.
* **E-Mail-Benachrichtigung:**\
  Ist "Mail senden" auf True gesetzt, wird eine E-Mail-Benachrichtigung an den Zuweisungsempfänger gesendet.

## **Einrichtung und Konfiguration**

1. **Zuweisungstyp definieren:**
   * Konfigurieren Sie das Feld Zuweisungstyp auf Basis der Ausgabe der Entscheidungstabelle auf entweder "User" oder "Group".
2. **Task/Notification auswählen:**
   * Wählen Sie "Task" oder "Notification" aus dem Dropdown Task/Notification.
3. **Details der Aufgabe/Benachrichtigung festlegen:**
   * Geben Sie den Titel und die Beschreibung für die Aufgabe oder Benachrichtigung ein.
   * Wählen Sie die Priorität (Hoch, Mittel oder Niedrig) aus dem Dropdown.
4. **E-Mail-Benachrichtigung aktivieren:**
   * Setzen Sie die Option Mail senden auf True oder False, je nachdem, ob eine E-Mail-Benachrichtigung gesendet werden soll.
5. **Numerische Priorität festlegen:**
   * Geben Sie im Feld Wert einen numerischen Wert ein, um die Priorität der Zuweisung zu bestimmen, wobei niedrigere Zahlen zuerst verarbeitet werden.
6. Speichern Sie die Kartenkonfiguration und aktivieren Sie den Workflow.

## **Fazit**

Die Workflow-Karte "Assign Document and Create Task/Notification Based on Decision Table" stellt sicher, dass Aufgaben oder Benachrichtigungen auf Basis der Ergebnisse der Entscheidungstabelle dynamisch dem passenden Benutzer oder der passenden Gruppe zugewiesen werden. Diese Karte ermöglicht eine effiziente Aufgabendelegation, anpassbare Prioritäten und optionale E-Mail-Benachrichtigungen, um die Reaktionsfähigkeit des Workflows zu verbessern.
