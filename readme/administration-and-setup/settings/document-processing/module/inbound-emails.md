# Eingehende E-Mails

### Überblick

DocBits kann Dokumente direkt aus E-Mails übernehmen — ohne manuelles Hochladen. Es gibt **zwei Wege**, E-Mail-Dokumente einzuspielen, beide unter **Einstellungen → Dokumentverarbeitung → Import**:

| Methode | Funktionsweise | Am besten für |
|---------|----------------|---------------|
| **E-Mail-Import-Konto** | DocBits verbindet sich mit einem Postfach, das Ihnen gehört (**IMAP**, **OAuth Office365** oder **OAuth Office365 – Tenant**), und importiert die gefundenen Dokumente. | Ein dediziertes Postfach, das Ihre Dokumente bereits empfängt (z. B. `rechnungen@ihrefirma.de`). |
| **Weitergeleitete E-Mails (Eingehende E-Mails)** | DocBits stellt Ihnen eine eindeutige Adresse bereit; autorisierte Absender können Dokumente dorthin **weiterleiten**. | Spontanes Weiterleiten von vielen Absendern, ohne Postfach-Zugangsdaten zu teilen. |

Sie können jede Methode einzeln oder beide zusammen verwenden.

### Methode 1 — Postfach verbinden (E-Mail-Import)

Gehen Sie zu **Einstellungen → Dokumentverarbeitung → Import** und öffnen Sie den Abschnitt **E-Mail-Import**. Klicken Sie auf **Neu**, um eine Postfach-Verbindung hinzuzufügen.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="E-Mail-Import-Abschnitt mit Neu-Button"><figcaption><p>Klicken Sie im Abschnitt E-Mail-Import auf <strong>Neu</strong>, um ein Postfach zu verbinden.</p></figcaption></figure>

Der Einrichtungsassistent öffnet sich. Das erste Feld, **Protokoll**, bestimmt, wie DocBits sich verbindet — wählen Sie **IMAP**, **OAuth Office365** oder **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Protokoll-Auswahl mit IMAP, OAuth Office365 und OAuth Office365 - Tenant"><figcaption><p>Die Auswahl <strong>Protokoll</strong> bietet die drei Verbindungsarten.</p></figcaption></figure>

#### IMAP

Für ein gewöhnliches Postfach wählen Sie **IMAP** und tragen die Serverdaten und Anmeldeinformationen ein:

* **Servername** und **Port** (Standard `993`) Ihres Mailservers.
* **Verschlüsselung** — `SSL`, `TLS` oder `None`.
* **Benutzername**, **E-Mail** und **Passwort** des Postfachs.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="IMAP-Verbindungsformular mit Server, Port, Verschlüsselung und Anmeldeinformationen"><figcaption><p>Das IMAP-Formular: Mailserver-Verbindung plus die Postfach-Anmeldeinformationen.</p></figcaption></figure>

#### OAuth Office365

Für ein einzelnes Microsoft-365-Benutzerpostfach wählen Sie **OAuth Office365**. Statt eines Passworts autorisieren Sie DocBits über Microsoft: Wählen Sie das Ziel der **Dokumentenweiterleitung**, klicken Sie dann auf **Authentifizieren** und schließen Sie die Microsoft-Anmeldung ab.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="OAuth-Office365-Formular mit Dokumentenweiterleitung und Authentifizieren-Button"><figcaption><p>OAuth Office365 verbindet über die Microsoft-Anmeldung — in DocBits wird kein Passwort gespeichert.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Um auf Tenant-Ebene (Organisation) über eine Azure-App-Registrierung zu verbinden, wählen Sie **OAuth Office365 – Tenant** und tragen die Azure-Daten ein: **Mandanten-ID** (Tenant ID), **Client-App-ID** und **Wert der Client-App** (Client Secret). Prüfen Sie mit **Verbindung testen** und klicken Sie dann auf **Speichern**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Azure-Mandantenkonfiguration mit Mandanten-ID, Client-App-ID und Wert der Client-App"><figcaption><p>OAuth Office365 – Tenant nutzt eine Azure-App-Registrierung (Mandanten-ID, Client-App-ID, Client Secret).</p></figcaption></figure>

{% hint style="info" %}
Die **Dokumentenweiterleitung** legt fest, wohin die importierten Dokumente gehen — **DocBits** (das Standard-Dashboard) oder **AI Workforce**. Nach dem Verbinden können Sie in den nächsten Schritten des Assistenten wählen, aus welchem **Ordner** importiert wird, optional ein **gemeinsames Postfach**, und ob verarbeitete E-Mails in einen anderen Ordner **verschoben** werden.
{% endhint %}

