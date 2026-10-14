# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.55.09 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass die Regel zur Verwaltung der zweiten Genehmigungsphase einer Einkaufsrechnung eingerichtet ist, mit einem besonderen Schwerpunkt auf der Validierung des Stückpreises.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente ausgelöst wird, die als Rechnungen identifiziert sind, filtert andere Dokumenttypen heraus und wahrt die Relevanz des Workflows.
2. **And…**
   * **Document Status is Pending Second Approval**: Dies legt fest, dass sich die Rechnung in der Phase befindet, in der sie auf eine zweite Genehmigung wartet. Dies ist in der Regel ein Schritt, der eine zusätzliche Aufsicht vor der endgültigen Verarbeitung sicherstellen soll.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Dies grenzt die Anwendung dieser Regel weiter auf jene Rechnungen ein, die als „Purchase Invoices" klassifiziert sind, und unterscheidet sie von anderen Rechnungs-Subtypen.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Diese logische Prüfung ist entscheidend, da sie den in der Auftragsbestätigung aufgeführten Stückpreis mit dem Stückpreis in der ursprünglichen Bestellung vergleicht. Die Aktion wird ausgelöst, wenn diese Werte nicht übereinstimmen, was auf eine Abweichung hinweisen könnte, die gelöst werden muss.

#### Aktion (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Wenn die festgelegten Bedingungen erfüllt sind (d. h. eine Abweichung bei den Stückpreisen vorliegt), wird die Rechnung automatisch einem Einkäufer (dem im Feld „Buyer Name" angegebenen Namen) zur weiteren Prüfung zugewiesen. Wenn das Feld „Buyer Name" leer oder nicht angegeben ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderer designierter Mitarbeiter) als Fallback zugewiesen, um die Genehmigung zu bearbeiten.

#### Zweck dieser Regel:

* **Genauigkeit und Compliance sicherstellen**: Diese Regel ist entscheidend, um sicherzustellen, dass der Rechnungsprozess korrekt ist und den vereinbarten Bedingungen entspricht. Indem bei einer Abweichung der Stückpreise eine Prüfung ausgelöst wird, hilft das System, finanzielle Fehler oder potenziellen Betrug zu verhindern.
* **Genehmigungen optimieren**: Die Automatisierung der Zuweisung zur Prüfung anhand bestimmter Abweichungen hilft, den Genehmigungsprozess zu optimieren, und stellt sicher, dass Probleme umgehend von den zuständigen Mitarbeitern behoben werden.
* **Finanzielle Aufsicht**: Die Anforderung einer zweiten Genehmigung, insbesondere auf Grundlage des Preisabgleichs, stärkt die finanziellen Kontrollen und die Rechenschaftspflicht innerhalb der Organisation.
