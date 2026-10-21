# Feldwert setzen

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-12fec1de4cae-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, ein angegebenes Feld im Dokument automatisch auf einen vordefinierten Textwert zu setzen, basierend auf den in den Abschnitten **„Wenn“** und **„Und“** definierten Bedingungen. Sie ermöglicht es Benutzern, die Dateneingabe zu optimieren, indem sichergestellt wird, dass Felder mit konsistenten Werten befüllt werden, wenn bestimmte Kriterien erfüllt sind.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung**: Gibt das Feld an, das mit dem Textwert aktualisiert wird.
   * **Detailliert**: Das ausgewählte Feld wird mit dem angegebenen Textwert aktualisiert, wenn die Bedingungen in den Abschnitten **„Wenn“** und **„Und“** erfüllt sind.
2. **Text**
   * **Beschreibung**: Legt den Textwert fest, der im Zielfeld gesetzt wird, wenn die Bedingungen als erfüllt ausgewertet werden.
   * **Detailliert**: Dies kann eine benutzerdefinierte Nachricht, ein Status oder ein vordefinierter Wert sein, den der Benutzer in das Feld schreiben möchte. Der Text sollte dem erwarteten Eingabeformat des Feldes entsprechen (z. B. alphanumerisch, Datum oder andere Arten textueller Informationen).

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die Bedingungen in den Abschnitten **„Wenn“** und **„Und“** aus:
  * Sind **beide Bedingungen erfüllt**, werden die im **"Then"-Abschnitt** definierten Aktionen ausgeführt. Konkret wird das Zielfeld (Feldname) mit dem angegebenen Text befüllt.
  * Ist **entweder der "Where"- oder der "And"-Abschnitt nicht erfüllt**, wird keine Aktion ausgeführt, und das Feld bleibt unverändert. Die Aktionen des **"Then"-Abschnitts** werden vollständig übersprungen, wenn eine der Bedingungen nicht erfüllt ist.
* **Ausführung der Aktion**: Sind beide Bedingungen in den Abschnitten **„Wenn“** und **„Und“** erfüllt, befüllt das System das angegebene Feld automatisch mit dem gewählten Textwert. Sind die Bedingungen nicht erfüllt, werden keine Änderungen am Feld vorgenommen.

## **Einrichtung und Konfiguration:**

Um diese Karte einzurichten:

1. **Wählen Sie das Feld aus** (Feldname), das mit dem Textwert aktualisiert wird. Die verfügbaren Felder im Dokument werden zur Auswahl aufgelistet.
2. **Geben Sie den Textwert an**, der in das Zielfeld geschrieben wird, wenn die Bedingungen erfüllt sind.
3. Die Aktion wird nur ausgeführt, wenn sowohl die Bedingungen im **„Wenn“**- als auch im **„Und“**-Abschnitt als erfüllt ausgewertet werden.

## **Fazit:**

Die Workflow-Karte **„Feld auf Text setzen“** bietet eine unkomplizierte Möglichkeit, das Befüllen von Textwerten in bestimmte Dokumentfelder auf Basis vordefinierter Bedingungen zu automatisieren. Dies reduziert die manuelle Dateneingabe und sorgt für Konsistenz bei der Dokumentverarbeitung, was sie zu einem nützlichen Werkzeug für die Automatisierung von Workflows und die Steigerung der Effizienz macht.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Schreiben Sie ein Routing-Ergebnis in ein Dokumentfeld.

**Konfiguration:** Wählen Sie das Textfeld `routing_result` und stellen Sie den Text auf `manual review` ein.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Feld enthält genau `manual review`. Eine nachfolgende Gleichheitsbedingung kann diesen Wert verwenden; Es handelt sich eher um ein Dokumentfeld als um eine Organisationsvariable.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
