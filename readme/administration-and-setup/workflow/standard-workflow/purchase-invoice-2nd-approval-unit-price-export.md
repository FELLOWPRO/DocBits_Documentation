# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass die Regel zur Verwaltung der zweiten Genehmigungsphase von Einkaufsrechnungen mit Schwerpunkt auf dem Stückpreis eingerichtet ist und sicherstellt, dass dieser mit den vereinbarten Bedingungen übereinstimmt.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente aktiviert wird, die als Rechnungen identifiziert sind, was für die präzise Steuerung des Workflows entscheidend ist.
2. **And…**
   * **Document Status is Pending Second Approval**: Dies legt fest, dass die Rechnung auf eine zweite Genehmigung wartet. Diese Phase bietet oft eine zusätzliche Aufsicht, um die Richtigkeit sicherzustellen, bevor die Transaktion abgeschlossen wird.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Diese Bedingung legt weiter fest, dass die Regel nur auf Rechnungen angewendet wird, die speziell als „Purchase Invoices" kategorisiert sind, und unterscheidet sie von anderen Rechnungsarten.
   * **Logic Unit Price in order confirmation Equals purchase order**: Diese Bedingung prüft, ob der in der Auftragsbestätigung aufgeführte Stückpreis mit dem Stückpreis in der Bestellung übereinstimmt. Sie stellt sicher, dass die Rechnungsverarbeitung nur dann fortgesetzt wird, wenn Konsistenz bei der Preisgestaltung besteht, was für die Budgetierung und Finanzberichterstattung entscheidend ist.

#### Aktion (Then…):

* **Start Export**: Sobald die Rechnung die festgelegten Bedingungen erfüllt (d. h. die Stückpreise zwischen Auftragsbestätigung und Bestellung übereinstimmen), wird die Aktion „Start Export" ausgelöst. Dies umfasst wahrscheinlich den Export der Rechnungsdaten zur weiteren Verarbeitung, möglicherweise an ein anderes Finanzsystem oder zu Berichtszwecken.

#### Zweck dieser Regel:

* **Genauigkeit und Konsistenz sicherstellen**: Durch die Überprüfung, ob die Stückpreise zwischen Auftragsbestätigung und Bestellung übereinstimmen, hilft das System, die finanzielle Genauigkeit zu wahren und Über- oder Unterberechnungen zu verhindern.
* **Finanzverarbeitung optimieren**: Die Automatisierung des Datenexports nach Bestätigung der Preise reduziert die manuelle Bearbeitung und beschleunigt den Finanzverarbeitungszyklus.
* **Compliance und Aufsicht verbessern**: Die Anforderung einer zweiten Genehmigung zur Preisüberprüfung fügt eine zusätzliche Aufsichtsebene hinzu, die für die Einhaltung von Finanzrichtlinien und -kontrollen entscheidend ist.

Diese Regel ist ein Beispiel dafür, wie Workflow-Automatisierung effektiv genutzt werden kann, um eine präzise und effiziente Bearbeitung von Finanzdokumenten innerhalb einer Organisation sicherzustellen, insbesondere im Kontext großer Transaktionsvolumina, die eine sorgfältige Validierung erfordern.
