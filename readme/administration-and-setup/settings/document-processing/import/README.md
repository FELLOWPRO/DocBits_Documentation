# Importieren

Die Importeinstellungen bestimmen, wie Dokumente verarbeitet werden, und ermöglichen den automatischen Empfang über FTP oder E-Mail. Öffnen Sie **Einstellungen → Dokumentverarbeitung → Importieren**.

## Dokumentoptionen

Prüfen Sie die maximale Seitenzahl, das standardmäßige Zahlungsziel in Tagen und das Datumsformat. Seiten oberhalb der eingestellten Grenze können verworfen werden. Für diese Funktion sind 60 Seiten als Standard dokumentiert; prüfen Sie vor dem Import die Einstellung Ihrer Organisation.

## FTP-Import

Sie benötigen einen kompatiblen FTP-Server, berechtigte Zugangsdaten und einen eigenen Importordner, auf den das Serverkonto zugreifen kann.

<figure><img src="../../../../.gitbook/assets/s150-ftp_0-de.png" alt="Deutsche Importübersicht für E-Mail- und FTP-Verbindungen."><figcaption><p>Deutsche Importübersicht für E-Mail- und FTP-Verbindungen.</p></figcaption></figure>

### Verbindung einrichten

Erstellen Sie eine Verbindung. Der Assistent beginnt mit der Serverkonfiguration; anschließend folgen die Optionen und die Importkonfiguration.

<figure><img src="../../../../.gitbook/assets/s150-ftp_5-de.png" alt="Serverkonfiguration im deutschen FTP-Importassistenten."><figcaption><p>Serverkonfiguration im deutschen FTP-Importassistenten.</p></figcaption></figure>

| Einstellung | Bedeutung |
| --- | --- |
| Protokoll und Port | Wählen Sie FTP, FTPS oder SFTP und den vom Serveradministrator bestätigten Port. |
| Server und Zugangsdaten | Serveradresse und ein Konto mit Leseberechtigung für den Importordner. |
| Dateinamenmuster | Beschränken den Import auf passende Dateinamen. |
| Unterorganisation | Bestimmt die Zuordnung der importierten Dokumente. |
| API-Schlüssel | Falls die Konfiguration einen Schlüssel verlangt, muss er zur richtigen Organisation gehören. Veröffentlichen Sie seinen Wert nicht. |
| Hauptordner und Importordner | Legen den Speicherort der Dateien auf dem Server fest. |
| Archivierung nach dem Import | Verschiebt erfolgreich importierte Dateien in den angegebenen Archivordner. Das Konto benötigt die entsprechenden Berechtigungen. |
| Unterordner einbeziehen | Erweitert die Suche auf untergeordnete Ordner. |

Prüfen Sie alle Schritte vor dem Speichern. Kontrollieren Sie anschließend gesondert, ob die Verbindung aktiv ist. Die verfügbaren Aktionen umfassen Verbindungstest, Protokolle, Aktivieren, Deaktivieren, Bearbeiten und Löschen. Prüfen Sie Testergebnis und Protokolle, bevor Sie den regelmäßigen Import starten. Die Bilder zeigen die Liste und den ersten Schritt des ungespeicherten Assistenten; sie belegen keine geprüfte Serververbindung.

## E-Mail-Import {#email-import}

Eine E-Mail-Verbindung holt Dokumente über IMAP oder Microsoft365 OAuth aus einem eigenen Postfach ab. Die Weiterleitung an eine von DocBits bereitgestellte Adresse ist ein anderer Importweg; siehe [Eingehende E-Mails](../module/inbound-emails.md).

### Unterstützte Anhänge

Importiert werden unter anderem `.pdf`, `.tiff` / `.tif`, `.eml`, `.dat`, `.xml`, `.edi` und `.purchaseorder`.

Zusätzlich zum vom Mailserver gemeldeten Dateityp erkennt DocBits Dokumente anhand ihres tatsächlichen Inhalts. Das ist relevant, wenn ein weitergeleiteter Anhang den allgemeinen Typ `application/octet-stream` statt `application/pdf` oder `application/xml` erhält.

* Weitergeleitete `.eml`-Nachrichten und Outlook-Anhänge vom Typ `winmail.dat` (TNEF) werden entpackt, um die enthaltenen Dokumente zu importieren.
* XML mit einem allgemeinen Dateityp wird anhand der Deklaration `<?xml` erkannt; ein vorangestelltes UTF-8- oder UTF-16-BOM (LE/BE) wird berücksichtigt. Derzeit werden nur diese BOM-Kodierungen automatisch anhand des Inhalts erkannt. Mit der Dateiendung `.xml` ist der Import unabhängig von der Kodierung möglich.
* Eingebettete Bilder wie Signaturlogos und PNG-, JPG-, GIF- oder BMP-Grafiken werden ignoriert und zählen nicht als fehlgeschlagene Importe.
* Ist für die Eingangsadresse die Antwort bei Importfehlern aktiviert, geht die Benachrichtigung an die konfigurierte Antwortadresse.

### IMAP-Verbindung

Erstellen Sie im Bereich E-Mail-Import eine Verbindung und wählen Sie IMAP. Prüfen Sie SSL- oder TLS-Verschlüsselung, Server, Port, Konfigurations- beziehungsweise Benutzernamen, E-Mail-Adresse und Passwort. Wählen Sie die Unterorganisation und die Adresse für Fehlermeldungen. Falls ein API-Schlüssel angezeigt wird, prüfen Sie den Organisationskontext.

