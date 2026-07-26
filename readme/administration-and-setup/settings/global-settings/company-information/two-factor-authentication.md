# Zwei-Faktor-Authentifizierung (Admin)

## Überblick

Als Administrator einer Organisation können Sie **für jedes Mitglied die Nutzung der Zwei-Faktor-Authentifizierung (2FA) verpflichtend machen**, wenn es sich mit einem Passwort anmeldet. Wenn die Anforderung aktiviert ist, wird ein Mitglied, das noch keinen zweiten Faktor eingerichtet hat, durch die Einrichtung geführt, bevor es die Anmeldung abschließen kann.

Single-Sign-On-Anmeldungen (SSO) — Google, Microsoft, SAML — sind **ausgenommen**: Ihr Identitätsanbieter erzwingt bereits seine eigene MFA, sodass die Anforderung nur Passwort-Anmeldungen betrifft.

Diese Einstellung finden Sie unter **Einstellungen → Globale Einstellungen → Unternehmensinformationen → Zwei-Faktor-Authentifizierung** und ist nur für Administratoren der Organisation verfügbar.

## MFA für Ihre Organisation verlangen

1. Gehen Sie zu **Einstellungen → Globale Einstellungen → Unternehmensinformationen**.
2. Öffnen Sie den Abschnitt **Zwei-Faktor-Authentifizierung**.
3. Aktivieren Sie **Zwei-Faktor-Authentifizierung für alle Mitglieder verlangen** und klicken Sie auf **Speichern**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Aktivieren Sie die Anforderung für alle Mitglieder und überwachen Sie die Verbreitung darunter.</p></figcaption></figure>

Nach dem Speichern wird die Änderung innerhalb einer Minute wirksam. Ab diesem Zeitpunkt gilt:

* Ein Mitglied **mit** einem zweiten Faktor wird nach seinem Passwort wie gewohnt danach gefragt.
* Ein Mitglied **ohne** einen zweiten Faktor muss einen einrichten, bevor es eine Sitzung erhält.
* SSO-/Social-Login-Anmeldungen sind nicht betroffen.

{% hint style="warning" %}
Das Aktivieren blockiert Passwort-Anmeldungen für Mitglieder ohne zweiten Faktor, bis sie die Einrichtung abgeschlossen haben. Informieren Sie Ihr Team über die Änderung und erwägen Sie, sie außerhalb der Stoßzeiten zu aktivieren.
{% endhint %}

## MFA-Verbreitungsbericht

Unterhalb des Schalters zeigt das Panel **MFA-Verbreitung**, wie verbreitet die 2FA in Ihrer Organisation ist, bevor Sie sie erzwingen:

* den gesamten **Verbreitungsprozentsatz** und einen Fortschrittsbalken,
* wie viele Ihrer Mitglieder die 2FA aktiviert haben (z. B. *0 von 74 Mitgliedern*),
* eine Aufschlüsselung nach Faktor — **Authenticator**, **E-Mail** und **Passkey**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>Der MFA-Verbreitungsbericht: Gesamtprozentsatz, eingerichtete Mitglieder und eine Aufschlüsselung nach Faktor.</p></figcaption></figure>

Nutzen Sie ihn, um die Bereitschaft einzuschätzen: Steigern Sie zunächst die Verbreitung und aktivieren Sie dann die Anforderung, sodass weniger Mitglieder beim Einrichtungsschritt blockiert werden.

## Was Mitglieder sehen

Ein Mitglied, das zur Einrichtung verpflichtet ist, wird bei seiner nächsten Anmeldung zur 2FA-Einrichtung geleitet und wählt eine Methode (Authenticator-App, E-Mail-Code oder Passkey). Die Schritte für Endbenutzer werden unter [Zwei-Faktor-Authentifizierung (2FA)](../../../../overview-and-basics/two-factor-authentication.md) beschrieben.

## Verwandte Sicherheitskontrollen

Die organisationsweite MFA-Anforderung ergänzt die integrierten Schutzmaßnahmen, die immer gelten, sobald ein Benutzer die 2FA aktiviert hat: einmalig verwendbare Login-Codes, ein TOTP-Replay-Schutz, Versuchslimits pro Abfrage und pro Konto (ein Konto wird nach zu vielen fehlgeschlagenen Versuchen vorübergehend gesperrt) und die automatische Aufhebung vertrauenswürdiger Geräte, wenn ein Mitglied sein Passwort ändert.
