# Import

## Überblick

In den Einstellungen für den **Import** können Sie dokumentenspezifische Optionen für den Import konfigurieren oder automatische Importe über FTP oder E-Mail einrichten. Diese Seite bietet einen detaillierten Überblick über alle verfügbaren Einstellungen.

## Zugriff

1.  Navigieren Sie zu **Einstellungen** -> **Dokumentenverarbeitung** -> **Import**

    <figure><img src="../../../.gitbook/assets/ftp_0_es.png" alt=""><figcaption></figcaption></figure>

## **Seitenbeschränkung beim Dokumentenimport**

* **Auf Seiten beschränken**: Mit dieser Einstellung können Sie die Verarbeitung auf eine bestimmte Anzahl von Seiten pro Dokument begrenzen. Der Standardwert beträgt **60 Seiten**, das heißt, Dokumente, die dieses Limit überschreiten, werden auf **60 Seiten** gekürzt, und alle **übrigen Seiten werden verworfen.**
* **Zahlungsbedingungen Tage**: Legt die standardmäßigen Zahlungsbedingungen (in Tagen) fest, die auf die Dokumente angewendet werden können.
* **Datumsmuster**: Legt das Muster dafür fest, wie Daten innerhalb der importierten Dokumente erkannt und formatiert werden sollen.

<figure><img src="../../../.gitbook/assets/document_settins_1_es.png" alt=""><figcaption></figcaption></figure>

## **FTP-Import**

### Voraussetzungen

Um FTP zum automatischen Datenimport zu verwenden, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

* Korrekt konfigurierter und Linux-kompatibler FTP-Server
* FTP-Hostname, Benutzername und Passwort
* Dediziertes Importverzeichnis

### Neue Verbindung hinzufügen

1.  Um eine neue Verbindung hinzuzufügen, klicken Sie auf die Schaltfläche **Hinzufügen** im FTP-Bereich.

    <figure><img src="../../../.gitbook/assets/ftp_7_es.png" alt=""><figcaption></figcaption></figure>
2.  Geben Sie Ihre FTP-Zugangsdaten in die dafür vorgesehenen Felder ein. Das Feld API-Schlüssel wird automatisch ausgefüllt.

    * **Typ:** Gibt das zu verwendende FTP-Protokoll an. Sie können zwischen **FTP**, **FTPS** oder **SFTP** wählen.
    * **Port:** Gibt die Portnummer an, die für das ausgewählte FTP-Protokoll verwendet werden soll.
    * **Servername (erforderlich):** Die Adresse des Servers, von dem die Dokumente abgerufen werden.
    * **Benutzername (erforderlich):** Der Anmeldename, der für den Zugriff auf den FTP-Server verwendet wird.
    * **Passwort (erforderlich):** Das Passwort, das mit dem Benutzernamen für den Zugriff auf den FTP-Server verknüpft ist.
    * **Muster für die Dateinamenübereinstimmung:** Um anhand der Dateinamen anzugeben, welche Dateien importiert werden sollen.
    * **Suborganisationen:** Wählen Sie aus, auf welche Suborganisation der FTP-Import angewendet werden soll.
    * **API-Schlüssel (erforderlich):** Dieses Feld wird automatisch auf Grundlage der Organisation ausgefüllt, in der Sie angemeldet sind.
    * **Hauptverzeichnis:** Gibt das Verzeichnis auf dem FTP-Server an, aus dem die Dateien importiert werden.
    * **Importverzeichnis:** Ermöglicht es Ihnen, ein Unterverzeichnis innerhalb des Hauptverzeichnisses anzugeben, aus dem die Dateien importiert werden.
    * **Nach dem Import archivieren:** Ermöglicht es Ihnen, Dateien nach dem Import zu archivieren. Sobald diese Option aktiviert ist, können Sie das Verzeichnis angeben, in das die Dateien nach einem erfolgreichen Import verschoben werden sollen.
    * **Dateien aus Unterordnern einbeziehen:** Wenn diese Option aktiviert ist, wird auch in Unterverzeichnissen innerhalb des Hauptverzeichnisses nach Dateien gesucht.

    <figure><img src="../../../.gitbook/assets/ftp_4_es.png" alt=""><figcaption></figcaption></figure>
3. Sobald Sie alle erforderlichen Angaben zu Ihrem FTP eingegeben haben, klicken Sie auf **Speichern**.
4. Nachdem Sie Ihre Verbindung gespeichert haben, können Sie sie aktivieren, indem Sie auf die drei Punkte in der Spalte **Aktion** Ihrer Verbindung klicken und dann **Aktivieren** auswählen.

### Aktionen für FTP

Sie können auf die drei Punkte in der Spalte **Aktion** klicken, um auf die folgenden Optionen für Ihre Verbindung zuzugreifen:

<figure><img src="../../../.gitbook/assets/ftp_5_es.png" alt="" width="184"><figcaption></figcaption></figure>

