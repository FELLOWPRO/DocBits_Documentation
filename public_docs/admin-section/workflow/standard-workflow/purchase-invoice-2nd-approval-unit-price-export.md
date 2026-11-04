# Kaufrechnung - 2. Genehmigungseinheit Preis Export

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="Bestellung Export Genehmigung Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel zeigt an, dass die Regel eingerichtet ist, um die zweite Genehmigungsphase von Kaufrechnungen mit Schwerpunkt auf dem Stückpreis zu verwalten und sicherzustellen, dass er den vereinbarten Bedingungen entspricht.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für als Rechnungen identifizierte Dokumente aktiviert wird, was für die genaue Lenkung des Workflows entscheidend ist.
2. **Und…**
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Dies gibt an, dass die Rechnung auf die zweite Genehmigung wartet. Diese Phase bietet oft zusätzliche Überwachung, um die Genauigkeit vor Abschluss der Transaktion sicherzustellen.
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Kaufrechnung**: Diese Bedingung spezifiziert weiter, dass die Regel nur für Rechnungen gilt, die speziell als "Kaufrechnungen" kategorisiert sind, um sie von anderen Arten von Rechnungen zu unterscheiden.
* **Logik Stückpreis in Auftragsbestätigung ist gleich Bestellung**: Diese Bedingung überprüft, ob der Stückpreis in der Auftragsbestätigung mit dem Stückpreis in der Bestellung übereinstimmt. Sie stellt sicher, dass die Rechnungsbearbeitung nur fortgesetzt wird, wenn eine Preiskonsistenz besteht, was für die Budgetierung und Finanzberichterstattung entscheidend ist.

#### Aktion (Dann…):

* **Export starten**: Sobald die Rechnung die spezifizierten Bedingungen erfüllt (d. h. die Stückpreise zwischen der Auftragsbestätigung und der Bestellung übereinstimmen), wird die Aktion "Export starten" ausgelöst. Dies beinhaltet wahrscheinlich das Exportieren der Rechnungsdaten für weitere Verarbeitung, möglicherweise in ein anderes Finanzsystem oder für Berichtszwecke.

#### Zweck dieser Regel:

* **Genauigkeit und Konsistenz sicherstellen**: Durch die Überprüfung, ob die Stückpreise zwischen der Auftragsbestätigung und der Bestellung übereinstimmen, hilft das System, die finanzielle Genauigkeit zu gewährleisten und Über- oder Unterbelastungen zu verhindern.
* **Finanzielle Verarbeitung optimieren**: Die Automatisierung des Datenexports, sobald die Preise bestätigt sind, reduziert die manuelle Bearbeitung und beschleunigt den Finanzverarbeitungszyklus.
* **Compliance und Überwachung verbessern**: Die Anforderung einer zweiten Genehmigung zur Preisüberprüfung fügt eine zusätzliche Überwachungsebene hinzu, die für die Einhaltung finanzieller Richtlinien und Kontrollen entscheidend ist.

Diese Regel ist ein Beispiel dafür, wie die Workflow-Automatisierung effektiv genutzt werden kann, um eine präzise und effiziente Bearbeitung von Finanzdokumenten innerhalb einer Organisation sicherzustellen, insbesondere im Kontext großer Transaktionsvolumina, die eine sorgfältige Validierung erfordern.
