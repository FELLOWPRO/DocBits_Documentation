# Einkaufsrechnung - 2. Genehmigungsmenge

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="Genehmigung Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel deutet darauf hin, dass die Regel speziell für die Bearbeitung von Einkaufsrechnungen während einer sekundären Genehmigungsphase gilt, wobei der Schwerpunkt auf der Überprüfung der Genauigkeit der aufgeführten Mengen liegt.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für als Rechnungen klassifizierte Dokumente aktiviert wird. Dies ist entscheidend, um Spezifität und Relevanz im Workflow aufrechtzuerhalten.
2. **Und…**
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Dies gibt an, dass die Rechnung derzeit auf die zweite Genehmigung wartet. Diese Phase soll in der Regel eine zusätzliche Überwachung vor der endgültigen Abwicklung der Rechnung ermöglichen.
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Einkaufsrechnung**: Diese Bedingung verfeinert die Regel weiter, um sie ausschließlich auf Rechnungen anzuwenden, die als "Einkaufsrechnungen" identifiziert sind. Diese Kategorisierung hilft dabei, sie von anderen Rechnungstypen zu unterscheiden.
* **Logikmenge in Auftragsbestätigung ist nicht gleich Bestellung**: Diese entscheidende Bedingung überprüft, ob die in der Auftragsbestätigung angegebene Menge mit der Menge in der ursprünglichen Bestellung übereinstimmt. Die Aktion wird ausgelöst, wenn ein Unterschied festgestellt wird, was auf einen möglichen Fehler oder ein Problem hinweist, das gelöst werden muss.

#### Aktion (Dann…):

* **Benutzer aus Feld Käufername zuweisen, Benutzer User als Fallback verwenden**: Wenn die Bedingungen der Regel erfüllt sind (d. h. es gibt eine Diskrepanz bei den Mengen), wird die Rechnung automatisch zur weiteren Überprüfung an die im Feld 'Käufername' aufgeführte Person zugewiesen. Wenn dieses Feld leer ist oder die angegebene Person nicht verfügbar ist, übernimmt ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderes festgelegtes Personal) die Aufgabe, um eine zeitnahe Überprüfung und Lösung sicherzustellen.

#### Zweck dieser Regel:

* **Genauigkeit und Konformität**: Die Regel ist entscheidend, um sicherzustellen, dass der Rechnungsprozess genau ist und mit den in der Bestellung vereinbarten Bedingungen übereinstimmt. Sie hilft, finanzielle Diskrepanzen und potenzielle Lagerfehler zu verhindern.
* **Vereinfachte Genehmigungen**: Die Automatisierung des Überprüfungsprozesses für spezifische Diskrepanzen trägt dazu bei, Genehmigungen zu vereinfachen und sicherzustellen, dass etwaige Probleme schnell von den entsprechenden Mitarbeitern angegangen werden.
* **Verbesserte finanzielle Aufsicht**: Die Anforderung einer zweiten Genehmigung für Mengenverifizierungen stärkt die finanziellen Kontrollen und die Rechenschaftspflicht innerhalb der Organisation.

Dieses Setup veranschaulicht, wie die Workflow-Automatisierung genutzt werden kann, um die operationale Effizienz zu steigern und die finanzielle Integrität sicherzustellen, insbesondere bei der Verwaltung komplexer Einkaufsprozesse innerhalb eines Unternehmens.
