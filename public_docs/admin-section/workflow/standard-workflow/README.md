# Standard Workflow

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="Workflow Bestellung Übersicht"><figcaption></figcaption></figure>

#### Übersicht der Workflow-Komponenten:

* **AP-Rechnungs-E-Mail**: Der Prozess beginnt wahrscheinlich mit einer per E-Mail erhaltenen Rechnung.
* **DocBits**: Dieses Tool wird möglicherweise für anfängliche Aufgaben im Dokumentenmanagement wie das Erfassen und Digitalisieren von Rechnungen verwendet.
* **Finanzüberprüfung**: Rechnungen durchlaufen eine Finanzüberprüfung, bei der Entscheidungen über ihre Gültigkeit und Genauigkeit getroffen werden.

#### Schritte im Workflow:

1. **Erstüberprüfung**:
* Rechnungen werden empfangen und zunächst mit DocBits verarbeitet.
* Anschließend werden sie vom Finanzteam überprüft, um sicherzustellen, dass sie aus dem Workflow entfernt werden, wenn sie vollständig sind, oder zur weiteren Verarbeitung weitergeleitet werden.
2. **PO vs. Nicht-PO-Rechnungen**:
* Der Workflow unterscheidet zwischen PO-bezogenen und nicht-PO-Rechnungen.
* Nicht-PO-Rechnungen werden basierend auf vordefinierten Kriterien wie Lieferanten-ID, Menge, Stückpreis und Artikelnummer zur weiteren Genehmigung oder Ablehnung weitergeleitet.
3. **Abgleich und Nichtübereinstimmung**:
* Rechnungen werden mit Warenempfangsbelegen abgeglichen, um sicherzustellen, dass Details übereinstimmen (wie Lieferanten-ID und Menge).
* Bei Abweichungen unterliegt die Rechnung einer weiteren Überprüfung und möglicherweise einer Ablehnung.
4. **Finanz- und Einkäuferüberprüfung**:
* Bei PO-bezogenen Rechnungen wird ein detaillierter Abgleichsprozess durchgeführt, der eine Einkäuferüberprüfung einschließt.
* Anpassungen an Bestellungen oder Warenempfangsbelegen können erforderlich sein.
5. **Endgültige Entscheidungen**:
* Rechnungen, die alle Prüfungen bestehen, werden genehmigt und in Finanzsysteme zur Aufzeichnung integriert.
* Abgelehnte Rechnungen lösen Benachrichtigungen aus, und der Einkäufer kann eine neue Rechnung anfordern.
6. **Integration mit Infor IDM & LN+M3**:
* Genehmigte Rechnungen werden wahrscheinlich an Infor's IDM zur Dokumentenverwaltung und an LN zur Buchung übermittelt.
* Diese Integration stellt sicher, dass alle Finanzdatensätze aktuell sind und dass der Workflow nahtlos in das umfassendere ERP-System einfließt.

#### Entscheidungspunkte:

* Im Verlauf des Workflows gibt es verschiedene Entscheidungspunkte, an denen eine Rechnung genehmigt, abgelehnt oder zur zusätzlichen Information zurückgesendet werden kann. Benachrichtigungen werden nach Verzögerungen versendet, um eine zeitnahe Bearbeitung sicherzustellen.

Diese Workflows werden in den Standard-Workflow aufgenommen.
