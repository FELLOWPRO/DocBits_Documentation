# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, Aktionen auf Basis des Vorhandenseins oder Zustands eines angegebenen Feldes innerhalb eines Dokuments zu automatisieren. Indem sie auswertet, ob das Feld leer ist, fehlt oder befüllt ist, ermöglicht sie es Workflows, Dokumente präzise und genau zu verarbeiten.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt den Namen des auszuwertenden Feldes an.
   * **Detail:** Dieser muss exakt mit dem im Dokument verwendeten Bezeichner übereinstimmen, um eine genaue Felderkennung sicherzustellen.
2. **Operatoren**
   * **Beschreibung**: Legt die Bedingung fest, die den Workflow auslöst, basierend auf dem Vorhandensein oder Zustand des Feldes.
   * **Optionen**:
     * **Empty/Not in Document:** Der Workflow wird ausgelöst, wenn das Feld entweder im Dokument fehlt oder vorhanden, aber leer ist.
     * **In Document/Not Empty:** Der Workflow wird ausgelöst, wenn das Feld im Dokument existiert und einen Wert enthält.

## **Funktionalität:**

* **Zustandserkennung:** Die Karte überwacht das angegebene Feld, um sein Vorhandensein und seinen Zustand auszuwerten.
* **Bedingungsauswertung:**
  * Das System wertet aus, ob sich das angegebene Feld in dem durch den ausgewählten Operator definierten Zustand (Empty/Not in Document oder In Document/Not Empty) befindet.
*

    **Ausführung der Aktion:**

    * **Bedingung Empty/Not in Document:** Stimmt der Zustand des Feldes mit dieser Bedingung überein (d. h. das Feld fehlt im Dokument oder ist vorhanden, aber leer), leitet das System die zugehörigen Aktionen ein. Dazu können das Erzeugen von Warnungen, das Markieren des Dokuments zur Prüfung oder das Anhalten des Workflows gehören.
    * **Bedingung In Document/Not Empty:** Stimmt der Zustand des Feldes mit dieser Bedingung überein (d. h. das Feld existiert im Dokument und enthält einen Wert), löst das System die zugehörigen Aktionen aus. Dazu können das Aktivieren nachfolgender Workflow-Schritte, das Aktualisieren von Datensätzen oder das Auslösen von Benachrichtigungen gehören.

## **Einrichtung und Konfiguration:**&#x20;

* Benutzer wählen das Feld aus einer Liste verfügbarer Dokumentfelder aus. Der Operator wird über ein Dropdown-Menü gewählt, das klare Optionen für "Empty/Not in Document" oder "In Document/Not Empty" bietet.

## **Fazit:**

Die Workflow-Karte "Field Presence and State Validation" ist ein wichtiges Werkzeug für Dokumentverarbeitungs-Workflows und stellt eine genaue Behandlung fehlender oder befüllter Felder sicher. Indem sie Aktionen auf Basis von Feldzuständen automatisiert, stärkt diese Karte die Datenintegrität, reduziert Fehler und sorgt dafür, dass Workflows reibungslos und effizient ablaufen.
