# Secure credentials: verification record

Review date: 16 October 2026. This file records the basis and limits of the English customer response and documentation change. It is outside the GitBook `readme/` root.

## Evidence and scope

| Claim | Evidence | Limit |
| --- | --- | --- |
| Login passwords use salted one-way hashing | `FELLOWPRO/DocBits_Auth`, local revision `0b835879`: `database/models/user.py`, `set_password` and `check_password`; pinned `Werkzeug==3.1.3` in `requirements.txt` | Source review; no production password records were accessed. The current library default is scrypt. Do not claim all historical hashes use the same algorithm. |
| Password recovery sets a new password | Same revision: `blueprints/users.py`, `SendForgetPasswordEmail` and `ResetPasswordFromToken`; `database/models/user.py`, reset token creation and verification; published Getting Access and Signing In guide | Reset flow was reviewed without sending email or changing an account. Do not claim single-use reset tokens or guaranteed session invalidation from this review. |
| Managed DocBits API keys are stored as hashes and shown once | Same revision: `database/dal/organisation_api_key.py`, `generate_key` and `hash_key`; `database/models/organisation_api_key.py`, `to_response_dict`; published API Key Management guide | Applies to keys created through API Key Management. SHA-256 hash and an identifying prefix are stored. This does not establish storage behavior for every legacy token or third-party credential. |
| Public endpoints support TLS 1.2 and TLS 1.3 | Direct certificate-validated TLS connections to `app.docbits.com`, `auth.docbits.com`, and `api.docbits.com`, forcing each version independently | Public listener only. Does not verify origin hops, other regional hostnames, internal service connections, databases, or external ERP endpoints. |
| Those endpoints reject TLS 1.0 and TLS 1.1 | Connections forced to each old version with the client security level lowered to allow the attempt; all six attempts returned `TLSV1_ALERT_PROTOCOL_VERSION` | Observed on the review date; not a continuous configuration guarantee. |
| Public endpoints support AES-128-GCM, AES-256-GCM, and ChaCha20-Poly1305 | Fifteen targeted OpenSSL handshakes: AES-128-GCM and AES-256-GCM under both TLS 1.2 and TLS 1.3, plus ChaCha20-Poly1305 under TLS 1.3, on each of the three endpoints | Each handshake selected one encryption method, verified the certificate and hostname, and succeeded. These are verified supported options; this check does not enumerate every supported cipher suite. |
| Account information is available to organization administrators | `DocBits_Auth/database/models/user.py` and the published Users guide | No assertion that every account field is individually encrypted or that vendor personnel have no access. |
| Connector secrets need separate treatment | `FELLOWPRO/DocBits_API`, local revision `93003bcc59`: `database/models/api_config_maps.py`, `module/helper/password_helper.py`, and `routers/export_configuration/export_router.py`; email/FTP configuration in `doc2app` | Some connectors use reversible encryption and the runtime can obtain usable secrets. A storage column or encryption helper does not prove all credentials are encrypted or establish personnel access policy. |

The user confirmed “Passwort-Hashing und TLS 1.2/1.3” during this review. This confirmation does not extend to databases, backups, every internal connection, or personnel access to integration secrets.

## TLS observations

| Endpoint | TLS 1.0 | TLS 1.1 | TLS 1.2 | TLS 1.3 |
| --- | --- | --- | --- | --- |
| `app.docbits.com` | Protocol version rejected | Protocol version rejected | Negotiated | Negotiated |
| `auth.docbits.com` | Protocol version rejected | Protocol version rejected | Negotiated | Negotiated |
| `api.docbits.com` | Protocol version rejected | Protocol version rejected | Negotiated | Negotiated |

## Cipher suite observations

On the same date, OpenSSL 3.6.3 `s_client` was invoked with the target hostname as both SNI and the hostname to verify, using `-verify_return_error`, a forced TLS version, and a constrained cipher selection. Each of the fifteen attempts exited successfully with `Verification: OK` and the requested protocol and encryption method.

| Protocol | Encryption / key bits | `app.docbits.com` | `auth.docbits.com` and `api.docbits.com` |
| --- | --- | --- | --- |
| TLS 1.2 | AES-128-GCM / 128 | `ECDHE-ECDSA-AES128-GCM-SHA256` | `ECDHE-RSA-AES128-GCM-SHA256` |
| TLS 1.2 | AES-256-GCM / 256 | `ECDHE-ECDSA-AES256-GCM-SHA384` | `ECDHE-RSA-AES256-GCM-SHA384` |
| TLS 1.3 | AES-128-GCM / 128 | `TLS_AES_128_GCM_SHA256` | `TLS_AES_128_GCM_SHA256` |
| TLS 1.3 | AES-256-GCM / 256 | `TLS_AES_256_GCM_SHA384` | `TLS_AES_256_GCM_SHA384` |
| TLS 1.3 | ChaCha20-Poly1305 / 256 | `TLS_CHACHA20_POLY1305_SHA256` | `TLS_CHACHA20_POLY1305_SHA256` |

For TLS 1.2, both ECDSA and RSA variants of the selected AES-GCM method were offered; the endpoint selected the variant shown. For TLS 1.3, only the named suite was offered. All tested TLS 1.2 connections reported an X25519 ephemeral key. The 128/256-bit values in the customer answer refer to symmetric encryption keys, not certificate keys, key-exchange group sizes, or SHA digest lengths.

## Remaining customer assurances

Before answering the entire questionnaire with an unqualified “yes”, obtain the deployment-specific evidence for:

1. Encryption at rest for account databases, relevant object or volume storage, and backups, including algorithms and key management.
2. Transport protection for internal service and database connections and for the customer's specific integration path.
3. Which vendor roles may access account information or usable integration secrets, and the controls and audit records governing that access.

The customer text explicitly limits its claims while these items remain unconfirmed. Cloud/serverless architecture and ISO certification are not substitutes for this evidence. This change prepares the English documentation and response; publication and translations are not evidenced by a local edit or draft pull request.

## Published sources checked

* [Security & Compliance FAQ](https://docs.docbits.com/overview-and-basics/security-and-compliance-faq)
* [API Key Management](https://docs.docbits.com/administration-and-setup/settings/global-settings/integration/api-key-management)
* [Getting Access and Signing In](https://docs.docbits.com/end-user-and-partner-section/end-user-section/getting-access-and-signing-in)
* [Two-Factor Authentication](https://docs.docbits.com/overview-and-basics/two-factor-authentication)
* [Users](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/users)
