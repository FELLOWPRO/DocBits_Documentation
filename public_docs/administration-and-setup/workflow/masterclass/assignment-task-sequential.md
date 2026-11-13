---
description: "P1：区分文档分配、任务与顺序审批"
---

# P1：区分文档分配、任务与顺序审批

**文档分配**确定当前责任人，**任务**是独立的工作项，**通知**用于告知。这三者都不是某个人已经批准。分配给组也不能证明每个组成员都同意。

顺序卡片收集审批人和审批顺序。示例中 A 的顺序值为 10，B 为 20。经检查的收尾逻辑从较小值开始。转交给 B 依赖审批流程已处理的用户决定，设计器中的 Wait 节点继续执行不会自动完成这次交接。

若希望首先分配给顺序流程的第一个审批人，应避免同一次运行中的直接分配：文档已经直接分配后，收尾逻辑可能跳过首次顺序分配。任务的 `task_type`、优先级、接收人和 `send_email` 分别配置。训练练习应关闭邮件发送。

业务验收包括 A→批准→B→批准、A 拒绝、接收人缺失和重复触发。拒绝后不能执行最终导出，接收人无法解析也不能显示为审批完成。分别检查文档责任人与任务清单。设计器模拟不能证明真实用户交接。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4" %}

**视频:** 使用决策表的两步审批 · 2:43 · [字幕 (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.vtt)

<details>

<summary>文字稿</summary>

**两步，两个决策表** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=0.25)

两步审批：先是决策表返回的审批人，然后是始终排在最后的最终组。两个决策表，一个返回用户，另一个返回组。

**一条链：表、分配、表、分配** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=10.05)

把每张分配卡紧跟在它自己的决策表后面，连成一条链：决策表、分配、决策表、分配。两个决策表都保存返回的数据。

**每张分配卡紧跟它的表** · [0:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=22.883)

Workflow 只保留最后一个决策表结果。每张分配卡在运行时读取它，所以必须在下一个决策表替换它之前运行。

**优先级决定顺序** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=32.516)

审批顺序由优先级决定，而不是卡片的顺序：数字最小的先收到文档。把最高的数字给最终组。

**测试：先审批人，后组** · [0:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=42.45)

测试显示每张卡都成功。第一张分配卡把两位审批人排入队列，第二张把最终组排入队列。运行结束时，最后一次分配把文档交给其中第一位。

**并排：行不通** · [1:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=70.516)

这种布局行不通。并排的两条路径看起来一样，但 Workflow 会一步一步地运行：先运行两个决策表，再运行两张分配卡。

**审批人丢失，没有报错** · [1:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=81.383)

测试先运行两个决策表，再运行两张分配卡。两张卡都读取第二个表的结果：组被排入两次，审批人丢失了。每张卡仍显示成功，没有任何警告。请使用链。

**固定的最后审批人：优先级 99** · [1:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=111.516)

在标准 Workflow 中，固定审批人可以始终排在最后：先分配决策表的用户，再添加一张以高优先级（例如 99）分配一位用户的卡。

**表的优先级保持更低** · [2:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=123.483)

决策表的优先级必须低于这个数字。如果决策表没有找到任何人，Workflow 会停在决策表卡，不会分配给任何人。两者都返回的用户会被询问两次。

**在测试中检查** · [2:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/zh.mp4#t=135.116)

标准 Workflow 一次只能测试一张卡，所以请在 Advanced Workflow 中测试相同的卡。第一张分配卡把表中的审批人排入队列，第二张加入固定用户。优先级让他排在最后。

</details>

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
