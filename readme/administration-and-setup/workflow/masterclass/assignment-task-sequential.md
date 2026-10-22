---
description: "P1：区分文档分配、任务与顺序审批"
---

# P1：区分文档分配、任务与顺序审批

**文档分配**确定当前责任人，**任务**是独立的工作项，**通知**用于告知。这三者都不是某个人已经批准。分配给组也不能证明每个组成员都同意。

顺序卡片收集审批人和审批顺序。示例中 A 的顺序值为 10，B 为 20。经检查的收尾逻辑从较小值开始。转交给 B 依赖审批流程已处理的用户决定，设计器中的 Wait 节点继续执行不会自动完成这次交接。

若希望首先分配给顺序流程的第一个审批人，应避免同一次运行中的直接分配：文档已经直接分配后，收尾逻辑可能跳过首次顺序分配。任务的 `task_type`、优先级、接收人和 `send_email` 分别配置。训练练习应关闭邮件发送。

业务验收包括 A→批准→B→批准、A 拒绝、接收人缺失和重复触发。拒绝后不能执行最终导出，接收人无法解析也不能显示为审批完成。分别检查文档责任人与任务清单。设计器模拟不能证明真实用户交接。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `action_assign_doc_to_user_sequential` · v2

标识: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

标识: `548b3583-6a96-483f-8c66-7871d5b067fa`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → 批准 → B → 批准 |
| ASSIGN-02 | A → 拒绝 | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | 后备路径 |
| ASSIGN-04 | RUN-1 → RUN-2 | 检查重复处理 |
| ASSIGN-05 | direct + sequential | 检查首位接收人 |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
