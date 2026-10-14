# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Zweck:**\
Diese Workflow-Karte führt Operationen abhängig davon aus, ob eine Aufgabe oder ein Dokument einer bestimmten Gruppe zugewiesen ist. Sie verwendet eine einfache Bedingung, um Aktionen je nach Gruppenzuweisung auszulösen oder zu verhindern.

**Bestandteile der Karte:**

1. **Operator**
   * **Beschreibung:** Legt die logische Bedingung fest, die auf die Gruppenzuweisung angewendet wird.
   * **Optionen:**
     * **IS:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe mit der angegebenen Gruppe übereinstimmt.
     * **IS NOT:** Löst die Operation aus, wenn die zugewiesene Gruppe des Dokuments oder der Aufgabe nicht mit der angegebenen Gruppe übereinstimmt.
2. **Gruppe**
   * **Beschreibung:** Gibt die Gruppe an, die mit der zugewiesenen Gruppe verglichen wird.
   * **Detail:** In diesem Feld können Sie eine einzelne Gruppe auswählen, mit der die Zuweisung verglichen wird.

**Funktionalität:**

* **Erkennung der Gruppenzuweisung:** Identifiziert automatisch die Gruppe, die einer bestimmten Aufgabe oder einem bestimmten Dokument zugewiesen ist.
* **Bedingungsauswertung:**
  * Mit dem Operator **IS** prüft die Karte, ob die zugewiesene Gruppe mit der angegebenen Gruppe übereinstimmt.
  * Mit dem Operator **IS NOT** stellt die Karte sicher, dass die zugewiesene Gruppe nicht mit der angegebenen Gruppe übereinstimmt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Erfüllt die Gruppenzuweisung die Bedingung (entweder **IS** oder **IS NOT**), werden relevante Aktionen ausgelöst, etwa Benachrichtigungen, das Anlegen von Aufgaben, Freigaben oder andere Workflow-Schritte.
  * **Bedingung nicht erfüllt (False):** Ist die Bedingung nicht erfüllt, kann das Dokument oder die Aufgabe über eine andere Weiterleitung laufen, oder es können alternative Aktionen festgelegt werden.

**Benutzerinteraktionen:**

* **Einrichtung und Konfiguration:**\
  Benutzer konfigurieren die Karte, indem sie einen Operator auswählen und die relevante Gruppe angeben. Die Einrichtung sollte einfach und intuitiv sein.
* **Überwachung und Berichterstattung:**\
  Das System sollte Funktionen bereitstellen, um die durch diese Karte ausgelösten Operationen zu überwachen und darüber zu berichten, und so Einblicke in die Zuweisungsgenauigkeit und Prozesseffizienz geben.
* **Fehlerbehandlung und Benachrichtigungen:**\
  Benutzer sollten die Möglichkeit haben, Warnungen oder Benachrichtigungen zu erhalten, wenn es Probleme mit den Zuweisungen gibt, etwa nicht zugewiesene Aufgaben oder Fehler bei der Gruppenauswahl.

**Fazit:**\
Die Workflow-Karte "Assigned Group Condition" ist unverzichtbar für die Verwaltung von Dokument- und Aufgaben-Workflows auf Basis von Gruppenzuweisungen. Indem sie Bedingungen darauf basieren lässt, ob eine Aufgabe oder ein Dokument einer bestimmten Gruppe zugewiesen ist, stellt sie sicher, dass Workflows nur durch passende Gruppeninteraktionen ausgelöst werden, und verbessert so das Aufgabenmanagement und die Workflow-Effizienz.
