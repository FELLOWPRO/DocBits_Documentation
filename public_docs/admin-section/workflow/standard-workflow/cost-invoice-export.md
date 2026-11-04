# Kostenrechnung - Export

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="Bestellung Export Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel deutet darauf hin, dass die Regel speziell für das Management von Kostenrechnungen konfiguriert ist und eine Exportaktion beinhaltet, möglicherweise für Berichterstattung, weitere Verarbeitung oder Integration mit anderen Systemen.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für als Rechnungen kategorisierte Dokumente ausgelöst wird und die Spezifität des Workflows für das Rechnungsmanagement beibehält.
2. **Und…**
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Kostenrechnung**: Dies legt fest, dass die Regel nur für diejenigen Rechnungen gilt, die explizit als "Kostenrechnungen" in einem bestimmten Feld innerhalb des Dokuments markiert sind. Dies hilft dabei, sie von anderen Arten von Rechnungen zu unterscheiden.
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Die Rechnung muss sich im Status "Ausstehende zweite Genehmigung" befinden. Dies deutet darauf hin, dass die Rechnung bereits eine erste Genehmigung durchlaufen hat und auf eine zweite, möglicherweise endgültige, Überprüfung wartet.

#### Aktion (Dann…):

* **Export starten**: Sobald die Rechnung die spezifizierten Bedingungen erfüllt (Kostenrechnung und ausstehende zweite Genehmigung), wird die Aktion "Export starten" ausgeführt. Dies könnte beinhalten, dass die Rechnungsdaten an ein anderes System für finanzielle Analyse, Berichterstattung oder Compliance-Zwecke gesendet werden.

#### Zweck dieser Regel:

* **Workflow-Effizienz**: Diese Regel hilft dabei, die Bearbeitung von Kostenrechnungen zu automatisieren, indem sichergestellt wird, dass sie ohne manuelle Eingriffe durch die erforderlichen Genehmigungsstufen bearbeitet werden, was die Geschwindigkeit und Genauigkeit der finanziellen Operationen erhöht.
* **Kontrolle und Compliance**: Durch die Anforderung einer zweiten Genehmigung setzt das System einen Kontrollmechanismus durch, der sicherstellt, dass Kostenrechnungen gründlich überprüft werden, was die finanzielle Aufsicht verbessert.
* **Integration und Berichterstattung**: Die Exportaktion legt nahe, dass genehmigte Rechnungen in andere Systeme integriert werden können, um sie weiter zu verarbeiten oder zu analysieren, was für die finanzielle Berichterstattung und Prüfungen entscheidend ist.

Diese Art von Regel ist für Organisationen unerlässlich, die mit verschiedenen Arten von Rechnungen umgehen und sicherstellen müssen, dass jede Art gemäß spezifischer Protokolle behandelt wird. Sie reduziert das Risiko von Fehlern und gewährleistet die Einhaltung interner Kontrollen und externer Vorschriften.
