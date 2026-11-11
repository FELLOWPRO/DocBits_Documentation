# Importieren

## Überblick

Zum Erstellen einer Verbindung ist ein Administratorkonto erforderlich. Mit **Import** konfigurieren Sie den automatischen Dokumentimport von einem FTP/SFTP-Server, aus einem angebundenen Postfach oder über die eingehende DocBits-E-Mail-Adresse. Prüfen Sie die aktuelle Organisation und Umgebung, bevor Sie Verbindungsdaten eingeben.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-de-20261109.png" alt="Importseite mit dem Diagramm Import Pipeline, der Liste FTP Import mit der Schaltfläche New und der Liste Email Import mit der Schaltfläche New"><figcaption><p>Die Seite Import: das schreibgeschützte Diagramm Import Pipeline, die Liste FTP Import und die Liste Email Import, jeweils mit eigener Schaltfläche <strong>New</strong>.</p></figcaption></figure>

## Zugriff

1. Navigieren Sie zu **Settings** → **Document Processing** → **Import**.
2. Klappen Sie den gewünschten Bereich auf. **FTP Import** und **Email Import** haben jeweils eine eigene Schaltfläche **New**.

## **Document Settings**

Die aktuelle Seite Import enthält **Import Pipeline**, **FTP Import**, **Email Import** und, sofern aktiviert, **Inbound Emails**. Das Kürzen von Seiten, standardmäßige Zahlungsbedingungen und Datumsmusterfelder sind in dieser Import-Ansicht keine Bedienelemente.

**Import Pipeline** zeigt die FTP/SFTP-Routing-Topologie einschließlich Quell- und Zielregionen. Prüfen Sie jeden angezeigten Hinweis, bevor Sie eine Verbindung ändern. Der Pipeline-Reiter **Email** zeigt derzeit eine Meldung, dass die Funktion folgt; ein Diagramm zur E-Mail-Verarbeitung wird nicht angezeigt.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tabelle FTP Import mit der Schaltfläche New und Spalten für Typ, Server, Benutzername, Port, Unterorganisation und Verzeichnis"><figcaption><p>Mit New in FTP Import fügen Sie eine Serververbindung hinzu. Bestehende Verbindungszeilen sind in diesem Beispiel unkenntlich gemacht.</p></figcaption></figure>

### Voraussetzungen

* Ein FTP-, FTPS- oder SFTP-Server, der vom Importdienst erreichbar ist.
* Die von Ihrem Administrator bereitgestellte Serveradresse, das Protokoll, der Port, der Benutzername und das Passwort.
* Ein Importverzeichnis und, falls eine Archivierung erforderlich ist, ein freigegebenes Archivverzeichnis.

### Neue Verbindung hinzufügen

1. Klicken Sie in **FTP Import** auf **New**.
2. Geben Sie die Verbindungseinstellungen ein. Ein neues Formular startet mit **SFTP** und Port **22**; ersetzen Sie diese Werte, wenn Ihr Server ein anderes Protokoll oder einen anderen Port verwendet.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Neues FTP-Verbindungsformular mit SFTP, Port 22, Verzeichnisfeldern, Wiederholungseinstellungen sowie Save und Cancel"><figcaption><p>Geben Sie Server- und Anmeldedaten ein und prüfen Sie anschließend Verzeichnisse, Routing und Wiederholungseinstellungen. Passwort- und API-Key-Felder sind unkenntlich gemacht; dieses Beispiel wurde nicht gespeichert.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** und **Password** identifizieren und authentifizieren die Serververbindung.
* **Primary Directory** legt das Basisverzeichnis fest. **Import Directory** wählt den zu verarbeitenden Ordner; die Ordnerauswahl wird verfügbar, nachdem die Verbindung gespeichert wurde.
* **Document Type** und **Sub-Organizations** steuern die Zuordnung. **File name matching patterns** begrenzt, welche Dateinamen berücksichtigt werden.
* **Archive after Import** ermöglicht das Verschieben verarbeiteter Dateien in das angegebene Archivverzeichnis. **Include Subfolder Files** erweitert die Verarbeitung auf Unterordner.
* **Retry interval (min)**, **Retry duration (hours)** und **Notification emails (comma-separated)** steuern Wiederholungs- und Benachrichtigungsverhalten. Die dargestellten Standardwerte sind 60 Minuten und 48 Stunden.
* **API Key** verwendet den vorhandenen App-Subscription-Schlüssel der Organisation. Das Augensymbol zeigt diesen Schlüssel an oder blendet ihn aus; das Kopiersymbol kopiert ihn in die Zwischenablage. Diese Bedienelemente erzeugen keinen neuen Schlüssel. Behandeln Sie den Schlüssel vertraulich; nehmen Sie ihn nicht in Screenshots oder Supportnachrichten auf.

