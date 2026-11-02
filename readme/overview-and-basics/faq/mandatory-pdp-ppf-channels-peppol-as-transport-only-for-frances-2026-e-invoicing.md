# 法国电子发票：获批平台与 PEPPOL

## 当前规则及实施时间

对于法国改革范围内、增值税纳税企业之间的国内 B2B 发票，必须通过**获批平台（plateforme agréée，PA；原称 PDP）**进行交换。**公共发票门户（PPF）**承担公共目录和税务数据汇总职能，并非这些发票的另一种交换平台。

* **2026 年 9 月 1 日：** 所有适用企业均须能够接收电子发票。大型企业（GE）和中间规模企业（ETI，法国企业分类）还须从该日起开具电子发票，并履行电子报告（e-reporting）义务。
* **2027 年 9 月 1 日：** 开具电子发票及电子报告义务适用于中小企业（PME）和微型企业。

具体义务取决于交易是否属于适用范围及企业类别。请参阅官方的[获批平台说明](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees)、[实施时间表](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation)及[主管部门答复](https://www.senat.fr/questions/base/2026/qSEQ260107185.html)。

## PEPPOL 与互操作性

PEPPOL 可为互联的系统和平台提供传输及互操作能力。使用 PEPPOL 并不能替代法国强制制度下通过 PA 交换发票的要求。仅建立 PEPPOL 连接，并不足以证明已履行法国的发票交换和数据报告义务。

## 历史技术背景

以下六张图及 API 说明来自早期 PPF/PDP 资料，保留用于历史技术背景参考。其术语和架构已属旧版，不表示当前可以通过 PPF 交换强制制度下的 B2B 发票。实施集成前，请核对 PA 及公共服务的现行规范。

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="发票生命周期图，从供应商经 Submitted、Received by the platform 和 Made available 状态，到 Rejected、Refused、Disputed、Partially approved、In hand 和 Completed 等结果"><figcaption></figcaption></figure>

### 历史 API 服务模型

早期模型描述了通过合作伙伴组织已有 IT 工具使用相关功能的两种集成方式：

* **信息系统（IS）：** 将 API 集成到发票开具方、接收方或其无纸化处理运营商（OD）的系统中。部分 API 面向 PDP 系统，作为 EDI 集成之外的技术方式。
* **第三方软件：** 软件开发商可为客户系统添加通信层。早期资料中连接 PPF 的描述属于这一历史模型，并非当前的发票交换渠道。

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="显示 Issuer OD-PDP 和 Receiver OD-PDP 通过服务门户和第三方软件相连接的图，两者之间有一个数据控制与恢复步骤"><figcaption></figcaption></figure>

### 历史互联示意图

此图展示早期平台互联的背景。当前实施须符合 PA 要求；此处并未断言所有交换都必须使用同一种传输网络。

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="三个编号控制层的图：技术控制、应用控制以及功能与业务控制，每层都汇入后续的流程步骤"><figcaption></figcaption></figure>

### 历史枢纽连接模型

早期模型描述了一种 Web 或应用程序方案，由**枢纽代表客户发起 API 调用**。其中提到每个合作伙伴需要技术账户，而枢纽需要 PISTE 中的应用程序及 PPF 连接。这些是历史架构细节，并非已核实的现行集成步骤。

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="中心枢纽模型图，显示一个合作伙伴、一个技术账户、该枢纽、PISTE 下的一个应用程序以及一个连接"><figcaption></figcaption></figure>

### 历史参考资料

早期资料引用了[旧版时间安排及法律概述](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform)、[2022 年规范](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html)、[2025 年改革概述](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html)、[平台互联背景](https://nymus.be/fr/facturation-electronique-en-france/)、[PEPPOL 背景](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france)及[交换背景](https://nymus.be/fr/facturation-electronique-en-france/)。这些链接和其余图表均保留为历史背景。了解当前义务，以及 PA 发票交换与 PPF 公共职能之间的区别时，应以上述官方资料为准。早期资料对法国《2024 年财政法》第 91 条的引用，并不构成当前可通过 PPF 交换发票的依据。

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="EDI 流和 Flow 2 via API 接收图，先通过语义格式、目录和数据一致性的功能控制，然后并入开票数据，最后得到已提交的发票"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="EDI 流和 API 流先通过功能控制和特定业务规则，随后发票被拒绝或退回，或者被接收并可供使用的图"><figcaption></figcaption></figure></div>
