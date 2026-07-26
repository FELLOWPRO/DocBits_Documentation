# Zwei-Faktor-Authentifizierung (2FA)

## Überblick

Die Zwei-Faktor-Authentifizierung (2FA) fügt Ihrem Login einen zweiten Schritt hinzu. Nach Ihrem Passwort fragt DocBits nach einem zweiten Faktor, den nur Sie besitzen — einem Code aus einer Authenticator-App, einem per E-Mail zugesandten Code oder einem Passkey (Touch ID, Windows Hello, YubiKey, 1Password). Selbst wenn jemand Ihr Passwort erfährt, kann er sich ohne diesen zweiten Faktor nicht anmelden.

Die 2FA ist **für jeden Benutzer optional** und kann **vom Administrator Ihrer Organisation verpflichtend gemacht werden**. Single-Sign-On-Anmeldungen (SSO) (Google, Microsoft, SAML) sind ausgenommen — Ihr Identitätsanbieter erzwingt bereits seine eigene MFA.

Sie können mehrere Methoden einrichten. DocBits unterstützt die folgenden Methoden:

* **Authenticator-App (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy usw.
* **E-Mail-Code** — ein 6-stelliger Code, der an Ihre Konto-E-Mail-Adresse gesendet wird.
* **Passkey (WebAuthn/FIDO2)** — Touch ID, Windows Hello, ein Hardware-Schlüssel (YubiKey) oder ein Passwort-Manager.

Wenn Sie Ihren ersten Faktor aktivieren, stellt DocBits Ihnen außerdem **zehn Backup-Codes** bereit, die Sie verwenden können, falls Sie einmal den Zugriff auf Ihre Methode verlieren.

## Wo Sie es finden

Öffnen Sie Ihre **Profil-/Kontoeinstellungen** (Kontomenü oben rechts → **Profil bearbeiten**) und wählen Sie **Zwei-Faktor-Authentifizierung**. Der 2FA-Dialog zeigt Ihren aktuellen Status und die Methoden an, die Sie hinzufügen können.

<figure><img src="../.gitbook/assets/mfa-2fa-dialog.png" alt="The Two-factor authentication dialog"><figcaption><p>Der Dialog Zwei-Faktor-Authentifizierung. Von hier aus können Sie eine Authenticator-App oder die E-Mail-Verifizierung aktivieren, einen Passkey hinzufügen oder <strong>Verwalten</strong> öffnen.</p></figcaption></figure>

## Authenticator-App einrichten (TOTP)

1. Klicken Sie im 2FA-Dialog auf **2FA aktivieren**.
2. Scannen Sie den QR-Code mit Ihrer Authenticator-App (Google Authenticator, 1Password, Authy, …). Wenn Sie nicht scannen können, verwenden Sie den **manuellen Schlüssel**, der unterhalb des QR-Codes angezeigt wird.
3. Geben Sie den 6-stelligen Code ein, den Ihre App anzeigt, und bestätigen Sie.
4. DocBits aktiviert die 2FA und zeigt Ihre **Backup-Codes** an (siehe unten).

<figure><img src="../.gitbook/assets/mfa-totp-setup.png" alt="The authenticator-app setup screen with QR code"><figcaption><p>Scannen Sie den QR-Code mit Ihrer Authenticator-App oder geben Sie den manuellen Schlüssel ein. Bestätigen Sie anschließend mit dem 6-stelligen Code, den die App anzeigt.</p></figcaption></figure>

## E-Mail-Verifizierung einrichten

1. Klicken Sie im 2FA-Dialog auf **E-Mail-Verifizierung aktivieren**.
2. DocBits sendet einen 6-stelligen Code per E-Mail an Ihre Kontoadresse.
3. Geben Sie den Code zur Bestätigung ein. Die E-Mail-Verifizierung ist jetzt aktiviert.

## Einen Passkey hinzufügen

1. Klicken Sie im 2FA-Dialog auf **Passkey hinzufügen**.
2. Ihr Browser oder Gerät fordert Sie auf, mit Touch ID, Windows Hello, einem Hardware-Schlüssel oder Ihrem Passwort-Manager zu bestätigen.
3. Der Passkey wird gespeichert. Sie können mehrere Passkeys hinzufügen und sie später umbenennen oder entfernen.

## Backup-Codes

Wenn Sie Ihren **ersten** Faktor aktivieren, zeigt DocBits **zehn Backup-Codes** an — **einmalig**. Jeder Code funktioniert nur ein einziges Mal und ermöglicht Ihnen die Anmeldung, falls Sie Ihren Authenticator oder Ihr Telefon verlieren.

* Bewahren Sie sie an einem sicheren Ort auf (ein Passwort-Manager ist ideal).
* Sie können jederzeit einen neuen Satz mit **Backup-Codes neu generieren** erstellen (dadurch wird der alte Satz ungültig).

<figure><img src="../.gitbook/assets/mfa-backup-codes.png" alt="The backup codes screen"><figcaption><p>Ihre zehn Backup-Codes, einmalig angezeigt. Jeder funktioniert nur ein einziges Mal — bewahren Sie sie an einem sicheren Ort auf.</p></figcaption></figure>

{% hint style="warning" %}
Backup-Codes werden nur im Moment ihrer Erstellung angezeigt. DocBits kann sie nicht erneut anzeigen — speichern Sie sie sofort.
{% endhint %}

## Anmelden mit 2FA

1. Geben Sie wie gewohnt Ihre E-Mail-Adresse und Ihr Passwort ein.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>Der Anmeldebildschirm. Sie können sich auch ohne Passwort über <strong>Mit einem Passkey anmelden</strong> anmelden.</p></figcaption></figure>
2. DocBits fragt nach Ihrem zweiten Faktor. Wählen Sie Ihre Methode:
   * **Authenticator** — geben Sie den aktuellen 6-stelligen Code aus Ihrer App ein.
   * **E-Mail** — klicken Sie auf **Code per E-Mail senden**, um einen Code per E-Mail zu erhalten, und geben Sie ihn dann ein.
   * **Passkey** — klicken Sie auf **Passkey verwenden** und bestätigen Sie mit Touch ID / Windows Hello / Ihrem Schlüssel.
   * **Backup-Code** — falls Sie Ihre übliche Methode nicht verwenden können.

    <figure><img src="../.gitbook/assets/mfa-challenge.png" alt="The second-factor challenge screen"><figcaption><p>Nach Ihrem Passwort fragt DocBits nach Ihrem zweiten Faktor. Wechseln Sie die Methode mit <strong>Passkey verwenden</strong> oder <strong>Code per E-Mail senden</strong> und stufen Sie das Gerät optional für 30 Tage als vertrauenswürdig ein.</p></figcaption></figure>
3. Bei Erfolg sind Sie angemeldet.

### Wie der E-Mail-Code aussieht

Wenn Sie **E-Mail** wählen, sendet DocBits eine Nachricht mit einem 6-stelligen Code, der nach 10 Minuten abläuft:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>Die E-Mail mit dem Verifizierungscode. Der Code läuft nach 10 Minuten ab und kann einmal verwendet werden.</p></figcaption></figure>

## Diesem Gerät vertrauen

Auf dem Bildschirm für den zweiten Faktor können Sie **Dieses Gerät merken** ankreuzen. DocBits überspringt dann den 2FA-Schritt auf diesem Gerät für **30 Tage**. Die Vertrauensstellung wird automatisch aufgehoben, wenn Sie Ihr Passwort ändern, und Sie können sie jederzeit selbst widerrufen (siehe unten).

## Ihre Passkeys und vertrauenswürdigen Geräte verwalten

Öffnen Sie den 2FA-Dialog und klicken Sie auf **Verwalten**, um zu überprüfen, was eingerichtet ist.

* **Passkeys** — benennen Sie einen Passkey um (klicken Sie auf seinen Namen) oder löschen Sie ihn. Das Löschen Ihres letzten verbleibenden Faktors deaktiviert die 2FA.
* **Vertrauenswürdige Geräte** — widerrufen Sie ein einzelnes Gerät oder verwenden Sie **Alle Geräte widerrufen**, um überall eine erneute 2FA-Abfrage zu erzwingen.

<figure><img src="../.gitbook/assets/mfa-passkeys-list.png" alt="Managing enrolled passkeys and trusted devices"><figcaption><p>Die Verwaltungsansicht listet Ihre eingerichteten Passkeys und vertrauenswürdigen Geräte auf, wo Sie sie umbenennen oder entfernen können.</p></figcaption></figure>

## 2FA deaktivieren

Klicken Sie im 2FA-Dialog auf **2FA deaktivieren** und bestätigen Sie mit einem aktuellen Authenticator-Code oder einem Backup-Code. Durch das Deaktivieren der 2FA werden auch Ihre Backup-Codes gelöscht und Ihre vertrauenswürdigen Geräte widerrufen.

{% hint style="info" %}
Wenn Ihre Organisation MFA **verlangt**, können Sie sich erst mit einem Passwort anmelden, wenn mindestens ein Faktor eingerichtet ist. Fragen Sie Ihren Administrator, wenn Sie nicht sicher sind, ob MFA für Ihre Organisation verpflichtend ist.
{% endhint %}

## Passwortlose Anmeldung (optional)

Sobald Sie einen Passkey haben, können Sie sich **ohne Eingabe Ihres Passworts** über **Mit einem Passkey anmelden** auf dem Anmeldebildschirm anmelden. Ihr Passwort funktioniert weiterhin als Ausweichlösung. Für die passwortlose Anmeldung muss der Passkey Sie verifizieren (Touch ID / Windows Hello / PIN), sodass sie sowohl schneller als auch phishing-resistent ist.
