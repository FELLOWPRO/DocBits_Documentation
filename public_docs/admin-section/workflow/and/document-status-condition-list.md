# Liste der Dokumentenstatusbedingungen

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Karte ist darauf ausgelegt, Workflow-Aktionen basierend auf dem aktuellen Status eines Dokuments zu steuern, indem bedingte Logik verwendet wird, um bestimmte Prozesse auszulösen oder einzuschränken. Sie stellt sicher, dass Dokumente nur durch Workflows fortschreiten, wenn sie vordefinierte Statuskriterien erfüllen.

**Komponenten der Karte**

1. **Operator**
* **Beschreibung**: Bestimmt, wie der Dokumentenstatus gegen eine spezifizierte Bedingung ausgewertet wird.
* **Optionen**:
* **ist**: Löst die zugehörigen Aktionen aus, wenn der aktuelle Status des Dokuments einem der spezifizierten Status entspricht.
* **ist nicht**: Löst die Aktionen aus, wenn der Status des Dokuments keinem der spezifizierten Status entspricht.
2. **Status (Liste)**&#x20;
* **Beschreibung**: Listet die spezifischen Status auf, gegen die der aktuelle Status des Dokuments verglichen wird.
* **Beispiele**: "Fehler", "Exportfehler", "Bereit zur Validierung", "Bereit zur Überprüfung", "Genehmigung ausstehend", "Zweite Genehmigung ausstehend". Diese repräsentieren verschiedene Stadien oder Bedingungen, in denen sich ein Dokument innerhalb eines Workflow-Prozesses befinden könnte.

**Funktionalität**

* **Statusidentifikation**: Identifiziert automatisch den aktuellen Status eines Dokuments, während es durch den Workflow des ERP-Systems bewegt wird.
* **Bedingungsauswertung**: Wendet den gewählten Operator (ist oder ist nicht) auf den Status des Dokuments im Vergleich zu den aufgelisteten Status an:
* Wenn **ist**, wird überprüft, ob der Status des Dokuments mit einem Status in der Liste übereinstimmt.
* Wenn **ist nicht**, wird überprüft, ob der Status des Dokuments nicht in der Liste erscheint.
* **Aktionenausführung**: Abhängig vom Ergebnis der Bedingungsauswertung:
* **Wahr**: Führt vordefinierte Aktionen oder Workflows aus, wenn die Bedingung erfüllt ist.
* **Falsch**: Überspringt oder löst alternative Workflows aus, wenn die Bedingung nicht erfüllt ist.
* **Workflow-Integration**: Integriert sich nahtlos mit anderen Workflow-Komponenten und stellt sicher, dass die Dokumentenbearbeitung im gesamten System koordiniert ist.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer konfigurieren die Karte, indem sie den Operator auswählen und die relevanten Status spezifizieren. Diese Einrichtung kann einfache Dropdown-Menüs oder Kontrollkästchen für die Auswahl von Status und Operatoren umfassen.
* **Überwachung und Verwaltung**: Benutzer können die Aktivität der Karte über ein Dashboard verfolgen, das Einblicke in die überwachten Statusbedingungen und die basierenden Aktionen bietet.
* **Fehlerbehandlung und Warnungen**: Unterstützt das Einrichten von Warnungen für Prozessfehler oder Abweichungen von erwarteten Dokumentenstatus, um schnelle Reaktionen auf operative Probleme zu ermöglichen.

#### Fazit

Die Workflow-Karte "Dokumentenstatusbedingung" ist entscheidend, um sicherzustellen, dass Dokumente gemäß ihrem aktuellen Status korrekt verarbeitet werden, was die Kontrolle und Effizienz im ERP-System verbessert. Eine klare Dokumentation dieser Karte im Handbuch des Systems hilft Benutzern dabei, sie effektiv zu implementieren und zu verwalten, wobei ihre Funktionalität genutzt wird, um reibungslose und konforme Dokumentenworkflows aufrechtzuerhalten. Diese Karte ist besonders nützlich für das Management von Dokumentenlebenszyklen und dafür zu sorgen, dass nur Dokumente, die bestimmte Kriterien erfüllen, in nachfolgende Phasen von Geschäftsprozessen übergehen.
