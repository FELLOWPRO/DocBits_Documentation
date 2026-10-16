---
description: 为某个文档类型单独复制现有自定义验证规则。
---

# 复制自定义验证规则

当某条规则适合作为起点，而你希望单独创建一个副本时，请使用 **Duplicate**。DocBits 会复制该规则的定义；新规则的名称和键由你选择。原规则仍会保留在列表中。

1. 前往 **Settings → Document Types**，打开要配置的文档类型，然后选择 **Custom Validation Rules**。页面会在规则卡片上方显示所选文档类型。有关此处其他可用设置，请参阅[文档类型](README.md)。
2. 找到源规则。如果列表较长，可使用搜索框或范围和状态筛选器。打开该规则的三点操作菜单，然后选择 **Duplicate**。系统默认规则和自定义规则都可以复制。
3. 在 **Rule Name** 中保留建议名称末尾的“Copy”，或输入更清晰的名称。系统会根据名称生成 **Rule Key**。如果需要自行编辑键，请选择铅笔图标。
4. 选择 **Duplicate** 创建单独的规则。保存后，DocBits 会刷新列表。选择 **Cancel** 可关闭对话框而不创建副本。

<figure><img src="../../../../.gitbook/assets/custom_validation_rule_duplicate_en.png" alt="英文“Duplicate Rule”对话框，包含 Rule Name、Rule Key、铅笔图标、Cancel 和 Duplicate 按钮"><figcaption><p>DocBits Sandbox 测试组织中的英文“Duplicate Rule”对话框。选择 Duplicate 前，可以更改复制规则的名称和键。</p></figcaption></figure>

**Duplicate** 按钮需要同时填写名称和键。如果保存失败，DocBits 会显示错误；请更正名称或键，然后重试。激活或更改新规则前，请先检查该规则，因为副本会沿用源规则的定义。
