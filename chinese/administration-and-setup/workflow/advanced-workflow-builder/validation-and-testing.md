# 验证与测试

## 视频: 变量、测试与激活

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.mp4) · [字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.vtt) · 1:50

<details>
<summary>文字稿</summary>

**选择变量类型**

点击花括号图标打开变量。选择文本、数字、是或否，或者文档，并按名称搜索。Document 变量存储由专用工作流动作设置的文档引用。此表单不接受文档值。

**变量属于整个组织**

设置唯一名称、类型和初始值。创建、修改或删除变量会立即保存到组织。其他工作流可以共用这些值。保存或放弃画布都无法撤销变量更改。

**先验证结构**

点击验证，查看画布上方的错误和警告。点击消息可以定位节点。检查动作、入口连接、输出、环路和合并节点。结构验证通过，并不代表运行时数据正确。

**选择测试上下文**

工具栏播放按钮打开测试文档选择器。选择文档、自定义数据，或对独立卡片选择无文档测试。Start 的播放按钮直接运行。测试使用当前画布，包括未保存的修改，并模拟破坏性动作。

**准备和检查测试场景**

分别准备用于大于、小于、等于一千以及缺少数据的测试。运行后，检查节点消息和耗时：绿色表示成功，橙色表示条件不成立，红色表示错误，灰色表示跳过。修正后重新测试。使用测试管理器重复运行测试场景。

**保存后再激活**

自动保存会在更改后约每三十秒保留本地浏览器草稿。请明确保存到服务器。首次保存前无法激活。在预期自动执行之前，检查工作流列表中的启用状态。

</details>

[查看全部五个章节](videos.md)

构建高级工作流时，工具栏中的两个控件可让你在构建器中直接检查工作流。它们用于*构建过程中的快速检查*；如需保存可重复运行的测试，请使用[Test Manager](../test-manager.md)。

## 验证

点击 **Validate** 控件（圆圈勾选图标，或按 <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>）。验证会检查流程图中的问题，例如未连接的节点、缺少配置和无效连接，并指出这些问题，方便你在工作流处理实际文档前进行修复。

## 测试

点击 **Test** 控件（播放图标，或按 <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>），即可使用样例运行当前流程并观察其行为，且不会影响实际文档。这是快速检查画布上刚完成的更改是否正常的方式。

## 何时使用哪种方式

- **在构建器中验证 / 测试**（本页）——设计流程时即时获得反馈。
- **[Test Manager](../test-manager.md)** ——保存测试场景，以便稍后重新运行，并与其他所有测试场景一起运行，从而在未来更改后发现回归问题。

## 后续步骤

- 在[节点](nodes.md)中查看节点类型和连接。
- 在[工具栏与画布](toolbar-and-canvas.md)中查看所有工具栏和画布控件。
