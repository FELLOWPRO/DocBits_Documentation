# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte steuert die Ausführung von Operationen abhängig davon, ob eine Aufgabe oder ein Dokument einem bestimmten Benutzer oder einer Reihe von Benutzern zugewiesen ist. Sie nutzt bedingte Logik, um bestimmte Aktionen auszulösen oder zu verhindern, und eignet sich daher ideal für Workflows, die eine benutzerspezifische Behandlung erfordern.

**Bestandteile der Karte**

1. **Operator**
   * **Beschreibung**: Legt die logische Bedingung fest, die auf die Benutzerzuweisung angewendet wird.
   * **Optionen**:
     * **IS**: Löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit einem der Benutzer in der angegebenen Liste übereinstimmt.
     * **IS NOT**: Löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit keinem der Benutzer in der angegebenen Liste übereinstimmt.
2. **Benutzerliste**
   * **Beschreibung**: Eine Liste oder Auswahl von Benutzern, die mit dem zugewiesenen Benutzer verglichen werden.
   * **Detail**: Diese Liste kann einen oder mehrere Benutzer enthalten, sodass die Karte sowohl einzelne als auch mehrere Benutzerbedingungen effektiv verarbeiten kann. Die Auswahl kann über Kontrollkästchen, ein Mehrfachauswahl-Dropdown oder ähnliche UI-Elemente erfolgen.

**Funktionalität**

* **Erkennung der Benutzerzuweisung**: Identifiziert automatisch den oder die Benutzer, die einer bestimmten Aufgabe oder einem bestimmten Dokument im ERP-System zugewiesen sind.
* **Bedingungsauswertung**:
  * Mit dem Operator **IS** prüft die Karte, ob der zugewiesene Benutzer zu den in der Benutzerliste aufgeführten Benutzern gehört.
  * Mit dem Operator **IS NOT** stellt die Karte sicher, dass der zugewiesene Benutzer nicht zu den aufgeführten Benutzern gehört.
* **Ausführung der Aktion**:
  * **Bedingung erfüllt (True)**: Erfüllt die Benutzerzuweisung die Bedingung (entweder IS oder IS NOT), werden relevante Aktionen ausgelöst, etwa Benachrichtigungen, das Anlegen von Aufgaben, Freigaben oder andere Workflow-Schritte.
  * **Bedingung nicht erfüllt (False)**: Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer konfigurieren die Karte, indem sie einen Operator auswählen und die relevanten Benutzer aus der Benutzerliste angeben. Die Einrichtung sollte benutzerfreundlich und intuitiv sein, um Auswahlen aus potenziell großen Benutzerbeständen zu ermöglichen.
* **Überwachung und Berichterstattung**: Das ERP-System sollte Funktionen bereitstellen, um die durch diese Karte ausgelösten Operationen zu überwachen und darüber zu berichten, und so Einblicke in die Zuweisungsgenauigkeit und Prozesseffizienz geben.
* **Fehlerbehandlung und Benachrichtigungen**: Benutzer sollten die Möglichkeit haben, Warnungen oder Benachrichtigungen zu erhalten, wenn es Probleme mit den Zuweisungen gibt, etwa nicht zugewiesene Aufgaben oder Fehler bei der Benutzerauswahl.

#### Fazit

Die Workflow-Karte "Assigned User Condition" ist ein wichtiges Werkzeug für die Verwaltung von Dokument- und Aufgaben-Workflows, die von Benutzerzuweisungen abhängen. Indem sie Bedingungen darauf basieren lässt, ob eine Aufgabe oder ein Dokument bestimmten Benutzern zugewiesen ist, stellt sie sicher, dass Workflows nur durch passende Benutzerinteraktionen ausgelöst werden, und verbessert so sowohl die Nachvollziehbarkeit als auch die Aufgabenzuordnung innerhalb von Teams. Eine klare Dokumentation dieser Karte hilft den Benutzern, ihre Bedeutung zu verstehen und sie effektiv in ihre Workflows zu integrieren, um reibungslose und effiziente Abläufe zu gewährleisten, die auf Benutzerrollen und -verantwortlichkeiten zugeschnitten sind.
