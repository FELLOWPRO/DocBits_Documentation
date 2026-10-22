---
description: "P1：明确容差参考侧与采购订单比较方向"
---

# P1：明确容差参考侧与采购订单比较方向

百分比容差取决于**参考侧**。经检查的 PO 卡片 v5 中，`document_po` 表示文档值相对于订单值比较，订单值为百分比基数。`po_document` 同时反转比较方向和基数。六种允许方向还包括已收货值。应明确选择方向、运算符和 Any/All。

示例：订单 100，文档 102.02，等于并允许 2% 容差。以订单为参考，范围为 98–102，文档值超出；以文档为参考，范围为 99.9796–104.0604，订单值 100 在范围内。文档值 102 恰好位于第一种方向包含的上界。绝对容差 2 则使用被比较值的单位。

卡片按价格单位归一化，并根据方向使用订单或收货数据。先检查匹配关系、数量和单位。Any 要求至少一个实际比较匹配，All 要求所有已执行比较都匹配。v5 中，**没有可比较行**是数据错误，并非自动满足 All。未匹配行必须单独统计。

对已有工作流，应重新读取保存的版本、方向和运算符，因为迁移曾修改这些设置。旧标签不足以完成验收。记录原值、参考侧、精确边界、最小超出量、舍入精度、订单缺失和未匹配行。本算例不能替代使用自身 PO 主数据的验收。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `condition_docfield_operator_docfield_tolerances` · v2

标识: `d0472648-d1a2-499d-83e3-b47306ae130a`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

标识: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | 数据错误 |
| PO-05 | unmatched_rows>0 | 另行核对匹配覆盖范围 |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
