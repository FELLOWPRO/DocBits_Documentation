# Kaufrechnung - 2. Genehmigungseinheit Preis

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="Genehmigung Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel zeigt an, dass die Regel eingerichtet ist, um die zweite Genehmigungsphase einer Kaufrechnung zu verwalten, wobei ein spezieller Fokus auf der Validierung des Stückpreises liegt.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente ausgelöst wird, die als Rechnungen identifiziert sind, wodurch andere Dokumententypen herausgefiltert und die Relevanz des Workflows aufrechterhalten wird.
2. **Und…**
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Dies gibt an, dass die Rechnung in der Phase ist, in der sie auf die zweite Genehmigung wartet. Dies ist in der Regel ein Schritt, der zusätzliches Aufsichtsverfahren vor der endgültigen Bearbeitung sicherstellt.
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Kaufrechnung**: Dies grenzt die Anwendung dieser Regel weiter ein und bezieht sich nur auf Rechnungen, die als "Kaufrechnungen" klassifiziert sind, wodurch sie von anderen Rechnungsuntertypen unterschieden werden.
* **Logik Stückpreis in Auftragsbestätigung ist nicht gleich Einkaufsbestellung**: Diese logische Überprüfung ist entscheidend, da sie den Stückpreis in der Auftragsbestätigung mit dem Stückpreis in der ursprünglichen Einkaufsbestellung vergleicht. Die Aktion wird ausgelöst, wenn diese Werte nicht übereinstimmen, was auf eine Diskrepanz hinweisen könnte, die gelöst werden muss.

#### Aktion (Dann…):

* **Benutzer aus Feld Käufername zuweisen, Benutzer User als Fallback verwenden**: Wenn die angegebenen Bedingungen erfüllt sind (d. h. es besteht ein Unterschied in den Stückpreisen), wird die Rechnung automatisch einem Käufer (dem im Feld 'Käufername' angegebenen Namen) zur weiteren Überprüfung zugewiesen. Wenn das Feld 'Käufername' leer oder nicht angegeben ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderes festgelegtes Personalmitglied) als Fallback zugewiesen, um die Genehmigung zu bearbeiten.

#### Zweck dieser Regel:

* **Genauigkeit und Einhaltung sicherstellen**: Diese Regel ist entscheidend, um sicherzustellen, dass der Rechnungsprozess genau ist und den vereinbarten Bedingungen entspricht. Durch Auslösen einer Überprüfung bei Diskrepanzen in den Stückpreisen hilft das System, finanzielle Fehler oder potenziellen Betrug zu verhindern.
* **Genehmigungen optimieren**: Die Automatisierung der Zuweisung zur Überprüfung basierend auf spezifischen Diskrepanzen hilft, den Genehmigungsprozess zu optimieren und sicherzustellen, dass Probleme schnell von den entsprechenden Mitarbeitern angegangen werden.
* **Finanzielle Aufsicht**: Die Anforderung einer zweiten Genehmigung, insbesondere basierend auf Preisabgleich, stärkt die finanziellen Kontrollen und die Rechenschaftspflicht innerhalb der Organisation.
