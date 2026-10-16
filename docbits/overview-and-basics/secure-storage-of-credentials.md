---
description: Password hashing, API key storage, TLS, credential visibility, and account recovery in DocBits.
---

# Secure Storage of Credentials

DocBits handles login passwords, DocBits API keys, account information, and credentials for connected systems according to their purpose. This page explains the protection and recovery behavior for each category.

## Login passwords

DocBits stores login passwords as **salted, one-way password hashes**. Authentication checks the password supplied at sign-in against the stored hash. The original password is not stored in a form that can be decrypted and retrieved.

Consequently, administrators and DocBits support cannot retrieve an existing plaintext login password from the stored password hash. If a user forgets a password, the password must be reset to resume signing in with a password.

### Password reset

1. Select **Forgot password?** on the login screen.
2. Enter the email address associated with the account.
3. Open the password-reset link sent to that address.
4. Set a new password and sign in with it.

Reset links expire. If a link has expired, request a new one. The procedure sets a new password; it does not reveal the previous password. See [Getting Access and Signing In](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md#forgot-password) for the full instructions.

Accounts with a configured SSO or passkey method may use that alternative sign-in method. For SSO, password recovery is handled by the identity provider. See [Two-Factor Authentication](two-factor-authentication.md).

## DocBits API keys

API keys created through **API Key Management** are displayed in full only once, at creation. DocBits stores a one-way hash of the key and a short identifying prefix. The prefix and key metadata remain visible in the management list; the original full key cannot be retrieved from its hash.

Neither administrators nor DocBits support can look up the full key after creation. If a key is lost, revoke it and create a replacement. Individual keys can have an expiration date and can be revoked separately. See [API Key Management](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Account details and credentials for connected systems

Names, email addresses, roles, and account status are account information that authorized organization administrators can view and manage. They are separate from the secret used to authenticate. See [Users](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Credentials supplied for connected systems, such as an ERP service account, mailbox, or SFTP server, are also separate from a DocBits login password or a DocBits-issued API key. A connector may need the usable secret to authenticate to the external system. Its storage and access controls must therefore be assessed for that connector.

The inability to retrieve a login password or a hashed DocBits API key does **not** mean that all account information or all integration secrets are inaccessible to the vendor. Any assurance about personnel access to integration credentials requires confirmation of the relevant operational access controls.

## Encryption in transit

The public DocBits endpoints below support **TLS 1.2 and TLS 1.3** over HTTPS. Checks on **16 October 2026** confirmed that TLS 1.0 and TLS 1.1 were rejected.

| Endpoint | Purpose | Supported TLS versions verified |
| --- | --- | --- |
| `app.docbits.com` | Web application | TLS 1.2 and TLS 1.3 |
| `auth.docbits.com` | Authentication service | TLS 1.2 and TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 and TLS 1.3 |

### What types of encryption are supported in transit?

| Questionnaire item | Answer for the public endpoints above |
| --- | --- |
| Is TLS 1.1 supported? | **No.** Connections using TLS 1.1 are rejected. |
| Is TLS 1.2 supported? | **Yes.** |
| Is TLS 1.3 supported? | **Yes.** |

The following encryption methods were successfully negotiated on **all three endpoints** in certificate-validated tests on 16 October 2026:

| Encryption method | Symmetric encryption key length | TLS versions verified |
| --- | --- | --- |
| AES-128-GCM | 128 bits | TLS 1.2 and TLS 1.3 |
| AES-256-GCM | 256 bits | TLS 1.2 and TLS 1.3 |
| ChaCha20-Poly1305 | 256 bits | TLS 1.3 |

These methods provide authenticated encryption, protecting the confidentiality and integrity of data in transit. The negotiated method depends on the capabilities and configuration of the client and server. The bit lengths above refer to the symmetric data-encryption keys, independently of certificate key sizes. The tested TLS 1.2 cipher suites use ECDHE for ephemeral key exchange.

This verification covers connections to these public endpoints, including clients or other servers connecting to them. It does not establish the protocol or encryption settings of every internal service connection, database connection, regional endpoint, or external integration. Those connections require confirmation for the applicable deployment and integration.

## Encryption of stored account information

DigitalOcean Managed Databases use full-volume LUKS encryption with AES-256-XTS; their managed backups use AES-256-CTR. Spaces uses 256-bit AES-XTS on physical disks. See [Encryption at Rest](encryption-at-rest.md) for methods, key management, backup coverage, and the answer to questionnaire item 4.8.

Password hashing and API key hashing are separate controls from encryption of databases, storage volumes, objects, and backups. The controls described above do not establish that every username, account field, or integration secret is individually encrypted, or that all stored data uses a particular encryption algorithm.

For a requirement covering all client account information, obtain a deployment-specific statement from FELLOWPRO AG covering the relevant data stores and backups, encryption methods, key management, and personnel access. A cloud or serverless hosting model alone does not establish these properties.

## Answering a customer security questionnaire

The following describes the confirmed scope:

> DocBits login passwords are stored as salted, one-way hashes. Administrators and DocBits support cannot retrieve the original plaintext password from the stored hash. Users who forget their password must set a new password through the email-based reset procedure to resume password-based sign-in. Configured SSO or passkey methods provide alternative sign-in options.
>
> API keys created through DocBits API Key Management are shown only once and stored as one-way hashes. Neither administrators nor DocBits support can retrieve the full key afterwards. Lost keys must be revoked and replaced.
>
> The public DocBits web application, authentication, and API endpoints listed above support HTTPS with TLS 1.2 and TLS 1.3; TLS 1.0 and TLS 1.1 were rejected in the checks dated 16 October 2026. Verified encryption methods include AES-128-GCM with 128-bit keys and AES-256-GCM with 256-bit keys under TLS 1.2 and TLS 1.3, and ChaCha20-Poly1305 with 256-bit keys under TLS 1.3. This statement covers connections to those endpoints. Encryption of all stored account information and backups, protection of every internal server connection, and personnel access to third-party integration credentials require separate confirmation for the relevant deployment.
