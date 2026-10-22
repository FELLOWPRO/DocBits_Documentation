---
description: "下载合成发票、工作流 JSON、测试输入、预期结果及真实测试响应。"
---

# 工作流练习包

此包配合[高级案例](advanced-workflow-case-study.md)使用，包含合成发票、可导入的工作流、七份完整文档输入、独立预期结果及实际保存的测试响应。所有语言版本的技术键名和路径名称保持一致。

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
包含示例与结果的工作流练习包
{% endfile %}

## 内容与格式

| 文件 | 用途 |
| --- | --- |
| `training-invoice.pdf` | 合成发票：净额 1500 EUR，税额 285 EUR，总额 1785 EUR。不得付款。 |
| `advanced-workflow.json` | 通过 **Import Workflow** 在停用状态下导入；无全局变量，仅匹配发票类型和精确培训编号。 |
| `*-input.json` | 用于 **Advanced Test → Custom Data** 的完整文档数据。 |
| `expectations.json` | 预期路径、状态消息和整体结果；属于业务验收规范，并非 Test Manager 上传文件。 |
| `*-result.json` | 真实 Dev 测试响应及节点结果和消息；私有组织引用已替换。 |
| `prepare_inputs.py` | 替换两个必需位置上的合成组织引用。 |
| `verify_results.py` | 对照独立预期结果检查已保存的响应。需要 Python 3，无需访问密钥。 |

## 使用步骤

1. 解压 ZIP 并阅读附带说明。
2. 将工作流导入自己的测试组织，确认其已停用。
3. 获取自己的测试组织 ID，在本地运行：

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. 在 Advanced 测试对话框中使用 `prepared/` 内的文件。不要将合成文档 ID 换成正在处理的客户发票 ID。
5. 按[结果表](advanced-workflow-case-study.md)检查全部七个案例。不同金额是刻意设置的测试变体，不会修改附带发票。

数据包含 `id`、`org_id`、`doc_type`、`status`，以及带有 `layout.groups`、`fields` 和 `tables` 的 `extracted_data`。顶层与 `extracted_data` 内的组织引用都必须与登录账户匹配。若没有对应的布局定义，字段值可能无法被读取为已有文档字段。

## 练习范围

预期文件检查的不只是文档状态，还包括所选路径、路由文本、状态消息和完成节点。因此，它不同于已保存 Test Manager 场景中的状态比较。

Advanced 测试成功表示提供的测试数据得到了处理。模拟操作不等于实际分配、邮件发送或交付。启用前需要合适的事件入口及另行验证的真实执行。参阅[我的工作流何时运行？](workflow-execution-model.md)。

## WF-03: 练习与验收

解压 v2，用 prepare_inputs.py 调整组织并执行 verify_results.py。decision-table-setup.json 是搭建指引，acceptance-record-template.json 是记录模板，两者都不是工作流导入文件。导入前确认未启用状态。

[学习路径](workflow-learning-path.md)
