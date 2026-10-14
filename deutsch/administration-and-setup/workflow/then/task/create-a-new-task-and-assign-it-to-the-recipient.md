# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Create Task with Fallback"** sorgt für eine effiziente Aufgabendelegation, indem sie Aufgaben bestimmten Rollen – Disponent oder Einkäufer – zuweist und dabei einen Ersatzmechanismus einbindet, um fehlgeschlagene Aufgabenzuweisungen zu verhindern. Diese Karte verbessert die Zuverlässigkeit und Anpassungsfähigkeit des Workflows in dynamischen Szenarien.

## **Bestandteile der Karte:**

1. **Titel**
   * **Beschreibung**: Gibt den Titel der erstellten Aufgabe an.
   * **Detail**: Liefert einen prägnanten Bezeichner für die Aufgabe.
2. **Beschreibung**
   * **Beschreibung**: Beschreibt den Zweck oder Kontext der Aufgabe.
   * **Detail**: Verdeutlicht die Details der Aufgabe.
3. **Priorität**
   * **Beschreibung**: Legt die Dringlichkeitsstufe der Aufgabe fest.
   * **Optionen**:
     * **Hoch**: Erfordert sofortige Aufmerksamkeit.
     * **Mittel**: Wichtig, aber nicht dringend.
     * **Niedrig**: Kann später bearbeitet werden.
4. **Zugewiesene Rolle**
   * **Beschreibung**: Gibt die primäre Rolle an, der die Aufgabe zugewiesen wird.
   * **Optionen**:
     * **Disponent**: Weist die Aufgabe dem Disponenten zu.
     * **Einkäufer**: Weist die Aufgabe dem Einkäufer zu.
5. **E-Mail-Benachrichtigung**
   * **Beschreibung**: Ermöglicht das Benachrichtigen des zugewiesenen Benutzers per E-Mail.
   * **Optionen**:
     * **True**: Sendet eine E-Mail-Benachrichtigung an den Benutzer.
     * **False**: Es wird keine E-Mail-Benachrichtigung gesendet.
6. **Ersatzbenutzer**
   * **Beschreibung**: Bietet eine Ersatzoption für die Aufgabenzuweisung, falls die Empfängerrolle nicht gefunden wird.
   * **Detail**: Ermöglicht die Auswahl eines Benutzers aus einer Dropdown-Liste, um die Aufgabendelegation sicherzustellen.

## **Funktionalität:**

* **Bedingungsauswertung**:\
  Die Karte wird nur ausgeführt, wenn die Bedingungen in den Abschnitten **"Where"** und **"And"** erfüllt sind.
* **Aufgabenzuweisung**:
  * Die Aufgabe wird der ausgewählten Rolle (Disponent oder Einkäufer) zugewiesen.
  * Wird die angegebene Rolle nicht gefunden, wird die Aufgabe einem Benutzer aus der Ersatz-Dropdown-Liste zugewiesen.
* **E-Mail-Benachrichtigung**:\
  Sendet eine E-Mail an den zugewiesenen Benutzer, wenn die E-Mail-Benachrichtigung aktiviert ist.

## **Einrichtung und Konfiguration:**

1. **Aufgabendetails angeben**: Geben Sie Titel, Beschreibung und Priorität der Aufgabe ein.
2. **Primäre Rolle auswählen**: Wählen Sie die Rolle, der die Aufgabe zugewiesen wird (Disponent oder Einkäufer).
3. **Ersatzbenutzer konfigurieren**: Wählen Sie einen Ersatzbenutzer aus der Dropdown-Liste, um die Aufgabenzuweisung sicherzustellen, falls die primäre Rolle nicht gefunden wird.
4. **E-Mail-Benachrichtigung aktivieren**: Geben Sie an, ob der zugewiesene Benutzer eine E-Mail-Benachrichtigung erhalten soll.

## **Fazit:**

Die Workflow-Karte **"Create Task with Fallback"** sorgt durch die Integration eines Ersatzmechanismus für eine nahtlose Aufgabendelegation. Indem sie Aufgaben auf Basis von Rollen zuweist und eine alternative Benutzeroption bietet, erhöht sie die Zuverlässigkeit und Flexibilität in den Prozessen des Aufgabenmanagements.
