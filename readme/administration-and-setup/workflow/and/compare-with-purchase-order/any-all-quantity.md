# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, die Menge in einem Dokument mit der in der Bestellung definierten Toleranz zu vergleichen. Sie ermöglicht es Benutzern auszuwerten, ob die Menge bestimmte Bedingungen erfüllt, etwa Gleichheit oder das Überschreiten der angegebenen Toleranz. In Version 4 erweitert die Karte ihre Funktionalität um die Möglichkeit, mehrere Entitäten zu vergleichen – darunter die Bestellung, die erhaltenen Mengen und die Dokumentmengen –, und bietet so mehr Flexibilität bei der Behandlung unterschiedlicher Szenarien.

## **Bestandteile der Karte:**

1. **Any / All:**
   * **Beschreibung**: Gibt an, wie der Vergleich über mehrere Elemente oder Bedingungen hinweg angewendet werden soll.
   * **Optionen**:
     * **Any**: Mindestens eine der Bedingungen muss erfüllt sein, damit die Aktion ausgelöst wird.
     * **All**: Alle Bedingungen müssen erfüllt sein, damit die Aktion fortgesetzt wird.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung fest, die angewendet wird, um die Dokumentmenge mit der angegebenen Toleranz zu vergleichen.
   * **Optionen**:
     * **Gleich (=)**: Prüft, ob die Menge mit dem angegebenen Toleranzwert übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich die Menge vom angegebenen Toleranzwert unterscheidet.
     * **Größer als (>)**: Überprüft, ob die Menge größer als die angegebene Toleranz ist.
     * **Größer oder gleich (≥)**: Prüft, ob die Menge größer oder gleich der angegebenen Toleranz ist.
     * **Kleiner als (<)**: Überprüft, ob die Menge kleiner als die angegebene Toleranz ist.
     * **Kleiner oder gleich (≤)**: Prüft, ob die Menge kleiner oder gleich der angegebenen Toleranz ist.
3. **Toleranzbetrag:**
   * **Beschreibung**: Gibt den Toleranzwert an, mit dem die Dokumentmenge verglichen wird.
   * **Detail**: Dieser Wert ist numerisch und stellt den Schwellenwert der zulässigen Abweichung bei der Menge dar.
4. **Toleranztyp:**
   * **Beschreibung**: Legt die Art der angewendeten Toleranz fest.
   * **Optionen**:
     * **Prozentsatz**: Die Toleranz wird als Prozentsatz der Bestellmenge berechnet.
     * **Wert**: Die Toleranz wird als fester numerischer Wert angegeben.

## **Zusätzliche Komponenten in Version 4:**

* **Vergleichstyp**: Wählt die zu vergleichenden Entitäten aus und bietet in Version 4 mehr Flexibilität bei der Auswertung der Mengen.
  * **Purchase Order to Document**: Vergleicht die Menge in der Bestellung mit der Menge im zugehörigen Dokument.
  * **Received to Document**: Vergleicht die erhaltene Menge mit der Menge im Dokument.
  * **Purchase Order to Received**: Vergleicht die Bestellmenge mit der erhaltenen Menge.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System vergleicht die Menge im Dokument mit der Toleranz in der Bestellung auf Basis des ausgewählten Operators und des Toleranzbetrags/-typs. In Version 4 ermöglicht der **Vergleichstyp** den Vergleich unterschiedlicher Mengen, etwa Bestellung zu Erhalten oder Bestellung zu Dokument, und bietet so einen dynamischeren Vergleich.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt der Vergleich „wahr“ (z. B. liegt die Dokumentmenge innerhalb des zulässigen Toleranzbereichs), wird der Workflow fortgesetzt.
  * **Bedingung nicht erfüllt (False)**: Ergibt der Vergleich „falsch“ (z. B. erfüllt die Menge die Toleranz nicht), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

**Version 3:**

* Benutzer konfigurieren die Karte, indem sie die Dokumentmenge auswählen, den Toleranzbetrag und den Toleranztyp festlegen und den passenden Operator wählen, um die Menge mit der Toleranz zu vergleichen. Die Karte wertet aus, ob die Menge innerhalb des Toleranzschwellenwerts liegt, und fährt je nach Ergebnis mit der "True"- oder "False"-Aktion fort.

**Version 4:**

* Zusätzlich zur Konfiguration aus Version 3 können Benutzer den **Vergleichstyp** auswählen, der Vergleiche zwischen verschiedenen Entitäten ermöglicht, etwa:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Beispiel-Szenario:**

Eine Rechnung zeigt, dass 100 Einheiten geliefert wurden, die Bestellung autorisierte jedoch nur 90 Einheiten. Der Toleranzbetrag ist auf 10 Einheiten gesetzt, und der Toleranztyp ist absolut.

* **Version 3**: Die Karte vergleicht die 100 Einheiten im Dokument mit der Toleranz der Bestellung von 90 Einheiten. Überschreitet die Menge die Toleranz, markiert die Karte die Abweichung zur weiteren Prüfung.
* **Version 4**: Die Karte könnte die **Bestellmenge** (90 Einheiten) mit der **erhaltenen Menge** (100 Einheiten) oder der **Dokumentmenge** (100 Einheiten) vergleichen. Je nach ausgewähltem **Vergleichstyp** prüft sie, ob die Differenz zwischen den beiden Entitäten die Toleranz überschreitet, und löst die entsprechende Aktion aus.

## **Fazit:**

* **Version 3**: Diese Workflow-Karte vergleicht die Dokumentmenge mit der Toleranz der Bestellung und hilft so sicherzustellen, dass Mengenabweichungen markiert und angemessen behandelt werden.
* **Version 4**: Erweitert diese Funktionalität, indem sie es Benutzern ermöglicht, verschiedene Entitäten zu vergleichen, etwa Bestellung zu Erhalten oder Bestellung zu Dokument, und bietet so mehr Flexibilität bei der Behandlung komplexerer Szenarien. Version 4 sorgt für eine engere Kontrolle über Beschaffungs- und Wareneingangs-Workflows und bietet dynamischere Vergleiche und Aktionen auf Basis des gewählten Vergleichstyps.
