# Less than Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel legt nahe, dass die eingerichtete Regel oder Bedingung dafür ausgelegt ist, Rechnungen zu behandeln, bei denen der Gesamtbetrag kleiner oder gleich einem festgelegten Maximalbetrag ist.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung prüft, ob das verarbeitete Dokument eine Rechnung ist. Dies ist entscheidend, um sicherzustellen, dass die Regel nur auf Rechnungen und nicht auf andere Dokumenttypen angewendet wird.
2. **And…**
   * **Document Status is Pending Approval**: Dies legt fest, dass die Rechnung den Status „Pending Approval" haben muss. Diese Statusprüfung stellt sicher, dass die Regel nur auf Rechnungen angewendet wird, die auf eine Genehmigung warten.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Diese Bedingung vergleicht den Gesamtbetrag der Rechnung mit dem maximal autorisierten Betrag eines Genehmigers. Wenn der Gesamtbetrag der Rechnung kleiner oder gleich diesem Maximalbetrag ist, fährt die Regel mit dem nächsten Schritt fort. Dies beinhaltet wahrscheinlich eine Toleranzstufe, die geringfügige Abweichungen innerhalb festgelegter Grenzen zulässt.

#### Aktion (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Wenn die festgelegten Bedingungen erfüllt sind, wird die Rechnung automatisch einem Genehmiger zugewiesen, dessen Name in einem Feld angegeben ist. Wenn dieses Feld leer oder nicht verfügbar ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderer designierter Mitarbeiter) als Fallback zugewiesen, um die Genehmigung zu bearbeiten.

#### Oberflächenelemente:

* **Add Card**: Diese Schaltfläche ermöglicht es Benutzern, weitere Bedingungen oder Aktionen zur Regel hinzuzufügen und so die Flexibilität und Spezifität des Workflows zu erhöhen.
* **Save**: Speichert die konfigurierte Regel im System.

#### Zweck dieser Regel:

Diese Einrichtung ist darauf ausgelegt, den Genehmigungsprozess für Rechnungen zu optimieren, indem Rechnungen anhand des Betrags automatisch an den passenden Genehmiger weitergeleitet werden und sichergestellt wird, dass nur jene innerhalb eines bestimmten Schwellenwerts auf diese automatisierte Weise bearbeitet werden. Sie hilft bei der Verwaltung finanzieller Kontrollen und beschleunigt den Workflow, indem manuelle Prüfungen für jede Rechnung reduziert werden.

\\
