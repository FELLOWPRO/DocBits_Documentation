---
description: "您的流程，您的逻辑，清晰连接。"
---

# DocBits Advanced Workflow

使用互相连接的卡片构建文档工作流。根据条件选择路径，汇合结果，并为错误设置独立路径，同时掌握整个流程。

## 观看功能概览

{% embed url="https://docbits-videos.fra1.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/zh.mp4" %}

[带字幕的播放器](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/zh.html) · [字幕](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/zh.vtt) · [画面文字](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/zh.txt) · 1:48 · Full HD

## 从发票到下一步操作

示例从收到一张发票开始。总金额大于 1,000 时进入 Approval 路径；小于或等于 1,000 时进入 Standard 路径。随后，视频展示 DocBits 设计器中使用 1,500 和 500 执行的真实测试及其结果。

## 三种流程控制方式

| 功能 | 实际用法 |
| --- | --- |
| **选择路径** | 将 Start 或 When 连接到条件。Success、Failed Condition 和 Error 分别使用不同的输出。 |
| **汇合连接的结果** | Wait ANY 需要至少一个匹配的已连接来源。Wait ALL 需要每个来源都产生与连接相匹配的结果。两者都不会取消其他操作。 |
| **连接下一步操作** | 使用错误路径、Call API 和注释连接系统并说明设计。注释本身不执行操作。 |

## 构建自己的工作流

<a href="../administration-and-setup/workflow/advanced-workflow-builder/README.md" class="button primary">打开 Advanced Workflow 配置指南</a>

[与 DocBits 讨论您的流程](https://docbits.com/en/book-demo/)

{% hint style="info" %}
视频结合了动画卡片和英文 Dev 界面的真实录屏，包含音乐和中文画面文字，没有旁白。测试操作将示例字段 `approval_route` 设置为 `Approval` 或 `Standard`；完整的人工审批流程需要单独配置业务操作。本演示未保存或激活。 汇合节点动画展示的是结果要求，而非执行时序。请测试节点可达性及完整的文档运行；仅通过局部测试不能证明生产流程能够完成。
{% endhint %}
