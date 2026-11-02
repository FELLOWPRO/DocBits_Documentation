---
description: "P1：从决策表追踪到文档分配"
---

# P1：从决策表追踪到文档分配

决策表将输入字段映射为带类型的返回结果。示例使用 `cost_center=4711` 和 `total_amount`：不超过 1000 分给审批人 A，超过 1000 分给 B。应创建两条不重叠的规则，并使用测试组织中有效的用户。练习包中的示例文件说明配置思路，不保证可直接导入编辑器。

在 **Decision Table has Returns** v3 中，启用 `store_data=wf_store_data`。v2 则读取布尔保存选项。后续分配卡片需要同一次运行中保存的返回结果。决策表执行成功本身不能证明返回的是有效用户。

用户返回值可以包含 `output_type=user` 和 `value=101`；101 是合成 ID，必须替换为已存在的测试用户。然后选择 **Assign document based on decision table**，设置 `assignee_type=user`。经检查的该动作 v2 选择最后一个匹配返回项。多条匹配不等于自动要求全部用户审批。

测试单条匹配、无匹配、多条匹配、错误返回类型、无效用户 ID 和关闭保存。为无匹配及分配错误配置明确的后备路径。应定义顺序和命中策略，而不是将偶然的表格顺序作为业务规则。最终在文档上验收真实分配。

决策表条件会实际调用表格服务求值。测试模式并不保证完全没有副作用；仅使用自有测试数据，并检查涉及的操作。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `condition_decision_tree_data` · v3

标识: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

标识: `699912a7-2369-47e0-9092-8d027e13752a`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | 无结果 / 无效用户 / 错误类型 | 后备路径 |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | 没有可供分配的已保存返回值 |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
