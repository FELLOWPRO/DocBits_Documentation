# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass die Regel zur Verwaltung der zweiten Genehmigungsphase für Einkaufsrechnungen mit Schwerpunkt auf den Mengendetails eingerichtet ist und sicherstellt, dass die Mengen auf der Rechnung mit denen auf der ursprünglichen Bestellung übereinstimmen.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente aktiviert wird, die als Rechnungen identifiziert sind, was für die präzise Steuerung des Workflows entscheidend ist.
2. **And…**
   * **Document Status is Pending Second Approval**: Dies legt fest, dass die Rechnung derzeit auf eine zweite Genehmigung wartet. Diese Phase bietet oft eine zusätzliche Aufsicht, um die Richtigkeit sicherzustellen, bevor die Transaktion abgeschlossen wird.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Diese Bedingung legt weiter fest, dass die Regel nur auf Rechnungen angewendet wird, die speziell als „Purchase Invoices" kategorisiert sind, und unterscheidet sie von anderen Rechnungsarten.
   * **Logic Quantity in order confirmation Equals purchase order**: Diese Bedingung prüft, ob die in der Auftragsbestätigung aufgeführte Menge mit der Menge in der Bestellung übereinstimmt. Sie stellt sicher, dass die Rechnungsverarbeitung nur dann fortgesetzt wird, wenn die Mengen konsistent sind, was für die Bestandsverwaltung und finanzielle Genauigkeit entscheidend ist.

#### Aktion (Then…):

* **Start Export**: Sobald die Rechnung die festgelegten Bedingungen erfüllt (d. h. die Mengen zwischen Auftragsbestätigung und Bestellung übereinstimmen), wird die Aktion „Start Export" ausgelöst. Dies umfasst wahrscheinlich den Export der Rechnungsdaten zur weiteren Verarbeitung, möglicherweise an ein anderes Finanzsystem oder zu Berichtszwecken.

#### Zweck dieser Regel:

* **Genauigkeit und Konsistenz sicherstellen**: Durch die Überprüfung, ob die Mengen zwischen Auftragsbestätigung und Bestellung übereinstimmen, hilft das System, die Bestandsgenauigkeit zu wahren und Abweichungen zu verhindern, die sich auf die Finanzberichterstattung oder die Bestandsverwaltung auswirken könnten.
* **Finanzverarbeitung optimieren**: Die Automatisierung des Datenexports nach Bestätigung der Mengen reduziert die manuelle Bearbeitung und beschleunigt den Finanzverarbeitungszyklus.
* **Compliance und Aufsicht verbessern**: Die Anforderung einer zweiten Genehmigung zur Mengenüberprüfung fügt eine zusätzliche Aufsichtsebene hinzu, die für die Einhaltung von Finanzrichtlinien und -kontrollen entscheidend ist.

Diese Regel ist ein klares Beispiel dafür, wie Workflow-Automatisierung effektiv eingesetzt werden kann, um eine präzise und effiziente Bearbeitung von Finanzdokumenten innerhalb einer Organisation sicherzustellen, insbesondere im Kontext von Einkaufsprozessen mit großen Transaktionsvolumina, die eine sorgfältige Validierung erfordern.
