---
description: "P1：从决策表追踪到文档分配"
---

# P1：从决策表追踪到文档分配

决策表将输入字段映射为带类型的返回结果。示例使用 `cost_center=4711` 和 `total_amount`：不超过 1000 分给审批人 A，超过 1000 分给 B。应创建两条不重叠的规则，并使用测试组织中有效的用户。练习包中的示例文件说明配置思路，不保证可直接导入编辑器。

在 **Decision Table has Returns** v3 中，启用 `store_data=wf_store_data`。v2 则读取布尔保存选项。后续分配卡片需要同一次运行中保存的返回结果。决策表执行成功本身不能证明返回的是有效用户。

用户返回值可以包含 `output_type=user` 和 `value=101`；101 是合成 ID，必须替换为已存在的测试用户。然后选择 **Assign document based on decision table**，设置 `assignee_type=user`。经检查的该动作 v2 选择最后一个匹配返回项。多条匹配不等于自动要求全部用户审批。

测试单条匹配、无匹配、多条匹配、错误返回类型、无效用户 ID 和关闭保存。为无匹配及分配错误配置明确的后备路径。应定义顺序和命中策略，而不是将偶然的表格顺序作为业务规则。最终在文档上验收真实分配。

决策表条件会实际调用表格服务求值。测试模式并不保证完全没有副作用；仅使用自有测试数据，并检查涉及的操作。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4" %}

**视频:** 分配卡中的决策表 · 1:40 · [字幕 (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.vtt)

<details>

<summary>文字稿</summary>

**决策表分两步工作** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=0.25)

决策表决定由谁处理文档。在 Workflow 中，它们分两步工作。一张和卡运行决策表并保留其返回结果。然后卡使用这些返回结果来分配文档或创建任务。

**成功、失败条件或错误** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=13.816)

当决策表为文档返回至少一个匹配时，和卡成功。没有匹配时，它以失败条件结束并走橙色路径。没有选择决策表，或决策表无法运行时，它以错误结束。

**运行决策表并保存返回结果** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=27.15)

添加检查决策表是否有返回结果的和卡，并选择决策表。然后设置它保存返回的数据。否则后面的卡片就没有可用的数据。

**第一个用户获得文档** · [0:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=42.183)

在成功路径上，按第一个返回用户分配的然后卡会把文档交给决策表返回的第一个用户。每个返回的用户，包括第一个，都会收到一个任务或通知。为任务设置标题、描述和优先级，并选择是否同时发送电子邮件。返回结果中的组会被忽略。

**没有字段：全部来自决策表** · [1:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=66.416)

而按决策表把文档顺序分配给用户或组的卡片完全没有字段。它从决策表中获取用户和组，每个都带有决策表返回的优先级，或者默认值。运行结束时，优先级数字最小的条目获得文档，除非另一张卡片已经直接分配了它。

**哪张卡片适合哪项工作** · [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/zh.mp4#t=85.35)

简而言之：要把文档交给一个人并通知其他所有人，使用第一个用户卡。要让决策表决定一切（包括优先级），使用没有字段的顺序分配卡。只想创建任务时，使用针对决策表返回结果的任务卡。

</details>

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
