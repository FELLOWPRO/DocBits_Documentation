# 供应商门户

## 概述

本页介绍如何启用和使用**供应商门户**，以及如何找到所有相关设置。供应商门户允许您邀请供应商加入 **DocBits**。获得访问权限后，供应商可以直接在 **DocBits** 中登录并查看其**采购订单**和**发票**的状态。

## 如何启用供应商门户

1.  前往**设置 → 文档处理 → 模块 → 文档集成**。

    <figure><img src="../../../.gitbook/assets/site-complete-supplier-portal-module-zh.png" alt="当前中文“模块 → 文档集成 → 运输和供应商”中的供应商门户开关。只查看现有状态，没有切换模块、修改订阅或邀请供应商。"><figcaption><p>当前中文“模块 → 文档集成 → 运输和供应商”中的供应商门户开关。只查看现有状态，没有切换模块、修改订阅或邀请供应商。</p></figcaption></figure>
2.  在**运输和供应商**部分检查**供应商门户**。如需启用，由获准管理员核对订阅、组织和访问范围后操作；本次只查看已有状态。



## 供应商设置

启用**供应商门户**功能后，**设置**菜单底部会显示新的 **Supplier Settings** 部分。

<!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->

[**Supplier General Settings**](../../settings/supplier-setting/supplier-general-settings.md)：在这里，您可以上传公司徽标来自定义**供应商门户**。徽标会显示在所有电子邮件模板的页眉中。您还可以管理法律文件，例如使用条款和隐私政策。

[**Email Templates**](../../settings/supplier-setting/editing-email-templates.md)**：**在这里，您可以创建并测试要发送给受邀供应商的邀请邮件模板。

[**Supplier Layout**](../../settings/supplier-setting/supplier-layout.md)**：**在这里，您可以创建和管理布局，以定义新供应商在注册过程中必须提供哪些信息。

[**Export Configuration**](../../settings/supplier-setting/export-configuration-for-supplier-portal-for-m3.md)：在这里，您可以使用 ION 和 IDM 映射文件定义**供应商门户**与 **Infor M3** 系统之间的数据映射和同步方式。

[**Supplier Permissions**](../../settings/supplier-setting/supplier-permissions.md)：在这里，您可以配置供应商在**供应商门户**中的权限。您还可以对供应商进行分组，以便更轻松地管理多个供应商的访问权限和设置。

所有供应商设置的详细指南请参见[此处](../../settings/supplier-setting/)。

## 供应商仪表板 <a href="#supplier-permissions" id="supplier-permissions"></a>

您可以通过左侧菜单访问**供应商仪表板**，如下所示。

<figure><img src="../../../.gitbook/assets/site-complete-supplier-portal-overview-zh.png" alt="当前中文供应商仪表板及工具栏，所有供应商记录值已隐藏。显示所有供应商、待批准、等待注册以及刷新、列设置、分析和新增入口；没有创建、审批或修改供应商，也没有发送邀请。"><figcaption><p>当前中文供应商仪表板及工具栏，所有供应商记录值已隐藏。显示所有供应商、待批准、等待注册以及刷新、列设置、分析和新增入口；没有创建、审批或修改供应商，也没有发送邀请。</p></figcaption></figure>

这里会显示您创建的所有供应商。

## 筛选供应商

您可以按供应商**名称**或**编号**搜索，也可以使用高级筛选条件缩小结果范围：

* **供应商组**
* **状态**
* **创建时间**

您还可以指定每页显示的供应商数量。

<figure><img src="../../../.gitbook/assets/site-complete-supplier-portal-filters-zh.png" alt="当前中文供应商筛选菜单，包含供应商组（界面写作“供应商团体”）、状态、创建日期及每页数量。只打开菜单，没有应用或清除筛选。"><figcaption><p>当前中文供应商筛选菜单，包含供应商组（界面写作“供应商团体”）、状态、创建日期及每页数量。只打开菜单，没有应用或清除筛选。</p></figcaption></figure>

此外，您可以点击筛选栏左侧的相应类别，快速筛选**待审批**或**待注册**状态的供应商。



