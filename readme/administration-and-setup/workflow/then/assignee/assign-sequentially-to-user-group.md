# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Die Workflow-Karte "**Assign the Document Sequentially to User/Group Based on Decision Table**" weist Dokumente dynamisch entweder einem Benutzer oder einer Gruppe zu, abhängig von der Auswertung der Entscheidungstabelle. Dadurch wird sichergestellt, dass Dokumente auf Basis vordefinierter Regeln angemessen weitergeleitet werden.

## **Bestandteile der Karte**

1. **Priorität (Wert)**
   * **Beschreibung**: Gibt die Prioritätsstufe für Zuweisungen an, wobei niedrigere Zahlen eine höhere Priorität darstellen.
   * **Detail**: Ein numerisches Eingabefeld, in dem der Prioritätswert festgelegt werden kann, um die Reihenfolge der Zuweisung zu steuern.

## **Funktionalität**

* **Auswertung der Entscheidungstabelle**:\
  Die Entscheidungstabelle wertet vordefinierte Bedingungen aus, um zu entscheiden, ob das Dokument einem Benutzer oder einer Gruppe zugewiesen wird.
* **Dokumentzuweisung**:
  * Gibt die Entscheidungstabelle einen Benutzer zurück, wird das Dokument direkt diesem Benutzer zugewiesen.
  * Gibt die Entscheidungstabelle eine Gruppe zurück, wird das Dokument der Gruppe sequenziell zugewiesen, wobei der angegebene Prioritätswert berücksichtigt wird.

## **Einrichtung und Konfiguration**

1. Fügen Sie die Karte **Assign the Document Sequentially** zu Ihrem Workflow hinzu.
2. Konfigurieren Sie das Feld **Priorität (Wert)**:
   * Geben Sie einen numerischen Wert ein, um die Zuweisungspriorität festzulegen.
3. Speichern und aktivieren Sie den Workflow, um die Konfiguration anzuwenden.

## **Fazit**

Die Workflow-Karte "**Assign the Document Sequentially to User/Group Based on Decision Table**" sorgt für eine effiziente und dynamische Weiterleitung von Dokumenten. Durch die Nutzung der Logik der Entscheidungstabelle und der Prioritätswerte ermöglicht die Karte eine präzise Zuweisung an entweder einen Benutzer oder eine Gruppe und optimiert so Dokument-Workflows.
