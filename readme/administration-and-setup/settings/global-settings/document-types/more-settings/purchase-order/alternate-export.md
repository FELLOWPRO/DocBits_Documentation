# 备用导出

## 概述

当文档处于特定状态时，您可以配置一个备用导出选项，使其显示在采购订单部分的导出下拉菜单中。\
本页介绍如何设置此选项。

## 激活步骤

1. 前往 **Settings** -> **Global Settings** -> **Document Types**
2.  选择所需的文档类型，然后点击 **More Settings**。

    <figure><img src="../../../../../../.gitbook/assets/po_settings_1.png" alt="文档类型列表，包含Invoice、Credit Note、Delivery Note和Order Confirmation行及其Activate开关"><figcaption></figcaption></figure>
3.  在 **Purchase Order** 部分中，找到 **Alternate Export** 选项。

    <figure><img src="../../../../../../.gitbook/assets/po_settings_alternate_export_1 (1).png" alt="Purchase Order 部分的 More Settings 面板，Alternate Export 选项位于 PO Tolerance Setting 和 PO disable statuses 之间"><figcaption></figcaption></figure>

## 设置方法

启用该设置后，您可以选择一种文档状态，并指定预定义的导出配置。

有关设置导出配置的更多信息，请参阅[此处](../../../../document-processing/export/)。

您可以选择以下状态：

* Classified（已分类）
* Pending confirmation（待确认）
* Pending approval（待审批）
* Pending second approval（待二次审批）
* Validated, pending export（已验证，待导出）
* Approved pending export（已批准，待导出）
* Rejected（已拒绝）
* Exported（已导出）
* On hold（暂停）
* Workflow（工作流）
* Error（错误）
* In Review（审核中）

设置完成后，采购订单匹配导出选项中会显示一个额外的导出选项。当文档符合指定状态时，此选项将使用指定的导出配置。

<figure><img src="../../../../../../.gitbook/assets/po_settings_alternate_export_2.png" alt="Purchase Order Matching 界面，Export 下拉菜单展开，显示 Alternate Export、Reject 和 Auto Export 选项"><figcaption></figcaption></figure>
