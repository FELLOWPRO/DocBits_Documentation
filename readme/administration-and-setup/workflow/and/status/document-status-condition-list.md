# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Zweck**

Diese Karte ist darauf ausgelegt, Workflow-Aktionen auf Basis des aktuellen Status eines Dokuments zu steuern, wobei eine bedingte Logik verwendet wird, um bestimmte Prozesse entweder auszulösen oder einzuschränken. Sie stellt sicher, dass Dokumente nur dann durch Workflows laufen, wenn sie vordefinierte Statuskriterien erfüllen.

**Bestandteile der Karte**

1. **Operator**
   * **Beschreibung**: Bestimmt, wie der Dokumentstatus anhand einer angegebenen Bedingung ausgewertet wird.
   * **Optionen**:
     * **is**: Löst die zugehörigen Aktionen aus, wenn der aktuelle Status des Dokuments mit einem der angegebenen Status übereinstimmt.
     * **is not**: Löst die Aktionen aus, wenn der Status des Dokuments mit keinem der angegebenen Status übereinstimmt.
2. **Status ( List )**
   * **Beschreibung**: Listet die spezifischen Status auf, mit denen der aktuelle Status des Dokuments verglichen wird.
   * **Beispiele**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Diese stellen verschiedene Phasen oder Zustände dar, in denen sich ein Dokument innerhalb eines Workflow-Prozesses befinden kann.

**Funktionalität**

* **Statuserkennung**: Identifiziert automatisch den aktuellen Status eines Dokuments, während es sich durch den Workflow des ERP-Systems bewegt.
* **Bedingungsauswertung**: Wendet den gewählten Operator (is oder is not) auf den Status des Dokuments im Vergleich zu den aufgeführten Status an:
  * Bei **is** wird geprüft, ob der Status des Dokuments mit einem Status in der Liste übereinstimmt.
  * Bei **is not** wird geprüft, ob der Status des Dokuments nicht in der Liste erscheint.
* **Ausführung der Aktion**: Je nach Ergebnis der Bedingungsauswertung:
  * **True**: Führt vordefinierte Aktionen oder Workflows aus, wenn die Bedingung erfüllt ist.
  * **False**: Überspringt die Aktion oder löst alternative Workflows aus, wenn die Bedingung nicht erfüllt ist.
* **Workflow-Integration**: Integriert sich nahtlos in andere Workflow-Komponenten und stellt sicher, dass die Dokumentbearbeitung systemweit koordiniert ist.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer konfigurieren die Karte, indem sie den Operator auswählen und die relevanten Status angeben. Diese Einrichtung kann einfache Dropdown-Menüs oder Kontrollkästchen zur Auswahl von Status und Operatoren umfassen.
* **Überwachung und Verwaltung**: Benutzer können die Aktivität der Karte über ein Dashboard verfolgen, das Einblicke in die überwachten Statusbedingungen und die darauf basierenden Aktionen bietet.
* **Fehlerbehandlung und Warnungen**: Unterstützt das Einrichten von Warnungen bei Prozessfehlern oder Abweichungen bei den erwarteten Dokumentstatus und ermöglicht so schnelle Reaktionen auf betriebliche Probleme.

#### Fazit

Die Workflow-Karte "Document Status Condition" ist unverzichtbar, um sicherzustellen, dass Dokumente entsprechend ihrem aktuellen Status korrekt verarbeitet werden, und stärkt so Kontrolle und Effizienz innerhalb des ERP-Systems. Eine klare Dokumentation dieser Karte im Systemhandbuch hilft den Benutzern, sie effektiv einzusetzen und zu verwalten und ihre Funktionalität zu nutzen, um reibungslose und konforme Dokument-Workflows aufrechtzuerhalten. Diese Karte ist besonders nützlich für die Verwaltung von Dokumentlebenszyklen und stellt sicher, dass nur Dokumente, die bestimmte Kriterien erfüllen, in nachfolgende Phasen von Geschäftsprozessen übergehen.
