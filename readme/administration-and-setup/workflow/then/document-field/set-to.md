# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, ein angegebenes Feld im Dokument automatisch auf einen vordefinierten Textwert zu setzen, basierend auf den in den Abschnitten **"Where"** und **"And"** definierten Bedingungen. Sie ermöglicht es Benutzern, die Dateneingabe zu optimieren, indem sichergestellt wird, dass Felder mit konsistenten Werten befüllt werden, wenn bestimmte Kriterien erfüllt sind.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung**: Gibt das Feld an, das mit dem Textwert aktualisiert wird.&#x20;
   * **Detail**: Das ausgewählte Feld wird mit dem angegebenen Textwert aktualisiert, wenn die Bedingungen in den Abschnitten **"Where"** und **"And"** erfüllt sind.
2. **Text**
   * **Beschreibung**: Legt den Textwert fest, der im Zielfeld gesetzt wird, wenn die Bedingungen als erfüllt ausgewertet werden.
   * **Detail**: Dies kann eine benutzerdefinierte Nachricht, ein Status oder ein vordefinierter Wert sein, den der Benutzer in das Feld schreiben möchte. Der Text sollte dem erwarteten Eingabeformat des Feldes entsprechen (z. B. alphanumerisch, Datum oder andere Arten textueller Informationen).

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die Bedingungen in den Abschnitten **"Where"** und **"And"** aus:
  * Sind **beide Bedingungen erfüllt**, werden die im **"Then"-Abschnitt** definierten Aktionen ausgeführt. Konkret wird das Zielfeld (Feldname) mit dem angegebenen Text befüllt.
  * Ist **entweder der "Where"- oder der "And"-Abschnitt nicht erfüllt**, wird keine Aktion ausgeführt, und das Feld bleibt unverändert. Die Aktionen des **"Then"-Abschnitts** werden vollständig übersprungen, wenn eine der Bedingungen nicht erfüllt ist.
* **Ausführung der Aktion**: Sind beide Bedingungen in den Abschnitten **"Where"** und **"And"** erfüllt, befüllt das System das angegebene Feld automatisch mit dem gewählten Textwert. Sind die Bedingungen nicht erfüllt, werden keine Änderungen am Feld vorgenommen.

## **Einrichtung und Konfiguration:**

Um diese Karte einzurichten:

1. **Wählen Sie das Feld aus** (Feldname), das mit dem Textwert aktualisiert wird. Die verfügbaren Felder im Dokument werden zur Auswahl aufgelistet.
2. **Geben Sie den Textwert an**, der in das Zielfeld geschrieben wird, wenn die Bedingungen erfüllt sind.
3. Die Aktion wird nur ausgeführt, wenn sowohl die Bedingungen im **"Where"**- als auch im **"And"**-Abschnitt als erfüllt ausgewertet werden.

## **Fazit:**

Die Workflow-Karte **"Set Field to Text"** bietet eine unkomplizierte Möglichkeit, das Befüllen von Textwerten in bestimmte Dokumentfelder auf Basis vordefinierter Bedingungen zu automatisieren. Dies reduziert die manuelle Dateneingabe und sorgt für Konsistenz bei der Dokumentverarbeitung, was sie zu einem nützlichen Werkzeug für die Automatisierung von Workflows und die Steigerung der Effizienz macht.
