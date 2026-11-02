# Test: FTP-Importverbindung

#### Zweck

Diese Tests prüfen das Hinzufügen einer FTP-Importverbindung, den Verbindungstest, die Deaktivierung und Reaktivierung sowie die anschließende Bereinigung.

{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Testszenarien

1. **Vorbereitung:** FTP-Serverdaten und Zugangsdaten aus den Umgebungsvariablen laden.
2. **FTP-Verbindungstests:**

   **Neue Verbindung hinzufügen:**
   * `test_add_new_ftp_import_connection`: Eine FTP-Importverbindung mit den angegebenen Zugangsdaten und Serverinformationen hinzufügen.
   * **Erwartetes Ergebnis:** Die Verbindung wird erfolgreich angelegt.

   **Verbindung deaktivieren:**
   * `test_deactivate_ftp_import_connection`: Die neu angelegte FTP-Importverbindung deaktivieren.
   * **Erwartetes Ergebnis:** Die Verbindung wird erfolgreich deaktiviert.

   **Verbindung testen:**
   * `test_test_ftp_connection`: Prüfen, ob die FTP-Importverbindung den FTP-Server erreichen kann.
   * **Erwartetes Ergebnis:** Der Verbindungstest ist erfolgreich.

   **Verbindung in der Liste prüfen:**
   * `test_check_ftp_connection_in_list`: Prüfen, ob die neu angelegte FTP-Importverbindung in der Verbindungsliste enthalten ist.
   * **Erwartetes Ergebnis:** Die Verbindung wird in der Liste gefunden.

   **Deaktivierten Status prüfen:**
   * `test_check_ftp_connection_deactivated`: Prüfen, ob die Verbindung in der Liste als inaktiv markiert ist.
   * **Erwartetes Ergebnis:** Die Verbindung ist inaktiv.

   **Testordner hinzufügen:**
   * `test_add_test_folder_to_connection`: Der FTP-Importverbindung ein Standardverzeichnis als Testordner hinzufügen.
   * **Erwartetes Ergebnis:** Das Standardverzeichnis wird erfolgreich hinzugefügt.

   **Verbindung reaktivieren:**
   * `test_reactivate_ftp_import_connection`: Die zuvor deaktivierte FTP-Importverbindung reaktivieren.
   * **Erwartetes Ergebnis:** Die Verbindung wird erfolgreich reaktiviert.

   **Reaktivierten Status prüfen:**
   * `test_check_ftp_connection_reactivated`: Prüfen, ob die Verbindung in der Liste als aktiv markiert ist.
   * **Erwartetes Ergebnis:** Die Verbindung ist aktiv.

   **Bereinigung:**
   * `test_cleanup_ftp_import`: Die FTP-Importverbindung nach den Tests löschen.
   * **Erwartetes Ergebnis:** Die Verbindung wird erfolgreich gelöscht.

## Erläuterung der einzelnen Tests

* **Vorbereitung und Initialisierung:** Gemeinsame Testdaten vorbereiten.
* **Verbindung hinzufügen:** Eine FTP-Importverbindung mit den angegebenen Zugangsdaten und Serverinformationen anlegen.
* **Verbindung deaktivieren:** Die neue Verbindung deaktivieren.
* **Verbindung testen:** Die Erreichbarkeit des FTP-Servers über die Importverbindung prüfen.
* **Verbindungsliste prüfen:** Sicherstellen, dass die neue Verbindung in der Liste vorhanden ist.
* **Deaktivierung prüfen:** Sicherstellen, dass die Verbindung in der Liste als inaktiv markiert ist.
* **Testordner hinzufügen:** Der Verbindung ein Standardverzeichnis als Testordner hinzufügen.
* **Verbindung reaktivieren:** Die zuvor deaktivierte Verbindung wieder aktivieren.
* **Reaktivierung prüfen:** Sicherstellen, dass die Verbindung in der Liste als aktiv markiert ist.
* **Bereinigung:** Die FTP-Importverbindung nach den Tests löschen.