* **Verbindung testen:** Testet die Verbindung zu Ihrem FTP-Server.
* **Verbindungsprotokolle:** Öffnet die Protokolle Ihrer FTP-Verbindung, einschließlich Fehlermeldungen, falls Probleme auftreten.
* **Aktivieren/Deaktivieren:** Aktiviert/deaktiviert Ihre Verbindung.
* **Bearbeiten:** Ermöglicht es Ihnen, Änderungen an Ihrer Verbindung vorzunehmen.
* **Löschen:** Entfernt Ihre Verbindung.

## **E-Mail-Import**

Sie können einen E-Mail-Import einrichten, der Dokumente automatisch aus Ihrem Posteingang importiert, sobald sie eintreffen. Sie können wählen, ob Sie eine IMAP-Verbindung oder eine OAuth-Verbindung einrichten möchten.

<mark style="color:red;">**Hinweis**</mark>: Es werden nur Dokumente mit den folgenden Dateitypen importiert:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

### Neue IMAP-Verbindung hinzufügen

1.  Um eine neue IMAP-Verbindung hinzuzufügen, klicken Sie auf die Schaltfläche **Hinzufügen** im Bereich **E-Mail-Import**.

    <figure><img src="../../../.gitbook/assets/email_1_es.png" alt=""><figcaption></figcaption></figure>
2. Wählen Sie IMAP als Protokoll aus.
3. Geben Sie Ihre E-Mail-Zugangsdaten in die dafür vorgesehenen Felder ein. Das Feld API-Schlüssel wird automatisch ausgefüllt.
   * **Verschlüsselung:** Wählen Sie den zu verwendenden Verschlüsselungstyp aus — entweder **SSL** oder **TLS**.
   * **Servername:** Die Adresse des E-Mail-Servers.
   * **Benutzername:** Die Kennung, die für Ihre E-Mail-Importkonfiguration in DocBits verwendet wird.
   * **E-Mail:** Die E-Mail-Adresse, die zum Importieren von Dokumenten in das System verwendet wird.
   * **Passwort:** Das Passwort, das mit der angegebenen E-Mail-Adresse verknüpft ist.
   * **Suborganisationen:** Wählen Sie die Suborganisation aus, auf die der E-Mail-Import angewendet werden soll.
   * **API-Schlüssel:** Dieses Feld wird automatisch auf Grundlage der Organisation ausgefüllt, in der Sie angemeldet sind.
   * **Importfehlermeldung an diese E-Mail-Adresse senden:** Geben Sie eine E-Mail-Adresse an, um Fehlerbenachrichtigungen zu erhalten, falls während des Importvorgangs etwas schiefgeht.
   * **Port:** Gibt die Portnummer an, die für die ausgewählte E-Mail-Importkonfiguration verwendet werden soll.
   * **Ordner:** Wählen Sie einen Ordner aus, aus dem die Dokumente importiert werden.\
     <mark style="color:red;">**Hinweis**</mark>: Die Option **Ordner** wird erst verfügbar, nachdem Sie erfolgreich eine IMAP-Verbindung erstellt haben. Um nach der Erstellung einen Ordner hinzuzufügen, klicken Sie auf die drei Punkte in der Spalte **Aktion** und wählen dann **Bearbeiten** aus. Die Option sollte nun verfügbar sein.
   * **E-Mails in einen anderen Ordner verschieben:** Wenn diese Option aktiviert ist, können Sie einen Ordner angeben, in den die E-Mails nach einem erfolgreichen Import verschoben werden.\
     <mark style="color:red;">**Hinweis**</mark>: Die Option **E-Mails in einen anderen Ordner verschieben** wird erst verfügbar, nachdem Sie erfolgreich eine IMAP-Verbindung erstellt haben. Um diese Einstellung zu aktivieren, klicken Sie auf die drei Punkte in der Spalte **Aktion** und wählen dann **Bearbeiten** aus. Die Option sollte nun verfügbar sein.
   * **Angehängte Dokumente zusammenführen:** Kombiniert mehrere angehängte Dokumente zu einem einzigen Dokument.
   * **E-Mail nach dem Import an den Absender senden:** Sendet eine Bestätigungs-E-Mail an den ursprünglichen Absender, nachdem der Import abgeschlossen ist. Sobald diese Option aktiviert ist, können Sie den Betreff und den Text der E-Mail angeben.
   * **Import von doppelten Dateinamen blockieren:** Verhindert den Import, wenn bereits ein Dokument mit demselben Namen existiert.
4. Nachdem Sie Ihre Verbindung gespeichert haben, können Sie sie aktivieren, indem Sie auf die drei Punkte in der Spalte **Aktion** Ihrer Verbindung klicken und dann **Aktivieren** auswählen.

### Aktionen für IMAP

Sie können auf die drei Punkte in der Spalte **Aktion** klicken, um auf die folgenden Optionen für Ihre Verbindung zuzugreifen:

<figure><img src="../../../.gitbook/assets/email_7_es.png" alt="" width="190"><figcaption></figcaption></figure>

