# Zugewiesene Gruppenbedingung

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-bdcdca2a5488-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

**Zweck:**

Diese Workflow-Karte führt Operationen abhängig davon aus, ob eine Aufgabe oder ein Dokument einer bestimmten Gruppe oder einer Reihe von Gruppen zugewiesen ist. Sie nutzt bedingte Logik, um bestimmte Aktionen je nach Gruppenzuweisung auszulösen oder zu verhindern, und eignet sich daher ideal für Workflows, die eine gruppenspezifische Behandlung erfordern.

**Bestandteile der Karte:**

1. **Operator**
   * **Beschreibung:** Legt die logische Bedingung fest, die auf die Gruppenzuweisung angewendet wird.
   * **Optionen:**
     * **IS:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe mit einer der Gruppen in der angegebenen Liste übereinstimmt.
     * **IST NICHT:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe mit keiner der Gruppen in der angegebenen Liste übereinstimmt.
2. **Gruppenliste**
   * **Beschreibung:** Eine Liste oder Auswahl von Gruppen, die mit der zugewiesenen Gruppe verglichen werden.
   * **Detail:** Diese Liste kann eine oder mehrere Gruppen enthalten, sodass die Karte sowohl einzelne als auch mehrere Gruppenbedingungen effektiv verarbeiten kann.

**Funktionalität:**

* **Erkennung der Gruppenzuweisung:** Identifiziert automatisch die Gruppe oder Gruppen, die einer bestimmten Aufgabe oder einem bestimmten Dokument im System zugewiesen sind.
* **Bedingungsauswertung:**
  * Mit dem Operator **IS** prüft die Karte, ob die zugewiesene Gruppe eine der in der Gruppenliste aufgeführten Gruppen ist.
  * Mit dem Operator **IST NICHT** stellt die Karte sicher, dass die zugewiesene Gruppe nicht zu den aufgeführten Gruppen gehört.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Erfüllt die Gruppenzuweisung die Bedingung (entweder **IS** oder **IST NICHT**), werden relevante Aktionen ausgelöst, etwa Benachrichtigungen, das Anlegen von Aufgaben, Freigaben oder andere Workflow-Schritte.
  * **Bedingung nicht erfüllt (False):** Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

**Benutzerinteraktionen:**

* **Einrichtung und Konfiguration:** Benutzer konfigurieren die Karte, indem sie einen Operator auswählen und die relevanten Gruppen aus der Gruppenliste angeben. Die Einrichtung sollte benutzerfreundlich und intuitiv sein, um Auswahlen aus potenziell großen Gruppenbeständen zu ermöglichen.
* **Überwachung und Berichterstattung:**\
  Das System sollte Funktionen bereitstellen, um die durch diese Karte ausgelösten Operationen zu überwachen und darüber zu berichten, und so Einblicke in die Zuweisungsgenauigkeit und Prozesseffizienz geben.
* **Fehlerbehandlung und Benachrichtigungen:**\
  Benutzer sollten die Möglichkeit haben, Warnungen oder Benachrichtigungen zu erhalten, wenn es Probleme mit den Zuweisungen gibt, etwa nicht zugewiesene Aufgaben oder Fehler bei der Gruppenauswahl.

**Fazit:**\
Die Workflow-Karte "Assigned Group Condition" ist unverzichtbar für die Verwaltung von Dokument- und Aufgaben-Workflows, die von Gruppenzuweisungen abhängen. Indem sie Bedingungen darauf basieren lässt, ob eine Aufgabe oder ein Dokument bestimmten Gruppen zugewiesen ist, stellt sie sicher, dass Workflows nur durch passende Gruppeninteraktionen ausgelöst werden, und verbessert so die Nachvollziehbarkeit und das Aufgabenmanagement über Teams hinweg.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Wann zu verwenden ist:** Wenden Sie dieselbe Regel auf zwei Prüfteams an.

**Konfiguration:** Wählen Sie eine der konfigurierten Gruppen `Demo Finance` und `Demo Procurement` aus.

**Erwartetes Ergebnis und Gegenbeispiel:** Ein Dokument, das einer der ausgewählten Gruppen zugeordnet ist, besteht. Ein Dokument, das nur `Demo Support` zugewiesen ist, schlägt fehl.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
