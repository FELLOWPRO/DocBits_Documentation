# 脚本编辑器中的 AI 助手

脚本编辑器内置了**人工智能助手**，可以为您编写并解释 DocBits 脚本。您只需用日常语言描述脚本应该做什么，助手就会给出可复制到编辑器中的 Python 代码。

{% hint style="info" %}
AI 助手属于 **DocNet**。您的组织需要有效的 DocNet 订阅才能使用它。请参见 [订阅计划](../../subscription-plan.md) 和 [模块](../../../document-processing/module/README.md)。
{% endhint %}

## 打开助手

1. 转到 **设置 → 文档类型**，打开相应的文档类型，然后点击 **脚本**。
2. 点击 **新的**，或将现有的脚本版本作为草稿打开。
3. 点击脚本名称旁边的机器人图标。**人工智能助手**面板会在编辑器右侧打开。

## 助手了解哪些信息

每次提问时，DocBits 都会向助手发送：

* **脚本参考**（即 [DocBits 中的脚本编写](scripting-in-docbits/README.md) 中介绍的函数），
* 脚本所属的**文档类型**，
* 编辑器中的**当前脚本**，
* 您的组织为该文档类型使用的**字段名称和表格列**。

由于有字段名称，助手会在 `get_field_value()` 和 `set_field_value()` 中使用您的真实字段，例如 `invoice_date` 或 `purchase_order`。

## 用助手编写脚本

1. 在面板底部的输入框中输入您的请求，例如：*如果币种为空，则将币种设置为 EUR。*
2. 按 **Enter** 键或点击发送图标。回答会以流式方式逐步显示。
3. 点击代码块旁边的复制图标（提示文字为 **抄送编辑**），即可将代码放入脚本编辑器。
4. 检查代码，为脚本命名，并将其保存为草稿。

后续提问可以在同一面板中继续。您可以粘贴错误信息，或者询问*为什么这个脚本没有设置到期日？*，助手会查看编辑器中的当前脚本。

## 务必检查结果

{% hint style="warning" %}
助手可能出错。请阅读生成的代码，确认字段名称与您的文档类型一致，并在启用脚本之前使用测试文档对其进行测试。请参见 [测试脚本](testing-scripts.md)。
{% endhint %}

脚本只能使用经批准的脚本函数运行。如果脚本调用了不存在的函数，DocBits 会拒绝它，并显示消息 *Unknown function*。

## 用量与限制

* 每个回答下方都会显示该回答所用的 token 数量（输入、输出和总计）。
* 用量会记录为您组织的 DocNet 用量。
* 如果缺少 DocNet 订阅（*DocNet subscription required*）、订阅已过期（*DocNet subscription expired*）或配额已用完（*DocNet quota exhausted*），DocBits 会拒绝该请求。

## 相关页面

* [创建和编辑脚本](creating-and-editing-scripts.md)
* [字段函数](scripting-in-docbits/field-functions.md)
* [示例脚本](scripting-in-docbits/sample-scripts/README.md)
* [启用和管理脚本](script-activation-and-management.md)
