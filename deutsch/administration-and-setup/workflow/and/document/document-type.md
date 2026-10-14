# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob ein Dokument einem bestimmten Typ entspricht. Indem geprüft wird, ob das Dokument dem angegebenen Typ entspricht, können Workflows fortgesetzt werden oder alternative Aktionen auf Basis dieser Bedingung ausführen. Dies hilft, Prozesse zu automatisieren, bei denen der Dokumenttyp die nächsten Schritte im Workflow bestimmt.

## Bestandteile der Karte:

1. **Operator**
   * **Beschreibung**: Legt fest, ob das Dokument vom angegebenen Typ sein soll oder nicht.
   * **Optionen**:
     * **Is**: Das Dokument muss dem angegebenen Typ entsprechen, damit die Bedingung erfüllt ist.
     * **Is Not**: Das Dokument darf nicht dem angegebenen Typ entsprechen, damit die Bedingung erfüllt ist.
2. **Typ**
   * **Beschreibung**: Gibt den Dokumenttyp an, mit dem verglichen wird.
   * **Detail**: Diese umfasst verschiedene Dokumenttypen wie "Invoice", "Purchase Order" usw., auf deren Grundlage die Bedingung (is/is not) ausgewertet wird.

## Funktionalität:

* **Bedingungsauswertung**: Das System wertet aus, ob der Dokumenttyp im angegebenen Feld die durch den Operator definierte Bedingung erfüllt. Es vergleicht den Feldwert mit dem angegebenen Dokumenttyp.
* **Ausführung der Aktion**:
  * **Bedingung erfüllt (True)**: Stimmt der Dokumenttyp mit dem angegebenen Typ überein (oder nicht, je nach Operator), fährt der Workflow mit der True-Bedingung fort. Dies kann Aktionen auslösen, etwa die weitere Verarbeitung des Dokuments, das Senden zur Freigabe oder das Anwenden bestimmter Regeln auf Basis des Dokumenttyps.
  * **Bedingung nicht erfüllt (False)**: Stimmt der Dokumenttyp nicht mit dem angegebenen Typ überein, fährt der Workflow mit der False-Bedingung fort. Dies kann alternative Aktionen auslösen, etwa das Weiterleiten des Dokuments an einen anderen Prozess oder das Stoppen weiterer Aktionen.

## Einrichtung und Konfiguration:

* Benutzer konfigurieren die Karte, indem sie das Dokumentfeld, das den Dokumenttyp enthält, aus einer Liste verfügbarer Felder auswählen. Anschließend wird der Operator ausgewählt, um festzulegen, ob das Dokument dem angegebenen Typ entsprechen muss oder nicht. Zuletzt legen die Benutzer die Fortsetzungsbedingung (True oder False) fest, die die nächste Aktion auf Basis des Dokumenttyps bestimmt.

## Fazit:

Die Workflow-Karte "Document Type Comparison" ist unverzichtbar, um sicherzustellen, dass Workflows auf Basis des Typs des verarbeiteten Dokuments ablaufen. Durch den Vergleich des Dokumenttyps hilft sie Organisationen, die Weiterleitung und Verarbeitung von Dokumenten zu automatisieren, und stellt sicher, dass Dokumente entsprechend ihrem Typ angemessen behandelt werden.
