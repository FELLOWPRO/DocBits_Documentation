# 审批历史

审批历史可帮助用户查看文档审批工作流中的决策。此页面的旧版本链接到了过时的 **General Settings** 路径，并展示了三张旧版界面的图片，却没有说明相关控件。请在当前文档类型设置中启用此选项，然后在您自己的组织中通过模拟审批验证结果。

## 为文档类型启用此选项

1. 使用管理员账户打开 **Settings → Document Types**。找到相应的文档类型，例如 **Invoice**，然后选择其**齿轮图标**以打开 **More Settings**。卡片上的 **Layouts** 和 **Fields** 链接会打开其他编辑器。

    <figure><img src="../../../../../../.gitbook/assets/dbdc163-document-types-en.png" alt="英文版 DocBits Document Types 页面，显示带有 More Settings 齿轮图标的 Invoice 卡片"><figcaption><p>在您想查看其审批工作流的文档类型上打开 More Settings。</p></figcaption></figure>
2. 展开 **Approval & Rejection**，找到 **Approval History**。此开关与 **Approve before export**、**Second Approval** 和 **Approval Stamp** 相互独立。英文 Sandbox 截图展示的是模拟组织 **DocBits Documentation Test A**，四个开关均为**关闭**。本指南未更改任何设置。

    <figure><img src="../../../../../../.gitbook/assets/dbdc222-approval-history-en.png" alt="英文版 Invoice More Settings 页面，已展开 Approval and Rejection，且 Approval History 处于关闭状态"><figcaption><p>检查所选文档类型的 Approval History 开关。</p></figcaption></figure>
3. 只有在确认预期的审批工作流以及谁可以查看其中的决策后，才启用 Approval History。记录启用前的设置，以便与测试结果进行比较。

## 使用测试文档验证

使用一个已配置类型的模拟文档，确保其确实进入审批工作流。让获授权的测试用户批准或拒绝该文档，然后打开文档的审批视图并检查可查看的历史记录。将决策、用户、时间和已填写的评论与您执行的操作进行核对。对于有多位审批人的工作流，请在每次决策后检查顺序。如果看不到历史记录，请先检查文档类型、工作流状态、开关和查看权限，再判断是否属于文档或产品错误。

由于 Test A 中没有可用的已批准或已拒绝文档，因此旧截图中的颜色和左上角导航不作为当前行为展示。两张新图片仅用于验证当前设置路径和开关；历史视图仍需使用有审批活动的模拟文档进行检查。
