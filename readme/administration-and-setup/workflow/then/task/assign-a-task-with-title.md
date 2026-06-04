# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte "Assign Task / Notification from Decision Table" ist darauf ausgelegt, Aufgaben oder Benachrichtigungen dynamisch auf Basis der Ergebnisse einer Entscheidungstabelle zuzuweisen. Diese Karte stellt sicher, dass Aufgaben oder Benachrichtigungen gemäß der in der Entscheidungstabelle definierten Logik dem richtigen Benutzer oder der richtigen Gruppe zugewiesen werden, mit einer optionalen E-Mail-Benachrichtigung an den Empfänger.

## **Bestandteile der Karte:**

1. **Titel**
   * **Beschreibung**: Gibt den Titel der erstellten Aufgabe oder Benachrichtigung an.
   * **Detail**: Der Titel sollte Kontext bieten und den Zweck der Aufgabe oder Benachrichtigung beschreiben.
2. **Beschreibung**
   * **Beschreibung**: Legt den Inhalt oder Zweck der Aufgabe oder Benachrichtigung fest.
   * **Detail**: Bietet zusätzliche Informationen über die Aufgabe oder Benachrichtigung und erläutert den Kontext oder die erforderliche Aktion.
3. **Priorität**
   * **Beschreibung**: Legt die Dringlichkeitsstufe der Aufgabe oder Benachrichtigung fest.
   * **Optionen**:
     * **Hoch**: Aufgaben oder Benachrichtigungen, die sofortige Aufmerksamkeit erfordern.
     * **Mittel**: Wichtige Aufgaben, die zeitnah bearbeitet werden sollten.
     * **Niedrig**: Aufgaben, die zu einem späteren Zeitpunkt bearbeitet werden können.
4. **Zuweisungstyp**
   * **Beschreibung**: Gibt den Benutzer oder die Gruppe an, der bzw. die der Aufgabe oder Benachrichtigung auf Basis der Ausgabe der Entscheidungstabelle zugewiesen wird.
   * **Detail**: Die Entscheidungstabelle wertet Bedingungen dynamisch aus und gibt den passenden Benutzer oder die passende Gruppe für die Zuweisung zurück.
5. **E-Mail-Benachrichtigung**
   * **Beschreibung**: Konfiguriert, ob eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer oder die zugewiesene Gruppe gesendet wird.
   * **Optionen**:
     * **True**: Sendet eine E-Mail-Benachrichtigung an den Empfänger.
     * **False**: Es wird keine E-Mail-Benachrichtigung gesendet.

#### **Zusätzliche Komponenten in Version 3**

1. **Benachrichtigungstyp**
   * **Beschreibung**: Gibt an, ob die Karte eine Aufgabe oder eine Benachrichtigung erstellt.
   * **Optionen**:
     * **Task**: Erstellt eine Aufgabe, die dem Benutzer oder der Gruppe aus der Entscheidungstabelle zugewiesen wird.
     * **Notification**: Sendet eine Benachrichtigung an den Benutzer oder die Gruppe aus der Entscheidungstabelle.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Zuweisung der Aufgabe / Benachrichtigung**\
  Die Karte weist die Aufgabe oder Benachrichtigung dem Benutzer oder der Gruppe zu, der bzw. die durch die Entscheidungstabelle identifiziert wird. Die Entscheidungstabelle wertet vordefinierte Bedingungen dynamisch aus und gibt den entsprechenden Empfänger zurück.
* **E-Mail-Benachrichtigung**\
  Sofern entsprechend konfiguriert, wird eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer oder die zugewiesene Gruppe gesendet.
* **Funktionalität in Version 3**\
  In Version 3 ermöglicht die Karte die Erstellung entweder einer Task oder einer Notification und bietet so mehr Flexibilität für Aufgabenmanagement und Kommunikation.

## **Einrichtung und Konfiguration:**

1. **Details der Aufgabe oder Benachrichtigung definieren**:\
   Geben Sie Titel, Beschreibung und Priorität für die Aufgabe oder Benachrichtigung ein.
2. **Entscheidungstabelle konfigurieren**:\
   Richten Sie die Entscheidungstabelle so ein, dass sie dynamisch bestimmt, welchem Benutzer oder welcher Gruppe die Aufgabe oder Benachrichtigung zugewiesen werden soll.
3. **E-Mail-Benachrichtigung aktivieren**:\
   Legen Sie fest, ob eine E-Mail-Benachrichtigung an den zugewiesenen Benutzer oder die zugewiesene Gruppe gesendet werden soll.
4. **Benachrichtigungstyp angeben (Version 3)**:\
   Wählen Sie, ob die Karte eine Aufgabe erstellt oder eine Benachrichtigung sendet.

## **Fazit:**

Die Workflow-Karte **"Assign Task / Notification from Decision Table"** automatisiert die Zuweisung von Aufgaben oder Benachrichtigungen auf Basis dynamischer, in einer Entscheidungstabelle definierter Bedingungen. Version 3 erweitert ihre Funktionalität, indem sie es Benutzern ermöglicht, zwischen der Erstellung einer Aufgabe oder einer Benachrichtigung zu wählen, und stellt sicher, dass stets der richtige Empfänger zugewiesen wird. Die Funktion der E-Mail-Benachrichtigung hält Benutzer auf dem Laufenden und optimiert so Kommunikation und Aufgabenmanagement.
