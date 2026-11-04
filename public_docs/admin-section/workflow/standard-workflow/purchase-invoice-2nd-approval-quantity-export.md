# Kaufrechnung - 2. Genehmigungsmenge Export

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="Bestellung Export Genehmigung Rechnung Übersicht"><figcaption></figcaption></figure>

Dieser Titel zeigt an, dass die Regel eingerichtet ist, um die zweite Genehmigungsphase für Kaufrechnungen mit Schwerpunkt auf den Mengendetails zu verwalten und sicherzustellen, dass die Mengen auf der Rechnung mit denen auf der ursprünglichen Bestellung übereinstimmen.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für als Rechnungen identifizierte Dokumente aktiviert wird, was für die genaue Lenkung des Workflows entscheidend ist.
2. **Und…**
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Dies gibt an, dass die Rechnung derzeit auf die zweite Genehmigung wartet. Diese Phase bietet oft zusätzliche Überwachung, um die Genauigkeit vor Abschluss der Transaktion sicherzustellen.
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Kaufrechnung**: Diese Bedingung spezifiziert weiter, dass die Regel nur für Rechnungen gilt, die speziell als "Kaufrechnungen" kategorisiert sind, um sie von anderen Arten von Rechnungen zu unterscheiden.
* **Logikmenge in Auftragsbestätigung Gleich Bestellung**: Diese Bedingung überprüft, ob die in der Auftragsbestätigung aufgeführte Menge mit der Menge in der Bestellung übereinstimmt. Sie stellt sicher, dass die Rechnungsbearbeitung nur fortgesetzt wird, wenn die Mengen konsistent sind, was für das Bestandsmanagement und die finanzielle Genauigkeit entscheidend ist.

#### Aktion (Dann…):

* **Export starten**: Sobald die Rechnung die spezifizierten Bedingungen erfüllt (d. h. die Mengen zwischen der Auftragsbestätigung und der Bestellung übereinstimmen), wird die Aktion "Export starten" ausgelöst. Dies beinhaltet wahrscheinlich das Exportieren der Rechnungsdaten für die weitere Verarbeitung, möglicherweise in ein anderes Finanzsystem oder für Berichtszwecke.

#### Zweck dieser Regel:

* **Genauigkeit und Konsistenz sicherstellen**: Durch die Überprüfung, ob die Mengen zwischen der Auftragsbestätigung und der Bestellung übereinstimmen, hilft das System, die Bestandsgenauigkeit zu gewährleisten und Diskrepanzen zu vermeiden, die sich auf die Finanzberichterstattung oder das Lagermanagement auswirken könnten.
* **Finanzielle Verarbeitung optimieren**: Die Automatisierung des Datenexports, sobald die Mengen bestätigt sind, reduziert die manuelle Bearbeitung und beschleunigt den Finanzverarbeitungszyklus.
* **Compliance und Überwachung verbessern**: Die Anforderung einer zweiten Genehmigung zur Mengenverifizierung fügt eine zusätzliche Überwachungsebene hinzu, die für die Einhaltung finanzieller Richtlinien und Kontrollen entscheidend ist.

Diese Regel ist ein klares Beispiel dafür, wie die Workflow-Automatisierung effektiv eingesetzt werden kann, um eine präzise und effiziente Bearbeitung von Finanzdokumenten innerhalb einer Organisation sicherzustellen, insbesondere im Kontext von Einkaufsprozessen, die eine große Anzahl von Transaktionen mit akribischer Validierung erfordern.
