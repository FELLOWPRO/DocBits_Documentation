# Test: E-Mail-Import und -Verarbeitung

## Was wird getestet?

Diese Tests prüfen, ob der E-Mail-Import korrekt funktioniert. Die wichtigsten Ziele sind:

1. E-Mails mit Anhängen senden.
2. E-Mails empfangen und in bestimmte Ordner verschieben.
3. Prüfen, ob die E-Mails gelesen oder ungelesen sind.
4. E-Mails ins System importieren.
5. Anschließend E-Mails und importierte Dokumente entfernen.

## Testablauf

1. **Vorbereitung:**
   * E-Mail-Serverdaten und Zugangsdaten aus den Umgebungsvariablen laden.
   * Das E-Mail-Passwort sicher verschlüsseln.
2. **E-Mails senden und verwalten:**
   * Mit einer SMTP-Funktion E-Mails mit festgelegten Betreffzeilen und Anhängen senden.
   * Die E-Mails mit IMAP-Funktionen in den Zielordner verschieben.
   * Über die Ordnerliste prüfen, ob der Zielordner vorhanden ist.
   * E-Mails zum Aufräumen aus den Ordnern löschen.
   * Prüfen, ob die E-Mails als ungelesen oder gelesen markiert sind.
3. **Testsequenz:**

   **Initialisierung:**
   * Die Verbindung zum E-Mail-Server prüfen und die Verbindungs-ID abrufen.
   * Prüfen, ob die Anmeldung mit den gespeicherten Zugangsdaten funktioniert.
   * Prüfen, ob der Zielordner auf dem Server vorhanden ist.

   **E-Mail-Vorgänge:**
   * Drei Test-E-Mails mit jeweils eindeutigem Betreff senden.
   * Die IDs der gesendeten E-Mails aus dem Posteingang abrufen.
   * Die E-Mails aus dem Posteingang in den Zielordner verschieben.
   * Prüfen, ob die E-Mails im Zielordner als ungelesen markiert sind.

   **E-Mail-Import:**
   * Die E-Mails aus dem Zielordner ins System importieren.
   * Prüfen, ob die importierten E-Mails korrekt abgerufen und protokolliert wurden.

   **Protokollprüfung:**
   * Prüfen, ob die Betreffzeilen der gesendeten E-Mails in den Importprotokollen erfasst wurden.

   **Bereinigung:**
   * Die aus den E-Mails importierten Dokumente entfernen.
   * Die gesendeten und verschobenen E-Mails aus den Ordnern löschen.

### Erläuterung der einzelnen Tests

* **Vorbereitung und Initialisierung:** Gemeinsame Testdaten vorbereiten.
* **Verbindungstests:** Die Verbindung zum E-Mail-Server und den Abruf einer Verbindungs-ID prüfen. Sicherstellen, dass die Anmeldung funktioniert.
* **Ordnerprüfung:** Sicherstellen, dass der Zielordner vorhanden ist und die vom Server gelieferte Ordnerliste den Erwartungen entspricht.
* **Versand und ID-Abruf:** Drei E-Mails mit festgelegten Betreffzeilen und Anhängen senden. Ihre eindeutigen IDs aus dem Posteingang abrufen.
* **Verschieben und Statusprüfung:** Die Test-E-Mails in den Zielordner verschieben und anschließend ihren Ungelesen-Status prüfen.
* **Abruf und Antwortprüfung:** Die E-Mails aus dem Zielordner importieren und prüfen, ob die abgerufenen E-Mails mit den gesendeten übereinstimmen.
* **Importprotokoll prüfen:** Das Protokoll der importierten E-Mails abrufen und sicherstellen, dass die Betreffzeilen der Test-E-Mails darin vorkommen.
* **Bereinigung:** Die importierten Dokumente entfernen und die Test-E-Mails aus Posteingang und Zielordner löschen.
