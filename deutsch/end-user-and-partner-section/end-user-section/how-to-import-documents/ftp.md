---
hidden: true
noIndex: true
---

# FTP

Wenn Sie Ihren SFTP mit DocBits integrieren möchten, um Dokumente zu importieren.

Voraussetzungen

* Korrekt konfigurierter, Linux-kompatibler SFTP-Server
* SFTP-Hostname, Benutzername und Passwort
* Dedizierter Import-Ordner

**Import-Konfiguration**

Öffnen Sie im Dashboard die Einstellungen und navigieren Sie zu „Import". Wählen Sie unter „FTP-Import" die Option, eine neue Konfiguration hinzuzufügen.

<figure><img src="../../../.gitbook/assets/ftp1.png" alt="Add New FTP Configuration"><figcaption></figcaption></figure>

Geben Sie die SFTP-Anmeldedaten in die vorgesehenen Felder ein und wählen Sie „Speichern" (das Feld „API-Schlüssel" wird automatisch mit dem API-Schlüssel der Umgebung gefüllt, in der Sie arbeiten).

<figure><img src="../../../.gitbook/assets/ftp_import_configuration_form.png" alt="FTP Import Configuration Form"><figcaption></figcaption></figure>

Sobald Sie alle erforderlichen Details Ihres SFTP eingegeben haben, klicken Sie auf SPEICHERN.

### **FTP-Dateiarchivierung**

1. **Dateiarchivierung aktivieren**
   * Suchen Sie die Option „Dateiarchivierung".
   * Schalten Sie den Schalter in die Position „Ein", um die Archivierung zu aktivieren.
2. **Archivverzeichnis auswählen**
   * Sobald der Schalter „Dateiarchivierung" aktiviert ist, erscheint ein Feld, in dem Sie den Verzeichnispfad für archivierte Dateien angeben können.
   * Wählen Sie den gewünschten Ordnerpfad auf dem SFTP-/FTP-Server aus, in dem die archivierten Dateien gespeichert werden sollen.
3. **Änderungen speichern**
   * Klicken Sie auf die Schaltfläche **Speichern**, um die Änderungen zu übernehmen.

<figure><img src="../../../.gitbook/assets/ftp_file_archiving_settings.png" alt="FTP File Archiving Settings"><figcaption></figcaption></figure>
