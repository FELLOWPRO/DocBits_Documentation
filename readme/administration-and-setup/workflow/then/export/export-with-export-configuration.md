# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Export Document with Export Configuration"** ist darauf ausgelegt, ein Dokument mithilfe einer angegebenen Exportkonfiguration zu exportieren. Sie bietet die Flexibilität, alle mit dem Dokument verbundenen offenen Aufgaben zu ignorieren, und gewährleistet so einen reibungslosen Exportprozess unabhängig vom aktuellen Zustand des Dokuments.

## **Bestandteile der Karte:**

1. **Exportkonfiguration**
   * **Beschreibung**: Gibt die Exportkonfiguration an, die zur Verarbeitung des Dokuments verwendet wird.
   * **Detail**: Diese Konfiguration bestimmt das Format, die Struktur und das Ziel des exportierten Dokuments.
2. **Offene Aufgaben ignorieren**
   * **Beschreibung**: Legt fest, ob mit dem Dokument verknüpfte offene Aufgaben während des Exportprozesses ignoriert werden sollen.
   * **Optionen**:
     * **True**: Exportiert das Dokument unabhängig von offenen Aufgaben.
     * **False**: Stellt sicher, dass offene Aufgaben vor dem Export abgeschlossen werden.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** des Workflows festgelegten Bedingungen aus. Sind beide Bedingungen erfüllt, wird der Exportprozess gestartet.
* **Dokumentexport**: Mithilfe der angegebenen **Exportkonfiguration** wird das Dokument im definierten Format und Ziel verarbeitet und exportiert.
* **Umgang mit offenen Aufgaben**: Ist **Offene Aufgaben ignorieren** auf **True** gesetzt, umgeht der Exportprozess alle ausstehenden, mit dem Dokument verknüpften Aufgaben. Ist die Einstellung auf **False** gesetzt, wird der Export aufgeschoben, bis alle Aufgaben erledigt sind.

## **Einrichtung und Konfiguration:**

Um diese Karte zu konfigurieren, müssen Benutzer:

1. Die gewünschte **Exportkonfiguration** auswählen, um festzulegen, wie das Dokument exportiert wird.
2. Wählen, ob **Offene Aufgaben ignorieren** werden sollen, indem der Wert auf **True** oder **False** gesetzt wird.
3. Sicherstellen, dass die Bedingungen in den Abschnitten **"Where"** und **"And"** korrekt festgelegt sind, da die Karte ihre Aktion nur ausführt, wenn diese Bedingungen erfüllt sind.

## **Fazit:**

Die Workflow-Karte **"Export Document with Export Configuration"** stellt sicher, dass Dokumente effizient und gemäß vordefinierter Konfigurationen exportiert werden. Mit der Möglichkeit, offene Aufgaben zu ignorieren, bietet diese Karte Flexibilität bei der Bearbeitung von Dokumenten in verschiedenen Phasen, reduziert Verzögerungen und optimiert den Exportprozess.
