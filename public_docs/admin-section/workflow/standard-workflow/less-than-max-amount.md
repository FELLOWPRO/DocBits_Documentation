# Weniger als maximale Menge

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel legt nahe, dass die festgelegte Regel oder Bedingung darauf ausgelegt ist, Rechnungen zu bearbeiten, bei denen der Gesamtbetrag weniger als oder gleich einer festgelegten maximalen Menge beträgt.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung überprüft, ob das zu verarbeitende Dokument eine Rechnung ist. Dies ist entscheidend, um sicherzustellen, dass die Regel nur für Rechnungen und nicht für andere Dokumententypen gilt.
2. **Und…**
* **Dokumentenstatus ist Ausstehende Genehmigung**: Dies legt fest, dass die Rechnung sich im Status "Ausstehende Genehmigung" befinden muss. Diese Statusüberprüfung stellt sicher, dass die Regel nur für Rechnungen gilt, die auf Genehmigung warten.
* **Vergleiche zwei Felder: Gesamtbetrag kleiner oder gleich Genehmiger Maximalbetrag**: Diese Bedingung vergleicht den Gesamtbetrag der Rechnung mit dem maximal autorisierten Betrag eines Genehmigers. Wenn der Gesamtbetrag der Rechnung kleiner als oder gleich diesem Maximalbetrag ist, wird die Regel zum nächsten Schritt fortgesetzt. Dies beinhaltet wahrscheinlich eine Toleranzgrenze, die geringfügige Abweichungen innerhalb festgelegter Grenzen zulässt.

#### Aktion (Dann…):

* **Benutzer aus Feld Genehmiger Name zuweisen, Benutzer User als Fallback verwenden**: Wenn die festgelegten Bedingungen erfüllt sind, wird die Rechnung automatisch einem Genehmiger zugewiesen, dessen Name in einem Feld angegeben ist. Wenn dieses Feld leer oder nicht verfügbar ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderes festgelegtes Personalmitglied) als Fallback zugewiesen, um die Genehmigung zu bearbeiten.

#### Schnittstellenelemente:

* **Karte hinzufügen**: Diese Schaltfläche ermöglicht Benutzern wahrscheinlich, weitere Bedingungen oder Aktionen zur Regel hinzuzufügen, um die Flexibilität und Spezifität des Workflows zu verbessern.
* **Speichern**: Speichert die konfigurierte Regel im System.

#### Zweck dieser Regel:

Diese Einrichtung soll den Genehmigungsprozess für Rechnungen optimieren, indem Rechnungen automatisch an den entsprechenden Genehmiger weitergeleitet werden, basierend auf dem Betrag, und sicherstellen, dass nur diejenigen innerhalb eines bestimmten Schwellenwerts auf diese automatisierte Weise behandelt werden. Dies hilft bei der Verwaltung finanzieller Kontrollen und beschleunigt den Workflow, indem manuelle Überprüfungen für jede Rechnung reduziert werden.
