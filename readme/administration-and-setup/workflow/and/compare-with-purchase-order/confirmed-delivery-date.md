# Bestätigter Liefertermin

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Diese Workflow-Karte ist darauf ausgelegt zu überprüfen, ob die bestätigten Lieferdaten auf Rechnungen oder Versanddokumenten mit den akzeptierten Lieferdaten übereinstimmen, die in einer Stammdaten-Nachschlagetabelle definiert sind. Durch den Vergleich dieser Daten hilft sie, die Einhaltung vereinbarter Lieferpläne sicherzustellen, und erhöht die Zuverlässigkeit der Lieferkette.

## **Bestandteile der Karte**

1. **Betreiber**
   * **Beschreibung:** Legt die Bedingung für den Vergleich des bestätigten Lieferdatums mit dem akzeptierten Lieferdatum fest.
   * **Optionen:**
     * **Is:** Bestätigt, dass das Lieferdatum mit dem akzeptierten Lieferdatum in den Stammdaten übereinstimmt.
     * **Ist nicht:** Stellt sicher, dass das Lieferdatum nicht mit dem akzeptierten Lieferdatum in den Stammdaten übereinstimmt.
2. **Stammdaten-Tabellen-Lookup**
   * **Beschreibung:** Gibt die Referenztabelle an, die die akzeptierten Lieferdaten für den Vergleich enthält.
   * **Detail:** Die Tabelle wird durch den Parameter **Stammdatentabelle** definiert und kann zusätzliche Metadaten wie Bestellnummern oder Lieferregionen enthalten.

## **Funktionalität**

* **Datumsvergleich:** Das System vergleicht das bestätigte Lieferdatum aus der Rechnung oder dem Versanddokument mit dem akzeptierten Lieferdatum in der angegebenen Stammdaten-Nachschlagetabelle.
* **Ausführung der Aktion:** Basierend auf dem Vergleichsergebnis kann die Karte Folgeaktionen wie Benachrichtigungen auslösen.

## **Einrichtung und Konfiguration**

* Um diese Karte zu konfigurieren, wählen Benutzer das Feld aus, das das bestätigte Lieferdatum im Dokument darstellt, und geben die Stammdaten-Nachschlagetabelle an, die die akzeptierten Lieferdaten enthält. Anschließend wird ein Operator gewählt, um festzulegen, wie die beiden Daten verglichen werden sollen (z. B. **Is** oder **Ist nicht**).

## **Beispiel-Szenario**

* Eine Rechnung weist ein bestätigtes Lieferdatum vom 10. Juni aus, während die Stammdaten-Nachschlagetabelle ein akzeptiertes Lieferdatum vom 15. Juni angibt. Mit dem Operator **Ist nicht** markiert die Karte die Abweichung zur Prüfung und ermöglicht es dem Logistikteam, die Ursache zu untersuchen und die Pläne entsprechend anzupassen.

## **Fazit**

Die Workflow-Karte **„Bestätigter Liefertermin vs. akzeptierter Liefertermin“** hilft Organisationen, die Einhaltung vereinbarter Lieferpläne aufrechtzuerhalten, indem sie den Vergleich bestätigter und akzeptierter Lieferdaten automatisiert. Dieser proaktive Ansatz im Liefermanagement steigert die betriebliche Effizienz, reduziert Verzögerungen und fördert eine bessere Zusammenarbeit über die gesamte Lieferkette hinweg.
