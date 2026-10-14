# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob ein angegebenes Land, das sich in einem festgelegten Feld befindet, Teil einer vordefinierten Länderliste ist. Basierend auf dieser Auswertung kann der Workflow mit einer True- oder False-Bedingung fortgesetzt werden. Sie hilft, Prozesse zu automatisieren, bei denen Aktionen davon abhängen, ob das Land in einer Reihe zulässiger oder eingeschränkter Länder enthalten ist.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt das Dokumentfeld an, in dem der Ländername oder -code gespeichert ist.
   * **Detail:** Dieser sollte exakt mit dem Feldbezeichner der Länderdaten innerhalb des Dokuments übereinstimmen.&#x20;
2. **Operator**
   * **Beschreibung:** Legt fest, ob das Land im Feld Teil einer vordefinierten Länderliste sein muss.
   * **Optionen:**
     * **Is:** Das Land muss in der Liste der angegebenen Länder enthalten sein, damit die Bedingung erfüllt ist.
     * **Is Not:** Das Land darf nicht in der Liste der angegebenen Länder enthalten sein, damit die Bedingung erfüllt ist.
3. **Länder**
   * **Beschreibung:** Gibt die Liste der Länder an, mit denen das ausgewählte Land verglichen wird.
   * **Detail:** Dies ist eine durch Kommas getrennte Länderliste. Der Vergleich prüft, ob das Land im Feld in dieser Liste enthalten ist.
4. **Fortsetzungsbedingung**
   * **Beschreibung:** Legt das Ergebnis des Vergleichs fest. Erfüllt das Land die Bedingung, wird der Workflow mit dem angegebenen Boolean-Wert fortgesetzt.
   * **Optionen:**
     * **True:** Der Workflow wird fortgesetzt, wenn die Bedingung übereinstimmt.
     * **False:** Der Workflow wird fortgesetzt, wenn die Bedingung nicht übereinstimmt.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System wertet aus, ob das im Feld angegebene Land Teil der Liste vordefinierter Länder ist. Diese Auswertung prüft den Ländernamen oder -code anhand der bereitgestellten Liste.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):**\
    Ist das Land im Feld Teil der angegebenen Länderliste, wird der Workflow mit der True-Bedingung fortgesetzt. Dies kann weitere Aktionen auslösen, etwa das Weiterleiten von Dokumenten an die zuständige Abteilung, das Anwenden bestimmter Verarbeitungsregeln oder das Aktivieren regionsspezifischer Funktionen.
  * **Bedingung nicht erfüllt (False):**\
    Stimmt das Land nicht mit der Liste überein, wird der Workflow mit der False-Bedingung fortgesetzt. Dies ermöglicht es, je nach Systemeinrichtung alternative Aktionen auszuführen oder den Workflow anzuhalten.

## **Einrichtung und Konfiguration:**

* Benutzer konfigurieren die Karte, indem sie das Dokumentfeld auswählen, das das Land enthält, und die Liste der zu prüfenden Länder angeben. Anschließend wird der Operator aus einer Dropdown-Liste gewählt, um festzulegen, ob das Land Teil der angegebenen Länderliste sein muss oder nicht. Zuletzt legen die Benutzer die Fortsetzungsbedingung (True oder False) fest, die den nächsten Schritt im Workflow bestimmt.

## **Fazit:**

Die Workflow-Karte "Country in Field Comparison with List" ist ein wertvolles Werkzeug, um Aktionen darauf basieren zu lassen, ob ein Land Teil einer vordefinierten Gruppe ist. Indem sie die Länderdaten mit einer Liste zulässiger oder eingeschränkter Länder vergleicht, steigert diese Karte die Workflow-Effizienz und stellt sicher, dass Systemprozesse den korrekten geografischen Regeln folgen.
