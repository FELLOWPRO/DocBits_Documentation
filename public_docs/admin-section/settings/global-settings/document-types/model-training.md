# Model Training

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.07.01.png" alt=""><figcaption></figcaption></figure>

#### Übersicht

Das Modelltraining ermöglicht es Administratoren, das Training von maschinellen Lernmodellen spezifisch für jeden Dokumententyp zu überwachen und zu verwalten. Indem Docbits eine strukturierte Benutzeroberfläche für den Import von Beispieldaten, das Training von Modellen und das Testen ihrer Leistung bereitstellt, stellt es sicher, dass seine Datenextraktionsfähigkeiten kontinuierlich verbessert werden.

#### Hauptfunktionen und Optionen

1. **Metrikenübersicht**:

* **Beispiel**: Anzahl der Beispieldokumente, die für das Training verwendet wurden.
* **Exportiert**: Anzahl der Dokumente, die nach der Verarbeitung erfolgreich exportiert wurden.
* **Unternehmen Σ**: Gesamtanzahl der unternehmensspezifischen verarbeiteten Dokumente.
* **Insgesamt Σ**: Gesamtanzahl der verarbeiteten Dokumente in allen Kategorien.

2. **Trainings- und Testoptionen**:

* **Importieren**: Ermöglicht es Administratoren, neue Trainingsdatensätze zu importieren, die in der Regel strukturierte Beispiele von Dokumenten sind, die vom System erkannt werden sollen.
* **Modell trainieren**: Startet den Schulungsprozess unter Verwendung der importierten Daten, um die Erkennungs- und Extraktionsfähigkeiten des Systems zu verbessern.
* **Klassifizierung testen**: Ermöglicht das Testen des Modells, um seine Leistung bei der Klassifizierung und Extraktion von Daten aus neuen oder unbekannten Dokumenten zu bewerten.

3. **Aktionsbuttons**:

* **Feld erstellen**: Neue Datenfelder hinzufügen, die das Modell erkennen und extrahieren soll.
* **Aktionen**: Dieses Dropdown-Menü kann Optionen wie Details anzeigen, Konfigurationen bearbeiten oder Trainingsdaten löschen enthalten.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2496" %}