Mit **Cancel** oder dem Schließen-Symbol verlassen Sie ein neues Verbindungsformular, ohne es zu speichern.

3. Prüfen Sie die Werte und klicken Sie auf **Save**, wenn die Verbindung erstellt werden kann.
4. Wählen Sie im Menü **Actions** der gespeicherten Zeile **Activate**, wenn Importe ausgeführt werden dürfen.

### Aktionen für FTP

Das Menü **Actions** der gespeicherten Verbindung bietet:

* **Test Connection**: kontaktiert den konfigurierten Server, um die Verbindung zu prüfen.
* **Connection Logs**: zeigt Verbindungsversuche und Fehler.
* **Activate/Deactivate**: aktiviert oder stoppt die automatische Verarbeitung für diese Verbindung.
* **Edit**: ändert die Konfiguration.
* **Delete**: entfernt die Verbindung.

Testen, Aktivieren, Bearbeiten und Löschen wirken auf eine echte Verbindung. Prüfen Sie die ausgewählte Zeile und Organisation, bevor Sie diese Aktionen verwenden.

## **Email Import**

Ein angebundenes Postfach ist von der eingehenden DocBits-E-Mail-Adresse aus der untenstehenden Videoanleitung zu unterscheiden. Wählen Sie die Methode, die zu Ihrem Prozess passt.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tabelle Email Import mit New, dem Importprotokoll-Symbol und Spalten zur Postfachkonfiguration"><figcaption><p>Mit New erstellen Sie eine Postfachverbindung, mit dem Protokollsymbol prüfen Sie Importe. Bestehende Verbindungszeilen und der Informationslink sind unkenntlich gemacht.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Es werden nur Dokumente mit den folgenden Dateitypen importiert:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Wie Anhänge erkannt werden**

Zusätzlich zu den oben aufgeführten Dateiendungen erkennt DocBits ein Dokument auch an seinem **tatsächlichen Dateiinhalt** (Dateisignatur) und nicht nur am Inhaltstyp, den das sendende Mailsystem angibt. Das ist bei **weitergeleiteten** Mails wichtig: Zwischengeschaltete Mailserver/Gateways kennzeichnen einen Anhang häufig mit einem allgemeinen Typ (`application/octet-stream`) statt beispielsweise mit `application/pdf` oder `application/xml`. DocBits erkennt und importiert solche Anhänge dennoch korrekt.

* **Weitergeleitete `.eml`**-Nachrichten und Outlook-Anhänge **`winmail.dat`** (TNEF) werden entpackt, und die darin enthaltenen Dokumente werden importiert.
* **XML-Kodierung:** Wird eine XML-Rechnung mit einem allgemeinen Typ (`application/octet-stream`) gekennzeichnet, erkennt DocBits sie an ihrer Deklaration `<?xml` und toleriert dabei eine vorangestellte **UTF-8**- oder **UTF-16**-Byte-Order-Mark (BOM, LE/BE) — derzeit werden nur diese BOM-Kodierungen automatisch anhand des Inhalts erkannt. Ein Anhang, der einen Dateinamen mit `.xml` behält, wird unabhängig von seiner Kodierung importiert.
* **Ignoriert:** Inline-Bilder, die in einer Mail mitgeführt werden (Signaturlogos / eingebettete Grafiken — PNG, JPG, GIF, BMP), werden stillschweigend übersprungen und **nicht** als fehlgeschlagene Importe gezählt.

Kann ein Anhang nicht importiert werden und ist für die Eingangsadresse die Option **“Reply to this email if import can not be done”** aktiviert, wird die konfigurierte Antwortadresse benachrichtigt.
{% endhint %}

### Neue IMAP-Verbindung hinzufügen

1. Klicken Sie in **Email Import** auf **New** und wählen Sie unter **Protocol** den Eintrag **IMAP**.
2. Geben Sie in **Email Server Setup** den Servernamen, den Port, die Verschlüsselung, den Benutzernamen, die E-Mail-Adresse und das Passwort ein. Verwenden Sie die von Ihrem Mailprovider geforderten Werte; die angezeigte 993 ist ein Portbeispiel und keine abgeschlossene Einstellung.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="IMAP Email Server Setup mit Protokoll, Server, Port, Verschlüsselung, Kontozugangsdaten und Next"><figcaption><p>Füllen Sie die erforderlichen Server- und Kontofelder vor Next aus. Der Passwortbereich ist unkenntlich gemacht; in diesem Beispiel wurden keine Postfach-Zugangsdaten übermittelt.</p></figcaption></figure>

Das Kopiersymbol neben **Password** kopiert das eingegebene Passwort in die Zwischenablage. Mit **Cancel** oder dem Schließen-Symbol verlassen Sie diesen Assistenten für eine neue Verbindung, ohne sie zu speichern.

