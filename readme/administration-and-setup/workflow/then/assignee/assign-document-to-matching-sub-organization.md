# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Assign Document to Matching Sub-Organization Based on Field"** weist ein Dokument dynamisch einer Unterorganisation zu, basierend auf einem angegebenen Feld im Dokument. Wird keine passende Unterorganisation gefunden, verwendet die Karte eine vordefinierte Ersatz-Unterorganisation.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt das Dokumentfeld an, das zur Bestimmung der passenden Unterorganisation verwendet wird.
   * **Detail:** Die Karte sucht nach einem Wert im angegebenen Feld, um ihn mit einer verfügbaren Unterorganisation abzugleichen.
2. **Unterorganisation (Ersatz)**
   * **Beschreibung:** Legt die Ersatz-Unterorganisation fest, die verwendet wird, wenn im angegebenen Feld keine Übereinstimmung gefunden wird.
   * **Detail:** Stimmt der Feldwert mit keiner Unterorganisation überein, wird das Dokument der ausgewählten Ersatz-Unterorganisation zugewiesen.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Dynamische Zuweisung:**\
  Die Karte prüft den Wert des angegebenen Feldes und weist das Dokument der Unterorganisation zu, die diesem Wert entspricht.
* **Ersatzmechanismus:**\
  Wird keine passende Unterorganisation gefunden, wird das Dokument der Ersatz-Unterorganisation zugewiesen.

## **Einrichtung und Konfiguration:**

* **Feldnamen auswählen:**\
  Wählen Sie das Feld aus dem Dokument, das den Wert enthält, der mit einer Unterorganisation abgeglichen werden soll.
* **Ersatz-Unterorganisation auswählen:**\
  Wählen Sie die Unterorganisation, die verwendet wird, wenn im Dokumentfeld keine Übereinstimmung gefunden wird.

## **Fazit:**

Die Workflow-Karte **"Assign Document to Matching Sub-Organization Based on Field"** bietet Flexibilität, indem sie Dokumente dynamisch an die passende Unterorganisation weiterleitet, mit einer zusätzlichen Ersatzoption, um sicherzustellen, dass kein Dokument unzugewiesen bleibt.
