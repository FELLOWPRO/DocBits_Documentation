# Rechnungsautomatisierungstests mit DocBits

## Übersicht

Dieses Dokument beschreibt den Testplan für die Rechnungsautomatisierung mit DocBits in Verbindung mit Infor LN oder M3. Es enthält Details zu Testfällen, Testvorbereitungen, Ausführungsschritten und Unterstützungsprozessen.

## Testfälle

| ID | Testfall                                                                              | Beschreibung                                                                                                                                                                            | Status    |
| -- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1  | Kostenrechnungen                                                                      | Rechnungen ohne Bestellung werden erfolgreich in DocBits verarbeitet und als „Kostenrechnung“ nach LN exportiert.                                                                       | ZU TESTEN |
| 2  | Bestellbezogene Rechnung mit perfekter Übereinstimmung                                | Bestellbezogene Rechnungen werden erfolgreich in DocBits verarbeitet, mit einer perfekten Übereinstimmung von Rechnung zu Bestellung, da Artikelnummer, Menge und Preis übereinstimmen. | ZU TESTEN |
| 3  | Bestellbezogene Rechnungen mit unterschiedlicher Menge                                | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung bei der Menge.                                                        | ZU TESTEN |
| 4  | Bestellbezogene Rechnungen mit unterschiedlichem Preis                                | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung beim Preis.                                                           | ZU TESTEN |
| 5  | Bestellbezogene Rechnungen mit unterschiedlicher oder nicht vorhandener Artikelnummer | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung oder eine nicht vorhandene Artikelnummer.                             | ZU TESTEN |
| 6  | Bestellbezogene Rechnungen mit einer Abweichung innerhalb der Toleranz                | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung bei Menge oder Preis, die jedoch innerhalb der Toleranz liegt.        | ZU TESTEN |
| 7  | Gutschriften                                                                          | Gutschriften werden erfolgreich in DocBits verarbeitet und nach LN exportiert. Klären Sie, ob Beträge mit einem positiven oder negativen Vorzeichen exportiert werden sollen.           | ZU TESTEN |

## Plan für Tests mit dem Kunden

### 1. Einrichtung

* **Erstes Treffen**: Planen Sie ein Kickoff-Meeting mit dem Kunden, um den Testprozess und die Ziele zu erläutern.
* **Zugriff und Berechtigungen**: Stellen Sie sicher, dass der Kunde alle notwendigen Zugriffe auf DocBits und Infor LN oder M3 für Testzwecke hat.

### 2. Testvorbereitung

* **Schulung**: Bieten Sie umfassende Schulungen für das Team des Kunden an, wie man DocBits zur Rechnungsverarbeitung verwendet.
* **Dokumentation**: Teilen Sie detaillierte Dokumentationen zu den Testverfahren, einschließlich der erwarteten Ergebnisse für jeden Testfall.

### 3. Ausführung der Testfälle

* **Testumgebung**: Richten Sie eine Testumgebung ein, die das Produktionssystem des Kunden so genau wie möglich nachbildet.
* **Schritt-für-Schritt-Tests**: Arbeiten Sie mit dem Kunden zusammen, um jeden Testfall auszuführen, und stellen Sie sicher, dass er jeden Schritt versteht:
  * Rechnungen über DocBits verarbeiten.
  * Die Ausgabe im Bestellabgleichsmodul überprüfen.
  * Die Exportergebnisse in LN oder M3 überprüfen.

### 4. Problemlösung

* **Verfolgung**: Verwenden Sie ein Verfolgungssystem (wie Jira oder eine einfache Tabelle), um alle Probleme oder Abweichungen zu protokollieren, die während der Tests auftreten.
* **Unterstützung**: Bieten Sie sofortige Unterstützung zur Lösung von Problemen und zur Klärung von Zweifeln.

### 5. Verifizierung und Feedback

* **Verifizierung**: Überprüfen Sie nach jedem Testfall die Ergebnisse mit dem Kunden, um die Genauigkeit sicherzustellen.
* **Feedback-Schleife**: Sammeln Sie Feedback vom Kunden zum Prozess und zu erforderlichen Verbesserungen.

### 6. Abschluss

* **Dokumentation der Ergebnisse**: Dokumentieren Sie die Ergebnisse jedes Testfalls und erstellen Sie einen zusammenfassenden Bericht für den Kunden.
* **Überprüfungstreffen**: Führen Sie ein Überprüfungstreffen durch, um die Testergebnisse und alle weiteren erforderlichen Schritte vor dem Live-Gang zu besprechen.

### 7. Vorbereitung auf den Live-Gang

* **Schulungserneuerung**: Bieten Sie bei Bedarf eine Auffrischungsschulung an.
* **Unterstützungsplan**: Entwickeln Sie einen Unterstützungsplan für die anfängliche Live-Phase, um einen reibungslosen Übergang zu gewährleisten.