3. Klicken Sie auf **Next**, um **Options** zu öffnen. Wählen Sie, ob **Merge attached documents** oder **Block duplicate filename import** gelten soll. **Email Notification** aktiviert eine Bestätigungs-E-Mail nach dem Import; aktivieren Sie die Option nur, wenn dieses Verhalten gewünscht ist.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="IMAP-Schritt Options mit Zusammenführen von Anhängen, Filterung doppelter Dateinamen, E-Mail-Benachrichtigung, Back und Next"><figcaption><p>Options trennt das Importverhalten von der E-Mail-Benachrichtigung. In diesem ungespeicherten Beispiel sind beide Kontrollkästchen und der Benachrichtigungsschalter ausgeschaltet.</p></figcaption></figure>

4. Klicken Sie auf **Next**, um **Config** zu öffnen. Wählen Sie die erforderlichen **Sub-Organizations**, prüfen Sie den vorhandenen **API Key**, legen Sie den Empfänger für Importfehler fest und kontrollieren Sie **Document Routing**. Klappen Sie **Advanced Settings** nur auf, wenn der Prozess zusätzliche Optionen benötigt.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="IMAP-Schritt Config mit Organisation, unkenntlich gemachtem API Key, Fehlerbenachrichtigungen, Document Routing, Advanced Settings und Save"><figcaption><p>Config bündelt die Organisationszuordnung, den vorhandenen Schlüssel, Fehlerbenachrichtigungen und das Routing. Der Schlüssel ist unkenntlich gemacht, und Save wurde nicht verwendet.</p></figcaption></figure>

In **Config** zeigt oder verbirgt das Augensymbol den vorhandenen **API Key**, und **Copy** kopiert ihn in die Zwischenablage. Keines der beiden Bedienelemente erzeugt einen neuen Schlüssel.

5. Klicken Sie auf **Save**, wenn die Konfiguration fertig ist. Verwenden Sie anschließend **Activate** im Menü **Actions** der gespeicherten Verbindung, um die automatische Verarbeitung zu starten.

Bei einer gespeicherten IMAP-Verbindung bietet **Edit** Optionen für Ordner und die Behandlung nach dem Import. Wählen Sie den Quellordner und den Zielordner für verschobene E-Mails erst, nachdem die Verbindung erstellt wurde und die verfügbaren Ordner geladen werden können.

### Aktionen für IMAP

Das Menü **Actions** der gespeicherten Verbindung bietet **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** und **Delete**. Der Verbindungstest kontaktiert das konfigurierte Postfach; die Aktivierung schaltet die Verarbeitung ein. Prüfen Sie die Protokolle, bevor Sie einen fehlgeschlagenen Import wiederholen.

### Neue OAuth Office365-Verbindung hinzufügen

1. Klicken Sie in **Email Import** auf **New** und wählen Sie unter **Protocol** den Eintrag **OAuth Office365**. Für eine vom Administrator verwaltete Tenant-Anwendung wählen Sie **OAuth Office365 - Tenant** und beachten [O365 Tenant](o365-tenant.md).
2. Prüfen Sie **Document Routing** vor der Authentifizierung.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="OAuth Office365-Einrichtung mit Document Routing und der Schaltfläche Authenticate vor der Microsoft-Authentifizierung"><figcaption><p>Wählen Sie die Route vor Authenticate. Diese Ansicht zeigt den Zustand vor der Anmeldung; es wurde keine Microsoft-Authentifizierung gestartet.</p></figcaption></figure>

3. Klicken Sie auf **Authenticate**, wenn die Postfachverbindung freigegeben ist. Schließen Sie die Microsoft-Anmeldung per Gerätecode mit dem von DocBits angezeigten Code ab, kehren Sie zurück und wählen Sie **Finish Authentication**.
4. Prüfen Sie nach der Authentifizierung die für die Verbindung angebotenen Optionen zu Organisation, Ordner, freigegebenem Postfach, Zielordner und Fehlerbenachrichtigung. Verwenden Sie **Next**, um zu **Config** zu wechseln, sobald es verfügbar ist, und speichern Sie dann die gewünschten Einstellungen.
5. Aktivieren Sie die gespeicherte Verbindung, wenn automatische Importe laufen sollen. **Import** startet, sofern für eine gespeicherte Verbindung angeboten, einen tatsächlichen Import; verwenden Sie diese Aktion bewusst.

### Aktionen für OAuth Office365

Das Menü **Actions** der gespeicherten Verbindung bietet **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** und **Delete**. Das Deaktivieren stoppt die automatische Verarbeitung; das Löschen entfernt die Konfiguration.

### Import Log

