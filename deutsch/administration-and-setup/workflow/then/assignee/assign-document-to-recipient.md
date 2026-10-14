# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Assign Document to Disponent / Purchaser"** weist ein Dokument entweder einem **Disponenten** oder einem **Einkäufer** zu. Wird kein gültiger Benutzer gefunden, wird ein Ersatzbenutzer ausgewählt, um sicherzustellen, dass das Dokument immer jemandem zugewiesen ist.

## **Bestandteile der Karte:**

1. **Disponent / Einkäufer**
   * **Beschreibung:** Gibt an, ob das Dokument einem Disponenten oder einem Einkäufer zugewiesen wird.
   * **Optionen:**
     * **Disponent:** Weist das Dokument dem Disponenten zu.
     * **Einkäufer:** Weist das Dokument dem Einkäufer zu.
2. **Ersatzbenutzer**
   * **Beschreibung:** Gibt einen Ersatzbenutzer für den Fall an, dass das Dokument dem ausgewählten Disponenten oder Einkäufer nicht zugewiesen werden kann.
   * **Detail:** Die Dropdown-Liste der verfügbaren Benutzer ermöglicht es Ihnen, einen Ersatzbenutzer auszuwählen, um sicherzustellen, dass das Dokument auch dann zugewiesen wird, wenn der primäre Benutzer nicht bestimmt werden kann.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
* **Dokumentzuweisung:**\
  Die Karte weist das Dokument je nach Auswahl entweder dem **Disponenten** oder dem **Einkäufer** zu. Ist die ausgewählte Person nicht verfügbar oder nicht gültig, wird das Dokument dem Ersatzbenutzer zugewiesen.

## **Einrichtung und Konfiguration:**

* **Disponent / Einkäufer auswählen:**\
  Wählen Sie, ob das Dokument dem **Disponenten** oder dem **Einkäufer** zugewiesen werden soll.
* **Ersatzbenutzer auswählen:**\
  Wählen Sie aus der Dropdown-Liste einen Ersatzbenutzer, der das Dokument erhält, wenn die primäre Zuweisung nicht möglich ist.

## **Fazit:**

Die Workflow-Karte **"Assign Document to Disponent / Purchaser"** stellt sicher, dass das Dokument immer zugewiesen wird – entweder dem ausgewählten Disponenten/Einkäufer oder bei Bedarf dem Ersatzbenutzer. Dies minimiert Workflow-Unterbrechungen und stellt sicher, dass die Dokumentverarbeitung reibungslos fortgesetzt wird.
