# Über dem maximalen Betrag

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel deutet darauf hin, dass die Regel darauf ausgelegt ist, Fälle zu verwalten, in denen der Rechnungsbetrag größer ist als der maximale Betrag, den ein Genehmiger berechtigt ist zu bearbeiten.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für Rechnungen gilt, was für die korrekte Weiterleitung des Workflows wesentlich ist.
2. **Und…**
* **Dokumentenstatus ist Ausstehende Genehmigung**: Die Rechnung muss sich im Status "Ausstehende Genehmigung" befinden. Dieser Status ist entscheidend, um sicherzustellen, dass die Regel auf Rechnungen angewendet wird, die noch bearbeitet werden und noch nicht abgeschlossen sind.
* **Vergleiche zwei Felder: Gesamtbetrag größer als Genehmiger Maximalbetrag**: Diese Bedingung überprüft, ob der Gesamtbetrag der Rechnung den maximalen Betrag überschreitet, den ein Genehmiger bearbeiten darf. Dieser Vergleich kann auch eine Toleranzeinstellung enthalten, die geringfügige Abweichungen basierend auf vordefinierten Kriterien zulässt.

#### Aktion (Dann…):

* **Benutzer aus Feld Nächster Genehmiger zuweisen, Benutzer User als Fallback verwenden**: Wenn die Rechnung den festgelegten maximalen Betrag überschreitet, wird sie automatisch einem Genehmiger auf einer höheren Ebene zugewiesen, der durch das Feld 'Nächster Genehmiger' angezeigt wird. Wenn dieses Feld nicht ausgefüllt ist oder der angegebene Benutzer nicht verfügbar ist, wird ein Standardbenutzer (wahrscheinlich ein Administrator oder ein anderes festgelegtes Personalmitglied) als Fallback verwendet, um sicherzustellen, dass die Rechnung ohne Verzögerung überprüft wird.

#### Schnittstellenelemente:

* **Karte hinzufügen**: Diese Option ermöglicht es, zusätzliche Bedingungen oder Aktionen zur Regel hinzuzufügen, um auf komplexe Szenarien eingehen zu können.
* **Speichern**: Diese Schaltfläche speichert die Regelkonfiguration im System.

#### Zweck dieser Regel:

Der Zweck dieser Regel besteht darin sicherzustellen, dass Rechnungen, die bestimmte finanzielle Schwellenwerte überschreiten, von Genehmigern mit den entsprechenden Autorisierungsebenen überprüft werden. Dies trägt dazu bei, die finanzielle Kontrolle und Überwachung aufrechtzuerhalten, indem sichergestellt wird, dass Ausgaben von Personal mit den erforderlichen Genehmigungslimits überprüft werden, wodurch die Organisation vor unbefugten oder unangemessenen Ausgaben geschützt wird.

Diese Regel, wie die vorherige, hilft dabei, den Workflow zu automatisieren, den manuellen Aufwand zu reduzieren und die Einhaltung der finanziellen Richtlinien der Organisation zu verbessern. Es ist ein Beispiel dafür, wie die Workflow-Automatisierung effektiv genutzt werden kann, um komplexe finanzielle Prozesse innerhalb eines Unternehmens zu verwalten.
