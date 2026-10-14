# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt auszuwerten, ob ein angegebenes Land, das sich in einem festgelegten Feld befindet, Teil eines bestimmten Handels- oder politischen Raums ist (Europäische Union, Schengen-Raum oder NAFTA). Basierend auf dieser Auswertung kann der Workflow mit einer True- oder False-Bedingung fortgesetzt werden und so weitere Aktionen innerhalb des Systems ermöglichen. Sie ist besonders nützlich, um regionsspezifische Geschäftsregeln zu automatisieren, Compliance sicherzustellen oder bestimmte Workflows auf Basis geografischer Zugehörigkeiten auszulösen.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt das Dokumentfeld an, in dem der Ländername oder -code gespeichert ist.
   * **Detail:** Dieser sollte exakt mit dem Feldbezeichner der Länderdaten innerhalb des Dokuments übereinstimmen.&#x20;
2. **Operator**
   * **Beschreibung:** Gibt an, ob das Land im ausgewählten Feld mit der ausgewählten Region oder dem Abkommen übereinstimmen soll oder nicht.
   * **Optionen:**
     * **Is:** Das Land muss Teil des ausgewählten Abkommens (EU, Schengen oder NAFTA) sein, damit die Bedingung erfüllt ist.
     * **Is Not:** Das Land darf nicht Teil des ausgewählten Abkommens sein, damit die Bedingung erfüllt ist.
3. **Ländervergleich**
   * **Beschreibung:** Legt fest, ob das Land im Feld anhand eines bestimmten politischen oder Handelsabkommens geprüft wird.
   * **Optionen:**
     * **Europäische Union:** Die Karte prüft, ob das Land Mitglied der Europäischen Union ist.
     * **Schengen-Raum:** Die Karte prüft, ob das Land Teil des Schengen-Raums ist.
     * **NAFTA:** Die Karte prüft, ob das Land Mitglied des NAFTA-Abkommens ist.
4. **Boolean**
   * **Beschreibung:** Legt das Ergebnis des Vergleichs fest. Erfüllt das Land die Bedingung, wird der Workflow mit dem angegebenen Boolean-Wert fortgesetzt.
   * **Optionen:**
     * **True:** Der Workflow wird fortgesetzt, wenn die Bedingung übereinstimmt.
     * **False:** Der Workflow wird fortgesetzt, wenn die Bedingung nicht übereinstimmt.

## **Funktionalität:**

* **Bedingungsauswertung:**
  * Das System wertet aus, ob das im Feld angegebene Land Teil der gewählten Region oder des Abkommens (EU, Schengen-Raum oder NAFTA) ist, basierend auf dem ausgewählten Operator. Diese Auswertung prüft den Ländernamen oder -code anhand einer vordefinierten Liste von Ländern, die zur jeweiligen Gruppe gehören.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):** Stimmt das Land im Feld mit der ausgewählten Region überein (gemäß dem Operator), wird der Workflow mit der angegebenen True-Bedingung fortgesetzt. Dies kann weitere Aktionen auslösen, etwa das Weiterleiten von Dokumenten, das Anwenden besonderer Verarbeitungsregeln oder das Aktivieren regionsspezifischer Funktionen.
  * **Bedingung nicht erfüllt (False):** Stimmt das Land nicht mit der ausgewählten Region überein (gemäß dem Operator), wird der Workflow mit der angegebenen False-Bedingung fortgesetzt und ermöglicht so je nach Systemeinrichtung die Ausführung alternativer Aktionen oder das Beenden des Workflows.

## **Einrichtung und Konfiguration:**&#x20;

* Benutzer konfigurieren die Karte, indem sie das Dokumentfeld auswählen, das das Land enthält, und die Region (Europäische Union, Schengen-Raum oder NAFTA) angeben. Anschließend wird der Operator aus einer Dropdown-Liste gewählt, um festzulegen, ob das Land Teil der ausgewählten Region sein muss oder nicht. Zuletzt legen die Benutzer die Fortsetzungsbedingung (True oder False) fest, die den nächsten Schritt im Workflow bestimmt.

## **Fazit:**

Die Workflow-Karte "Country in Field Comparison" ist ein unverzichtbares Werkzeug, um Prozesse zu automatisieren, die von geografischen Regeln abhängen, etwa die Einhaltung von Handelsabkommen oder politische Zugehörigkeiten. Indem sie Länderdaten mit bestimmten Regionen wie der Europäischen Union, dem Schengen-Raum oder NAFTA vergleicht, stellt diese Karte sicher, dass das System die richtige Verarbeitungslogik anwendet, und verbessert so die Effizienz und gewährleistet eine präzise Workflow-Ausführung auf Basis geografischer Bedingungen.
