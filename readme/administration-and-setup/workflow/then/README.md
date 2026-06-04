# Then

## Überblick über die "Then..."-Aktionskarten

### **1. Document Field-Aktionen:**

* **Invert Checkbox:** Diese Aktion kehrt den Zustand eines Kontrollkästchenfelds in einem Dokument um.
* **Set Checkbox:** Setzt den Zustand eines Kontrollkästchenfelds auf entweder wahr (aktiviert) oder falsch (deaktiviert).
* **Set Field to Text:** Diese Aktion setzt ein angegebenes Dokumentfeld auf einen bestimmten Textwert.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Document-Aktionen:**

* **Approve the Document:** Markiert ein Dokument im System als freigegeben.
* **Reject the Document:** Markiert ein Dokument als abgelehnt.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Export-Aktionen:**

* **Export document with export configuration:** Startet den Exportvorgang mit einer bestimmten Exportkonfiguration.
* **Start Export:** Startet den Exportvorgang.



<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Status-Aktionen:**



* **Change Status:** Ändert den Status eines Dokuments oder einer Aufgabe in einen angegebenen neuen Status.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Task-Aktionen:**

* Zuweisungen und Benachrichtigungen:
  * **Assign Task:** Erstellt und weist eine Aufgabe mit bestimmten Details einer Einzelperson oder Gruppe zu, einschließlich der Option, diese per E-Mail zu benachrichtigen.
  * **Create a New Task:** Ähnlich wie Zuweisen, jedoch mit dem Fokus auf das Einrichten einer völlig neuen Aufgabe im System.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Table-Aktionen:**

* **Calculate in Table:** Führt Berechnungen mit Tabellendaten auf Basis festgelegter Bedingungen durch und speichert die Ergebnisse in einer bestimmten Spalte.
* **Change Entries:** Aktualisiert Einträge in einer Tabelle auf Basis festgelegter Bedingungen.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Assignee-Aktionen:**

* **Assign User from Field:** Weist einer Aufgabe oder einem Dokument einen Benutzer auf Basis von Benutzerdaten zu, die in einem bestimmten Feld gespeichert sind, mit der Option eines Ersatzbenutzers, falls der primäre nicht verfügbar ist.
* **Assign Document to User or Group:** Weist ein Dokument direkt einem Benutzer oder einer Gruppe zu und stellt so sicher, dass die Verantwortung angemessen festgelegt wird.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Aktionen für externe Interaktionen:**

* **Call API:** Sendet eine Anfrage an eine externe API, die mit bestimmten Methoden, Parametern und Daten angepasst werden kann.
* **Send HTTPS Request:** Ähnlich wie API-Aufrufe, jedoch speziell für HTTPS-Protokolle formatiert.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Erweiterte Verarbeitung:**

* **Run Workflow:** Löst einen weiteren Workflow innerhalb des Systems aus und ermöglicht so die Verkettung komplexer Prozesse.

#### Praktische Anwendung

Diese Aktionskarten werden verwendet, um Reaktionen auf Basis bestimmter Auslöser zu automatisieren, die in den früheren Teilen der Workflow-Einrichtung identifiziert wurden. Zum Beispiel:

* Wenn ein Dokument als prüfungsbedürftig identifiziert wird, kann die Aktion "Approve the Document" automatisch ausgelöst werden, sobald es alle festgelegten Bedingungen erfüllt.
* Für Aufgaben der Datenverwaltung stellen Aktionen wie "Set Checkbox" oder "Set Field to Text" sicher, dass Dokumentfelder automatisch aktualisiert werden, wodurch manuelle Dateneingaben und das Fehlerpotenzial reduziert werden.
* Komplexe Aufgaben wie API-Interaktionen oder Statusänderungen optimieren Interaktionen nicht nur innerhalb des ERP-Systems, sondern auch mit externen Diensten und Tools und verbessern so Integration und Funktionalität.

### Fazit

Der Abschnitt "Then..." in Ihrem Workflow-System bietet robuste Werkzeuge, um präzise Aktionen zu definieren, die als Ergebnis erfüllter Workflow-Bedingungen erfolgen sollen. Durch den effektiven Einsatz dieser Aktionen können Unternehmen Routineprozesse automatisieren, die Datengenauigkeit sicherstellen und dynamisch auf sich ändernde Informationen und Systemzustände reagieren. Zu verstehen, wie diese Aktionen konfiguriert und genutzt werden, ist der Schlüssel, um die Effizienz und Wirksamkeit der Workflow-Funktionen Ihres ERP-Systems zu maximieren.
