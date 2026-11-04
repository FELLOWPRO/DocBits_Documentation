# 数据存储、保留与删除

您的数据在 DocBits 手中十分安心。我们在两个区域运营 DocBits：**德国法兰克福（EU）**和**美国旧金山（USA）**，您可以在设置中自行决定文档在我们这里保留多久。本页介绍存储位置、保留期限和删除方式。

**文档更新日期：2026年10月28日。**

## 概览

- **区域由您选择：**欧盟客户使用法兰克福，美国客户使用旧金山。
- **您的数据留在您所在的区域。**欧盟数据托管在法兰克福，美国数据托管在旧金山，不同区域的数据绝不混合。
- **文档保留多久由您掌控**，设置位置为**文档处理 → 文档过期时间**（[前往该设置](../administration-and-setup/settings/document-processing/documents-expiry.md)）。
- **临时 OCR 文件**会在 90 分钟后自动删除。
- **我们乐意提供帮助：**我们的团队会通过 **compliance@fellowpro.com** 解答问题并处理删除请求。

## 您的数据存储在哪里？

| 区域 | 适用对象 | 位置 | 使用的服务 |
| --- | --- | --- | --- |
| **EU** | 所有欧盟客户 | **德国法兰克福（Frankfurt am Main）** | DigitalOcean Kubernetes（区域 `fra1`），搭配托管的 PostgreSQL、OpenSearch 和 Valkey 数据库（`fra1`），以及用于文件存储的 DigitalOcean Spaces |
| **USA** | 美国客户 | **美国旧金山** | DigitalOcean Kubernetes（区域 `sfo2`），搭配托管的 PostgreSQL、OpenSearch 和 Valkey 数据库（`sfo2`） |

**欧盟的备份：**法兰克福是主要备份位置，阿姆斯特丹（荷兰）是次要备份位置，因此您的备份副本同样保留在欧盟境内。

**已连接的系统：**如果您将文档导出到 ERP、Infor IDM 或其他目标系统，这些副本将按该系统的规则存储在该系统所在的位置。这部分由您自己掌控。

## 数据保留多久？

| 数据类型 | 保留期限 |
| --- | --- |
| **已上传的文档和提取的数据** | 由您通过[文档过期时间](../administration-and-setup/settings/document-processing/documents-expiry.md)控制（见下文）。 |
| **临时 OCR 文件** | 在 **90 分钟**后自动清理。这仅适用于临时 OCR 存储，不影响您在 DocBits 中的文档。 |
| **客户可访问的日志**（可在[活动日志](../administration-and-setup/settings/log-settings/README.md)中查看） | **30 天** |
| **内部日志** | **3 个月** |
| **每日数据库备份（托管）** | **7 天**；更早的备份会被自动删除。 |
| **额外的每日备份（SnapShooter）** | 适用于生产和沙盒数据库；保留期限按环境分别设定。 |
| **Cookie 和浏览器存储** | 因用途而异，请参阅 [Cookie 与浏览器存储](cookies-and-browser-storage.md)。 |

此外，我们还会进行每日、每周、每季度和每年的备份。如有需要，我们很乐意向您提供这些备份类型在您所在环境中的确切保留期限。

## 如何设置文档的保留期限

在“设置”中，打开**文档处理 → 文档过期时间**。这里有两项设置：

- **Delete document after：**文档的保留时长。
- **Delete finished document after：**已完成、已完全处理并已导出的文档的保留时长。

可选项为 **Default**、**48 Hours**、**1 Week**、**2 Weeks** 和 **4 Weeks**。**Default** 表示采用系统默认值。如果您想要固定的期限，只需选择其中一个时长即可。完整说明请参阅[文档过期时间指南](../administration-and-setup/settings/document-processing/documents-expiry.md)。

## 数据删除时会发生什么？

文档过期时间功能会在您选定的期限结束后自动删除您的文档。这与临时 OCR 文件的清理、日志的过期以及备份的保留是相互独立的。

请注意：

- **备份按各自的计划过期。**因此，在在线系统中删除文档不会立即清除备份副本，而是在相应备份期限结束时才会清除。
- **导出的副本归您所有。**DocBits 删除文档后，您的 ERP 或归档系统中的副本仍会保留。请根据您自身的要求在那里规划保留期限。

## 有疑问或需要提交删除请求？我们随时为您服务

如需了解您部署的相关信息或提交删除请求，请写信至 **compliance@fellowpro.com**。请告知您的组织、涉及的环境、数据类型以及所需的范围。请不要发送密码或 API 密钥。

我们也乐意为您确认：

- 您当前生效的区域和实际生效的保留设置，包括系统默认值。
- 删除期限从何时开始，以及清理多久运行一次。
- 文档、提取数据、搜索索引和衍生数据的删除范围。
- 所有备份类型的位置和保留期限，包括合同终止之后的情况。

## 更多安全信息

- [DocBits (FELLOWPRO AG) — 安全与合规问卷](security-and-compliance-faq.md)
- [静态数据加密](encryption-at-rest.md)
- [凭据的安全存储](secure-storage-of-credentials.md)
- [Cookie 与浏览器存储](cookies-and-browser-storage.md)
