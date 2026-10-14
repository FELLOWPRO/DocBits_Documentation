# Above Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass die Regel dafür ausgelegt ist, Fälle zu verwalten, in denen der Rechnungsgesamtbetrag höher ist als der maximale Betrag, den ein Genehmiger bearbeiten darf.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur auf Rechnungen angewendet wird, was für die korrekte Steuerung des Workflows wesentlich ist.
2. **And…**
   * **Document Status is Pending Approval**: Die Rechnung muss den Status „Pending Approval" haben. Dieser Status ist entscheidend, um sicherzustellen, dass die Regel auf Rechnungen angewendet wird, die noch in Bearbeitung sind und noch nicht abgeschlossen wurden.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Diese Bedingung prüft, ob der Gesamtbetrag der Rechnung den maximalen Betrag überschreitet, den ein Genehmiger bearbeiten darf. Dieser Vergleich kann auch eine Toleranzeinstellung enthalten, die geringfügige Abweichungen anhand vordefinierter Kriterien zulässt.

#### Aktion (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Wenn die Rechnung den festgelegten Maximalbetrag überschreitet, wird sie automatisch einem übergeordneten Genehmiger zugewiesen, der im Feld „Next Level Approver" angegeben ist. Wenn dieses Feld nicht ausgefüllt oder der angegebene Benutzer nicht verfügbar ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderer designierter Mitarbeiter) als Fallback verwendet, um sicherzustellen, dass die Rechnung ohne Verzögerung geprüft wird.

#### Oberflächenelemente:

* **Add Card**: Diese Option ermöglicht das Hinzufügen weiterer Bedingungen oder Aktionen zur Regel und bietet Flexibilität für komplexe Szenarien.
* **Save**: Diese Schaltfläche speichert die Regelkonfiguration im System.

#### Zweck dieser Regel:

Der Zweck dieser Regel besteht darin, sicherzustellen, dass Rechnungen, die bestimmte finanzielle Schwellenwerte überschreiten, von Genehmigern mit den entsprechenden Autorisierungsstufen geprüft werden. Dies hilft, die finanzielle Kontrolle und Aufsicht zu wahren, indem sichergestellt wird, dass Ausgaben von Personal mit den erforderlichen Genehmigungsgrenzen geprüft werden, und schützt so die Organisation vor unbefugten oder unangemessenen Ausgaben.

Diese Regel hilft wie die vorherige, den Workflow zu automatisieren, den manuellen Aufwand zu reduzieren und die Einhaltung der Finanzrichtlinien der Organisation zu verbessern. Sie ist ein Beispiel dafür, wie Workflow-Automatisierung effektiv zur Verwaltung komplexer Finanzprozesse innerhalb eines Unternehmens eingesetzt werden kann.
