# Zugewiesene Benutzerbedingung

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte verwaltet die Ausführung von Operationen basierend darauf, ob eine Aufgabe oder ein Dokument einem bestimmten Benutzer oder einer Gruppe von Benutzern zugewiesen ist. Sie verwendet bedingte Logik, um spezifische Aktionen auszulösen oder zu verhindern, was sie ideal für Workflows macht, die eine benutzerspezifische Bearbeitung erfordern.

**Komponenten der Karte**

1. **Operator**
* **Beschreibung**: Definiert die logische Bedingung, die auf die Benutzerzuweisung angewendet werden soll.
* **Optionen**:
* **IST**: Löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit einem Benutzer in der angegebenen Liste übereinstimmt.
* **IST NICHT**: Löst die Operation aus, wenn der zugewiesene Benutzer des Dokuments oder der Aufgabe mit keinem Benutzer in der angegebenen Liste übereinstimmt.
2. **Benutzerliste**
* **Beschreibung**: Eine Liste oder Auswahl von Benutzern, die mit dem zugewiesenen Benutzer verglichen werden sollen.
* **Detail**: Diese Liste kann einen oder mehrere Benutzer enthalten, sodass die Karte sowohl einzelne als auch mehrere Benutzerbedingungen effektiv behandeln kann. Die Auswahl kann über Kontrollkästchen, ein Dropdown-Menü für Mehrfachauswahl oder ähnliche UI-Elemente erfolgen.

**Funktionalität**

* **Benutzerzuweisungserkennung**: Identifiziert automatisch den Benutzer oder die Benutzer, die einer bestimmten Aufgabe oder einem Dokument im ERP-System zugewiesen sind.
* **Bedingungsauswertung**:
* Mit dem **IST**-Operator überprüft die Karte, ob der zugewiesene Benutzer in der Benutzerliste aufgeführt ist.
* Mit dem **IST NICHT**-Operator stellt die Karte sicher, dass der zugewiesene Benutzer nicht in der Liste enthalten ist.
* **Aktionenausführung**:
* **Wahre Bedingung**: Wenn die Benutzerzuweisung die Bedingung erfüllt (entweder IST oder IST NICHT), werden relevante Aktionen ausgelöst, wie Benachrichtigungen, Aufgabeninitiierungen, Genehmigungen oder andere Workflow-Schritte.
* **Falsche Bedingung**: Wenn die Bedingung nicht erfüllt ist, kann das Dokument oder die Aufgabe einen anderen Weg durchlaufen, oder es können alternative Aktionen festgelegt werden.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer konfigurieren die Karte, indem sie einen Operator auswählen und die relevanten Benutzer aus der Benutzerliste angeben. Die Einrichtung sollte benutzerfreundlich und intuitiv sein, um Auswahlmöglichkeiten aus potenziell großen Benutzergruppen zu ermöglichen.
* **Überwachung und Berichterstellung**: Das ERP-System sollte Funktionen zur Überwachung und Berichterstellung über die durch diese Karte ausgelösten Operationen bereitstellen und Einblicke in die Genauigkeit der Zuweisung und die Prozesseffizienz bieten.
* **Fehlerbehandlung und Benachrichtigungen**: Benutzer sollten die Möglichkeit haben, Benachrichtigungen zu erhalten, wenn es Probleme mit den Zuweisungen gibt, wie nicht zugewiesene Aufgaben oder Fehler bei der Benutzerauswahl.

#### Fazit

Die Workflow-Karte "Zugewiesene Benutzerbedingung" ist ein wichtiges Werkzeug zur Verwaltung von Dokumenten- und Aufgaben-Workflows, die von Benutzerzuweisungen abhängen. Indem Bedingungen basierend darauf ermöglicht werden, ob eine Aufgabe oder ein Dokument bestimmten Benutzern zugewiesen ist, wird sichergestellt, dass Workflows nur durch geeignete Benutzerinteraktionen ausgelöst werden, was sowohl die Rechenschaftspflicht als auch die Aufgabenabstimmung innerhalb von Teams verbessert. Eine klare Dokumentation dieser Karte hilft Benutzern, ihre Bedeutung zu verstehen und sie effektiv in ihre Workflows zu integrieren, um reibungslose und effiziente Abläufe anzupassen, die auf Benutzerrollen und -verantwortlichkeiten zugeschnitten sind.
