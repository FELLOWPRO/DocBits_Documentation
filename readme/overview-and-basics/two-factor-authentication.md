# Two-Factor Authentication (2FA)

## Overview

Two-Factor Authentication (2FA) adds a second step to your login. After your password, DocBits asks for a second factor that only you have — a code from an authenticator app, a code emailed to you, or a passkey (Touch ID, Windows Hello, YubiKey, 1Password). Even if someone learns your password, they cannot sign in without that second factor.

2FA is **optional for each user** and can be **required by your organisation's administrator**. Single sign-on (SSO) logins (Google, Microsoft, SAML) are exempt — your identity provider already enforces its own MFA.

You can enrol more than one method. The methods DocBits supports are:

* **Authenticator app (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy, etc.
* **Email code** — a 6-digit code sent to your account email.
* **Passkey (WebAuthn/FIDO2)** — Touch ID, Windows Hello, a hardware key (YubiKey), or a password manager.

When you turn on your first factor, DocBits also gives you **ten backup codes** to use if you ever lose access to your method.

## Where to find it

Open your **profile / account settings** (top-right account menu → **Edit profile**) and select **Two-factor authentication**. The 2FA dialog shows your current status and the methods you can add.

## Set up an authenticator app (TOTP)

1. In the 2FA dialog, click **Enable 2FA**.
2. Scan the QR code with your authenticator app (Google Authenticator, 1Password, Authy, …). If you cannot scan, use the **manual key** shown below the QR code.
3. Enter the 6-digit code your app shows and confirm.
4. DocBits enables 2FA and shows your **backup codes** (see below).

## Set up email verification

1. In the 2FA dialog, click **Enable email verification**.
2. DocBits emails a 6-digit code to your account address.
3. Enter the code to confirm. Email verification is now on.

## Add a passkey

1. In the 2FA dialog, click **Add a passkey**.
2. Your browser or device prompts you to confirm with Touch ID, Windows Hello, a hardware key, or your password manager.
3. The passkey is saved. You can add several passkeys and rename or remove them later.

## Backup codes

When you enable your **first** factor, DocBits shows **ten backup codes** — **once**. Each code works a single time and lets you sign in if you lose your authenticator or phone.

* Save them somewhere safe (a password manager is ideal).
* You can generate a fresh set any time with **Regenerate backup codes** (this invalidates the old set).

{% hint style="warning" %}
Backup codes are shown only at the moment they are generated. DocBits cannot show them again — store them immediately.
{% endhint %}

## Signing in with 2FA

1. Enter your email and password as usual.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>The login screen. You can also sign in without a password using <strong>Sign in with a passkey</strong>.</p></figcaption></figure>
2. DocBits asks for your second factor. Choose your method:
   * **Authenticator** — type the current 6-digit code from your app.
   * **Email** — click to receive a code by email, then type it in.
   * **Passkey** — confirm with Touch ID / Windows Hello / your key.
   * **Backup code** — if you cannot use your usual method.
3. On success you are signed in.

### What the email code looks like

If you choose **Email**, DocBits sends a message with a 6-digit code that expires in 10 minutes:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>The verification-code email. The code expires after 10 minutes and can be used once.</p></figcaption></figure>

## Trust this device

On the second-factor screen you can tick **Remember this device**. DocBits then skips the 2FA step on that device for **30 days**. The trust is dropped automatically when you change your password, and you can revoke it yourself at any time (see below).

## Manage your passkeys and trusted devices

Open the 2FA dialog and click **Manage** to review what is enrolled.

* **Passkeys** — rename a passkey (click its name) or delete it. Deleting your last remaining factor turns 2FA off.
* **Trusted devices** — revoke a single device, or **Revoke all devices** to force a fresh 2FA prompt everywhere.

## Turn 2FA off

In the 2FA dialog click **Disable 2FA** and confirm with a current authenticator code or a backup code. Turning 2FA off also clears your backup codes and revokes your trusted devices.

{% hint style="info" %}
If your organisation **requires** MFA, you cannot log in with a password until at least one factor is set up. Ask your administrator if you are unsure whether MFA is mandatory for your organisation.
{% endhint %}

## Passwordless sign-in (optional)

Once you have a passkey, you can sign in **without typing your password** using **Sign in with a passkey** on the login screen. Your password keeps working as a fallback. Passwordless requires the passkey to verify you (Touch ID / Windows Hello / PIN), so it is both quicker and phishing-resistant.
