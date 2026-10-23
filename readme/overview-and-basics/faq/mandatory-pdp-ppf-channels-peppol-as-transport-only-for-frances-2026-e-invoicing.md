# 法国 2026 年电子发票：必须使用 PDP/PPF 渠道，PEPPOL 仅作为传输方式

## 国内 B2B 电子发票必须通过 PDP 或 PPF

根据法国 2026 年电子发票强制规定，企业不能仅依靠 PEPPOL 网络交换国内 B2B 发票。法律要求，法国增值税登记企业之间的所有发票都必须通过经认证的私人平台（PDP）或国家公共发票门户（PPF）传输，以满足法律[要求](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) ￼。换言之，企业将不再直接向客户发送发票，而必须通过获批的电子发票平台（PDP）或政府[门户](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) ￼进行传输。这样可确保税务机关实时收到所需数据。仅通过 PEPPOL 交换发票而不经过认可的 PDP/PPF，将无法满足强制规定的数据报告和传输义务。

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="发票生命周期图，从供应商经 Submitted、Received by the platform 和 Made available 状态，到 Rejected、Refused、Disputed、Partially approved、In hand 和 Completed 等结果"><figcaption></figcaption></figure>

### 服务方案简介

API 模式使用户可以通过合作伙伴组织已部署的 IT 工具，使用其可用的所有功能。有两种集成方式：

### ·       集成到信息系统（IS）中：

API 直接集成到开具和接收发票的各方所使用的信息系统或管理软件中，也可集成到其无纸化处理运营商（OD）的系统中。这样，用户就能直接通过日常使用的 IT 工具（无论是内部工具还是 OD 提供的工具）访问解决方案的功能及其升级。

API 也可以集成到 PDP 的信息系统中，以提供更大的灵活性（相比 EDI 模式），其中一些 API 专供 PDP 使用。

### ·       集成到第三方软件中：

软件开发商可以基于这些 API 提供软件。根据开发商选择的模式，连接可以由开发商完成，也可以由客户在其信息系统中安装或部署软件时自行完成。此类第三方软件会通过添加与 PPF 通信的层来扩展客户的信息系统。

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="显示 Issuer OD-PDP 和 Receiver OD-PDP 通过服务门户和第三方软件相连接的图，两者之间有一个数据控制与恢复步骤"><figcaption></figcaption></figure>

## PEPPOL 仅用作互操作层

法国正在将 PEPPOL 纳入其基础设施，但仅将其作为 PDP 框架内的传输层，而不是独立的合规渠道。法国税务机关（DGFiP）将成为 Peppol Authority，以统一 PDP 之间的[互联](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html)方式。所有经认证的 PDP 都必须通过 PEPPOL 网络互联，以交换[发票](https://nymus.be/fr/facturation-electronique-en-france/)。这意味着 PEPPOL 将促进授权平台之间的互操作，而不会取代对这些平台的需求。实际上，企业只有通过使用 PEPPOL 发送或接收发票的 PDP（或在其有限职责范围内运行的 PPF），才能使用 PEPPOL。官方指南也已确认这一点：公共门户侧重于数据收集，而发票分发将完全由 PDP 负责，这些 PDP 会利用 [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) 等网络进行[交换](https://nymus.be/fr/facturation-electronique-en-france/)。

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt="三个编号控制层的图：技术控制、应用控制以及功能与业务控制，每层都汇入后续的流程步骤"><figcaption></figcaption></figure>

## 枢纽连接：

枢纽会向客户提供 Web 或应用程序解决方案，以便客户发起各类 API 调用。**因此，API 调用由枢纽代表其所有客户发起**。在这种情况下，每个合作伙伴都必须拥有一个技术账户，但只有枢纽需要在 PISTE 下注册应用程序并连接到 PPF。

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="中心枢纽模型图，显示一个合作伙伴、一个技术账户、该枢纽、PISTE 下的一个应用程序以及一个连接"><figcaption></figcaption></figure>



来源：法国《2024 年财政法》第 91 条（由 EY 概述）规定，电子发票必须通过经认证的 PDP 或国家门户发送。法国税务机关的更新进一步明确，2024 年改革后，企业必须使用已注册的 PDP 进行 B2B 电子发票处理（PPF 将不再作为免费交换平台）。PEPPOL 正在用于连接这些 PDP，而不是作为系统之外的替代渠道。这证实，仅使用 PEPPOL 网络并不足以合规——要符合法国 2026 年电子发票制度的要求，必须接入 PPF 或经认证的 PDP，而 PEPPOL 仅作为这些平台之间的底层传输网络。

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="EDI 流和 Flow 2 via API 接收图，先通过语义格式、目录和数据一致性的功能控制，然后并入开票数据，最后得到已提交的发票"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="EDI 流和 API 流先通过功能控制和特定业务规则，随后发票被拒绝或退回，或者被接收并可供使用的图"><figcaption></figcaption></figure></div>