Nach dem Erstellen der Verbindung können Sie den Postfachordner und das Verschieben verarbeiteter Nachrichten in einen anderen Ordner festlegen. Falls diese Optionen noch fehlen, bearbeiten Sie die gespeicherte Verbindung. Je nach Konfiguration lassen sich auch Dokumentanhänge zusammenführen, Empfangsbestätigungen an den Absender senden und doppelte Dateinamen blockieren. Prüfen Sie Betreff und Nachricht einer Bestätigung vor deren Aktivierung.

Speichern und Aktivieren sind getrennte Aktionen. Das Menü kann Verbindungstest, Verbindungs- und Importprotokolle, Bearbeiten, Aktivieren, Deaktivieren und Löschen anbieten.

### OAuth Office365

Erstellen Sie eine E-Mail-Verbindung und wählen Sie OAuth Office365. Starten Sie die Microsoft-Authentifizierung. Falls ein Gerätecode angezeigt wird, übernehmen Sie den DocBits-Code auf die angegebene Microsoft-Seite und melden Sie sich mit dem richtigen Konto an. Kehren Sie anschließend zu DocBits zurück und schließen Sie die Authentifizierung ab.

Prüfen Sie Unterorganisation, Ordner, optionales freigegebenes Postfach, Zielordner für verarbeitete Nachrichten und die Adresse für Fehlermeldungen. Kontrollieren Sie gegebenenfalls auch die Übergabe an DocBits oder AI Workforce. Speichern Sie die Konfiguration und legen Sie fest, wann die Verbindung aktiviert beziehungsweise der Import gestartet wird. OAuth Office365 – Tenant benötigt die Daten der Anwendungsregistrierung Ihrer Organisation; stimmen Sie diese mit dem Administrator ab und beachten Sie [Eingehende E-Mails](../module/inbound-emails.md).

### Importprotokolle

Verbindungsprotokolle helfen bei Kommunikationsproblemen; Importprotokolle zeigen bisherige Ergebnisse. Das zusammengefasste Protokoll im E-Mail-Bereich umfasst die eingerichteten Verbindungen. Sie können nach Betreff oder Absender filtern, über Spaltenüberschriften sortieren und die Spaltenreihenfolge ändern. Prüfen Sie die Meldung, bevor Sie einen Import wiederholen.


## Videoanleitung: E-Mail-Import einrichten und Fehler gezielt finden

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/de.mp4" %}
E-Mail-Import einrichten und Fehler gezielt finden
{% endembed %}

[Mit Untertiteln und Kapiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/de.html)

Einzelne native Produktbeschriftungen können abweichend übersetzt sein. Technische Feld-IDs bleiben erhalten.

Unter Einstellungen und Import verwende ich in diesem Beispiel die eingehende DocBits-Adresse. Ein direkt angebundenes Postfach ist ein eigener Importweg. Für die Schulung arbeite ich in einer eigenen Demoorganisation mit synthetischen Rechnungen. Benachrichtigungen bleiben ausgeschaltet.

Ich kontrolliere zuerst die angezeigte Empfangsadresse und den Geltungsbereich. Die Adresse gehört genau zu dieser Organisation und ihrer Umgebung. Für ein anderes Unternehmen oder eine produktive Umgebung übernehme ich immer die dort tatsächlich angezeigte Adresse.

Hier beschränke ich den Eingang auf unseren freigegebenen Testabsender. Die Zuordnung zu einer Unterorganisation wähle ich nur, wenn sie zum vorgesehenen Prozess gehört. Ich speichere die Einstellung und öffne sie erneut. Der erlaubte Absender ist erhalten geblieben; automatische Antwortmails sind in dieser Schulung weiterhin ausgeschaltet.

<figure><img src="../../../../.gitbook/assets/admin-save-de-accounting-email-v2.png" alt="Erlaubter Absender gespeichert, Benachrichtigungen ausgeschaltet"><figcaption><p>Erlaubter Absender gespeichert, Benachrichtigungen ausgeschaltet</p></figcaption></figure>

Für die Schulung wurde ein Testeingang direkt an die DocBits-Eingangsverarbeitung übergeben. Dieser Test bestätigt keine externe Mailzustellung. Im Protokoll prüfe ich den passenden Betreff, den Absender und den importierten Anhang. Erst der tatsächlich angelegte Beleg zeigt, dass der Eingang weiterverarbeitet wurde.

Ich öffne den zugehörigen Beleg und vergleiche den PDF-Anhang mit der Rechnung in DocBits. Dateiname, Rechnungsnummer, Lieferant und Betrag müssen übereinstimmen. Ein erfolgreicher Import sagt noch nichts über eine Freigabe oder eine ERP-Buchung aus.

Ein zweiter kontrollierter Test stammt von einem nicht zugelassenen Absender. Im Protokoll suche ich gezielt nach diesem Eingang und aktiviere den Fehlerfilter. Die Details nennen den abgelehnten Absender. Ich prüfe die Ursache anhand des Betreffs und der Vorgangskennung, statt den Import mehrfach anzustoßen.

Bei einem echten Fall kläre ich zuerst, ob dieser Absender überhaupt berechtigt ist. Eine erlaubte Änderung an der Absenderliste wird gespeichert und erneut geprüft. Anschließend kontrolliere ich einen neuen eindeutigen Testeingang bis zum angelegten Dokument. Für technische Fehler übergebe ich die Vorgangskennung und die konkrete Fehlermeldung.

<figure><img src="../../../../.gitbook/assets/admin-error-de-accounting-email-v2.png" alt="Fehlgeschlagener Import mit Anhang, Ursache und Vorgangskennung"><figcaption><p>Fehlgeschlagener Import mit Anhang, Ursache und Vorgangskennung</p></figcaption></figure>