Mit dem Protokollsymbol oben rechts in **Email Import** prüfen Sie Importe über alle konfigurierten Postfachverbindungen. Für eine einzelne Verbindung verwenden Sie die Aktion **Import Log** in der gespeicherten Zeile. Prüfen Sie Betreff, Absender, Status und die verfügbaren Fehlerdetails, bevor Sie über eine Wiederholung entscheiden.

## Inbound Emails

Die beiden Screenshots der Anleitung unten zeigen die eingehende DocBits-Adresse und ihre Protokolle. Das ist von den oben beschriebenen Postfachverbindungen zu unterscheiden.

* Mit dem Kopiersymbol neben **E-Mail** kopieren Sie die Empfangsadresse, die für die aktuelle Organisation und Umgebung angezeigt wird.
* **Add** fügt im Formular eine weitere Zeile für einen zulässigen Absender ein. Wählen Sie den Absender und gegebenenfalls die vorgesehene Unterorganisation und speichern Sie die Konfiguration mit **Save**. Das bloße Hinzufügen einer Zeile speichert sie nicht.
* **Logs** öffnet das Protokoll der eingehenden E-Mails. **Errors** filtert auf Fehler; **Inbound** und **Outbound** wählen die Nachrichtenrichtung.
* Klappen Sie eine Protokollzeile über das Pfeilsymbol auf, um Anhangsdetails zu prüfen. Das Kopiersymbol neben der Trace-ID kopiert diese ID für die Fehlersuche. **Original email** lädt, sofern für eine eingehende Zeile verfügbar, die ausgewählte Originalnachricht als `.eml`-Datei herunter; ein erneuter Import wird dabei nicht ausgelöst.

## Videoanleitung: E-Mail-Postfach und Fehlersuche

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/de.mp4" %}
E-Mail-Postfach und Fehlersuche
{% endembed %}

[Mit Untertiteln und Kapiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/de.html)

Einzelne native Produktbeschriftungen können in einer anderen Sprache verbleiben. Technische Feld-IDs bleiben erhalten.

Unter Einstellungen und Import verwende ich in diesem Beispiel die eingehende DocBits-Adresse. Ein direkt angebundenes Postfach ist eine eigene Importmethode. Für diese Schulung arbeite ich in einer eigenen Demoorganisation mit synthetischen Rechnungen. Benachrichtigungen bleiben ausgeschaltet.

Zuerst prüfe ich die angezeigte Empfangsadresse und den Geltungsbereich. Die Adresse gehört genau zu dieser Organisation und ihrer Umgebung. Für ein anderes Unternehmen oder eine Produktionsumgebung verwende ich immer die dort tatsächlich angezeigte Adresse.

Hier beschränke ich den Posteingang auf unseren freigegebenen Testabsender. Die Zuordnung zu einer Unterorganisation wähle ich nur, wenn sie zum vorgesehenen Prozess gehört. Ich speichere die Einstellung und öffne sie erneut. Der zulässige Absender ist erhalten geblieben; automatische Antwort-E-Mails bleiben in dieser Schulung ausgeschaltet.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Zulässiger Absender gespeichert, Benachrichtigungen ausgeschaltet"><figcaption><p>Zulässiger Absender gespeichert, Benachrichtigungen ausgeschaltet</p></figcaption></figure>

Für diese Schulung wurde eine Testnachricht direkt an die DocBits-Eingangsverarbeitung übergeben. Dieser Test bestätigt keine externe E-Mail-Zustellung. Im Protokoll prüfe ich den passenden Betreff, den Absender und den importierten Anhang. Anschließend prüfe ich das tatsächlich erstellte Dokument.

Ich öffne das zugehörige Dokument und vergleiche den PDF-Anhang mit der Rechnung in DocBits. Dateiname, Rechnungsnummer, Lieferant und Betrag müssen übereinstimmen. Ein erfolgreicher Import sagt nichts über eine Freigabe oder eine ERP-Buchung aus.

Ein zweiter kontrollierter Test stammt von einem nicht freigegebenen Absender. Im Protokoll suche ich gezielt nach diesem Eingang und aktiviere den Fehlerfilter. Die Details nennen den abgelehnten Absender. Ich prüfe die Ursache anhand des Betreffs und der Trace-ID, statt den Import mehrfach auszulösen.

In einem echten Fall kläre ich zuerst, ob dieser Absender überhaupt berechtigt ist. Eine genehmigte Änderung an der Absenderliste wird gespeichert und erneut geprüft. Danach überprüfe ich einen neuen eindeutigen Testeingang bis zum erstellten Dokument. Bei technischen Fehlern übergebe ich die Trace-ID und die konkrete Fehlermeldung.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Fehlgeschlagener Import mit Anhang, Ursache und Trace"><figcaption><p>Fehlgeschlagener Import mit Anhang, Ursache und Trace</p></figcaption></figure>
