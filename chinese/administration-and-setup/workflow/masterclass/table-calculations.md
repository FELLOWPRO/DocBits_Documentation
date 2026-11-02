---
description: "P1：计算表格列并检查正则依赖"
---

# P1：计算表格列并检查正则依赖

**Calculate Columns** 对同一行的两个列进行计算并写入结果列。**Calculate in / CALC_COLUMNS_REGEX** 额外对第三列应用正则条件。此处正则决定是否计算，不提取或替换文本。旧的正则替换说明不适用于这张卡片。

示例：`QTY=2`、`PRICE=10`，运算 `*`，结果 `TOTAL=20.0`。正则变体使用 `TYPE` 和模式 `^A$`。A 行会被计算。对不匹配的 B 行，经检查的代码写入空结果，已有 TOTAL 值不会自动保留。

算术辅助函数将数值结果舍入到四位小数。单个空操作数可能当作 0，两个空字符串返回空。使用 `+` 时，非数值文本可能被连接。在经检查的函数中，`10/0` 会产生错误。因此应预先校验数值和必填单元格，并配置错误路径。

保存完整的计算前后表：两条匹配行、一条不匹配正则的行、空输入、无效文本和除零。对 A→B 的依赖计算，明确连接卡片并检查 B 实际读取的更新值。比较每一行及原有其他列，不能只看文档状态。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `calc_columns` · v2

标识: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

标识: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
