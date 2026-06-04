# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Create Field-Based Task or Notification"** wird verwendet, um Aufgaben oder Benachrichtigungen zu erstellen, die dynamisch Benutzern zugewiesen werden, die innerhalb bestimmter Dokumentfelder identifiziert werden. Diese Karte bietet einen optionalen Ersatzmechanismus, um einen reibungslosen Workflow-Ablauf auch dann sicherzustellen, wenn das Dokumentfeld keinen gültigen Benutzer angibt.

## **Bestandteile der Karte:**&#x20;

1. **Titel**
   * **Beschreibung**: Gibt den Titel der Aufgabe oder Benachrichtigung an.
   * **Detail**: Wird verwendet, um die erstellte Aufgabe oder Benachrichtigung zu benennen und zu kennzeichnen.
2. **Beschreibung**
   * **Beschreibung**: Liefert zusätzliche Details zur Aufgabe oder Benachrichtigung.
   * **Detail**: Stellt sicher, dass der Empfänger den Zweck und Kontext der Aufgabe oder Benachrichtigung versteht.
3. **Priorität**
   * **Beschreibung**: Legt die Dringlichkeit der Aufgabe oder Benachrichtigung fest.
   * **Optionen**:
     * **Hoch**: Erfordert sofortige Aufmerksamkeit.
     * **Mittel**: Wichtig, aber weniger dringend.
     * **Niedrig**: Kann zu einem späteren Zeitpunkt bearbeitet werden.
4. **Feldname**
   * **Beschreibung**: Gibt das Dokumentfeld an, das zur Zuweisung der Aufgabe oder Benachrichtigung verwendet wird.
   * **Detail**: Das ausgewählte Feld bestimmt dynamisch den Benutzer, dem die Aufgabe oder Benachrichtigung zugewiesen wird. Ist das Feld leer oder ungültig, wird die Aufgabe oder Benachrichtigung dem aus der Dropdown-Liste ausgewählten Ersatzbenutzer zugewiesen.
5. **E-Mail-Benachrichtigung**
   * **Beschreibung**: Konfiguriert, ob der zugewiesene Benutzer per E-Mail benachrichtigt wird.
   * **Optionen**:
     * **True**: Sendet eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer.
     * **False**: Es wird keine E-Mail-Benachrichtigung gesendet.
6. **Ersatzbenutzer**
   * **Beschreibung**: Ermöglicht die Auswahl eines Benutzers aus einer Dropdown-Liste, um die Aufgabe oder Benachrichtigung zuzuweisen, wenn im Dokumentfeld kein gültiger Benutzer gefunden wird.
   * **Detail**: Stellt sicher, dass die Aufgabe oder Benachrichtigung auch dann zugewiesen wird, wenn das Dokumentfeld leer oder ungültig ist.

## **Zusätzliche Komponenten in Version 3:**

1. **Benachrichtigungstyp**&#x20;
   * **Beschreibung**: Gibt an, ob die Karte eine Aufgabe oder eine Benachrichtigung erstellt.
   * **Optionen**:
     * **Task**: Erstellt eine Aufgabe, die dem angegebenen Benutzer zugewiesen wird.
     * **Notification**: Sendet eine Benachrichtigung, anstatt eine Aufgabe zu erstellen.

## **Funktionalität:**

* **Bedingungsauswertung**:\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Erstellung von Aufgabe oder Benachrichtigung**:
  * Weist die Aufgabe oder Benachrichtigung dem im Dokumentfeld identifizierten Benutzer zu.
  * In Version 3 ist die Erstellung entweder einer Aufgabe oder einer Benachrichtigung möglich.
* **Ersatzmechanismus**:\
  Identifiziert das Dokumentfeld keinen gültigen Benutzer, weist die Karte die Aufgabe oder Benachrichtigung dem aus der Dropdown-Liste ausgewählten Ersatzbenutzer zu.
* **E-Mail-Benachrichtigung**:\
  Sendet eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer, sofern entsprechend konfiguriert.

## **Einrichtung und Konfiguration:**

1. **Details der Aufgabe oder Benachrichtigung definieren**: Geben Sie Titel, Beschreibung und Priorität ein.
2. **Dokumentfeld auswählen**: Wählen Sie das Feld, das den Benutzer für die Zuweisung der Aufgabe oder Benachrichtigung angibt.
3. **E-Mail-Benachrichtigung aktivieren**: Legen Sie fest, ob eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer gesendet werden soll.
4. **Ersatzbenutzer auswählen**: Wählen Sie einen Ersatzbenutzer aus der Dropdown-Liste für die Zuweisung, falls das Dokumentfeld keinen gültigen Benutzer identifiziert.
5. **Benachrichtigungstyp angeben (Version 3)**: Geben Sie an, ob die Karte eine Aufgabe oder Benachrichtigung erstellt.

## **Fazit:**

Die Workflow-Karte **"Create Field-Based Task or Notification"** optimiert das Management von Aufgaben und Benachrichtigungen, indem sie Verantwortlichkeiten dynamisch auf Basis von Dokumentfeldern zuweist. Ihr Ersatzbenutzer-Mechanismus und die erweiterten Optionen in Version 3 bieten Flexibilität und stellen sicher, dass Aufgaben oder Benachrichtigungen stets zugewiesen werden, auch wenn die Dokumentdaten unvollständig sind.
