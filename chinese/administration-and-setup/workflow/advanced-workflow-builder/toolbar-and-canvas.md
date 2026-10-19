# 工具栏和画布

## 视频: 构建器与画布

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/zh.vtt) · 1:35

<details>
<summary>文字稿</summary>

**一张发票，两条路径**

这是 DocBits 中真实的高级工作流界面。发票金额检查连接到两个操作。连接关系决定执行哪一个操作。本示例使用尚未保存的草稿和演示字段。

**配置金额检查**

打开添加菜单，选择 And，再选择文档字段条件。设置金额字段，选择大于，并输入一千。请使用文档配置中准确的字段键名。

**配置操作卡片**

添加两张 Then 卡片。两张卡片都设置演示字段 approval route。一张写入 Approval，另一张写入 Standard。这些值用于标记路径。生产工作流需要配置实际的业务操作。

**连接不同结果的输出**

将 Start 连接到条件的输入端。将蓝色成功输出连接到 Approval，将橙色条件不满足输出连接到 Standard。红色错误输出用于单独处理求值错误。仅移动卡片的位置不会建立执行路径。

**准备测试用例**

在工具栏中打开测试。选择测试文档，或以 JSON 格式输入完整的文档数据。分别检查大于、小于和等于一千的金额，以及缺失值。执行后，请检查各个节点的结果。

**验证、保存并检查启用状态**

验证连接和卡片设置。明确保存到服务器，然后单独检查工作流是否已启用。浏览器自动草稿不能代替保存。执行工作流和访问日志需要相应的模块及订阅。

</details>

[查看全部五个章节](videos.md)

高级工作流工具栏位于画布底部，提供构建、导航和管理流程所需的一切。

## 工具栏控件

- **+ Add** — 打开节点菜单以添加节点（参见[节点](nodes.md)）。
- **Undo / Redo** — 向后或向前逐步恢复或重做更改。
- **Zoom in / Zoom out** — 更改画布缩放级别。
- **Workflow name** — 在行内为工作流命名。
- **Edit description** — 为工作流添加描述。
- **Variables** — 打开[变量](variables.md)面板。
- **Help** — 打开键盘快捷键和帮助对话框。
- **Validate / Test** — 检查并运行流程（参见[验证和测试](validation-and-testing.md)）。
- **Snap to grid** — 切换节点是否吸附到网格，以便整齐布局。
- **Mini-map** — 切换小型概览地图，以便浏览大型图表。
- **Save** — 保存工作流。**auto-save** 指示器会显示流程最近一次自动保存的时间。

## 键盘快捷键

在画布上随时按 <kbd>?</kbd> 打开快捷键和帮助对话框。

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="键盘快捷键和帮助对话框"><figcaption><p>键盘快捷键和帮助对话框——快捷键、执行路径高亮和连接线颜色。</p></figcaption></figure>

| 快捷键 | 操作 |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | 保存工作流 |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | 验证工作流 |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | 测试工作流 |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | 撤销 / 重做 |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | 复制 / 粘贴 / 复制所选节点 |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | 选择所有节点 |
| <kbd>Shift</kbd> + 拖动 | 选择节点（拖动） |
| <kbd>Cmd/Ctrl</kbd> + 单击鼠标左键 | 将节点添加到选择中或从中移除 |
| 单击鼠标右键 | 打开添加节点菜单 |
| <kbd>Del</kbd> | 删除所选节点 |
| <kbd>?</kbd> | 显示此帮助 |

## 后续步骤

- 使用[节点](nodes.md)和[变量](variables.md)构建流程。
