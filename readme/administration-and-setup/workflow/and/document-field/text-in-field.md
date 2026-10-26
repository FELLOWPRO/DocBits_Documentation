# Text im Feld

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61d692604341-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, Aktionen auf Basis des Vorhandenseins oder Fehlens eines bestimmten Textes innerhalb eines angegebenen Dokumentfelds zu automatisieren. Sie sorgt dafür, dass sich Workflows dynamisch an den Inhalt von Dokumenten anpassen können, und unterstützt so eine effiziente Verarbeitung und eine präzise Entscheidungsfindung.

## **Bestandteile der Karte:**

1. **Text**
   * **Beschreibung:** Gibt die Textzeichenfolge an, die innerhalb des Feldes geprüft wird.
   * **Detail:** Dies kann ein Wort, eine Phrase oder eine Zeichenfolge sein, die für den Workflow relevant ist.
2. **Operator**
   * **Beschreibung:** Legt die Bedingung für das Vorhandensein des Textes im Feld fest.
   * **Optionen:**
     * **Is:** Löst den Workflow aus, wenn der angegebene Text im Feld vorhanden ist.
     * **Ist nicht:** Löst den Workflow aus, wenn der angegebene Text im Feld nicht vorhanden ist.
3. **Feldname**
   * **Beschreibung:** Gibt den Namen des auszuwertenden Dokumentfelds an.
   * **Detail:** Dieser muss exakt mit dem Bezeichner des Feldes innerhalb des Dokuments übereinstimmen.

## **Funktionalität:**

1. **Bedingungsauswertung:** Das System prüft auf Basis des ausgewählten Operators (Is oder Is Not), ob der angegebene Text im Feld vorhanden ist.
2. **Ausführung der Aktion:**
   * **Bedingung erfüllt (True):**\
     Stimmt das Vorhandensein des Textes im Feld mit der angegebenen Bedingung überein, leitet das System die zugehörigen Aktionen ein. Dazu können das Auslösen von Warnungen, das Fortführen von Workflows oder das Aktualisieren von Datensätzen gehören.
   * **Bedingung nicht erfüllt (False):**\
     Stimmt das Vorhandensein des Textes im Feld nicht mit der Bedingung überein, werden je nach Workflow-Konfiguration alternative oder keine Aktionen ausgeführt.

## **Einrichtung und Konfiguration:**

* Der Benutzer gibt den zu prüfenden Text ein. Anschließend wählt er den Feldnamen des relevanten Dokuments aus.

## **Fazit:**

Die Workflow-Karte "Text Presence in Field" ist ein einfaches, aber leistungsstarkes Werkzeug für die Analyse von Dokumentinhalten. Indem sie Aktionen auf Basis der Texterkennung automatisiert, unterstützt diese Karte intelligentere Workflows, verbessert die Genauigkeit der Dokumentbearbeitung und reduziert den manuellen Aufwand.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Suchen Sie nach Dokumenten, die eine Überprüfungsmarkierung tragen.

**Konfiguration:** Wählen Sie das Textfeld `review_note` aus, das Operator und Text `manual review` enthält.

**Erwartetes Ergebnis und Gegenbeispiel:** `Please start manual review` besteht. `Ready for export` enthält den ausgewählten Text nicht und schlägt fehl.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
