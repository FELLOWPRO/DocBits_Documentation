---
description: "DocBits 在 DigitalOcean 上的静态数据加密，包括数据库、Spaces、备份覆盖范围以及问卷第 4.8 项。"
---

# 静态数据加密

DocBits 使用 DigitalOcean Managed Databases 和 DigitalOcean Spaces。**2026 年 10 月 16 日**的审查确认，欧盟生产环境使用托管 PostgreSQL、OpenSearch 和 Valkey 服务，部署在法兰克福。[安全与合规常见问题](security-and-compliance-faq.md)说明了 Spaces 的存储用途。

以下内容介绍 DigitalOcean 发布的这些服务的加密控制措施。本地部署以及存储在其他系统中的副本需要单独评估。

## 加密方法和范围

| 存储服务 | 静态数据加密 | 覆盖范围 |
| --- | --- | --- |
| Managed Databases：PostgreSQL、OpenSearch、Valkey | LUKS 全卷加密；使用 `aes-xts-plain64:sha256` 和 512 位 XTS 密钥材料 | 底层数据库服务卷，包括存储在这些卷上的数据。这是存储层保护，并不表示对每个数据库字段进行单独加密。 |
| Managed Database 备份 | AES-256 CTR 模式加密，使用 HMAC-SHA256 确保完整性；每个文件的密钥由 RSA-3072 保护 | 由托管数据库服务创建的备份。其他导出内容和备份副本需要单独验证。 |
| DigitalOcean Spaces | 256 位 AES-XTS 全盘加密 | 物理存储磁盘上的数据。这与可选的对象级或客户端加密相互独立。 |
| DigitalOcean Volumes（如有使用） | 对存储集群进行 LUKS 加密 | 这些块存储卷上的数据；卷快照沿用该加密保护。 |

XTS 使用两个 AES 密钥。托管数据库服务使用的 512 位组合 XTS 密钥材料对应两个 256 位 AES 密钥（AES-256-XTS），并非使用 512 位密钥的 AES 密码。

数据库和备份的详细信息来自 DigitalOcean 的[托管数据库安全模型](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases)。
[Spaces 安全模型](https://www.digitalocean.com/security/shared-responsibility-model-spaces)确认了静态数据加密；[App Platform 安全模型](https://www.digitalocean.com/security/shared-responsibility-model-app-platform)说明 Spaces 物理磁盘使用 256 位 AES-XTS。[卷功能](https://docs.digitalocean.com/products/volumes/details/features/)说明了卷和快照的覆盖范围。

## 密钥管理和授权访问

DigitalOcean 管理上述基础设施加密。对于 Managed Databases，DigitalOcean 说明每个实例和卷都会使用随机生成的密钥，并在实例销毁时丢弃该密钥。托管数据库备份的每个文件使用随机密钥，并由服务专用的 RSA 密钥对保护。

存储加密可保护存储介质上的数据。经过授权的应用程序和数据库用户仍可通过服务读取数据。这并不能证明供应商人员无法访问账户信息，也不能证明每个字段都经过应用层加密。登录密码和 API 密钥哈希属于单独的控制措施；请参阅[凭据的安全存储](secure-storage-of-credentials.md)。

Spaces 还支持[使用客户提供密钥的 SSE-C](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/)。这项可选功能并不能证明 DocBits 使用 SSE-C 或客户管理的加密密钥。

## 备份覆盖范围

托管数据库备份、卷快照和 Droplet 镜像备份是不同的产品。DigitalOcean 的 [Droplet 备份限制](https://docs.digitalocean.com/products/backups/details/limits/)指出，这些镜像备份的静态数据未加密。本次审查未能确认 DocBits 是否使用该备份产品。

因此，上述控制措施仅支持针对所列服务的限定性声明。要将保障范围扩展到所有副本，必须先确认其他数据库转储、导出文件、长期归档和灾难恢复副本的存储目的地、加密方式及密钥管理方式。仅有备份计划或云端/无服务器架构，并不能证明这些副本均受到上述保护。

## 4.8 — 静态数据加密类型

以下措辞可用于说明已记录的范围：

> DocBits 使用 DigitalOcean Managed Databases 和 Spaces。托管数据库数据在静态状态下通过 LUKS 全卷加密，使用 AES-256-XTS（512 位组合 XTS 密钥材料）。托管数据库备份使用 AES-256-CTR，并通过 HMAC-SHA256 保护完整性，通过 RSA-3072 保护每个文件的加密密钥。Spaces 在其物理存储上使用 256 位 AES-XTS 全盘加密。
>
> 这些是存储层控制措施，覆盖受保护卷和磁盘上的数据；这并不意味着对每个数据库字段进行单独加密。DigitalOcean 管理基础设施加密密钥。此声明适用于所列托管服务。对于其他导出内容、归档和备份副本，必须针对相关部署单独确认其加密和密钥管理方式。
