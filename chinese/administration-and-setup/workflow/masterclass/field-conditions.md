---
description: "P1：选择 Field is、Docfield is 或 Compare two Fields"
---

# P1：选择 Field is、Docfield is 或 Compare two Fields

使用 **Field is** 检查是否为空，使用 **Docfield is** 与配置值比较，使用 **Compare two Fields** 比较当前文档的两个字段。空值检查不能证明字段存在于布局中，也不能证明业务数据有效。

对 Field is v2，字段缺失、`null`、空字符串、只有空格的字符串以及布尔值 `false` 都属于空。数字 `0`、字符串 `"0"` 和字符串 `"false"` 不为空。这八种情况已使用完整文档数据在 Dev 中测试。若业务判断是勾选框的真或假，应使用明确的勾选框条件。

AMOUNT 字段中的 `"1000.01"` 与文本字段中相同字符不同。v2 练习包使用 AMOUNT，并在 JSON 中使用小数点。应同时核对技术字段键、布局和类型。本地化标签不是技术键，货币符号也不是数值。

使用 Compare two Fields 时，应配置左字段、运算符和右字段。检查类型兼容性及两个输入；缺失或不可比较的数据是数据错误，并非已经证明“不相等”。复测正例、反例、缺失输入和精确边界，记录字段值、类型与所选出口。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `condition_docfield_status` · v2

标识: `6f346541-faa0-42bd-b1a5-b23282157da1`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

标识: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

标识: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## 验证依据与限制

所选卡片及节点结果已使用合成数据在 Advanced Test 中验证，响应位于练习包。文档操作经过模拟，不能据此证明已持久保存的文档运行或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
