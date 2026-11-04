# Einzelner Dokumentenstatusbedingung

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte ist darauf ausgerichtet, Operationen an Dokumenten basierend auf einem einzigen, festgelegten Dokumentenstatus zu verwalten. Durch Vereinfachung der Bedingung auf einen Status konzentriert sich die Karte auf sehr spezifische Workflow-Auslöser, was sie ideal für gezielte Dokumentenverarbeitungsaktivitäten innerhalb eines ERP-Systems macht.

**Komponenten der Karte**

1. **Operator**
* **Beschreibung**: Legt die Methode fest, um den Status des Dokuments gegen die ausgewählte Bedingung zu bewerten.
* **Optionen**:
* **ist**: Löst die Operation aus, wenn der aktuelle Status des Dokuments mit dem ausgewählten Status übereinstimmt.
* **ist nicht**: Löst die Operation aus, wenn der aktuelle Status des Dokuments nicht mit dem ausgewählten Status übereinstimmt.
2. **Status**
* **Beschreibung**: Ermöglicht die Auswahl eines einzelnen Dokumentenstatus, um die Bedingung festzulegen.
* **Beispiele für Status**: "Fehler", "Exportfehler", "Bereit zur Validierung", "Bereit zur Überprüfung", "Genehmigung ausstehend", "Zweite Genehmigung ausstehend".
* **Details**: Benutzer wählen einen Status aus einem Dropdown-Menü oder einer Gruppe von Optionsfeldern aus. Dieser Status dient dann als Kriterium für die Operation der Karte.

**Funktionalität**

* **Identifizierung des Dokumentenstatus**: Ermittelt den aktuellen Status eines Dokuments, während es durch das ERP-System verarbeitet wird.
* **Bedingungsauswertung**:
* Basierend auf dem ausgewählten Operator (`ist` oder `ist nicht`) überprüft die Karte, ob der aktuelle Status des Dokuments mit dem gewählten Statuskriterium übereinstimmt.
* **Ausführung der Aktion**:
* **Wahre Bedingung**: Wenn der Status übereinstimmt (oder nicht übereinstimmt, basierend auf dem Operator), wird die entsprechende Aktion eingeleitet. Dies könnte die Weiterleitung zur weiteren Verarbeitung, die Generierung von Benachrichtigungen oder andere vordefinierte Workflows sein.
* **Falsche Bedingung**: Wenn die Bedingung nicht erfüllt ist, wird keine Aktion ausgeführt oder ein alternativer Pfad wird ausgelöst.
* **Integration mit anderen Workflows**: Obwohl es für die Bewertung eines einzelnen Status konzipiert ist, kann diese Karte effektiv in breitere Workflow-Sequenzen integriert werden, um eine präzise Dokumentenverarbeitung sicherzustellen.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer richten die Karte ein, indem sie einen Operator auswählen und dann einen Status aus den verfügbaren Optionen wählen. Dieser Auswahlprozess ist unkompliziert und soll Verwirrung vermeiden.
* **Überwachung und Berichterstellung**: Ermöglicht die Überwachung durch systemgenerierte Berichte oder Dashboards, die die Verarbeitung von Dokumenten basierend auf ihrem Status verfolgen und dazu beitragen, die Effektivität der implementierten Workflows zu überwachen.
* **Fehlerbehandlung und Benachrichtigungen**: Konfigurierbar, um Benutzer über Verarbeitungsanomalien zu informieren oder Dokumente zu kennzeichnen, die die festgelegten Bedingungen nicht erfüllen, um eine schnelle Aufmerksamkeit und Lösung sicherzustellen.

#### Fazit

Die Workflow-Karte "Einzelner Dokumentenstatusbedingung" vereinfacht das Dokumentenmanagement, indem sie sich auf einzelne Statusbedingungen konzentriert. Diese Spezifikation ist hilfreich in Fällen, in denen eine präzise Kontrolle über Dokumentenflüsse erforderlich ist, insbesondere in Umgebungen mit strengen Verarbeitungskriterien. Eine klare Dokumentation dieser Version der Karte stellt sicher, dass Benutzer ihre Anwendung vollständig verstehen und sie effektiv in ihren täglichen Abläufen integrieren können, was sowohl die Einhaltung als auch die Effizienz bei der Dokumentenverarbeitung verbessert.
