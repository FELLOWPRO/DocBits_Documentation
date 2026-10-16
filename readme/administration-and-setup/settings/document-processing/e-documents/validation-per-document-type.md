# 每种文档类型的验证

管理员可以针对每种文档类型，决定 DocBits 是否验证收到的电子发票，以及验证失败时是否阻止文档。每项更改都会经过确认并记录到[更改日志](validation-change-log.md)。

> 只有**组织管理员**可以更改这些设置。其他用户只能以只读方式查看此表，或者看不到此表。

## 表格

前往 **Settings → E-Documents → E-Invoice Validation**。**Rules and policy** 选项卡首先显示 **Validation for each document type** 表格。

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings.png" alt="显示“Validation for each document type”表格，以及“Enabled”和“Blocking”开关"><figcaption><p>每种文档类型对应一行，包含“Enabled”和“Blocking”开关。示例组织。</p></figcaption></figure>

| 开关 | 功能 |
| --- | --- |
| **Enabled** | DocBits 会验证此文档类型的每张收到的电子发票，并保存[验证报告](validation-report.md)。 |
| **Blocking** | 如果发现错误，则会停止处理该文档。文档状态会变为 **Error**。关闭此选项时，DocBits 会保存报告并继续处理文档。只有在 **Enabled** 已开启时，才能开启 **Blocking**。 |

如果某种文档类型设有子类型覆盖项，表格中会显示相关提示。

## 更改设置

1. 选择要更改的开关。
2. DocBits 会显示 **Confirm validation change**，其中包含文档类型和更改内容，例如 *QUOTE: Enabled → On*。

<figure><img src="../../../../.gitbook/assets/einvoice-validation-confirm.png" alt="“Confirm validation change”对话框"><figcaption><p>每项更改都需要确认</p></figcaption></figure>

3. 阅读提示：**已保存的报告不会更改。** 更改仅适用于新的验证，包括重新启动文档处理时执行的验证。
4. 选择 **Confirm change** 以确认，或选择 **Cancel** 保留原设置。

如果你没有相应权限，DocBits 会提示需要组织管理员，且不会进行任何更改。

## 相关页面

* [电子发票验证](validation-rules.md)
* [更改日志](validation-change-log.md)
* [验证设置与接受的版本](validation-setup.md)
* [验证报告](validation-report.md)
* [启用或停用电子发票验证](README.md#enable-or-disable-e-invoice-validation)
