# Dem Benutzer nacheinander zuweisen

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-5b15eaee7258-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck**

Die Workflow-Karte "**Dem Benutzer nacheinander zuweisen**" automatisiert die Zuweisung von Dokumenten an einen ausgewählten Benutzer in sequenzieller Weise. Der Prioritätswert bestimmt die Reihenfolge der Zuweisung, wobei niedrigere Zahlen eine höhere Priorität darstellen.

## **Bestandteile der Karte**

1. **Benutzer**
   * **Beschreibung**: Dem ausgewählten Benutzer wird das Dokument gemäß der Workflow-Reihenfolge zugewiesen.
   * **Detailliert**: Ein Dropdown-Menü, das alle verfügbaren Benutzer für die Zuweisung auflistet.
2. **Priorität (Wert)**
   * **Beschreibung**: Ein numerisches Eingabefeld, in dem die Prioritätsstufe für den Benutzer festgelegt werden kann.
   * **Detailliert**: Niedrigere Zahlen bedeuten eine höhere Priorität. Dokumente werden den Benutzern in aufsteigender Reihenfolge der Priorität zugewiesen.

## **Funktionalität**

* **Dokumentzuweisung**:\
  Die Karte weist Dokumente dem ausgewählten Benutzer sequenziell zu und berücksichtigt dabei die Prioritätsstufe.\
  Haben mehrere Benutzer dieselbe Priorität, werden die Dokumente in der Reihenfolge zugewiesen, in der die Benutzer im Dropdown-Menü erscheinen.

## **Einrichtung und Konfiguration**

1. Fügen Sie die Karte **Ordnen Sie das Dokument der Reihe nach zu** zu Ihrem Workflow hinzu.
2. Konfigurieren Sie das Feld **Benutzer**:
   * Wählen Sie einen Benutzer aus dem Dropdown-Menü.
3. Konfigurieren Sie das Feld **Priorität (Wert)**:
   * Geben Sie einen numerischen Wert ein, um die Zuweisungspriorität festzulegen.
4. Speichern und aktivieren Sie den Workflow, um die Konfiguration anzuwenden.

## **Fazit**

Die Workflow-Karte "Assign the Document Sequentially to User" sorgt für eine organisierte Dokumentverteilung, indem sie Dokumente in einer priorisierten Reihenfolge zuweist. Dies verbessert das Aufgabenmanagement und reduziert Verzögerungen bei der Verarbeitung.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Fügen Sie einen Benutzer zu einer priorisierten Dokumentgenehmigungssequenz hinzu.

**Konfiguration:** Wählen Sie `Demo Reviewer A` und Priorität `10`. Fügen Sie eine separate Aufgabe mit der Priorität `20` hinzu, wenn ein späterer Prüfer benötigt wird.

**Erwartetes Ergebnis und Gegenbeispiel:** Die Zuweisungen tragen die konfigurierten Prioritäten; Der niedrigere numerische Wert hat die höhere Priorität. Überprüfen Sie die Reihenfolge der Aufgaben, nicht nur die Reihenfolge der Karten auf der Leinwand.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
