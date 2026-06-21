# Test der Rechnungsautomatisierung mit DocBits

## Überblick

Dieses Dokument beschreibt den Testplan für die Rechnungsautomatisierung mit DocBits unter Verwendung von Infor LN oder M3. Es enthält Details zu Testfällen, zur Testvorbereitung, zu den Ausführungsschritten sowie zu den Support-Prozessen.

## Testfälle

| ID | Testfall                                                                    | Beschreibung                                                                                                                                                                              | Status            |
| -- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 1  | Kostenrechnungen                                                          | Rechnungen ohne Bestellung werden in DocBits erfolgreich verarbeitet und als „Kostenrechnung" nach LN exportiert.                                                                          | ZU TESTEN         |
| 2  | Bestellbezogene Rechnung mit perfekter Übereinstimmung                    | Bestellbezogene Rechnungen werden in DocBits erfolgreich verarbeitet, mit einer perfekten Übereinstimmung von Rechnung zu Bestellung, da Artikelnummer, Menge und Stückpreis übereinstimmen. | ZU TESTEN         |
| 3  | Bestellbezogene Rechnungen mit abweichender Menge                         | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im PO-Matching-Modul gibt es eine Abweichung bei der Menge.                                                                 | ZU TESTEN         |
| 4  | Bestellbezogene Rechnungen mit abweichendem Stückpreis                    | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im PO-Matching-Modul gibt es eine Abweichung beim Stückpreis.                                                               | ZU TESTEN         |
| 5  | Bestellbezogene Rechnungen mit abweichender oder nicht vorhandener Artikelnummer | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im PO-Matching-Modul gibt es eine Abweichung oder eine nicht vorhandene Artikelnummer.                                | ZU TESTEN         |
| 6  | Bestellbezogene Rechnungen mit einer Abweichung innerhalb der Toleranz    | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im PO-Matching-Modul gibt es eine Abweichung bei Menge oder Stückpreis, die jedoch innerhalb der Toleranz liegt.            | ZU TESTEN         |
| 7  | Gutschriften                                                              | Gutschriften werden in DocBits erfolgreich verarbeitet und nach LN exportiert. Klären Sie, ob die Beträge mit positivem oder negativem Vorzeichen exportiert werden sollen.                | ZU TESTEN         |

## Plan für den Test mit dem Kunden

### 1. Einrichtung

* **Erstgespräch**: Vereinbaren Sie ein Kick-off-Meeting mit dem Kunden, um den Testprozess und die Ziele zu erläutern.
* **Zugang und Berechtigungen**: Stellen Sie sicher, dass der Kunde über alle erforderlichen Zugänge zu DocBits und Infor LN oder M3 für Testzwecke verfügt.

### 2. Testvorbereitung

* **Schulung**: Bieten Sie dem Team des Kunden eine umfassende Schulung darüber an, wie DocBits für die Rechnungsverarbeitung verwendet wird.
* **Dokumentation**: Stellen Sie eine detaillierte Dokumentation zu den Testverfahren bereit, einschließlich der erwarteten Ergebnisse für jeden Testfall.

### 3. Ausführung der Testfälle

* **Testumgebung**: Richten Sie eine Testumgebung ein, die das Produktivsystem des Kunden so genau wie möglich abbildet.
* **Schritt-für-Schritt-Test**: Arbeiten Sie mit dem Kunden zusammen, um jeden Testfall auszuführen, und stellen Sie sicher, dass er jeden Schritt versteht:
  * Verarbeiten Sie Rechnungen über DocBits.
  * Überprüfen Sie das Ergebnis im PO-Matching-Modul.
  * Prüfen Sie die Exportergebnisse in LN oder M3.

### 4. Problembehebung

* **Nachverfolgung**: Verwenden Sie ein Tracking-System (wie Jira oder eine einfache Tabelle), um alle Probleme oder Abweichungen zu protokollieren, die während des Tests auftreten.
* **Support**: Bieten Sie sofortigen Support, um Probleme zu lösen und etwaige Unklarheiten zu beseitigen.

### 5. Überprüfung und Feedback

* **Überprüfung**: Überprüfen Sie nach jedem Testfall die Ergebnisse mit dem Kunden, um die Korrektheit sicherzustellen.
* **Feedback-Schleife**: Sammeln Sie Feedback vom Kunden zum Prozess und zu allen notwendigen Verbesserungen.

### 6. Abschluss

* **Dokumentation der Ergebnisse**: Dokumentieren Sie die Ergebnisse jedes Testfalls und stellen Sie dem Kunden einen zusammenfassenden Bericht zur Verfügung.
* **Review-Meeting**: Führen Sie ein Review-Meeting durch, um die Testergebnisse und alle weiteren Schritte zu besprechen, die vor dem Go-live erforderlich sind.

### 7. Vorbereitung des Go-live

* **Auffrischungsschulung**: Bieten Sie bei Bedarf eine Auffrischungsschulung an.
* **Support-Plan**: Entwickeln Sie einen Support-Plan für die anfängliche Go-live-Phase, um einen reibungslosen Übergang zu gewährleisten.