### Methode 2 — E-Mails an DocBits weiterleiten (Eingehende E-Mails)

Für diese Methode muss zuerst das Modul **Eingehende E-Mails** aktiviert sein. Gehen Sie zu **Einstellungen → Dokumentverarbeitung → Modul**, öffnen Sie den Abschnitt **Dokumenttyp**, suchen Sie **Eingehende E-Mails** und aktivieren Sie den Schalter.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Aktivieren des Moduls Eingehende E-Mails"><figcaption><p>Aktivieren Sie <strong>Eingehende E-Mails</strong> unter Einstellungen → Dokumentverarbeitung → Modul.</p></figcaption></figure>

Sobald es aktiviert ist, erscheint unter **Einstellungen → Dokumentverarbeitung → Import** ein Abschnitt **Eingehende E-Mails**. Er enthält alles, was zum Empfang weitergeleiteter Dokumente nötig ist:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Abschnitt Eingehende E-Mails: Import-Adresse, vordefinierte Absender und Adresse für Fehlerbenachrichtigung"><figcaption><p>Der Abschnitt Eingehende E-Mails: Ihre Import-Adresse, die Liste der vordefinierten Absender und die Adresse für Fehlerbenachrichtigungen.</p></figcaption></figure>

* **Import-Adresse** — eine eindeutige, systemgenerierte Adresse im Format `org_id@environment.inbound.docbits.com`. Leiten Sie Dokumente an diese Adresse weiter (oder senden Sie sie dorthin), und DocBits importiert sie automatisch. Mit dem Kopier-Symbol übernehmen Sie die Adresse.
* **Dokument nur aus vordefinierter(n) E-Mail(s) importieren** — wenn aktiviert, werden nur die hier gelisteten Absenderadressen akzeptiert; E-Mails von allen anderen werden ignoriert. Für jeden Absender können Sie eine **Unter-Organisation** wählen (leer lassen, um der Haupt-Organisation zuzuordnen). Mit **hinzufügen** listen Sie weitere Absender, mit **Löschen** entfernen Sie einen.
* **Antworten Sie auf diese E-Mail, wenn der Import nicht möglich ist** — wenn aktiviert, tragen Sie eine Adresse ein, die bei jedem fehlgeschlagenen Importversuch benachrichtigt werden soll, damit Probleme nicht unbemerkt bleiben.

Klicken Sie auf **Speichern**, um Ihre Änderungen zu übernehmen.

{% hint style="info" %}
**Welche Anhänge werden importiert?** DocBits importiert **PDF**-, **TIFF**- und **XML**-Anhänge (z. B. eCOS-/EDI-E-Rechnungen) und entpackt weitergeleitete `.eml`-Nachrichten, um die darin enthaltenen Dokumente zu importieren. Die Erkennung basiert auf dem **tatsächlichen Dateiinhalt**, sodass Anhänge, die ein weiterleitender Mailserver mit einem generischen Typ (`application/octet-stream`) neu kennzeichnet, dennoch korrekt importiert werden. Inline-Bilder (Signatur-Logos / eingebettete Grafiken) werden ignoriert. Die vollständige Liste und das Verhalten finden Sie unter [Import → E-Mail-Import](../import/README.md#email-import).
{% endhint %}

### Wann welche Methode

* **Nutzen Sie ein E-Mail-Import-Konto**, wenn Dokumente bereits in einem dedizierten Postfach eingehen und DocBits sie selbstständig abholen soll — IMAP für allgemeine Mailserver, OAuth Office365 für Microsoft 365.
* **Nutzen Sie Weitergeleitete E-Mails**, wenn Personen Dokumente bei Bedarf weiterleiten sollen, oder wenn Sie keine Postfach-Zugangsdaten an DocBits weitergeben möchten.
* **Kombinieren Sie beide**, wenn manche Dokumente in einem festen Postfach ankommen und andere spontan weitergeleitet werden.

{% hint style="info" %}
Das Einschränken von Absendern (Methode 2) und die Wahl des richtigen Ziels der **Dokumentenweiterleitung** (Methode 1) sind die zwei gängigsten Wege, eine eingehende Pipeline sauber zu halten — nur die erwarteten Dokumente, dorthin geleitet, wo Sie sie haben möchten.
{% endhint %}
