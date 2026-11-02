---
hidden: true
noIndex: true
---

# E-Mail

DocBits kann Dokumente auf zwei Wegen aus E-Mails importieren. Beide werden unter **Einstellungen → Import** (Dokumentenverarbeitung) konfiguriert.

## Methode 1 – E-Mail-Import (Postfach verbinden)

Verbinden Sie ein E-Mail-Konto, und DocBits importiert Dokumente automatisch, sobald neue E-Mails eintreffen. Öffnen Sie auf der Import-Seite den Bereich **E-Mail-Import** und klicken Sie auf **+ Neu**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Bereich E-Mail-Import"><figcaption>E-Mail-Import – ein Postfach für den automatischen Dokumentenimport verbinden</figcaption></figure>

Wählen Sie anschließend das Protokoll für Ihr Postfach:

* **IMAP** – siehe [IMAP](imap.md)
* **OAuth (Office 365)** – siehe [OAuth Office365](oauth-office365.md)

## Methode 2 – Eingehende E-Mails (an DocBits weiterleiten)

Leiten Sie E-Mails – oder senden Sie sie direkt – an die eindeutige Eingangsadresse Ihrer Organisation, und DocBits importiert die Anhänge automatisch. Eine Postfachverbindung ist nicht erforderlich. Öffnen Sie auf der Import-Seite den Bereich **Eingehende E-Mails**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Bereich Eingehende E-Mails"><figcaption>Eingehende E-Mails – Dokumente an Ihre DocBits-Adresse weiterleiten</figcaption></figure>

* **Info / E-Mail** – die eindeutige Eingangsadresse Ihrer Organisation (Format `<org-id>@inbound.docbits.com`). Leiten Sie Ihre Dokumente an diese Adresse weiter; über das Kopiersymbol kopieren Sie sie.
* **Dokument nur aus vordefinierter(n) E-Mail(s) importieren** – wenn aktiviert, werden nur E-Mails von den auf der Whitelist eingetragenen Absendern importiert; E-Mails anderer Absender werden ignoriert.
* **Auf diese E-Mail antworten, wenn der Import nicht möglich ist** – sendet dem Absender eine automatische Antwort, wenn der Import fehlschlägt.
* **Absender benachrichtigen, wenn der Import fehlschlägt** – benachrichtigt den Absender, wenn seine E-Mail nicht importiert werden konnte.
* **Logs** – öffnet das Protokoll der Verarbeitung eingehender E-Mails. Klicken Sie auf **Speichern**, um Ihre Änderungen zu übernehmen.

## Unterstützte Dokumentanhänge

Beide E-Mail-Importmethoden akzeptieren diese Dokumentanhänge:

| Format | Dateiendungen | Typische Verwendung |
| --- | --- | --- |
| PDF | `.pdf` | Rechnungen und andere PDF-Dokumente |
| TIFF | `.tif`, `.tiff` | Gescannte Dokumente |
| XML | `.xml` | Strukturierte elektronische Dokumente |
| EDI / Bestelldaten | `.edi`, `.purchaseorder` | Elektronischer Datenaustausch und Bestellungen |

Wenn ein Weiterleitungsdienst eine PDF-, TIFF- oder XML-Datei als generischen Anhang kennzeichnet, kann DocBits sie anhand des Dateiinhalts oder einer bekannten Dateiendung erkennen. Weitergeleitete `.eml`-Nachrichten können ebenfalls unterstützte Dokumente enthalten; DocBits extrahiert diese inneren Anhänge vor dem Import.

Bilder wie PNG, JPG, GIF und BMP werden nicht als Dokumente importiert. Inline-Signaturbilder und Logos in weitergeleiteten E-Mails werden übersprungen. Office-Dateien wie Word, Excel und PowerPoint werden von diesen E-Mail-Importmethoden nicht unterstützt.

Prüfen Sie bei weitergeleiteten E-Mails die **Logs** unter **Eingehende E-Mails**, wenn ein Dokument fehlt. Wenn **Absender benachrichtigen, wenn der Import fehlschlägt** aktiviert ist, erhält der Absender eine Erklärung und einen Link zu dieser Seite. Für ein verbundenes Postfach nutzen Sie die Anleitung zur [IMAP](imap.md)- oder [OAuth (Office 365)](oauth-office365.md)-Einrichtung.
