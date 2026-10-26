# Der Beschaffungsgruppe sequenziell zuweisen

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-3b31b4f42710-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck**

Die Workflow-Karte "**Ordnen Sie das Dokument der Reihe nach der Beschaffungsgruppe zu**" ermöglicht die sequenzielle Zuweisung von Dokumenten an eine angegebene Beschaffungsgruppe. Der Prioritätswert bestimmt die Reihenfolge der Zuweisung, wobei niedrigere Zahlen eine höhere Priorität darstellen.

## **Bestandteile der Karte**

1. **Gruppe**
   * **Beschreibung**: Ein Texteingabefeld, in dem der Name der Beschaffungsgruppe eingegeben werden kann.
   * **Detailliert**: Gibt die Beschaffungsgruppe an, der das Dokument zugewiesen wird.
2. **Priorität (Wert)**
   * **Beschreibung**: Ein numerisches Eingabefeld, in dem die Prioritätsstufe für die Gruppe festgelegt werden kann.
   * **Detailliert**: Niedrigere Zahlen bedeuten eine höhere Priorität und stellen sicher, dass Dokumente den Gruppen in aufsteigender Reihenfolge der Priorität zugewiesen werden.

## **Funktionalität**

* **Dokumentzuweisung**:\
  Die Karte weist Dokumente sequenziell der angegebenen Beschaffungsgruppe zu.\
  Die Prioritätswerte bestimmen die Zuweisungsreihenfolge, wobei niedrigere Zahlen zuerst verarbeitet werden.

## **Einrichtung und Konfiguration**

1. Fügen Sie die Karte **Ordnen Sie das Dokument der Reihe nach zu** zu Ihrem Workflow hinzu.
2. Konfigurieren Sie das Feld **Gruppe**:
   * Geben Sie den Namen der Beschaffungsgruppe in das Textfeld ein.
3. Konfigurieren Sie das Feld **Priorität (Wert)**:
   * Geben Sie einen numerischen Wert ein, um die Zuweisungspriorität festzulegen.
4. Speichern und aktivieren Sie den Workflow, um die Konfiguration anzuwenden.

## **Fazit**

Die Workflow-Karte "Assign the Document Sequentially to the Procurement Group" sorgt für eine effektive Dokumentzuweisung an Beschaffungsgruppen auf Basis der Priorität. Dies steigert die organisatorische Effizienz und das Aufgabenmanagement.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Priorisieren Sie eine Beschaffungsgruppe innerhalb der Dokumentenprüfung.

**Konfiguration:** Wählen Sie `Demo Procurement` und Priorität `10`.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Dokument erhält die Beschaffungsgruppenzuordnung mit der Priorität `10`. Überprüfen Sie, ob spätere Zuweisungen die vorgesehenen höheren numerischen Prioritäten verwenden.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
