# 基础设施

通过 **Infrastructure** 页面，管理员可以随时查看平台各部分运行在哪里（EU 或 US），以及处理是否正常。该页面为只读，因此这里不进行任何配置。

> **Access:** Infrastructure 是仅管理员可见的页面。打开 **Settings → Organization & Access → Infrastructure**。

页面有三个选项卡。每个选项卡在首次打开时加载数据，因此来回切换不会重新获取全部内容。

| Tab | Answers |
|-----|---------|
| **Topology** | 每个组件运行在哪里，文档如何流经 DocBits？ |
| **Processing** | 文档处理步骤是否在运行，工作是否在积压？ |
| **Scheduled Tasks** | 周期性后台任务是否按计划触发？ |

## Topology

**Topology** 默认打开。该视图以两种方式展示平台：**Architecture** 和 **Process**。使用图表上方的切换按钮在两者之间切换；旁边的指示器显示 **live** 时，表示视图正在流式传输其状态。

图表上方的横幅汇总区域检查结果：

* **Green**：所有组件都在您组织的区域内运行，横幅会指明该区域（例如 **EU**）。
* **Red**：标记为关键的组件在您组织的区域之外运行。
* **Amber**：提示会列出位于其他区域的组件，尽管整体检查通过。这属于区域差异，不是故障。

### 架构视图（Architecture）

架构视图把平台绘制成由组件卡片组成的泳道，例如 Edge / Web、Core API、Import、Background Services 和 Modules。箭头表示卡片之间的连接。

每张卡片显示组件名称、区域标记；对于关键组件，还会显示一个状态点，组件有响应时该点变为绿色，并在上报数值时显示以毫秒为单位的延迟。

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | 组件在您组织的区域内运行。 |
| **SHARED** | 诸如 CDN 之类的全局组件，没有单一区域。这属于正常情况。 |
| **EU ⓘ** / **US ⓘ** | 组件在其他区域运行，并作为提示上报。 |
| **EU ⚠** / **US ⚠** | 组件在其他区域运行，并作为错误上报。请向支持团队反映。 |
| 灰色标记、无符号 | 该组件的区域未知。 |

### 流程视图（Process）

流程视图会为一个文档在流水线中的流转制作动画：入口来源 **Email**、**FTP** 和 **Web** 汇聚到 **API**，然后经过 **OCR**、**Extraction**、**PO matching**、**Auto Accounting** 和 **Export**。每个阶段都连接到包含 **Postgres** 和文件存储的数据库条。说明文字标明当前正在动画展示的步骤，播放按钮可以暂停或继续动画。

PO matching 和 Auto Accounting 是可选的。当其中之一对您组织关闭时，相应阶段显示为灰色，动画会跳过它。

### 可选模块

可选模块（Full-Text Search、DocFlow、Auto-Accounting、DocNet 和 PO Matching）在其卡片上带有 **active** 或 **inactive** 标记。已停用的模块会提供一个 **Activate** 按钮，带您前往启用它的页面：大多数模块是 Modules 设置，PO Matching 则是 **Document Types**，因为它按文档类型启用。

## Processing

**Processing** 选项卡列出您组织的文档处理步骤，并说明工作是顺畅流转还是在积压。

| Column | Description |
|--------|-------------|
| **Process** | 处理步骤：Document Processing、OCR、TR-OCR、Barcode Split、Barcode Extraction、Extraction 和 PO Match。 |
| **Last run** | 该步骤上次运行距今多久。将鼠标悬停可查看确切时间戳。**Never run** 表示尚无文档到达该步骤。 |
| **Status** | 一个或多个标记（见下文）。 |

状态标记是彼此独立的信号：

* 红色标记 **Errors (N)**：最近有 `N` 个文档在该步骤失败。
* 带计数的琥珀色标记：当前有 `N` 个文档正由该步骤处理。
* 绿色标记 **OK**：没有近期错误，也没有待处理的工作。

由于错误和进行中的工作分开计数，一个步骤可以同时显示两者，因此当其他文档仍在运行时，故障依然可见。

## Scheduled Tasks

**Scheduled Tasks** 选项卡列出维持 DocBits 运行的周期性后台任务，例如缓存刷新、状态告警、文档超时和出站同步。每一行显示该任务是否按时触发。

| Column | Description |
|--------|-------------|
| **Task** | 计划任务的名称，其中分隔符已替换为空格。 |
| **Last run** | 上次运行距今多久。将鼠标悬停可查看确切时间戳。**Never run** 表示尚未触发。 |
| **Status** | 计划状态（见下文）。 |

| Status | Meaning |
|--------|---------|
| **On schedule**（绿色） | 任务按预期间隔运行。 |
| **Delayed**（红色） | 任务未在预期时间运行。请排查或向支持团队反映。 |
| **Unknown**（灰色） | 无法确定计划状态。 |

两个表格都有 **Refresh** 按钮，可按需重新加载当前数值。
