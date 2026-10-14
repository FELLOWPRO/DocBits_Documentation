# Standard Workflow

<figure><img src="../../../.gitbook/assets/DocBits-APWorkflow-Gronbach.drawio (1) (1).svg" alt=""><figcaption></figcaption></figure>

#### Überblick über die Workflow-Komponenten:

* **AP Invoice Email**: Der Prozess beginnt in der Regel mit einer per E-Mail eingegangenen Rechnung.
* **DocBits**: Dieses Tool wird für erste Dokumentenmanagement-Aufgaben wie das Erfassen und Digitalisieren von Rechnungen verwendet.
* **Finance Review**: Rechnungen durchlaufen eine Finanzprüfung, bei der über ihre Gültigkeit und Richtigkeit entschieden wird.

#### Schritte im Workflow:

1. **Erstprüfung**:
   * Rechnungen werden empfangen und zunächst mit DocBits verarbeitet.
   * Anschließend werden sie vom Finanzteam geprüft, um sicherzustellen, dass sie aus dem Workflow entfernt werden, wenn sie vollständig sind, oder zur weiteren Verarbeitung weitergeleitet werden.
2. **PO- vs. Nicht-PO-Rechnungen**:
   * Der Workflow unterscheidet zwischen PO-bezogenen und Nicht-PO-Rechnungen.
   * Nicht-PO-Rechnungen werden anhand vordefinierter Kriterien wie Lieferanten-ID, Menge, Stückpreis und Artikelnummer zur weiteren Genehmigung oder Ablehnung weitergeleitet.
3. **Übereinstimmung und Abweichung**:
   * Rechnungen werden mit Wareneingängen abgeglichen, um sicherzustellen, dass die Details übereinstimmen (wie Lieferanten-ID und Menge).
   * Treten Abweichungen auf, unterliegt die Rechnung einer weiteren Prüfung und möglicherweise einer Ablehnung.
4. **Finanz- und Einkäuferprüfung**:
   * Für PO-bezogene Rechnungen wird ein detaillierter Abgleichsprozess durchgeführt, der eine Einkäuferprüfung umfasst.
   * Möglicherweise sind Anpassungen an Bestellungen oder Wareneingängen erforderlich.
5. **Endgültige Entscheidungen**:
   * Rechnungen, die alle Prüfungen bestehen, werden genehmigt und zur Aufbewahrung in Finanzsysteme integriert.
   * Abgelehnte Rechnungen lösen Benachrichtigungen aus, und der Einkäufer kann eine neue Rechnung anfordern.
6. **Integration mit Infor IDM & LN+M3**:
   * Genehmigte Rechnungen werden in der Regel an Infors IDM für das Dokumentenmanagement und an LN für die Buchung im Hauptbuch gesendet.
   * Diese Integration stellt sicher, dass alle Finanzunterlagen aktuell sind und der Workflow nahtlos in das umfassendere ERP-System einfließt.

#### Entscheidungspunkte:

* Im gesamten Workflow gibt es verschiedene Entscheidungspunkte, an denen eine Rechnung genehmigt, abgelehnt oder zur Beschaffung zusätzlicher Informationen zurückgesendet werden kann. Nach Verzögerungen werden Benachrichtigungen versendet, um eine zeitnahe Verarbeitung sicherzustellen.

Diese Workflows werden in den Standard Workflow aufgenommen.
