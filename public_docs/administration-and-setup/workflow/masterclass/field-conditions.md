---
description: "选择 Field is、Docfield is 或 Compare two Fields"
---

# 选择 Field is、Docfield is 或 Compare two Fields

在设计器里，三张条件卡片看起来很像，而它们的区别决定了一条规则究竟能识别出什么。本页帮您选出正确的那一张，然后用三个短练习展示每张卡片各自返回什么。做完之后，您就能分清"空"和数字 `0`、"假"和"缺失"，以及"条件未满足"和"出错"；技术上的 `null` 算作空，数字 `0` 不算。

请在您自己的测试组织里，用一份合成文档在 Advanced Test 中完成这些练习。这里不会碰到任何客户文档。

## 您需要哪张卡片？

| 如果您想检查…… | 使用 | 卡片与版本 |
| --- | --- | --- |
| 字段是否带有任何值 | **Field is** | `condition_docfield_status` v2 |
| 字段与您输入的某个值 | **Docfield is** | `condition_docfield_operator_value` v2 |
| 同一文档中的两个字段互相比较 | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

这三张都是条件卡片：它们只返回结果，不会改动文档。检查空状态既不能证明字段在布局中存在，也不能证明其内容在业务上有效。各卡片页面列出了全部设置：[Field is](../cards-overview/and/document-field/field-is.md)、[Docfield is](../cards-overview/and/document-field/docfield-is.md) 和 [Compare two Fields](../cards-overview/and/document-field/compare-two-fields.md)。

## 练习 1：弄清"空"到底指什么

**目标：** 知道 Field is 版本 2 把哪些值当作空。

1. 在测试组织里把 **Field is** 版本 2 加进一条规则，并选择布局中的一个文本字段。
2. 把字段状态设为 `field_empty`（Empty or missing）。
3. 用完整文档数据跑八个 Advanced Test 用例：字段缺失、`null`、空文本 `""`、只有空格 `" "`、布尔值 `false`、数字 `0`、文本 `"0"` 和文本 `"false"`。

**完成标准：** 前五个用例返回 `field_empty=success`，后三个返回 `field_empty=failed_condition`。这八个用例已在 Dev 中用完整文档数据验证过。

数字 `0`、文本 `"0"` 和文本 `"false"` 都是值，不是缺失。如果您的业务判断是"真"或"假"，请改用明确的复选框条件，而不是去检查字段是否为空。

## 练习 2：把字段与一个值比较

**目标：** 看清运算符和字段类型如何改变答案。

1. 选一个数值字段，例如 `total_amount`，运算符 `gt`，值 `1000`。
2. 测试 `1000`、`1000.01`、字段缺失和一个无效值。

**完成标准：** `1000` 返回 `failed_condition`（因为 `gt` 表示严格大于），`1000.01` 返回 `success`，缺失或无效输入返回 `error`。

## 练习 3：比较两个字段

**目标：** 知道什么时候两个值会被比较，什么时候卡片根本无法比较它们。

1. 设置左侧字段、运算符和右侧字段。请使用类型相容的两个字段。
2. 测试取值相同、取值不同，以及输入缺失三种情况。

**完成标准：** 取值相同时满足 `eq`，取值不同时返回 `failed_condition`，输入缺失时返回 `error`，而不是给出一个已证明的"不相等"。

## 三种结果分别意味着什么

| 结果 | 它告诉您什么 |
| --- | --- |
| `success` | 卡片比较了这些值，且条件满足。 |
| `failed_condition` | 卡片比较了这些值，但条件未满足。在空状态检查中，`0` 和 `"0"` 会落到这里。 |
| `error` | 卡片无法比较，例如某个值缺失或无效。出错与"不相等"不是同一个答案。 |

## 类型是比较的一部分

AMOUNT 字段里的 `"1000.01"` 与文本字段里同样的字符并不等同。v2 练习包在 JSON 中使用 AMOUNT 和小数点。请把字段技术键、布局和类型放在一起核对。翻译后的显示名称不是技术键，货币符号也不是数值。

## 卡片与示例参数

这些值描述的是单张卡片的参数，而不是一份可导入的完整 workflow。请把 YOUR\_\* 替换为您自己的测试选择。隐藏的调用方 ID 由设计器管理。目录：Dev，DocFlow 2.10.38，2026 年 10 月 21 日；请在您自己的组织中确认可用版本与权限。

### `condition_docfield_status` · v2

标识：`6f346541-faa0-42bd-b1a5-b23282157da1`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

标识：`1c35a5a0-1592-446c-9a61-6abb14d27450`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

标识：`3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## 业务测试用例

| 用例 | 输入 / 设置 | 预期结果 |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## 证据与边界

部分卡片与节点结果已在 Advanced Test 中用合成数据核对过，答案放在练习包里。文档动作是模拟的；这些测试既不能证明一次已保存的文档运行，也不能证明对外发送。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
