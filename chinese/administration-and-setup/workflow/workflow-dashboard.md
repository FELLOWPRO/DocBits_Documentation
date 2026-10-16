# 仪表板

**工作流仪表板**是工作流区域的主页。它展示工作流的运行情况，包括运行总数、成功率和失败率、随时间变化的运行次数图表以及近期活动，并提供访问工作流列表、测试管理器和 Card SDK 的入口。

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="工作流仪表板，显示运行总数、成功率和失败率、运行次数图表以及近期活动"><figcaption><p>工作流仪表板 — 每个工作流的运行总数、成功率和失败率以及近期活动。</p></figcaption></figure>

## 选项卡

* **Dashboard** — 运行指标和近期活动（如上所示）。
* **Workflow List** — 列出每个工作流及其类型、执行顺序和触发器。使用 **New Workflow** 创建新工作流。
* **Test Manager List** — 用于验证工作流的测试场景；使用 **Run All Tests** 运行这些场景。
* **License** — 工作流许可信息。
* **Card SDK** — 构建并上传自定义工作流卡片（参见 [Card SDK](card-sdk.md)）。

工具栏还提供 **Templates**，用于打开 [Workflow Templates](standard-workflow-builder/#workflow-templates) 库；以及 **Import Workflow**，用于从 JSON 文件导入工作流。

**Test Manager** 允许你为每个工作流保存测试场景并批量运行，从而确认更改后工作流仍能正常运行：

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="工作流测试管理器列表，显示测试场景和 Run All Tests"><figcaption><p>测试管理器列表 — 每个场景都会显示通过/失败结果；使用 <strong>Run All Tests</strong> 重新运行所有场景。</p></figcaption></figure>

## 后续步骤

* 使用 **Standard Workflow** 构建器构建线性自动化流程。
* 使用 **Advanced Workflow** 构建器构建分支流程。
