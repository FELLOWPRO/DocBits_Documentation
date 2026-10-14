# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass sich die Regel speziell auf die Behandlung von Einkaufsrechnungen während einer zweiten Genehmigungsphase bezieht, mit dem Schwerpunkt auf der Überprüfung der Richtigkeit der aufgeführten Mengen.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente aktiviert wird, die als Rechnungen klassifiziert sind. Dies ist wesentlich, um Spezifität und Relevanz im Workflow zu wahren.
2. **And…**
   * **Document Status is Pending Second Approval**: Dies legt fest, dass die Rechnung derzeit auf eine zweite Genehmigung wartet. Diese Phase ist in der Regel dazu gedacht, eine zusätzliche Aufsicht zu bieten, bevor die Rechnung abgeschlossen wird.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Diese Bedingung verfeinert die Regel weiter, sodass sie ausschließlich auf Rechnungen angewendet wird, die als „Purchase Invoices" identifiziert sind. Diese Kategorisierung hilft, sie von anderen Rechnungsarten zu unterscheiden.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Diese entscheidende Bedingung prüft, ob die in der Auftragsbestätigung angegebene Menge mit der Menge auf der ursprünglichen Bestellung übereinstimmt. Die Aktion wird ausgelöst, wenn eine Abweichung vorliegt, die auf einen möglichen Fehler oder ein Problem hinweist, das gelöst werden muss.

#### Aktion (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Wenn die Bedingungen der Regel erfüllt sind (d. h. eine Abweichung bei den Mengen vorliegt), wird die Rechnung automatisch der im Feld „Buyer Name" aufgeführten Person zur weiteren Prüfung zugewiesen. Wenn dieses Feld leer oder die angegebene Person nicht verfügbar ist, übernimmt ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderer designierter Mitarbeiter), um eine zeitnahe Prüfung und Lösung sicherzustellen.

#### Zweck dieser Regel:

* **Genauigkeit und Compliance**: Die Regel ist entscheidend, um sicherzustellen, dass der Rechnungsprozess korrekt ist und mit den in der Bestellung vereinbarten Bedingungen übereinstimmt. Sie hilft, finanzielle Abweichungen und potenzielle Bestandsfehler zu verhindern.
* **Optimierte Genehmigungen**: Die Automatisierung des Prüfprozesses für bestimmte Abweichungen hilft, Genehmigungen zu optimieren, und stellt sicher, dass etwaige Probleme schnell von den zuständigen Mitarbeitern behoben werden.
* **Verbesserte finanzielle Aufsicht**: Die Anforderung einer zweiten Genehmigung für Mengenüberprüfungen stärkt die finanziellen Kontrollen und die Rechenschaftspflicht innerhalb der Organisation.

Diese Einrichtung veranschaulicht, wie Workflow-Automatisierung genutzt werden kann, um die betriebliche Effizienz zu steigern und die finanzielle Integrität sicherzustellen, insbesondere bei der Verwaltung komplexer Einkaufsprozesse innerhalb eines Unternehmens.
