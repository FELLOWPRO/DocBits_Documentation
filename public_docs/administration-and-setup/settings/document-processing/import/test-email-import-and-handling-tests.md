# Test: E-Mail-Import und -Verarbeitung

## Zweck

Diese Tests prüfen den E-Mail-Import: E-Mails senden, empfangen und in bestimmte Ordner verschieben, den Gelesen-/Ungelesen-Status prüfen, E-Mails ins System importieren und die Testdaten anschließend entfernen.

## Testablauf

1. **Vorbereitung:**
   * **Umgebungseinstellungen laden:** E-Mail-Serverdaten und Zugangsdaten aus den Umgebungsvariablen laden.
   * **E-Mail-Passwort verschlüsseln:** Das Passwort für die sichere Verwendung verschlüsseln.
2. **E-Mail senden und verwalten:**
   * **E-Mail senden:** Mit einer SMTP-Funktion eine E-Mail mit festgelegtem Betreff und Anhang senden.
   * **E-Mail verschieben:** Die E-Mail mit IMAP-Funktionen in den Zielordner verschieben.
   * **Ordner auflisten:** Prüfen, ob der Zielordner vorhanden ist.
   * **E-Mail löschen:** Die E-Mail zum Aufräumen aus dem Ordner löschen.
   * **Status prüfen:** Prüfen, ob die E-Mail als gelesen oder ungelesen markiert ist.
3. **Testsequenz:**

   **Initialisierung:**
   * Die Verbindung zum E-Mail-Server prüfen und die Verbindungs-ID abrufen.
   * Prüfen, ob die Anmeldung mit den gespeicherten Zugangsdaten funktioniert.
   * Prüfen, ob der Zielordner auf dem Server vorhanden ist.

   **E-Mail-Vorgänge:**
   * Eine Test-E-Mail mit festgelegtem Betreff senden.
   * Die ID der gesendeten E-Mail aus dem Posteingang abrufen.
   * Die E-Mail aus dem Posteingang in den Zielordner verschieben.
   * Prüfen, ob die E-Mail im Zielordner als ungelesen markiert ist.

   **E-Mail-Import:**
   * Die E-Mail aus dem Zielordner ins System importieren.
   * Prüfen, ob die importierte E-Mail korrekt abgerufen und protokolliert wurde.

   **Protokollprüfung:**
   * Prüfen, ob der Betreff der gesendeten E-Mail im Importprotokoll erfasst wurde.

   **Bereinigung:**
   * Das aus der E-Mail importierte Dokument entfernen.
   * Die gesendete und verschobene E-Mail aus den Ordnern löschen.

## Erläuterung der einzelnen Tests

* **Vorbereitung und Initialisierung:** Gemeinsame Testdaten vorbereiten.
* **Verbindungstests:** Die Verbindung zum E-Mail-Server und den Abruf einer Verbindungs-ID prüfen. Sicherstellen, dass die Anmeldung funktioniert.
* **Ordnerprüfung:** Sicherstellen, dass der Zielordner vorhanden ist und die vom Server gelieferte Ordnerliste den Erwartungen entspricht.
* **Versand und ID-Abruf:** Eine E-Mail mit festgelegtem Betreff und Anhang senden. Ihre eindeutige ID aus dem Posteingang abrufen.
* **Verschieben und Statusprüfung:** Die Test-E-Mail in den Zielordner verschieben und anschließend ihren Ungelesen-Status prüfen.
* **Abruf und Antwortprüfung:** Die E-Mail aus dem Zielordner importieren und prüfen, ob sie in der Antwort enthalten ist.
* **Importprotokoll prüfen:** Das Protokoll der importierten E-Mails abrufen und sicherstellen, dass der Betreff der Test-E-Mail darin vorkommt.
* **Bereinigung:** Das importierte Dokument entfernen und die Test-E-Mail aus Posteingang und Zielordner löschen.
