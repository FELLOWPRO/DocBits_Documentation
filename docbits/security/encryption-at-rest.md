---
description: Encryption at rest for DocBits on DigitalOcean, including databases, Spaces, and backup coverage.
---

# Encryption at Rest

DocBits uses DigitalOcean Managed Databases and DigitalOcean Spaces. The review on **16 October 2026** confirmed managed PostgreSQL, OpenSearch, and Valkey services for EU production in Frankfurt. The [Security & Compliance FAQ](security-and-compliance-faq.md) documents the use of Spaces for storage.

The following describes DigitalOcean's published encryption controls for these services. On-premises installations and copies stored in other systems require their own assessment.

## Encryption methods and scope

| Storage service | Encryption at rest | Coverage |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | LUKS full-volume encryption; `aes-xts-plain64:sha256` with 512-bit XTS key material | The underlying database service volumes, including data stored on those volumes. This is storage-level protection, not a claim of separate encryption for each database field. |
| Managed Database backups | AES-256 in CTR mode, with HMAC-SHA256 for integrity; per-file keys protected by RSA-3072 | Backups created by the managed database service. Additional exports and backup copies require separate verification. |
| DigitalOcean Spaces | 256-bit AES-XTS full-disk encryption | Data on the physical storage disks. This is separate from optional object-level or client-side encryption. |
| DigitalOcean Volumes, where used | LUKS encryption of the storage cluster | Data on these block-storage volumes; volume snapshots inherit the encryption. |

XTS uses two AES keys. The managed database service's 512-bit combined XTS key material corresponds to two 256-bit AES keys (AES-256-XTS), not an AES cipher with a 512-bit key.

The database and backup details come from DigitalOcean's [Managed Databases security model](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). The [Spaces security model](https://www.digitalocean.com/security/shared-responsibility-model-spaces) confirms encryption at rest; the [App Platform security model](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) specifies 256-bit AES-XTS for Spaces physical disks. [Volume Features](https://docs.digitalocean.com/products/volumes/details/features/) documents volume and snapshot coverage.

## Key management and authorized access

DigitalOcean manages the infrastructure encryption described above. For Managed Databases, it documents a randomly generated key for each instance and volume, discarded when the instance is destroyed. Managed database backups use a random key per file, protected by a service-specific RSA key pair.

Storage encryption protects data on storage media. Authorized applications and database users can still read data through the service. It does not establish that vendor personnel cannot access account information, or that every field has application-level encryption. Login password and API key hashing are separate controls; see [Secure Storage of Credentials](secure-storage-of-credentials.md).

Spaces also supports [SSE-C with customer-provided keys](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). This optional capability does not establish that DocBits uses SSE-C or customer-managed encryption keys.

## Backup encryption

Backups created by DigitalOcean Managed Databases are encrypted with AES-256-CTR and protected against undetected changes with HMAC-SHA256. The per-file encryption keys are protected by RSA-3072. Volume snapshots inherit the encryption of the underlying DigitalOcean volume. These details describe the backup capabilities of the named managed services.

## Types of Encryption at Rest

The main encryption methods used by the named services are summarized below:

> DocBits uses DigitalOcean Managed Databases and Spaces. Managed database data is encrypted at rest at the full-volume level using LUKS with AES-256-XTS (512-bit combined XTS key material). Managed database backups use AES-256-CTR with HMAC-SHA256 integrity protection and RSA-3072 protection of the per-file encryption keys. Spaces uses 256-bit AES-XTS full-disk encryption on its physical storage.
>
> These are storage-level controls covering the data on the protected volumes and disks; they do not imply separate encryption of every database field. DigitalOcean manages the infrastructure encryption keys. This statement covers the named managed services.
