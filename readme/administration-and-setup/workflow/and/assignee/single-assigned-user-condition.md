# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte ermöglicht Operationen auf Basis der Zuweisung einer Aufgabe oder eines Dokuments zu einem einzelnen, bestimmten Benutzer. Mit einem direkten Ansatz aus bedingter Logik steuert sie Workflows, die ein gezieltes Benutzerengagement erfordern, und gewährleistet so Präzision bei der benutzerbasierten Aufgabenbearbeitung.

**Bestandteile der Karte**

1. **Operator**
   * **Beschreibung**: Gibt die Logik an, die auf die Benutzerzuweisung angewendet wird.
   * **Optionen**:
     * **IS**: Löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit dem angegebenen Benutzer übereinstimmt.
     * **IS NOT**: Löst die Operation aus, wenn der zugewiesene Benutzer nicht mit dem angegebenen Benutzer übereinstimmt.
2. **Benutzer**
   * **Beschreibung**: Ermöglicht die Auswahl eines einzelnen Benutzers, mit dem der zugewiesene Benutzer verglichen wird.
   * **Detail**: Dies erfolgt über ein einfaches Dropdown- oder Autovervollständigungsfeld, in dem jeweils ein Benutzer ausgewählt werden kann.

**Funktionalität**

* **Erkennung der Benutzerzuweisung**: Identifiziert den Benutzer, der einer bestimmten Aufgabe oder einem bestimmten Dokument aktuell zugewiesen ist.
* **Bedingungsauswertung**:
  * Beim Operator **IS** prüft die Karte, ob der zugewiesene Benutzer mit dem ausgewählten Benutzer identisch ist.
  * Beim Operator **IS NOT** überprüft sie, ob sich der zugewiesene Benutzer vom ausgewählten Benutzer unterscheidet.
* **Ausführung der Aktion**:
  * **Bedingung erfüllt (True)**: Erfüllt die Zuweisung die festgelegte Bedingung (IS oder IS NOT), löst sie vordefinierte Aktionen aus, etwa das Fortfahren mit Freigaben, das Anstoßen weiterer Aufgaben, das Senden von Benachrichtigungen oder andere zugehörige Workflows.
  * **Bedingung nicht erfüllt (False)**: Ist die Bedingung nicht erfüllt, wird der Workflow nicht fortgesetzt.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer richten die Karte ein, indem sie einen Operator wählen und einen Benutzer aus dem Benutzerfeld auswählen. Diese Einrichtung sollte unkompliziert sein und eine einfache Benutzerauswahl und Konfiguration ermöglichen.
* **Überwachung und Berichterstattung**: Bietet Werkzeuge zur Überwachung der Leistung der Karte, etwa die Nachverfolgung, welche Aufgaben durch bestimmte Benutzerzuweisungen ausgelöst werden, und der Ergebnisse dieser Auslöser.
* **Fehlerbehandlung und Benachrichtigungen**: Stellt Mechanismen bereit, um Benutzer zu warnen, wenn Aufgaben falsch zugewiesen werden oder wenn betriebliche Fehler aufgrund von Zuweisungsproblemen auftreten.

#### Fazit

Die Workflow-Karte "Single Assigned User Condition" ist unverzichtbar für ein präzises, benutzerspezifisches Dokument- und Aufgabenmanagement innerhalb eines ERP-Systems. Sie vereinfacht Workflows, indem sie sich auf einzelne Benutzerzuweisungen konzentriert, und stellt so sicher, dass Aktionen nur dann ausgeführt werden, wenn es angemessen ist – basierend auf der Rolle und den Verantwortlichkeiten des Benutzers. Eine klare Dokumentation dieser Karte unterstützt die Benutzer dabei, ihre Anwendung zu verstehen, und ermöglicht es ihnen, sie effektiv in ihren täglichen Abläufen einzusetzen und zu verwalten. Diese Dokumentation stellt sicher, dass alle potenziellen Benutzer den Zweck der Karte leicht erfassen und sie nahtlos in ihre Workflows integrieren können.
