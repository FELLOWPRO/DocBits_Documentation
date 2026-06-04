# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Karte ist darauf ausgelegt, Aktionen an Dokumenten abhängig von ihrem Typ zu steuern, wobei eine einfache bedingte Logik (is/is not) verwendet wird, um bestimmte Workflows entweder auszulösen oder zu verhindern. Dies ermöglicht eine präzise Kontrolle darüber, wie verschiedene Dokumenttypen innerhalb des ERP-Systems verarbeitet werden.

## **Bestandteile der Karte:**

1. **Operator**
   * **Beschreibung**: Bestimmt die auf die Dokumenttypen angewendete bedingte Logik.
   * **Optionen**:
     * **is**: Die Operation wird ausgelöst, wenn der Typ des Dokuments mit einem der angegebenen Typen in der Liste übereinstimmt.
     * **is not**: Die Operation wird ausgelöst, wenn der Typ des Dokuments mit keinem der aufgeführten Typen übereinstimmt.
2. **Dokumenttypenliste**
   * **Beschreibung**: Gibt eine Liste von Dokumenttypen an, für die die Bedingung gilt.
   * **Detail**: Diese umfasst verschiedene Dokumenttypen wie "Invoice", "Purchase Order" usw., auf deren Grundlage die Bedingung (is/is not) ausgewertet wird.

## Funktionalität:

* **Bedingungsauswertung:** Das System prüft, ob der Dokumenttyp die Operatorbedingung (is oder is not) anhand der angegebenen Dokumenttypenliste erfüllt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):**\
    Erfüllt der Dokumenttyp die angegebene Bedingung (ist entweder in der Liste enthalten oder nicht), wird der Workflow fortgesetzt. Dies kann Prozesse wie Dokumentfreigaben, bestimmte Validierungen oder Weiterleitungsaktionen auslösen.
  * **Bedingung nicht erfüllt (False):**\
    Erfüllt der Dokumenttyp die Bedingung nicht, werden alternative Aktionen ausgeführt, etwa das Ablehnen des Dokuments oder das Anhalten des Workflows.

## Einrichtung und Konfiguration:

* Benutzer konfigurieren die Karte, indem sie das Dokumenttyp-Feld auswählen und den Operator (is oder is not) festlegen. Anschließend geben sie die Liste der zu prüfenden Dokumenttypen an. Die Einrichtung ist unkompliziert und umfasst Dropdown-Menüs für die Feld- und Operatorauswahl sowie ein Feld zur Eingabe der Liste der Dokumenttypen.

## Fazit:

Die Workflow-Karte "Document Type Condition" spielt eine entscheidende Rolle bei der präzisen und flexiblen Steuerung dokumentbasierter Vorgänge. Durch die Verwendung einer einfachen bedingten Logik hilft sie sicherzustellen, dass Dokumente angemessen verarbeitet werden, und steigert so die Effizienz und Compliance. Eine klare Dokumentation dieser Karte hilft Benutzern zu verstehen, wie sie sie effektiv einsetzen und nutzen können, und macht sie zu einem wertvollen Bestandteil der Dokumentation Ihres ERP-Systems.
