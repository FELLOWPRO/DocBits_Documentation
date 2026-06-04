# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Create Group Task or Notification"** ermöglicht die Erstellung von Aufgaben oder Benachrichtigungen für bestimmte Gruppen und gewährleistet so eine effiziente Kommunikation und ein effizientes Aufgabenmanagement. In späteren Versionen um eine Entscheidungsbaum-Funktionalität erweitert, bestimmt sie die zugewiesene Gruppe oder Methode dynamisch und optimiert so die Abläufe.

## **Bestandteile der Karte:**

1. **Titel**
   * **Beschreibung**: Gibt den Titel der Aufgabe oder Benachrichtigung an.
   * **Detail**: Dient als Bezeichner für die erstellte Aufgabe oder Benachrichtigung.
2. **Beschreibung**
   * **Beschreibung**: Beschreibt den Kontext oder die Details der Aufgabe oder Benachrichtigung.
   * **Detail**: Schafft Klarheit über ihren Zweck.
3. **Priorität**
   * **Beschreibung**: Legt die Wichtigkeitsstufe der Aufgabe fest.
   * **Optionen**:
     * **Hoch**: Erfordert sofortiges Handeln.
     * **Mittel**: Wichtig, aber weniger dringend.
     * **Niedrig**: Kann später bearbeitet werden.
4. **Zugewiesene Gruppe**
   * **Beschreibung**: Gibt die Gruppe an, die für die Aufgabe oder Benachrichtigung verantwortlich ist.
   * **Detail**: Wird aus einer Dropdown-Liste der verfügbaren Gruppen ausgewählt.
5. **E-Mail-Benachrichtigung**
   * **Beschreibung**: Ermöglicht das Senden einer E-Mail, um die zugewiesene Gruppe zu benachrichtigen.
   * **Optionen**:
     * **True**: Sendet eine E-Mail-Benachrichtigung.
     * **False**: Es wird keine E-Mail-Benachrichtigung gesendet.

## **Zusätzliche Komponenten in Version 3 und Version 4**

1. **Entscheidungsbaum (nur Version 3)**
   * **Beschreibung**: Ermöglicht die Verwendung eines Entscheidungsbaums für die dynamische Aufgabenerstellung.
   * **Optionen**:
     * **True**: Aktiviert die Verarbeitung über den Entscheidungsbaum.
     * **False**: Deaktiviert die Verarbeitung über den Entscheidungsbaum.
2. **Task/Notification-Option** **(nur Version 4)**
   * **Beschreibung**: Ermöglicht die Erstellung entweder einer Aufgabe oder einer Benachrichtigung.
   * **Optionen**:
     * **Task**: Erstellt eine Aufgabe für die ausgewählte Gruppe.
     * **Notification**: Sendet eine Benachrichtigung, anstatt eine Aufgabe zu erstellen.

## **Funktionalität:**

* **Bedingungsauswertung**:\
  Führt die Kartenaktion nur aus, wenn die Abschnitte **"Where"** und **"And"** erfüllt sind.
* **Erstellung von Aufgabe oder Benachrichtigung**:
  * Es wird eine Aufgabe für die ausgewählte Gruppe mit dem angegebenen Titel, der Beschreibung und der Priorität erstellt.
  * In Version 4 kann die Karte anstelle einer Aufgabe eine Benachrichtigung erstellen.
* **Dynamische Zuweisung (nur Version 3)**:\
  Sofern aktiviert, bestimmt der Entscheidungsbaum die Zielgruppe dynamisch.
* **E-Mail-Benachrichtigung**:\
  Sendet eine E-Mail-Benachrichtigung an die Gruppe, wenn die E-Mail-Option auf true gesetzt ist.

## **Einrichtung und Konfiguration:**

1. **Details der Aufgabe oder Benachrichtigung definieren**: Geben Sie Titel, Beschreibung und Priorität ein.
2. **Einer Gruppe zuweisen**: Wählen Sie eine Gruppe aus der Dropdown-Liste für die Zuweisung der Aufgabe oder Benachrichtigung.
3. **E-Mail-Benachrichtigung aktivieren**: Geben Sie an, ob die Gruppe per E-Mail benachrichtigt werden soll.
4. **Entscheidungsbaum verwenden (nur Version 3)**: Aktivieren Sie den Entscheidungsbaum, um die Gruppe dynamisch zuzuweisen.
5. **Ausgabetyp auswählen (nur Version 4)**: Wählen Sie, ob die Karte eine Aufgabe oder eine Benachrichtigung erstellt.

## **Fazit:**

Die Workflow-Karte **"Create Group Task or Notification"** vereinfacht das Management von Aufgaben und Benachrichtigungen, indem sie Gruppen direkt anspricht. Ihre dynamische Zuweisungsfunktion, die durch den Entscheidungsbaum ermöglicht wird, erhöht die Flexibilität, während E-Mail-Benachrichtigungen eine zeitnahe Kommunikation gewährleisten. Die Versionen 3 und 4 fügen erweiterte Funktionalität hinzu und machen sie zu einem vielseitigen Werkzeug für eine effiziente Workflow-Ausführung.
