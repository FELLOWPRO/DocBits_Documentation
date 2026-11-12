---
description: "明确容差的参考侧与采购订单比较方向"
---

# 明确容差参考侧与采购订单比较方向

2% 的相对容差不是一个固定金额。它是您用来比较的那一侧的 2%，所以同一条发票行在一个方向上可能不通过，在另一个方向上却能通过。本页用一对数值说明这一点，给出三个可复现的练习，然后列出六种比较方向以及可以搬到您自己测试里的卡片参数。

请在您自己的测试组织里，用一份合成文档和一条已匹配的采购订单，在 Advanced Test 中完成这些练习。

## 参考侧就是基数

在所核查的采购订单卡片版本 5 中，`document_po` 用文档值去比订单值，因此订单是百分比容差的基数。`po_document` 则把比较和基数同时反过来。六种允许的方向还包括已收货一侧。请显式设置方向、运算符和 Any/All，而不要依赖已保存卡片里残留的内容。

## 练习 1：相同数值，两个方向

**目标：** 看清同样的数字如何得出两个不同结果。

1. 准备一条金额为 `100` 的已匹配订单，以及文档中 `102.02` 的单价。
2. 用运算符 `eq`、容差 `2`（相对容差 2%），先用 `document_po` 比较。预期 `false`：100 的 2% 是 2，闭区间因此是 98 到 102，而 102.02 高出 0.02。
3. 用 `po_document` 重复同一用例。预期 `true`：102.02 的 2% 是 2.0404，区间是 99.9796 到 104.0604，订单值 100 正好落在其中。

**完成标准：** 两个结果和两个区间都已记录，并且您能说出每个方向上的百分比是按哪个值算出来的。

绝对容差 `2` 的行为不同：它使用被比较值的单位，不会随参考值一起移动。

## 练习 2：找到精确边界

**目标：** 知道区间边缘是否算在内。

1. 保持 `document_po`、`eq` 和 2% 的相对容差，把文档值改成 `102`。
2. 运行该用例，然后用 `102.01` 再跑一次。

**完成标准：** `102` 返回 `true`，`102.01` 返回 `false`。边界是包含的：102 正好落在 98 到 102 区间的上边界上。

## 练习 3：Any、All 与被比较的行

**目标：** 知道卡片在多行时怎么处理，以及没有可比内容时会发生什么。

1. 用同一张已匹配订单配一份两行的文档：一行在容差内，一行在容差外。
2. 先用 `match_any` 运行卡片，再用 `match_all` 运行。
3. 运行一份完全没有可比行的文档。

**完成标准：** `match_any` 因那一行匹配而通过，`match_all` 只要有一个比较失败就失败，而没有可比行的文档返回数据错误。在版本 5 中这是一个错误，不是自动满足的 All。

## 哪一侧是基数？

| 已保存的选项 | 被比较的一侧 | 参考侧（百分比基数） |
| --- | --- | --- |
| `po_document` | 订单 | 文档 |
| `received_document` | 已收货数据 | 文档 |
| `po_received` | 订单 | 已收货数据 |
| `document_po` | 文档 | 订单 |
| `document_received` | 文档 | 已收货数据 |
| `received_po` | 已收货数据 | 订单 |

## 在信任现有 workflow 之前先核对

卡片会按价格单位归一化价格，并根据方向使用订单或收货数据，所以请先核对匹配关系、数量和单位。Any 需要一个匹配的比较，All 需要每一个实际执行的比较。未匹配的行要单独记录。

对现有 workflow，请重新读取已保存的版本、方向和运算符：迁移改动过比较设置，历史标签不足以作为验收证据。请记录数值与参考值、精确边界、最小超出量、舍入精度、订单缺失和未匹配行。这套计算不能替代使用您自己 PO 主数据的验收。

## 卡片与示例参数

这些值描述的是单张卡片的参数，而不是一份可导入的完整 workflow。请把 YOUR\_\* 替换为您自己的测试选择。隐藏的调用方 ID 由设计器管理。目录：Dev，DocFlow 2.10.38，2026 年 10 月 21 日；请在您自己的组织中确认可用版本与权限。

### `condition_docfield_operator_docfield_tolerances` · v2

标识：`d0472648-d1a2-499d-83e3-b47306ae130a`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

标识：`ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## 业务测试用例

| 用例 | 输入 / 设置 | 预期结果 |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | 数据错误 |
| PO-05 | unmatched\_rows>0 | 单独检查覆盖率 |

## 证据与边界

参数与行为已对照 Dev 目录和所核查的代码版本核对。业务测试用例是一套验收流程。本章没有进行个人审批、真实数据变更或交付。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
