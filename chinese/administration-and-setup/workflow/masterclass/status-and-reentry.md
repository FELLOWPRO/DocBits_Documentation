---
description: "P0：更改状态并限制重复执行"
---

# P0：更改状态并限制重复执行

**Change Status to** 用于更新文档状态。在版本 3 中，`trigger_docflow` 控制是否请求后续工作流处理。请明确设置它。参数缺失时，代码使用 `true`；版本 1/2 并不通过相同执行路径读取这个开关。应检查已保存的卡片版本。

先使用 `validated_pending_approval` 和 `trigger_docflow=false`。状态是技术选项，不能自行用 `pending_approval` 替代。Advanced Test 会模拟更新，既不能证明状态已经持久保存，也不能证明请求的后续运行已经处理。

有边界的业务流程应检查初始状态和处理标记，执行操作后进入下一状态。重复事件不应再次满足原始条件。但两个并发运行仍可能同时读取旧标记，因此任务和导出目标还需要额外的重复处理控制。

验收时比较第一次和第二次真实运行的文档状态、请求的后续处理，以及任务或目标记录数量。不要仅为实验而反复切换两个状态。更改状态不能代替尚未满足业务条件的审批。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `staus_change` · v3

标识: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | 已请求后续执行 ≠ 已完成后续执行 |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## 验证依据与限制

所选卡片及节点结果已使用合成数据在 Advanced Test 中验证，响应位于练习包。文档操作经过模拟，不能据此证明已持久保存的文档运行或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
