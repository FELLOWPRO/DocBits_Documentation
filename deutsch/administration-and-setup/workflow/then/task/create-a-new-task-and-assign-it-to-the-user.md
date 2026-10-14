# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Die Workflow-Karte **"Create Task or Notification"** optimiert das Management von Aufgaben und Benachrichtigungen innerhalb von Workflows. Je nach Version kann die Karte Aufgaben erstellen, Benachrichtigungen senden und zusätzliche Funktionen wie Entscheidungsbäume für die dynamische Verarbeitung nutzen.

## **Bestandteile der Karte**

1. **Titel**
   * **Beschreibung**: Legt den Titel der erstellten Aufgabe oder Benachrichtigung fest.
   * **Detail**: Der Titel liefert einen klaren und prägnanten Bezeichner für die Aufgabe oder Benachrichtigung.
2. **Beschreibung**
   * **Beschreibung**: Liefert Details zur Aufgabe oder Benachrichtigung.
   * **Detail**: Hilft, den Zweck oder Kontext der Aufgabe oder Benachrichtigung für den zugewiesenen Benutzer zu verdeutlichen.
3. **Priorität**
   * **Beschreibung**: Legt die Dringlichkeitsstufe der Aufgabe fest.
   * **Optionen**:
     * **Hoch**: Erfordert sofortige Aufmerksamkeit.
     * **Mittel**: Wichtig, aber nicht dringend.
     * **Niedrig**: Kann später bearbeitet werden.
4. **Zugewiesener Benutzer**
   1. **Beschreibung**: Gibt den Benutzer an, dem die Aufgabe zugewiesen wird.
   2. **Detail**: Benutzer werden aus einer Dropdown-Liste des verfügbaren Personals ausgewählt.
5. **E-Mail-Benachrichtigung**
   * **Beschreibung**: Legt fest, ob der zugewiesene Benutzer eine E-Mail-Benachrichtigung erhält.
   * **Optionen**:
     * **True**: Sendet eine E-Mail-Benachrichtigung an den Benutzer.
     * **False**: Es wird keine E-Mail-Benachrichtigung gesendet.

## Zusätzliche Komponenten **in Version 3 und Version 4**

1. **Entscheidungsbaum (nur Version 3)**
   * **Beschreibung**: Ermöglicht die Verwendung eines Entscheidungsbaums für die dynamische Aufgabenerstellung.
   * **Optionen**:
     * **True**: Aktiviert die Verarbeitung über den Entscheidungsbaum.
     * **False**: Deaktiviert die Verarbeitung über den Entscheidungsbaum.
2. **Task oder Notification (nur Version 4)**
   * **Beschreibung**: Ermöglicht die Auswahl zwischen der Erstellung einer Aufgabe oder einer Benachrichtigung.
   * **Optionen**:
     * **Task**: Erstellt eine Aufgabe.
     * **Notification**: Erstellt eine Benachrichtigung anstelle einer Aufgabe.

## **Funktionalität:**

* **Bedingungsauswertung**:\
  Diese Karte wird nur ausgelöst, wenn die Bedingungen in den Abschnitten **"Where"** und **"And"** erfüllt sind.
* **Erstellung von Aufgabe oder Benachrichtigung**:
  * Versionen 2 und 3: Es wird eine Aufgabe mit dem angegebenen Titel, der Beschreibung, der Priorität und dem zugewiesenen Benutzer erstellt.
  * Version 4: Ermöglicht die Erstellung entweder einer Aufgabe oder einer Benachrichtigung.
* **Dynamische Zuweisung**:
  * In Version 3 bestimmt der Entscheidungsbaum dynamisch den Benutzer, dem die Aufgabe auf Basis der Workflow-Parameter zugewiesen wird.
* **E-Mail-Benachrichtigung**:\
  Sendet eine E-Mail an den zugewiesenen Benutzer, wenn die Benachrichtigungsoption aktiviert ist.

## **Einrichtung und Konfiguration:**

1. **Version auswählen**: Wählen Sie die Version der Karte je nach erforderlicher Funktionalität:
   * Version 2: Grundlegende Aufgabenerstellung mit manueller Benutzerzuweisung und E-Mail-Benachrichtigungen.
   * Version 3: Umfasst die Entscheidungsbaum-Funktionalität für die dynamische Benutzerzuweisung.
   * Version 4: Fügt die Möglichkeit hinzu, anstelle einer Aufgabe eine Benachrichtigung zu erstellen.
2. **Aufgabendetails eingeben**: Geben Sie den Titel, die Beschreibung und die Priorität der Aufgabe oder Benachrichtigung an.
3. **Benutzer zuweisen**:
   * Wählen Sie bei den Versionen 2 und 4 manuell einen Benutzer aus der Dropdown-Liste.
   * Aktivieren Sie bei Version 3 den Entscheidungsbaum, um den zugewiesenen Benutzer dynamisch zu bestimmen.
4. **E-Mail-Benachrichtigung aktivieren**: Legen Sie fest, ob der zugewiesene Benutzer eine E-Mail-Benachrichtigung erhalten soll.
5. (Für Version 4) **Task oder Notification wählen**: Geben Sie an, ob eine Aufgabe oder Benachrichtigung erstellt werden soll.

## **Fazit:**

Die Workflow-Karte **"Create Task or Notification"** ist ein vielseitiges Werkzeug zur Verwaltung von Aufgaben und Benachrichtigungen. Indem sie die dynamische Benutzerzuweisung über Entscheidungsbäume unterstützt und Optionen für die Erstellung von Aufgaben oder Benachrichtigungen bietet, verbessert sie die Anpassungsfähigkeit des Workflows und die Effizienz der Zusammenarbeit.
