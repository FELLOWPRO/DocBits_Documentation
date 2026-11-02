# 电子发票验证

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/en.mp4" %}

**电子发票验证**页面（**设置 → 电子文档 → 电子发票验证**，路径 `/settings/einvoice-validation`；早期名称为*验证规则*）用于控制 DocBits 如何验证收到的电子发票。它基于官方 **KoSIT XRechnung + ZUGFeRD** 规则集，以及验证器内部使用的发现代码，并允许你为组织覆盖每条规则的严重性。

> 此页面适用于**电子发票**（XRechnung、ZUGFeRD、Factur-X）。它与**数据验证规则**不同，后者用于检查提取的文档字段。

## 此页面包含的内容

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings.png" alt="电子发票验证页面，其中显示“按文档类型验证”表格"><figcaption><p>电子发票验证页面。“<strong>规则和策略</strong>”选项卡从<strong>按文档类型验证</strong>表格开始。示例组织。</p></figcaption></figure>

| 主题 | 功能 | 适用对象 |
| --- | --- | --- |
| [验证设置和接受的版本](validation-setup.md) | 设置向导、接受的 XRechnung 版本、接受的配置文件，以及每种严重性的含义。 | 组织管理员 |
| [规则严重性](validation-rule-severities.md) | 规则表：更改组织中每条规则的严重性。 | 组织管理员 |
| [按文档类型验证](validation-per-document-type.md) | 开启验证（**已启用**），并决定检查失败是否会阻止文档（**阻止**）。每次更改都需要确认。 | 组织管理员 |
| [更改日志](validation-change-log.md) | 每项设置更改的记录：时间、操作者、规则，以及从 → 到的变化。 | 组织管理员 |
| [被拒绝的电子发票错误页面](validation-error-screen.md) | 上传错误 XML 时显示的内容：说明、出错行和后续步骤。 | 所有处理发票的人员 |
| [验证报告](validation-report.md) | 发票验证失败时用户看到的内容：以通俗语言说明发现的问题。此报告从文档打开，而非从此页面打开。 | 所有处理发票的人员 |
| [后续步骤和拒绝文档](validation-next-step-and-reject.md) | 阅读报告后的操作、下载报告，以及**拒绝文档**。 | 所有处理发票的人员 |
