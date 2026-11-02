---
description: "P1：选择导出方式、待办检查与最终状态"
---

# P1：选择导出方式、待办检查与最终状态

**Start Export** 使用已配置的导出路径。**Export with Export Configuration** 执行选定的配置。其延后变体把配置加入当前运行结束时的最终导出队列。入队不代表会在未来所有人工审批完成后自动发送。

经检查的新版本支持 `status=finished` 或 `status=exported`：finished 关闭文档，exported 允许继续编辑。Start Export 从 v4 提供此选择，指定配置导出及延后导出从 v3 提供。旧版本使用 finished。新版本缺少选择时，代码同样默认 finished；无效值则是配置错误。

设置 `ignore_pending_tasks=false` 会检查未完成任务。因此文档服务可能拒绝立即执行的指定配置导出。该卡片不能证明任务之后完成时会自动恢复导出。应定义新的运行事件，并在重新发送前检查目标是否已存在对应记录。忽略待办不能替代审批。

只有在明确验证审批条件之后才连接导出。验收包括未完成任务、任务完成、缺少批准、测试目标成功接收以及重复运行。区分请求导出、接收方收到和 ERP 已处理。练习包不包含真实导出目标，其测试不能证明送达。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `export` · v4

标识: `757f30ca-ed60-4e04-8131-2779df17f019`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

标识: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

标识: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| EXPORT-01 | status=finished | 已关闭 |
| EXPORT-02 | status=exported | 可继续编辑 |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | 可能拒绝；未证明会自动恢复 |
| EXPORT-04 | action_export_with_config_deferred | 已入队 ≠ 已收到 |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
