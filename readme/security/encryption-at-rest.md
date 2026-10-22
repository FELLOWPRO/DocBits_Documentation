---
description: Versleuteling van opgeslagen DocBits-gegevens bij DigitalOcean, inclusief databases, Spaces en back-ups.
---

# Versleuteling van opgeslagen gegevens

DocBits gebruikt DigitalOcean Managed Databases en DigitalOcean Spaces. De controle op **16 oktober 2026** bevestigde beheerde PostgreSQL-, OpenSearch- en Valkey-diensten voor EU-productie in Frankfurt. De [FAQ over beveiliging en compliance](security-and-compliance-faq.md) beschrijft het gebruik van Spaces voor opslag.

Deze pagina beschrijft de versleutelingsmaatregelen die DigitalOcean voor deze diensten publiceert. Lokale installaties en kopieën in andere systemen vereisen een eigen beoordeling.

## Versleutelingsmethoden en reikwijdte

| Opslagdienst | Versleuteling van opgeslagen gegevens | Dekking |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | Volledige volumeversleuteling met LUKS; `aes-xts-plain64:sha256` met 512 bits XTS-sleutelmateriaal | De onderliggende volumes van de databasedienst, inclusief de gegevens op die volumes. Dit beschermt op opslagniveau en betekent geen afzonderlijke versleuteling van elk databaseveld. |
| Back-ups van Beheerde Databases | AES-256 in CTR-modus, met HMAC-SHA256 voor integriteit; sleutels per bestand beschermd met RSA-3072 | Back-ups die de beheerde databasedienst maakt. Aanvullende exports en back-upkopieën vereisen afzonderlijke verificatie. |
| DigitalOcean Spaces | Volledige schijfversleuteling met 256-bits AES-XTS | Gegevens op de fysieke opslagschijven. Dit staat los van optionele versleuteling per object of aan de clientzijde. |
| DigitalOcean Volumes, indien gebruikt | LUKS-versleuteling van het opslagcluster | Gegevens op deze blokopslagvolumes; volumesnapshots nemen de versleuteling over. |

XTS gebruikt twee AES-sleutels. De 512 bits gecombineerd XTS-sleutelmateriaal van de beheerde databasedienst komen overeen met twee AES-sleutels van 256 bits (AES-256-XTS), niet met een AES-algoritme met een sleutel van 512 bits.

De details voor databases en back-ups komen uit het [beveiligingsmodel voor Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). Het [beveiligingsmodel voor Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) bevestigt versleuteling van opgeslagen gegevens; het [beveiligingsmodel voor App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) noemt 256-bits AES-XTS voor de fysieke schijven van Spaces. De [functies van Volumes](https://docs.digitalocean.com/products/volumes/details/features/) beschrijven de dekking van volumes en snapshots.

## Sleutelbeheer en geautoriseerde toegang

DigitalOcean beheert de beschreven infrastructuurversleuteling. Voor Managed Databases documenteert de aanbieder een willekeurig gegenereerde sleutel per instantie en volume, die bij het vernietigen van de instantie wordt verwijderd. Back-ups van beheerde databases gebruiken een willekeurige sleutel per bestand, beschermd met een RSA-sleutelpaar per dienst.

Opslagversleuteling beschermt gegevens op opslagmedia. Geautoriseerde applicaties en databasegebruikers kunnen de gegevens nog steeds via de dienst lezen. Dit toont niet aan dat medewerkers van de leverancier geen accountgegevens kunnen inzien of dat elk veld op applicatieniveau versleuteld is. Het hashen van wachtwoorden en API-sleutels is een afzonderlijke maatregel; zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md).

Spaces ondersteunt ook [SSE-C met door de klant aangeleverde sleutels](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Deze optionele mogelijkheid toont niet aan dat DocBits SSE-C of door klanten beheerde versleutelingssleutels gebruikt.

## Versleuteling van back-ups

Back-ups die door DigitalOcean Managed Databases worden gemaakt, zijn versleuteld met AES-256-CTR en worden met HMAC-SHA256 beschermd tegen onopgemerkte wijzigingen. De versleutelingssleutels per bestand zijn beschermd met RSA-3072. Volumesnapshots nemen de versleuteling van het onderliggende DigitalOcean-volume over. Deze informatie beschrijft de back-upfuncties van de genoemde beheerde diensten.

## Soorten versleuteling van opgeslagen gegevens

Hieronder staan de belangrijkste versleutelingsmethoden van de genoemde diensten:

> DocBits gebruikt DigitalOcean Managed Databases en Spaces. Opgeslagen gegevens van beheerde databases worden op volledig volumeniveau versleuteld met LUKS en AES-256-XTS (512 bits gecombineerd XTS-sleutelmateriaal). Back-ups van beheerde databases gebruiken AES-256-CTR met HMAC-SHA256 voor integriteit en RSA-3072 voor bescherming van de versleutelingssleutels per bestand. Spaces gebruikt volledige schijfversleuteling met 256-bits AES-XTS op de fysieke opslag.
>
> Deze maatregelen op opslagniveau dekken de gegevens op de beschermde volumes en schijven; ze betekenen geen afzonderlijke versleuteling van elk databaseveld. DigitalOcean beheert de infrastructuurversleutelingssleutels. Deze verklaring dekt de genoemde beheerde diensten.
