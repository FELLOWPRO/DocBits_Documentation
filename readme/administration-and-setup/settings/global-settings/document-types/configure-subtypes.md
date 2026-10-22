# 配置子类型

当同一文档类型的发票需要不同的字段、不同的验证布局或专属处理脚本时，请使用文档子类型。当前测试环境的列表为空；以下步骤适用于已创建的子类型，并非截图中已经完成的配置。先[创建子类型](creating-a-new-sub-type.md)，然后打开 **Settings → Document Types**，选择文档类型，再打开 **Document Sub Types**（文档子类型）。在子类型行中，打开 **Actions**（三个点）。菜单提供 **Fields**、**Layout Builder** 和 **Scripts**；其中还包含[复制、编辑和删除](using-actions.md)。

<figure><img src="../../../../.gitbook/assets/site-complete-subtypes-overview-zh.png" alt="当前中文发票子类型列表为空，显示“未找到记录！”。下文介绍配置已有子类型的步骤，本图没有创建子类型或展示已完成的字段、布局或脚本配置。"><figcaption><p>当前中文发票子类型列表为空，显示“未找到记录！”。下文介绍配置已有子类型的步骤，本图没有创建子类型或展示已完成的字段、布局或脚本配置。</p></figcaption></figure>

## 字段

选择 **Fields**，以决定用户在此子类型中看到和填写哪些信息。你可以在分组中创建字段，将现有字段设为必填、只读或隐藏，也可以调整识别选项。更改完成后，选择 **Save Settings**。有关操作步骤，请参阅[添加和编辑字段](fields/adding-and-editing-fields.md)；有关列选项，请参阅[配置字段属性](fields/configuring-field-properties-1.md)；如果字段需要使用查找数据，请参阅[主数据设置](fields/master-data-settings.md)。

<!-- Obsolete illustration retired: Retire obsolete English configured-subtype result illustration. The current test list is empty; complete field/layout/script procedures remain without fabricating a configured subtype or editing organization data. -->

## 布局编辑器

选择 **Layout Builder**，以便在文档验证屏幕上排列分组和字段。左侧列出元素；右侧可上传示例文档以供预览。检查结果，布局就绪后选择 **Save**。[Layout Builder 指南](../../../setup/document-types/layout-builder.md)介绍了元素、文档预览以及如何保存布局。

<!-- Obsolete illustration retired: Retire obsolete English configured-subtype result illustration. The current test list is empty; complete field/layout/script procedures remain without fabricating a configured subtype or editing organization data. -->

## 脚本

选择 **Scripts**，查看此子类型的脚本。如果列表为空，请选择 **Create Script** 或 **New** 以开始创建。搜索功能以及 **All**、**Active** 和 **Inactive** 筛选器可帮助查找现有脚本。按照[创建和编辑脚本](script/creating-and-editing-scripts.md)中的说明创建脚本；在启用脚本进行处理之前，请先阅读[脚本激活与管理](script/script-activation-and-management.md)。

<!-- Obsolete illustration retired: Retire obsolete English configured-subtype result illustration. The current test list is empty; complete field/layout/script procedures remain without fabricating a configured subtype or editing organization data. -->
