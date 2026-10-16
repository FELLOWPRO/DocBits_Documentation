---
description: Cifragem em repouso do DocBits na DigitalOcean, incluindo bases de dados, Spaces e cobertura de cópias de segurança.
---

# Cifragem em repouso

O DocBits utiliza DigitalOcean Managed Databases e DigitalOcean Spaces. A verificação de **16 de outubro de 2026** confirmou serviços geridos de PostgreSQL, OpenSearch e Valkey para produção da UE em Frankfurt. As [perguntas frequentes sobre segurança e conformidade](../overview-and-basics/security-and-compliance-faq.md) documentam a utilização de Spaces para armazenamento.

Esta página descreve os controlos de cifragem publicados pela DigitalOcean para estes serviços. As instalações locais e as cópias armazenadas noutros sistemas exigem uma avaliação própria.

## Métodos de cifragem e âmbito

| Serviço de armazenamento | Cifragem em repouso | Cobertura |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | Cifragem de volumes completos com LUKS; `aes-xts-plain64:sha256` com 512 bits de material de chave XTS | Os volumes subjacentes do serviço de base de dados, incluindo os dados neles armazenados. É proteção ao nível do armazenamento, não uma afirmação de cifragem separada de cada campo. |
| Cópias de segurança de Managed Databases | AES-256 no modo CTR, com HMAC-SHA256 para integridade; chaves por ficheiro protegidas por RSA-3072 | Cópias criadas pelo serviço de base de dados gerida. Exportações e cópias adicionais exigem verificação separada. |
| DigitalOcean Spaces | Cifragem integral dos discos com AES-XTS de 256 bits | Dados nos discos físicos de armazenamento. É distinta da cifragem opcional por objeto ou do lado do cliente. |
| DigitalOcean Volumes, quando utilizados | Cifragem LUKS do cluster de armazenamento | Dados nestes volumes de armazenamento em blocos; os snapshots dos volumes herdam a cifragem. |

O XTS utiliza duas chaves AES. Os 512 bits de material combinado de chave XTS do serviço de base de dados gerida correspondem a duas chaves AES de 256 bits (AES-256-XTS), não a um algoritmo AES com uma chave de 512 bits.

Os detalhes sobre bases de dados e cópias provêm do [modelo de segurança de Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). O [modelo de segurança de Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) confirma a cifragem em repouso; o [modelo de segurança de App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) especifica AES-XTS de 256 bits para os discos físicos de Spaces. As [funcionalidades de Volumes](https://docs.digitalocean.com/products/volumes/details/features/) documentam a cobertura de volumes e snapshots.

## Gestão de chaves e acesso autorizado

A DigitalOcean gere a cifragem de infraestrutura descrita. Para Managed Databases, documenta uma chave gerada aleatoriamente por instância e volume, eliminada quando a instância é destruída. As cópias de segurança de bases de dados geridas utilizam uma chave aleatória por ficheiro, protegida por um par de chaves RSA específico do serviço.

A cifragem do armazenamento protege os dados nos suportes. As aplicações e os utilizadores autorizados da base de dados continuam a poder ler os dados através do serviço. Isto não demonstra que o pessoal do fornecedor não possa aceder a informações de conta, nem que cada campo esteja cifrado ao nível da aplicação. O hashing de palavras-passe e chaves API é um controlo separado; consulte [Armazenamento seguro de credenciais](../overview-and-basics/secure-storage-of-credentials.md).

Spaces também suporta [SSE-C com chaves fornecidas pelo cliente](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Esta capacidade opcional não demonstra que o DocBits utilize SSE-C ou chaves de cifragem geridas pelo cliente.

## Cifragem de cópias de segurança

As cópias de segurança criadas pelo DigitalOcean Managed Databases são cifradas com AES-256-CTR e protegidas contra alterações não detetadas através de HMAC-SHA256. As chaves de cifragem de cada ficheiro são protegidas por RSA-3072. Os snapshots de volumes herdam a cifragem do volume DigitalOcean subjacente. Estas informações descrevem as funções de cópia de segurança dos serviços geridos indicados.

## Tipos de cifragem em repouso

Os principais métodos de cifragem dos serviços indicados estão resumidos abaixo:

> O DocBits utiliza DigitalOcean Managed Databases e Spaces. Os dados das bases de dados geridas são cifrados em repouso ao nível de volumes completos com LUKS e AES-256-XTS (512 bits de material combinado de chave XTS). As cópias de segurança das bases de dados geridas utilizam AES-256-CTR com proteção de integridade HMAC-SHA256 e RSA-3072 para proteger as chaves de cifragem de cada ficheiro. Spaces utiliza cifragem integral dos discos com AES-XTS de 256 bits no armazenamento físico.
>
> Estes controlos ao nível do armazenamento abrangem os dados nos volumes e discos protegidos; não implicam cifragem separada de cada campo da base de dados. A DigitalOcean gere as chaves de cifragem da infraestrutura. Esta declaração abrange os serviços geridos indicados.
