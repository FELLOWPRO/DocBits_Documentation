# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Zweck:**

Diese Workflow-Karte führt Operationen abhängig davon aus, ob eine Aufgabe oder ein Dokument einer bestimmten Gruppe oder einer Reihe von Gruppen zugewiesen ist. Sie nutzt bedingte Logik, um bestimmte Aktionen je nach Gruppenzuweisung auszulösen oder zu verhindern, und eignet sich daher ideal für Workflows, die eine gruppenspezifische Behandlung erfordern.

**Bestandteile der Karte:**

1. **Operator**
   * **Beschreibung:** Legt die logische Bedingung fest, die auf die Gruppenzuweisung angewendet wird.
   * **Optionen:**
     * **IS:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe mit einer der Gruppen in der angegebenen Liste übereinstimmt.
     * **IS NOT:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe mit keiner der Gruppen in der angegebenen Liste übereinstimmt.
2. **Gruppenliste**
   * **Beschreibung:** Eine Liste oder Auswahl von Gruppen, die mit der zugewiesenen Gruppe verglichen werden.
   * **Detail:** Diese Liste kann eine oder mehrere Gruppen enthalten, sodass die Karte sowohl einzelne als auch mehrere Gruppenbedingungen effektiv verarbeiten kann.

**Funktionalität:**

* **Erkennung der Gruppenzuweisung:** Identifiziert automatisch die Gruppe oder Gruppen, die einer bestimmten Aufgabe oder einem bestimmten Dokument im System zugewiesen sind.
* **Bedingungsauswertung:**
  * Mit dem Operator **IS** prüft die Karte, ob die zugewiesene Gruppe eine der in der Gruppenliste aufgeführten Gruppen ist.
  * Mit dem Operator **IS NOT** stellt die Karte sicher, dass die zugewiesene Gruppe nicht zu den aufgeführten Gruppen gehört.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Erfüllt die Gruppenzuweisung die Bedingung (entweder **IS** oder **IS NOT**), werden relevante Aktionen ausgelöst, etwa Benachrichtigungen, das Anlegen von Aufgaben, Freigaben oder andere Workflow-Schritte.
  * **Bedingung nicht erfüllt (False):** Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

**Benutzerinteraktionen:**

* **Einrichtung und Konfiguration:** Benutzer konfigurieren die Karte, indem sie einen Operator auswählen und die relevanten Gruppen aus der Gruppenliste angeben. Die Einrichtung sollte benutzerfreundlich und intuitiv sein, um Auswahlen aus potenziell großen Gruppenbeständen zu ermöglichen.
* **Überwachung und Berichterstattung:**\
  Das System sollte Funktionen bereitstellen, um die durch diese Karte ausgelösten Operationen zu überwachen und darüber zu berichten, und so Einblicke in die Zuweisungsgenauigkeit und Prozesseffizienz geben.
* **Fehlerbehandlung und Benachrichtigungen:**\
  Benutzer sollten die Möglichkeit haben, Warnungen oder Benachrichtigungen zu erhalten, wenn es Probleme mit den Zuweisungen gibt, etwa nicht zugewiesene Aufgaben oder Fehler bei der Gruppenauswahl.

**Fazit:**\
Die Workflow-Karte "Assigned Group Condition" ist unverzichtbar für die Verwaltung von Dokument- und Aufgaben-Workflows, die von Gruppenzuweisungen abhängen. Indem sie Bedingungen darauf basieren lässt, ob eine Aufgabe oder ein Dokument bestimmten Gruppen zugewiesen ist, stellt sie sicher, dass Workflows nur durch passende Gruppeninteraktionen ausgelöst werden, und verbessert so die Nachvollziehbarkeit und das Aufgabenmanagement über Teams hinweg.
