# Two-Factor Authentication (Admin)

## Overview

As an organisation administrator you can **require every member to use two-factor authentication (2FA)** when they log in with a password. When the requirement is on, a member who has not yet set up a second factor is guided through enrollment before they can finish signing in.

Single sign-on (SSO) logins — Google, Microsoft, SAML — are **exempt**: their identity provider already enforces its own MFA, so the requirement only affects password logins.

This setting lives in **Settings → Global Settings → Company Information → Two-factor authentication** and is available to organisation administrators only.

## Require MFA for your organisation

1. Go to **Settings → Global Settings → Company Information**.
2. Open the **Two-factor authentication** section.
3. Turn on **Require two-factor authentication for all members** and click **Save**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Turn on the requirement for all members, and monitor adoption below.</p></figcaption></figure>

Once saved, the change takes effect within a minute. From then on:

* A member **with** a second factor is challenged for it after their password, as usual.
* A member **without** a second factor is required to enrol one before they receive a session.
* SSO / social logins are unaffected.

{% hint style="warning" %}
Turning this on blocks password logins for members who have no second factor until they finish enrollment. Communicate the change to your team, and consider enabling it outside peak hours.
{% endhint %}

## MFA adoption report

Below the toggle, the **MFA adoption** panel shows how widely 2FA is used in your organisation before you enforce it:

* the overall **adoption percentage** and a progress bar,
* how many of your members have 2FA enabled (e.g. *0 of 74 members*),
* a per-factor breakdown — **Authenticator**, **Email**, and **Passkey**.

Use it to gauge readiness: drive adoption up first, then switch the requirement on with fewer members blocked at the enrollment step.

## What members see

A member who is required to enrol is sent to the 2FA setup on their next login and picks a method (authenticator app, email code, or passkey). The end-user steps are covered in [Two-Factor Authentication (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Related security controls

The organisation-wide MFA requirement complements the built-in protections that always apply once a user has 2FA on: single-use login codes, a TOTP replay guard, per-challenge and per-account attempt limits (an account is temporarily locked after too many failed attempts), and automatic revocation of trusted devices when a member changes their password.
