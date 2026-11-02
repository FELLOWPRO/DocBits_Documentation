---
description: "P0：理解 Run Workflow、目标条件和错误"
---

# P0：理解 Run Workflow、目标条件和错误

**Run Workflow** 通过 ID 调用工作流，并等待其执行。名称不足以定位目标。设计器管理调用方的隐藏工作流 ID，不要将它作为业务参数修改。当前文档会传给目标，并重新求值目标入口和条件。

经检查的显式调用也可以到达**未启用**的目标。因此，未启用并不等于无法通过 Run Workflow 调用。Dev 测试覆盖了自有未启用训练目标、自我调用和未知目标 ID；后两者进入 Error。内置递归和调用链限制不能代替限制重复调用的业务规则。

应区分组织变量、文档字段与仅属于本次运行的返回数据。调用不会自动转发父运行的全部决策表或 HTTP 返回结果。应约定所需文档字段，并在下一张卡片中检查实际值。

调用显示绿色不代表目标的全部业务条件都满足：Advanced 目标只要没有技术错误，就可能被视为调用成功，其中也可能包含 `failed_condition`。应查看目标实际选择的路径和效果，并在调用方明确处理错误，避免 A→B→A 和重复调用同一目标。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `run_workflow` · v2

标识: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | 调用可能成功；仍须检查目标 |

## 验证依据与限制

所选卡片及节点结果已使用合成数据在 Advanced Test 中验证，响应位于练习包。文档操作经过模拟，不能据此证明已持久保存的文档运行或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