## 供应商详情（内部视图）

在**供应商仪表板**中点击供应商所在行，即可打开该供应商的**供应商详情**视图。此内部视图会显示供应商在注册过程中填写的相同六个部分——**供应商详情**、**地址数据**、**供应商联系人**、**供应商财务信息**、**供应商采购信息**和**供应商证书**——以及供应商当前的**状态**徽标。

您可以在此视图中查看供应商资料、更正或补充缺失信息，并为审批决策做准备。有关各部分的说明，请参见[供应商注册](supplier-registration.md)。点击视图顶部的返回按钮即可返回**供应商仪表板**。

## 供应商状态

如果您使用**供应商门户**，了解供应商可能处于的不同状态很重要。以下列出了所有可能的供应商状态及其含义：

* **未开放**：现有供应商，尚未收到门户邀请。
* **待注册**：供应商已收到邀请，但尚未完成注册流程。
* **待供应商补充信息**：注册已完成，但仍需供应商补充信息或进行更改。
* **待审批**：供应商已完成注册，正在等待首次审批。
* **待应付账款审批**：供应商已通过首次审批，正在等待第二次（应付账款）审批。
* **已批准**：供应商已完成流程并通过全部审批。
* **已拒绝**：供应商的注册或审批未获通过。

## 供应商仪表板中的工具

在搜索栏右侧，您会看到几个工具，可帮助您更高效地使用和管理仪表板。

### 刷新表格 <a href="#refresh-table" id="refresh-table"></a>



点击此按钮可刷新仪表板，加载最新的数据和状态。

### 设置表格列以便整理 <a href="#set-table-columns-for-organization" id="set-table-columns-for-organization"></a>

<figure><img src="../../../.gitbook/assets/site-complete-supplier-portal-columns-zh.png" alt="当前中文供应商列设置窗口。只查看可见／隐藏列和顺序配置，没有选择列、拖动或保存；此窗口控制供应商表格，不能据此推断采购订单表格已更改。"><figcaption><p>当前中文供应商列设置窗口。只查看可见／隐藏列和顺序配置，没有选择列、拖动或保存；此窗口控制供应商表格，不能据此推断采购订单表格已更改。</p></figcaption></figure>

点击列设置按钮，管理供应商表格中列的显示情况。使用复选框和箭头按钮可在显示和隐藏区域之间移动列。您还可以拖放列名称来调整列的顺序。按当前窗口的**完毕（Done）**保存更改；取消会放弃本次调整。相同显示名称可能对应不同列配置，修改前请核对目标列。



### 分析 <a href="#analytics" id="analytics"></a>

<!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->

若当前版本提供此分析按钮，可打开到期统计区域；请确认统计字段和时间范围，不要把历史截图中的数量当作当前数据。\
点击任意类别可应用筛选，仅查看符合条件的供应商。

<!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->

## 创建供应商并发送注册邮件

### **创建新供应商：**

1.  点击右上角的加号（+）图标。


2.  填写必填字段，然后点击 **Save**。

    <!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->
3. 根据实际邀请与邮件配置，系统可能发起注册邮件。保存供应商记录不等于邮件已经送达；请核对发送结果和收件地址，必要时按下述流程发送邀请。本文没有创建供应商或发送邮件。

### **向现有供应商发送注册邮件：**

1. 在**供应商仪表板**中找到该供应商。
2. 点击 **Actions** 列中的三点菜单。
3.  选择 **Magic Link**。

    <!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->
4. 核实供应商信息。
5.  点击 **Send**，通过电子邮件发送注册链接。

    <!-- Obsolete illustration retired: Retire legacy English supplier navigation, analytics or create/invitation result illustration. Current native module/list/filter/column context is shown; preserve complete conditional steps without opening row actions, creating suppliers or sending email. -->

## 供应商的注册流程是怎样的？

发送邀请邮件后，供应商必须完成注册流程才能访问**供应商门户**。

注册流程的详细分步指南请参见[此处](supplier-registration.md)。
