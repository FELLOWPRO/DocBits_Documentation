# 架构

## **DocBits 云端客户**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="DocBits 云端客户架构"><figcaption></figcaption></figure>

## DocBits 本地部署

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="DocBits 本地部署架构"><figcaption></figcaption></figure>

Doc**Bits** 通过 ION API、ION Desk 和 Infor 标准 BOD 与 Infor LN/M3 无缝集成。通过 API 集成，我们可以将数据导出到 Infor，并在 Doc**Bits** 中执行主数据验证。

## **DocBits Operator 架构**

组件之间的所有连接均使用行业标准加密协议进行保护。SSH、HTTPS 和其他安全通道可确保整个系统中的数据完整性和机密性。

**本地部署：**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt="Operator On-Prem 架构图，显示客户端计算机上的 DocAgent 连接 Prefect API 和 DocBits 云端"><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[Prefect 本地设置要求](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**云端**：

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt="Operator Cloud 架构图，显示 Chrome 扩展、DocBits Operator Cloud、DocFlow 和 DocBits AI 之间交换任务与响应消息"><figcaption></figcaption></figure>

## 将数据导出到 Infor

我们使用 ION API 将带有属性的 PDF 发送到 IDM，并将 BOD Sync.CaptureDocument 发送到 ION Desk。在 ION Desk 中，我们根据正在处理的文档类型，将 [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) 转换为所需的目标 BOD。随后，这些转换后的 Infor BOD 会自动导入 LN 或 M3。

{% hint style="info" %}
导出到 [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## 在 DocBits 中验证主数据

为识别供应商或比较/匹配采购订单行，我们会在 LN/M3 中激活一个触发器，将 Sync.RemitToPartyMaster、Sync.SupplierPartyMaster 和 Sync.PurchaseOrder BOD 发送到 Doc**Bits**。我们在 ION Desk 中配置此流程，将数据流定义到 Doc**Bits** 的特定连接点。

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt="DocBits 的 Kubernetes 集群架构图，包含负载均衡器、Redis、PostgreSQL、工作线程 Pod 和 Spaces 数据存储"><figcaption></figcaption></figure>

{% hint style="info" %}
[主数据验证](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## 电子邮件导入 OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt="Office 365 邮件导入图，显示 Microsoft Graph API 向 DocBits 邮件服务和主系统颁发访问令牌"><figcaption></figcaption></figure>
