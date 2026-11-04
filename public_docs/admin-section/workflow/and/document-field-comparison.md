# Dokumentenfeldvergleich

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Workflow-Karte ist darauf ausgelegt, automatisch die Werte von zwei angegebenen Feldern innerhalb eines Dokuments anhand eines definierten Operators zu vergleichen. Sie wird verwendet, um die Datenintegrität durchzusetzen und sicherzustellen, dass die Dokumentendaten den Geschäftsregeln oder Bedingungen entsprechen.

**Komponenten der Karte**

1. **Feldnamen**
* **Beschreibung**: Gibt die Namen der beiden Felder im Dokument an, die verglichen werden sollen.
* **Detail**: Benutzer müssen die genauen Namen der Felder eingeben, wie sie im System erscheinen. Diese Felder können jeden Datentyp unterstützen, der Vergleiche ermöglicht, wie numerische, Datums- oder Textfelder.
2. **Operator**
* **Beschreibung**: Der Vergleichsoperator, der verwendet wird, um die Beziehung zwischen den Werten der beiden Felder zu bewerten.
* **Optionen**:
* **Gleich (==)**: Überprüft, ob der Wert des ersten Feldes gleich dem Wert des zweiten Feldes ist.
* **Nicht gleich (!=)**: Überprüft, ob der Wert des ersten Feldes ungleich dem Wert des zweiten Feldes ist.
* **Größer als (>)**: Überprüft, ob der Wert des ersten Feldes größer ist als der Wert des zweiten Feldes.
* **Größer als oder gleich (>=)**: Überprüft, ob der Wert des ersten Feldes größer oder gleich dem Wert des zweiten Feldes ist.
* **Kleiner als (<)**: Überprüft, ob der Wert des ersten Feldes kleiner ist als der Wert des zweiten Feldes.
* **Kleiner als oder gleich (<=)**: Überprüft, ob der Wert des ersten Feldes kleiner oder gleich dem Wert des zweiten Feldes ist.

**Funktionalität**

* **Feldauswahl**: Benutzer geben die Namen der beiden zu vergleichenden Felder ein oder wählen sie aus. Dies erfolgt in der Regel über ein Formular oder ein Dropdown-Menü innerhalb der Karteneinrichtung.
* **Operatorauswahl**: Benutzer wählen einen Operator aus einer Liste verfügbarer Optionen aus, der definiert, wie die Felder verglichen werden sollen.
* **Vergleichsausführung**:
* Das System liest die Werte aus den angegebenen Feldern und wendet den ausgewählten Operator an, um die Beziehung zwischen ihnen zu bewerten.
* Basierend auf dem Ergebnis des Vergleichs (wahr oder falsch) können nachfolgende Aktionen ausgelöst werden. Wenn beispielsweise ein Vergleich fehlschlägt, könnte das System das Dokument zur Überprüfung markieren, die weitere Verarbeitung blockieren oder die verantwortlichen Parteien benachrichtigen.

**Benutzerinteraktionen**

* **Einrichtung und Konfiguration**: Benutzer konfigurieren den Vergleich, indem sie Feldnamen eingeben und einen Operator auswählen. Diese Einrichtung sollte einfach und geführt sein, möglicherweise mit Hilfetexten oder Beispielen.
* **Überwachung und Berichterstattung**: Das System kann Feedback zu den Ergebnissen von Vergleichen geben, wie das Protokollieren aller durchgeführten Vergleiche, ihrer Ergebnisse und etwaiger Maßnahmen als Reaktion auf die Vergleichsergebnisse.
* **Fehlerbehandlung und Benachrichtigungen**: Benutzer erhalten Benachrichtigungen, wenn der Vergleich nicht ausgeführt werden kann (z. B. wenn eines der Felder im Dokument nicht gefunden wird oder nicht in einem vergleichbaren Format vorliegt).

#### Fazit

Die Workflow-Karte "Dokumentenfeldvergleich" ist entscheidend für die Aufrechterhaltung der Datenpräzision und -konsistenz in Dokumenten eines ERP-Systems. Sie hilft dabei, Überprüfungen zu automatisieren, die ansonsten manuell, fehleranfällig und zeitaufwändig wären, und verbessert so die Effizienz und Zuverlässigkeit bei der Dokumentenverarbeitung. Eine klare Dokumentation dieser Karte in der Anleitung Ihres ERP-Systems wird Benutzern dabei helfen, diese Funktion effektiv einzusetzen und sicherzustellen, dass die Daten in den Dokumenten konsistent bleiben und den Geschäftsregeln entsprechen.
