# Encryption at rest: verification record

Review date: 16 October 2026. This record supports questionnaire item 4.8 and the multilingual public `overview-and-basics/encryption-at-rest.md` page. It is outside the published GitBook content roots.

## Deployment evidence and limits

A read-only DigitalOcean Managed Databases inventory returned online, production-named DocBits PostgreSQL, OpenSearch, and Valkey clusters in `fra1` (Frankfurt). The existing English Security & Compliance FAQ identifies DigitalOcean Spaces as storage in Frankfurt. This supports identifying the relevant provider products; it is not a host-level audit of encryption or a complete trace of every application's storage path.

Only cluster names, engines, regions, status, and tags were used from the database inventory response. Connection details, passwords, users, certificates, and keys were excluded from displayed output and this record. No database contents were queried. No infrastructure configuration was changed.

A read-only volume inventory also returned DigitalOcean block-storage volumes associated with Kubernetes. These were not mapped to individual application data paths. The public page therefore states the documented Volume encryption property **where that product is used**, rather than claiming that every container or node filesystem is covered.

No inventory of backup contents or additional export/archive destinations was collected. The managed-backup statement uses the provider's documented controls for that service. It does not verify the wider daily/weekly/quarterly/yearly backup schedule or every Frankfurt/Amsterdam copy described elsewhere in the FAQ. No conclusion is drawn about DocBits use of Droplet image backups.

## Provider evidence

| Source | Relevant published property | Public wording / limit |
| --- | --- | --- |
| [Managed Databases security model](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases) | All Managed Database clusters use LUKS. Full-volume encryption uses `aes-xts-plain64:sha256` and 512-bit key material. A random key is generated per instance and volume and discarded at instance destruction. Managed backups use AES-256-CTR, HMAC-SHA256, random per-file encryption keys, and a service-specific RSA-3072 key pair protecting those keys. | Applies to the managed services identified above. XTS has two AES keys: combined 512-bit key material means AES-256-XTS, not “AES-512”. No fixed periodic key-rotation interval or customer key-management feature is asserted. |
| [PostgreSQL security](https://docs.digitalocean.com/products/databases/postgresql/how-to/secure/), [OpenSearch responsibility model](https://docs.digitalocean.com/products/databases/opensearch/concepts/responsibility-model/), [Valkey security](https://docs.digitalocean.com/products/databases/valkey/how-to/secure/) | Product documentation independently states LUKS encryption at rest. | Confirms the named managed engine types are within the documented service controls. |
| [Spaces security model](https://www.digitalocean.com/security/shared-responsibility-model-spaces) | Spaces data is encrypted at rest; client-side encryption can add a separate control. | Do not mistake optional object encryption for the absence of physical storage encryption. |
| [App Platform security model](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) | Its storage section specifically describes Spaces physical disks as encrypted using 256-bit AES-XTS full-disk encryption. | Used for the **Spaces** algorithm statement, together with the Spaces-specific source. This does not assert DocBits uses App Platform. |
| [Volumes features](https://docs.digitalocean.com/products/volumes/details/features/) | LUKS encryption of the storage cluster; volume snapshots inherit encryption. | No extra assumption about the standalone Volume cipher/key length or Droplet root disks. |
| [Spaces S3 compatibility](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/) | Optional SSE-C; bucket-level encryption settings are unsupported. | Does not establish DocBits uses SSE-C, BYOK, or customer-managed encryption keys. S3 API compatibility does not establish AWS hosting. |
| [Droplet backup limits](https://docs.digitalocean.com/products/backups/details/limits/) | Droplet image backups are not encrypted at rest. | Separate product from Managed Database backups and Volume snapshots. Do not generalize any one backup product's controls to all DigitalOcean or DocBits backups. |

The sources were read on the review date. Product security models provide the detailed algorithms that the shorter product documentation does not specify. A cloud/serverless architecture, a TLS cipher result, a hashing implementation, or ISO certification alone is not evidence of storage encryption.

## Scope of the documentation change

- Add the same at-rest page, service table, key-management explanation, backup limits, and reusable 4.8 answer in all eight published languages.
- Maintain both English roots (`readme/` and `docbits/`) and the seven language branches plus publication folders documented in [the credential verification record](secure-credentials-verification-2026-10-16.md#publication-and-translation-mapping).
- Link the page from navigation, the credential-storage page, and FAQ questions 1, 3, and 5.
- Replace stale AWS/S3 hosting and storage references in the seven translated FAQs (questions 1, 14, and 15) with the DigitalOcean facts already established in English; limit question 1's production statement to the EU deployment reviewed.
- Keep FAQ question 5 partially confirmed because complete coverage of other copies, application field encryption, personnel access, and all internal connections has not been established.

The public response asserts storage-level encryption for named managed services. It does not assert field-by-field encryption, absence of authorized plaintext access, universal backup coverage, or deployment of optional customer key features.

## Validation

The nine maintained content roots (two English roots plus seven translations) passed front-matter, GitBook-tag, navigation, and complete import-structure validation using the repository's language-bridge validator. The 63 relative links in the new pages and added cross-references resolve locally. All language versions retain the same service rows, algorithms, key lengths, optional SSE-C distinction, and backup-product limitation. New page contents and additions to existing pages match their language source branches; both English roots also match for this change. `git diff --check` passed. Existing missing-image warnings in unrelated translated pages remain outside this text-only change.
