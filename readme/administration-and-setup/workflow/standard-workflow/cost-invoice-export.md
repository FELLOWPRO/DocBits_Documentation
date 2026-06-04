# Cost Invoice - Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28 (1).png" alt=""><figcaption></figcaption></figure>

Dieser Titel weist darauf hin, dass die Regel speziell für die Verwaltung von Kostenrechnungen konfiguriert ist und eine Export-Aktion umfasst, möglicherweise für Berichte, weitere Verarbeitung oder Integration mit anderen Systemen.

#### Regelkonfiguration:

1. **When…**
   * **Document Type is Invoice**: Diese Bedingung stellt sicher, dass die Regel nur für Dokumente ausgelöst wird, die als Rechnungen kategorisiert sind, und erhält so die Spezifität des Workflows für die Rechnungsverwaltung.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Dies legt fest, dass die Regel nur auf jene Rechnungen angewendet wird, die in einem bestimmten Feld innerhalb des Dokuments ausdrücklich als „Cost Invoices" markiert sind. Dies hilft, sie von anderen Rechnungsarten zu unterscheiden.
   * **Document Status is Pending Second Approval**: Die Rechnung muss den Status „Pending Second Approval" haben. Dies weist darauf hin, dass die Rechnung bereits eine erste Genehmigung durchlaufen hat und auf eine zweite, möglicherweise abschließende Prüfung wartet.

#### Aktion (Then…):

* **Start Export**: Sobald die Rechnung die festgelegten Bedingungen erfüllt (eine Kostenrechnung ist und auf die zweite Genehmigung wartet), wird die Aktion „Start Export" ausgeführt. Dies kann das Senden der Rechnungsdaten an ein anderes System zur Finanzanalyse, für Berichte oder zu Compliance-Zwecken umfassen.

#### Zweck dieser Regel:

* **Workflow-Effizienz**: Diese Regel hilft, die Bearbeitung von Kostenrechnungen zu automatisieren, indem sichergestellt wird, dass sie ohne manuelles Eingreifen die erforderlichen Genehmigungsstufen durchlaufen, was die Geschwindigkeit und Genauigkeit der Finanzvorgänge erhöht.
* **Kontrolle und Compliance**: Durch die Anforderung einer zweiten Genehmigung erzwingt das System einen Kontrollmechanismus, der sicherstellt, dass Kostenrechnungen gründlich geprüft werden, und verbessert so die finanzielle Aufsicht.
* **Integration und Berichterstattung**: Die Export-Aktion legt nahe, dass vollständig genehmigte Rechnungen zur weiteren Verarbeitung oder Analyse in andere Systeme integriert werden können, was für die Finanzberichterstattung und Audits entscheidend ist.

Diese Art von Regel ist für Organisationen unverzichtbar, die mit verschiedenen Rechnungsarten umgehen und sicherstellen müssen, dass jede Art gemäß bestimmten Protokollen behandelt wird. Sie reduziert das Fehlerrisiko und gewährleistet die Einhaltung interner Kontrollen und externer Vorschriften.
