# Einzelne zugewiesene Benutzerbedingung

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte erleichtert Operationen, die auf der Zuweisung einer Aufgabe oder eines Dokuments an einen einzelnen, spezifischen Benutzer basieren. Mit einem direkten bedingten logischen Ansatz verwaltet sie Workflows, die eine gezielte Benutzerinteraktion erfordern und so eine präzise Bearbeitung von benutzerbasierten Aufgaben gewährleisten.

**Komponenten der Karte**

1. **Operator**
* **Beschreibung**: Legt die Logik fest, die auf die Benutzerzuweisung angewendet werden soll.
* **Optionen**:
* **IST**: löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit dem angegebenen Benutzer übereinstimmt.
* **IST NICHT**: löst die Operation aus, wenn der zugewiesene Benutzer nicht mit dem angegebenen Benutzer übereinstimmt.
2. **Benutzer**
* **Beschreibung**: Ermöglicht die Auswahl eines einzelnen Benutzers, mit dem der zugewiesene Benutzer verglichen wird.
* **Detail**: Dies umfasst ein einfaches Dropdown-Menü oder ein Autocomplete-Feld, in dem jeweils ein Benutzer ausgewählt werden kann.

**Funktionalität**

* **Identifizierung der Benutzerzuweisung**: Ermittelt den Benutzer, der derzeit einer bestimmten Aufgabe oder einem bestimmten Dokument zugewiesen ist.
* **Bedingungsauswertung**:
* Für den Operator **IST** überprüft die Karte, ob der zugewiesene Benutzer mit dem ausgewählten Benutzer übereinstimmt.
* Für den Operator **IST NICHT** wird überprüft, ob der zugewiesene Benutzer vom ausgewählten Benutzer abweicht.
* **Aktionenausführung**:
* **Wahre Bedingung**: Wenn die Zuweisung die festgelegte Bedingung erfüllt (IST oder IST NICHT), löst sie vordefinierte Aktionen aus, die das Weiterleiten von Genehmigungen, das Initiieren weiterer Aufgaben, das Senden von Benachrichtigungen oder andere damit verbundene Workflows umfassen könnten.
* **Falsche Bedingung**: Wenn die Bedingung nicht erfüllt ist, kann das System die Aufgabe umleiten, sie zur Überprüfung halten oder alternative vordefinierte Aktionen auslösen.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer richten die Karte ein, indem sie einen Operator auswählen und einen Benutzer aus dem Benutzerfeld auswählen. Diese Einrichtung sollte unkompliziert sein und eine einfache Benutzerwahl und Konfiguration ermöglichen.
* **Überwachung und Berichterstellung**: Bietet Tools zur Überwachung der Leistung der Karte, z. B. zur Verfolgung, welche Aufgaben durch bestimmte Benutzerzuweisungen ausgelöst werden und welche Ergebnisse diese Auslöser haben.
* **Fehlerbehandlung und Benachrichtigungen**: Bietet Mechanismen, um Benutzer zu benachrichtigen, wenn Aufgaben falsch zugewiesen sind oder wenn operative Fehler aufgrund von Zuweisungsproblemen auftreten.

#### Fazit

Die Workflow-Karte "Einzelne zugewiesene Benutzerbedingung" ist für die präzise, benutzerspezifische Dokumenten- und Aufgabenverwaltung innerhalb eines ERP-Systems unerlässlich. Sie vereinfacht Workflows, indem sie sich auf individuelle Benutzerzuweisungen konzentriert und so sicherstellt, dass Aktionen nur ausgeführt werden, wenn sie entsprechend der Rolle und Verantwortlichkeiten des Benutzers angemessen sind. Eine klare Dokumentation dieser Karte hilft Benutzern, ihre Anwendung zu verstehen, sodass sie diese effektiv in ihren täglichen Abläufen implementieren und verwalten können. Diese Dokumentation stellt sicher, dass alle potenziellen Benutzer den Zweck der Karte leicht erfassen und nahtlos in ihre Workflows integrieren können.