* **Verbindung testen:** Testet die Verbindung zu Ihrem IMAP-Client.
* **Verbindungsprotokolle:** Öffnet die Protokolle Ihrer E-Mail-Verbindung, einschließlich aller Fehlermeldungen, die während des Vorgangs auftreten.
* **Importprotokoll:** Öffnet die Protokolle vergangener Importe für die jeweilige Verbindung, einschließlich aller Fehlermeldungen, die während des Vorgangs aufgetreten sind.
* **Aktivieren/Deaktivieren:** Aktiviert/deaktiviert Ihre Verbindung.
* **Bearbeiten:** Ermöglicht es Ihnen, Änderungen an Ihrer Verbindung vorzunehmen.
* **Löschen:** Entfernt Ihre Verbindung.

### Neue OAuth-Office365-Verbindung hinzufügen

1.  Um eine neue OAuth-Office365-Verbindung hinzuzufügen, klicken Sie auf die Schaltfläche **Hinzufügen** im Bereich **E-Mail-Import**.

    <figure><img src="../../../.gitbook/assets/email_1_es.png" alt=""><figcaption></figcaption></figure>
2.  Wählen Sie **OAuth Office365** als Protokoll aus und klicken Sie dann auf **Authentifizieren**.

    <figure><img src="../../../.gitbook/assets/email_3_es.png" alt=""><figcaption></figcaption></figure>
3.  Sie werden zu einer Microsoft-Seite weitergeleitet, auf der Sie aufgefordert werden, einen Code einzugeben. Um diesen Code abzurufen, kehren Sie zu DocBits zurück — der Code wird dort angezeigt, wie unten dargestellt. Kopieren Sie den Code und geben Sie ihn auf der Microsoft-Seite ein. Anschließend werden Sie aufgefordert, Ihre Microsoft-Zugangsdaten einzugeben.

    <figure><img src="../../../.gitbook/assets/email_4_es.png" alt=""><figcaption></figcaption></figure>
4. Folgen Sie den Schritten auf der Microsoft-Seite. Sobald Sie fertig sind, kehren Sie zu DocBits zurück und klicken auf **Authentifizierung abschließen**.
5.  Nun können Sie die folgenden Einstellungen konfigurieren:

    * **Suborganisationen:** Wählen Sie die Suborganisation aus, auf die der E-Mail-Import angewendet werden soll.
    * **Ordner verwenden:** Wählen Sie einen Ordner aus, aus dem die Dokumente importiert werden.
    * **Gemeinsames Postfach verwenden:** Geben Sie die gemeinsame E-Mail-Adresse an, aus der die Dokumente importiert werden sollen.
    * **E-Mail in einen anderen Ordner verschieben:** Geben Sie einen Ordner an, in den die E-Mails nach einem erfolgreichen Import verschoben werden sollen.
    * **Importfehlermeldung an diese E-Mail-Adresse senden:** Geben Sie eine E-Mail-Adresse an, um Fehlerbenachrichtigungen zu erhalten, falls während des Importvorgangs etwas schiefgeht.

    <figure><img src="../../../.gitbook/assets/email_5_es.png" alt=""><figcaption></figcaption></figure>
6. Sobald Sie das gewünschte Verhalten konfiguriert haben, können Sie den Import von E-Mails durch Klicken auf **Importieren** starten oder Ihre Änderungen durch Klicken auf **Speichern** sichern.
7. Nachdem Sie Ihre Verbindung gespeichert haben, können Sie sie aktivieren, indem Sie auf die drei Punkte in der Spalte **Aktion** Ihrer Verbindung klicken und dann **Aktivieren** auswählen.

### Aktionen für OAuth Office365

Sie können auf die drei Punkte in der Spalte **Aktion** klicken, um auf die folgenden Optionen für Ihre Verbindung zuzugreifen:

<figure><img src="../../../.gitbook/assets/email_6_es.png" alt="" width="189"><figcaption></figcaption></figure>

* **Verbindungsprotokolle:** Öffnet die Protokolle Ihrer E-Mail-Verbindung, einschließlich aller Fehlermeldungen, die während des Vorgangs auftreten.
* **Importprotokoll:** Öffnet die Protokolle vergangener Importe für die jeweilige Verbindung, einschließlich aller Fehlermeldungen, die während des Vorgangs aufgetreten sind.
* **Aktivieren/Deaktivieren:** Aktiviert/deaktiviert Ihre Verbindung.
* **Bearbeiten:** Ermöglicht es Ihnen, Änderungen an Ihrer Verbindung vorzunehmen.
* **Löschen:** Entfernt Ihre Verbindung.

### Importprotokoll

Sie können das Importprotokoll aller erstellten E-Mail-Verbindungen einsehen, einschließlich aller Fehlermeldungen, die während des Vorgangs aufgetreten sind, indem Sie auf die Schaltfläche **Importprotokoll** in der oberen rechten Ecke des Bereichs E-Mail-Import klicken.

<figure><img src="../../../.gitbook/assets/email_8_es.png" alt=""><figcaption></figcaption></figure>

Sie können die Protokolle nach Betreff oder Absender filtern, Spalten in auf- oder absteigender Reihenfolge sortieren, indem Sie auf die Spaltenüberschriften klicken, und Spalten per Ziehen und Ablegen neu anordnen.
