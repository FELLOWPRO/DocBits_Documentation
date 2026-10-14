# Assign to group

<figure><img src="../../../../.gitbook/assets/image (304).png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Die Workflow-Karte **"Assign to Group"** ermöglicht die Zuweisung von Dokumenten an eine bestimmte **Gruppe** innerhalb des Systems. Dadurch wird sichergestellt, dass das Dokument vom passenden Team verarbeitet wird, und der Workflow wird optimiert. In späteren Versionen erweitert, führt sie eine Entscheidungsbaum-Funktionalität für die dynamische Gruppenzuweisung ein.

## Bestandteile der Karte:

1. **Gruppen**
   * **Beschreibung:** Gibt die **Gruppe** an, der das Dokument zugewiesen wird.
   * **Detail:** Wird aus einer Dropdown-Liste der verfügbaren **Gruppen** ausgewählt.



## **Zusätzliche Komponenten in Version 3**

1. **Entscheidungsbaum (nur Version 3)**
   * **Beschreibung:** Ermöglicht die Verwendung eines Entscheidungsbaums, um die **Gruppe** dynamisch zu bestimmen, der das Dokument zugewiesen werden soll.
   * **Optionen:**
     * **True:** Aktiviert die Verarbeitung über den Entscheidungsbaum.
     * **False:** Deaktiviert die Verarbeitung über den Entscheidungsbaum.

## Funktionalität:

* **Bedingungsauswertung:** Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Dokumentzuweisung:** Weist das Dokument der ausgewählten **Gruppe** zu. In **Version 3** bestimmt der **Entscheidungsbaum** die Zielgruppe dynamisch, sofern aktiviert.

## Einrichtung und Konfiguration:

* **Gruppe auswählen:** Wählen Sie die **Gruppe** aus der Dropdown-Liste, um das Dokument zuzuweisen.
* **Entscheidungsbaum verwenden (nur Version 3):** Aktivieren Sie diese Option, wenn der **Entscheidungsbaum** für die dynamische Zuweisung verwendet werden soll.

## Fazit:

Die Workflow-Karte **"Assign to Group"** automatisiert die Dokumentzuweisung an vordefinierte **Gruppen** und verbessert so die Teamkoordination. **Version 3** führt die Möglichkeit ein, Gruppen dynamisch auf Basis der Logik eines Entscheidungsbaums zuzuweisen.
